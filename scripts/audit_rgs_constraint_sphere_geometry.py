#!/usr/bin/env python3
"""A15 — audit the exact RGS constraint manifold encoded by A13/A14.

Input: the A13 RGS_PSU_all_matrices.npz containing X_Oh_reconstructed (64,3)
and Q_tangent (192,188).

The four constraint equations define a centered, fixed-radius sphere
S^188(sqrt(240)) in the 189-dimensional zero-centroid subspace of R^192.
This is intrinsic 188D Riemannian geometry, NOT a 4D spacetime tetrad.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import numpy as np


def fro(a: np.ndarray) -> float:
    return float(np.linalg.norm(a, ord="fro"))


def audit(path: Path) -> dict:
    with np.load(path, allow_pickle=False) as z:
        required = ("X_Oh_reconstructed", "Q_tangent")
        missing = [k for k in required if k not in z.files]
        if missing:
            raise KeyError(f"Missing arrays: {missing}")
        X = np.asarray(z["X_Oh_reconstructed"], dtype=float)
        Q = np.asarray(z["Q_tangent"], dtype=float)

    if X.shape != (64, 3) or Q.shape != (192, 188):
        raise ValueError(f"Unexpected shapes: X={X.shape}, Q={Q.shape}")

    x = X.reshape(-1)
    r2 = float(x @ x)
    r = float(np.sqrt(r2))

    # J is the derivative of (sum_i X_i^x, sum_i X_i^y,
    # sum_i X_i^z, 1/2*(||X||^2-r^2)).
    J = np.zeros((4, 192), dtype=float)
    J[0, 0::3] = 1.0
    J[1, 1::3] = 1.0
    J[2, 2::3] = 1.0
    J[3, :] = x

    # Three normalized translation normals and the radial unit normal.
    T = np.zeros((192, 3), dtype=float)
    for a in range(3):
        T[a::3, a] = 1.0 / 8.0
    n = x / r
    N = np.column_stack((T, n))

    Pq = Q @ Q.T
    Pt = np.eye(192) - N @ N.T
    residuals = {
        "centroid_max_abs": float(np.max(np.abs(X.sum(axis=0)))),
        "radius_squared_abs_error_from_240": abs(r2 - 240.0),
        "J_rank": int(np.linalg.matrix_rank(J)),
        "JQ_fro": fro(J @ Q),
        "Q_orthonormality_fro": fro(Q.T @ Q - np.eye(188)),
        "tangent_projector_symmetry_fro": fro(Pq - Pq.T),
        "tangent_projector_idempotence_fro": fro(Pq @ Pq - Pq),
        "canonical_normal_frame_orthonormality_fro": fro(N.T @ N - np.eye(4)),
        "normal_tangent_orthogonality_fro": fro(N.T @ Q),
        "canonical_projector_vs_archived_Q_fro": fro(Pt - Pq),
    }
    thresholds = {
        "centroid_max_abs": 1e-12,
        "radius_squared_abs_error_from_240": 1e-10,
        "JQ_fro": 1e-10,
        "Q_orthonormality_fro": 1e-10,
        "tangent_projector_symmetry_fro": 1e-10,
        "tangent_projector_idempotence_fro": 1e-10,
        "canonical_normal_frame_orthonormality_fro": 1e-10,
        "normal_tangent_orthogonality_fro": 1e-10,
        "canonical_projector_vs_archived_Q_fro": 1e-10,
    }
    checks = {
        key: (residuals[key] < limit)
        for key, limit in thresholds.items()
    }
    rank_pass = residuals["J_rank"] == 4
    checks["J_rank_is_four"] = rank_pass
    status = "PASS" if all(checks.values()) else "FAIL"

    # The manifold is S^188(r) with its induced Euclidean metric.
    dimension = 188
    sectional = 1.0 / r2
    ricci = (dimension - 1) / r2
    scalar = dimension * (dimension - 1) / r2

    return {
        "title": "A15 RGS A13/A14 constraint-manifold geometry audit",
        "status": status,
        "source": str(path),
        "source_arrays": {
            "X_Oh_reconstructed": list(X.shape),
            "Q_tangent": list(Q.shape),
        },
        "constraint_definition": [
            "sum_i X_i^x = 0",
            "sum_i X_i^y = 0",
            "sum_i X_i^z = 0",
            "1/2*(sum_i ||X_i||^2 - 240) = 0",
        ],
        "geometry": {
            "ambient_space": "R^192",
            "centroid_subspace_dimension": 189,
            "constraint_manifold": "S^188(sqrt(240))",
            "dimension": dimension,
            "radius_squared": r2,
            "radius": r,
            "induced_metric": "restriction of the Euclidean metric on R^192",
            "tangent_space": "ker(J) = image(Q_tangent)",
            "tangent_projector": "P_X = I_192 - sum_{a=1}^3 t_a t_a^T - n n^T",
            "translation_normals": "t_a has entries 1/8 in coordinate a at all 64 sites",
            "radial_normal": "n = vec(X)/sqrt(240)",
        },
        "induced_levi_civita": {
            "formula": "nabla_v W = P_X D_v W for tangent vector fields W",
            "second_fundamental_form": "II(v,w) = -( <v,w> / sqrt(240) ) n, using outward radial normal",
            "shape_operator": "S_n = -(1/sqrt(240))*Id under convention S_n(v)=-D_v n",
            "normal_connection": "zero connection coefficients in the global orthonormal frame of three constant translations plus radial normal; D_v n = v/sqrt(240) is tangent",
            "sectional_curvature": sectional,
            "ricci_eigenvalue": ricci,
            "scalar_curvature": scalar,
        },
        "residuals": residuals,
        "checks": checks,
        "scope": {
            "proved_by_constraint_geometry": [
                "The A14 constraint set through the archived X is exactly a centered fixed-radius sphere S^188(sqrt(240)).",
                "The archived Q_tangent spans its tangent space to numerical precision.",
                "The induced Riemannian Levi-Civita connection is the ambient derivative projected onto the tangent space.",
                "The induced metric has constant positive sectional curvature 1/240."
            ],
            "not_established": [
                "A coordinate-dependent 4x4 spacetime coframe.",
                "A Lorentzian metric or a Spin(3,1) spin connection.",
                "A 3+1 splitting or a derived SU(2) connection.",
                "That the archived edgewise SU(2) transports are holonomies of this induced connection.",
                "A physical spacetime interpretation of the 188-dimensional constraint manifold."
            ]
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", type=Path, help="A13 RGS_PSU_all_matrices.npz")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = audit(args.archive)
    rendered = json.dumps(result, indent=2, ensure_ascii=False)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
