# MagCharge Universal Receiver V1 — Component BOM

## Status

Engineering reference BOM for the MagCharge Universal Receiver V1 prototype.

This BOM uses the verified component values from the TI BQ51013C evaluation-module reference design where applicable.

**Important:** These are reference-design values, not a final production BOM. The receiver coil, resonant network, FOD network, thermal behavior, magnetic stack, and mechanical construction must be re-characterized for the final MagCharge product.

---

## 1. Wireless Power Receiver

| Ref | Component | Value / Part | Package | Qty | Status |
|---|---|---|---|---:|---|
| U1 | Wireless power receiver IC | TI BQ51013CRHLR | VQFN-20 | 1 | Verified TI reference |
| L1 | Qi receiver coil | Würth 760308103215 | 48 × 32 mm | 1 | Verified TI EVM |
| C1 | Resonant capacitor | 68 nF, 50 V, X7R | 0603 | 1 | Verified TI EVM |
| C2 | Resonant capacitor | 68 nF, 50 V, X7R | 0603 | 1 | Verified TI EVM |
| C3 | Resonant capacitor | 47 nF, 50 V, X7R | 0603 | 1 | Verified TI EVM |
| C4 | Resonant capacitor | 1.8 nF, 50 V, C0G/NP0 | 0603 | 1 | Verified TI EVM |
| C5 | Resonant capacitor | 100 pF, 100 V, C0G/NP0 | 0603 | 1 | Verified TI EVM |

### Coil reference

Würth 760308103215:

- Approximate size: 48 × 32 mm
- Inductance: 14.3 µH
- Maximum resistance: 190 mΩ
- Must be re-characterized with the final ferrite, magnetic ring, adhesive, case/phone spacing and PCB stack.

---

## 2. Receiver IC Support Capacitors

| Ref | Component | Value | Rating / Dielectric | Qty |
|---|---|---:|---|---:|
| C6 | Ceramic capacitor | 100 nF | 50 V X7R | 1 |
| C7 | Ceramic capacitor | 1 µF | 50 V X7R | 1 |
| C8 | Ceramic capacitor | 22 nF | 50 V X7R | 1 |
| C9 | Ceramic capacitor | 470 nF | 25 V X7R | 1 |
| C10 | Ceramic capacitor | 10 nF | 50 V X7R | 1 |
| C11 | Ceramic capacitor | 10 nF | 50 V X7R | 1 |
| C12 | Ceramic capacitor | 470 nF | 25 V X7R | 1 |
| C13 | Ceramic capacitor | 22 nF | 50 V X7R | 1 |
| C14 | Ceramic capacitor | 10 µF | 35 V X7R | 1 |
| C15 | Ceramic capacitor | 10 µF | 35 V X7R | 1 |
| C16 | Ceramic capacitor | 100 nF | 50 V X7R | 1 |
| C17 | Ceramic capacitor | 1 µF | 50 V X7R | 1 |
| C18 | Ceramic capacitor | 100 nF | 50 V X7R | 1 |
| C19 | Ceramic capacitor | 100 nF | 50 V X7R | 1 |
| C20 | Ceramic capacitor | 1 µF | 50 V X7R | 1 |

---

## 3. FOD and Current-Limit Components

| Ref | Component | Value | Package | Status |
|---|---|---:|---|---|
| R17 | FOD resistor | 42.2 kΩ, 1% | 0603 | Verified TI EVM |
| R4 | ILIM resistor | 110 Ω, 1% | 0603 | Verified TI EVM |
| R11 | TS simulation resistor | 10 kΩ | 0603 | EVM test configuration |

### Production note

R11 must not automatically be copied into production.

The final product should use a properly characterized temperature-sensing element/NTC and validate the complete thermal response of:

- RX coil
- receiver IC
- PCB
- ferrite
- magnetic ring
- USB-C connector
- attached phone/case

The FOD network must also be re-validated with the final coil and mechanical stack.

---

## 4. Additional Resistors

| Ref | Component | Value | Tolerance | Package | Status |
|---|---|---:|---:|---|---|
| R1 | Resistor | 10 kΩ | 1% | 0603 | Verified TI EVM |
| R2 | Resistor | 200 Ω | 1% | 0603 | Verified TI EVM |
| R7 | Resistor | 1.50 kΩ | 1% | 0603 | Verified TI EVM |
| R10 | Resistor | 499 Ω | 1% | 0603 | Verified TI EVM |
| R15 | Resistor | 1.00 kΩ | 1% | 0603 | Verified TI EVM |

---

## 5. Protection Components

| Ref | Component | Part | Function | Status |
|---|---|---|---|---|
| D2 | Zener diode | BZT52C5V1T-7 | 5.1 V protection | Verified TI EVM |
| Q1 | P-channel MOSFET | SQ4949EY-T1_GE3 | Output/protection switching | Verified TI EVM |

Additional protection may be required after prototype testing depending on the final USB-C implementation.

---

## 6. USB-C Output

### V1 target

- Output voltage: 5 V nominal
- Target current: up to 1 A
- Target power: approximately 5 W
- USB-C connector: male plug / short flex-tail implementation
- USB-C role: source
- Correct CC source resistors required
- No USB-PD negotiation in V1
- Reverse-current protection required
- Short-circuit protection required
- ESD protection required

The exact USB-C connector and CC implementation should be selected after the mechanical prototype dimensions are frozen.

---

## 7. Thermal Sensor

### Prototype

Use the TI EVM's 10 kΩ TS simulation arrangement only for bench validation where appropriate.

### Production

Use a characterized NTC positioned to monitor the thermally critical area.

Candidate location:

```text
         PHONE / CASE
              │
        ┌─────┴─────┐
        │ RX COIL   │
        │           │
        │    NTC ●  │
        └───────────┘
              │
        RECEIVER PCB
