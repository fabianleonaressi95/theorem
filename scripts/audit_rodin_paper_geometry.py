#!/usr/bin/env python3
"""Audit the published Rodin-coil dimensions before attempting 3-D reconstruction.

This deliberately does NOT invent a 3-D conductor path. It checks the
published right-triangle relations (8)-(9) against the reported dimensions.
"""
from __future__ import annotations
import json
import math
from dataclasses import asdict, dataclass

@dataclass(frozen=True)
class PublishedGeometry:
    external_diameter_m: float = 0.0995
    aperture_diameter_m: float = 0.029
    winding_angle_deg: float = 150.0
    poles_used: int = 12
    poles_in_numerical_map: int = 36

def audit(g: PublishedGeometry = PublishedGeometry()) -> dict[str, float | int | bool]:
    if g.external_diameter_m <= 0 or g.aperture_diameter_m <= 0:
        raise ValueError("diameters must be positive")
    if not 0 < g.winding_angle_deg < 180:
        raise ValueError("winding angle must lie between 0 and 180 degrees")
    if g.poles_used < 1 or g.poles_in_numerical_map < 1:
        raise ValueError("pole counts must be positive")

    rp = g.external_diameter_m / 2.0
    rc_reported = g.aperture_diameter_m / 2.0
    theta_deg = 90.0 - g.winding_angle_deg / 2.0
    theta = math.radians(theta_deg)
    rc_from_eq8 = rp * math.sin(theta)
    l_from_eq9 = 2.0 * rp * math.cos(theta)
    relative_discrepancy = abs(rc_from_eq8 - rc_reported) / rc_reported
    theta_from_reported_rc = math.degrees(math.asin(rc_reported / rp))
    angle_from_reported_rc = 2.0 * (90.0 - theta_from_reported_rc)

    return {
        "outer_radius_mm": rp * 1e3,
        "reported_aperture_radius_mm": rc_reported * 1e3,
        "theta_from_reported_winding_deg": theta_deg,
        "aperture_radius_from_eq8_mm": rc_from_eq8 * 1e3,
        "eq9_segment_length_mm": l_from_eq9 * 1e3,
        "aperture_radius_discrepancy_mm": (rc_from_eq8 - rc_reported) * 1e3,
        "relative_aperture_discrepancy": relative_discrepancy,
        "winding_angle_implied_by_reported_aperture_deg": angle_from_reported_rc,
        "geometry_consistent_within_1_percent": relative_discrepancy <= 0.01,
        "poles_used": g.poles_used,
        "poles_in_numerical_map": g.poles_in_numerical_map,
    }

if __name__ == "__main__":
    print(json.dumps(audit(), indent=2))
