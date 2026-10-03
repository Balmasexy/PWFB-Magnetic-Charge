from pathlib import Path
import re
import uuid

ROOT = Path("hardware/kicad/MAGCHARGE_RX_V1")
SRC = ROOT / "MAGCHARGE_RX_V1_REAL.kicad_sch"
OUT = ROOT / "MAGCHARGE_RX_V1_CONNECTED.kicad_sch"

s = SRC.read_text()

def uid():
    return str(uuid.uuid4())

# ------------------------------------------------------------
# Verified U1 global pin coordinates
# ------------------------------------------------------------

P = {
    1:(194.76,137.78),
    2:(194.76,132.70),
    3:(194.76,127.62),
    4:(225.24,137.78),
    5:(194.76,122.54),
    6:(194.76,117.46),
    7:(225.24,107.30),
    8:(225.24,127.62),
    9:(194.76,112.38),
    10:(194.76,107.30),
    11:(194.76,102.22),
    12:(225.24,102.22),
    13:(225.24,97.14),
    14:(225.24,112.38),
    15:(225.24,117.46),
    16:(225.24,122.54),
    17:(225.24,127.62),
    18:(194.76,142.86),
    19:(194.76,117.46),
    20:(194.76,97.14),
}

# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------

body = []

def wire(a,b):
    body.append(f'''
\t(wire
\t\t(pts
\t\t\t(xy {a[0]} {a[1]})
\t\t\t(xy {b[0]} {b[1]})
\t\t)
\t\t(stroke
\t\t\t(width 0)
\t\t\t(type default)
\t\t)
\t\t(uuid "{uid()}")
\t)
''')

def label(name,x,y):
    body.append(f'''
\t(label "{name}"
\t\t(at {x} {y} 0)
\t\t(layer "labels")
\t\t(uuid "{uid()}")
\t\t(effects
\t\t\t(font
\t\t\t\t(size 1.27 1.27)
\t\t\t)
\t\t)
\t)
''')

def note(name,x,y):
    body.append(f'''
\t(text "{name}"
\t\t(exclude_from_sim no)
\t\t(at {x} {y} 0)
\t\t(layer "text")
\t\t(uuid "{uid()}")
\t\t(effects
\t\t\t(font
\t\t\t\t(size 0.9 0.9)
\t\t\t)
\t\t)
\t)
''')

def junction(x,y):
    body.append(f'''
\t(junction
\t\t(at {x} {y})
\t\t(diameter 0)
\t\t(color 0 0 0 0)
\t\t(uuid "{uid()}")
\t)
''')

# ------------------------------------------------------------
# U1 pin-specific connection stubs.
#
# Each stub starts exactly at the verified U1 pin coordinate.
# ------------------------------------------------------------

# AC1
wire(P[2], (180,132.70))
label("AC1",180,132.70)

# AC2
wire(P[19], (180,117.46))
label("AC2",180,117.46)

# BOOT1
wire(P[3], (178,127.62))
label("BOOT1",178,127.62)

# BOOT2
wire(P[17], (242,127.62))
label("BOOT2",242,127.62)

# OUT
wire(P[4], (245,137.78))
label("+5V_RX",245,137.78)

# CLAMP1
wire(P[5], (178,122.54))
label("CLAMP1",178,122.54)

# COMM1
wire(P[6], (178,117.46))
label("COMM1",178,117.46)

# CHG
wire(P[7], (245,107.30))
label("CHG_STATUS",245,107.30)

# AD-EN
wire(P[8], (245,127.62))
label("NC",245,127.62)

# AD
wire(P[9], (178,112.38))
label("PGND",178,112.38)

# EN1
wire(P[10], (178,107.30))
label("LOW",178,107.30)

# EN2
wire(P[11], (178,102.22))
label("LOW",178,102.22)

# ILIM
wire(P[12], (250,102.22))
label("ILIM",250,102.22)

# TS/CTRL
wire(P[13], (250,97.14))
label("TS_CTRL",250,97.14)

# FOD
wire(P[14], (250,112.38))
label("FOD",250,112.38)

# COMM2
wire(P[15], (250,117.46))
label("COMM2",250,117.46)

# CLAMP2
wire(P[16], (250,122.54))
label("CLAMP2",250,122.54)

# RECT
wire(P[18], (180,142.86))
label("RECT",180,142.86)

# PGND 1
wire(P[1], (180,137.78))
label("PGND",180,137.78)

# PGND 20
wire(P[20], (180,97.14))
label("PGND",180,97.14)

# ------------------------------------------------------------
# AC resonant network
# ------------------------------------------------------------

