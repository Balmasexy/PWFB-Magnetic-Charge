# MagCharge Universal Receiver V1 - TI Verified Reference Values

## Source

Texas Instruments BQ51013C datasheet:

- Document: SLUSFU9A
- Original publication: October 2024
- Revised: May 2025
- Device: BQ51013C
- Package: VQFN20 / RHL

These values are based on the current TI BQ51013C documentation and are
reference starting points for the MagCharge Universal Receiver V1.

They do not constitute production validation or WPC certification.

---

## Receiver IC

U1

Part:
BQ51013CRHLR

Manufacturer:
Texas Instruments

Package:
VQFN20 / RHL

---

## Receiver Coil

Selected MagCharge candidate:

L1:
Würth Electronics 760308103215

Nominal inductance:
14.3 uH

Dimensions:
48 mm x 32 mm

TI listed output-current range:
50 mA - 1000 mA

The final MagCharge mechanical stack must be characterized again.

Required measurements:

- Ls' with the WPC test fixture
- Ls in free space
- Coil DC resistance
- Quality factor Q

The WPC/TI guidance requires Q > 77.

Do not use the TI example resonant values from the 11-uH reference coil
as final MagCharge values.

---

## Resonant Network

C1:
Series resonant capacitor

Status:
TBD after Ls' measurement

C2:
Parallel resonant capacitor

Status:
TBD after Ls measurement

Minimum voltage rating:
25 V

Calculation order:

1. Measure Ls' using the WPC receiver test fixture.
2. Calculate C1 from Ls'.
3. Measure free-space Ls.
4. Calculate C2 using the selected C1 and Ls.
5. Verify resonance and efficiency on the final mechanical stack.

TI's published example uses an 11-uH coil and therefore its example values
must not be copied directly to the MagCharge 14.3-uH coil.

---

## Communication Network

COMM1:
22 nF starting value

COMM2:
22 nF starting value

Minimum voltage rating:
25 V

A 47-nF value may be evaluated only if communication robustness testing of
the final design requires it.

Larger COMM capacitance can strengthen communication but can reduce
efficiency.

---

## Clamp Network

CLAMP1:
0.47 uF starting value

CLAMP2:
0.47 uF starting value

Minimum voltage rating:
25 V

These capacitors support the receiver overvoltage clamping function.

---

## Boot Network

BOOT1:
10 nF starting value

BOOT2:
10 nF starting value

Minimum voltage rating:
25 V

---

## RECT Capacitance

For the TI 1-A IMAX reference:

RECT:
2 x 10 uF + 0.1 uF

Minimum voltage rating:
16 V

The exact capacitor population and PCB designators must follow the final
MagCharge schematic.

---

## OUT Capacitance

For the TI reference:

OUT:
10 uF + 0.1 uF

The exact capacitor population and PCB designators must follow the final
MagCharge schematic.

---

## FOD and Current Limit

ROS:
20 kOhm starting/reference value

RFOD:
196 Ohm starting/reference value

R1:
66 Ohm starting/reference value

Total RILIM:
262 Ohm

Relationship:

RILIM = R1 + RFOD

For IMAX = 1 A, TI's reference design uses:

RILIM = 262 Ohm

This produces approximately a 1.2-A hardware current limit to allow
temporary current surges.

IMPORTANT:

RFOD and ROS require final FOD calibration.

The values above are starting/reference values and must not be represented
as final production-calibrated values.

Good PCB practice is to provide resistor population options for RFOD and ROS
so calibrated values can be fitted without redesigning the board.

---

## TS / Temperature

TS/CTRL should use a properly characterized NTC in the production design.

A 10-kOhm resistor may be used as a test/simulation termination during
prototype evaluation.

R11:
10 kOhm

Status:
Prototype/test only.

The final receiver must validate temperature behavior of:

- RX coil
- BQ51013C
- PCB
- ferrite/shield
- USB-C connector
- surrounding mechanical assembly

---

## Wireless-Only Control Pins

AD:
Tie to PGND for the wireless-only architecture.

AD_EN:
Leave floating.

EN1:
Low/floating during normal wireless operation.

EN2:
Low/floating during normal wireless operation.

The internal pulldowns allow normal wireless operation with EN1 and EN2 low.

The final design may connect EN1/EN2 to a controller if system-level power
control is required.

---

## CHG

CHG is an open-drain charging-status output.

An optional indicator LED may be connected according to the TI reference
application.

Example TI reference:
2.1-V LED with 1.5-kOhm series resistor.

Status:
Optional.

---

## EVM-Only / Architecture-Dependent Components

The following components from TI EVM configurations must not automatically
be copied into the compact MagCharge Universal Receiver:

- EVM-specific input multiplexing components
- external PMOS circuitry
- EVM protection/auxiliary circuitry
- EVM-specific resistor networks
- EVM-specific resonant capacitor populations
- EVM-specific test components

Examples previously documented include:

D2:
BZT52C5V1T-7 5.1-V Zener

Q1:
SQ4949EY-T1_GE3 P-channel MOSFET

These may be required only if the final MagCharge architecture uses the
corresponding wired-input or power-multiplexing function.

---

## TI Reference Output

Reference application:

5 V output

Maximum normal output current:
1 A

Reference power:
5 W

The MagCharge Universal Receiver V1 target remains:

5 V / 1 A maximum prototype output.

Higher-power versions require a separate validated design.

---

## PCB / Layout Requirements

TI requires special attention to:

- Very short AC1 and AC2 power paths
- Resonant capacitors close to the receiver IC
- COMM capacitors close to the receiver IC
- CLAMP capacitors close to the receiver IC
- BOOT capacitors close to the receiver IC
- High-frequency bypass capacitors close to RECT and OUT
- Minimal ILIM/FOD sensing loops
- Quiet routing of sensing signals
- Ground plane with appropriate vias
- Thermal connection of the exposed pad to PGND

For the 1-A reference application, TI lists approximately:

AC1:
1.2 A

AC2:
1.2 A

OUT:
1 A

RECT:
100 mA RMS

COMM1/COMM2:
300 mA

CLAMP1/CLAMP2:
500 mA

Other low-power signals:
10 mA or less

These are design-reference current ratings and must be reviewed against the
final PCB geometry and thermal design.

---

## Receiver Coil Characterization Fixture

TI/WPC reference conditions:

Primary shield:
50 mm x 50 mm x 1 mm ferrite

Example ferrite:
TDK PC44

Fixture gap:
3.4 mm

Measurement:
1 V RMS

Measurement frequency:
100 kHz

Measure:

Ls':
Coil inductance with the specified fixture

Ls:
Free-space coil inductance

The final MagCharge mechanical stack must be represented during the
appropriate measurements.

---

## Production Validation Status

Current status:

NOT PRODUCTION VALIDATED

Still required:

- Resonant-network calculation
- Coil characterization
- FOD calibration
- Current-limit validation
- Thermal testing
- USB-C output testing
- Foreign-object testing
- Alignment testing
- Efficiency measurement
- Load/transient testing
- EMC/EMI evaluation
- Safety review
- WPC/Qi compliance assessment as applicable

The Android application and BLE telemetry must never be treated as the
primary safety mechanism.

Hardware protection must remain functional without the Android application.
