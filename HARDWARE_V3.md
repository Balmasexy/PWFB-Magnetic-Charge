# MagCharge V3 Hardware Build Definition

Target: 15W prototype.

## Electrical chain
USB-C PD adapter -> protected PD input -> Qi/Qi2 transmitter reference module -> matched TX coil -> magnetic alignment.

## Intelligence chain
BLE 5.x MCU -> temperature sensor + current/voltage monitor -> GATT telemetry -> MagCharge Android app.

## Receiver
Use a matched Qi/Qi2 receiver reference module and coil. For phones without built-in wireless charging, package the receiver in a thin MagCharge case/receiver accessory. Do not assume a universal receiver fit; phone models must be validated.

## Safety
Use the transmitter/receiver reference design's FOD, thermal and current protections. Do not make BLE or the Android app the primary safety mechanism.

## Public product path
Prototype -> engineering validation -> EMC/electrical/thermal testing -> applicable WPC certification -> manufacturing validation.
