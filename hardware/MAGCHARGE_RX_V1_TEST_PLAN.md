# MagCharge Universal Receiver V1 - Test Plan

## Test 1 - Receiver Output

Connect the receiver to a known Qi transmitter.

Measure:
- VOUT
- current
- power
- receiver temperature

Use an electronic load before connecting a phone.

## Test 2 - MagCharge Puck

MagCharge Puck
      |
      v
Universal Receiver
      |
      v
USB-C
      |
      v
Electronic Load

Verify stable output.

## Test 3 - Android Charging

Connect the Universal Receiver to an Android phone without native wireless charging.

Verify:
- phone detects charging
- charging remains stable
- USB-C connection is mechanically secure

## Test 4 - Alignment

Test:
- centered
- small X offset
- small Y offset
- rotated alignment

Record output power and temperatures.

## Test 5 - Long Duration

Operate at the intended V1 load for an extended period.

Record:
- coil temperature
- receiver IC temperature
- PCB temperature
- USB-C temperature
- phone temperature

## Test 6 - Fault Conditions

Using appropriate laboratory equipment, verify supported:
- over-current protection
- short-circuit protection
- over-temperature behavior
- foreign-object behavior

Do not perform uncontrolled fault tests using a phone.

## Test 7 - Mechanical

Check:
- magnetic attachment
- connector strain
- flex/PCB bending
- case compatibility
- adhesive strength

## Pass Criteria

The prototype must provide stable charging without:
- abnormal heating
- smoke
- component damage
- unstable output
- unsafe electrical behavior

This is an engineering prototype test plan and does not replace formal certification testing.
