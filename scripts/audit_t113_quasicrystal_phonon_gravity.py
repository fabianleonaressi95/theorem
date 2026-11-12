#!/usr/bin/env python3
"""Regression audit for the isotropic acoustic limit of T113.

This is not a quasicrystal simulation and does not compute gravitational mass
from a phonon-phason action. It checks the published scalar control formula.
"""
from __future__ import annotations

import argparse
import json
import math


def gravitational_mass(energy: float, sound_speed: float,
                       dlogc_dlogrho: float) -> float:
    if energy < 0 or sound_speed <= 0:
        raise ValueError("energy must be nonnegative and sound_speed positive")
    return -dlogc_dlogrho * energy / sound_speed**2


def logarithmic_slope(rho: float, c_of_rho, relative_step: float = 1e-5) -> float:
    if rho <= 0 or relative_step <= 0:
        raise ValueError("rho and relative_step must be positive")
    lo, hi = rho * math.exp(-relative_step), rho * math.exp(relative_step)
    clo, chi = c_of_rho(lo), c_of_rho(hi)
    if clo <= 0 or chi <= 0:
        raise ValueError("sound speed must remain positive")
    return (math.log(chi) - math.log(clo)) / (2 * relative_step)


def audit() -> dict:
    # Illustrative power-law equation of state c_s(rho) = c0*(rho/rho0)^alpha.
    # The exact logarithmic derivative is alpha; alpha>0 gives M_g<0.
    rho0, c0, energy, alpha = 2.0, 300.0, 1.0e-6, 0.25
    c_of_rho = lambda rho: c0 * (rho / rho0) ** alpha
    slope = logarithmic_slope(rho0, c_of_rho)
    mass = gravitational_mass(energy, c0, slope)
    expected = -alpha * energy / c0**2
    return {
        "model": "isotropic scalar acoustic control only",
        "logarithmic_slope": slope,
        "expected_slope": alpha,
        "mass": mass,
        "expected_mass": expected,
        "slope_error": abs(slope - alpha),
        "mass_error": abs(mass - expected),
        "negative_for_positive_slope": mass < 0,
        "scope": "does not establish a quasicrystal phonon-phason result",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.parse_args()
    print(json.dumps(audit(), indent=2))


if __name__ == "__main__":
    main()
