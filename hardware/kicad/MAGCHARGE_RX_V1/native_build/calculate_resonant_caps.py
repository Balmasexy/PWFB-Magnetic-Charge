#!/usr/bin/env python3

import math

# ============================================================
# MagCharge Universal Receiver V1
# BQ51013C Resonant Capacitor Calculator
#
# TI BQ51013C datasheet:
#   fS = 100 kHz
#   fD = 1 MHz
#
# Enter measured Ls' and Ls from the actual receiver coil
# and final mechanical stack.
# ============================================================

FS = 100_000.0       # Hz
FD = 1_000_000.0     # Hz

# ------------------------------------------------------------
# USER MEASUREMENTS
# ------------------------------------------------------------
LS_PRIME_UH = None   # Measured with WPC test fixture
LS_UH = None         # Measured free-space inductance
RDC_MOHM = None      # Measured DC resistance


def cs_from_ls_prime(ls_prime_uH):
    """
    TI Equation 5:
        Cs = 1 / ((2*pi*fS)^2 * Ls')
    """
    L = ls_prime_uH * 1e-6
    return 1 / ((2 * math.pi * FS) ** 2 * L)


def cd_from_ls(ls_uH, cs_f):
    """
    TI dual-resonant relationship.

    1/Cd = (2*pi*fD)^2 * Ls - 1/Cs

    Therefore:
        Cd = 1 / (((2*pi*fD)^2 * Ls) - (1/Cs))
    """
    L = ls_uH * 1e-6
    denominator = ((2 * math.pi * FD) ** 2 * L) - (1 / cs_f)

    if denominator <= 0:
        raise ValueError(
            "Calculated Cd denominator is not positive. "
            "Check measured Ls/Ls' values."
        )

    return 1 / denominator


def q_factor(ls_uH, rdc_mohm):
    """
    TI Equation 6:
        Q = (2*pi*fD*Ls) / R
    """
    L = ls_uH * 1e-6
    R = rdc_mohm * 1e-3
    return (2 * math.pi * FD * L) / R


def nf(c):
    return c * 1e9


print("=== MAGCHARGE BQ51013C RESONANT CAPACITOR CALCULATOR ===")
print()
print("Required measurements:")
print("  Ls' : coil installed in WPC test fixture, 1 Vrms, 100 kHz")
print("  Ls  : free-space coil, 1 Vrms, 100 kHz")
print("  Rdc : coil DC resistance")
print()

if LS_PRIME_UH is None or LS_UH is None:
    print("STATUS: WAITING FOR MEASUREMENTS")
    print()
    print("C_RX1 / Cs = TBD")
    print("C_RX2 / Cd = TBD")
    print()
    print("Do NOT change the schematic capacitor values yet.")
    raise SystemExit(0)

cs = cs_from_ls_prime(LS_PRIME_UH)
cd = cd_from_ls(LS_UH, cs)

print(f"Ls' = {LS_PRIME_UH:.4f} uH")
print(f"Ls  = {LS_UH:.4f} uH")

print()
print(f"Calculated Cs = {nf(cs):.3f} nF")
print(f"Calculated Cd = {nf(cd):.3f} nF")

if RDC_MOHM is not None:
    q = q_factor(LS_UH, RDC_MOHM)
    print(f"Rdc = {RDC_MOHM:.3f} mOhm")
    print(f"Q   = {q:.2f}")
    print(f"Q requirement (>77): {'PASS' if q > 77 else 'FAIL'}")

print()
print("Both resonant capacitors require >=25 V rating.")
print()
print("STATUS: CALCULATION COMPLETE")
