# MagCharge Universal Receiver V1 — Schematic Source

## Engineering Status

PRELIMINARY ENGINEERING SOURCE — NOT FABRICATION READY

This source defines the intended electrical topology.
Final KiCad schematic must use the current TI BQ51013C datasheet
and verified symbol pin mapping before PCB fabrication.

## Main IC

U1 = TI BQ51013CRHLR

Function:
- Qi wireless power receiver
- Rectification
- Power management
- 5 V regulated output
- FOD
- Thermal/temperature input
- Current-limit configuration

## Nets

RX_COIL_A
RX_COIL_B
RECT_IN
RECT_GND
VOUT_RAW
+5V_USB
GND
TS
FOD
ILIM
USB_VBUS
USB_GND
USB_CC1
USB_CC2

## Power Path

L1 RX coil
  -> U1 wireless receiver input
  -> internal rectification
  -> VOUT_RAW
  -> protection/current control
  -> +5V_USB
  -> USB-C VBUS

Ground:
U1 / coil return / protection / USB-C ground
-> GND

## Receiver Coil

L1:
Wurth 760308103215
48 x 32 mm
14.3 uH nominal
Maximum resistance: 190 mOhm

The final coil must be re-characterized with the
MagCharge magnetic/ferrite/mechanical stack.

## Reference Components

C1  68 nF 50 V X7R
C2  68 nF 50 V X7R
C3  47 nF 50 V X7R
C4  1.8 nF 50 V C0G/NP0
C5  100 pF 100 V C0G/NP0
C6  100 nF 50 V X7R
C7  1 uF 50 V X7R
C8  22 nF 50 V X7R
C9  470 nF 25 V X7R
C10 10 nF 50 V X7R
C11 10 nF 50 V X7R
C12 470 nF 25 V X7R
C13 22 nF 50 V X7R
C14 10 uF 35 V X7R
C15 10 uF 35 V X7R
C16 100 nF 50 V X7R
C17 1 uF 50 V X7R
C18 100 nF 50 V X7R
C19 100 nF 50 V X7R
C20 1 uF 50 V X7R

## Configuration

R17 = 42.2 kOhm, 1%
FOD reference

R4 = 110 Ohm, 1%
ILIM reference

R11 = 10 kOhm
Prototype TS simulation only

R1 = 10 kOhm
R2 = 200 Ohm
R7 = 1.50 kOhm
R10 = 499 Ohm
R15 = 1.00 kOhm

D2 = BZT52C5V1T-7
5.1 V Zener

Q1 = SQ4949EY-T1_GE3
P-channel MOSFET

## USB-C Output

Target:
5 V / 1 A maximum for V1 prototype

USB-C:
VBUS -> +5V_USB
GND -> GND

CC1 and CC2:
Implement according to the final USB-C source configuration
and applicable USB-C requirements.

V1 does NOT implement USB Power Delivery.

## Thermal

Production design:
- characterized NTC
- thermal shutdown/protection
- thermal validation under worst-case alignment

R11 is only a prototype placeholder where applicable.

## Safety

Hardware safety must operate independently of:
- Android application
- BLE
- cloud services
- phone software

Do not use the Android application as a safety controller.

## Validation

Initial electrical validation:
- no phone connected
- certified/proven Qi transmitter
- electronic load
- current-limited laboratory supply where applicable
- measure VOUT_RAW
- measure +5V_USB
- measure temperature
- verify FOD
- verify current limit
- verify thermal protection

Phone testing occurs only after electrical validation passes.

## Fabrication Gate

DO NOT fabricate until:

1. Current TI datasheet pin mapping is verified.
2. TI reference schematic is cross-checked.
3. Coil/resonant network is verified.
4. FOD network is verified.
5. USB-C implementation is reviewed.
6. PCB clearances are reviewed.
7. Thermal limits are validated.
8. ERC is clean in KiCad.
9. Prototype BOM is frozen.
