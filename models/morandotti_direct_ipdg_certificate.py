"""Direct exact-interval assembly and coercivity certificate for the C0-IPDG form.

The implementation certifies one fixed mesh. Geometry coordinates are interpreted
as exact dyadic rationals by the existing curved-P3 primitives.
"""
from __future__ import annotations

from fractions import Fraction as F
from time import perf_counter

from models.morandotti_certified_curved_p3_forms import (
    _as_fraction, _cell_data, _edge_q_data, _compose_line, _add, _scale,
    _derivative, _REF_VERTICES, _add1, _mul1, _scale1, _pow1,
    integrate_rational_sqrt_segments_many, assemble_cell_volume_interval,
    _zero_interval_matrix, _accumulate, _add_block,
)


def _edge_ipdg_data(node_coordinates, interpolation_points, edge):
    maps, basis, jac, adj, det, hessians, _ = _cell_data(
        node_coordinates, interpolation_points
    )
    a, b = (_REF_VERTICES[k] for k in edge)
    direction = (b[0]-a[0], b[1]-a[1])
    tangent = [
        _compose_line(
            _add(
                _scale(_derivative(maps[c], 0), direction[0]),
                _scale(_derivative(maps[c], 1), direction[1]),
            ), a, b
        )
        for c in range(2)
    ]
    tx, ty = tangent
    radicand = _add1(_mul1(tx, tx), _mul1(ty, ty))
    normal = (ty, _scale1(tx, F(-1)))
    qnums, det3 = _edge_q_data(maps, det, hessians, edge, normal)
    # n . grad_x(phi) = gnum / (det(J)*sqrt(|F'|^2)).
    # J^{-1} normal is polynomial; dot it with the reference gradient.
    # N is a pair of univariate polynomials, so compose adjugate entries first.
    from models.morandotti_certified_curved_p3_forms import _compose_line as compose
    n0, n1 = normal
    adj_line = [[compose(adj[r][c], a, b) for c in range(2)] for r in range(2)]
    gnums = []
    for phi in basis:
        gx = compose(_derivative(phi, 0), a, b)
        gy = compose(_derivative(phi, 1), a, b)
        jn_x = _add1(_mul1(adj_line[0][0], n0),
                     _mul1(adj_line[0][1], n1))
        jn_y = _add1(_mul1(adj_line[1][0], n0),
                     _mul1(adj_line[1][1], n1))
        gnums.append(_add1(_mul1(jn_x, gx), _mul1(jn_y, gy)))
    return qnums, gnums, det3, _pow1(_compose_line(det, a, b), 1), radicand


def _integrate_penalty(g_i, g_j, det_i, det_j, radicand, inverse_length,
                       tolerance, max_depth):
    # (g_i/det_i/sqrt(s)) (g_j/det_j/sqrt(s)) ds
    # = g_i*g_j/(det_i*det_j*sqrt(s)) dt.
    numerator = _scale1(_mul1(_mul1(g_i, g_j), radicand),
                        _as_fraction(inverse_length))
    return integrate_rational_sqrt_segments_many(
        [numerator], _mul1(det_i, det_j), radicand,
        absolute_tolerance=tolerance, max_depth=max_depth
    )[0][:2]


def _integrate_consistency(q_i, g_j, det3_i, det_j, radicand,
                           sign, tolerance, max_depth):
    # q_i*j_j ds = qnum_i*gnum_j/(det_i^3*det_j*s) dt.
    denominator = _mul1(_mul1(det3_i, det_j), radicand)
    numerator = _scale1(_mul1(q_i, g_j), _as_fraction(sign))
    return integrate_rational_sqrt_segments_many(
        [numerator], denominator, {0: F(1)},
        absolute_tolerance=tolerance, max_depth=max_depth
    )[0][:2]


def _zero_block(rows=10, cols=10):
    return [[(F(0), F(0)) for _ in range(cols)] for _ in range(rows)]


def _assemble_boundary_facet(nodes, points, edge, h, tolerance, max_depth):
    q, g, det3, det, s = _edge_ipdg_data(nodes, points, edge)
    P, C = _zero_block(), _zero_block()
    inv_h = F(1) / _as_fraction(h)
    for i in range(10):
        for j in range(10):
            P[i][j] = _integrate_penalty(
                g[i], g[j], det, det, s, inv_h, tolerance, max_depth
            )
            C[i][j] = _integrate_consistency(
                q[i], g[j], det3, det, s, 1, tolerance, max_depth
            )
    return P, C


