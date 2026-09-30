# MagCharge Universal Receiver V1 — Engineering BOM

## Status

Engineering prototype BOM based on the Texas Instruments BQ51013C
datasheet (SLUSFU9A, revised May 2025) and the MagCharge V1
pin-accurate receiver netlist.

**NOT production validated.**
**NOT a fabrication release.**
**NOT WPC certification.**

Final component values require receiver characterization,
FOD calibration, thermal testing, electrical validation and applicable
WPC/Qi compliance work.

---

## 1. Receiver Core

| Ref | Component | Manufacturer / Part | Value / Specification | Status |
|---|---|---|---|---|
| U1 | Qi receiver IC | Texas Instruments BQ51013CRHLR | BQ51013C, VQFN20/RHL | Preferred V1 device |
| L1 | Receiver coil | Würth Elektronik 760308103215 | 14.3 µH nominal, 48 × 32 mm | Starting coil |
| SH1 | Ferrite shield | TBD | Thin flexible ferrite suitable for Qi receiver stack | TBD |
| MR1 | Magnetic alignment ring | TBD | Thin permanent-magnet ring | Prototype/mechanical TBD |

The receiver coil, ferrite, compensation network and mechanical stack
must be validated as one magnetic system.

---

## 2. Resonant Network

The final resonant values must be calculated from measured coil
parameters in the final mechanical stack.

| Ref | Function | Value | Status |
|---|---|---:|---|
| C_RX1 | Series resonant capacitor Cs | TBD | Requires measured Ls' |
| C_RX2 | Parallel resonant capacitor Cd | TBD | Requires measured Ls and C_RX1 |

Minimum starting voltage rating:

- 25 V minimum
- use suitable low-loss ceramic capacitors
- final dielectric/package selected during validation

### Required characterization

Measure:

- Ls'
- Ls
- DC resistance
- Q factor
- resonance
- receiver efficiency

For Ls':

- WPC v1.3 receiver coil test fixture
- 50 × 50 × 1 mm TDK PC44 ferrite primary shield
- dZ = 3.4 mm
- 1 Vrms
- 100 kHz

Calculate:

