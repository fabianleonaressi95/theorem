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
    _map_trace_on_edge,
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
    # J^{-1} n is geometry-only: compute it once per facet, not once
    # for each of the ten basis functions.  Rebuilding these exact Fraction
    # polynomials inside the basis loop multiplied the dominant edge work by 10.
    jn_x = _add1(_mul1(adj_line[0][0], n0),
                 _mul1(adj_line[0][1], n1))
    jn_y = _add1(_mul1(adj_line[1][0], n0),
                 _mul1(adj_line[1][1], n1))
    gnums = []
    for phi in basis:
        gx = compose(_derivative(phi, 0), a, b)
        gy = compose(_derivative(phi, 1), a, b)
        gnums.append(_add1(_mul1(jn_x, gx), _mul1(jn_y, gy)))
    return qnums, gnums, det3, _pow1(_compose_line(det, a, b), 1), radicand


def _integrate_penalty_matrix(g_left, g_right, det_left, det_right,
                               radicand, inverse_length, tolerance, max_depth):
    """Integrate a whole 10x10 penalty block on one shared certified tree."""
    scale = _as_fraction(inverse_length)
    numerators = [
        _scale1(_mul1(_mul1(g_i, g_j), radicand), scale)
        for g_i in g_left for g_j in g_right
    ]
    enclosed = integrate_rational_sqrt_segments_many(
        numerators, _mul1(det_left, det_right), radicand,
        absolute_tolerance=tolerance, max_depth=max_depth
    )
    intervals = [entry[:2] for entry in enclosed]
    return [intervals[10*i:10*(i+1)] for i in range(10)]


def _integrate_consistency_matrix(q_left, g_right, det3_left, det_right,
                                  radicand, sign, tolerance, max_depth):
    """Integrate a 10x10 consistency block with a shared tree per row."""
    denominator = _mul1(_mul1(det3_left, det_right), radicand)
    scale = _as_fraction(sign)
    # Certify the complete 10x10 block on one adaptive tree.  The former
    # row-at-a-time loop rebuilt the same denominator/radicand bounds and
    # subdivision tree ten times for every consistency block.
    numerators = [
        _scale1(_mul1(q_i, g_j), scale)
        for q_i in q_left for g_j in g_right
    ]
    enclosed = integrate_rational_sqrt_segments_many(
        numerators, denominator, {0: F(1)},
        absolute_tolerance=tolerance, max_depth=max_depth
    )
    return [
        [enclosed[10*i+j][:2] for j in range(10)]
        for i in range(10)
    ]


def _zero_block(rows=10, cols=10):
    return [[(F(0), F(0)) for _ in range(cols)] for _ in range(rows)]


def _assemble_boundary_facet(nodes, points, edge, h, tolerance, max_depth):
    q, g, det3, det, s = _edge_ipdg_data(nodes, points, edge)
    inv_h = F(1) / _as_fraction(h)
    P = _integrate_penalty_matrix(g, g, det, det, s, inv_h, tolerance, max_depth)
    C = _integrate_consistency_matrix(q, g, det3, det, s, 1, tolerance, max_depth)
    return P, C

