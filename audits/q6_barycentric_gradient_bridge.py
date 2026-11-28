"""Operator-level bridge between T130's Q6 gradient and barycentric P1 cells.

The 240 Q6 square 2-cells are split by a fixed combinatorial diagonal into
480 triangles in the declared 2D Q6ShapeMap. This is an operator audit on
the calibrated shape plane, not a 4D spacetime cell decomposition.
"""
from __future__ import annotations

from itertools import combinations, product
import numpy as np

from audits.purcell_swimmer_wall.discrete_geometry import q6_least_squares_gradient
from audits.purcell_swimmer_wall.q6_cut_project_interface import (
    Q6ShapeMap, q6_edges, q6_states,
)


def q6_square_faces():
    """Return all 240 elementary Q6 square faces, cyclically ordered."""
    faces = []
    for axes in combinations(range(6), 2):
        fixed_axes = [k for k in range(6) if k not in axes]
        for fixed in product((0, 1), repeat=4):
            base = [None] * 6
            for k, bit in zip(fixed_axes, fixed):
                base[k] = bit
            cycle = []
            for a, b in ((0, 0), (1, 0), (1, 1), (0, 1)):
                bits = base.copy()
                bits[axes[0]], bits[axes[1]] = a, b
                label = sum(int(bits[k]) << (5-k) for k in range(6))
                cycle.append(label)
            faces.append(tuple(cycle))
    return np.asarray(faces, dtype=np.int64)


def q6_square_triangulation():
    """Split each square along its (v0,v2) diagonal; returns 480 triangles."""
    faces = q6_square_faces()
    triangles = np.empty((2 * len(faces), 3), dtype=np.int64)
    triangles[0::2] = faces[:, (0, 1, 2)]
    triangles[1::2] = faces[:, (0, 2, 3)]
    return triangles


def triangle_p1_geometry(vertices):
    """Return positive area, barycentre and normalized 2D covariance."""
    x = np.asarray(vertices, dtype=float)
    if x.shape != (3, 2) or not np.isfinite(x).all():
        raise ValueError("triangle vertices must be finite with shape (3,2)")
    jac = np.column_stack((x[1] - x[0], x[2] - x[0]))
    det = float(np.linalg.det(jac))
    area = 0.5 * abs(det)
    if area <= 1e-14:
        raise ValueError("degenerate projected Q6 triangle")
    centre = x.mean(axis=0)
    y = x - centre
    covariance = y.T @ y / 12.0
    return area, centre, covariance


def triangle_p1_gradient(vertices, values):
    """Exact constant gradient of the affine P1 interpolant on a triangle."""
    x = np.asarray(vertices, dtype=float)
    f = np.asarray(values, dtype=float)
    if x.shape != (3, 2) or f.shape != (3,):
        raise ValueError("expected three 2D vertices and three scalar values")
    jac = np.column_stack((x[1] - x[0], x[2] - x[0]))
    if abs(np.linalg.det(jac)) <= 1e-14:
        raise ValueError("degenerate projected Q6 triangle")
    return np.linalg.solve(jac.T, np.array([f[1]-f[0], f[2]-f[0]]))


def barycentric_p1_vertex_projection(coordinates, values, triangles):
    """Area-weighted average of incident P1 gradients at each Q6 vertex."""
    x = np.asarray(coordinates, dtype=float)
    f = np.asarray(values, dtype=float)
    tri = np.asarray(triangles, dtype=np.int64)
    if x.shape != (64, 2) or f.shape != (64,) or tri.ndim != 2 or tri.shape[1] != 3:
        raise ValueError("expected 64 Q6 points, 64 scalar values and triangle indices")
    accum = np.zeros((64, 2), dtype=float)
    weights = np.zeros(64, dtype=float)
    for ids in tri:
        area, _, _ = triangle_p1_geometry(x[ids])
        grad = triangle_p1_gradient(x[ids], f[ids])
        for vertex in ids:
            accum[vertex] += area * grad
            weights[vertex] += area
    if np.any(weights <= 0):
        raise ValueError("triangulation leaves a Q6 vertex without incident cells")
    return accum / weights[:, None]


