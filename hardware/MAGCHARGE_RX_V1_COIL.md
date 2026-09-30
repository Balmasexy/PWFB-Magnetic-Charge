# MagCharge Universal Receiver V1 - Coil Specification

## Purpose

Define the initial requirements for the wireless-power receiver coil used by the MagCharge Universal Receiver V1.

## Target Geometry

Initial mechanical target:

- Approximately 48 x 32 mm class
- Low profile
- Flexible or thin rigid construction
- Ferrite backed

These dimensions are preliminary. The final coil must be selected from the validated receiver IC reference design.

## Electrical Requirements

The selected coil must be compatible with:

- Receiver IC operating frequency
- Required inductance
- Required Q factor
- Compensation network
- Coupling requirements
- Target 5W power level
- Thermal limitations

The coil must not be selected based only on physical dimensions.

## Mechanical Stack

Phone / phone case
        |
Insulating layer
        |
Receiver PCB or flex
        |
Ferrite shielding
        |
Qi RX coil
        |
Magnetic alignment ring
        |
Protective outer layer

## Ferrite

A suitable ferrite layer should be placed behind the receiver coil according to the selected receiver reference design.

The ferrite should:

- support magnetic coupling
- reduce unwanted magnetic interaction
- fit within the mechanical thickness target
- tolerate the expected temperature

## Magnetic Alignment

The magnetic ring provides physical alignment between the receiver and transmitter.

The magnets do not transfer charging power.

The magnetic system must be tested to ensure it does not negatively affect:

- coil coupling
- receiver efficiency
- phone operation
- thermal behavior

## Coil Validation

Measure and validate:

- inductance
- Q factor
- resistance
- operating frequency
- received power
- efficiency
- temperature rise

Test the coil with the exact receiver IC and compensation network intended for the prototype.

## Alignment Tests

Test:

1. Perfect center alignment
2. Horizontal offset
3. Vertical offset
4. Rotational offset
5. Different phone-case thicknesses

Record:

- output voltage
- output current
- received power
- charging stability
- coil temperature

## Selection Rule

The production coil must come from a validated receiver design or be electrically characterized and validated against the selected receiver IC.

Do not manufacture the final receiver using approximate coil specifications alone.

## V1 Objective

The V1 coil should provide reliable 5W-class wireless power reception while maintaining a thin accessory profile and controlled temperature.

## Future Development

Future versions may investigate:

- thinner coils
- larger active area
- improved efficiency
- 10W operation
- 15W operation
- Qi2-compatible receiver architecture
