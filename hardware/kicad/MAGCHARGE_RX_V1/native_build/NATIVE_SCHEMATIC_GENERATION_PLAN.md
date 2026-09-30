# MagCharge RX V1 — Native Schematic Generation Plan

Target:
MAGCHARGE_RX_V1.kicad_sch

Primary IC:
Texas Instruments BQ51013CRHLR

Verified pin map:
1 PGND
2 AC1
3 BOOT1
4 OUT
5 CLAMP1
6 COMM1
7 CHG
8 AD-EN
9 AD
10 EN1
11 EN2
12 ILIM
13 TS/CTRL
14 FOD
15 COMM2
16 CLAMP2
17 BOOT2
18 RECT
19 AC2
20 PGND
EP PGND

Engineering requirements:
- Wireless-only receiver
- AD tied to PGND
- AD-EN intentionally floating
- EN1/EN2 normally LOW/floating
- C_RX1/C_RX2 remain TBD pending coil characterization
- FOD calibration network retained
- USB-C output is 5V nominal, target 1A
- No USB-PD
- Production NTC required
- ESD and fuse selections remain TBD
- Native KiCad validation required before fabrication
