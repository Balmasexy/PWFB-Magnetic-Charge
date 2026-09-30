# TI BQ51013C EVM Figure 3-1 — Connection Reference

Source:
Texas Instruments BQ51013CEVM User Guide
SLUUD57A, revised May 2025

Figure:
3-1 — BQ51013C Schematic

## U1 — BQ51013CRHLR

Pin 1  PGND
Pin 2  AC1
Pin 3  BOOT1
Pin 4  OUT
Pin 5  CLAMP1
Pin 6  COMM1
Pin 7  CHG
Pin 8  AD-EN
Pin 9  AD
Pin 10 EN1
Pin 11 EN2
Pin 12 ILIM
Pin 13 TS/CTRL
Pin 14 FOD
Pin 15 COMM2
Pin 16 CLAMP2
Pin 17 BOOT2
Pin 18 RECT
Pin 19 AC2
Pin 20 PGND
EP    PGND

## TI EVM peripheral connections

AC1:
L1 / C1 / BOOT1 / COMM1 / CLAMP1

AC2:
L1 / C2 / BOOT2 / COMM2 / CLAMP2

BOOT1:
10nF to AC1

BOOT2:
10nF to AC2

COMM1:
22nF to AC1

COMM2:
22nF to AC2

CLAMP1:
470nF to AC1

CLAMP2:
470nF to AC2

RECT:
10uF + 10uF + 100nF to GND

OUT:
1uF + 100nF to GND

AD:
EVM wired adapter detection network

AD-EN:
EVM external PFET control

EN1:
EVM jumper-controlled

EN2:
EVM jumper-controlled

TS/CTRL:
EVM adjustable/fixed NTC network

CHG:
EVM LED/status circuit

ILIM:
EVM adjustable current-limit network

FOD:
EVM FOD calibration network

## MagCharge V1 deviations

MagCharge V1 is wireless-only.

AD:
PGND

AD-EN:
NC / floating

EN1:
LOW / floating
Internal pulldown

EN2:
LOW / floating
Internal pulldown

CHG:
Status/test point only

TS/CTRL:
Production NTC required

USB-C:
5V regulated output, target 1A

FOD / ILIM:
Use MagCharge verified calibration topology:

RECT -> R_OS -> FOD

ILIM -> R1 -> FOD

FOD -> R_FOD -> PGND

Starting values:

R_OS  = 20k
R1    = 66R
R_FOD = 196R

R_ILIM = R1 + R_FOD = 262R

Final values require receiver characterization and FOD calibration.

## Resonant network

C_RX1:
Series resonant capacitor (Cs)
Value TBD after Ls' measurement

C_RX2:
Parallel resonant capacitor (Cd)
Value TBD after Ls measurement

Do not copy TI EVM C1/C2 values directly.

## Important

This file is a reference map, not a fabrication release.

MagCharge V1 must be validated against:
- BQ51013C datasheet
- final receiver coil
- final magnetic stack
- resonance measurements
- FOD calibration
- thermal testing
- USB-C electrical testing
- WPC requirements
