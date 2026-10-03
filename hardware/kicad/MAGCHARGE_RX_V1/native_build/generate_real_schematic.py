from pathlib import Path
import re
import uuid

ROOT = Path("hardware/kicad/MAGCHARGE_RX_V1")
SRC = ROOT / "MAGCHARGE_RX_V1.kicad_sch"
OUT = ROOT / "MAGCHARGE_RX_V1_REAL.kicad_sch"

src = SRC.read_text()

def uid():
    return str(uuid.uuid4())

# ------------------------------------------------------------
# Extract embedded library symbols from the existing schematic.
# ------------------------------------------------------------
m = re.search(
    r'(\n\t\(lib_symbols\b.*?\n\t\)\n)',
    src,
    flags=re.S
)

if not m:
    raise SystemExit("ERROR: embedded lib_symbols section not found")

lib_symbols = m.group(1)

# ------------------------------------------------------------
# Locate schematic header information.
# ------------------------------------------------------------
version_match = re.search(r'\(version\s+([0-9]+)\)', src)
version = version_match.group(1) if version_match else "20250114"

generator_match = re.search(r'\(generator\s+([^)]+)\)', src)
generator = generator_match.group(1).strip() if generator_match else "eeschema"

# ------------------------------------------------------------
# Native schematic body.
#
# Coordinates are arranged as:
#
#       COIL / AC INPUT
#              |
#       BQ51013C RECEIVER
#              |
#       RECT / +5V
#              |
#          USB-C OUT
#
# Control/FOD network is below U1.
# ------------------------------------------------------------

body = []

def text(t, x, y, size=1.0):
    body.append(f'''
\t(text "{t}"
\t\t(exclude_from_sim no)
\t\t(at {x} {y} 0)
\t\t(layer "text")
\t\t(uuid "{uid()}")
\t\t(effects
\t\t\t(font
\t\t\t\t(size {size} {size})
\t\t\t)
\t\t)
\t)
''')

# ------------------------------------------------------------
# Titles
# ------------------------------------------------------------

text("MAGCHARGE RX V1", 80, 45, 2.0)
text("BQ51013C WIRELESS POWER RECEIVER / 5V USB-C SOURCE", 80, 49, 1.2)

text("WIRELESS COIL", 65, 70, 1.2)
text("BQ51013C RECEIVER", 135, 70, 1.2)
text("RECTIFIED DC / OUTPUT", 205, 70, 1.2)
text("FOD / ILIM / THERMAL", 135, 170, 1.2)

# ------------------------------------------------------------
# Net labels / architecture labels.
# ------------------------------------------------------------

for label, x, y in [
    ("AC1", 95, 82),
    ("AC2", 95, 112),
    ("RECT", 190, 85),
    ("+5V_RX", 225, 85),
    ("PGND", 190, 125),
    ("FOD", 160, 150),
    ("ILIM", 120, 150),
    ("TS_CTRL", 185, 150),
    ("CHG_STATUS", 210, 150),
]:
    text(label, x, y, 1.0)

# ------------------------------------------------------------
# Native connection documentation inside schematic.
# ------------------------------------------------------------

notes = [
    "L1 760308103215 = 14.3uH NOMINAL",
    "C_RX1 = TBD AFTER COIL CHARACTERIZATION",
    "C_RX2 = TBD AFTER COIL CHARACTERIZATION",
    "BOOT1 -> 10nF -> AC1",
    "BOOT2 -> 10nF -> AC2",
    "COMM1 -> 22nF -> AC1",
    "COMM2 -> 22nF -> AC2",
    "CLAMP1 -> 0.47uF -> AC1",
    "CLAMP2 -> 0.47uF -> AC2",
    "RECT -> 10uF + 10uF + 0.1uF -> PGND",
    "OUT -> +5V_RX -> 10uF + 0.1uF -> PGND",
    "ILIM -> 66R -> FOD",
    "RECT -> 20k -> FOD",
    "FOD -> 196R -> PGND",
    "TS/CTRL -> NTC1 -> PGND",
    "AD -> PGND",
    "AD-EN -> NC",
    "EN1/EN2 -> LOW / INTERNAL PULLDOWN",
    "USB-C = 5V SOURCE / TARGET 1A / NO USB-PD",
    "ESD1 / FUSE1 = TBD",
    "DO NOT FABRICATE UNTIL RESONANCE + FOD ARE VALIDATED",
]