def _assemble_interior_facet(nodes_a, nodes_b, points, edge_a, edge_b,
                             h_average, tolerance, max_depth):
    maps_a = _cell_data(nodes_a, points)[0]
    maps_b = _cell_data(nodes_b, points)[0]
    if _map_trace_on_edge(maps_a, edge_a) != _map_trace_on_edge(maps_b, edge_b):
        raise ValueError("neighboring P3 maps do not define the same exact curved facet trace")
    qa, ga, da3, da, s = _edge_ipdg_data(nodes_a, points, edge_a)
    qb, gb, db3, db, sb = _edge_ipdg_data(nodes_b, points, edge_b)
    if s != sb:
        raise ValueError("paired cells do not have the same exact facet metric")
    inv_h = F(1) / _as_fraction(h_average)
    Paa = _integrate_penalty_matrix(ga, ga, da, da, s, inv_h, tolerance, max_depth)
    Pbb = _integrate_penalty_matrix(gb, gb, db, db, s, inv_h, tolerance, max_depth)
    Pab = _integrate_penalty_matrix(ga, gb, da, db, s, inv_h, tolerance, max_depth)
    Pab = [[(-interval[1], -interval[0]) for interval in row]
           for row in Pab]
    Caa = _integrate_consistency_matrix(qa, ga, da3, da, s, F(1, 2), tolerance, max_depth)
    Cab = _integrate_consistency_matrix(qa, gb, da3, db, s, F(-1, 2), tolerance, max_depth)
    Cba = _integrate_consistency_matrix(qb, ga, db3, da, s, F(1, 2), tolerance, max_depth)
    Cbb = _integrate_consistency_matrix(qb, gb, db3, db, s, F(-1, 2), tolerance, max_depth)
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
        "row_interval_radius_bounds": tuple(row_radii),
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
    if not free:
        raise ValueError("the certified free-DOF space must be nonempty")
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
    # Preserve the full requested dimension even if an assembled row is empty;
    # an empty row must fail the strict pivot test, never disappear silently.
    for i in range(len(free)):
        shifted.setdefault((i, i), (F(0), F(0)))
    certificate = certify_interval_spd(shifted)
    certificate.update({
        "alpha": alpha, "kappa": kappa,
        "free_dimension": len(free),
        "free_dofs": tuple(free),
        "matrix": "A_h,ell - kappa*(D+P)",
        "form": "A=D-C-C^T+alpha*P; W=D+P",
        "integration_uncertainty_propagated": True,
        "scope": "one fixed mesh and the supplied free-DOF ordering",
    })
    return certificate