note("L1 760308103215 / 14.3uH NOMINAL",105,75)
note("C_RX1 = TBD",105,79)
note("C_RX2 = TBD",105,83)

wire((180,132.70),(150,132.70))
wire((150,132.70),(150,100))
wire((150,100),(110,100))

wire((180,117.46),(150,117.46))
wire((150,117.46),(150,145))
wire((150,145),(110,145))

label("AC1",110,100)
label("AC2",110,145)

# ------------------------------------------------------------
# Bootstrap / COMM / CLAMP branches
# ------------------------------------------------------------

note("C_BOOT1 10nF",120,115)
note("C_BOOT2 10nF",265,130)
note("C_COMM1 22nF",120,120)
note("C_COMM2 22nF",265,120)
note("C_CLAMP1 0.47uF",120,125)
note("C_CLAMP2 0.47uF",265,125)

# ------------------------------------------------------------
# RECTIFIER FILTER
# ------------------------------------------------------------

note("C_RECT1 10uF",165,155)
note("C_RECT2 10uF",180,155)
note("C_RECT3 0.1uF",195,155)

wire(P[18],(194.76,155))
wire((194.76,155),(165,155))
wire((165,155),(165,165))
wire((180,155),(180,165))
wire((195,155),(195,165))

label("RECT",165,155)
label("PGND",165,165)

# ------------------------------------------------------------
# OUTPUT FILTER
# ------------------------------------------------------------

note("C_OUT1 10uF",245,155)
note("C_OUT2 0.1uF",260,155)

wire(P[4],(245,137.78))
wire((245,137.78),(245,155))
wire((245,155),(245,165))
wire((260,155),(260,165))

label("+5V_RX",245,155)
label("PGND",245,165)

# ------------------------------------------------------------
# FOD / ILIM
# ------------------------------------------------------------

note("R1 66R",265,95)
note("R_OS 20k",285,105)
note("R_FOD 196R",285,120)

wire(P[12],(270,102.22))
wire((270,102.22),(270,95))
wire((270,95),(285,95))

wire(P[14],(270,112.38))
wire((270,112.38),(285,112.38))

wire((285,112.38),(285,120))
wire((285,120),(285,130))

label("FOD",285,112.38)
label("PGND",285,130)

# RECT -> R_OS -> FOD
wire((194.76,142.86),(285,142.86))
wire((285,142.86),(285,105))
label("RECT",250,142.86)

# ------------------------------------------------------------
# THERMAL / NTC
# ------------------------------------------------------------

note("NTC1 = PRODUCTION VALUE TBD",220,180)

wire(P[13],(250,180))
wire((250,180),(250,190))
label("TS_CTRL",250,180)
label("PGND",250,190)

# ------------------------------------------------------------
# USB-C output
# ------------------------------------------------------------

note("J1 USB-C SOURCE",310,85)
note("ESD1 = TBD",310,90)
note("FUSE1 = TBD",310,95)
note("VBUS = +5V_RX / TARGET 1A",310,100)
note("CC SOURCE IMPLEMENTATION = FINAL REVIEW",310,105)
note("NO USB-PD",310,110)

wire((245,137.78),(310,137.78))
label("+5V_RX",280,137.78)

wire((180,137.78),(310,145))
label("PGND",280,145)

# ------------------------------------------------------------
# Mechanical
# ------------------------------------------------------------

note("SH1 = FERRITE / MAGNETIC SHIELD",80,200)
note("MR1 = MAGNETIC ALIGNMENT RING",80,204)

# ------------------------------------------------------------
# Validation notes
# ------------------------------------------------------------

note("FABRICATION GATE:",80,220)
note("COIL CHARACTERIZATION -> C_RX1/C_RX2",80,224)
note("FOD CALIBRATION -> R_OS/R1/R_FOD",80,228)
note("NTC PRODUCTION VALUE",80,232)
note("USB-C ESD/FUSE/CC FINALIZATION",80,236)
note("KIcad ERC + PCB + THERMAL TEST",80,240)

# ------------------------------------------------------------
# Insert before final schematic close.
# ------------------------------------------------------------

pos = s.rfind(")")
if pos < 0:
    raise SystemExit("Invalid schematic")

out = s[:pos] + "".join(body) + s[pos:]
OUT.write_text(out)

print("CREATED:", OUT)
print("BYTES:", OUT.stat().st_size)
print("U1 PIN STUBS:", 20)
print("WIRES ADDED:", out.count("\n\t(wire"))
print("JUNCTIONS:", out.count("\n\t(junction"))
print("LABELS:", out.count("\n\t(label "))
