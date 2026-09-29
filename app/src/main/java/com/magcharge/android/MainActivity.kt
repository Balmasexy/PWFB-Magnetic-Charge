package com.magcharge.android

import android.Manifest
import android.annotation.SuppressLint
import android.bluetooth.BluetoothDevice
import android.bluetooth.BluetoothManager
import android.bluetooth.le.*
import android.content.*
import android.os.*
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewmodel.compose.viewModel
import java.util.UUID
import kotlin.math.abs

private val SERVICE_UUID = UUID.fromString("7f2a0001-6b2d-4b8e-9b7a-4c6c2f000001")
private val STATUS_UUID = UUID.fromString("7f2a0002-6b2d-4b8e-9b7a-4c6c2f000002")

data class BatteryUi(val level: Int = 0, val charging: Boolean = false, val wireless: Boolean = false, val temp: Float? = null, val voltage: Float? = null, val current: Int? = null)
data class ChargerUi(val device: BluetoothDevice, val rssi: Int)

class MagViewModel : ViewModel() {
    var battery by mutableStateOf(BatteryUi()); private set
    var chargers by mutableStateOf(listOf<ChargerUi>()); private set
    var scanning by mutableStateOf(false); private set
    var connected by mutableStateOf<String?>(null); private set
    var message by mutableStateOf("Ready"); private set
    private var scanner: BluetoothLeScanner? = null
    private var scanCallback: ScanCallback? = null
    private var gatt: android.bluetooth.BluetoothGatt? = null

    fun updateBattery(context: Context, intent: Intent?) {
        if (intent == null) return
        val level = intent.getIntExtra(android.os.BatteryManager.EXTRA_LEVEL, 0)
        val scale = intent.getIntExtra(android.os.BatteryManager.EXTRA_SCALE, 100).coerceAtLeast(1)
        val status = intent.getIntExtra(android.os.BatteryManager.EXTRA_STATUS, 0)
        val plugged = intent.getIntExtra(android.os.BatteryManager.EXTRA_PLUGGED, 0)
        val t = intent.getIntExtra(android.os.BatteryManager.EXTRA_TEMPERATURE, Int.MIN_VALUE)
        val v = intent.getIntExtra(android.os.BatteryManager.EXTRA_VOLTAGE, 0)
        val batteryManager = context.getSystemService(Context.BATTERY_SERVICE) as? android.os.BatteryManager
        val c = batteryManager?.getIntProperty(android.os.BatteryManager.BATTERY_PROPERTY_CURRENT_NOW)
            ?: Int.MIN_VALUE
        battery = BatteryUi(
            level = (level * 100 / scale).coerceIn(0, 100),
            charging = status == android.os.BatteryManager.BATTERY_STATUS_CHARGING || status == android.os.BatteryManager.BATTERY_STATUS_FULL,
            wireless = plugged == android.os.BatteryManager.BATTERY_PLUGGED_WIRELESS,
            temp = t.takeIf { it != Int.MIN_VALUE }?.div(10f),
            voltage = v.takeIf { it > 0 }?.div(1000f),
            current = c.takeIf { it != Int.MIN_VALUE && it != 0 }?.let { abs(it) / 1000 }
        )
    }

    @SuppressLint("MissingPermission")
    fun scan(context: Context) {
        val adapter = context.getSystemService(BluetoothManager::class.java)?.adapter
        if (adapter == null || !adapter.isEnabled) { message = "Turn on Bluetooth"; return }
        scanner = adapter.bluetoothLeScanner
        chargers = emptyList(); scanning = true; message = "Scanning for MagCharge chargers..."
        scanCallback = object : ScanCallback() {
            override fun onScanResult(type: Int, result: ScanResult) {
                val name = result.device.name ?: return
                if (!name.contains("MagCharge", true)) return
                chargers = (chargers + ChargerUi(result.device, result.rssi)).distinctBy { it.device.address }
            }
            override fun onScanFailed(code: Int) { scanning = false; message = "BLE scan failed: $code" }
        }
        val filter = ScanFilter.Builder().setServiceUuid(android.os.ParcelUuid(SERVICE_UUID)).build()
        scanner?.startScan(listOf(filter), ScanSettings.Builder().setScanMode(ScanSettings.SCAN_MODE_LOW_LATENCY).build(), scanCallback)
        Handler(Looper.getMainLooper()).postDelayed({ stopScan() }, 10_000)
    }

    @SuppressLint("MissingPermission")
    fun stopScan() {
        scanCallback?.let { scanner?.stopScan(it) }
        scanCallback = null; scanning = false
        if (message.startsWith("Scanning")) message = "Scan complete"
    }

    @SuppressLint("MissingPermission")
    fun connect(context: Context, item: ChargerUi) {
        stopScan(); message = "Connecting..."
        gatt?.close()
        gatt = item.device.connectGatt(context, false, object : android.bluetooth.BluetoothGattCallback() {
            override fun onConnectionStateChange(g: android.bluetooth.BluetoothGatt, status: Int, newState: Int) {
                if (newState == android.bluetooth.BluetoothProfile.STATE_CONNECTED) {
                    connected = item.device.name ?: "MagCharge"; message = "Connected"; g.discoverServices()
                } else if (newState == android.bluetooth.BluetoothProfile.STATE_DISCONNECTED) {
                    connected = null; message = "Disconnected"; g.close()
                }
            }
            override fun onServicesDiscovered(g: android.bluetooth.BluetoothGatt, status: Int) {
                if (status == android.bluetooth.BluetoothGatt.GATT_SUCCESS) message = "Connected • telemetry ready"
            }
        })
    }

