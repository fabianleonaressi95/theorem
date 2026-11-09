"""Exact Schur complement and finite-beta Bessel/Gaussian fibre-slice audit.

This module compares the exact normalized Wilson character weight
    prod_e I_{|n_e|}(beta)/I_0(beta)
against its weak-coupling Gaussian approximation
    exp(-||n||_2^2/(2 beta))
on a finite integer slice of the Q6-D5 saturated fibre.

The comparison is finite and explicit; it does not assert equality or a
uniform approximation on the complete rank-124 fibre.
"""
from __future__ import annotations

import itertools
import math

import numpy as np
import sympy as sp
from scipy.special import ive

from src.rgs_q6_d5_gaussian_poisson import q6_d5_fiber_gaussian_gram


def q6_d5_exact_schur_complement(rank: int = 4, split: int = 2) -> dict:
    """Return exact Schur complement for G=[[A,B],[B.T,C]], with split size."""
    if not isinstance(split, int) or not isinstance(rank, int):
        raise ValueError("rank and split must be integers")
    if rank < 2 or split < 1 or split >= rank:
        raise ValueError("require rank >= 2 and 1 <= split < rank")
    G = q6_d5_fiber_gaussian_gram(rank)["gram"]
    A = G[:split, :split]
    B = G[:split, split:]
    C = G[split:, split:]
    S = C - B.T * A.inv() * B
    if S != S.T or S.det() <= 0:
        raise ArithmeticError("Schur complement is not positive definite")
    det_identity = sp.simplify(G.det() - A.det() * S.det())
    return {
        "rank": rank,
        "split": split,
        "gram": G,
        "A": A,
        "B": B,
        "C": C,
        "schur_complement": S,
        "det_gram": G.det(),
        "det_A": A.det(),
        "det_schur": S.det(),
        "determinant_identity_residual": det_identity,
        "exact_checks": {
            "schur_symmetric": S == S.T,
            "schur_positive_definite": S.det() > 0,
            "determinant_factorization": det_identity == 0,
        },
    }


def q6_d5_bessel_gaussian_slice(beta: float = 20.0, rank: int = 2,
                                cutoff: int = 2) -> dict:
    """Compare Bessel Wilson and Gaussian weights over a finite integer cube."""
    if not math.isfinite(beta) or beta <= 0:
        raise ValueError("beta must be finite and positive")
    if not isinstance(rank, int) or rank < 1 or rank > 124:
        raise ValueError("rank must be an integer in [1,124]")
    if not isinstance(cutoff, int) or cutoff < 0:
        raise ValueError("cutoff must be a nonnegative integer")
    data = q6_d5_fiber_gaussian_gram(rank)
    edge_basis = np.asarray(data["edge_lattice_basis"], dtype=np.int64)
    bessel_norm = float(ive(0, beta))
    if bessel_norm <= 0 or not math.isfinite(bessel_norm):
        raise FloatingPointError("I_0(beta) scaled value is invalid")

    n_vectors = 0
    bessel_sum = 0.0
    gaussian_sum = 0.0
    absolute_sum_error = 0.0
    max_pointwise_abs = 0.0
    max_pointwise_rel = 0.0
    sum_squared_flux = 0.0

    for coords in itertools.product(range(-cutoff, cutoff + 1), repeat=rank):
        z = np.asarray(coords, dtype=np.int64)
        flux = z @ edge_basis
        orders = np.abs(flux)
        ratios = ive(orders, beta) / bessel_norm
        bessel_weight = float(np.exp(np.sum(np.log(ratios))))
        gaussian_weight = math.exp(-float(flux @ flux) / (2.0 * beta))
        abs_err = abs(bessel_weight - gaussian_weight)
        rel_err = abs_err / max(bessel_weight, 1e-300)
        bessel_sum += bessel_weight
        gaussian_sum += gaussian_weight
        absolute_sum_error += abs_err
        max_pointwise_abs = max(max_pointwise_abs, abs_err)
        max_pointwise_rel = max(max_pointwise_rel, rel_err)
        sum_squared_flux += float(flux @ flux)
        n_vectors += 1

    return {
        "audit": "Q6_D5_FINITE_BESSEL_GAUSSIAN_SLICE",
        "beta": float(beta),
        "rank": rank,
        "coordinate_cube_cutoff": cutoff,
        "vectors_enumerated": n_vectors,
        "wilson_bessel_slice_sum": bessel_sum,
        "gaussian_slice_sum": gaussian_sum,
        "absolute_slice_sum_difference": abs(bessel_sum - gaussian_sum),
        "sum_of_pointwise_absolute_errors": absolute_sum_error,
        "max_pointwise_absolute_error": max_pointwise_abs,
        "max_pointwise_relative_error": max_pointwise_rel,
        "average_squared_edge_flux": sum_squared_flux / n_vectors,
        "scope": {
            "exact": [
                "integer flux vectors in selected finite slice",
                "normalized Bessel Wilson weights evaluated with scaled scipy ive",
            ],
            "approximation": [
                "weak-coupling Gaussian exp(-||n||^2/(2 beta))",
            ],
            "not_claimed": [
                "complete rank-124 fibre sum",
                "uniform Gaussian approximation at finite beta",
                "certified interval arithmetic",
            ],
        },
    }