def _assemble_interior_facet(nodes_a, nodes_b, points, edge_a, edge_b,
                             h_average, tolerance, max_depth):
    qa, ga, da3, da, s = _edge_ipdg_data(nodes_a, points, edge_a)
    qb, gb, db3, db, sb = _edge_ipdg_data(nodes_b, points, edge_b)
    if s != sb:
        raise ValueError("paired cells do not have the same exact facet metric")
    Paa, Pab, Pbb = _zero_block(), _zero_block(), _zero_block()
    Caa, Cab, Cba, Cbb = (_zero_block() for _ in range(4))
    inv_h = F(1) / _as_fraction(h_average)
    half = F(1, 2)
    for i in range(10):
        for j in range(10):
            Paa[i][j] = _integrate_penalty(
                ga[i], ga[j], da, da, s, inv_h, tolerance, max_depth
            )
            Pbb[i][j] = _integrate_penalty(
                gb[i], gb[j], db, db, s, inv_h, tolerance, max_depth
            )
            # The jump is j_A - j_B with the common A-side normal.
            Pab[i][j] = tuple(-x for x in _integrate_penalty(
                ga[i], gb[j], da, db, s, inv_h, tolerance, max_depth
            ))
            Caa[i][j] = _integrate_consistency(
                qa[i], ga[j], da3, da, s, half, tolerance, max_depth
            )
            Cab[i][j] = _integrate_consistency(
                qa[i], gb[j], da3, db, s, -half, tolerance, max_depth
            )
            Cba[i][j] = _integrate_consistency(
                qb[i], ga[j], db3, da, s, half, tolerance, max_depth
            )
            Cbb[i][j] = _integrate_consistency(
                qb[i], gb[j], db3, db, s, -half, tolerance, max_depth
            )
    return {
        "P_AA": Paa, "P_AB": Pab,
        "P_BA": [[Pab[j][i] for j in range(10)] for i in range(10)],
        "P_BB": Pbb,
        "C_AA": Caa, "C_AB": Cab, "C_BA": Cba, "C_BB": Cbb,
    }


def assemble_global_direct_ipdg_forms(
    cell_node_coordinates, interpolation_points, cell_dofs, cell_diameters,
    boundary_facets, interior_facets, number_of_dofs, *,
    absolute_tolerance=F(1, 10**8), max_depth=24,
):
    """Assemble sparse interval matrices D, P and nonsymmetric C.

    Facet edge pairs must use matching physical endpoint order. Boundary edge
    directions must be the positively oriented reference-cell boundary order
    (0,1), (1,2), or (2,0), so the normal is outward.
    """
    nc = len(cell_node_coordinates)
    if not (len(cell_dofs) == len(cell_diameters) == nc):
        raise ValueError("cell geometry, dof maps and diameters must have equal lengths")
    if any(len(dofs) != 10 for dofs in cell_dofs):
        raise ValueError("each P3 cell must provide ten scalar dofs")
    tol = _as_fraction(absolute_tolerance)
    D, P, C = (_zero_interval_matrix(number_of_dofs) for _ in range(3))
    t0 = perf_counter()
    for cell in range(nc):
        block = assemble_cell_volume_interval(
            cell_node_coordinates[cell], interpolation_points,
            absolute_tolerance=tol, max_depth=max_depth
        )["matrix_interval"]
        _add_block(D, block, cell_dofs[cell])
    volume_seconds = perf_counter() - t0
    t1 = perf_counter()
    for cell, edge in boundary_facets:
        pb, cb = _assemble_boundary_facet(
            cell_node_coordinates[cell], interpolation_points, tuple(edge),
            cell_diameters[cell], tol, max_depth
        )
        _add_block(P, pb, cell_dofs[cell])
        _add_block(C, cb, cell_dofs[cell])
    boundary_seconds = perf_counter() - t1
    t2 = perf_counter()
    for ca, ea, cb, eb in interior_facets:
        blocks = _assemble_interior_facet(
            cell_node_coordinates[ca], cell_node_coordinates[cb],
            interpolation_points, tuple(ea), tuple(eb),
            ( _as_fraction(cell_diameters[ca]) +
              _as_fraction(cell_diameters[cb]) ) / 2, tol, max_depth
        )
        da, db = cell_dofs[ca], cell_dofs[cb]
        _add_block(P, blocks["P_AA"], da)
        _add_block(P, blocks["P_BB"], db)
        _add_block(C, blocks["C_AA"], da)
        _add_block(C, blocks["C_BB"], db)
        for i, gi in enumerate(da):
            for j, gj in enumerate(db):
                _accumulate(P, gi, gj, blocks["P_AB"][i][j])
                _accumulate(P, gj, gi, blocks["P_BA"][j][i])
                _accumulate(C, gi, gj, blocks["C_AB"][i][j])
                _accumulate(C, gj, gi, blocks["C_BA"][j][i])
    interior_seconds = perf_counter() - t2
    return {
        "D_interval": D, "P_interval": P, "C_interval": C,
        "dofs": number_of_dofs,
        "assembly_timings_seconds": {
            "volume_cells": volume_seconds,
            "boundary_facets": boundary_seconds,
            "interior_facets": interior_seconds,
        },
        "assembly_counts": {
            "cells": nc, "boundary_facets": len(boundary_facets),
            "interior_facets": len(interior_facets),
        },
    }


