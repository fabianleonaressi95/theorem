#!/usr/bin/env python3
"""Audit archived RGS discrete geometry inputs without inventing a continuum tetrad.

Usage:
  python scripts/audit_rgs_coframe_spin_connection_inputs.py path/to/psu_fibre_connection_matrices.npz

The archive contains a 3D point cloud and discrete SO(3)/SU(2) edge transports.
It does not contain a coordinate-dependent 4D coframe, so this script deliberately
does not construct a Levi-Civita or spin connection.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    with np.load(args.archive, allow_pickle=False) as data:
        required = ("X", "Q", "K0", "normals", "edges", "R_SO3", "U_SU2")
        missing = [key for key in required if key not in data.files]
        if missing:
            raise SystemExit(f"Missing required arrays: {missing}")
        X, Q, K0, normals, edges, R, U = (data[k] for k in required)

    if X.shape != (64, 3) or Q.shape != (192, 188):
        raise SystemExit(f"Unexpected geometry shapes: X={X.shape}, Q={Q.shape}")
    if normals.shape != (64, 3) or edges.shape != (192, 3):
        raise SystemExit(f"Unexpected normals/edges shapes: {normals.shape}, {edges.shape}")
    if R.shape != (192, 3, 3) or U.shape != (192, 2, 2):
        raise SystemExit(f"Unexpected transport shapes: R={R.shape}, U={U.shape}")

    I3, I2 = np.eye(3), np.eye(2)
    centered_rank = int(np.linalg.matrix_rank(X - X.mean(axis=0)))
    normal_res = float(np.max(np.abs(np.linalg.norm(normals, axis=1) - 1)))
    R_orth = float(np.max(np.linalg.norm(np.swapaxes(R, -1, -2) @ R - I3, axis=(1, 2))))
    R_det = float(np.max(np.abs(np.linalg.det(R) - 1)))
    U_unit = float(np.max(np.linalg.norm(np.swapaxes(U.conj(), -1, -2) @ U - I2, axis=(1, 2))))
    U_det = float(np.max(np.abs(np.linalg.det(U) - 1)))

    # Adjoint action: U sigma_j U^dagger = R_ij sigma_i.
    sigma = np.array([
        [[0, 1], [1, 0]],
        [[0, -1j], [1j, 0]],
        [[1, 0], [0, -1]],
    ], dtype=complex)
    R_from_U = np.empty_like(R)
    for k, u in enumerate(U):
        for j in range(3):
            transformed = u @ sigma[j] @ u.conj().T
            R_from_U[k, :, j] = [np.trace(sigma[i] @ transformed).real / 2 for i in range(3)]
    adjoint_res = float(np.max(np.abs(R - R_from_U)))

    result = {
        "archive": str(args.archive),
        "classification": {
            "3d_discrete_embedding": "PASS",
            "archived_SO3_edge_transports": "PASS" if R_orth < 1e-12 and R_det < 1e-12 else "FAIL",
            "archived_SU2_edge_transports": "PASS" if U_unit < 1e-12 and U_det < 1e-12 else "FAIL",
            "SU2_to_SO3_adjoint_compatibility": "PASS" if adjoint_res < 1e-12 else "FAIL",
            "coordinate_dependent_4d_coframe": "NOT_PRESENT_IN_ARCHIVE",
            "Levi_Civita_spin_connection_from_coframe": "NOT_COMPUTABLE",
            "continuum_to_Q6_holonomy_convergence": "NOT_TESTED",
        },
        "shapes": {
            "X": list(X.shape), "Q": list(Q.shape), "K0": list(K0.shape),
            "normals": list(normals.shape), "edges": list(edges.shape),
            "R_SO3": list(R.shape), "U_SU2": list(U.shape),
        },
        "numerical_residuals": {
            "centered_embedding_rank": centered_rank,
            "unit_normal_max_abs_residual": normal_res,
            "SO3_orthogonality_max_fro_residual": R_orth,
            "SO3_determinant_max_abs_residual": R_det,
            "SU2_unitarity_max_fro_residual": U_unit,
            "SU2_determinant_max_abs_residual": U_det,
            "SU2_adjoint_to_SO3_max_abs_residual": adjoint_res,
            "K0_symmetry_fro_residual": float(np.linalg.norm(K0 - K0.T)),
        },
        "interpretation": (
            "The archive supports a 3D discrete embedding and mutually compatible "
            "edgewise SO(3)/SU(2) transports. These are archived discrete transports; "
            "they are not shown to be sampled from a continuum Levi-Civita spin "
            "connection. No coordinate-dependent 4D coframe or derivatives are present."
        ),
        "required_missing_inputs": [
            "coordinate domain/chart and coordinate-dependent invertible coframe e^a_mu(x)",
            "signature and internal metric convention",
            "derivative data or a specified discrete differential calculus for e^a_mu",
            "for SU(2) reduction: a unit timelike field / 3+1 split and spatial triad",
            "edge paths or a documented map from continuum connection to Q6 links",
        ],
    }
    rendered = json.dumps(result, indent=2, ensure_ascii=False)
    print(rendered)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
