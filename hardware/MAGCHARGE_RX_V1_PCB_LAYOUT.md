# MagCharge Universal Receiver V1 — PCB Layout Specification

## 1. Purpose

This document defines the preliminary PCB/flex-PCB layout requirements for the MagCharge Universal Receiver V1.

The design is based on the TI BQ51013C receiver reference architecture and the verified TI BQ51013CEVM component values documented in:

- `hardware/MAGCHARGE_RX_V1_BQ51013C_REFERENCE.md`
- `hardware/MAGCHARGE_RX_V1_TI_VERIFIED_VALUES.md`
- `hardware/MAGCHARGE_RX_V1_COMPONENT_BOM.md`

This is an engineering layout specification, not a final manufacturing drawing.

---

## 2. Preliminary Mechanical Envelope

Target receiver assembly:

- Overall target: approximately 60 × 40 mm
- Prototype thickness target: approximately 3–4 mm including coil/ferrite/mechanical stack
- RX coil: approximately 48 × 32 mm
- USB-C connection: short flex tail or integrated connector
- Flexible receiver construction preferred for the first thin prototype

The final dimensions must be adjusted after the coil, ferrite, magnetic structure and connector are selected.

---

## 3. Recommended Layer Arrangement

For a thin receiver PCB/flex assembly:

```text
PHONE / PHONE CASE
        │
        ▼
PROTECTIVE INSULATION
        │
        ▼
RX COIL
        │
        ▼
FERRITE SHIELD
        │
        ▼
PCB / FLEX PCB
        │
        ├── BQ51013C
        ├── Resonant network
        ├── Protection
        ├── Thermal sensing
        └── USB-C output
        │
        ▼
PROTECTIVE BACKING
