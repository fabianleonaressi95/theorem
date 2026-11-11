#!/usr/bin/env python3
"""Run the five reproducible bicircular-annular geometry checks."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from models.bicircular_annular_geometry import (
    annular_points,
    fit_affine_deformation,
    green_strain,
    lens_area_centroid,
    lens_area_exact,
    lens_geometry,
    sample_loop_closure,
    strain_anisotropy,
)


def run_audit() -> dict:
    # E001: classical vesica, R1=R2=d=1.
    geom = lens_geometry(1.0, 1.0, 1.0)
    area_num, cx, cy = lens_area_centroid(1.0, 1.0, 1.0)
    area_exact = lens_area_exact(1.0, 1.0, 1.0)
    area_classical = (4.0 * np.pi - 3.0 * np.sqrt(3.0)) / 6.0

    # E002: asymmetric lens; quadrature is checked against the exact formula.
    asym = (1.35, 0.92, 1.10)
    area_q, cx_q, cy_q = lens_area_centroid(*asym)
    area_e = lens_area_exact(*asym)

    # E003: exact affine deformation recovered from two annular sample sets.
    F_exact = np.array([[1.20, 0.15], [0.05, 0.82]])
    centres = [(-0.5, 0.0), (0.5, 0.0)]
    points = np.vstack([
        annular_points(c, 0.15, 0.55, n_radial=5, n_angular=48)
        for c in centres
    ])
    displacements = (F_exact - np.eye(2)) @ points.T
    F_fit, _ = fit_affine_deformation(points, displacements.T)
    E_fit = green_strain(F_fit)

    # E004: local gradient convergence for a smooth cubic manufactured field.
    # u(x0+xi)=A xi + c*(xi_1^3, xi_2^3), so grad u(x0)=A.
    A = np.array([[0.12, -0.07], [0.04, -0.09]])
    x0 = np.array([0.2, -0.1])
    convergence = []
    for h in (0.40, 0.20, 0.10, 0.05):
        xi = annular_points((0.0, 0.0), h, 2.0 * h, n_radial=4, n_angular=96)
        u = xi @ A.T + 0.7 * xi ** 3
        F_h, _ = fit_affine_deformation(xi + x0, u)
        convergence.append({
            "h": h,
            "gradient_error": float(np.linalg.norm((F_h - np.eye(2)) - A)),
        })

    # E005: controlled loop closure around a manufactured 1/r defect field.
    b_target = np.array([0.7, -0.25])
    frank_target = 0.4
    loop = []
    for n in (32, 64, 128, 256, 512):
        b_measured, frank_measured = sample_loop_closure(
            radius=0.8, n=n, burgers=tuple(b_target), frank=frank_target
        )
        loop.append({
            "n": n,
            "burgers_error": float(np.linalg.norm(b_measured - b_target)),
            "frank_error": float(abs(frank_measured - frank_target)),
        })

    return {
        "classification": "manufactured numerical audit; not a physical validation",
        "E001_vesica_baseline": {
            "chord": geom["chord"],
            "chord_error": float(abs(geom["chord"] - np.sqrt(3.0))),
            "area_quadrature": area_num,
            "area_exact": area_exact,
            "area_classical": float(area_classical),
            "area_error": float(abs(area_num - area_classical)),
            "centroid": [cx, cy],
            "centroid_error_from_symmetry": float(abs(cx - 0.5) + abs(cy)),
        },
        "E002_asymmetric_lens": {
            "r1_r2_d": list(asym),
            "area_quadrature": area_q,
            "area_exact": area_e,
            "area_relative_error": float(abs(area_q - area_e) / area_e),
            "centroid": [cx_q, cy_q],
        },
        "E003_affine_anisotropy": {
            "F_exact": F_exact.tolist(),
            "F_reconstructed": F_fit.tolist(),
            "F_error_frobenius": float(np.linalg.norm(F_fit - F_exact)),
            "green_strain": E_fit.tolist(),
            "strain_anisotropy": strain_anisotropy(E_fit),
        },
        "E004_annular_gradient_convergence": convergence,
        "E005_defect_loop_closure": {
            "target_burgers": b_target.tolist(),
            "target_frank": frank_target,
            "levels": loop,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="artifacts/bicircular_annular_audit.json")
    args = parser.parse_args()
    report = run_audit()
    path = Path(args.out)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    e = report["E001_vesica_baseline"]
    a = report["E002_asymmetric_lens"]
    f = report["E003_affine_anisotropy"]
    if e["chord_error"] > 1e-10 or e["area_error"] > 1e-10:
        raise SystemExit("E001 failed")
    if a["area_relative_error"] > 1e-9:
        raise SystemExit("E002 failed")
    if f["F_error_frobenius"] > 1e-10:
        raise SystemExit("E003 failed")
    conv = [v["gradient_error"] for v in report["E004_annular_gradient_convergence"]]
    if not all(conv[i + 1] < conv[i] for i in range(len(conv) - 1)):
        raise SystemExit("E004 failed: gradient error did not decrease")
    last = report["E005_defect_loop_closure"]["levels"][-1]
    if last["burgers_error"] > 1e-4 or last["frank_error"] > 1e-4:
        raise SystemExit("E005 failed")
    print(f"PASS: report written to {path}")


if __name__ == "__main__":
    main()
