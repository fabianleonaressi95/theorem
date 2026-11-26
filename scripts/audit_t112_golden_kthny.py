#!/usr/bin/env python3
"""Exact/numerical sanity checks for the T112 golden integer-lattice map.

This is not a KTHNY simulation. It audits only the imposed GL(2,Z) map and
its coordinate-covariance identity.
"""
from __future__ import annotations

import argparse
import json
import numpy as np


A = np.array([[1, 1], [1, 0]], dtype=np.int64)


def fibonacci_matrix(n: int) -> np.ndarray:
    if n < 1:
        raise ValueError("n must be >= 1")
    out = np.linalg.matrix_power(A, n)
    return out


def audit(n_max: int = 12) -> dict:
    det = round(float(np.linalg.det(A)))
    eig = np.sort(np.linalg.eigvals(A.astype(float)))
    phi = (1.0 + np.sqrt(5.0)) / 2.0
    powers = []
    for n in range(1, n_max + 1):
        m = fibonacci_matrix(n)
        powers.append({"n": n, "matrix": m.tolist(),
                       "det": round(float(np.linalg.det(m)))})
    # Coordinate covariance: b'=A b, G'=A^{-T} G A^{-1}.
    G = np.array([[2.0, 0.25], [0.25, 1.5]])
    b = np.array([2.0, -1.0])
    Ai = np.linalg.inv(A.astype(float))
    bp = A @ b
    Gp = Ai.T @ G @ Ai
    e0 = float(b @ G @ b)
    e1 = float(bp @ Gp @ bp)
    return {
        "det_A": det,
        "eigenvalues": sorted(float(x) for x in eig),
        "phi": float(phi),
        "negative_inverse_phi": float(-1.0 / phi),
        "eigenvalue_residual": float(max(abs(eig - np.array([phi, -1.0 / phi])))),
        "powers": powers,
        "coordinate_energy_before": e0,
        "coordinate_energy_after": e1,
        "coordinate_covariance_residual": abs(e0 - e1),
        "scope": "algebraic audit only; no KTHNY dynamics or critical scaling",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=12)
    args = parser.parse_args()
    print(json.dumps(audit(args.n_max), indent=2))


if __name__ == "__main__":
    main()
