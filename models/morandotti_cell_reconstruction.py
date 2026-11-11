"""Finite-dimensional Airy reconstruction for Morandotti cell fields.

The cell fields are ordered (kappa_0^1, kappa_1^1, kappa_2^1, ...).
The interaction matrix must be the Laplacian-product matrix used by the
published postprocessor: M_ij = integral Delta(kappa_i) Delta(kappa_j).
"""
from __future__ import annotations

import numpy as np


def build_defect_vector(centers: np.ndarray, frank_angles: np.ndarray,
                        burgers_vectors: np.ndarray) -> np.ndarray:
    """Build Phi=(s_i, s_i*x_i+b_i2, s_i*y_i-b_i1)_{i=1}^N."""
    x = np.asarray(centers, dtype=float)
    s = np.asarray(frank_angles, dtype=float)
    b = np.asarray(burgers_vectors, dtype=float)
    if x.ndim != 2 or x.shape[1] != 2 or x.shape[0] == 0:
        raise ValueError("centers must have shape (N, 2), with N >= 1")
    n = x.shape[0]
    if s.shape != (n,):
        raise ValueError("frank_angles must have shape (N,)")
    if b.shape != (n, 2):
        raise ValueError("burgers_vectors must have shape (N, 2)")
    if not (np.isfinite(x).all() and np.isfinite(s).all() and np.isfinite(b).all()):
        raise ValueError("defect data must be finite")
    phi = np.empty((n, 3), dtype=float)
    phi[:, 0] = s
    phi[:, 1] = s * x[:, 0] + b[:, 1]
    phi[:, 2] = s * x[:, 1] - b[:, 0]
    return phi.reshape(3 * n)


def solve_interaction_system(interaction_matrix: np.ndarray,
                             defect_vector: np.ndarray) -> np.ndarray:
    """Solve M a = Phi after symmetry and positive-definiteness checks."""
    M = np.asarray(interaction_matrix, dtype=float)
    phi = np.asarray(defect_vector, dtype=float)
    if M.ndim != 2 or M.shape[0] != M.shape[1] or M.shape[0] == 0:
        raise ValueError("interaction_matrix must be non-empty and square")
    if phi.shape != (M.shape[0],):
        raise ValueError("defect_vector length must match interaction_matrix")
    if not (np.isfinite(M).all() and np.isfinite(phi).all()):
        raise ValueError("interaction system must be finite")
    scale = max(float(np.linalg.norm(M, ord="fro")), 1.0)
    if np.linalg.norm(M - M.T, ord="fro") > 1e-10 * scale:
        raise ValueError("interaction_matrix must be symmetric")
    M = 0.5 * (M + M.T)
    try:
        np.linalg.cholesky(M)
    except np.linalg.LinAlgError as exc:
        raise ValueError("interaction_matrix must be positive definite") from exc
    coeff = np.linalg.solve(M, phi)
    if not np.isfinite(coeff).all():
        raise FloatingPointError("interaction solve produced non-finite coefficients")
    return coeff


def reconstruct_airy_potential(cell_fields: np.ndarray, coefficients: np.ndarray,
                               young_modulus: float, poisson_ratio: float) -> np.ndarray:
    """Reconstruct v_h = -E/(1-nu^2) sum_i a_i kappa_i^h pointwise."""
    fields = np.asarray(cell_fields, dtype=float)
    a = np.asarray(coefficients, dtype=float)
    E, nu = float(young_modulus), float(poisson_ratio)
    if fields.ndim < 2 or fields.shape[0] == 0:
        raise ValueError("cell_fields must have shape (3N, ...), with at least one point axis")
    if a.shape != (fields.shape[0],):
        raise ValueError("coefficients length must match the number of cell fields")
    if not np.isfinite(fields).all() or not np.isfinite(a).all():
        raise ValueError("cell fields and coefficients must be finite")
    if not np.isfinite(E) or E <= 0.0:
        raise ValueError("young_modulus must be finite and positive")
    if not np.isfinite(nu) or not (-1.0 < nu < 0.5):
        raise ValueError("poisson_ratio must lie in (-1, 1/2) for the plane-strain model")
    return -(E / (1.0 - nu**2)) * np.tensordot(a, fields, axes=(0, 0))
