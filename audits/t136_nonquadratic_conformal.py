#!/usr/bin/env python3
"""T136 non-quadratic smooth-metric audit via a conformal metric.

The physical-coordinate metric is g = exp(2 f(x)) delta, with a quadratic
and a genuinely cubic term in f. Tetrahedra are mapped by the numerical
Riemannian exponential map from the origin. The pulled-back volume density
is exp(3 f(exp(v))) det(D exp(v)).
Only NumPy is required.
"""
from __future__ import annotations

import json
import numpy as np
from numpy.polynomial.legendre import leggauss

RICCI_EXACT = np.array([
    [0.80, 0.12, -0.08],
    [0.12, 0.50, 0.09],
    [-0.08, 0.09, 0.30],
], dtype=float)

# For g=exp(2f) delta in dimension three and df(0)=0:
# Ric(0) = -H - tr(H) I, where H=Hess f(0).
HESSIAN = -RICCI_EXACT + 0.25 * np.trace(RICCI_EXACT) * np.eye(3)

# Fully symmetric cubic jet; it makes nabla Ric nonzero at the origin.
CUBIC = np.zeros((3, 3, 3), dtype=float)
CUBIC[0, 0, 0] = 0.21
for index in ((0, 1, 2), (0, 2, 1), (1, 0, 2),
              (1, 2, 0), (2, 0, 1), (2, 1, 0)):
    CUBIC[index] = 0.04


def tetrahedra(seed=136, count=6):
    rng = np.random.default_rng(seed)
    result = []
    while len(result) < count:
        vertices = rng.normal(size=(4, 3))
        volume = abs(np.linalg.det(vertices[1:] - vertices[0])) / 6.0
        if volume < 0.02:
            continue
        bary = np.full((4, 4), volume / 20.0)
        np.fill_diagonal(bary, volume / 10.0)
        moment = vertices.T @ bary @ vertices
        result.append((vertices, volume, moment))
    return result


def measurement_matrix(items):
    rows = []
    for _, volume, moment in items:
        m = moment / volume
        rows.append([m[0, 0], m[1, 1], m[2, 2],
                     2*m[0, 1], 2*m[0, 2], 2*m[1, 2]])
    return np.asarray(rows, dtype=float)


def quadrature(vertices, order=7):
    nodes, weights = leggauss(order)
    nodes, weights = (nodes + 1.0) / 2.0, weights / 2.0
    points, measures = [], []
    jacobian = abs(np.linalg.det(vertices[1:] - vertices[0]))
    for i, a in enumerate(nodes):
        for j, b in enumerate(nodes):
            for k, c in enumerate(nodes):
                y = (vertices[0] + a*(vertices[1]-vertices[0])
                     + (1-a)*b*(vertices[2]-vertices[0])
                     + (1-a)*(1-b)*c*(vertices[3]-vertices[0]))
                points.append(y)
                measures.append(weights[i]*weights[j]*weights[k]
                                * (1-a)**2 * (1-b) * jacobian)
    return np.asarray(points), np.asarray(measures)


def conformal_data(x):
    f = (0.5*np.einsum("ni,ij,nj->n", x, HESSIAN, x)
         + (1.0/6.0)*np.einsum("ijk,ni,nj,nk->n", CUBIC, x, x, x))
    grad = (x @ HESSIAN
            + 0.5*np.einsum("ijk,nj,nk->ni", CUBIC, x, x))
    hess = (np.broadcast_to(HESSIAN, (len(x), 3, 3)).copy()
            + np.einsum("ijk,nk->nij", CUBIC, x))
    return f, grad, hess


def geodesic_rhs(state):
    x, velocity, derivative_x, derivative_v = state
    f, grad, hess = conformal_data(x)
    grad_dot_v = np.sum(grad*velocity, axis=1)
    speed2 = np.sum(velocity*velocity, axis=1)
    acceleration = (-2*velocity*grad_dot_v[:, None]
                    + speed2[:, None]*grad)

    # Variational equation for D exp: X'=V, V'=D_x(a)X+D_v(a)V.
    hess_x = np.einsum("nij,nja->nia", hess, derivative_x)
    v_hess_x = np.einsum("ni,nia->na", velocity, hess_x)
    dgamma = (2*velocity[:, :, None]*v_hess_x[:, None, :]
              - speed2[:, None, None]*hess_x)
    grad_dot_vvar = np.einsum("ni,nia->na", grad, derivative_v)
    v_dot_vvar = np.einsum("ni,nia->na", velocity, derivative_v)
    dacc_v = (-2*derivative_v*grad_dot_v[:, None, None]
              -2*velocity[:, :, None]*grad_dot_vvar[:, None, :]
              +2*grad[:, :, None]*v_dot_vvar[:, None, :])
    dacc_x = -dgamma
    return velocity, acceleration, derivative_v, dacc_x+dacc_v


