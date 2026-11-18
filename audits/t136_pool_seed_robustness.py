#!/usr/bin/env python3
"""T136 robustness audit across candidate-pool seeds and pool sizes.

For every configuration, rebuilds the exact 12-probe D-, A-, and risk-selected
designs from scratch, then evaluates all of them on the same independent
validation grid. A/A-risk selection remains greedy from the D-optimal
six-probe seed; no global combinatorial optimum is claimed.
"""
from __future__ import annotations

import json
import numpy as np

from audits import t136_exact_design_comparison as base
from audits.t136_moment_design_optimization import (
    candidate_pool, greedy_d_optimal_design,
)

TRIALS = (
    {"label": "seed_A_pool128", "pool_seed": 13620261118, "pool_size": 128},
    {"label": "seed_B_pool128", "pool_seed": 13620261219, "pool_size": 128},
    {"label": "seed_C_pool128", "pool_seed": 13620261320, "pool_size": 128},
    {"label": "seed_A_pool256", "pool_seed": 13620261118, "pool_size": 256},
    {"label": "seed_B_pool256", "pool_seed": 13620261219, "pool_size": 256},
)
MC_REPLICAS = 2000
MC_SEED_BASE = 20261118


def monte_carlo_at_scale(vertices, indices, pool_size, scale, sigma_rel, seed, replicas):
    """Candidate-indexed common random numbers for one design and scale."""
    rng = np.random.default_rng(seed)
    eps = rng.normal(size=(pool_size, replicas)) * sigma_rel
    A = np.asarray([base.moment_row(v) for v in vertices], dtype=float)
    L = base.reconstruction_map(A)
    _, _, q = base.observation_and_covariance(
        vertices, scale, sigma_rel,
        base.EVALUATION_QUADRATURE_ORDER, base.EVALUATION_RK4_STEPS
    )
    clean_y = -6.0 * (q - 1.0) / scale**2
    noise_y = (-6.0 * q / scale**2)[:, None] * eps[np.asarray(indices)]
    noise_R = L @ noise_y
    estimates = L @ clean_y[:, None] + noise_R
    errors = estimates - base.target_ricci_vector()[:, None]
    squared_error = np.einsum(
        "ir,ij,jr->r", errors, base.TENSOR_METRIC, errors
    )
    centered_noise = noise_R - noise_R.mean(axis=1, keepdims=True)
    covariance = centered_noise @ centered_noise.T / (replicas - 1)
    noise_squared = np.einsum(
        "ir,ij,jr->r", centered_noise, base.TENSOR_METRIC, centered_noise
    )
    return {
        "replicas": int(replicas),
        "mean_squared_error": float(squared_error.mean()),
        "mean_squared_error_standard_error": float(
            squared_error.std(ddof=1) / np.sqrt(replicas)
        ),
        "covariance_R_monte_carlo": covariance.tolist(),
        "weighted_covariance_trace_monte_carlo": float(
            np.trace(base.TENSOR_METRIC @ covariance)
        ),
        "weighted_noise_trace_standard_error": float(
            noise_squared.std(ddof=1) / np.sqrt(replicas)
        ),
    }


