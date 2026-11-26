#!/usr/bin/env python3
"""Deterministic C01-C04 spectral controls for the cymatics programme.

Requires Python >=3.10 and NumPy. These are mathematical benchmarks, not
experimental Chladni data and not a helicon/plasma simulation.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

import numpy as np


def square_dirichlet_laplacian(n: int, length: float = 1.0) -> np.ndarray:
    """Positive five-point -Delta on an n x n interior grid."""
    if n < 2 or length <= 0:
        raise ValueError("n must be >=2 and length must be positive")
    h = length / (n + 1)
    one = np.diag(np.full(n, 2.0)) + np.diag(np.full(n - 1, -1.0), 1) + np.diag(np.full(n - 1, -1.0), -1)
    return (np.kron(np.eye(n), one) + np.kron(one, np.eye(n))) / (h * h)


def plate_spectrum(n: int = 18, length: float = 1.0) -> tuple[np.ndarray, np.ndarray]:
    """Simply supported square Kirchhoff-Love plate, dimensionless D_b/(rho*h)=1.

    The discrete biharmonic stiffness is L @ L, where L is the positive
    Dirichlet finite-difference Laplacian. Its eigenvectors are those of L.
    """
    lap = square_dirichlet_laplacian(n, length)
    stiffness = lap @ lap
    values, vectors = np.linalg.eigh(stiffness)
    return values, vectors


def discrete_laplacian_eigenvalue(n: int, p: int, q: int, length: float = 1.0) -> float:
    h = length / (n + 1)
    return 4.0 / (h * h) * (
        math.sin(p * math.pi / (2 * (n + 1))) ** 2
        + math.sin(q * math.pi / (2 * (n + 1))) ** 2
    )


def q6_laplacian_spectrum() -> tuple[np.ndarray, np.ndarray]:
    """Return sorted eigenvalues and multiplicities of the 6-cube graph Laplacian."""
    nbits = 6
    adjacency = np.zeros((1 << nbits, 1 << nbits), dtype=float)
    for vertex in range(1 << nbits):
        for bit in range(nbits):
            adjacency[vertex, vertex ^ (1 << bit)] = 1.0
    laplacian = np.diag(adjacency.sum(axis=1)) - adjacency
    values = np.linalg.eigvalsh(laplacian)
    unique, counts = np.unique(np.rint(values).astype(int), return_counts=True)
    return unique, counts


def run_benchmarks(n: int = 18) -> dict[str, Any]:
    # C01: lowest plate eigenvalues against the exact discrete FD spectrum.
    values, vectors = plate_spectrum(n)
    expected = sorted(
        (
            discrete_laplacian_eigenvalue(n, p, q) ** 2,
            p,
            q,
        )
        for p in range(1, n + 1)
        for q in range(1, n + 1)
    )
    c01 = {
        "grid_interior": n,
        "max_abs_error_first_12": float(
            max(abs(values[i] - expected[i][0]) for i in range(12))
        ),
        "continuum_relative_error_mode_11": float(
            abs(math.sqrt(values[0]) - 2 * math.pi**2) / (2 * math.pi**2)
        ),
        "first_mode_vector_norm": float(np.linalg.norm(vectors[:, 0])),
    }

    # C02: square symmetry gives exact (1,2)/(2,1) degeneracy.
    e12 = discrete_laplacian_eigenvalue(n, 1, 2) ** 2
    e21 = discrete_laplacian_eigenvalue(n, 2, 1) ** 2
    c02 = {
        "mode_12": e12,
        "mode_21": e21,
        "absolute_degeneracy_gap": abs(e12 - e21),
    }

    # C03: a localized asymmetric stiffness perturbation splits the pair.
    lap = square_dirichlet_laplacian(n)
    stiffness = lap @ lap
    perturbation = np.zeros_like(stiffness)
    # Choose an off-centre grid point where the (1,2) and (2,1) modes
    # have different amplitudes; the central point is nodal for both.
    row, col = n // 3, n // 4
    idx = row * n + col
    perturbation[idx, idx] = 0.05 * float(np.max(np.diag(stiffness)))
    perturbed_values = np.linalg.eigvalsh(stiffness + perturbation)
    # The unperturbed (1,2)/(2,1) pair occupies sorted indices 1 and 2.
    c03 = {
        "perturbation_relative_diagonal": 0.05,
        "unperturbed_pair_gap": float(values[2] - values[1]),
        "perturbed_pair_gap": float(perturbed_values[2] - perturbed_values[1]),
    }

    # C04: Q6 hypercube graph Laplacian eigenvalues 2k, multiplicity C(6,k).
    q6_values, q6_counts = q6_laplacian_spectrum()
    q6_expected_values = np.arange(0, 13, 2, dtype=int)
    q6_expected_counts = np.array([1, 6, 15, 20, 15, 6, 1], dtype=int)
    c04 = {
        "eigenvalues": q6_values.tolist(),
        "multiplicities": q6_counts.tolist(),
        "expected_eigenvalues": q6_expected_values.tolist(),
        "expected_multiplicities": q6_expected_counts.tolist(),
        "exact_integer_spectrum_match": bool(
            np.array_equal(q6_values, q6_expected_values)
            and np.array_equal(q6_counts, q6_expected_counts)
        ),
        "interpretation": "Q6 graph control only; not a plate or plasma discretization",
    }

    return {
        "schema": "cymatics-wave-benchmarks/v1",
        "model": "dimensionless simply-supported square Kirchhoff-Love plate and Q6 graph control",
        "numpy_version": np.__version__,
        "C01": c01,
        "C02": c02,
        "C03": c03,
        "C04": c04,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--grid", type=int, default=18)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run_benchmarks(args.grid)
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