def exponential_map(initial_velocity, steps=80):
    count = len(initial_velocity)
    x = np.zeros((count, 3))
    velocity = initial_velocity.copy()
    derivative_x = np.zeros((count, 3, 3))
    derivative_v = np.broadcast_to(np.eye(3), (count, 3, 3)).copy()
    state = (x, velocity, derivative_x, derivative_v)
    dt = 1.0 / steps
    for _ in range(steps):
        k1 = geodesic_rhs(state)
        s2 = tuple(a + dt*b/2 for a, b in zip(state, k1))
        k2 = geodesic_rhs(s2)
        s3 = tuple(a + dt*b/2 for a, b in zip(state, k2))
        k3 = geodesic_rhs(s3)
        s4 = tuple(a + dt*b for a, b in zip(state, k3))
        k4 = geodesic_rhs(s4)
        state = tuple(a + dt*(b+2*c+2*d+e)/6
                      for a, b, c, d, e in zip(state, k1, k2, k3, k4))
    return state[0], state[2]


def geodesic_tetrahedron_volume(vertices, scale, order=7, steps=80):
    points, weights = quadrature(vertices, order)
    endpoint, d_exp = exponential_map(scale*points, steps)
    f, _, _ = conformal_data(endpoint)
    jacobian = np.linalg.det(d_exp)
    if np.any(jacobian <= 0):
        raise RuntimeError("Exponential-map Jacobian lost orientation")
    # Pullback of physical volume form by exp_p(scale*y).
    return scale**3 * np.sum(weights * np.exp(3*f) * jacobian)


def run_audit():
    items = tetrahedra()
    matrix = measurement_matrix(items)
    singular = np.linalg.svd(matrix, compute_uv=False)
    if np.linalg.matrix_rank(matrix) != 6:
        raise RuntimeError("Moment matrix is rank deficient")
    target = np.array([RICCI_EXACT[0, 0], RICCI_EXACT[1, 1],
                       RICCI_EXACT[2, 2], RICCI_EXACT[0, 1],
                       RICCI_EXACT[0, 2], RICCI_EXACT[1, 2]])
    scales = [0.06, 0.045, 0.03375, 0.0253125]
    # Fixed relative volume perturbations; b_T scales the relative error by 6/r^2.
    relative_noise = np.random.default_rng(20261119).normal(size=6)*1e-9
    records, truncation_errors, noise_amplification = [], [], []
    for scale in scales:
        clean, perturbed = [], []
        for index, (vertices, euclidean_volume, _) in enumerate(items):
            measured = geodesic_tetrahedron_volume(vertices, scale)
            ratio = measured/(scale**3*euclidean_volume)
            clean.append(-6.0/scale**2*(ratio-1.0))
            perturbed.append(-6.0/scale**2
                             *(ratio*(1.0+relative_noise[index])-1.0))
        estimate, *_ = np.linalg.lstsq(matrix, np.asarray(clean), rcond=None)
        noisy_estimate, *_ = np.linalg.lstsq(matrix, np.asarray(perturbed), rcond=None)
        truncation = float(np.linalg.norm(estimate-target))
        noise = float(np.linalg.norm(noisy_estimate-estimate))
        truncation_errors.append(truncation)
        noise_amplification.append(noise)
        records.append({
            "scale": scale,
            "ricci_estimate_xx_yy_zz_xy_xz_yz": estimate.tolist(),
            "truncation_l2_error": truncation,
            "reconstruction_change_from_relative_volume_noise": noise,
        })
    return {
        "audit": "T136 smooth non-quadratic conformal metric via exponential map",
        "ricci_at_origin": RICCI_EXACT.tolist(),
        "ricci_derivation": "Ric(0)=-Hess(f)(0)-Delta(f)(0) I in dimension 3",
        "cubic_jet_nonzero": bool(np.linalg.norm(CUBIC) > 0),
        "moment_matrix_rank": int(np.linalg.matrix_rank(matrix)),
        "moment_matrix_condition_number": float(singular[0]/singular[-1]),
        "relative_volume_noise_amplitude": 1e-9,
        "scale_records": records,
        "successive_truncation_error_ratios": [
            truncation_errors[i+1]/truncation_errors[i]
            for i in range(len(truncation_errors)-1)],
        "successive_noise_amplification_ratios": [
            noise_amplification[i+1]/noise_amplification[i]
            for i in range(len(noise_amplification)-1)],
        "interpretation": (
            "A smooth conformal metric with a nonzero cubic jet is sampled "
            "through its numerical exponential map, not by inserting a "
            "quadratic normal-coordinate density. The normalized truncation "
            "error decreases approximately linearly with scale, while fixed "
            "relative volume noise is amplified approximately as r^{-2}. "
            "Finite manufactured numerical evidence only; no general stability "
            "theorem, Regge convergence, or Q6 limit is established."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2))
