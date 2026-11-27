#!/usr/bin/env python3
"""Deterministic, standard-library audit for T156.

This checks exact rational conjugacies and finite geometric identities.  It does
not solve the elastic-strip minimization problem or infer a physical FDT map.
"""
from __future__ import annotations

import json
import math
from fractions import Fraction
from typing import Iterable


def h(alpha: Fraction) -> Fraction:
    return alpha / (2 - alpha)


def h_inverse(x: Fraction) -> Fraction:
    return 2 * x / (1 + x)


def farey(x: Fraction) -> Fraction:
    if not 0 <= x <= 1:
        raise ValueError("Farey input must lie in [0, 1]")
    if x <= Fraction(1, 2):
        return x / (1 - x)
    return (1 - x) / x


def conjugated_farey(alpha: Fraction) -> Fraction:
    if not 0 <= alpha <= 1:
        raise ValueError("alpha must lie in [0, 1]")
    if alpha <= Fraction(2, 3):
        return 2 * alpha / (2 - alpha)
    return 4 * (1 - alpha) / (2 - alpha)


def tent(y: Fraction) -> Fraction:
    if not 0 <= y <= 1:
        raise ValueError("tent input must lie in [0, 1]")
    return 1 - abs(2 * y - 1)


def continued_fraction(x: Fraction) -> list[int]:
    """Canonical finite continued fraction, with final term > 1 if nontrivial."""
    if not 0 <= x <= 1:
        raise ValueError("question-mark input must lie in [0, 1]")
    if x in (0, 1):
        return []
    n, d = x.numerator, x.denominator
    terms: list[int] = []
    while d:
        a, r = divmod(n, d)
        terms.append(a)
        n, d = d, r
    if len(terms) > 1 and terms[-1] == 1:
        terms[-2] += 1
        terms.pop()
    return terms[1:]  # omit the initial zero


def question_mark_rational(x: Fraction) -> Fraction:
    """Exact Minkowski ? value for a rational x in [0,1]."""
    if x == 0:
        return Fraction(0)
    if x == 1:
        return Fraction(1)
    terms = continued_fraction(x)
    total = Fraction(0)
    partial_sum = 0
    for k, term in enumerate(terms, start=1):
        partial_sum += term
        piece = Fraction(1, 2 ** (partial_sum - 1))
        total += piece if k % 2 else -piece
    return total


def vesica_metrics(chi: float) -> tuple[float, float]:
    if not 0.0 < chi < 1.0:
        raise ValueError("chi must lie strictly between 0 and 1")
    b_over_r = math.sqrt(1.0 - chi * chi)
    area_over_r2 = 2.0 * math.acos(chi) - 2.0 * chi * b_over_r
    return b_over_r, area_over_r2


def mobius_transverse_after_laps(q: float, laps: int) -> float:
    return (-1.0 if laps % 2 else 1.0) * q


def developability_residual(
    eta: Iterable[float], kappa: Iterable[float], tau: Iterable[float]
) -> float:
    triples = list(zip(eta, kappa, tau))
    if not triples:
        raise ValueError("at least one profile sample is required")
    if any(kappa_i == 0 for _, kappa_i, _ in triples):
        raise ValueError("the narrow-strip Sadowsky density is singular at kappa=0")
    return max(abs(tau_i - eta_i * kappa_i) for eta_i, kappa_i, tau_i in triples)


def sadowsky_density(kappa: float, tau: float) -> float:
    if kappa == 0:
        raise ValueError("Sadowsky density is singular at kappa=0")
    return (kappa * kappa + tau * tau) ** 2 / (kappa * kappa)


def run_audit() -> dict[str, object]:
    alpha_grid = [
        Fraction(p, q)
        for q in range(2, 31)
        for p in range(1, q)
    ]
    conjugacy_checks = 0
    for alpha in alpha_grid:
        lhs = conjugated_farey(alpha)
        rhs = h_inverse(farey(h(alpha)))
        assert lhs == rhs
        conjugacy_checks += 1

    question_mark_checks = 0
    for q in range(2, 31):
        for p in range(1, q):
            x = Fraction(p, q)
            qm_x = question_mark_rational(x)
            assert question_mark_rational(farey(x)) == tent(qm_x)
            question_mark_checks += 1

    alpha_c = Fraction(2, 3)
    assert h(alpha_c) == Fraction(1, 2)
    assert conjugated_farey(alpha_c) == 1

    chi = 0.5
    b_over_r, area_over_r2 = vesica_metrics(chi)
    expected_area = 2.0 * math.pi / 3.0 - math.sqrt(3.0) / 2.0
    assert math.isclose(b_over_r, math.sqrt(3.0) / 2.0, rel_tol=0.0, abs_tol=1e-14)
    assert math.isclose(area_over_r2, expected_area, rel_tol=0.0, abs_tol=1e-14)

    q0 = 0.37
    assert mobius_transverse_after_laps(q0, 1) == -q0
    assert mobius_transverse_after_laps(q0, 2) == q0

    eta = [0.0, 0.25, -0.5, 1.0]
    kappa = [0.5, 1.0, 2.0, 0.75]
    tau = [e * k for e, k in zip(eta, kappa)]
    residual = developability_residual(eta, kappa, tau)
    assert residual == 0.0
    densities = [sadowsky_density(k, t) for k, t in zip(kappa, tau)]
    assert all(value > 0.0 for value in densities)

    return {
        "record": "T156",
        "classification": "finite regression audit; not an elastic equilibrium solve",
        "farey_conjugacy_rational_checks": conjugacy_checks,
        "question_mark_tent_rational_checks": question_mark_checks,
        "threshold": {
            "alpha": "2/3",
            "h_alpha": str(h(alpha_c)),
            "G_alpha": str(conjugated_farey(alpha_c)),
        },
        "vesica_chi_half": {
            "b_over_R": b_over_r,
            "area_over_R2": area_over_r2,
            "closed_form_area_over_R2": "2*pi/3 - sqrt(3)/2",
        },
        "mobius_transverse_coordinate": {
            "initial": q0,
            "after_one_lap": mobius_transverse_after_laps(q0, 1),
            "after_two_laps": mobius_transverse_after_laps(q0, 2),
        },
        "developability_profile_max_residual": residual,
        "sadowsky_density_samples": densities,
        "not_claimed": [
            "Starostin-van der Heijden equilibrium reproduced",
            "Vesica geometry physically derives chi=h(alpha)",
            "FDT equations derive a Farey return map",
            "Möbius linking equals Frenet torsion",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
