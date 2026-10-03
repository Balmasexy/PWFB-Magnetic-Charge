# MagCharge Universal Receiver V1 — Resonant Network Measurement

## Purpose

Determine the production values of:

- C_RX1 = series resonant capacitor (Cs)
- C_RX2 = parallel resonant capacitor (Cd)

for the BQ51013C receiver and Würth 760308103215 receiver coil.

The schematic must keep both values as `TBD` until the required measurements and validation are completed.

## Reference

Texas Instruments BQ51013C datasheet, section 9.2.1.2.2:

- Series resonance frequency: 100 kHz +5/-10%
- Parallel resonance frequency: 1 MHz ±10%
- Measurement voltage: 1 Vrms
- Ls' = inductance measured with the WPC test fixture
- Ls = free-space inductance

## Coil

Manufacturer: Würth Elektronik

Part number: 760308103215

Nominal inductance: 14.3 uH

Dimensions: 48 mm x 32 mm

Application: General 5-V power supply

Nominal output-current range: 50 mA - 1000 mA

The 14.3 uH nominal value must NOT be used as a substitute for the required Ls/Ls' measurements.

## Required Measurements

### 1. Ls'

Measure the coil in the final intended mechanical configuration using the WPC-style test fixture:

- Primary ferrite: 50 mm x 50 mm x 1 mm
- Ferrite material: TDK PC44
- Coil/system placed as it will be used in the final product
- Fixture gap dZ: 3.4 mm
- Measurement voltage: 1 Vrms
- Measurement frequency: 100 kHz

Record:

    Ls' = ______ uH

### 2. Ls

Repeat the measurement without the WPC test fixture.

- Measurement voltage: 1 Vrms
- Measurement frequency: 100 kHz

Record:

    Ls = ______ uH

### 3. Coil DC resistance

Measure the coil DC resistance.

Record:

    Rdc = ______ mOhm

## Calculations

### Series capacitor Cs

Use:

    Cs = 1 / ((2*pi*fS)^2 * Ls')

where:

    fS = 100 kHz

The result becomes the target value for:

    C_RX1 = Cs

### Parallel capacitor Cd

After selecting the practical Cs value, calculate Cd using the BQ51013C dual-resonant equation.

The result becomes the target value for:

    C_RX2 = Cd

## Capacitor Requirements

Both resonant capacitors:

- Minimum voltage rating: 25 V
- Must use practical standard values
- Parallel combinations are acceptable where required
- Final values must be validated experimentally

## Quality Factor

Calculate:

    Q = (2*pi*fD*Ls) / R

where:

    fD = 1 MHz
    R = measured DC resistance

TI requires:

    Q > 77

Record:

    Q = ______

## Validation Before Finalizing the Schematic

After selecting practical capacitor values:

1. Verify resonance.
2. Verify 5-V output regulation.
3. Verify output current capability.
4. Verify receiver efficiency.
5. Verify coil temperature.
6. Verify receiver IC temperature.
7. Verify operation with the intended magnetic alignment ring.
8. Verify operation with intended ferrite/shielding.
9. Test centered alignment.
10. Test horizontal offset.
11. Test vertical offset.
12. Test rotational offset.
13. Test intended phone-case thicknesses.
14. Perform FOD calibration.
15. Perform USB-C output/load testing.

## Current Status

C_RX1 / Cs:

    TBD

C_RX2 / Cd:

    TBD

Ls':

    NOT MEASURED

Ls:

    NOT MEASURED

Rdc:

    NOT MEASURED

Q:

    NOT MEASURED

## Important

Do not fabricate the production receiver using the nominal 14.3 uH coil value alone.

Do not replace C_RX1 or C_RX2 `TBD` values in the KiCad schematic until the physical coil/stack measurements and subsequent receiver validation are complete.
