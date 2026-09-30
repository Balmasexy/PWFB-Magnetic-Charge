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

Final resonance must be calculated and verified using the actual
MagCharge coil and mechanical stack.

---

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

## FOD

U1 pin 14:

FOD = rectified-power measurement input.

The FOD pin voltage is proportional to output current and is used by
the BQ51013C to report received power to the Qi transmitter.

RFOD is part of the ILIM resistance path and participates in FOD
calibration.

RFOD starting/reference:
196 ohm

Final RFOD value requires FOD calibration.


### ROS

ROS is a separate FOD calibration resistor shown in TI Figure 9-1.

Starting/reference value:

ROS = 20 kohm

ROS and RFOD are both subject to final FOD calibration.

TI recommends providing two resistor positions for ROS and two resistor
positions for RFOD so that the final calibrated values can be fitted
after receiver characterization.

Do not treat ROS as part of RILIM.

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
U1 pin 10 -> low/floating

EN2:
U1 pin 11 -> low/floating

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
