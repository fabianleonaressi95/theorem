#!/usr/bin/env python3
"""T136 finer-scale and integration-resolution audit for bias/noise balance.

No fitted target is imposed. The audit compares the same deterministic
manufactured metric and probe designs at a finer r-grid and at two numerical
integration resolutions. It is intentionally a finite numerical diagnostic.
"""
from __future__ import annotations

import json
import numpy as np

from audits.t136_nonquadratic_conformal import (
    RICCI_EXACT, geodesic_tetrahedron_volume, tetrahedra,
)
from audits.t136_scale_selection import (
    TENSOR_METRIC, design_matrix, target_ricci_vector,
)
from audits.t136_moment_design_optimization import (
    candidate_pool, greedy_d_optimal_design,
)

SIGMA = 1.0e-9
FINE_SCALES = (0.00375, 0.00210, 0.00120, 0.00090,
               0.00060, 0.00040, 0.00030)
RESOLUTIONS = ((7, 80), (9, 120))


def evaluate(vertices, matrix, scale, order, steps):
    inverse = np.linalg.pinv(matrix)
    ratios = []
    for tetra in vertices:
        euclidean_volume = abs(np.linalg.det(tetra[1:] - tetra[0])) / 6.0
        volume = geodesic_tetrahedron_volume(
            tetra, scale, order=order, steps=steps
        )
        ratios.append(volume / (scale**3 * euclidean_volume))
    ratios = np.asarray(ratios)

    estimate = inverse @ (-6.0 / scale**2 * (ratios - 1.0))
    bias = estimate - target_ricci_vector()
    bias_sq = float(bias @ TENSOR_METRIC @ bias)

    variances = (6.0 * SIGMA * ratios / scale**2)**2
    covariance = (inverse * variances[None, :]) @ inverse.T
    covariance = 0.5 * (covariance + covariance.T)
    noise_sq = float(np.trace(TENSOR_METRIC @ covariance))
    bias_norm = float(np.sqrt(max(0.0, bias_sq)))
    noise_rms = float(np.sqrt(max(0.0, noise_sq)))
    return {
        "scale": float(scale),
        "bias_frobenius": bias_norm,
        "noise_rms_frobenius": noise_rms,
        "rho_bias_over_noise": bias_norm / noise_rms,
        "effective_bias_coefficient": bias_norm / scale,
        "effective_noise_coefficient": scale**2 * noise_rms / SIGMA,
        "risk_rmse": float(np.sqrt(max(0.0, bias_sq + noise_sq))),
        "max_abs_volume_ratio_minus_one": float(np.max(np.abs(ratios - 1.0))),
    }


def build_designs():
    base = tetrahedra()
    six = np.asarray([item[0] for item in base])
    pool, pool_vertices = candidate_pool(include_vertices=True)
    indices = greedy_d_optimal_design(pool, count=12)
    twelve = pool_vertices[indices]
    return {
        "six_probe": (six, design_matrix(six)),
        "twelve_probe_d_optimal": (twelve, design_matrix(twelve)),
    }


def run_audit():
    designs = build_designs()
    output = {
        "audit": "T136 finer-scale and integration-resolution check",
        "noise_sigma_relative_volume": SIGMA,
        "scales": list(FINE_SCALES),
        "resolutions": [
            {"duffy_order": order, "rk4_steps": steps}
            for order, steps in RESOLUTIONS
        ],
        "designs": {},
        "interpretation": (
            "rho is measured from the clean reconstruction bias and the "
            "analytically propagated covariance. The two integration settings "
            "are a numerical sensitivity check, not rigorous error bounds. "
            "A finite list of scales cannot establish an asymptotic limit."
        ),
    }

    for name, (vertices, matrix) in designs.items():
        design_result = {
            "moment_rank": int(np.linalg.matrix_rank(matrix)),
            "moment_condition_number": float(np.linalg.cond(matrix)),
            "resolution_records": {},
        }
        for order, steps in RESOLUTIONS:
            records = [
                evaluate(vertices, matrix, r, order, steps)
                for r in FINE_SCALES
            ]
            minimum = min(records, key=lambda row: row["risk_rmse"])
            design_result["resolution_records"][f"q{order}_rk{steps}"] = {
                "records": records,
                "grid_minimum_scale": minimum["scale"],
                "rho_at_grid_minimum": minimum["rho_bias_over_noise"],
            }
        coarse = design_result["resolution_records"]["q7_rk80"]["records"]
        fine = design_result["resolution_records"]["q9_rk120"]["records"]
        design_result["resolution_sensitivity"] = [
            {
                "scale": left["scale"],
                "bias_change": abs(left["bias_frobenius"] - right["bias_frobenius"]),
                "noise_change": abs(left["noise_rms_frobenius"] - right["noise_rms_frobenius"]),
                "rho_change": abs(left["rho_bias_over_noise"] - right["rho_bias_over_noise"]),
            }
            for left, right in zip(coarse, fine)
        ]
        output["designs"][name] = design_result
    return output


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2))
