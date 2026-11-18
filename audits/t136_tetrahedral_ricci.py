#!/usr/bin/env python3
"""T136 manufactured constant-curvature audit.

Uses normal coordinates in a 3D space form of sectional curvature K>0.
The exact normal-coordinate volume density is
    sqrt(det g)(x) = (sin(sqrt(K)|x|)/(sqrt(K)|x|))**2.
No external packages beyond NumPy are required.
"""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss


def tetrahedra(seed: int = 136, count: int = 6):
    rng = np.random.default_rng(seed)
    out = []
    while len(out) < count:
        vertices = rng.normal(size=(4, 3))
        volume = abs(np.linalg.det(vertices[1:] - vertices[0])) / 6.0
        if volume < 0.02:
            continue
        bary = np.full((4, 4), volume / 20.0)
        np.fill_diagonal(bary, volume / 10.0)
        moment = vertices.T @ bary @ vertices
        out.append((vertices, volume, moment))
    return out


def measurement_matrix(items):
    rows = []
    for _, volume, moment in items:
        m = moment / volume
        rows.append([m[0, 0], m[1, 1], m[2, 2],
                     2*m[0, 1], 2*m[0, 2], 2*m[1, 2]])
    return np.asarray(rows, dtype=float)


def tetra_volume_space_form(vertices, curvature, scale, order=18):
    nodes, weights = leggauss(order)
    nodes, weights = (nodes + 1.0) / 2.0, weights / 2.0
    jac = abs(np.linalg.det(vertices[1:] - vertices[0]))
    total = 0.0
    for i, a in enumerate(nodes):
        for j, b in enumerate(nodes):
            for k, c in enumerate(nodes):
                y = (vertices[0] + a*(vertices[1]-vertices[0])
                     + (1-a)*b*(vertices[2]-vertices[0])
                     + (1-a)*(1-b)*c*(vertices[3]-vertices[0]))
                rho = scale * np.linalg.norm(y)
                q = np.sqrt(curvature) * rho
                density = 1.0 if q == 0.0 else (np.sin(q)/q)**2
                total += (weights[i]*weights[j]*weights[k]
                          * (1-a)**2 * (1-b) * density)
    return scale**3 * jac * total


def run_audit():
    curvature = 0.4
    exact_ricci = np.array([2*curvature]*3 + [0.0]*3)
    items = tetrahedra()
    matrix = measurement_matrix(items)
    singular = np.linalg.svd(matrix, compute_uv=False)
    condition = float(singular[0] / singular[-1])
    if singular[-1] <= 1e-10:
        raise RuntimeError("Moment design is rank deficient")

    scales = [0.16, 0.12, 0.09, 0.0675]
    records = []
    errors = []
    for scale in scales:
        b = []
        for vertices, volume, _ in items:
            measured = tetra_volume_space_form(vertices, curvature, scale)
            b.append(-6.0/scale**2 * (measured/(scale**3*volume)-1.0))
        estimate, *_ = np.linalg.lstsq(matrix, np.asarray(b), rcond=None)
        error = float(np.linalg.norm(estimate-exact_ricci))
        errors.append(error)
        records.append({"scale": scale, "ricci_estimate": estimate.tolist(),
                        "l2_error": error})

    # Fixed, deterministic perturbation of the six leading-order observations.
    rng = np.random.default_rng(20261118)
    clean = matrix @ exact_ricci
    noise = rng.normal(size=6) * 1e-7
    noisy_estimate, *_ = np.linalg.lstsq(matrix, clean+noise, rcond=None)
    noise_error = float(np.linalg.norm(noisy_estimate-exact_ricci))

    # For a space form the density is even in radius, so the first omitted
    # term improves to O(r^2) in the normalized measurement (special case).
    ratios = [errors[i+1]/errors[i] for i in range(len(errors)-1)]
    return {
        "audit": "T136-A/B manufactured space-form and moment-rank audit",
        "curvature": curvature,
        "exact_ricci_components_xx_yy_zz_xy_xz_yz": exact_ricci.tolist(),
        "moment_matrix_rank": int(np.linalg.matrix_rank(matrix)),
        "moment_matrix_singular_values": singular.tolist(),
        "moment_matrix_condition_number": condition,
        "scale_records": records,
        "successive_error_ratios": ratios,
        "deterministic_noise_amplitude": 1e-7,
        "noise_reconstruction_l2_error": noise_error,
        "interpretation": (
            "Full rank is verified for this six-tetrahedron design. "
            "The constant-curvature space-form test shows decreasing error; "
            "its even radial density gives a special O(r^2) normalized "
            "remainder, stronger than the generic O(r) bound. "
            "This is a finite manufactured benchmark, not a continuum "
            "convergence or Q6/Regge result."
        ),
    }


if __name__ == "__main__":
    result = run_audit()
    print(json.dumps(result, indent=2))
