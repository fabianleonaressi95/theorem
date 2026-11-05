"""Exact 2I-isotypic projectors on the SU(2) blocks used in T021.

The result is representation-theoretic: it certifies the projectors on each
Sym^m(C^2) block. It does not construct geometric Rumin eigenforms.
"""
from __future__ import annotations

import sympy as sp

from src.t032_2i_molien import IRREP_DIMENSIONS, molien_coefficients
from src.t034_exact_2i_character_table import reconstruct_character_table
from src.t036_2i_irreducible_models import symmetric_power_matrix
from audits.t035_exact_binary_icosahedral_model import (
    CLASS_SCALARS, elements_2i, rho2,
)


def build_actions(degree: int):
    """Return the 120 exact matrices of the pullback action on Sym^degree."""
    if degree < 0:
        raise ValueError("degree must be nonnegative")
    group = elements_2i()
    actions = tuple(symmetric_power_matrix(rho2(q), degree) for q in group)
    return group, actions


def isotypic_projectors(degree: int):
    """Construct all nine exact central projectors on Sym^degree(C^2)."""
    group, actions = build_actions(degree)
    characters, _ = reconstruct_character_table()
    class_indices = tuple(CLASS_SCALARS.index(q[0]) for q in group)
    size = degree + 1
    projectors = {}
    for label, dimension in IRREP_DIMENSIONS.items():
        P = sp.zeros(size)
        for j, action in zip(class_indices, actions):
            P += sp.conjugate(characters[label][j]) * action
        P = sp.simplify(sp.Rational(dimension, 120) * P)
        projectors[label] = P
    return group, actions, characters, projectors


def audit_isotypic_degree(degree: int, check_centrality: bool = True):
    """Check idempotence, orthogonality, completeness and Molien ranks.

    For an irreducible rho, rank(P_rho on Sym^m) = d_rho * b_(m,rho).
    Since P_rho is idempotent, its exact trace equals its rank.
    """
    group, actions, characters, projectors = isotypic_projectors(degree)
    size = degree + 1
    identity = sp.eye(size)
    labels = tuple(IRREP_DIMENSIONS)
    traces = {}
    centrality_checks = 0

    for label in labels:
        P = projectors[label]
        if sp.simplify(P * P - P) != sp.zeros(size):
            raise AssertionError(f"idempotence failed: {label}, degree {degree}")
        expected = IRREP_DIMENSIONS[label] * molien_coefficients(label, degree)[degree]
        trace = sp.simplify(sp.trace(P))
        if sp.simplify(trace - expected) != 0:
            raise AssertionError(
                f"Molien rank mismatch: {label}, degree {degree}: "
                f"trace={trace}, expected={expected}"
            )
        traces[label] = str(trace)

        if check_centrality:
            for action in actions:
                if sp.simplify(P * action - action * P) != sp.zeros(size):
                    raise AssertionError(
                        f"centrality failed: {label}, degree {degree}"
                    )
                centrality_checks += 1

    for i, left in enumerate(labels):
        for right in labels[i + 1:]:
            if (sp.simplify(projectors[left] * projectors[right])
                    != sp.zeros(size)):
                raise AssertionError(
                    f"orthogonality failed: {left}/{right}, degree {degree}"
                )

    total = sp.zeros(size)
    for P in projectors.values():
        total += P
    if sp.simplify(total - identity) != sp.zeros(size):
        raise AssertionError(f"completeness failed at degree {degree}")

    return {
        "passed": True,
        "degree": degree,
        "ambient_dimension": size,
        "group_order": len(group),
        "irreducibles_checked": len(labels),
        "idempotents_checked": len(labels),
        "pairwise_orthogonality_checks": len(labels) * (len(labels) - 1) // 2,
        "centrality_checks": centrality_checks,
        "projector_traces_and_expected_ranks": traces,
    }


def rumin_block_dimension(degree: int, label: str, sector: str) -> int:
    """Dimension contributed by the T021 U(2)-weight blocks at fixed degree.

    E0 has degree+1 weights p=0,...,degree.
    E1 has two conjugate bidegrees, each with degree+1 weights.
    This is a blockwise dimension count; coincident eigenvalues from
    different weights must be added when forming an eigenspace.
    """
    if label not in IRREP_DIMENSIONS:
        raise KeyError(label)
    if degree < 0:
        raise ValueError("degree must be nonnegative")
    if sector == "E0":
        copies = degree + 1
    elif sector == "E1":
        copies = 2 * (degree + 1)
    else:
        raise ValueError("sector must be 'E0' or 'E1'")
    multiplicity = molien_coefficients(label, degree)[degree]
    return copies * IRREP_DIMENSIONS[label] * multiplicity
