# MagCharge Universal Receiver V1 - Preliminary BOM

## Core Receiver

### 1. Qi Receiver IC

Preferred starting class:

TI BQ51013C or an approved currently available equivalent.

Purpose:
- Qi wireless power reception
- rectification
- regulated output
- receiver control
- supported protection functions

The final part must be selected according to availability and the manufacturer's current reference design.

### 2. Receiver Coil

Low-profile Qi-compatible receiver coil.

Initial target:
- approximately 48 x 32 mm class
- low profile
- ferrite backed
- matched to the selected receiver IC

The exact coil must be selected together with the receiver IC/reference design.

### 3. Ferrite Shield

Flexible or thin ferrite sheet positioned behind the receiver coil.

Purpose:
- improve magnetic coupling
- reduce unwanted magnetic interaction with the phone
- support receiver efficiency

### 4. Magnetic Alignment Ring

Thin permanent-magnet ring.

Purpose:
- align the receiver with the MagCharge transmitter
- maintain the correct coil position

The magnets are for alignment only. They do not transfer charging power.

### 5. Temperature Sensor

NTC thermistor or the exact temperature-sensing component specified by the selected receiver IC/reference design.

Purpose:
- thermal monitoring
- charging protection

### 6. USB-C Connector

USB-C male connector configured as a 5V power source.

V1 target:
- 5V
- up to 1A target
- USB Power Delivery not implemented

### 7. Protection Components

Use the protection components specified by the selected receiver IC reference design.

Potential functions:

- over-voltage protection
- over-current protection
- short-circuit protection
- thermal protection
- foreign-object detection where supported

### 8. PCB

Prototype PCB or flexible PCB.

Target:

- compact
- low profile
- receiver coil area
- receiver IC area
- protection/regulation area
- USB-C connection
- test points

Follow the exact receiver IC reference layout.

## Mechanical Materials

- electrical insulation film
- protective outer film
- thin adhesive layer
- connector strain relief
- optional protective enclosure

## Prototype Laboratory Equipment

The first prototype should be tested with:

- known-good Qi transmitter
- MagCharge puck
- electronic load
- USB power meter
- multimeter
- temperature probe
- oscilloscope where available
- USB-C breakout
- current/voltage measurement equipment

## Component Selection Rule

Do not purchase large quantities before the receiver IC and coil combination has been validated.

The receiver IC, coil and compensation network must be treated as one validated power-transfer system.

## Production BOM

The final production BOM must contain:

- manufacturer
- manufacturer part number
- package
- quantity
- approved substitute
- supplier
- availability
- lifecycle status
- reference-design source

This document is a preliminary engineering BOM and not a final production purchasing list.
