"""Discrete gradients, barycentres, traction moments and resistance assembly.

Finite-dimensional local-drag assembly only; quadrature and drag data are
inputs from a declared hydrodynamic model, not a Stokes/BEM solver.
"""
import numpy as np


def weighted_barycentre(points, weights):
    x, w = np.asarray(points, float), np.asarray(weights, float)
    if x.ndim != 2 or x.shape[1] != 2 or w.shape != (len(x),):
        raise ValueError("points must be (n,2) and weights (n,)")
    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(w)) or np.any(w <= 0):
        raise ValueError("finite points and strictly positive weights required")
    return np.einsum("i,ij->j", w, x) / w.sum()


def cross2(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    if a.shape != (2,) or b.shape != (2,):
        raise ValueError("cross2 expects 2-vectors")
    return float(a[0] * b[1] - a[1] * b[0])


def q6_least_squares_gradient(shape_coordinates, edges, values, rcond=1e-12):
    x, f, e = np.asarray(shape_coordinates, float), np.asarray(values, float), np.asarray(edges, int)
    if x.ndim != 2 or x.shape[1] != 2 or f.shape != (len(x),):
        raise ValueError("expected 2D coordinates and one scalar per vertex")
    if e.ndim != 2 or e.shape[1] != 2 or np.any(e < 0) or np.any(e >= len(x)):
        raise ValueError("edges must have shape (m,2) and valid indices")
    gram, rhs = np.zeros((len(x), 2, 2)), np.zeros((len(x), 2))
    for u, v in e:
        dx, df = x[v] - x[u], f[v] - f[u]
        norm2 = float(dx @ dx)
        if norm2 <= np.finfo(float).eps:
            raise ValueError("a Q6 edge collapses in the shape map")
        weight = 1.0 / norm2
        contribution = weight * np.outer(dx, dx)
        vector = weight * dx * df
        gram[u] += contribution
        gram[v] += contribution
        rhs[u] += vector
        rhs[v] += vector
    gradients, conditions = np.empty((len(x), 2)), np.empty(len(x))
    for i, matrix in enumerate(gram):
        singular = np.linalg.svd(matrix, compute_uv=False)
        if singular[-1] <= rcond * singular[0]:
            raise ValueError(f"shape-edge star at vertex {i} does not span 2D")
        gradients[i] = np.linalg.solve(matrix, rhs[i])
        conditions[i] = singular[0] / singular[-1]
    return gradients, conditions


def assemble_local_resistance(points, quadrature_weights, drag_tensors,
                              shape_velocity_jacobians, reference=None):
    """Assemble R=sum_i w_i J_i.T D_i J_i in planar generalized coordinates."""
    x, w = np.asarray(points, float), np.asarray(quadrature_weights, float)
    d, js = np.asarray(drag_tensors, float), np.asarray(shape_velocity_jacobians, float)
    n = len(x)
    if x.shape != (n, 2) or w.shape != (n,) or np.any(w <= 0):
        raise ValueError("invalid points or positive quadrature weights")
    if d.shape != (n, 2, 2) or js.ndim != 3 or js.shape[:2] != (n, 2):
        raise ValueError("incompatible drag tensors or shape Jacobians")
    if not np.allclose(d, d.transpose(0, 2, 1), atol=1e-11):
        raise ValueError("local drag tensors must be symmetric")
    if any(np.min(np.linalg.eigvalsh(di)) <= 0 for di in d):
        raise ValueError("local drag tensors must be positive definite")
    origin = np.zeros(2) if reference is None else np.asarray(reference, float)
    if origin.shape != (2,):
        raise ValueError("reference must be a 2-vector")
    rel = x - origin
    body = np.zeros((n, 2, 3))
    body[:, 0, 0], body[:, 1, 1] = 1.0, 1.0
    body[:, 0, 2], body[:, 1, 2] = -rel[:, 1], rel[:, 0]
    jac = np.concatenate((body, js), axis=2)
    resistance = np.einsum("i,ija,ijk,ikb->ab", w, jac, d, jac)
    resistance = 0.5 * (resistance + resistance.T)
    return {"resistance": resistance, "velocity_jacobians": jac,
            "geometric_barycentre": weighted_barycentre(x, w), "reference": origin}


def resistance_connection(resistance, shape_dimension):
    r = np.asarray(resistance, float)
    if r.ndim != 2 or r.shape[0] != r.shape[1] or shape_dimension < 1:
        raise ValueError("resistance must be square and shape dimension positive")
    if r.shape[0] - shape_dimension != 3:
        raise ValueError("expected three planar body coordinates")
    rbb, rbs = r[:3, :3], r[:3, 3:]
    rsb, rss = r[3:, :3], r[3:, 3:]
    if np.min(np.linalg.eigvalsh(0.5 * (rbb + rbb.T))) <= 0:
        raise ValueError("body resistance block must be positive definite")
    connection = -np.linalg.solve(rbb, rbs)
    metric = rss - rsb @ np.linalg.solve(rbb, rbs)
    return connection, 0.5 * (metric + metric.T)


def evaluate_local_loads(assembly, generalized_velocity, points,
                         quadrature_weights, drag_tensors):
    qdot = np.asarray(generalized_velocity, float)
    x, w, d = np.asarray(points, float), np.asarray(quadrature_weights, float), np.asarray(drag_tensors, float)
    jac = assembly["velocity_jacobians"]
    if qdot.shape != (jac.shape[2],) or x.shape != (len(w), 2) or d.shape != (len(w), 2, 2):
        raise ValueError("load inputs do not match assembly")
    velocity = np.einsum("ija,a->ij", jac, qdot)
    traction = -np.einsum("ijk,ik->ij", d, velocity)
    force = np.einsum("i,ij->j", w, traction)
    origin, centre = assembly["reference"], assembly["geometric_barycentre"]
    moment_o = sum(wi * cross2(xi-origin, ti) for wi, xi, ti in zip(w, x, traction))
    moment_c = sum(wi * cross2(xi-centre, ti) for wi, xi, ti in zip(w, x, traction))
    power = float(np.einsum("i,ij,ijk,ik->", w, velocity, d, velocity))
    return {"point_velocities": velocity, "tractions": traction, "force": force,
            "moment_about_reference": float(moment_o),
            "moment_about_barycentre": float(moment_c), "dissipation": power}
