# MagCharge Universal Receiver V1 — KiCad Schematic Source

## Engineering Status

PRELIMINARY ENGINEERING SOURCE — NOT FABRICATION READY

This source is aligned with the verified BQ51013C engineering
netlist and BOM.

The native KiCad schematic must be cross-checked against the
current Texas Instruments BQ51013C datasheet before fabrication.

---

## Main IC

U1:
Texas Instruments BQ51013CRHLR

Package:
VQFN20 / RHL

Function:
- Qi wireless power receiver
- Internal rectification
- 5 V regulated output
- Foreign object detection
- Current limiting
- Thermal/temperature control

---

## Receiver Coil

L1:
Würth Elektronik 760308103215

Nominal inductance:
14.3 uH

Dimensions:
48 mm x 32 mm

Connections:
- L1-A -> AC1 / resonant network
- L1-B -> AC2 / resonant network

Final characterization required:
- Ls'
- Ls
- DC resistance
- Q
- resonance
- efficiency
- final mechanical/ferrite stack

---

## Resonant Network

C_RX1:
Series resonant capacitor (Cs)

Connection:
Receiver coil / AC input series resonance

Value:
TBD after Ls' measurement

Voltage:
25 V minimum

C_RX2:
Parallel resonant capacitor (Cd)

Connection:
AC1/AC2 receiver network

Value:
TBD after Ls measurement

Voltage:
25 V minimum

Do NOT finalize C_RX1 or C_RX2 from nominal coil inductance alone.

---

## BQ51013C Pin Mapping

| Pin | Function | Net |
|---:|---|---|
| 1 | PGND | PGND |
| 2 | AC1 | AC1 |
| 3 | BOOT1 | BOOT1 |
| 4 | OUT | +5V_RX |
| 5 | CLAMP1 | CLAMP1 |
| 6 | COMM1 | COMM1 |
| 7 | CHG | CHG_STATUS |
| 8 | AD-EN | NC / floating |
| 9 | AD | PGND |
| 10 | EN1 | EN1 |
| 11 | EN2 | EN2 |
| 12 | ILIM | ILIM |
| 13 | TS/CTRL | TS_CTRL |
| 14 | FOD | FOD |
| 15 | COMM2 | COMM2 |
| 16 | CLAMP2 | CLAMP2 |
| 17 | BOOT2 | BOOT2 |
| 18 | RECT | RECT |
| 19 | AC2 | AC2 |
| 20 | PGND | PGND |
| EP | Exposed pad | PGND |

---

## BOOT Capacitors

C_BOOT1:
10 nF minimum 25 V

BOOT1 -> C_BOOT1 -> AC1

C_BOOT2:
10 nF minimum 25 V

BOOT2 -> C_BOOT2 -> AC2

---

## COMM Capacitors

C_COMM1:
22 nF minimum 25 V

COMM1 -> C_COMM1 -> AC1

C_COMM2:
22 nF minimum 25 V

COMM2 -> C_COMM2 -> AC2

---

## CLAMP Capacitors

C_CLAMP1:
0.47 uF minimum 25 V

CLAMP1 -> C_CLAMP1 -> AC1

C_CLAMP2:
0.47 uF minimum 25 V

CLAMP2 -> C_CLAMP2 -> AC2

---

## RECT Supply

U1 pin 18 -> RECT

C_RECT1:
10 uF, 16 V minimum

C_RECT2:
10 uF, 16 V minimum

C_RECT3:
0.1 uF, 16 V minimum

All RECT capacitors:
RECT -> capacitor -> PGND

---

## Output

U1 pin 4 -> +5V_RX

C_OUT1:
10 uF

C_OUT2:
0.1 uF

Both:
+5V_RX -> capacitor -> PGND

Target V1 output:
5 V nominal

Target maximum:
1 A reference design

---

## FOD / ILIM Calibration Network

FOD node:
U1 pin 14

R_OS:
RECT -> R_OS -> FOD

Starting/reference:
20 kOhm

R_FOD:
FOD -> R_FOD -> PGND

Starting/reference:
196 Ohm

R1:
ILIM -> R1 -> FOD

Starting/reference:
66 Ohm

ILIM:
U1 pin 12 -> R1 -> FOD -> R_FOD -> PGND

Therefore:

RILIM = R1 + R_FOD

RILIM = 66 Ohm + 196 Ohm
RILIM = 262 Ohm

Reference IMAX:
1 A

Reference hardware current limit:
1.2 A

Final R_OS, R_FOD and R1 values require receiver characterization
and FOD calibration.

Provide calibration footprint flexibility for R_OS and R_FOD.

---

## TS / CTRL

U1 pin 13 -> TS_CTRL

Production:
characterized NTC to PGND.

Prototype:
10 kOhm test resistor may be used only for controlled testing.

Final NTC value and thermal thresholds require validation.

---

## EN1 / EN2

EN1:
U1 pin 10 -> LOW / floating

EN2:
U1 pin 11 -> LOW / floating

Normal wireless-enabled V1 state:

EN1 = LOW
EN2 = LOW

The BQ51013C contains internal pulldowns on EN1 and EN2.

No external controller is required for the normal enabled state.

Future system-control implementation may drive these pins LOW.

---

## AD / AD-EN

AD:
U1 pin 9 -> PGND

AD-EN:
U1 pin 8 -> NC / floating

This is the wireless-only V1 configuration.

---

## CHG

U1 pin 7:
CHG_STATUS

Open-drain charging-status output.

Prototype indicator circuitry may be added during implementation,
but it must not interfere with the receiver operation.

---

## USB-C Output

J1:
USB-C male / short flex-tail output

+5V_RX -> protected USB-C VBUS

PGND -> USB-C GND

V1 target:
5 V nominal
up to 1 A

No USB Power Delivery.

USB-C source-role CC implementation must be reviewed against the
final connector and applicable USB-C requirements.

---

## Protection

Include:

ESD protection:
ESD1

Output/current protection:
FUSE1

Protection components must be selected and validated for the
5 V / 1 A V1 output.

Protection must operate independently of:
- Android application
- BLE
- cloud services
- phone software

---

## Mechanical Stack

RX coil:
Würth 760308103215

Ferrite shield:
SH1

Magnetic alignment ring:
MR1

The final resonant values and efficiency must be validated with the
complete mechanical stack installed.

---

## KiCad Implementation Requirements

The native schematic must contain:

- U1 BQ51013CRHLR
- L1 receiver coil
- C_RX1
- C_RX2
- C_BOOT1
- C_BOOT2
- C_COMM1
- C_COMM2
- C_CLAMP1
- C_CLAMP2
- C_RECT1
- C_RECT2
- C_RECT3
- C_OUT1
- C_OUT2
- R1
- R_FOD
- R_OS
- NTC1
- J1 USB-C
- ESD1
- FUSE1
- required test points
- PGND
- +5V_RX
- RECT
- FOD
- ILIM
- TS_CTRL
- EN1
- EN2
- CHG_STATUS

---

## Fabrication Gate

DO NOT fabricate until:

1. Native KiCad schematic is completed.
2. BQ51013C symbol pin mapping is verified.
3. TI reference schematic is cross-checked.
4. Resonant network is characterized.
5. FOD calibration is completed.
6. USB-C source implementation is reviewed.
7. Protection components are validated.
8. PCB layout is completed.
9. ERC is clean.
10. Electrical prototype testing passes.
11. Thermal testing passes.
12. Prototype BOM is frozen.
13. Appropriate Qi/WPC compliance requirements are addressed.
