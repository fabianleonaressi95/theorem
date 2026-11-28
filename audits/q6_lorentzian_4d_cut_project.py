"""Explicit 6D -> Lorentzian 4D Q6 cut-project and 4-simplex audit.

The time row is a declared generic internal direction selected by a
deterministic nondegeneracy criterion. The resulting 4-skeleton is an
abstract branched 4-complex: every cubical 3-face belongs to three 4-cells,
so it is not a 4-manifold.
"""
from __future__ import annotations

from itertools import combinations, permutations, product
from math import gcd
import numpy as np

from audits.purcell_swimmer_wall.q6_cut_project_interface import (
    golden_cut_project_frame, q6_edges, q6_states,
)


ETA = np.diag([1.0, -1.0, -1.0, -1.0])


def _primitive_positive_triples(max_l1=12):
    for total in range(3, max_l1 + 1):
        for a in range(1, total - 1):
            for b in range(1, total - a):
                c = total - a - b
                if c >= 1 and gcd(gcd(a, b), c) == 1:
                    yield np.array([a, b, c], dtype=float)


def q6_lorentzian_cut_project_frame(tolerance=1e-10):
    """Return row-orthonormal 4x6 frame; first row is internal-time candidate.

    The time direction is the first primitive positive integer combination
    (ordered by L1 norm and lexicographically) of the three internal rows for
    which all fifteen 4x4 coordinate minors are nonzero.
    """
    physical, internal = golden_cut_project_frame()
    selected = None
    selected_min_minor = None
    for coeff in _primitive_positive_triples():
        time_row = coeff @ internal / np.linalg.norm(coeff)
        frame = np.vstack((time_row, physical))
        minors = [
            abs(float(np.linalg.det(frame[:, axes])))
            for axes in combinations(range(6), 4)
        ]
        if min(minors) > tolerance:
            selected = frame
            selected_min_minor = min(minors)
            break
    if selected is None:
        raise RuntimeError("no nondegenerate internal time direction found")
    return selected, selected_min_minor


def q6_four_faces():
    """Return 60 coordinate 4-faces as (free_axes, fixed_axis_bits)."""
    cells = []
    for axes in combinations(range(6), 4):
        fixed_axes = tuple(k for k in range(6) if k not in axes)
        for fixed in product((0, 1), repeat=2):
            cells.append((tuple(axes), tuple(zip(fixed_axes, fixed))))
    return tuple(cells)


def _label(bits):
    return sum(int(bits[k]) << (5-k) for k in range(6))


def q6_four_simplex_triangulation():
    """Conforming Freudenthal split: 24 4-simplices per coordinate 4-cube."""
    simplices = []
    for axes, fixed in q6_four_faces():
        base = [0] * 6
        for axis, bit in fixed:
            base[axis] = bit
        for order in permutations(axes):
            bits = base.copy()
            path = [_label(bits)]
            for axis in order:
                bits = bits.copy()
                bits[axis] = 1
                path.append(_label(bits))
            simplices.append(tuple(path))
    return np.asarray(simplices, dtype=np.int64)


def q6_three_face_incidence():
    """Count 4-cell incidences of every coordinate 3-face."""
    incidence = {}
    for axes, fixed in q6_four_faces():
        fixed_map = dict(fixed)
        for dropped in axes:
            face_axes = tuple(a for a in axes if a != dropped)
            for bit in (0, 1):
                face_fixed = dict(fixed_map)
                face_fixed[dropped] = bit
                key = (face_axes, tuple(sorted(face_fixed.items())))
                incidence[key] = incidence.get(key, 0) + 1
    return incidence


def _simplex_geometry(coordinates, ids):
    x = np.asarray(coordinates, dtype=float)[np.asarray(ids, dtype=int)]
    if x.shape != (5, 4):
        raise ValueError("a 4-simplex requires five 4D vertices")
    jac = (x[1:] - x[0]).T
    determinant = float(np.linalg.det(jac))
    volume = abs(determinant) / 24.0
    if volume <= 1e-14:
        raise ValueError("degenerate projected 4-simplex")
    centre = x.mean(axis=0)
    centred = x - centre
    covariance = centred.T @ centred / 30.0
    lorentz_gram = jac.T @ ETA @ jac
    return volume, centre, covariance, lorentz_gram


def q6_least_squares_gradient_4d(coordinates, values):
    """Six-neighbour weighted LS gradient in the projected 4D affine chart."""
    x = np.asarray(coordinates, dtype=float)
    f = np.asarray(values, dtype=float)
    if x.shape != (64, 4) or f.shape != (64,):
        raise ValueError("expected 64 projected 4D points and 64 scalar values")
    gram = np.zeros((64, 4, 4))
    rhs = np.zeros((64, 4))
    for u, v, _axis in q6_edges():
        dx = x[v] - x[u]
        norm2 = float(dx @ dx)
        if norm2 <= 1e-14:
            raise ValueError("collapsed projected Q6 edge")
        weight = 1.0 / norm2
        outer = weight * np.outer(dx, dx)
        vector = weight * dx * (f[v] - f[u])
        gram[u] += outer
        gram[v] += outer
        rhs[u] += vector
        rhs[v] += vector
    gradients = np.empty((64, 4))
    conditions = np.empty(64)
    for vertex, matrix in enumerate(gram):
        singular = np.linalg.svd(matrix, compute_uv=False)
        if singular[-1] <= 1e-12 * singular[0]:
            raise ValueError(f"Q6 4D edge star at vertex {vertex} is rank deficient")
        gradients[vertex] = np.linalg.solve(matrix, rhs[vertex])
        conditions[vertex] = singular[0] / singular[-1]
    return gradients, conditions


