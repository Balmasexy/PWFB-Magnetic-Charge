# MagCharge Universal Receiver V1 — Schematic Netlist Specification

## 1. Purpose

This document defines the preliminary electrical netlist for the MagCharge Universal Receiver V1.

The design is based on the TI BQ51013C receiver architecture and the verified TI BQ51013CEVM reference values documented in this repository.

This is an engineering reference specification. The final schematic must be checked against the latest TI datasheet and reference design before fabrication.

---

## 2. Main Power Flow

```text
QI TX
  │
  ▼
L1 RX COIL
  │
  ▼
BQ51013C RECEIVER
  │
  ▼
RECTIFIED / REGULATED OUTPUT
  │
  ▼
PROTECTION
  │
  ▼
+5V_USB
  │
  ▼
USB-C