    override fun onCleared() { gatt?.close(); super.onCleared() }
}

class MainActivity : ComponentActivity() {
    private val permissionLauncher = registerForActivityResult(ActivityResultContracts.RequestMultiplePermissions()) { }
    private val batteryFilter = IntentFilter(Intent.ACTION_BATTERY_CHANGED)
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val initial = registerReceiver(null, batteryFilter)
        setContent {
            val context = this@MainActivity
            val vm: MagViewModel = viewModel()
            LaunchedEffect(Unit) { vm.updateBattery(context, initial) }
            DisposableEffect(Unit) {
                val r = object : BroadcastReceiver() { override fun onReceive(c: Context?, i: Intent?) { vm.updateBattery(context, i) } }
                registerReceiver(r, batteryFilter)
                onDispose { unregisterReceiver(r) }
            }
            MagTheme { Screen(vm) }
        }
    }
    fun requestBluetooth() {
        if (Build.VERSION.SDK_INT >= 31) permissionLauncher.launch(arrayOf(Manifest.permission.BLUETOOTH_SCAN, Manifest.permission.BLUETOOTH_CONNECT))
        else permissionLauncher.launch(arrayOf(Manifest.permission.BLUETOOTH, Manifest.permission.BLUETOOTH_ADMIN))
    }
}

@Composable
fun Screen(vm: MagViewModel) {
    val context = androidx.compose.ui.platform.LocalContext.current
    val activity = context as? MainActivity
    Column(Modifier.fillMaxSize().padding(18.dp)) {
        Text("MAGCHARGE", style = MaterialTheme.typography.headlineMedium)
        Text("Android magnetic charging companion")
        Spacer(Modifier.height(20.dp))
        Card(Modifier.fillMaxWidth(), shape = RoundedCornerShape(22.dp)) {
            Column(Modifier.padding(20.dp), horizontalAlignment = Alignment.CenterHorizontally) {
                Box(Modifier.size(150.dp), contentAlignment = Alignment.Center) {
                    Surface(Modifier.fillMaxSize(), CircleShape, color = MaterialTheme.colorScheme.primaryContainer) {}
                    Column(horizontalAlignment = Alignment.CenterHorizontally) {
                        Text("⚡", style = MaterialTheme.typography.headlineLarge)
                        Text("${vm.battery.level}%", style = MaterialTheme.typography.displaySmall)
                        Text(if (vm.battery.charging) "CHARGING" else "NOT CHARGING")
                    }
                }
                Spacer(Modifier.height(10.dp))
                Text(if (vm.battery.wireless) "Wireless charging detected" else "Wireless charging not detected")
            }
        }
        Spacer(Modifier.height(14.dp))
        Card(Modifier.fillMaxWidth()) {
            Column(Modifier.padding(16.dp)) {
                Metric("Temperature", vm.battery.temp?.let { "%.1f °C".format(it) } ?: "Unavailable")
                Metric("Voltage", vm.battery.voltage?.let { "%.2f V".format(it) } ?: "Unavailable")
                Metric("Current", vm.battery.current?.let { "$it mA" } ?: "Unavailable")
            }
        }
        Spacer(Modifier.height(14.dp))
        Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
            Button(onClick = { activity?.requestBluetooth() }) { Text("Allow Bluetooth") }
            Button(enabled = !vm.scanning, onClick = { vm.scan(context) }) { Text(if (vm.scanning) "Scanning..." else "Find Charger") }
        }
        Spacer(Modifier.height(8.dp))
        Text(vm.connected?.let { "Connected: $it" } ?: vm.message)
        Spacer(Modifier.height(8.dp))
        LazyColumn(Modifier.fillMaxWidth()) {
            items(vm.chargers) { item ->
                Card(Modifier.fillMaxWidth().padding(vertical = 4.dp)) {
                    Row(Modifier.fillMaxWidth().padding(12.dp), horizontalArrangement = Arrangement.SpaceBetween, verticalAlignment = Alignment.CenterVertically) {
                        Column(Modifier.weight(1f)) { Text(item.device.name ?: "MagCharge"); Text("${item.rssi} dBm") }
                        Button(onClick = { vm.connect(context, item) }) { Text("Connect") }
                    }
                }
            }
        }
    }
}

@Composable fun Metric(label: String, value: String) { Row(Modifier.fillMaxWidth().padding(vertical = 4.dp), horizontalArrangement = Arrangement.SpaceBetween) { Text(label); Text(value) } }
@Composable fun MagTheme(content: @Composable () -> Unit) { MaterialTheme(colorScheme = lightColorScheme(primary = androidx.compose.ui.graphics.Color(0xFF1B7F4B), secondary = androidx.compose.ui.graphics.Color(0xFFF28C28)), content = content) }
