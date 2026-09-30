# Native KiCad Template Plan

The native schematic will be generated from a KiCad-format template
rather than fabricated from an assumed file syntax.

Required native objects:

U1  BQ51013CRHLR
L1  760308103215
C_RX1
C_RX2
C_BOOT1
C_BOOT2
C_COMM1
C_COMM2
C_CLAMP1
C_CLAMP2
C_RECT1
C_RECT2
C_RECT3
C_OUT1
C_OUT2
R_OS
R1
R_FOD
NTC1
J1
ESD1
FUSE1
SH1
MR1

Required nets:

AC1
AC2
BOOT1
BOOT2
COMM1
COMM2
CLAMP1
CLAMP2
RECT
FOD
ILIM
TS_CTRL
EN1
EN2
CHG_STATUS
+5V_RX
PGND

Critical verified connections:

U1 pin 9 AD -> PGND
U1 pin 8 AD-EN -> intentionally floating
U1 pin 10 EN1 -> LOW/floating
U1 pin 11 EN2 -> LOW/floating
U1 pin 12 ILIM -> R1 -> FOD
U1 pin 14 FOD -> R_FOD -> PGND
RECT -> R_OS -> FOD
U1 pin 18 RECT -> RECT capacitors
U1 pin 4 OUT -> +5V_RX
U1 pins 1,20,EP -> PGND

Status:
PRELIMINARY ENGINEERING SOURCE
KiCad application/ERC validation required before fabrication.
