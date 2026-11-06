#!/usr/bin/env python3
"""Sampled Koopman/observable-closure audit for the 3D totalistic CA.

Dependencies: numpy
Run: python audit_koopman.py

This is a diagnostic, not a proof of an invariant 3D Koopman subspace.
It tests whether a natural vector of first Fourier moments closes linearly
under one CA step. The 24-rotation orbit augmentation reduces sampling bias.
"""
from __future__ import annotations
import itertools
import json
import numpy as np


def cubic_rotations():
    rotations = []
    for perm in itertools.permutations(range(3)):
        P = np.zeros((3, 3), dtype=int)
        for i, j in enumerate(perm):
            P[i, j] = 1
        for signs in itertools.product((-1, 1), repeat=3):
            R = np.diag(signs) @ P
            if round(np.linalg.det(R)) == 1:
                rotations.append(R)
    assert len(rotations) == 24
    return rotations


def rotate(a: np.ndarray, R: np.ndarray) -> np.ndarray:
    L = a.shape[0]
    out = np.zeros_like(a)
    for x in np.ndindex(a.shape):
        y = tuple((R @ np.asarray(x, dtype=int) % L).tolist())
        out[y] = a[x]
    return out


def update(a: np.ndarray, rule: np.ndarray) -> np.ndarray:
    neighbors = np.zeros_like(a, dtype=np.int16)
    for delta in itertools.product((-1, 0, 1), repeat=3):
        if delta != (0, 0, 0):
            neighbors += np.roll(a, shift=delta, axis=(0, 1, 2))
    q = 27 * a.astype(np.int16) + neighbors
    if q.min() < 0 or q.max() > 53:
        raise AssertionError("lookup index outside [0,53]")
    return rule[q]


def vector_observable(a: np.ndarray) -> np.ndarray:
    """Three sine first moments; transform as the cubic vector representation."""
    L = a.shape[0]
    s = np.sin(2.0 * np.pi * np.arange(L) / L)
    return np.array([
        np.einsum("ijk,i->", a, s),
        np.einsum("ijk,j->", a, s),
        np.einsum("ijk,k->", a, s),
    ], dtype=float) / a.size


def main():
    seed = 20261106
    rng = np.random.default_rng(seed)
    L = 3
    rule = rng.integers(0, 2, size=54, dtype=np.uint8)
    rotations = cubic_rotations()

    # Orbit augmentation: each sampled configuration contributes all 24 rotations.
    n_base = 1000
    X_rows, Y_rows = [], []
    equivariance_mismatches = 0
    for _ in range(n_base):
        a = rng.integers(0, 2, size=(L, L, L), dtype=np.uint8)
        Fa = update(a, rule)
        for R in rotations:
            Ra = rotate(a, R)
            RFa = rotate(Fa, R)
            F_Ra = update(Ra, rule)
            equivariance_mismatches += int(np.count_nonzero(F_Ra != RFa))
            X_rows.append(vector_observable(Ra))
            Y_rows.append(vector_observable(F_Ra))

    X = np.asarray(X_rows)
    Y = np.asarray(Y_rows)
    # Fit K f ~= A f in column-vector convention: y ~= A x.
    A = np.linalg.lstsq(X, Y, rcond=None)[0].T
    residual = Y - X @ A.T
    relative_closure_error = float(np.linalg.norm(residual) / np.linalg.norm(Y))
    eig = np.linalg.eigvals(A)
    psi = 1.465571231876768
    psi_polynomial_residual = float(psi**3 - psi**2 - 1.0)
    fitted_eigenvalue_polynomial_residuals = [
        float(abs(z**3 - z**2 - 1.0)) for z in eig
    ]
    isotropic_scalar = float(np.trace(A).real / 3.0)
    anisotropy = float(np.linalg.norm(A - isotropic_scalar * np.eye(3)))

    result = {
        "status": "DIAGNOSTIC_ONLY",
        "seed": seed,
        "lattice": [L, L, L],
        "rule_table_length": int(rule.size),
        "proper_cubic_rotations": len(rotations),
        "base_configurations": n_base,
        "orbit_augmented_samples": int(X.shape[0]),
        "update_equivariance_mismatches": equivariance_mismatches,
        "observable": "three sine first Fourier moments",
        "fitted_projected_matrix_A": A.tolist(),
        "fitted_projected_eigenvalues": [
            {"real": float(z.real), "imag": float(z.imag)} for z in eig
        ],
        "relative_linear_closure_error": relative_closure_error,
        "isotropic_scalar_trace_over_3": isotropic_scalar,
        "distance_from_scalar_matrix": anisotropy,
        "psi": psi,
        "psi_cubic_polynomial_residual": psi_polynomial_residual,
        "fitted_eigenvalue_polynomial_residuals_abs": fitted_eigenvalue_polynomial_residuals,
        "interpretation": [
            "The tested CA update is exactly cubic-equivariant on the sampled configurations.",
            "The selected three-observable span is not closed to useful accuracy if the relative closure error is large.",
            "The least-squares matrix is a projected regression, not an exact Koopman restriction.",
            "No supergolden eigenvalue is established by this experiment.",
        ],
    }
    print(json.dumps(result, indent=2))
    if equivariance_mismatches != 0:
        raise SystemExit("FAIL: cubic equivariance mismatch")


if __name__ == "__main__":
    main()
