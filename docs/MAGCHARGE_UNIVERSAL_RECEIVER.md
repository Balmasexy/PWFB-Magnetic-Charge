# MagCharge Universal Receiver V1

## Purpose

A thin magnetic wireless-power receiver accessory for Android phones without built-in wireless charging.

The receiver accepts Qi-compatible wireless power and converts it to regulated 5V USB-C output.

## V1 Target

- Qi-compatible wireless input
- 5W prototype target
- 5V nominal output
- Up to 1A target output
- USB-C male connector
- Magnetic alignment ring
- Low-profile Qi receiver coil
- Ferrite shielding
- NTC thermal monitoring
- Hardware over-voltage, over-current, short-circuit and thermal protection
- Target size: approximately 60 x 40 mm
- Target thickness: approximately 3-4 mm
- Optional BLE telemetry in future versions

## Architecture

Qi/MagCharge transmitter
        |
        v
RX coil
        |
        v
Qi receiver IC
        |
        v
Protection / regulation
        |
        v
5V USB-C
        |
        v
Android phone

## Receiver IC

The first prototype should use a proven Qi receiver reference design.

A TI BQ51013C-class receiver is a suitable starting architecture for a 5W prototype.

The exact receiver IC, coil, compensation network and passive values must follow the selected manufacturer's reference design.

## USB-C

USB-C operates as a power-source output.

V1 does not implement USB Power Delivery.

The connector must use the correct USB-C source-role and CC configuration.

## Mechanical Stack

Phone / case
    |
Insulation
    |
Receiver PCB or flex
    |
Ferrite
    |
Qi RX coil
    |
Magnetic alignment ring
    |
Protective film

## Compatibility

V1 targets Android phones that:

- use USB-C
- accept 5V USB charging
- do not have native wireless charging

The receiver is an external accessory. It does not add native wireless charging hardware to the phone.

## App Integration

The MagCharge Android app should distinguish:

1. Native Wireless Charging
2. MagCharge Universal Receiver
3. USB Cable
4. Not Charging

Android may report Universal Receiver charging as USB charging because the receiver converts wireless power to 5V USB.

Future BLE telemetry may report:

- temperature
- voltage
- current
- estimated power
- receiver ID
- fault status

BLE must never be the only safety mechanism.

## Safety

Safety-critical protection must remain in hardware and/or receiver firmware.

The Android application must not be required to prevent overheating, over-current, short circuits, foreign-object conditions or unsafe power regulation.

## Development Stages

### Stage 1 - Bench Proof

Use a proven Qi transmitter, receiver module, matching coil, USB-C source breakout, electronic load and temperature measurement.

### Stage 2 - MagCharge Test

MagCharge puck -> Universal Receiver -> USB-C -> Android phone.

Test centered and moderate-offset alignment.

### Stage 3 - Prototype PCB

Create a compact PCB following the selected receiver IC reference layout.

### Stage 4 - Mechanical Prototype

Integrate the coil, ferrite, magnetic ring, PCB, USB-C connector and protective enclosure.

### Stage 5 - Thermal Validation

Measure coil, receiver IC, PCB, USB-C and phone temperatures.

### Stage 6 - Electrical Validation

Test normal load, maximum intended load, misalignment, short circuit, over-temperature and foreign-object behavior.

### Stage 7 - Certification

Before commercial launch, perform applicable electrical, EMC, thermal, mechanical and wireless-power certification/testing.

Do not claim Qi or Qi2 certification until the final product has completed the applicable certification process.

## Acceptance Criteria

The prototype must demonstrate:

- stable wireless power reception
- regulated 5V USB-C output
- reliable Android charging
- stable normal alignment
- acceptable moderate misalignment
- controlled thermal behavior
- functioning hardware protection
- no abnormal heating, smoke, damage or instability

## Engineering Note

Exact coil characteristics, resonant/compensation components and passive values must come from the selected receiver IC reference design.

This document is an engineering architecture and prototype specification, not a certified manufacturing drawing.

## Future V2

Potential improvements:

- 10W
- 15W
- improved efficiency
- thinner flex PCB
- BLE telemetry
- temperature/current/power reporting
- improved magnetic alignment
- evaluation of Qi2-compatible architecture
