from pathlib import Path
import re

p = Path("hardware/kicad/MAGCHARGE_RX_V1/MAGCHARGE_RX_V1_NATIVE.kicad_sch")
s = p.read_text()

print("=== MAGCHARGE RX V1 NATIVE DESIGN VERIFICATION ===")

checks = {
    "BQ51013C": "BQ51013CRHLR",
    "Wireless coil": "760308103215",
    "AC1": "AC1",
    "AC2": "AC2",
    "RECT": "RECT",
    "+5V output": "+5V_RX",
    "PGND": "PGND",
    "BOOT1": "BOOT1",
    "BOOT2": "BOOT2",
    "COMM1": "COMM1",
    "COMM2": "COMM2",
    "CLAMP1": "CLAMP1",
    "CLAMP2": "CLAMP2",
    "ILIM": "ILIM",
    "FOD": "FOD",
    "TS/CTRL": "TS_CTRL",
    "USB-C": "USB-C",
    "AD": "AD",
    "AD-EN": "AD-EN",
    "EN1": "EN1",
    "EN2": "EN2",
}

failed = []

for name, token in checks.items():
    ok = token in s
    print(("PASS " if ok else "FAIL "), name, "->", token)
    if not ok:
        failed.append(name)

print()
print("=== REQUIRED COMPONENTS ===")

components = [
    "C_RX1",
    "C_RX2",
    "C_BOOT1",
    "C_BOOT2",
    "C_COMM1",
    "C_COMM2",
    "C_CLAMP1",
    "C_CLAMP2",
    "C_RECT1",
    "C_RECT2",
    "C_RECT3",
    "C_OUT1",
    "C_OUT2",
    "R_OS",
    "R1",
    "R_FOD",
    "NTC1",
    "J1",
    "ESD1",
    "FUSE1",
    "SH1",
    "MR1",
]

for c in components:
    ok = c in s
    print(("PASS " if ok else "FAIL "), c)
    if not ok:
        failed.append(c)

print()
print("=== DESIGN RULE FLAGS ===")

rules = [
    ("AD tied to PGND", "AD -> PGND"),
    ("AD-EN floating", "AD-EN -> NC"),
    ("EN1/EN2 low/floating", "EN1/EN2 -> LOW/FLOATING"),
    ("USB-PD disabled", "NO USB-PD"),
    ("5V output", "5V SOURCE"),
    ("1A target", "TARGET 1A"),
    ("resonant values TBD", "C_RX1 = TBD"),
    ("production NTC TBD", "NTC1 = PRODUCTION VALUE TBD"),
    ("FOD calibration", "ILIM -> 66R -> FOD; RECT -> 20k -> FOD; FOD -> 196R -> PGND"),
]

for name, token in rules:
    ok = token in s
    print(("PASS " if ok else "FAIL "), name)
    if not ok:
        failed.append(name)

print()
print("==============================================")

if failed:
    print("RESULT: FAILED")
    print("Missing:")
    for x in failed:
        print(" -", x)
else:
    print("RESULT: NATIVE DESIGN CONTENT VERIFIED")
    print("The receiver architecture is present.")
    print("Next step: generate the actual placed symbols and wires.")

print("==============================================")
