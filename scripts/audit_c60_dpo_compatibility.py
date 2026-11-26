#!/usr/bin/env python3
"""Algebraic compatibility checks for the C60 surface-valued DPO ansatz.

This is deliberately NOT an injectivity or DPO-admissibility proof.  It checks
only the facewise 3x2 algebra for orthonormal tangent frames and SO(2) fields.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def rot(angle: float) -> np.ndarray:
    c, s = np.cos(angle), np.sin(angle)
    return np.array([[c, -s], [s, c]], dtype=float)


def face_fields(B: np.ndarray, phi: float, theta: float):
    E = rot(phi)
    D = rot(theta)
    F = B @ E                 # approximate/macroscopic gradient ∇g
    G = B @ D                 # deformation without disarrangements
    M = F - G
    return F, G, M


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    # Canonical oriented orthonormal 2-frame in R^3.  The identities below
    # are frame-covariant, so one exact frame suffices for the algebra audit.
    B = np.array([[1., 0.], [0., 1.], [0., 0.]])
    normal = np.cross(B[:, 0], B[:, 1])

    deltas = np.linspace(-np.pi, np.pi, 257)
    rank_min = 2
    area_min = float("inf")
    orientation_min = float("inf")
    formula_error = 0.0
    isometry_error = 0.0
    determinant_error = 0.0

    for delta in deltas:
        F, G, M = face_fields(B, float(delta), 0.0)
        singular_values = np.linalg.svd(F, compute_uv=False)
        rank_min = min(rank_min, int(np.sum(singular_values > 1e-12)))
        area = float(np.sqrt(np.linalg.det(F.T @ F)))
        area_min = min(area_min, area)
        orientation = float(np.dot(np.cross(F[:, 0], F[:, 1]), normal))
        orientation_min = min(orientation_min, orientation)

        expected = 4.0 * (1.0 - np.cos(delta))
        actual = float(np.linalg.norm(M, ord="fro") ** 2)
        formula_error = max(formula_error, abs(actual - expected))
        isometry_error = max(
            isometry_error,
            float(np.linalg.norm(F.T @ F - np.eye(2), ord="fro")),
            float(np.linalg.norm(G.T @ G - np.eye(2), ord="fro")),
        )

        # Canonical normal extension to a 3x3 rotation, face by face.
        # This confirms det=+1 locally, but does not provide a globally
        # compatible thickening across edges/vertices.
        Q = B @ rot(float(delta)) @ B.T + np.outer(normal, normal)
        determinant_error = max(
            determinant_error,
            abs(float(np.linalg.det(Q)) - 1.0),
            float(np.linalg.norm(Q.T @ Q - np.eye(3), ord="fro")),
        )

    # In the tree-faithful choice phi=theta, ∇g=G and M vanishes identically.
    F0, G0, M0 = face_fields(B, 0.37, 0.37)
    zero_M = float(np.linalg.norm(M0, ord="fro"))

    result = {
        "title": "C60 surface DPO ansatz: facewise algebraic compatibility",
        "status": "ALGEBRAIC_CHECKS_ONLY_NOT_DPO_ADMISSIBILITY",
        "conventions": {
            "F": "B @ R(phi), the approximate/macroscopic gradient",
            "G": "B @ R(theta), the deformation without disarrangements",
            "M": "F - G",
            "norm": "standard Frobenius norm (not half the squared Frobenius norm)",
        },
        "checks": {
            "sampled_angle_differences": int(len(deltas)),
            "minimum_rank_F": rank_min,
            "minimum_area_jacobian_F": area_min,
            "minimum_oriented_area": orientation_min,
            "max_isometry_residual_F_G": isometry_error,
            "max_M_norm_formula_residual": formula_error,
            "max_normal_extension_SO3_residual": determinant_error,
            "M_zero_when_phi_equals_theta": zero_M,
        },
        "identities": {
            "J2(B R(phi))": "1 for B^T B=I_2 and R(phi) in SO(2)",
            "||B(R(phi)-R(theta))||_F^2":
                "4*(1-cos(phi-theta)); equals 2*(1-cos(...)) only for half-Frobenius energy",
        },
        "not_checked": [
            "global injectivity of the piecewise map on the 32-face surface",
            "non-overlap of images of distinct faces and correct edge/vertex incidence",
            "a globally compatible thickening of the surface map to a 3D body",
            "the DPO accommodation condition for a justified 3D extension",
            "existence of injective piecewise-smooth determining maps f_n",
            "convergence f_n -> g and gradients of f_n -> G",
        ],
    }
    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    if args.out is not None:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
