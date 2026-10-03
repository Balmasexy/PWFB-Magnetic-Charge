# MAGCHARGE RX V1 — NATIVE CIRCUIT CONNECTIONS

## U1 — BQ51013CRHLR

1  PGND      -> PGND
2  AC1       -> AC1
3  BOOT1     -> C_BOOT1 -> AC1
4  OUT       -> +5V_RX
5  CLAMP1    -> C_CLAMP1 -> AC1
6  COMM1     -> C_COMM1 -> AC1
7  CHG       -> CHG_STATUS
8  AD-EN     -> NC / FLOATING
9  AD        -> PGND
10 EN1       -> LOW / INTERNAL PULLDOWN
11 EN2       -> LOW / INTERNAL PULLDOWN
12 ILIM      -> R1 66R -> FOD
13 TS/CTRL   -> NTC1 -> PGND
14 FOD       -> FOD NETWORK
15 COMM2     -> C_COMM2 -> AC2
16 CLAMP2    -> C_CLAMP2 -> AC2
17 BOOT2     -> C_BOOT2 -> AC2
18 RECT      -> RECT_FILTER
19 AC2       -> AC2
20 PGND      -> PGND
EP           -> PGND / THERMAL

## WIRELESS INPUT

L1 = Würth 760308103215
Nominal inductance = 14.3uH

L1 terminal A -> AC1
L1 terminal B -> AC2

C_RX1 = TBD
Series resonant capacitor.

C_RX2 = TBD
Parallel resonant capacitor.

C_RX1/C_RX2 values must be selected after actual coil characterization.

## BOOTSTRAP

C_BOOT1 = 10nF
BOOT1 -> C_BOOT1 -> AC1

C_BOOT2 = 10nF
BOOT2 -> C_BOOT2 -> AC2

## COMMUNICATION

C_COMM1 = 22nF
COMM1 -> C_COMM1 -> AC1

C_COMM2 = 22nF
COMM2 -> C_COMM2 -> AC2

## CLAMP

C_CLAMP1 = 0.47uF
CLAMP1 -> C_CLAMP1 -> AC1

C_CLAMP2 = 0.47uF
CLAMP2 -> C_CLAMP2 -> AC2

## RECTIFIER

RECT -> C_RECT1 10uF -> PGND
RECT -> C_RECT2 10uF -> PGND
RECT -> C_RECT3 0.1uF -> PGND

## OUTPUT

OUT -> +5V_RX

+5V_RX -> C_OUT1 10uF -> PGND
+5V_RX -> C_OUT2 0.1uF -> PGND

Target:
5V nominal
1A target
No USB-PD

## FOD / ILIM

ILIM -> R1 66R -> FOD

RECT -> R_OS 20k -> FOD

FOD -> R_FOD 196R -> PGND

These are starting values and require calibration.

## THERMAL

TS/CTRL -> NTC1 -> PGND

NTC1 production value = TBD.

## CONTROL

AD -> PGND

AD-EN -> NC / FLOATING

EN1 -> LOW / INTERNAL PULLDOWN

EN2 -> LOW / INTERNAL PULLDOWN

CHG -> open-drain CHG_STATUS

## USB-C

J1 = USB-C source output.

+5V_RX -> protection -> USB-C VBUS

PGND -> USB-C GND

No USB-PD.

ESD1 = TBD
FUSE1 = TBD

USB-C source CC implementation requires final review before fabrication.

## MECHANICAL

SH1 = magnetic/ferrite shielding
MR1 = magnetic alignment ring

Final stack-up and alignment require validation.

## FABRICATION GATE

Do not fabricate until:

1. Native schematic loads correctly in KiCad.
2. U1 pin mapping is verified.
3. AC1/AC2 resonant network is characterized.
4. C_RX1/C_RX2 are selected.
5. FOD is calibrated.
6. NTC value is selected.
7. USB-C protection is finalized.
8. ERC is reviewed.
9. PCB placement/routing is completed.
10. Thermal/electrical testing is completed.
