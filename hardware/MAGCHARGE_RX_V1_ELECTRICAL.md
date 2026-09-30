# MagCharge Universal Receiver V1 - Electrical Design

## 1. Electrical Objective

Design a compact Qi-compatible wireless receiver that converts received wireless power into regulated 5V USB-C power for Android phones.

V1 target power: approximately 5W.

## 2. Power Architecture

Qi transmitter
    |
    v
RX coil
    |
    v
Qi receiver IC
    |
    +--> Rectification
    |
    +--> Regulation
    |
    +--> Protection
    |
    v
5V power rail
    |
    v
USB-C source connector
    |
    v
Android phone

## 3. Receiver IC

Initial architecture:

TI BQ51013C-class Qi receiver or an approved equivalent.

The final IC must be selected from a currently available component and its manufacturer's reference design must be followed.

Do not invent the resonant network or compensation values.

## 4. Output Target

Nominal output:

5V DC

Initial target:

Up to 1A

Target prototype power:

Approximately 5W

The actual continuous output must be limited by the selected receiver IC, coil, thermal design and USB-C implementation.

## 5. Protection

The receiver design should provide the protection functions supported by the selected receiver IC/reference design, including:

- over-voltage protection
- over-current protection
- short-circuit protection
- thermal protection
- foreign-object detection where supported

Protection must operate independently of the Android application.

## 6. Thermal Monitoring

Include an NTC or equivalent temperature-sensing method according to the selected receiver reference design.

Monitor during validation:

- RX coil temperature
- receiver IC temperature
- PCB temperature
- USB-C connector temperature

## 7. Test Points

Provide accessible test points for:

- 5V output
- ground
- current measurement
- receiver status where available
- temperature/NTC signal where available

## 8. PCB Layout

Follow the selected receiver IC manufacturer's reference layout.

Important principles:

- keep high-current paths short
- use adequate copper width
- minimize unnecessary loop area
- maintain the recommended coil-to-IC arrangement
- keep sensitive control signals away from noisy power paths
- provide adequate thermal copper where recommended
- maintain required clearances

## 9. Receiver Coil

The receiver coil must be electrically matched to the selected receiver IC and compensation network.

The coil must not be selected only by physical dimensions.

Validate:

- inductance
- Q factor
- operating frequency
- coupling
- temperature rise
- efficiency

## 10. USB-C Output

V1 USB-C operates as a power source.

USB Power Delivery is not implemented in V1.

Use the appropriate USB-C source-role configuration and CC pull-up arrangement.

## 11. Bench Validation

Before connecting a phone:

1. Place receiver on a known-good Qi transmitter.
2. Measure output voltage.
3. Connect an electronic load.
4. Increase load gradually.
5. Measure current and power.
6. Monitor receiver temperature.
7. Verify protection behavior.

Use an electronic load for initial fault testing rather than a phone.

## 12. Acceptance Criteria

The V1 electrical prototype should demonstrate:

- stable wireless power reception
- stable regulated 5V output
- target output power near 5W where supported
- controlled temperature
- correct protection behavior
- stable operation during normal alignment
- acceptable behavior during moderate misalignment

## 13. Engineering Warning

This document is not a manufacturing schematic.

The final schematic, PCB layout, coil and passive component values must be based on the exact receiver IC and manufacturer reference design selected for the production prototype.

Do not manufacture a production PCB from this document alone.
