from fractions import Fraction as F

from models.morandotti_direct_ipdg_certificate import (
    assemble_global_direct_ipdg_forms,
    certify_direct_ipdg_coercivity,
)


def _identity_p3():
    points = [
        (F(i, 3), F(j, 3))
        for i in range(4)
        for j in range(4-i)
    ]
    return points, points


def test_direct_boundary_assembly_builds_D_P_C_with_exact_intervals():
    points, nodes = _identity_p3()
    result = assemble_global_direct_ipdg_forms(
        [nodes], points, [list(range(10))], [F(1)],
        [(0, (0, 1)), (0, (1, 2)), (0, (2, 0))], [],
        10, absolute_tolerance=F(1, 2), max_depth=8,
    )
    for name in ("D_interval", "P_interval", "C_interval"):
        matrix = result[name]
        assert matrix
        assert all(lo <= hi for lo, hi in matrix.values())
    P = result["P_interval"]
    for (i, j), interval in P.items():
        assert P[(j, i)] == interval
    assert result["assembly_counts"] == {
        "cells": 1, "boundary_facets": 3, "interior_facets": 0
    }


def test_direct_coercivity_certificate_requires_strict_positive_pivots():
    D = {(0, 0): (F(1), F(1)), (1, 1): (F(1), F(1)),
         (0, 1): (F(0), F(0)), (1, 0): (F(0), F(0))}
    P = {(0, 0): (F(1), F(1)), (1, 1): (F(1), F(1)),
         (0, 1): (F(0), F(0)), (1, 0): (F(0), F(0))}
    C = {}
    result = certify_direct_ipdg_coercivity(D, P, C, [0, 1], F(2), F(1))
    assert result["certified"]
    assert result["minimum_exact_schur_pivot"] == 1
    assert result["kappa"] == 1
    assert result["scope"].startswith("one fixed mesh")


def test_direct_coercivity_certificate_rejects_nonpositive_shift():
    D = {(0, 0): (F(1), F(1))}
    P = {(0, 0): (F(0), F(0))}
    result = certify_direct_ipdg_coercivity(D, P, {}, [0], F(1), F(1))
    assert not result["certified"]
    assert result["failed_pivot"] == 0
