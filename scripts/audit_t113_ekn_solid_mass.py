#!/usr/bin/env python3
"""Regression checks for the EKN isotropic-solid packet-mass normalization."""
from __future__ import annotations
import math


def ekn_solid_packet_mass(*, c_longitudinal: float, dlog_c_dlog_rho: float, energy: float) -> float:
    """EKN Eq. (24): both L and T packets use the longitudinal Green scale c_L^2."""
    if c_longitudinal <= 0 or energy < 0:
        raise ValueError("c_L must be positive and energy nonnegative")
    if not all(map(math.isfinite, (c_longitudinal, dlog_c_dlog_rho, energy))):
        raise ValueError("inputs must be finite")
    return -dlog_c_dlog_rho * energy / c_longitudinal**2


def ekn_solid_packet_mass_from_compression(*, b0: float, c_longitudinal: float,
                                            dc_branch_db0: float, energy: float) -> float:
    """Use rho_m proportional to b0 under hydrostatic compression."""
    if b0 <= 0 or c_longitudinal <= 0 or energy < 0:
        raise ValueError("b0,c_L must be positive and energy nonnegative")
    slope = b0 * dc_branch_db0 / c_longitudinal
    return ekn_solid_packet_mass(c_longitudinal=c_longitudinal,
                                 dlog_c_dlog_rho=slope, energy=energy)


def fluid_limit_mass(*, c_sound: float, slope: float, energy: float) -> float:
    if c_sound <= 0 or energy < 0:
        raise ValueError("c_s must be positive and energy nonnegative")
    return -slope * energy / c_sound**2


def audit() -> dict:
    cL, EL, ET = 4.0, 10.0, 6.0
    alphaL, alphaT = 0.3, -0.2
    ML = ekn_solid_packet_mass(c_longitudinal=cL, dlog_c_dlog_rho=alphaL, energy=EL)
    MT = ekn_solid_packet_mass(c_longitudinal=cL, dlog_c_dlog_rho=alphaT, energy=ET)
    return {
        "classification": "algebraic regression of published EKN Eq. (24)",
        "longitudinal_packet_mass": ML,
        "transverse_packet_mass": MT,
        "combined_separated_packets_mass": ML + MT,
        "fluid_limit": fluid_limit_mass(c_sound=cL, slope=alphaL, energy=EL),
        "scope": "Does not independently derive the nonlinear PDE or its 1/r^2 tail."
    }


if __name__ == "__main__":
    import json
    print(json.dumps(audit(), indent=2))
