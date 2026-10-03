# MAGCHARGE RX V1 — USB-C Output Protection

## Power path

+5V_RX
  -> FUSE1
  -> U_USB_PROTECT / BD2242G
  -> VBUS_PROTECTED
  -> USB-C VBUS

## Protection IC

Part: ROHM BD2242G-GTR
Package: SSOP6
Supply: +5V_RX
Control: Active-high
IN: +5V_RX
OUT: VBUS_PROTECTED
GND: PGND
EN: +5V_RX
ILIM: R_USB_ILIM to PGND
OC: optional fault monitor

## Current limit

Target typical threshold: 1.000 A
RLIM: 20.57 kOhm
Recommended tolerance: 1%

Datasheet table:
20.57 kOhm -> 884 mA min / 1000 mA typ / 1116 mA max

Place RLIM as close to BD2242G as practical.

## USB-C CC

J1 is a USB-C source.

CC1 -> Rp
CC2 -> Rp

Initial conservative implementation:
Rp1 = 56 kOhm, 1%
Rp2 = 56 kOhm, 1%

This advertises Default USB Power.

Do NOT advertise 1.5 A unless the final source power budget and protection design
are explicitly validated for that advertised capability.

## VBUS protection

ESD1:
VBUS_PROTECTED -> PGND

FUSE1:
+5V_RX -> BD2242G input

BD2242G:
+5V_RX -> VBUS_PROTECTED

## Status

BD2242G candidate: VERIFIED
RLIM = 20.57 kOhm: VERIFIED
EN active-high: VERIFIED
USB-C Rp values: VERIFIED against Type-C source termination requirements
Physical USB-C connector: footprint still TBD
ESD: selection TBD
Fuse: selection TBD
PCB thermal/layout: TBD
ERC: pending KiCad-capable environment
USB-C compliance: not yet claimed

## CC implementation

R_USB_CC1 = 56 kOhm from +5V source rail to CC1.
R_USB_CC2 = 56 kOhm from +5V source rail to CC2.

These values represent Default USB Power source advertisement.
The design must not claim 1.5-A USB-C source capability unless changed to the
appropriate Rp implementation and the complete source power path is validated.

A future integrated USB-C source controller such as TI TPS25821 may be evaluated
if automatic CC attach/detach handling or stronger Type-C integration is required.
TPS25821 integrates a Type-C source controller and 1.5-A-rated power switch.
