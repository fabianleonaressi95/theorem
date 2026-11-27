#!/usr/bin/env python3
"""Finite audit for T150: golden 6D frame and projected-cube zonotope."""
from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

import numpy as np


def projection_matrices() -> tuple[np.ndarray, np.ndarray]:
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    phi_star = (1.0 - math.sqrt(5.0)) / 2.0

    def A(p: float) -> np.ndarray:
        return np.array(
            [
                [0.0, 0.0, 1.0, -1.0, p, p],
                [1.0, -1.0, p, p, 0.0, 0.0],
                [p, p, 0.0, 0.0, 1.0, -1.0],
            ],
            dtype=float,
        )

    return (
        A(phi) / math.sqrt(2.0 * (2.0 + phi)),
        A(phi_star) / math.sqrt(2.0 * (2.0 + phi_star)),
    )


def run_audit() -> dict:
    p_parallel, p_perp = projection_matrices()
    eye3 = np.eye(3)
    frame_residuals = {
        "parallel_orthonormal": float(np.linalg.norm(p_parallel @ p_parallel.T - eye3)),
        "perp_orthonormal": float(np.linalg.norm(p_perp @ p_perp.T - eye3)),
        "cross_orthogonal": float(np.linalg.norm(p_parallel @ p_perp.T)),
    }

    generators = 0.5 * p_perp
    triple_determinants = [
        float(np.linalg.det(generators[:, triple]))
        for triple in itertools.combinations(range(6), 3)
    ]
    min_abs_det = min(abs(value) for value in triple_determinants)

    states = list(itertools.product((0, 1), repeat=6))
    points = np.array(
        [p_perp @ (np.asarray(state, dtype=float) - 0.5) for state in states]
    )
    distinct_count = int(np.unique(np.round(points, decimals=12), axis=0).shape[0])
    antipodal_residual = max(
        float(np.linalg.norm(points[index] + points[-1 - index]))
        for index in range(64)
    )

    # Every projected cube corner belongs to the projected cube by construction.
    # This check independently reconstructs it from the signed generators.
    signed_points = np.array(
        [
            sum((1.0 if bit else -1.0) * generators[:, i] for i, bit in enumerate(state))
            for state in states
        ]
    )
    reconstruction_residual = float(np.max(np.linalg.norm(points - signed_points, axis=1)))

    return {
        "frame_residuals": frame_residuals,
        "generator_triple_count": len(triple_determinants),
        "minimum_absolute_generator_triple_determinant": min_abs_det,
        "all_generator_triples_independent_numerically": bool(min_abs_det > 1e-12),
        "q6_state_count": len(states),
        "distinct_internal_projected_points_rounded_1e-12": distinct_count,
        "antipodal_pairing_max_residual": antipodal_residual,
        "minkowski_sum_reconstruction_max_residual": reconstruction_residual,
        "zonotope_combinatorics_if_general_position": {
            "vertices": 32,
            "edges": 60,
            "rhombic_facets": 30,
        },
        "classification": (
            "finite numerical audit; zonotope counts follow from 3D general-position "
            "combinatorics; no IVM/FCC isomorphism or Lorentzian continuum limit tested"
        ),
    }


def main() -> None:
    result = run_audit()
    output = Path("audits/Q6_GOLDEN_ZONOTOPE_T150_AUDIT.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
