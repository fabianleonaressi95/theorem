#!/usr/bin/env python3
"""Bicone two-sheet model: spinor holonomy produces the factor 1/2.

Model (constructed, not fitted to K0):
  * A double cone  x^2 + y^2 = k z^2  has two nappes (sheets) that are
    disjoint except at the apex -- the unique singular point.
  * On each nappe (a cone of half-angle alpha), parallel transport of a
    VECTOR around the apex once rotates by the deficit angle
    delta = 2*pi*(1 - sin(alpha)).
  * A SPINOR (spin-1/2 representation of SO(2)) acquires only HALF that
    angle: holonomy = exp(i*delta/2).  The factor 1/2 is the spinor
    weight -- the same mechanism that makes SU(2) the double cover of
    SO(3) and that puts 2I inside SU(2) at spin j = 1/2.
  * The two nappes are exchanged by the Z2 sheet grading already
    certified on the RGS carrier (S = 2 Z_S|_W, P_pm = (I +- S)/2).

This is a geometric MODEL explaining how a factor 1/2 can arise
canonically from a two-sheeted cone singularity. It is NOT derived
from the archived K0/Z_S/Z_A arrays; the link to K0 remains open.
"""
from pathlib import Path
import json

import numpy as np

OUT = Path(__file__).resolve().parent.parent / "audits" / "CONE_BICONE_SPINOR_HALF.json"


def main() -> None:
    # Cone half-angle alpha: nappe z = r * cot(alpha)? Use slope parameter.
    # Parametrize: radius rho at height z: rho = z * tan(alpha), alpha in (0, pi/2).
    # Metric on nappe: ds^2 = dz^2 + rho^2 dtheta^2 with rho = z tan a
    #   => proper radius coordinate r = z / cos(a); circumference = 2 pi r sin a.
    # Deficit angle delta = 2 pi (1 - sin a)  (a < pi/2 cone is "sharp").
    results = {}
    for alpha_deg in (30.0, 45.0, 60.0):
        a = np.deg2rad(alpha_deg)
        delta = 2 * np.pi * (1 - np.sin(a))
        vector_holonomy_deg = np.rad2deg(delta) % 360.0
        spinor_phase = np.exp(1j * delta / 2)
        # For the spinor to return to itself after ONE turn we need delta/2 = pi
        # mod 2pi  <=> delta = 2pi mod 4pi. The "half" is explicit:
        # spinor_angle = vector_angle / 2.
        results[f"alpha_{alpha_deg}deg"] = {
            "deficit_angle_rad": float(delta),
            "vector_holonomy_deg": float(vector_holonomy_deg),
            "spinor_holonomy_phase": [float(spinor_phase.real), float(spinor_phase.imag)],  # noqa
            "spinor_angle_is_half_vector_angle": True,
        }

    # Canonical check: spin-1/2 rep of SO(2): rotation by delta acts as
    # multiplication by exp(i sigma_z delta / 2) on the spinor doublet.
    # Eigenvalues exp(+- i delta/2): the "half" is the su(2) weight.
    delta = 2 * np.pi * (1 - np.sin(np.deg2rad(45.0)))
    su2_weights = np.array([+0.5, -0.5])  # m = +-1/2 for spin j=1/2
    phases = np.exp(1j * su2_weights * delta)
    check = {
        "su2_spin_half_weights": [0.5, -0.5],
        "holonomy_phases": [[float(p.real), float(p.imag)] for p in phases],
        "note": "exp(i m delta) with m=+-1/2 gives exp(+-i delta/2): "
                "the factor 1/2 is the magnetic quantum number of the "
                "spin-1/2 representation -- i.e. the same 1/2 as j=1/2 "
                "of the defining SU(2) rep of 2I.",
    }

    # Two-sheet structure: nappes exchanged by Z2; projectors (I +- S)/2.
    # On the certified carrier, S = 2 Z_S|_W has eigenvalues +-1 (sheets),
    # and Z_S itself carries eigenvalues +-1/2 = sheet-sign * 1/2.
    sheet_check = {
        "sheets": "two nappes of the double cone, disjoint except apex",
        "singular_point": "apex (unique common point of the two sheets)",
        "Z2_exchange": "nappe swap <-> S = 2 Z_S|_W on the RGS carrier",
        "eigenvalue_split": "Z_S eigenvalues +-1/2 = (sheet sign)/2",
    }

    report = {
        "title": "Bicone two-sheet model: spinor holonomy gives factor 1/2",
        "status": "constructed model; NOT derived from archived K0 data",
        "cone_results": results,
        "spinor_check": check,
        "sheet_structure": sheet_check,
        "claims": {
            "proved_in_model": [
                "two nappes are disjoint except at the apex",
                "vector holonomy = deficit angle delta",
                "spinor (spin-1/2) holonomy = delta/2 -- factor 1/2 canonical",
                "SU(2) weights m=+-1/2 reproduce the same half-angle",
            ],
            "open": [
                "which cone angle alpha (if any) is selected by RGS/K0 data",
                "whether the bicone apex maps to the K0 kernel or carrier",
                "any derivation of f's coefficients 1/240, 1/120 from cone data",
            ],
        },
    }
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["cone_results"], indent=2))
    print("wrote", OUT)


if __name__ == "__main__":
    main()
