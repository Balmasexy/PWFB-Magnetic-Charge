# MagCharge Universal Receiver V1 - BQ51013C Reference Design

## Design Status

Prototype engineering reference.

This design is based on the Texas Instruments BQ51013C 5W Qi receiver architecture.

It is not a certified Qi or Qi2 product.

Final PCB fabrication must use the latest TI datasheet, EVM documentation and validated component specifications.

## Primary IC

Part:
Texas Instruments BQ51013C

Package:
VQFN, 20 pins, 4.5 mm x 3.5 mm

Target:

- Qi/WPC v1.3
- 5W Baseline Power Profile
- 5V output
- up to 1A target output
- integrated synchronous rectifier
- integrated regulation
- integrated Qi communication control
- FOD support
- thermal shutdown
- NTC/control input

## Power Architecture

Qi Transmitter
      |
      v
48 x 32 mm RX Coil
      |
      v
AC1 / AC2
      |
      v
BQ51013C
      |
      v
5V REGULATED OUTPUT
      |
      v
Protection / USB-C
      |
      v
Android Phone

## Recommended RX Coil Candidates

Initial candidates from the TI datasheet:

1. Würth Electronics
   Part: 760308103215
   Size: 48 x 32 mm
   Nominal Ls: 14.3 uH

2. XFMRS
   Part: XFMCC483201-143
   Size: 48 x 32 mm
   Nominal Ls: 14.3 uH

3. TDK
   Part: WR483265-15F5-G
   Size: 48 x 32 mm
   Nominal Ls: approximately 13.3 uH

The final coil must be electrically characterized in the actual MagCharge mechanical stack.

Do not assume the catalog inductance remains unchanged after ferrite, adhesive, case and magnetic-ring integration.

## Coil Requirements

Target:

- 48 x 32 mm class
- low profile
- ferrite backing
- suitable Qi receiver construction
- compatible with BQ51013C
- suitable for 50 mA to 1 A receiver operation

Measure in the final mechanical assembly:

- inductance
- DC resistance
- Q factor
- received power
- temperature

## Resonant Network

The BQ51013C datasheet specifies the receiver resonant-network design around the selected coil.

For the final selected coil, calculate and verify:

- C_RX1 series resonant capacitance (Cs)
- C_RX2 parallel resonant capacitance (Cd)
- operating frequency
- coil Q
- voltage rating

C_RX1 and C_RX2 must use capacitors with at least 25 V rating.

C_RX1 and C_RX2 are part of the receiver resonant network and must
not be confused with the separate COMM capacitors.

Do not substitute arbitrary values without recalculating the network.

## BOOT Capacitors

Use the TI reference value as the starting point:

AC1 -> BOOT1:
10 nF, minimum 25 V

AC2 -> BOOT2:
10 nF, minimum 25 V

These capacitors support correct operation of the internal synchronous-rectifier FETs.

## CLAMP Capacitors

Starting reference value:

AC1 -> CLAMP1:
0.47 uF, minimum 25 V

AC2 -> CLAMP2:
0.47 uF, minimum 25 V

These capacitors support the receiver over-voltage clamping function.

## COMM Capacitors

Starting reference value:

COMM network:
22 nF, minimum 25 V

The TI datasheet notes that 47 nF may be evaluated if communication robustness requires it.

Do not change this value without testing communication and efficiency.

## Input Protection

The BQ51013C provides internal receiver-side protection features.

The final design must additionally consider:

- PCB-level ESD protection where appropriate
- USB-C interface protection
- output current limiting
- short-circuit behavior
- thermal monitoring

The Android application must never be the primary safety mechanism.

## Output

Target:

Voltage: 5 V nominal
Current: up to 1 A
Power: approximately 5 W

Provide appropriate output filtering according to the TI reference design.

The USB-C interface must be configured as a power source.

USB-PD is not part of V1.

## Temperature

Use the BQ51013C TS/CTRL function with an appropriate NTC implementation.

Initial prototype monitoring points:

- RX coil
- receiver IC
- USB-C connector
- PCB hot spot

The firmware/app may later report temperature through BLE.

Hardware thermal protection remains independent of BLE.

## Control Pins

For the wireless-only prototype:

AD may be configured according to the TI wireless-only reference design.

AD_EN may remain unused where permitted by the TI design.

EN1 and EN2 may be left in their normal enabled state for a simple always-ready receiver prototype.

If a future MCU controls these pins, the MCU must not be required for basic safety.

## FOD

The BQ51013C includes Qi v1.3 FOD functionality.

FOD parameters must be calibrated for the final:

- receiver coil
- ferrite
- magnetic ring
- enclosure
- phone/case geometry

Do not assume TI default parameters are sufficient for the finished MagCharge product.

## PCB Layout

Follow the TI EVM/reference layout as closely as practical.

Important rules:

- keep AC1/AC2 paths short
- minimize parasitic loop area
- keep high-current paths short and wide
- place BOOT capacitors close to their pins
- place CLAMP capacitors close to their pins
- place COMM components according to TI layout guidance
- keep sensitive control traces away from noisy switching nodes
- provide a solid controlled ground strategy
- maintain the required coil/ferrite mechanical stack

## Mechanical Stack

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

The magnetic ring is an alignment mechanism.

It does not transfer electrical power.

Validate the magnetic ring for:

- coupling
- efficiency
- temperature
- mechanical retention
- interference with the receiver system

## USB-C Stage

V1:

- USB-C source role
- 5V nominal
- up to 1A target
- no USB-PD
- correct CC source configuration
- short-circuit protection
- ESD protection
- mechanical strain relief

The USB-C connector should be downstream of the regulated receiver output.

## BLE Extension

Optional.

Future BLE MCU may measure:

- VOUT
- current
- temperature
- estimated power
- fault state
- receiver ID

BLE does not participate in Qi power negotiation or primary safety functions.

## Initial Bench Test

Do not begin testing with a phone.

First connect:

BQ51013C Receiver
       |
       v
5V Output
       |
       v
Electronic Load

Test progressively:

1. no load
2. 100 mA
3. 250 mA
4. 500 mA
5. 750 mA
6. 1 A target

At each stage record:

- output voltage
- output current
- output power
- coil temperature
- receiver IC temperature
- USB-C temperature
- charging stability

Stop testing if abnormal heating, smoke, component damage or unstable electrical behavior occurs.

## Prototype Acceptance

The first prototype passes engineering bring-up when it can:

1. receive Qi power from a compatible transmitter
2. produce regulated 5V output
3. sustain the intended test load
4. maintain controlled temperatures
5. communicate correctly with the transmitter
6. demonstrate stable operation under alignment variation

Passing this prototype test does not constitute Qi certification.

## Certification

The finished commercial product must undergo the applicable Wireless Power Consortium certification process before being marketed as Qi-certified.

Do not describe the MagCharge Universal Receiver V1 as Qi-certified based solely on use of the BQ51013C.

## Design References

Texas Instruments BQ51013C product documentation:
https://www.ti.com/product/BQ51013C

Texas Instruments BQ51013C-Q1EVM:
https://www.ti.com/tool/BQ51013C-Q1EVM

Texas Instruments BQ51013CEVM:
https://www.ti.com/tool/BQ51013CEVM

Use the latest manufacturer documentation when creating the final schematic and PCB.