def audit_q6_barycentric_gradient_bridge(calibration, values=None):
    """Compare T130 six-neighbour LS gradients with barycentric P1 projection."""
    shape = Q6ShapeMap(np.asarray(calibration, dtype=float))
    coordinates = shape.coordinates()
    states = q6_states()
    edges = q6_edges()[:, :2]
    triangles = q6_square_triangulation()
    if values is None:
        target = np.array([0.73, -1.21])
        scalar = coordinates @ target + 0.44
    else:
        scalar = np.asarray(values, dtype=float)
        if scalar.shape != (64,) or not np.isfinite(scalar).all():
            raise ValueError("values must be a finite vector of length 64")
        target = None
    q6_grad, condition = q6_least_squares_gradient(coordinates, edges, scalar)
    p1_grad = barycentric_p1_vertex_projection(coordinates, scalar, triangles)
    residual = q6_grad - p1_grad
    return {
        "q6_vertices": int(len(states)),
        "q6_edges": int(len(edges)),
        "q6_square_faces": int(len(q6_square_faces())),
        "p1_triangles": int(len(triangles)),
        "minimum_projected_triangle_area": float(min(
            triangle_p1_geometry(coordinates[t])[0] for t in triangles
        )),
        "maximum_q6_star_condition_number": float(np.max(condition)),
        "q6_gradient": q6_grad.tolist(),
        "barycentric_p1_vertex_gradient": p1_grad.tolist(),
        "max_operator_residual": float(np.max(np.linalg.norm(residual, axis=1))),
        "affine_patch_target": None if target is None else target.tolist(),
        "affine_patch_pass": None if target is None else bool(
            np.max(np.linalg.norm(residual, axis=1)) < 1e-9
        ),
        "status": "2D_CALIBRATED_Q6_SHAPE_OPERATOR_BRIDGE_ONLY",
    }


def lift_shape_gradient_to_lorentzian_4d(gradient_2d, tangent_frame_4x2,
                                        eta=None, tolerance=1e-12):
    """Lift a 2D covector to a nondegenerate 2-plane in Minkowski 4-space.

    Returns the unique vector in span(tangent_frame) satisfying
    B.T @ eta @ grad4 = gradient2d. It does not construct the missing
    complementary two spacetime directions or a 4D Q6 cell complex.
    """
    g2 = np.asarray(gradient_2d, dtype=float)
    frame = np.asarray(tangent_frame_4x2, dtype=float)
    metric = np.diag([1.0, -1.0, -1.0, -1.0]) if eta is None else np.asarray(eta, dtype=float)
    if g2.shape != (2,) or frame.shape != (4, 2) or metric.shape != (4, 4):
        raise ValueError("expected gradient (2,), tangent frame (4,2), metric (4,4)")
    if not np.isfinite(g2).all() or not np.isfinite(frame).all() or not np.isfinite(metric).all():
        raise ValueError("all inputs must be finite")
    if not np.allclose(metric, metric.T, atol=tolerance):
        raise ValueError("Lorentzian metric must be symmetric")
    gram = frame.T @ metric @ frame
    if np.linalg.matrix_rank(frame, tol=tolerance) != 2:
        raise ValueError("tangent frame must have rank two")
    if abs(np.linalg.det(gram)) <= tolerance:
        raise ValueError("induced metric on the selected 2-plane is degenerate")
    lifted = frame @ np.linalg.solve(gram, g2)
    residual = frame.T @ metric @ lifted - g2
    if np.linalg.norm(residual) > 100 * tolerance * max(1.0, np.linalg.norm(g2)):
        raise ArithmeticError("Lorentzian tangent lift failed its defining identity")
    return lifted