C1 = 1 / ((2*pi*fS)^2 * Ls')

where fS = 100 kHz (+5% / -10%).

Then:

C2 = 1 / ((2*pi*fD)^2 * Ls - 1/C1)

where fD = 1 MHz (+/-10%).

The final values must not be copied from the TI 11-µH example.

---

## 3. BQ51013C Support Network

| Ref | Function | Value | Voltage / Type | Status |
|---|---|---:|---|---|
| C_BOOT1 | BOOT1 capacitor | 10 nF | 25 V minimum | TI starting value |
| C_BOOT2 | BOOT2 capacitor | 10 nF | 25 V minimum | TI starting value |
| C_COMM1 | COMM1 capacitor | 22 nF | 25 V minimum | TI starting value |
| C_COMM2 | COMM2 capacitor | 22 nF | 25 V minimum | TI starting value |
| C_CLAMP1 | AC1 clamp capacitor | 0.47 µF | 25 V minimum | TI starting value |
| C_CLAMP2 | AC2 clamp capacitor | 0.47 µF | 25 V minimum | TI starting value |

---

## 4. RECT and OUT Filtering

| Ref | Function | Value | Voltage | Status |
|---|---|---:|---:|---|
| C_RECT1 | RECT reservoir | 10 µF | 16 V minimum | Reference starting value |
| C_RECT2 | RECT reservoir | 10 µF | 16 V minimum | Reference starting value |
| C_RECT3 | RECT bypass | 0.1 µF | 16 V minimum | Reference starting value |
| C_OUT1 | OUT reservoir | 10 µF | 10 V minimum | Prototype starting value |
| C_OUT2 | OUT bypass | 0.1 µF | 10 V minimum | Prototype starting value |

Final voltage ratings must include appropriate derating.

---

## 5. FOD and Current Limit

| Ref | Function | Value | Status |
|---|---|---:|---|
| R_ILIM | ILIM resistor R1 | 66 Ω | Starting/reference |
| R_FOD | RFOD | 196 Ω | Starting/reference |
| R_OS | FOD calibration resistor ROS | 20 kΩ | Starting/reference |

The ILIM resistance is:

RILIM = R_ILIM + R_FOD

Therefore:

RILIM = 66 Ω + 196 Ω = 262 Ω

Reference IMAX:

1 A

The TI reference arrangement gives a nominal 1.2 A hardware current
limit, allowing temporary current surges.

Final values require board validation.

### FOD calibration

RFOD and ROS are calibration components.

Provide suitable resistor positions so that final calibrated values
can be fitted after receiver characterization.

ROS is separate from the ILIM resistance path.

---

## 6. Thermal Sensing

| Ref | Component | Value | Status |
|---|---|---:|---|
| NTC1 | Production NTC | TBD | Must be characterized |
| R_TS_TEST | Prototype TS termination | 10 kΩ | Prototype only |

The 10-kΩ resistor is a prototype/test termination and must not be
treated as the final production thermal sensor.

NTC placement must monitor the thermally critical receiver area.

---

## 7. CHG Status

| Ref | Function | Value | Status |
|---|---|---:|---|
| TP_CHG | CHG_STATUS test point | — | Recommended |

The BQ51013C CHG output is open-drain.

An LED indicator may be added after the core receiver electrical
design is validated.

---

## 8. USB-C Output

### Architecture

V1 uses a **USB-C male plug / short flex-tail** intended to connect
directly to the Android phone.

| Ref | Component | Specification | Status |
|---|---|---|---|
| J1 | USB-C male plug | 5 V source, up to 1 A target | Prototype architecture |
| ESD1 | USB-C ESD protection | Suitable USB ESD device | TBD |
| FUSE1 | Output protection | Current/thermal protection as required | TBD |

USB Power Delivery is not implemented in V1.

The USB-C output must provide:

- protected 5 V
- controlled output current
- short-circuit protection
- reverse-current protection where required
- ESD protection
- mechanical strain relief

A known-good USB-C source-role breakout may be used during prototype
validation before integrating the final flex-tail connector.

---

## 9. Ground and Thermal

U1 pins 1 and 20 and the exposed pad connect to PGND.

The exposed pad requires a low-impedance thermal connection to PGND.

PGND includes:

- U1 ground pins
- U1 exposed pad
- RECT capacitors
- OUT capacitors
- ILIM network
- TS/NTC network
- USB-C ground

---

## 10. Test Points

Recommended prototype test points:

| Ref | Net |
|---|---|
| TP_AC1 | AC1 |
| TP_AC2 | AC2 |
| TP_RECT | RECT |
| TP_OUT | +5V_RX |
| TP_PGND | PGND |
| TP_CHG | CHG_STATUS |
| TP_TS | TS_CTRL |
| TP_FOD | FOD |
| TP_ILIM | ILIM |

Test points must be arranged so that probing does not compromise
the magnetic stack or safety insulation.

---

## 11. Mechanical Materials

| Item | Requirement |
|---|---|
| Ferrite | Thin flexible receiver ferrite |
| Insulation | Electrical insulation between coil/PCB/mechanics |
| Adhesive | Thin electrically safe adhesive |
| Alignment ring | Magnetic alignment only |
| Backing | Protective mechanical layer |
| Flex strain relief | Required around USB-C tail |
| Enclosure/film | Optional prototype protection |

Magnetic material must not interfere with the validated Qi receiver
magnetic stack.

---

## 12. Prototype Laboratory Equipment

Required or recommended:

- known-good Qi transmitter
- MagCharge transmitter/puck
- electronic load
- USB power meter
- multimeter
- temperature probe
- oscilloscope where available
- USB-C breakout
- current/voltage measurement equipment

Initial electrical testing must use an electronic load before
connecting a phone.

---

## 13. Production BOM Requirements

Before production release, every component must have:

- manufacturer
- manufacturer part number
- package
- quantity
- approved substitute
- supplier
- availability
- lifecycle status
- datasheet
- reference-design source
- validated electrical rating
- validated thermal rating

---

## 14. Engineering Gate

The BOM is not production-ready until:

1. The exact BQ51013C implementation is reviewed against the current
   TI datasheet.
2. The selected coil is characterized.
3. Ls' and Ls are measured.
4. C_RX1 and C_RX2 are calculated and experimentally tuned.
5. Q > 77 is verified.
6. FOD is calibrated.
7. Thermal behavior is validated.
8. 5 V / 1 A operation is validated with an electronic load.
9. USB-C source behavior is validated.
10. Short-circuit and protection behavior are validated.
11. The PCB layout follows the receiver IC manufacturer's guidance.
12. Applicable Qi/WPC compliance requirements are addressed.

This BOM is an engineering reference and must not be interpreted as
a manufacturing release.
