"""TSMR-F: exact Cantor-Bernoulli dimensions and finite self-affine pressure.

The Cantor-Bernoulli formulas are exact for the separated two-branch model.
The anisotropic pressure routine is deliberately finite-level and diagnostic;
it does not claim that a pressure root equals a measure dimension.
"""
from __future__ import annotations

import itertools
import math


def cantor_bernoulli_tau(q: float, p: float, ratio: float) -> float:
    """Exact tau(q) for a separated two-branch Cantor Bernoulli measure."""
    _validate_cantor_parameters(p, ratio)
    if p in (0.0, 1.0):
        raise ValueError("both branch probabilities must be positive")
    if q <= 0:
        raise ValueError("q must be positive in this implementation")
    return math.log(p**q + (1.0-p)**q) / math.log(ratio)


def cantor_bernoulli_dimension(q: float, p: float, ratio: float) -> float:
    """Generalized dimension D_q, using the information-dimension limit at q=1."""
    _validate_cantor_parameters(p, ratio)
    if p in (0.0, 1.0):
        raise ValueError("both branch probabilities must be positive")
    if q <= 0:
        raise ValueError("q must be positive in this implementation")
    if math.isclose(q, 1.0, rel_tol=0.0, abs_tol=1e-10):
        entropy = -(p*math.log(p) + (1.0-p)*math.log(1.0-p))
        return entropy / math.log(1.0/ratio)
    return cantor_bernoulli_tau(q, p, ratio) / (q-1.0)


def _validate_cantor_parameters(p: float, ratio: float) -> None:
    if not 0.0 < p < 1.0:
        raise ValueError("p must lie strictly between 0 and 1")
    if not 0.0 < ratio < 1.0:
        raise ValueError("contraction ratio must lie strictly between 0 and 1")


def singular_values_2x2(matrix: tuple[tuple[float, float],
                                      tuple[float, float]]) -> tuple[float, float]:
    """Return singular values in descending order using eigenvalues of A^T A."""
    (a, b), (c, d) = matrix
    trace = a*a + b*b + c*c + d*d
    determinant_sq = (a*d-b*c)**2
    discriminant = max(0.0, trace*trace - 4.0*determinant_sq)
    lam_hi = max(0.0, 0.5*(trace + math.sqrt(discriminant)))
    lam_lo = max(0.0, 0.5*(trace - math.sqrt(discriminant)))
    return math.sqrt(lam_hi), math.sqrt(lam_lo)


def singular_value_function(matrix: tuple[tuple[float, float],
                                           tuple[float, float]],
                            s: float) -> float:
    """Planar singular-value function phi^s(A), for 0 <= s <= 2."""
    if not 0.0 <= s <= 2.0:
        raise ValueError("s must lie in [0, 2]")
    sigma_1, sigma_2 = singular_values_2x2(matrix)
    if sigma_2 <= 0.0:
        raise ValueError("matrix must be invertible")
    if s <= 1.0:
        return sigma_1**s
    return sigma_1 * sigma_2**(s-1.0)


def _multiply_2x2(left, right):
    return (
        (left[0][0]*right[0][0] + left[0][1]*right[1][0],
         left[0][0]*right[0][1] + left[0][1]*right[1][1]),
        (left[1][0]*right[0][0] + left[1][1]*right[1][0],
         left[1][0]*right[0][1] + left[1][1]*right[1][1]),
    )


def finite_level_self_affine_pressure(matrices, probabilities, q: float,
                                      s: float, depth: int) -> float:
    """Compute P_n(q,s) exactly over all words up to the requested finite depth."""
    if len(matrices) == 0 or len(matrices) != len(probabilities):
        raise ValueError("matrices and probabilities must have equal nonzero length")
    if any(prob <= 0.0 for prob in probabilities):
        raise ValueError("all branch probabilities must be positive")
    if not math.isclose(sum(probabilities), 1.0, rel_tol=1e-10, abs_tol=1e-10):
        raise ValueError("branch probabilities must sum to one")
    if q <= 0.0 or depth < 1 or not 0.0 <= s <= 2.0:
        raise ValueError("require q > 0, depth >= 1 and s in [0, 2]")
    total = 0.0
    for word in itertools.product(range(len(matrices)), repeat=depth):
        product = ((1.0, 0.0), (0.0, 1.0))
        weight = 1.0
        for index in word:
            product = _multiply_2x2(product, matrices[index])
            weight *= probabilities[index]
        phi = singular_value_function(product, s)
        total += weight**q * phi**(1.0-q)
    if total <= 0.0 or not math.isfinite(total):
        raise ArithmeticError("non-finite pressure sum")
    return math.log(total) / depth
