#!/usr/bin/env python3
"""T136 audit of the bias/noise balance across the complete scale grid.

Reuses the deterministic geometric-volume and covariance calculations in
t136_scale_selection.py. It does not fit or force the sqrt(2) target.
"""
from __future__ import annotations

import json
import numpy as np

from audits.t136_scale_selection import (
    RELATIVE_VOLUME_NOISE,
    run_audit,
)


def enrich_design(design):
    records = []
    for row in design["scale_records"]:
        r = float(row["scale"])
        bias = float(row["bias_frobenius"])
        noise = float(row["noise_rms_frobenius"])
        rho = bias / noise if noise > 0.0 else None
        records.append({
            **row,
            "bias_noise_ratio": rho,
            "effective_bias_coefficient": bias / r,
            "effective_noise_coefficient": (
                r**2 * noise / RELATIVE_VOLUME_NOISE
            ),
        })

    optimum = min(
        records, key=lambda item: item["expected_total_rmse_frobenius"]
    )
    return {
        "probe_count": design["probe_count"],
        "moment_rank": design["moment_rank"],
        "grid_optimal_scale": optimum["scale"],
        "grid_optimum_bias_noise_ratio": optimum["bias_noise_ratio"],
        "sqrt2_reference": float(np.sqrt(2.0)),
        "absolute_ratio_gap": abs(
            optimum["bias_noise_ratio"] - np.sqrt(2.0)
        ),
        "scale_records": records,
        "interpretation": (
            "The ratio is evaluated from the deterministic clean-reconstruction "
            "bias and the analytically propagated covariance at each grid scale. "
            "The sqrt(2) identity is exact only for the stated asymptotic power "
            "laws; no convergence is inferred from a finite grid."
        ),
    }


def run_audit():
    base = run_audit_base = run_audit_original()
    return {
        "audit": "T136 finite-grid bias/noise ratio",
        "relative_volume_noise_sigma": RELATIVE_VOLUME_NOISE,
        "asymptotic_reference": "sqrt(2)",
        "six_probe": enrich_design(base["six_probe"]),
        "twelve_probe_d_optimal": enrich_design(
            base["twelve_probe_d_optimal"]
        ),
        "scope": (
            "Same non-quadratic conformal metric, deterministic probe designs, "
            "scale grid and independent relative-volume noise model as the "
            "T136 scale-selection audit."
        ),
    }


def run_audit_original():
    # Local import alias avoids changing or duplicating the underlying model.
    from audits.t136_scale_selection import run_audit as original
    return original()


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2))
