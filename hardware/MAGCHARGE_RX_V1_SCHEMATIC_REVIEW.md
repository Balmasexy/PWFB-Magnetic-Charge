# MagCharge Universal Receiver V1 — Schematic Review & Fabrication Gate

## 1. Purpose

This document defines the review gates that must be completed before the MagCharge Universal Receiver V1 schematic is released for PCB layout or fabrication.

## 2. Reference Design Verification

Verify directly against the current TI BQ51013C documentation:

- [ ] BQ51013CRHLR part number
- [ ] VQFN-20 footprint
- [ ] Pin numbering
- [ ] Pin functions
- [ ] Exposed-pad connection
- [ ] RX coil connection
- [ ] Resonant capacitor network
- [ ] FOD network
- [ ] ILIM network
- [ ] TS network
- [ ] Output network
- [ ] Protection network
- [ ] Recommended PCB layout

No undocumented pin connection should be fabricated.

## 3. Component Verification

Check every component against the verified BOM:

- [ ] U1 BQ51013CRHLR
- [ ] L1 RX coil
- [ ] C1–C20
- [ ] R1
- [ ] R2
- [ ] R4
- [ ] R7
- [ ] R10
- [ ] R15
- [ ] R17
- [ ] D2
- [ ] Q1

Verify:

- value
- tolerance
- voltage rating
- dielectric
- package
- manufacturer part number
- availability

## 4. Coil Verification

Confirm:

- [ ] 48 × 32 mm target geometry
- [ ] approximately 14.3 µH reference inductance
- [ ] resistance specification
- [ ] ferrite backing
- [ ] coil orientation
- [ ] connector/terminal arrangement
- [ ] final mechanical stack

The final coil must be characterized in the actual MagCharge assembly.

## 5. Resonant Network Gate

Do not change resonant components simply to fit the PCB.

If any of the following changes:

- coil
- ferrite
- magnetic ring
- spacing
- PCB material
- enclosure

then re-check:

- resonance
- input behavior
- output voltage
- efficiency
- thermal behavior
- FOD

## 6. FOD Gate

FOD must be tested with the final:

- coil
- ferrite
- magnetic ring
- PCB
- enclosure
- phone/case spacing

Test conditions must include appropriate foreign-object and abnormal-condition scenarios.

## 7. Thermal Gate

Measure:

- RX coil temperature
- BQ51013C temperature
- PCB temperature
- protection-component temperature
- USB-C connector temperature
- representative phone/case temperature

Test at:

- low load
- medium load
- maximum intended load
- misalignment
- extended duration

## 8. USB-C Gate

Verify:

- [ ] VBUS = approximately 5 V
- [ ] correct source-role CC configuration
- [ ] CC1
- [ ] CC2
- [ ] ESD protection
- [ ] short-circuit behavior
- [ ] reverse-current behavior
- [ ] connector mechanical strength
- [ ] voltage drop under load

V1 does not require USB-PD negotiation.

## 9. Electrical Bench Gate

Initial validation must use an electronic load.

Do not begin with a phone.

Test:

```text
Qi transmitter
      ↓
MagCharge receiver
      ↓
5 V output
      ↓
Electronic load