def assemble_dolfinx_direct_ipdg_forms(mesh, function_space, *,
                                       absolute_tolerance=F(1, 10**8),
                                       max_depth=24):
    """Extract a serial equispaced P3 mesh and assemble D, P, C.

    Boundary reference edges are oriented as (0,1), (1,2), (2,0), which
    gives the outward normal for the positively oriented reference triangle.
    Interior B-side endpoints are matched to A-side physical endpoint order.
    """
    import numpy as np
    import basix
    import hashlib
    import json
    from dolfinx import fem
    from dolfinx.mesh import exterior_facet_indices

    if mesh.comm.size != 1:
        raise RuntimeError("direct interval assembly currently requires a serial mesh")
    if mesh.topology.dim != 2 or mesh.geometry.dim != 2:
        raise ValueError("requires a planar triangular mesh")
    cmap = mesh.geometry.cmaps[0]
    if cmap.degree != 3 or cmap.dim != 10:
        raise ValueError("coordinate map must be triangular P3")
    if basix.LagrangeVariant(cmap.variant) != basix.LagrangeVariant.equispaced:
        raise ValueError("coordinate map must use equispaced P3 nodes")
    coordinate_element = basix.create_element(
        basix.ElementFamily.P, basix.CellType.triangle, 3,
        basix.LagrangeVariant.equispaced
    )
    points = np.asarray(coordinate_element.points, dtype=float)
    try:
        solution = function_space.element.basix_element
        solution_points = np.asarray(solution.points, dtype=float)
        interpolation = np.asarray(solution.interpolation_matrix, dtype=float)
    except AttributeError as exc:
        raise RuntimeError("cannot inspect the scalar P3 solution element") from exc
    if (solution.family != basix.ElementFamily.P or solution.degree != 3
            or solution_points.shape != points.shape
            or interpolation.shape != (10, 10)
            or not np.allclose(interpolation, np.eye(10), rtol=0, atol=1e-12)):
        raise ValueError("solution space must be nodal scalar equispaced P3")
    order = []
    used = set()
    for point in points:
        distances = np.linalg.norm(solution_points-point, axis=1)
        idx = int(np.argmin(distances))
        if distances[idx] > 1e-12 or idx in used:
            raise ValueError("solution and geometry P3 reference nodes do not match")
        order.append(idx)
        used.add(idx)
    nc = mesh.topology.index_map(2).size_local
    geometry_dofs = np.asarray(mesh.geometry.dofmaps[0], dtype=np.int32)
    if geometry_dofs.shape != (nc, 10):
        raise ValueError("expected ten geometry nodes per owned triangle")
    cell_nodes = [mesh.geometry.x[geometry_dofs[c], :2].copy() for c in range(nc)]
    cell_dofs = [
        np.asarray(function_space.dofmap.cell_dofs(c), dtype=np.int64)[order]
        for c in range(nc)
    ]
    diameters = np.asarray(mesh.h(2, np.arange(nc, dtype=np.int32)), dtype=float)

    mesh.topology.create_connectivity(2, 0)
    mesh.topology.create_connectivity(1, 0)
    mesh.topology.create_connectivity(1, 2)
    cell_vertices = mesh.topology.connectivity(2, 0)
    facet_vertices = mesh.topology.connectivity(1, 0)
    facet_cells = mesh.topology.connectivity(1, 2)
    nfacets = mesh.topology.index_map(1).size_local
    boundary, interior = [], []
    canonical = {frozenset((0, 1)): (0, 1),
                 frozenset((1, 2)): (1, 2),
                 frozenset((0, 2)): (2, 0)}
    for facet in range(nfacets):
        adjacent = list(map(int, facet_cells.links(facet)))
        if len(adjacent) not in (1, 2):
            continue
        fv = list(map(int, facet_vertices.links(facet)))
        if len(fv) != 2:
            raise RuntimeError("facet must have two vertices")
        ca = adjacent[0]
        va = list(map(int, cell_vertices.links(ca)))
        unordered_a = tuple(va.index(vertex) for vertex in fv)
        edge_a = canonical[frozenset(unordered_a)]
        physical_order = (va[edge_a[0]], va[edge_a[1]])
        if len(adjacent) == 1:
            boundary.append((ca, edge_a))
        else:
            cb = adjacent[1]
            vb = list(map(int, cell_vertices.links(cb)))
            edge_b = (vb.index(physical_order[0]), vb.index(physical_order[1]))
            interior.append((ca, edge_a, cb, edge_b))

    assembled = assemble_global_direct_ipdg_forms(
        cell_nodes, points, cell_dofs, diameters, boundary, interior,
        int(function_space.dofmap.index_map.size_local),
        absolute_tolerance=absolute_tolerance, max_depth=max_depth
    )
    exterior = exterior_facet_indices(mesh.topology)
    boundary_dofs = fem.locate_dofs_topological(function_space, 1, exterior)
    free = np.setdiff1d(
        np.arange(function_space.dofmap.index_map.size_local, dtype=np.int64),
        boundary_dofs
    )
    coordinate_payload = [[float(x).hex() for x in row] for cell in cell_nodes for row in cell]
    connectivity_payload = [list(map(int, dofs)) for dofs in cell_dofs]
    assembled.update({
        "coordinate_hash": hashlib.sha256(json.dumps(coordinate_payload, separators=(",", ":")).encode()).hexdigest(),
        "cell_dof_connectivity_hash": hashlib.sha256(json.dumps(connectivity_payload, separators=(",", ":")).encode()).hexdigest(),
        "free_dofs": free.tolist(),
        "cell_count": nc,
        "coordinate_nodes": "IEEE-754 binary64 interpreted as exact dyadic rationals",
        "boundary_orientation": "reference edges (0,1),(1,2),(2,0), outward on positive reference triangle",
        "interior_jump": "outward-normal sum, represented as j_A-j_B in the common A-side normal",
        "free_space": "homogeneous Dirichlet trace; boundary trace DOFs eliminated, interior DOFs retained",
    })
    return assembled