def _interval_linear_combination(terms):
    out = {}
    keys = set().union(*(set(matrix) for matrix, _ in terms))
    for key in keys:
        lo = hi = F(0)
        for matrix, coefficient in terms:
            a, b = matrix.get(key, (F(0), F(0)))
            c = _as_fraction(coefficient)
            if c >= 0:
                lo += c*a
                hi += c*b
            else:
                lo += c*b
                hi += c*a
        if lo or hi:
            out[key] = (lo, hi)
    return out


def certify_interval_spd(matrix_interval):
    """Strict interval SPD certificate using exact rational sparse LDL^T."""
    entries = dict(matrix_interval)
    indices = [i for ij in entries for i in ij]
    n = max(indices, default=-1) + 1
    for (i, j), interval in entries.items():
        if entries.get((j, i), (F(0), F(0))) != interval:
            raise ValueError("matrix interval must be exactly symmetric")
    row_radii = [F(0) for _ in range(n)]
    midpoint = {}
    for i in range(n):
        for j in range(i, n):
            lo, hi = entries.get((i, j), (F(0), F(0)))
            if lo > hi:
                raise ValueError("invalid interval")
            radius = (hi-lo)/2
            row_radii[i] += radius
            if i != j:
                row_radii[j] += radius
            mid = (lo+hi)/2
            if mid:
                midpoint[(i, j)] = mid
    perturbation = max(row_radii, default=F(0))
    for i in range(n):
        midpoint[(i, i)] = midpoint.get((i, i), F(0)) - perturbation
    adjacency = [set() for _ in range(n)]
    for i, j in midpoint:
        if i != j and midpoint[(i, j)]:
            adjacency[i].add(j)
    pivots = []
    fill_updates = 0
    started = perf_counter()
    for k in range(n):
        pivot = midpoint.get((k, k), F(0))
        if pivot <= 0:
            return {
                "certified": False, "dimension": n,
                "spectral_error_bound": perturbation,
                "failed_pivot_index": k, "failed_pivot": pivot,
                "exact_schur_pivots": tuple(pivots),
                "method": "strict sparse exact-rational LDL^T with interval row-sum perturbation",
            }
        pivots.append(pivot)
        neighbors = sorted(adjacency[k])
        column = {i: midpoint[(k, i)] for i in neighbors}
        for ii, i in enumerate(neighbors):
            for j in neighbors[ii:]:
                key = (i, j)
                updated = midpoint.get(key, F(0)) - column[i]*column[j]/pivot
                if updated:
                    midpoint[key] = updated
                    if i != j:
                        adjacency[i].add(j)
                else:
                    midpoint.pop(key, None)
                    if i != j:
                        adjacency[i].discard(j)
                fill_updates += 1
        for i in neighbors:
            midpoint.pop((k, i), None)
        adjacency[k].clear()
        midpoint.pop((k, k), None)
    return {
        "certified": True, "dimension": n,
        "spectral_error_bound": perturbation,
        "minimum_exact_schur_pivot": min(pivots, default=None),
        "exact_schur_pivots": tuple(pivots),
        "ldl_fill_updates": fill_updates,
        "ldl_seconds": perf_counter()-started,
        "method": "strict sparse exact-rational LDL^T with interval row-sum perturbation",
    }


def certify_direct_ipdg_coercivity(D_interval, P_interval, C_interval,
                                   free_dofs, alpha, kappa):
    """Certify A - kappa W > 0 on the supplied fixed-mesh free-DOF space."""
    alpha, kappa = _as_fraction(alpha), _as_fraction(kappa)
    if alpha <= 0 or kappa <= 0:
        raise ValueError("alpha and kappa must be positive rationals")
    free = list(map(int, free_dofs))
    if len(set(free)) != len(free) or any(i < 0 for i in free):
        raise ValueError("free_dofs must be unique nonnegative global indices")
    index = {dof: i for i, dof in enumerate(free)}
    D, P, C = ({} for _ in range(3))
    for source, target in ((D_interval, D), (P_interval, P), (C_interval, C)):
        for (i, j), interval in source.items():
            if i in index and j in index:
                target[(index[i], index[j])] = interval
    CT = {(j, i): value for (i, j), value in C.items()}
    A = _interval_linear_combination(((D, 1), (C, -1), (CT, -1), (P, alpha)))
    W = _interval_linear_combination(((D, 1), (P, 1)))
    shifted = _interval_linear_combination(((A, 1), (W, -kappa)))
    certificate = certify_interval_spd(shifted)
    certificate.update({
        "alpha": alpha, "kappa": kappa,
        "free_dimension": len(free),
        "matrix": "A_h,ell - kappa*(D+P)",
        "form": "A=D-C-C^T+alpha*P; W=D+P",
        "integration_uncertainty_propagated": True,
        "scope": "one fixed mesh and the supplied free-DOF ordering",
    })
    return certificate
