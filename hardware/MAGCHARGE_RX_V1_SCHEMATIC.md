# MagCharge Universal Receiver V1 - Schematic Specification

## Purpose

Define the electrical architecture for the first 5W-class MagCharge Universal Receiver prototype.

This document is an engineering specification. Final component values and PCB layout must follow the selected receiver IC manufacturer's validated reference design.

## Power Path

MagCharge Qi Transmitter
        |
        v
      RX Coil
        |
        v
   Receiver IC
        |
        v
   Regulated 5V
        |
        v
 Protection / Current Limit
        |
        v
     USB-C
        |
        v
    Android Phone

## Main Blocks

### 1. Wireless Receiver Coil

The RX coil receives wireless power from the MagCharge transmitter.

Requirements:

- Qi-compatible receiver coil
- approximately 48 x 32 mm class initial target
- ferrite backing
- low-profile construction
- electrically matched to the selected receiver IC
- validated for the intended operating frequency

The final coil must not be selected using physical dimensions alone.

## 2. Qi Receiver IC

Initial target:

- 5W-class Qi receiver
- regulated 5V output
- integrated rectification where supported
- over-voltage protection
- over-current protection
- thermal protection
- foreign-object detection where supported

A BQ51013C-class receiver architecture may be evaluated for the V1 prototype.

The exact IC and reference design must be confirmed before PCB fabrication.

## 3. Rectification and Regulation

The receiver IC converts the AC power induced in the coil into regulated DC power.

Target:

- nominal output: 5V
- V1 target current: up to 1A
- target power: approximately 5W

Use the manufacturer's recommended rectifier, compensation, filtering and regulation network.

Do not substitute arbitrary passive values.

## 4. Protection

The receiver output must include appropriate protection for:

- over-current
- short circuit
- over-voltage
- over-temperature
- reverse current where applicable
- ESD at the USB-C interface

Protection must operate independently of the Android application.

## 5. Temperature Monitoring

Include an NTC or equivalent temperature-sensing method where supported by the receiver architecture.

Suggested monitoring points:

- RX coil
- receiver IC
- PCB hot spot
- USB-C connector

Temperature monitoring may later be exposed through BLE telemetry.

## 6. USB-C Output

USB-C operates as a power source to the phone.

V1 target:

- 5V nominal
- up to 1A target
- USB-PD not implemented
- correct USB-C source-role CC configuration
- protected power rail

The USB-C connector should have suitable mechanical strain relief.

## 7. Test Points

Provide accessible test points for:

- RX coil / AC input where practical
- receiver IC output
- regulated 5V
- ground
- temperature sensor
- current measurement
- USB-C VBUS

Test points should be positioned so that electrical measurements can be performed without disturbing the coil.

## 8. Optional BLE Telemetry

BLE is optional for V1.

If included, the BLE MCU may monitor:

- receiver temperature
- output voltage
- output current
- estimated power
- fault status
- receiver identification

BLE must not control or replace the primary hardware safety mechanisms.

## 9. Grounding

Use a controlled PCB ground strategy according to the selected receiver IC reference design.

Keep high-current paths short and wide.

Keep sensitive measurement and communication traces away from noisy wireless-power switching nodes where practical.

## 10. Mechanical Stack

Phone / Case
        |
Insulation
        |
Receiver PCB / Flex
        |
Ferrite
        |
RX Coil
        |
Magnetic Alignment Ring
        |
Protective Layer

The final mechanical stack must be validated for:

- coil coupling
- temperature
- charging efficiency
- magnetic alignment
- phone compatibility
- case thickness

## 11. Prototype Acceptance

Before connecting a production phone, verify using laboratory equipment:

1. regulated output voltage
2. output current
3. output power
4. thermal behavior
5. protection behavior
6. coil alignment tolerance
7. USB-C electrical behavior

The prototype must not be treated as a certified Qi/Qi2 product.

## 12. Design Rule

The final schematic must be derived from the selected receiver IC's official reference design.

This specification defines the system architecture but does not replace the manufacturer's schematic, layout guidance, or certification requirements.
