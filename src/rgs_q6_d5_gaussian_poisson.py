"""Gaussian theta/Poisson cross-check on finite-rank Q6-D5 fibre slices.

This is a controlled diagnostic on an explicitly selected rank-r sublattice
of the rank-124 fibre. It is NOT the full 124-dimensional Wilson fibre sum.
The Gram matrix and its inverse/determinant are exact SymPy rationals;
finite Gaussian sums and analytic tail envelopes are evaluated in float64.
"""
from __future__ import annotations

import itertools
import math

import numpy as np
import sympy as sp

from src.rgs_q6_d5_saturated_kernel_bounds import (
    build_q6_d5_saturated_integer_kernel,
)
from src.rgs_q6_u1_character_electric_flux import build_q6_integer_cycle_basis


def q6_d5_fiber_gaussian_gram(rank: int = 3) -> dict:
    """Build the exact Gram matrix for the first rank saturated fibre rows."""
    if not isinstance(rank, int) or rank < 1 or rank > 124:
        raise ValueError("rank must be an integer in [1, 124]")
    kernel = build_q6_d5_saturated_integer_kernel()
    cycles = sp.Matrix(build_q6_integer_cycle_basis().tolist())
    edge_lattice = kernel["kernel_basis"] * cycles
    basis = edge_lattice[:rank, :]
    if basis.rank() != rank:
        raise ArithmeticError("selected fibre rows are not independent")
    gram = basis * basis.T
    if gram != gram.T or gram.det() <= 0:
        raise ArithmeticError("fibre Gram matrix is not positive definite")
    return {
        "rank": rank,
        "edge_lattice_basis": basis,
        "gram": gram,
        "gram_inverse": gram.inv(),
        "gram_determinant": gram.det(),
        "exact_positive_definite": True,
    }


def _one_dimensional_gaussian_sum_bound(a: float) -> float:
    """Upper bound for sum_{k in Z} exp(-a k^2), a>0."""
    if a <= 0 or not math.isfinite(a):
        raise ValueError("a must be finite and positive")
    return 1.0 + 2.0 * math.exp(-a) / (-math.expm1(-3.0 * a))


def _one_dimensional_gaussian_tail_bound(a: float, cutoff: int) -> float:
    """Upper bound for sum_{|k|>cutoff} exp(-a k^2)."""
    if a <= 0 or not math.isfinite(a) or cutoff < 0:
        raise ValueError("a must be positive finite and cutoff nonnegative")
    first = cutoff + 1
    ratio = math.exp(-a * (2 * first + 1))
    if ratio >= 1.0:
        return math.inf
    return 2.0 * math.exp(-a * first * first) / (1.0 - ratio)


def _cube_tail_bound(a: float, rank: int, cutoff: int) -> float:
    """Union-bound remainder outside [-cutoff,cutoff]^rank."""
    one_sum = _one_dimensional_gaussian_sum_bound(a)
    one_tail = _one_dimensional_gaussian_tail_bound(a, cutoff)
    return rank * one_tail * one_sum ** (rank - 1)


def _theta_cube(matrix: np.ndarray, coefficient: float, cutoff: int) -> float:
    rank = matrix.shape[0]
    total = 0.0
    for vector in itertools.product(range(-cutoff, cutoff + 1), repeat=rank):
        x = np.asarray(vector, dtype=float)
        total += math.exp(-coefficient * float(x @ matrix @ x))
    return total


def q6_d5_gaussian_poisson_crosscheck(rank: int = 3, t: float = 1.0,
                                      cutoff: int = 5) -> dict:
    r"""Compare both sides of
       sum_m exp(-pi*t*m'Gm) =
       t^(-r/2)/sqrt(det G) sum_n exp(-pi/t*n'G^-1*n).
    """
    if not math.isfinite(t) or t <= 0:
        raise ValueError("t must be finite and positive")
    if not isinstance(cutoff, int) or cutoff < 0:
        raise ValueError("cutoff must be a nonnegative integer")
    data = q6_d5_fiber_gaussian_gram(rank)
    gram = data["gram"]
    inverse = data["gram_inverse"]
    g = np.asarray(gram, dtype=float)
    g_inv = np.asarray(inverse, dtype=float)
    det_g = float(data["gram_determinant"])
    if not math.isfinite(det_g) or det_g <= 0:
        raise FloatingPointError("Gram determinant is outside float64 range")
    prefactor = t ** (-rank / 2.0) / math.sqrt(det_g)

    direct_a = math.pi * t / float(sp.trace(inverse))
    dual_a = math.pi / (t * float(sp.trace(gram)))
    direct_partial = _theta_cube(g, math.pi * t, cutoff)
    dual_partial = _theta_cube(g_inv, math.pi / t, cutoff)
    direct_tail = _cube_tail_bound(direct_a, rank, cutoff)
    dual_tail = prefactor * _cube_tail_bound(dual_a, rank, cutoff)
    direct_interval = [direct_partial, direct_partial + direct_tail]
    dual_interval = [
        prefactor * dual_partial,
        prefactor * dual_partial + dual_tail,
    ]
    overlap = max(direct_interval[0], dual_interval[0]) <= min(
        direct_interval[1], dual_interval[1]
    )
    return {
        "audit": "Q6_D5_GAUSSIAN_POISSON_FIBER_SLICE",
        "rank": rank,
        "full_fiber_rank": 124,
        "t": float(t),
        "cube_cutoff": cutoff,
        "gram_exact": [[str(gram[i, j]) for j in range(rank)] for i in range(rank)],
        "gram_determinant_exact": str(data["gram_determinant"]),
        "gram_inverse_exact": [
            [str(inverse[i, j]) for j in range(rank)] for i in range(rank)
        ],
        "direct_partial_sum": direct_partial,
        "direct_tail_envelope": direct_tail,
        "direct_enclosure": direct_interval,
        "dual_partial_sum_with_prefactor": prefactor * dual_partial,
        "dual_tail_envelope_with_prefactor": dual_tail,
        "dual_enclosure": dual_interval,
        "enclosures_overlap": bool(overlap),
        "scope": {
            "exact": [
                "integer fibre-slice basis",
                "positive-definite Gram matrix",
                "Gram inverse and determinant",
                "Poisson theta identity for the selected full-rank slice",
            ],
            "numerical": [
                "finite direct and dual Gaussian sums",
                "float64 analytic Gaussian tail envelopes",
            ],
            "not_claimed": [
                "full rank-124 Gaussian theta sum evaluated",
                "Gaussian approximation equals the Bessel/Wilson fibre sum",
                "uniform Gaussian approximation at finite beta",
                "certified interval with directed-rounding arithmetic",
            ],
        },
    }
