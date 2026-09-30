# MagCharge Universal Receiver V1 — Pin-Accurate Schematic Netlist

## Status

Engineering reference specification based on the Texas Instruments
BQ51013C datasheet, SLUSFU9A, revised May 2025.

NOT production validated.
NOT a fabrication release.
NOT WPC certification.

---

## Receiver IC

U1:
Texas Instruments BQ51013CRHLR

Package:
VQFN20 / RHL

---

## Verified Pin Map

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

## Receiver Coil

L1:
Würth Electronics 760308103215

Nominal inductance:
14.3 uH

Dimensions:
48 mm x 32 mm

Connections:

L1-A -> AC1 / resonant network
L1-B -> AC2 / resonant network

Required final characterization:

- Ls'
- Ls
- DC resistance
- Q factor
- resonance
- efficiency

The TI 11-uH example resonant values must not be copied directly.

---

## Resonant Network

C1:
Series resonant capacitor (Cs)

Value:
TBD after Ls' measurement

Voltage:
25 V minimum

C2:
Parallel resonant capacitor (Cd)

Value:
TBD after Ls measurement

Voltage:
25 V minimum

### TI / WPC Resonance Characterization Procedure

C1 and C2 form the dual-resonant circuit with the receiver coil.

The final values must be calculated using the actual MagCharge receiver
coil and the final mechanical stack.

Measure the receiver coil with the final intended construction.

For Ls' measurement, use the WPC v1.3 receiver coil test fixture:

- Primary shield: 50 mm x 50 mm x 1 mm TDK PC44 ferrite
- Test fixture gap dZ: 3.4 mm
- Receiver coil installed as it will be used in the final product
- Include relevant back cover, battery, spacer, shielding and other
  mechanical materials that affect the magnetic stack
- Measure at 1 V RMS and 100 kHz
- Record this value as Ls'

Repeat the measurement without the WPC test fixture to obtain the
free-space inductance Ls.

Calculate C1 first:

C1 = 1 / ((2*pi*fS)^2 * Ls')

where:

fS = 100 kHz (+5% / -10%)

Then calculate C2:

C2 = 1 / ((2*pi*fD)^2 * Ls - 1/C1)

where:

fD = 1 MHz (+/-10%)

C1 must be selected before calculating C2.

### Coil Quality Factor

Verify:

Q > 77

Q = (2*pi*fD*Ls) / R

where R is the DC resistance of the receiver coil.

### MagCharge V1 Coil

Selected starting coil:

Wurth Electronics 760308103215

Nominal free-space inductance:
14.3 uH

Dimensions:
48 mm x 32 mm

This 14.3-uH nominal value is NOT sufficient by itself to finalize C1
and C2. The actual Ls' and Ls measurements must be performed with the
final magnetic/mechanical stack.

The TI 11-uH example values of approximately 154 nF for C1 and 2.3 nF
for C2 must not be copied directly into MagCharge V1.

Final C1/C2 values require measured coil data, calculation, receiver
testing and WPC v1.3 validation.

## BOOT Network

C_BOOT1:
10 nF starting value

BOOT1 -> C_BOOT1 -> AC1

C_BOOT2:
10 nF starting value

BOOT2 -> C_BOOT2 -> AC2

Minimum voltage rating:
25 V

---

## COMM Network

C_COMM1:
22 nF starting value

COMM1 -> C_COMM1 -> AC1

C_COMM2:
22 nF starting value

COMM2 -> C_COMM2 -> AC2

Minimum voltage rating:
25 V

47 nF may be evaluated only if final communication testing requires it.

---

## CLAMP Network

C_CLAMP1:
0.47 uF starting value

CLAMP1 -> C_CLAMP1 -> AC1

C_CLAMP2:
0.47 uF starting value

CLAMP2 -> C_CLAMP2 -> AC2

Minimum voltage rating:
25 V

---

## RECT Network

C_RECT1:
10 uF

C_RECT2:
10 uF

C_RECT3:
0.1 uF

Minimum voltage:
16 V for the 1-A reference arrangement.

Connections:

RECT -> C_RECT1 -> PGND
RECT -> C_RECT2 -> PGND
RECT -> C_RECT3 -> PGND

---

## OUT Network

C_OUT1:
10 uF

C_OUT2:
0.1 uF

Connections:

OUT -> C_OUT1 -> PGND
OUT -> C_OUT2 -> PGND

OUT net:
+5V_RX

---

## ILIM

U1 pin 12:

ILIM -> R1 -> RFOD -> PGND

The TI Figure 9-1 application defines the total ILIM resistance as:

RILIM = R1 + RFOD

Starting/reference values:

RFOD = 196 ohm
R1 = 66 ohm
RILIM total = 262 ohm

Reference IMAX:
1 A

This gives a nominal 1.2 A hardware current limit according to the
TI reference design, allowing temporary current surges.

Final current-limit behavior requires board validation.


---

## FOD / ILIM Calibration Network

U1 pin 14:

FOD = rectified-power measurement input.

The FOD network follows the TI Figure 9-1 reference topology.

FOD node:
- U1 pin 14 (FOD)
- R_OS output from RECT
- R_FOD to PGND
- R1 connection from ILIM

### R_OS

R_OS:
RECT -> R_OS -> FOD node

Starting/reference:
20 kohm

R_OS is a separate FOD calibration resistor and is NOT part of RILIM.

### R_FOD

R_FOD:
FOD node -> R_FOD -> PGND

Starting/reference:
196 ohm

R_FOD participates in both FOD calibration and the ILIM resistance path.

### R1

R1:
ILIM -> R1 -> FOD node

Starting/reference:
66 ohm

### ILIM Resistance

The total resistance seen from ILIM to PGND is:

RILIM = R1 + R_FOD

Starting/reference:

RILIM = 66 ohm + 196 ohm = 262 ohm

Reference IMAX:
1 A

This produces a nominal 1.2-A hardware current limit according to the
TI reference application, allowing temporary current surges.

Final R_OS, R_FOD and R1 values require receiver characterization and
FOD calibration.

TI recommends providing two resistor positions for R_OS and two
positions for R_FOD so that precise values can be fitted after
calibration.

## TS / CTRL

U1 pin 13:

TS_CTRL -> characterized NTC -> PGND

Prototype/test termination:
10 kohm

The 10-kohm resistor is not a production substitute for a characterized
NTC.

---

## Wireless-Only Control

AD:
U1 pin 9 -> PGND

AD-EN:
U1 pin 8 -> floating

EN1:
U1 pin 10 -> LOW / floating

EN2:
U1 pin 11 -> LOW / floating

Wireless-only V1 control state:
EN1 = LOW
EN2 = LOW

The BQ51013C has internal pulldown resistors on EN1 and EN2.
For the wireless-only V1 receiver, no external controller is required
for the normal enabled state. EN1 and EN2 may therefore remain LOW
through their internal pulldowns or be driven LOW by the system
controller in a future controlled implementation.

With EN1 = EN2 = LOW, wireless power is enabled.

---

## CHG

U1 pin 7 -> CHG_STATUS

CHG is an open-drain charging-status output.

Optional LED circuitry may be added later.

---

## Ground

PGND includes:

- U1 pin 1
- U1 pin 20
- U1 exposed pad
- RECT capacitors
- OUT capacitors
- ILIM network
- TS/NTC network
- USB-C ground

The exposed pad requires a low-impedance thermal connection to PGND.