def run_trial(config):
    pool_seed = int(config["pool_seed"])
    pool_size = int(config["pool_size"])
    pool_matrix, pool_vertices = candidate_pool(
        seed=pool_seed, size=pool_size, include_vertices=True
    )
    pool_matrix = np.asarray(pool_matrix, dtype=float)

    d12 = greedy_d_optimal_design(pool_matrix, count=base.PROBE_COUNT)
    common_seed = d12[:6]
    q_table = base.precompute_selection_q(pool_vertices)

    def objective(indices, kind):
        return base.cached_subset_objective(
            indices, kind, pool_matrix, q_table
        )

    a12 = base.greedy_exact_augmentation(
        pool_vertices, common_seed, base.PROBE_COUNT,
        lambda ids: objective(ids, "A"),
    )
    risk12 = base.greedy_exact_augmentation(
        pool_vertices, common_seed, base.PROBE_COUNT,
        lambda ids: objective(ids, "risk"),
    )

    designs = {
        "D": d12,
        "A": a12,
        "risk": risk12,
    }
    validation = {}
    monte_carlo = {}
    # Same candidate-indexed random stream for equal pool seeds at sizes 128
    # and 256; within each trial all three designs share candidate noise.
    mc_seed = MC_SEED_BASE + (pool_seed % 100000)
    for label, indices in designs.items():
        vertices = pool_vertices[np.asarray(indices)]
        summary = base.summarize_design(
            vertices, base.VALIDATION_SCALES, base.SIGMA_REL,
            base.EVALUATION_QUADRATURE_ORDER, base.EVALUATION_RK4_STEPS
        )
        minimum = next(
            row for row in summary["scale_records"]
            if row["scale"] == summary["minimum_risk_scale"]
        )
        validation[label] = {
            "probe_count": summary["probe_count"],
            "moment_rank": summary["moment_rank"],
            "moment_condition_number": summary["moment_condition_number"],
            "selected_candidate_indices": [int(i) for i in indices],
            "minimum_risk_scale": summary["minimum_risk_scale"],
            "bias_squared": minimum["bias_squared_frobenius"],
            "weighted_covariance_trace": minimum["weighted_covariance_trace"],
            "risk_squared": minimum["risk_squared_frobenius"],
            "rmse": float(np.sqrt(minimum["risk_squared_frobenius"])),
            "bias_noise_ratio": minimum["bias_noise_ratio"],
        }
        monte_carlo[label] = monte_carlo_at_scale(
            vertices, indices, pool_size, summary["minimum_risk_scale"],
            base.SIGMA_REL, mc_seed, MC_REPLICAS
        )

    d_risk = validation["D"]["risk_squared"]
    a_risk = validation["A"]["risk_squared"]
    r_risk = validation["risk"]["risk_squared"]
    return {
        "label": config["label"],
        "pool_seed": pool_seed,
        "pool_size": pool_size,
        "exact_probe_budget": base.PROBE_COUNT,
        "selection_scales": base.SELECTION_SCALES.tolist(),
        "validation_scales": base.VALIDATION_SCALES.tolist(),
        "selection_quadrature_order": base.SELECTION_QUADRATURE_ORDER,
        "selection_rk4_steps": base.SELECTION_RK4_STEPS,
        "evaluation_quadrature_order": base.EVALUATION_QUADRATURE_ORDER,
        "evaluation_rk4_steps": base.EVALUATION_RK4_STEPS,
        "monte_carlo_seed": mc_seed,
        "validation": validation,
        "monte_carlo_at_each_design_minimum": monte_carlo,
        "risk_design_relative_reduction_vs_D": float(1.0 - r_risk / d_risk),
        "risk_design_relative_reduction_vs_A": float(1.0 - r_risk / a_risk),
        "risk_design_beats_D": bool(r_risk < d_risk),
        "risk_design_beats_A": bool(r_risk < a_risk),
        "risk_design_beats_both": bool(r_risk < min(d_risk, a_risk)),
    }


def summarize_trials(trials):
    reductions_d = np.asarray([
        t["risk_design_relative_reduction_vs_D"] for t in trials
    ])
    reductions_a = np.asarray([
        t["risk_design_relative_reduction_vs_A"] for t in trials
    ])
    return {
        "trial_count": len(trials),
        "risk_design_beats_D_count": int(sum(t["risk_design_beats_D"] for t in trials)),
        "risk_design_beats_A_count": int(sum(t["risk_design_beats_A"] for t in trials)),
        "risk_design_beats_both_count": int(sum(t["risk_design_beats_both"] for t in trials)),
        "relative_risk_reduction_vs_D": {
            "mean": float(reductions_d.mean()),
            "standard_deviation_across_trials": float(reductions_d.std(ddof=1)),
            "minimum": float(reductions_d.min()),
            "maximum": float(reductions_d.max()),
        },
        "relative_risk_reduction_vs_A": {
            "mean": float(reductions_a.mean()),
            "standard_deviation_across_trials": float(reductions_a.std(ddof=1)),
            "minimum": float(reductions_a.min()),
            "maximum": float(reductions_a.max()),
        },
        "interpretation": (
            "These are five finite candidate-pool experiments, not a sampling "
            "distribution over all tetrahedral designs. Robustness is supported "
            "only if the risk-selected design repeatedly beats the alternatives "
            "on the independent validation grid; no universal guarantee follows."
        ),
    }


def run_audit():
    trials = [run_trial(config) for config in TRIALS]
    return {
        "audit": "T136 candidate-pool and seed robustness",
        "fixed_model": "same nonquadratic conformal metric and exact Ricci target",
        "fixed_budget": base.PROBE_COUNT,
        "fixed_noise_sigma_relative": base.SIGMA_REL,
        "fixed_selection_grid": base.SELECTION_SCALES.tolist(),
        "fixed_independent_validation_grid": base.VALIDATION_SCALES.tolist(),
        "trial_design": list(TRIALS),
        "selection_method": (
            "D-optimal exact 12-subset; A- and risk-selected exact 12-subsets "
            "greedily augmented from the same D-optimal six-probe seed"
        ),
        "monte_carlo_coupling": (
            "candidate-indexed Gaussian relative-volume noise, shared across "
            "the three designs within each trial; same seed reused for nested "
            "128/256 pools with the same pool-generation seed"
        ),
        "summary": summarize_trials(trials),
        "trials": trials,
        "limitations": (
            "Finite pool sizes and five deterministic configurations only. "
            "Greedy A/risk search is not globally optimal. The validation grid "
            "is independent of design selection but finite. Monte Carlo errors "
            "are reported at each design's own validation-grid minimizer."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2))
