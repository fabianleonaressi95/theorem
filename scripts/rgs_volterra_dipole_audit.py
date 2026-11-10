#!/usr/bin/env python3
"""Volterra dipole-to-edge source audit (profile level; not an elasticity solve).

Compares the y-profile in the incompatibility of an opposite wedge-disclination
pair with the y-derivative profile of a regularized edge dislocation.

For a normalized core f_sigma(y)=sigma^{-1} f(y/sigma), the dipole profile is
    q_d(y) = [f_sigma(y-d/2)-f_sigma(y+d/2)]/d,
which tends to -f_sigma'(y).  This is the sign appearing in
inc(e_xy^p=b H(x-x0) f_sigma(y)) = -b delta(x-x0) f_sigma'(y).

The script sweeps d/h and sigma/h, but the profile error depends only on
d/sigma=(d/h)/(sigma/h). It deliberately does NOT claim to compare elastic
stress or energy: those require solving the same boundary-value problem for
both source representations with matched boundary conditions and constitutive
data.

Run:
  python scripts/rgs_volterra_dipole_audit.py --out artifacts/volterra_dipole_audit
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np


def gaussian(z: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    f = np.exp(-0.5 * z * z) / np.sqrt(2.0 * np.pi)
    return f, -z * f


def sech2(z: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    # Integral over R is one.
    f = 0.25 / np.cosh(0.5 * z) ** 2
    fp = -0.25 * np.cosh(0.5 * z) ** -2 * np.tanh(0.5 * z)
    return f, fp


PROFILES = {"gaussian": gaussian, "sech2": sech2}
D_OVER_H = (1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 8.0)
SIGMA_OVER_H = (1.0, 2.0, 3.2, 6.4)


def profile_audit(profile: str, d_over_h: float, sigma_over_h: float,
                  points: int = 200001) -> dict[str, float | str]:
    if profile not in PROFILES:
        raise ValueError(f"unknown profile: {profile}")
    if d_over_h <= 0 or sigma_over_h <= 0:
        raise ValueError("d/h and sigma/h must be positive")

    # z=y/sigma. The finite-dipole quotient, multiplied by sigma, is
    # dimensionless and is compared with -f'(z).
    z = np.linspace(-14.0, 14.0, points)
    f, fp = PROFILES[profile](z)
    ratio = d_over_h / sigma_over_h  # d/sigma
    half = 0.5 * ratio
    q = (f(z - half) - f(z + half)) / ratio
    target = -fp

    norm = np.sqrt(np.trapezoid(target * target, z))
    error = np.sqrt(np.trapezoid((q - target) ** 2, z)) / norm
    # The target has unit first moment: integral z*(-f') dz = 1.
    moment = np.trapezoid(z * q, z)
    zeroth = np.trapezoid(q, z)
    return {
        "profile": profile,
        "d_over_h": d_over_h,
        "sigma_over_h": sigma_over_h,
        "d_over_sigma": ratio,
        "relative_L2_error": float(error),
        "zeroth_moment": float(zeroth),
        "first_moment": float(moment),
        "target_first_moment": 1.0,
    }


def run(out: Path) -> dict:
    out.mkdir(parents=True, exist_ok=True)
    rows = [
        profile_audit(name, d_h, s_h)
        for name in PROFILES
        for s_h in SIGMA_OVER_H
        for d_h in D_OVER_H
    ]

    # Explicitly test the second-order small-separation regime at fixed core.
    convergence = []
    for name in PROFILES:
        vals = [
            profile_audit(name, d_h, 64.0)["relative_L2_error"]
            for d_h in (8.0, 4.0, 2.0, 1.0)
        ]
        convergence.append({
            "profile": name,
            "d_over_sigma": [8/64, 4/64, 2/64, 1/64],
            "relative_L2_error": vals,
            "successive_error_ratios": [
                vals[i] / vals[i + 1] for i in range(len(vals) - 1)
            ],
        })

    report = {
        "title": "Regularized Volterra dipole-to-edge profile audit",
        "scope": "source-profile/incompatibility factor only; no FEM stress or energy solve",
        "identity": " [f_sigma(y-d/2)-f_sigma(y+d/2)]/d -> -f_sigma'(y) ",
        "sweeps": {"d_over_h": list(D_OVER_H),
                   "sigma_over_h": list(SIGMA_OVER_H),
                   "profiles": list(PROFILES)},
        "rows": rows,
        "small_separation_check": convergence,
        "interpretation": [
            "At fixed sigma, the finite-dipole quotient should converge to -f_sigma' as d/sigma tends to zero.",
            "The profile comparison depends on d/sigma, not independently on d/h and sigma/h.",
            "d/h=2 is not intrinsically special in the continuum; it is only a grid-alignment value.",
            "No elastic energy equivalence is inferred from this profile-level test.",
        ],
    }
    (out / "report.json").write_text(json.dumps(report, indent=2) + "\n")
    with (out / "profile_sweep.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="artifacts/volterra_dipole_audit")
    args = parser.parse_args()
    report = run(Path(args.out))
    print(json.dumps({
        "rows": len(report["rows"]),
        "profiles": report["sweeps"]["profiles"],
        "output": args.out,
        "scope": report["scope"],
    }, indent=2))


if __name__ == "__main__":
    main()
