#!/usr/bin/env python3
"""Facewise proximal solver for |G|_F^2 + lambda ||A-G||_*.

Input JSON:
{
  "faces": [
    {"name": "face-0", "area": 1.0,
     "A": [[...,...], [...,...], [...,...]]}
  ]
}

The script solves each independent face exactly by singular-value
soft-thresholding. It does not load or invent C60 face data.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np


def solve_face(A: np.ndarray, lam: float) -> dict[str, Any]:
    A = np.asarray(A, dtype=float)
    if A.shape != (3, 2):
        raise ValueError(f"Expected a 3x2 matrix, got {A.shape}")
    if not np.isfinite(A).all():
        raise ValueError("A contains non-finite entries")
    if lam < 0 or not np.isfinite(lam):
        raise ValueError("lambda must be finite and nonnegative")

    U, s, Vt = np.linalg.svd(A, full_matrices=False)
    bulk_sv = np.minimum(s, lam / 2.0)
    residual = np.maximum(s - lam / 2.0, 0.0)
    G = (U * bulk_sv) @ Vt
    M = A - G

    bulk = float(np.sum(G * G))
    micro = float(lam * np.sum(np.linalg.svd(M, compute_uv=False)))
    objective = bulk + micro
    predicted = float(np.sum(bulk_sv**2 + lam * residual))

    return {
        "singular_values_A": s.tolist(),
        "singular_values_G": bulk_sv.tolist(),
        "singular_values_M": residual.tolist(),
        "G_opt": G.tolist(),
        "M_opt": M.tolist(),
        "bulk_energy_per_area": bulk,
        "weighted_micro_energy_per_area": micro,
        "objective_per_area": objective,
        "formula_objective_per_area": predicted,
        "objective_formula_residual": abs(objective - predicted),
        "rank_A": int(np.linalg.matrix_rank(A)),
        "rank_G_opt": int(np.count_nonzero(bulk_sv > 1e-12)),
        "rank_M_opt": int(np.count_nonzero(residual > 1e-12)),
    }


def solve_document(doc: dict[str, Any], lam: float) -> dict[str, Any]:
    faces = doc.get("faces")
    if not isinstance(faces, list) or not faces:
        raise ValueError("JSON must contain a non-empty 'faces' list")
    out = []
    total = 0.0
    for i, face in enumerate(faces):
        area = float(face.get("area", 1.0))
        if not np.isfinite(area) or area <= 0:
            raise ValueError(f"Face {i}: area must be finite and positive")
        result = solve_face(np.asarray(face["A"], dtype=float), lam)
        weighted = area * result["objective_per_area"]
        total += weighted
        out.append({
            "name": face.get("name", f"face-{i}"),
            "area": area,
            **result,
            "weighted_objective": weighted,
        })
    return {
        "model": "sum_f area_f * (||G_f||_F^2 + lambda * ||A_f-G_f||_*)",
        "lambda": lam,
        "faces": out,
        "total_objective": total,
    }


def self_test() -> None:
    # Singular values (3,1), lambda=2: G singular values (1,1),
    # while the residual M has singular values (2,0) (rank-one defect).
    A = np.diag([3.0, 1.0, 0.0])[:, :2]
    got = solve_face(A, 2.0)
    np.testing.assert_allclose(got["singular_values_G"], [1.0, 1.0], atol=1e-12)
    np.testing.assert_allclose(got["singular_values_M"], [2.0, 0.0], atol=1e-12)
    assert got["rank_G_opt"] == 2
    assert got["rank_M_opt"] == 1
    np.testing.assert_allclose(got["objective_per_area"], 6.0, atol=1e-12)

    # Rank-one residual: A itself rank one.
    A1 = np.array([[2.0, 0.0], [0.0, 0.0], [0.0, 0.0]])
    got1 = solve_face(A1, 1.0)
    assert got1["rank_M_opt"] == 1
    np.testing.assert_allclose(got1["singular_values_M"], [1.5, 0.0], atol=1e-12)

    # Orthogonal invariance of the solution and objective.
    theta = 0.37
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    Q = np.eye(3)
    Q[:2, :2] = R
    base = solve_face(A, 0.8)
    rotated = solve_face(Q @ A @ R.T, 0.8)
    np.testing.assert_allclose(rotated["objective_per_area"],
                               base["objective_per_area"], atol=1e-10)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="JSON file containing face matrices")
    parser.add_argument("--lambda", dest="lam", type=float, default=1.0,
                        help="nonnegative interface penalty (default: 1)")
    parser.add_argument("--output", type=Path, help="optional output JSON path")
    parser.add_argument("--self-test", action="store_true",
                        help="run deterministic algebraic tests")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        print("SELF-TEST PASS")
    if args.input:
        doc = json.loads(args.input.read_text(encoding="utf-8"))
        result = solve_document(doc, args.lam)
        rendered = json.dumps(result, indent=2, ensure_ascii=False)
        if args.output:
            args.output.write_text(rendered + "\n", encoding="utf-8")
        print(rendered)
    if not args.self_test and not args.input:
        parser.error("provide --input or --self-test")


if __name__ == "__main__":
    main()
