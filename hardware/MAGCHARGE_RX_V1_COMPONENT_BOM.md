# MagCharge Universal Receiver V1 - Component BOM

## Design Target

Product:
MagCharge Universal Receiver V1

Architecture:
Qi 1.3 / 5W BPP receiver

Target output:
5V nominal
Up to 1A
Approximately 5W

Primary receiver IC:
Texas Instruments BQ51013C

Prototype status:
Engineering prototype - not certified

---

## 1. Wireless Receiver IC

Reference:
U1

Part:
TI BQ51013C

Package:
VQFN-20
4.5 mm x 3.5 mm

Quantity:
1

Function:

- Qi receiver
- synchronous rectification
- regulation
- Qi communication
- FOD
- current sensing
- thermal protection

Source:
Texas Instruments

---

## 2. Receiver Coil

Reference:
L1

Preferred initial candidate:

Manufacturer:
Würth Elektronik

Part:
760308103215

Nominal dimensions:
48 mm x 32 mm

Nominal inductance:
14.3 uH

Target current range:
50 mA - 1A

Quantity:
1

Alternative:

Manufacturer:
XFMRS

Part:
XFMCC483201-143

Dimensions:
48 mm x 32 mm

Nominal inductance:
14.3 uH

Alternative:

Manufacturer:
TDK

Part:
WR483265-15F5-G

Dimensions:
48 mm x 32 mm

Nominal inductance:
approximately 13.3 uH

Important:

The final coil must be electrically characterized in the actual MagCharge mechanical stack.

The measured inductance may change because of:

- ferrite
- magnetic ring
- phone case
- phone/battery
- adhesive
- mechanical spacing

Do not fabricate the final production PCB using catalog inductance alone.

---

## 3. Ferrite Layer

Reference:
F1

Type:
Flexible magnetic shielding ferrite

Target:
Approximately 48 mm x 32 mm class

Quantity:
1

Requirements:

- suitable for wireless-power receiver applications
- compatible with the selected coil
- thin construction
- suitable temperature rating
- mechanically compatible with adhesive/lamination

Final ferrite thickness must be selected during coil validation.

---

## 4. Resonant Capacitors

References:
C1 / C2

Type:
High-quality ceramic capacitors

Minimum voltage rating:
25V

Dielectric:
X7R preferred

Initial value:

C1:
To be calculated/verified from the selected coil and TI reference design.

C2:
To be calculated/verified from the selected coil and TI reference design.

Do not substitute arbitrary values.

The BQ51013C datasheet requires the resonant network to be designed around the selected receiver coil.

---

## 5. BOOT Capacitors

References:
C_BOOT1
C_BOOT2

Initial value:
10 nF

Voltage rating:
Minimum 25V

Dielectric:
X7R preferred

Package:
0402 or 0603 subject to assembly capability

Quantity:
2

Purpose:

Support the internal synchronous-rectifier operation.

Place close to the corresponding BQ51013C pins.

---

## 6. CLAMP Capacitors

References:
C_CLAMP1
C_CLAMP2

Initial value:
0.47 uF

Voltage rating:
Minimum 25V

Dielectric:
X7R preferred

Package:
0603 preferred

Quantity:
2

Purpose:

Support receiver-side over-voltage clamp operation.

Place close to the corresponding BQ51013C pins.

---

## 7. COMM Capacitor

Reference:
C_COMM

Initial value:
22 nF

Voltage rating:
Minimum 25V

Dielectric:
X7R preferred

Quantity:
1

Purpose:

Wireless communication network.

A higher value may be evaluated only according to the TI reference design and communication testing.

---

## 8. Output Capacitors

References:
C_OUT1
C_OUT2

Initial prototype selection:

Type:
Ceramic X7R

Voltage rating:
Minimum 10V

Target capacitance:
Use the value specified by the selected TI reference schematic/EVM.

Quantity:
2

Important:

Do not finalize the exact value until the current EVM schematic revision is checked against the PCB implementation.

---

## 9. NTC Temperature Sensor

Reference:
NTC1

Initial prototype:

10 kOhm NTC

Purpose:

Monitor receiver temperature through the BQ51013C TS/CTRL function.

Quantity:
1

Placement:

Position thermally close to the receiver/coil hot region according to the final mechanical design.

The EVM documentation uses a 10 kOhm temperature-simulation resistor during evaluation; the production prototype should use an appropriate thermistor implementation.

---

## 10. Output Current-Limit Network

Reference:
R_ILIM

Purpose:

Set or limit receiver output current according to the BQ51013C design.

Value:
To be selected from the TI reference design for the desired V1 current limit.

Target:

Approximately 1A maximum prototype output.

Do not select the resistor by guesswork.

---

## 11. USB-C Connector

Reference:
J1

Type:
USB Type-C receptacle or mechanically suitable USB-C output connector

Role:
Power source

V1 output:

5V nominal
Up to 1A target

USB Power Delivery:
Not implemented in V1

Requirements:

- correct USB-C source-role configuration
- appropriate CC pull-up resistors
- protected VBUS
- suitable connector current rating
- ESD protection
- mechanical strain relief

