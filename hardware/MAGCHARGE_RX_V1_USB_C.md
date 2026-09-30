# MagCharge Universal Receiver V1 - USB-C Output

## Role

The receiver's USB-C connector operates as a power source to the Android phone.

## V1 Target

Voltage: 5V nominal
Target current: up to 1A
USB-PD: Not implemented in V1

## Requirements

- correct USB-C source-role configuration
- correct CC pull-up implementation
- protected 5V rail
- appropriate current limiting
- short-circuit protection
- ESD protection where required
- mechanical strain relief

## Prototype

A known-good USB-C source-role breakout may be used for early testing.

After electrical behavior is proven, integrate the USB-C connector into the receiver PCB/flex design.

## Validation

Test:

- no-load voltage
- normal phone load
- electronic-load maximum target
- connector temperature
- cable/connector mechanical stress
- short-circuit response
- reverse-current behavior
