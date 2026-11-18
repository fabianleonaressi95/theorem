#!/usr/bin/env python3
"""T136 matched-budget comparison of exact 12-probe tetrahedral designs.

All designs use the same candidate pool, observation model, reconstruction map,
scale grids and common random numbers. The A- and risk-optimal designs are
greedy exact subsets (12 physical probes), not approximate weighted designs.
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
from audits.t136_scale_selection import TENSOR_METRIC, moment_row, target_ricci_vector

SEED = 13620261118
POOL_SIZE = 128
PROBE_COUNT = 12
SIGMA_REL = 1.0e-9
REPLICAS = 2000
SELECTION_SCALES = np.asarray(
    (0.012, 0.009, 0.00675, 0.0050, 0.00375,
     0.00280, 0.00210, 0.00160, 0.00120, 0.00090), dtype=float
)
# Independent validation grid: not used to select the risk-optimal design.
VALIDATION_SCALES = np.geomspace(0.0007, 0.014, 18)
SELECTION_QUADRATURE_ORDER = 3
SELECTION_RK4_STEPS = 20
EVALUATION_QUADRATURE_ORDER = 5
EVALUATION_RK4_STEPS = 40


def observation_and_covariance(vertices, scale, sigma_rel, order, steps):
    """Return y, Cov(y), and q for y_j=-6(q_j-1)/r^2.

    Relative volume errors satisfy eps_j iid, E eps=0, Var eps=sigma_rel^2.
    Thus Cov(y)=diag((6 sigma_rel q_j/r^2)^2).
    """
    volumes0 = np.abs(np.linalg.det(vertices[:, 1:] - vertices[:, :1])) / 6.0
    measured = np.asarray([
        geodesic_tetrahedron_volume(v, scale, order=order, steps=steps)
        for v in vertices
    ])
    q = measured / (scale**3 * volumes0)
    y = -6.0 * (q - 1.0) / scale**2
    covariance_y = np.diag((6.0 * sigma_rel * q / scale**2) ** 2)
    return y, covariance_y, q


def reconstruction_map(moment_matrix):
    """OLS left inverse L=(A^T A)^+ A^T, represented by pinv(A)."""
    return np.linalg.pinv(moment_matrix)


def evaluate_at_scale(vertices, scale, sigma_rel, order, steps):
    A = np.asarray([moment_row(v) for v in vertices], dtype=float)
    L = reconstruction_map(A)
    y, covariance_y, q = observation_and_covariance(
        vertices, scale, sigma_rel, order, steps
    )
    estimate = L @ y
    bias = estimate - target_ricci_vector()
    covariance_R = L @ covariance_y @ L.T
    covariance_R = 0.5 * (covariance_R + covariance_R.T)
    bias_sq = float(bias @ TENSOR_METRIC @ bias)
    variance = float(np.trace(TENSOR_METRIC @ covariance_R))
    return {
        "scale": float(scale),
        "bias_squared_frobenius": bias_sq,
        "weighted_covariance_trace": variance,
        "risk_squared_frobenius": bias_sq + variance,
        "bias_noise_ratio": (
            float(np.sqrt(bias_sq / variance)) if variance > 0 else None
        ),
        "bias_vector": bias.tolist(),
        "covariance_R": covariance_R.tolist(),
        "max_abs_q_minus_1": float(np.max(np.abs(q - 1.0))),
    }


def multiscale_objective(vertices, scales, kind, sigma_rel, order, steps):
    rows = [
        evaluate_at_scale(vertices, r, sigma_rel, order, steps)
        for r in scales
    ]
    if kind == "A":
        values = [row["weighted_covariance_trace"] for row in rows]
    elif kind == "risk":
        values = [row["risk_squared_frobenius"] for row in rows]
    else:
        raise ValueError(f"unknown objective: {kind}")
    return float(np.mean(values))


def precompute_selection_q(pool_vertices):
    """Compute low-fidelity volume ratios once per candidate and scale."""
    q_table = np.empty((len(pool_vertices), len(SELECTION_SCALES)))
    for i, vertices in enumerate(pool_vertices):
        volume0 = abs(np.linalg.det(vertices[1:] - vertices[0])) / 6.0
        for j, scale in enumerate(SELECTION_SCALES):
            volume = geodesic_tetrahedron_volume(
                vertices, scale, order=SELECTION_QUADRATURE_ORDER,
                steps=SELECTION_RK4_STEPS
            )
            q_table[i, j] = volume / (scale**3 * volume0)
    return q_table


def cached_subset_objective(indices, kind, pool_matrix, q_table):
    """Exact-subset objective evaluated from cached per-probe observations."""
    A = pool_matrix[np.asarray(indices)]
    if np.linalg.matrix_rank(A) < 6:
        return float("inf")
    L = reconstruction_map(A)
    total = []
    for j, scale in enumerate(SELECTION_SCALES):
        q = q_table[np.asarray(indices), j]
        y = -6.0 * (q - 1.0) / scale**2
        cov_y_diag = (6.0 * SIGMA_REL * q / scale**2)**2
        covariance_R = (L * cov_y_diag[None, :]) @ L.T
        variance = float(np.trace(TENSOR_METRIC @ covariance_R))
        if kind == "A":
            total.append(variance)
        elif kind == "risk":
            bias = L @ y - target_ricci_vector()
            total.append(float(bias @ TENSOR_METRIC @ bias) + variance)
        else:
            raise ValueError(f"unknown objective: {kind}")
    return float(np.mean(total))


def greedy_exact_augmentation(pool_vertices, initial_indices, count, objective):
    """Greedily augment a full-rank seed to an exact count of physical probes."""
    selected = list(initial_indices)
    available = set(range(len(pool_vertices))) - set(selected)
    while len(selected) < count:
        best_index, best_value = None, float("inf")
        for index in sorted(available):
            trial_indices = selected + [index]
            value = objective(trial_indices)
            if value < best_value:
                best_index, best_value = index, value
        if best_index is None:
            raise RuntimeError("could not augment to a full-rank exact design")
        selected.append(best_index)
        available.remove(best_index)
    return selected


def summarize_design(vertices, scales, sigma_rel, order, steps):
    A = np.asarray([moment_row(v) for v in vertices], dtype=float)
    records = [
        evaluate_at_scale(vertices, r, sigma_rel, order, steps)
        for r in scales
    ]
    optimum = min(records, key=lambda row: row["risk_squared_frobenius"])
    return {
        "probe_count": int(len(vertices)),
        "moment_rank": int(np.linalg.matrix_rank(A)),
        "moment_condition_number": float(np.linalg.cond(A)),
        "scale_records": records,
        "minimum_risk_scale": optimum["scale"],
        "minimum_risk_squared_frobenius": optimum["risk_squared_frobenius"],
        "bias_squared_at_minimum": optimum["bias_squared_frobenius"],
        "noise_variance_at_minimum": optimum["weighted_covariance_trace"],
        "bias_noise_ratio_at_minimum": optimum["bias_noise_ratio"],
    }


def monte_carlo_check(designs, scales, pool_size, sigma_rel, replicas, seed):
    """Common random numbers indexed by candidate and replica.

    A candidate's relative-volume error is reused whenever that candidate
    occurs in multiple designs and across scales. Distinct candidates and
    replicas receive independent standard-normal variates.
    """
    rng = np.random.default_rng(seed)
    eps = rng.normal(size=(pool_size, replicas)) * sigma_rel
    output = {}
    for name, (vertices, indices) in designs.items():
        A = np.asarray([moment_row(v) for v in vertices], dtype=float)
        L = reconstruction_map(A)
        per_scale = []
        for scale in scales:
            _, _, q = observation_and_covariance(
                vertices, scale, sigma_rel,
                EVALUATION_QUADRATURE_ORDER, EVALUATION_RK4_STEPS
            )
            clean_y = -6.0 * (q - 1.0) / scale**2
            noise_y = (-6.0 * q / scale**2)[:, None] * eps[np.asarray(indices)]
            estimates = L @ (clean_y[:, None] + noise_y)
            errors = estimates - target_ricci_vector()[:, None]
            noise_errors = estimates - (L @ clean_y)[:, None]
            centered_noise = noise_errors - np.mean(noise_errors, axis=1, keepdims=True)
            outer = np.einsum("ir,jr->rij", centered_noise, centered_noise)
            covariance_mc = np.mean(outer, axis=0)
            covariance_mc_se = np.std(outer, axis=0, ddof=1) / np.sqrt(replicas)
            squared = np.einsum(
                "ir,ij,jr->r", errors, TENSOR_METRIC, errors
            )
            per_scale.append({
                "scale": float(scale),
                "monte_carlo_mean_squared_error": float(np.mean(squared)),
                "monte_carlo_standard_error": float(
                    np.std(squared, ddof=1) / np.sqrt(replicas)
                ),
                "monte_carlo_covariance_R": covariance_mc.tolist(),
                "monte_carlo_covariance_entry_standard_errors": covariance_mc_se.tolist(),
            })
        output[name] = per_scale
    return output


def run_audit():
    # One shared candidate pool defines all three exact 12-probe comparisons.
    _, pool_vertices = candidate_pool(
        seed=SEED, size=POOL_SIZE, include_vertices=True
    )
    pool_matrix = np.asarray([moment_row(v) for v in pool_vertices])
    d12 = greedy_d_optimal_design(pool_matrix, count=PROBE_COUNT)
    d6 = d12[:6]

    # Selection uses a fixed low-fidelity table, computed once per candidate.
    # Final reported risks are recomputed at the higher evaluation resolution.
    q_table = precompute_selection_q(pool_vertices)
    objective = lambda ids, kind: cached_subset_objective(
        ids, kind, pool_matrix, q_table
    )
    a12 = greedy_exact_augmentation(
        pool_vertices, d6, PROBE_COUNT,
        lambda ids: objective(ids, "A"),
    )
    r12 = greedy_exact_augmentation(
        pool_vertices, d6, PROBE_COUNT,
        lambda ids: objective(ids, "risk"),
    )

    designs = {
        "d_optimal_exact_12": (pool_vertices[d12], d12),
        "a_optimal_exact_12": (pool_vertices[a12], a12),
        "risk_optimal_exact_12": (pool_vertices[r12], r12),
    }
    selection_results = {}
    for name, (vertices, _) in designs.items():
        selection_results[name] = {
            "selection_objective": (
                "logdet(A.T @ A)" if name.startswith("d_") else
                "equal-weight mean trace(W Cov(Rhat)) on selection scales"
                if name.startswith("a_") else
                "equal-weight mean [bias^T W bias + trace(W Cov(Rhat))] "
                "on selection scales"
            ),
            "selection_scales": SELECTION_SCALES.tolist(),
            "selection_quadrature_order": SELECTION_QUADRATURE_ORDER,
            "selection_rk4_steps": SELECTION_RK4_STEPS,
            "selected_candidate_indices": (
                d12 if name.startswith("d_") else
                a12 if name.startswith("a_") else r12
            ),
        }

    # Six-probe legacy benchmark is reported separately (different budget).
    legacy_items = tetrahedra(seed=136, count=6)
    legacy_vertices = np.asarray([item[0] for item in legacy_items])
    validation = {
        name: summarize_design(
            vertices, VALIDATION_SCALES, SIGMA_REL,
            EVALUATION_QUADRATURE_ORDER, EVALUATION_RK4_STEPS
        )
        for name, (vertices, _) in designs.items()
    }
    legacy = summarize_design(
        legacy_vertices, VALIDATION_SCALES, SIGMA_REL,
        EVALUATION_QUADRATURE_ORDER, EVALUATION_RK4_STEPS
    )
    monte_carlo = monte_carlo_check(
        designs, VALIDATION_SCALES, POOL_SIZE, SIGMA_REL, REPLICAS, SEED + 1
    )
    return {
        "audit": "T136 exact matched-budget design comparison",
        "observation_model": (
            "y_j(r)=-6(q_j(r)-1)/r^2; Vobs_j=V_j(1+eps_j); "
            "eps_j independent, zero mean, variance sigma_rel^2"
        ),
        "reconstruction": "Rhat=L_D y, L_D=pinv(A_D), ordinary least squares",
        "covariance": "Cov(Rhat)=L_D diag((6 sigma_rel q_j/r^2)^2) L_D.T",
        "tensor_metric": TENSOR_METRIC.tolist(),
        "candidate_pool_size": POOL_SIZE,
        "exact_probe_budget": PROBE_COUNT,
        "relative_noise_sigma": SIGMA_REL,
        "validation_scales": VALIDATION_SCALES.tolist(),
        "evaluation_quadrature_order": EVALUATION_QUADRATURE_ORDER,
        "evaluation_rk4_steps": EVALUATION_RK4_STEPS,
        "monte_carlo_replicas": REPLICAS,
        "common_random_numbers": (
            "relative-volume errors are generated once per candidate and "
            "replica; shared candidates reuse identical errors across designs"
        ),
        "selection": selection_results,
        "validation": validation,
        "legacy_six_probe_reference": legacy,
        "monte_carlo": monte_carlo,
        "decision_rule": (
            "No cross-objective dominance is presumed. Report each design's "
            "validation-grid minimum risk, minimizing scale, bias/noise ratio, "
            "and Monte Carlo uncertainty. A winner is declared only for a "
            "predeclared primary objective."
        ),
        "limitations": (
            "The A- and risk-optimal exact subsets are greedy augmentations "
            "from a common D-optimal six-probe seed, not global combinatorial "
            "optima. Design selection uses a lower numerical integration "
            "resolution than final evaluation. The six-probe reference has "
            "a different budget. Numerical resolution checks and tests remain "
            "separate from this audit."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2))
