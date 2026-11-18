#!/usr/bin/env python3
"""T136 scale selection from truncation bias and propagated volume-noise covariance.

The noise model is independent, zero-mean relative volume error:
    V_i^obs = V_i (1 + eps_i),  eps_i ~ N(0, sigma_rel^2).
For each scale the script computes clean geodesic volumes on the manufactured
smooth non-quadratic metric, then evaluates the exact linearized covariance
of the least-squares Ricci estimator under that measurement-noise model.
"""
from __future__ import annotations

import json
import numpy as np

from audits.t136_nonquadratic_conformal import (
    RICCI_EXACT, geodesic_tetrahedron_volume, tetrahedra,
)
from audits.t136_moment_design_optimization import (
    candidate_pool, greedy_d_optimal_design,
)


RELATIVE_VOLUME_NOISE = 1.0e-9
SCALES = (0.012, 0.009, 0.00675, 0.0050, 0.00375,
          0.00280, 0.00210, 0.00160, 0.00120, 0.00090)


def moment_row(vertices):
    volume = abs(np.linalg.det(vertices[1:] - vertices[0])) / 6.0
    bary = np.full((4, 4), volume / 20.0)
    np.fill_diagonal(bary, volume / 10.0)
    moment = vertices.T @ bary @ vertices / volume
    return np.array([moment[0, 0], moment[1, 1], moment[2, 2],
                     2*moment[0, 1], 2*moment[0, 2], 2*moment[1, 2]])


def design_matrix(vertices):
    return np.asarray([moment_row(v) for v in vertices], dtype=float)


def target_ricci_vector():
    return np.array([RICCI_EXACT[0, 0], RICCI_EXACT[1, 1],
                     RICCI_EXACT[2, 2], RICCI_EXACT[0, 1],
                     RICCI_EXACT[0, 2], RICCI_EXACT[1, 2]])


def evaluate_design(vertices, matrix, scale, sigma_rel):
    ratios = []
    for tetra in vertices:
        euclidean_volume = abs(np.linalg.det(tetra[1:] - tetra[0])) / 6.0
        measured = geodesic_tetrahedron_volume(tetra, scale)
        ratios.append(measured / (scale**3 * euclidean_volume))
    ratios = np.asarray(ratios)

    observations = -6.0 / scale**2 * (ratios - 1.0)
    pseudoinverse = np.linalg.pinv(matrix)
    estimate = pseudoinverse @ observations
    bias = estimate - target_ricci_vector()

    # Independent relative volume noise gives Var(b_i)=36 sigma^2 q_i^2/r^4.
    variances = (6.0 * sigma_rel * ratios / scale**2)**2
    covariance = (pseudoinverse * variances[None, :]) @ pseudoinverse.T
    covariance = 0.5 * (covariance + covariance.T)
    noise_rms = float(np.sqrt(max(0.0, np.trace(covariance))))
    bias_norm = float(np.linalg.norm(bias))
    rmse = float(np.sqrt(bias_norm**2 + noise_rms**2))
    return {
        "scale": float(scale),
        "bias_l2": bias_norm,
        "noise_rms_l2": noise_rms,
        "expected_total_rmse_l2": rmse,
        "covariance_trace": float(np.trace(covariance)),
        "max_volume_ratio_deviation": float(np.max(np.abs(ratios - 1.0))),
    }


def summarize_design(vertices, matrix, sigma_rel):
    rows = [evaluate_design(vertices, matrix, r, sigma_rel) for r in SCALES]
    optimum = min(rows, key=lambda row: row["expected_total_rmse_l2"])

    # Estimate asymptotic coefficients from the four finest scales:
    # ||bias|| ~ a r and RMS(noise) ~ b sigma_rel/r^2.
    tail = rows[-4:]
    a = float(np.mean([row["bias_l2"] / row["scale"] for row in tail]))
    b = float(np.mean([
        row["noise_rms_l2"] * row["scale"]**2 / sigma_rel
        for row in tail
    ]))
    asymptotic_optimum = (
        (np.sqrt(2.0) * b * sigma_rel / a)**(1.0/3.0)
        if a > 0.0 and b > 0.0 else None
    )
    return {
        "probe_count": int(len(vertices)),
        "moment_rank": int(np.linalg.matrix_rank(matrix)),
        "moment_condition_number": float(np.linalg.cond(matrix)),
        "scale_records": rows,
        "grid_optimal_scale": optimum["scale"],
        "grid_minimum_expected_rmse_l2": optimum["expected_total_rmse_l2"],
        "asymptotic_bias_coefficient_a": a,
        "asymptotic_noise_coefficient_b": b,
        "asymptotic_optimal_scale": asymptotic_optimum,
    }


def run_audit():
    baseline_items = tetrahedra()
    baseline_vertices = np.asarray([item[0] for item in baseline_items])
    pool, candidate_vertices = candidate_pool(include_vertices=True)
    selected = greedy_d_optimal_design(pool, count=12)
    optimized_vertices = candidate_vertices[selected]

    baseline = summarize_design(
        baseline_vertices, design_matrix(baseline_vertices),
        RELATIVE_VOLUME_NOISE,
    )
    optimized = summarize_design(
        optimized_vertices, design_matrix(optimized_vertices),
        RELATIVE_VOLUME_NOISE,
    )
    return {
        "audit": "T136 scale selection by bias-covariance balance",
        "metric": "same smooth non-quadratic conformal metric with numerical exp map",
        "relative_volume_noise_model": "independent zero-mean Gaussian relative errors",
        "relative_volume_noise_sigma": RELATIVE_VOLUME_NOISE,
        "scales": list(SCALES),
        "six_probe": baseline,
        "twelve_probe_d_optimal": optimized,
        "interpretation": (
            "At each scale the clean reconstruction bias is computed from "
            "geodesic volumes and the covariance is propagated analytically "
            "through the least-squares map. The reported grid optimum minimizes "
            "bias^2 + trace(covariance) for this metric, design, scale grid and "
            "noise model only. The cube-root asymptotic estimate assumes bias "
            "proportional to r and relative-volume noise proportional to "
            "sigma/r^2; neither coefficient is universal."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2))
