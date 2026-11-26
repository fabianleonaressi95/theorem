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


def test_direct_interior_facet_assembly_uses_two_sided_jump_and_average():
    points, nodes_a = _identity_p3()
    nodes_b = [(1-y, x+y) for x, y in points]
    result = assemble_global_direct_ipdg_forms(
        [nodes_a, nodes_b], points,
        [list(range(10)), list(range(10, 20))],
        [F(1), F(1)], [],
        [(0, (1, 2), 1, (0, 2))], 20,
        absolute_tolerance=F(1, 2), max_depth=8,
    )
    P, C = result["P_interval"], result["C_interval"]
    assert P and C
    for i in range(10):
        for j in range(10):
            assert P[(i, 10+j)] == P[(10+j, i)]
    assert result["assembly_counts"]["interior_facets"] == 1


def test_direct_volume_assembly_forwards_t135_integrator_options(monkeypatch):
    import models.morandotti_direct_ipdg_certificate as direct

    captured = {}

    def fake_volume(*args, **kwargs):
        captured.update(kwargs)
        return {"matrix_interval": {}}

    monkeypatch.setattr(direct, "assemble_cell_volume_interval", fake_volume)
    direct.assemble_global_direct_ipdg_forms(
        [object()], [], [list(range(10))], [F(1)], [], [], 10,
        integration_method="bernstein_residual",
        residual_expansion_order=4,
    )
    assert captured["integration_method"] == "bernstein_residual"
    assert captured["residual_expansion_order"] == 4
