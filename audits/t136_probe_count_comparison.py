#!/usr/bin/env python3
"""Compare 6 baseline and 12 D-optimal probes on the same smooth metric."""
from __future__ import annotations

import json
import numpy as np

from audits.t136_nonquadratic_conformal import (
    RICCI_EXACT, geodesic_tetrahedron_volume, tetrahedra,
)
from audits.t136_moment_design_optimization import (
    candidate_pool, greedy_d_optimal_design,
)


def moment_row(vertices):
    volume = abs(np.linalg.det(vertices[1:] - vertices[0])) / 6.0
    bary = np.full((4, 4), volume / 20.0)
    np.fill_diagonal(bary, volume / 10.0)
    moment = vertices.T @ bary @ vertices / volume
    return np.array([moment[0, 0], moment[1, 1], moment[2, 2],
                     2*moment[0, 1], 2*moment[0, 2], 2*moment[1, 2]])


def design_matrix(vertices):
    return np.asarray([moment_row(v) for v in vertices])


def fit_design(vertices, matrix, scale, relative_noise):
    observations, noisy_observations = [], []
    for index, tetra in enumerate(vertices):
        euclidean_volume = abs(np.linalg.det(tetra[1:] - tetra[0])) / 6.0
        measured = geodesic_tetrahedron_volume(tetra, scale)
        ratio = measured/(scale**3*euclidean_volume)
        clean = -6.0/scale**2*(ratio-1.0)
        observations.append(clean)
        noisy_observations.append(
            -6.0/scale**2*(ratio*(1.0+relative_noise[index])-1.0)
        )
    estimate, *_ = np.linalg.lstsq(matrix, np.asarray(observations), rcond=None)
    noisy_estimate, *_ = np.linalg.lstsq(
        matrix, np.asarray(noisy_observations), rcond=None
    )
    target = np.array([RICCI_EXACT[0, 0], RICCI_EXACT[1, 1],
                       RICCI_EXACT[2, 2], RICCI_EXACT[0, 1],
                       RICCI_EXACT[0, 2], RICCI_EXACT[1, 2]])
    return (float(np.linalg.norm(estimate-target)),
            float(np.linalg.norm(noisy_estimate-estimate)))


def run_audit():
    baseline_items = tetrahedra()
    baseline_vertices = [item[0] for item in baseline_items]
    pool, candidate_vertices = candidate_pool(include_vertices=True)
    selected = greedy_d_optimal_design(pool, count=12)
    optimized_vertices = candidate_vertices[selected]
    baseline_matrix = design_matrix(baseline_vertices)
    optimized_matrix = design_matrix(optimized_vertices)
    scales = [0.06, 0.045, 0.03375, 0.0253125]
    baseline_noise = np.random.default_rng(20261119).normal(size=6)*1e-9
    optimized_noise = np.random.default_rng(20261119).normal(size=12)*1e-9
    records = []
    for scale in scales:
        base_error, base_noise = fit_design(
            baseline_vertices, baseline_matrix, scale, baseline_noise
        )
        opt_error, opt_noise = fit_design(
            optimized_vertices, optimized_matrix, scale, optimized_noise
        )
        records.append({
            "scale": scale,
            "six_probe_truncation_error": base_error,
            "twelve_probe_truncation_error": opt_error,
            "six_probe_noise_change": base_noise,
            "twelve_probe_noise_change": opt_noise,
            "truncation_error_reduction_factor": base_error/opt_error,
            "noise_change_reduction_factor": base_noise/opt_noise,
        })
    return {
        "audit": "T136 six-vs-twelve probe comparison on non-quadratic conformal metric",
        "six_probe_condition_number": float(np.linalg.cond(baseline_matrix)),
        "twelve_probe_condition_number": float(np.linalg.cond(optimized_matrix)),
        "relative_volume_noise_amplitude": 1e-9,
        "scale_records": records,
        "interpretation": (
            "For this one smooth non-quadratic metric and fixed candidate pool, "
            "the D-optimal 12-probe family reduces both truncation reconstruction "
            "error and sensitivity to the same-amplitude relative volume noise "
            "compared with the original six-probe design. This is finite numerical "
            "evidence, not a uniform theorem for all metrics or noise models."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2))