def four_simplex_p1_gradient(coordinates, ids, values):
    """Exact P1 gradient on one nondegenerate affine 4-simplex."""
    ids = np.asarray(ids, dtype=int)
    x = np.asarray(coordinates, dtype=float)[ids]
    f = np.asarray(values, dtype=float)[ids]
    jac = (x[1:] - x[0]).T
    if abs(np.linalg.det(jac)) <= 1e-14:
        raise ValueError("degenerate 4-simplex")
    return np.linalg.solve(jac.T, f[1:] - f[0])


def barycentric_p1_vertex_projection_4d(coordinates, values, simplices):
    """4-volume-weighted vertex average of incident 4-simplex P1 gradients."""
    x = np.asarray(coordinates, dtype=float)
    f = np.asarray(values, dtype=float)
    simplices = np.asarray(simplices, dtype=np.int64)
    accum = np.zeros((64, 4))
    weights = np.zeros(64)
    for ids in simplices:
        volume, _, _, _ = _simplex_geometry(x, ids)
        gradient = four_simplex_p1_gradient(x, ids, f)
        for vertex in ids:
            accum[vertex] += volume * gradient
            weights[vertex] += volume
    if np.any(weights <= 0):
        raise ValueError("a Q6 vertex has no incident 4-simplex")
    return accum / weights[:, None]


def audit_q6_lorentzian_4d_cut_project():
    """Audit 4D projection, 4-cells, branched incidence and gradient patch."""
    frame, min_minor = q6_lorentzian_cut_project_frame()
    states = q6_states().astype(float)
    centred = states - 0.5
    coordinates = centred @ frame.T
    simplices = q6_four_simplex_triangulation()
    cells = q6_four_faces()
    incidence = q6_three_face_incidence()

    volumes, lorentz_nondegenerate = [], []
    covariances = []
    for ids in simplices:
        volume, _centre, covariance, gram = _simplex_geometry(coordinates, ids)
        volumes.append(volume)
        covariances.append(covariance)
        lorentz_nondegenerate.append(abs(np.linalg.det(gram)) > 1e-14)

    target = np.array([0.7, -1.3, 0.2, 0.9])
    affine_values = coordinates @ target + 0.37
    q6_grad, condition = q6_least_squares_gradient_4d(coordinates, affine_values)
    p1_grad = barycentric_p1_vertex_projection_4d(
        coordinates, affine_values, simplices
    )
    affine_residual = float(np.max(np.linalg.norm(q6_grad - p1_grad, axis=1)))

    parity_values = np.asarray([
        (-1.0) ** int(int(v).bit_count()) * (1.0 + v / 64.0)
        for v in range(64)
    ])
    q6_nonaffine, _ = q6_least_squares_gradient_4d(coordinates, parity_values)
    p1_nonaffine = barycentric_p1_vertex_projection_4d(
        coordinates, parity_values, simplices
    )
    nonaffine_residual = float(np.max(
        np.linalg.norm(q6_nonaffine - p1_nonaffine, axis=1)
    ))

    return {
        "frame": frame.tolist(),
        "frame_row_orthogonality_residual": float(
            np.linalg.norm(frame @ frame.T - np.eye(4))
        ),
        "time_internal_integer_direction": [1, 1, 2],
        "minimum_abs_4x4_cut_project_minor": float(min_minor),
        "vertices": 64,
        "edges": 192,
        "coordinate_4_cells": len(cells),
        "coordinate_3_faces": len(incidence),
        "freudenthal_4_simplices": int(len(simplices)),
        "minimum_4_simplex_volume": float(min(volumes)),
        "maximum_4_simplex_volume": float(max(volumes)),
        "all_lorentzian_simplex_grams_nondegenerate": bool(all(lorentz_nondegenerate)),
        "minimum_lorentzian_gram_abs_determinant": float(min(
            abs(np.linalg.det(_simplex_geometry(coordinates, ids)[3]))
            for ids in simplices
        )),
        "facet_incidence_values": sorted(set(incidence.values())),
        "minimum_4_cell_incidence_per_3_face": int(min(incidence.values())),
        "maximum_4_cell_incidence_per_3_face": int(max(incidence.values())),
        "is_4_manifold_by_facet_incidence": bool(
            all(count == 2 for count in incidence.values())
        ),
        "maximum_q6_4d_star_condition_number": float(max(condition)),
        "affine_patch_max_operator_residual": affine_residual,
        "affine_patch_pass": bool(affine_residual < 1e-9),
        "nonaffine_parity_field_operator_residual": nonaffine_residual,
        "simplex_covariance_shape": list(covariances[0].shape),
        "status": "EXPLICIT_4D_CUT_PROJECT_BRANCHED_COMPLEX_NOT_A_4_MANIFOLD",
    }
