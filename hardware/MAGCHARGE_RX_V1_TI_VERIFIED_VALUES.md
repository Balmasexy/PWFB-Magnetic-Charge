# MagCharge Universal Receiver V1 - TI Verified Reference Values

## Source

Texas Instruments BQ51013C Evaluation Module User's Guide.

Document:
SLUUD57A

Revision:
A

Revision date:
May 2025

The values below are taken from the TI BQ51013CEVM schematic and BOM.

These are reference-design values, not a claim that the final MagCharge PCB is already validated.

## Receiver IC

U1

Part:
BQ51013CRHLR

Manufacturer:
Texas Instruments

Package:
VQFN20

## Receiver Coil

L1

Part:
760308103215

Manufacturer:
Würth Electronics

Nominal inductance:
14.3 uH

Dimensions:
48 mm x 32 mm

Maximum resistance:
190 mOhm

The final MagCharge mechanical stack must be characterized again.

## Resonant Capacitors

C1:
68 nF
50 V
X7R

C2:
68 nF
50 V
X7R

C3:
47 nF
50 V
X7R

## Communication Network

C8:
22 nF
50 V
X7R

C13:
22 nF
50 V
X7R

## Clamp Network

C9:
470 nF
25 V
X7R

C12:
470 nF
25 V
X7R

## Boot Network

C10:
10 nF
50 V
X7R

C11:
10 nF
50 V
X7R

## Additional Receiver Network

C4:
1.8 nF
50 V
C0G/NP0

C5:
100 pF
100 V
C0G/NP0

## Output Capacitors

C14:
10 uF
35 V
X7R

C15:
10 uF
35 V
X7R

## Additional Decoupling

C6:
100 nF
50 V
X7R

C7:
1 uF
50 V
X7R

C16:
100 nF
50 V
X7R

C17:
1 uF
50 V
X7R

C18:
100 nF
50 V
X7R

C19:
100 nF
50 V
X7R

C20:
1 uF
50 V
X7R

## FOD

R17:
42.2 kOhm
1%
0603

## ILIM

R4:
110 Ohm
1%
0603

The EVM also provides an adjustable current-limit option using a 5 kOhm trimmer.

For the first MagCharge prototype, start with the fixed reference configuration and validate the actual current limit.

## TS / Temperature

R11:
10 kOhm

The TI EVM uses a 10 kOhm resistor to simulate the NTC during evaluation.

For the MagCharge production prototype, replace the simulation resistor with an appropriately characterized NTC.

## Other Reference Resistors

R1:
10 kOhm

R2:
200 Ohm

R7:
1.50 kOhm

R10:
499 Ohm

R15:
1.00 kOhm

R17:
42.2 kOhm

The exact population of these resistors depends on the final MagCharge schematic and which EVM features are retained.

## EVM Protection / Auxiliary Components

D2:
BZT52C5V1T-7
5.1 V Zener

Q1:
SQ4949EY-T1_GE3
P-channel MOSFET

These belong to the TI EVM's auxiliary/external-input implementation.

They should not automatically be copied into the compact MagCharge receiver until the final USB-C architecture is defined.

## EVM Output

TI EVM:

5 V
Up to 1 A
5 W BPP

## EVM Test Conditions

TI specifies:

- 5 V transmitter supply
- electronic/resistive load
- 500 mA initial test
- 10 Ohm load
- output verification approximately 4.9 V to 5.1 V
- rectified voltage approximately 5 V to 5.2 V under the documented test setup

## Critical Engineering Rule

The TI EVM values are the starting reference for MagCharge V1.

Before manufacturing the final receiver:

1. verify the selected coil
2. measure the coil in the final mechanical stack
3. verify resonant behavior
4. verify FOD
5. verify current limit
6. verify thermal behavior
7. verify USB-C output behavior
8. verify alignment performance

Do not assume the EVM automatically validates the MagCharge mechanical design.

## Certification

Using the BQ51013C or copying the EVM reference values does not make MagCharge Qi-certified.

The finished product must complete the applicable certification and regulatory process before commercial certification claims are made.

## Primary TI References

BQ51013C product:
https://www.ti.com/product/BQ51013C

BQ51013CEVM:
https://www.ti.com/tool/BQ51013CEVM

BQ51013C datasheet:
https://www.ti.com/lit/ds/symlink/bq51013c.pdf

BQ51013CEVM User's Guide:
https://www.ti.com/lit/ug/sluud57/sluud57.pdf