y = 180
for n in notes:
    text(n, 80, y, 0.85)
    y += 3.2

# ------------------------------------------------------------
# Create explicit wire records.
#
# These are architectural wire paths.  The final component
# pin coordinates will be placed around this grid.
# ------------------------------------------------------------

def wire(x1, y1, x2, y2):
    body.append(f'''
\t(wire
\t\t(pts
\t\t\t(xy {x1} {y1})
\t\t\t(xy {x2} {y2})
\t\t)
\t\t(stroke
\t\t\t(width 0)
\t\t\t(type default)
\t\t)
\t\t(uuid "{uid()}")
\t)
''')

# AC1 / AC2 bus
wire(95, 82, 120, 82)
wire(95, 112, 120, 112)

# RECT bus
wire(180, 85, 205, 85)

# +5V bus
wire(205, 85, 235, 85)

# PGND
wire(180, 125, 235, 125)

# FOD
wire(120, 150, 190, 150)

# TS
wire(180, 150, 215, 150)

# CHG
wire(205, 150, 235, 150)

# ------------------------------------------------------------
# Junctions.
# ------------------------------------------------------------

for x, y in [
    (120,82),
    (120,112),
    (205,85),
    (235,85),
    (235,125),
    (160,150),
    (190,150),
]:
    body.append(f'''
\t(junction
\t\t(at {x} {y})
\t\t(diameter 0)
\t\t(color 0 0 0 0)
\t\t(uuid "{uid()}")
\t)
''')

# ------------------------------------------------------------
# Connection table as schematic notes.
# ------------------------------------------------------------

text("U1 PIN CONNECTION TABLE", 80, 250, 1.3)

pins = [
    "1  PGND      -> PGND",
    "2  AC1       -> AC1",
    "3  BOOT1     -> C_BOOT1 10nF -> AC1",
    "4  OUT       -> +5V_RX",
    "5  CLAMP1    -> C_CLAMP1 0.47uF -> AC1",
    "6  COMM1     -> C_COMM1 22nF -> AC1",
    "7  CHG       -> CHG_STATUS",
    "8  AD-EN     -> NC",
    "9  AD        -> PGND",
    "10 EN1       -> LOW / INTERNAL PULLDOWN",
    "11 EN2       -> LOW / INTERNAL PULLDOWN",
    "12 ILIM      -> R1 66R -> FOD",
    "13 TS/CTRL   -> NTC1 -> PGND",
    "14 FOD       -> FOD NETWORK",
    "15 COMM2     -> C_COMM2 22nF -> AC2",
    "16 CLAMP2    -> C_CLAMP2 0.47uF -> AC2",
    "17 BOOT2     -> C_BOOT2 10nF -> AC2",
    "18 RECT      -> RECT FILTER",
    "19 AC2       -> AC2",
    "20 PGND      -> PGND",
    "EP           -> PGND / THERMAL",
]

y = 255
for p in pins:
    text(p, 80, y, 0.85)
    y += 3.0

# ------------------------------------------------------------
# Fabrication gate.
# ------------------------------------------------------------

text("FABRICATION GATE", 80, 320, 1.4)

gate = [
    "1. Verify U1 pin mapping in KiCad",
    "2. Characterize L1 / select C_RX1 / C_RX2",
    "3. Calibrate FOD network",
    "4. Select production NTC",
    "5. Finalize USB-C ESD + fuse + CC implementation",
    "6. Complete PCB placement/routing",
    "7. Run KiCad ERC",
    "8. Thermal and electrical testing",
    "9. Freeze BOM",
]

y = 325
for g in gate:
    text(g, 80, y, 0.9)
    y += 3.2

# ------------------------------------------------------------
# Assemble valid KiCad schematic.
# ------------------------------------------------------------

header = f'''(kicad_sch
\t(version {version})
\t(generator {generator})
'''

tail = '''
)
'''

OUT.write_text(header + lib_symbols + "".join(body) + tail)

print("CREATED:", OUT)
print("SIZE:", OUT.stat().st_size)
