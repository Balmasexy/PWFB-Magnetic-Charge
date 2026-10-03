from pathlib import Path
import re

p = Path("hardware/kicad/MAGCHARGE_RX_V1/MAGCHARGE_RX_V1_CONNECTED.kicad_sch")
s = p.read_text()

print("=== EMBEDDED SYMBOL LIBRARY CHECK ===")

symbols = [
    "BQ51013CRHLR",
    "Device:C",
    "Device:R",
    "Device:L",
    "Device:D",
    "Device:Thermistor",
    "Connector:USB_C",
]

for x in symbols:
    n = s.count(f'(symbol "{x}"')
    print(f"{x}: {n}")

print()
print("BQ51013CRHLR definitions:", s.count("BQ51013CRHLR"))
print("Embedded lib_symbols:", "(lib_symbols" in s)

print()
print("=== AVAILABLE DEVICE SYMBOL NAMES ===")

for x in re.findall(r'\(symbol "([^"]+)"', s):
    if x.startswith(("Device:", "Connector:", "BQ")):
        print(x)

print()
print("RESULT: LIBRARY INVENTORY COMPLETE")
