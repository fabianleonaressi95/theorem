#!/usr/bin/env python3
"""Independent grid audit for the C60 nuclear-penalty proximal optimizer.

The optimizer uses the closed-form singular-value thresholding formula.
This verifier does not call that formula to find its comparison point:
it minimizes each reduced scalar objective on a dense grid, then compares
the independently located minimizer and objective with the closed form.

Model per face:
    min_G ||G||_F^2 + lambda ||A-G||_*
with A in R^(3x2), lambda >= 0.

The singular-value reduction is exact for this unitarily invariant problem.
The grid check is a numerical cross-check, not a replacement for the proof.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np

from optimize_c60_cf_bulk_nuclear_penalty import solve_face


def scalar_grid_check(sigma: float, lam: float, points: int) -> dict[str, float]:
    if points < 3:
        raise ValueError("grid points must be >= 3")
    # A minimizer lies in [0, sigma]; values outside this interval cannot
    # improve g^2 + lambda |sigma-g|.
    grid = np.linspace(0.0, sigma, points)
    values = grid * grid + lam * np.abs(sigma - grid)
    j = int(np.argmin(values))
    step = sigma / (points - 1) if sigma else 0.0
    g_closed = min(sigma, lam / 2.0)
    f_closed = g_closed * g_closed + lam * abs(sigma - g_closed)
    f_grid = float(values[j])
    return {
        "sigma": float(sigma),
        "g_closed": float(g_closed),
        "g_grid": float(grid[j]),
        "grid_step": float(step),
        "minimizer_error": float(abs(g_closed - grid[j])),
        "objective_closed": float(f_closed),
        "objective_grid": f_grid,
        "objective_gap": float(f_closed - f_grid),
        "allowed_objective_gap": float(step * step / 4.0 + 1e-13),
    }


def verify_matrix(A: np.ndarray, lam: float, points: int) -> dict[str, Any]:
    A = np.asarray(A, dtype=float)
    if A.shape != (3, 2) or not np.isfinite(A).all():
        raise ValueError("each A must be a finite 3x2 matrix")
    if lam < 0 or not np.isfinite(lam):
        raise ValueError("lambda must be finite and nonnegative")

    # Closed-form solver under audit.
    result = solve_face(A, lam)
    # Independent numerical minimization of the two scalar spectral modes.
    sigma = np.linalg.svd(A, compute_uv=False)
    checks = [scalar_grid_check(float(s), lam, points) for s in sigma]
    max_gap = max((x["objective_gap"] for x in checks), default=0.0)
    max_allowed = max((x["allowed_objective_gap"] for x in checks), default=1e-13)
    max_location_error = max((x["minimizer_error"] for x in checks), default=0.0)
    max_step = max((x["grid_step"] for x in checks), default=0.0)

    # Independent direct evaluation of the matrix objective at the returned G.
    G = np.asarray(result["G_opt"], dtype=float)
    M = A - G
    direct_objective = float(np.sum(G * G) + lam * np.sum(np.linalg.svd(M, compute_uv=False)))
    matrix_residual = abs(direct_objective - result["objective_per_area"])

    passed = (
        max_gap <= max_allowed + 1e-12
        and max_location_error <= max_step / 2.0 + 1e-12
        and matrix_residual <= 1e-10 * max(1.0, direct_objective)
    )
    return {
        "passed": bool(passed),
        "singular_mode_checks": checks,
        "max_grid_objective_gap": max_gap,
        "max_allowed_grid_gap": max_allowed,
        "max_grid_location_error": max_location_error,
        "max_grid_step": max_step,
        "direct_matrix_objective": direct_objective,
        "optimizer_objective": result["objective_per_area"],
        "matrix_objective_residual": matrix_residual,
        "rank_G_opt": result["rank_G_opt"],
        "rank_M_opt": result["rank_M_opt"],
    }


def self_test(points: int) -> dict[str, Any]:
    rng = np.random.default_rng(20261121)
    matrices = [
        np.diag([3.0, 1.0, 0.0])[:, :2],
        np.array([[2.0, 0.0], [0.0, 0.0], [0.0, 0.0]]),
        np.zeros((3, 2)),
    ]
    matrices.extend(rng.normal(size=(3, 2)) for _ in range(8))
    lambdas = [0.0, 0.8, 2.0, 5.0]
    cases = []
    for i, A in enumerate(matrices):
        lam = lambdas[i % len(lambdas)]
        cases.append({"case": i, "lambda": lam, **verify_matrix(A, lam, points)})
    return {
        "cases": cases,
        "passed": all(case["passed"] for case in cases),
        "number_of_cases": len(cases),
        "grid_points_per_singular_mode": points,
        "seed": 20261121,
    }


def verify_document(doc: dict[str, Any], lam: float, points: int) -> dict[str, Any]:
    faces = doc.get("faces")
    if not isinstance(faces, list) or not faces:
        raise ValueError("JSON input must contain a non-empty 'faces' list")
    results = []
    for i, face in enumerate(faces):
        results.append({
            "name": face.get("name", f"face-{i}"),
            "area": float(face.get("area", 1.0)),
            **verify_matrix(np.asarray(face["A"], dtype=float), lam, points),
        })
    return {
        "model": "independent scalar-grid check of ||G||_F^2 + lambda ||A-G||_*",
        "lambda": lam,
        "grid_points_per_singular_mode": points,
        "faces": results,
        "passed": all(x["passed"] for x in results),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="JSON with a non-empty 'faces' list")
    parser.add_argument("--lambda", dest="lam", type=float, default=1.0)
    parser.add_argument("--grid-points", type=int, default=50001)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.grid_points < 3:
        parser.error("--grid-points must be >= 3")
    if args.self_test:
        result = self_test(args.grid_points)
    elif args.input:
        doc = json.loads(args.input.read_text(encoding="utf-8"))
        result = verify_document(doc, args.lam, args.grid_points)
    else:
        parser.error("provide --input or --self-test")

    rendered = json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
