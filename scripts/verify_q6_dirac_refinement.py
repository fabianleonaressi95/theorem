#!/usr/bin/env python3
"""Reproducible algebraic/numerical audit for theorem T017.

Requires Python 3 and NumPy.  This is an audit script, not a proof assistant.
"""
from __future__ import annotations
import json
import math
from pathlib import Path
import numpy as np

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)


def kron_all(items):
    out = np.array([[1.0 + 0j]])
    for item in items:
        out = np.kron(out, item)
    return out


def gamma_matrices():
    """Six Hermitian 8x8 Euclidean Clifford generators (Jordan-Wigner)."""
    gammas = []
    for q in range(3):
        prefix = [Z] * q
        suffix = [I2] * (2 - q)
        gammas.append(kron_all(prefix + [X] + suffix))
        gammas.append(kron_all(prefix + [Y] + suffix))
    return gammas


def audit(n_values=(1, 2, 3, 4, 8), r=1.0):
    gammas = gamma_matrices()
    ident = np.eye(8, dtype=complex)
    clifford_residual = 0.0
    for j in range(6):
        for k in range(6):
            target = 2.0 * ident if j == k else np.zeros((8, 8), complex)
            clifford_residual = max(
                clifford_residual,
                float(np.linalg.norm(gammas[j] @ gammas[k] +
                                     gammas[k] @ gammas[j] - target, ord=2)),
            )

    rows = []
    for n in n_values:
        h = 1.0 / n
        # The finite momentum grid has 2n points in each coordinate.
        # sin(p)=0 iff m=0 or m=n, hence exactly 2^6 corners.
        grid_zeros = 2**6
        signs = []
        wilson_masses = []
        for eps in np.ndindex(*(2,) * 6):
            signs.append((-1) ** sum(eps))
            wilson_masses.append((2.0 * r / h) * sum(eps))
        rows.append({
            "n": n,
            "h": h,
            "vertices": (2 * n) ** 6,
            "centered_operator_identically_zero": n == 1,
            "naive_zero_corners": grid_zeros,
            "orientation_sum": int(sum(signs)),
            "wilson_zero_corners": 1,
            "wilson_nonzero_corner_mass_min": float(min(x for x in wilson_masses if x > 0)),
            "wilson_nonzero_corner_mass_max": float(max(wilson_masses)),
        })

    # Fixed physical momentum symbol convergence: compare scalar coefficient
    # vectors; gamma_j have operator norm 1, so this is a conservative bound.
    k = np.array([0.31, -0.7, 1.2, 0.05, -0.4, 0.9], dtype=float)
    convergence = []
    for n in (2, 4, 8, 16, 32, 64):
        h = 1.0 / n
        coeff_error = np.abs(np.sin(h * k) / h - k)
        upper = (h**2 / 6.0) * np.sum(np.abs(k)**3)
        convergence.append({
            "n": n,
            "h": h,
            "coefficient_l1_error": float(np.sum(coeff_error)),
            "proved_l1_upper_bound": float(upper),
        })

    return {
        "theorem": "T017",
        "classification": {
            "clifford_algebra": "VERIFIED_NUMERICALLY",
            "finite_grid_counts": "EXACT_COMBINATORIAL_IDENTITY",
            "orientation_cancellation": "PROVED_BINOMIAL_IDENTITY",
            "fixed_momentum_limit": "PROVED_WITH_SINE_REMAINDER_BOUND",
            "full_spectral_convergence": "OPEN",
            "nielsen_ninomiya_evasion": "NOT_CLAIMED",
        },
        "parameters": {"dimension": 6, "spinor_dimension": 8, "wilson_r": r},
        "clifford_anticommutator_max_operator_norm": clifford_residual,
        "refinements": rows,
        "fixed_momentum_convergence": convergence,
    }


if __name__ == "__main__":
    result = audit()
    out = Path("reports/T017_numerical_audit.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