Quantity:
1

---

## 12. USB-C CC Resistors

References:
R_CC1
R_CC2

Function:
USB-C source advertisement

Use the appropriate USB-C source Rp implementation for the V1 5V source design.

Exact resistor value:
Must be selected according to the applicable USB Type-C specification and the desired advertised current.

Quantity:
2

Do not use arbitrary pull resistors.

---

## 13. USB-C ESD Protection

Reference:
D_ESD1

Type:
Low-capacitance USB/ESD protection device suitable for USB-C VBUS/CC interface.

Quantity:
1

Purpose:

Protect the connector/interface from electrostatic discharge.

Final part:
Select according to the PCB and connector implementation.

---

## 14. VBUS Protection

Reference:
F1 / Q_PROTECT

Possible implementation:

- resettable fuse or current-limiting element
- load-switch/current-limit IC
- suitable reverse-current protection

The exact protection architecture must be selected after confirming the USB-C source implementation.

Do not place an unverified protection device in series with the 5V rail without checking voltage drop and thermal dissipation.

---

## 15. BLE Telemetry - Optional

Reference:
U2

V1 status:
OPTIONAL

Function:

- receiver identification
- temperature
- voltage
- current
- estimated power
- fault status

Requirements:

- BLE 5.x
- low power
- hardware-independent safety
- electrically isolated from sensitive Qi switching nodes where practical

The V1 receiver must operate safely without BLE.

---

## 16. BLE Temperature / Current / Voltage Monitoring

If BLE is installed:

Temperature:
NTC1 or dedicated temperature sensor

Voltage:
resistor divider or suitable ADC monitor

Current:
current-sense circuit

Power:
calculated from measured voltage and current

The BLE MCU must only monitor the power system.

It must not be required for:

- Qi negotiation
- over-current protection
- thermal shutdown
- FOD
- short-circuit protection

---

## 17. PCB

Reference:
PCB1

Initial target:

Approximately:
60 mm x 40 mm

Target thickness:
Approximately 1.0 - 1.6 mm PCB before mechanical stack-up.

Requirements:

- controlled Qi receiver layout
- short AC1/AC2 paths
- short high-current paths
- appropriate grounding
- ferrite clearance
- coil alignment
- test points
- USB-C mechanical support

The final PCB layout must follow TI's BQ51013C reference/EVM layout guidance.

---

## 18. Test Points

Required:

TP1:
GND

TP2:
5V output

TP3:
USB-C VBUS

TP4:
AC1

TP5:
AC2

TP6:
Temperature-sense node

Optional:

TP7:
Current measurement

TP8:
BLE supply

---

## 19. Prototype Quantity

Recommended first bench build:

BQ51013C:
3 units

RX coil:
3 units

Ferrite:
3 units

BOOT capacitors:
10 units

CLAMP capacitors:
10 units

COMM capacitors:
10 units

Resistors:
10 units per selected value

NTC:
5 units

USB-C connectors:
5 units

ESD devices:
5 units

PCB:
5 boards minimum

Reason:

The first receiver PCB should not be fabricated as a single unit.

Multiple boards allow:

- assembly mistakes
- coil comparison
- thermal testing
- FOD tuning
- component replacement
- mechanical experiments

---

## 20. Critical Design Dependencies

The following must be verified before final PCB fabrication:

1. Exact BQ51013C package footprint
2. Latest TI reference schematic
3. Latest TI EVM BOM
4. Exact resonant capacitor values
5. Exact output capacitor values
6. Exact current-limit resistor
7. NTC characteristics
8. USB-C source-role implementation
9. Selected coil's measured inductance
10. Coil/ferrite/magnet mechanical stack
11. FOD calibration
12. PCB layout

---

## 21. Prototype Safety

Initial tests must use:

- laboratory power measurement
- electronic load
- temperature measurement
- current measurement
- controlled alignment

Do not perform uncontrolled short-circuit or fault testing using a phone.

Stop testing if there is:

- abnormal heating
- smoke
- component damage
- unstable output
- burning smell
- unexpected current
- damaged connector

---

## 22. Certification Status

The use of the BQ51013C does not by itself make MagCharge a Qi-certified product.

The final commercial receiver must complete the applicable Wireless Power Consortium certification process before being marketed as Qi-certified.

---

## 23. Primary References

Texas Instruments BQ51013C:
https://www.ti.com/product/BQ51013C

Texas Instruments BQ51013C Evaluation Module:
https://www.ti.com/tool/BQ51013CEVM

Texas Instruments BQ51013C-Q1 Evaluation Module:
https://www.ti.com/tool/BQ51013C-Q1EVM

Texas Instruments BQ51013C datasheet:
https://www.ti.com/lit/ds/symlink/bq51013c.pdf

## 24. BOM Status

This document is the preliminary component-level BOM.

Parts marked "to be selected" must not be treated as final production components.

The next engineering revision must replace those entries with values taken directly from the selected TI reference schematic/EVM and verified against the selected coil.
