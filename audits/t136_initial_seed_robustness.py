#!/usr/bin/env python3
"""T136 sensitivity to the six-probe initialization of greedy A/risk designs.

For each fixed candidate pool, compare the existing D-optimal six-probe seed
with independently drawn, rank-six random seeds. A and risk then use the same
greedy augmentation rule and the same exact budget. Random seeds are generated
without inspecting either objective; no global optimum is claimed.
"""
from __future__ import annotations

import json
import numpy as np

from audits import t136_exact_design_comparison as base
from audits.t136_moment_design_optimization import (
    candidate_pool, greedy_d_optimal_design,
)

POOL_TRIALS = (
    {"label": "pool_A", "pool_seed": 13620261118},
    {"label": "pool_B", "pool_seed": 13620261219},
    {"label": "pool_C", "pool_seed": 13620261320},
)
RANDOM_SEEDS_PER_POOL = 4
SEED_GENERATOR_BASE = 13620261120
MC_REPLICAS = 2000


def random_full_rank_seeds(pool_matrix, pool_seed, count=RANDOM_SEEDS_PER_POOL):
    """Draw distinct full-rank six-subsets independently of design objectives."""
    rng = np.random.default_rng(SEED_GENERATOR_BASE + int(pool_seed) % 100000)
    found = []
    seen = set()
    attempts = 0
    while len(found) < count:
        attempts += 1
        if attempts > 100000:
            raise RuntimeError("unable to draw enough distinct full-rank seeds")
        ids = tuple(sorted(int(i) for i in rng.choice(
            len(pool_matrix), size=6, replace=False
        )))
        if ids in seen:
            continue
        if np.linalg.matrix_rank(pool_matrix[list(ids)]) == 6:
            seen.add(ids)
            found.append(list(ids))
    return found


def monte_carlo_at_minimum(vertices, indices, pool_size, scale, seed):
    rng = np.random.default_rng(seed)
    eps = rng.normal(size=(pool_size, MC_REPLICAS)) * base.SIGMA_REL
    A = np.asarray([base.moment_row(v) for v in vertices], dtype=float)
    L = base.reconstruction_map(A)
    _, _, q = base.observation_and_covariance(
        vertices, scale, base.SIGMA_REL,
        base.EVALUATION_QUADRATURE_ORDER, base.EVALUATION_RK4_STEPS
    )
    clean_y = -6.0 * (q - 1.0) / scale**2
    noise_y = (-6.0 * q / scale**2)[:, None] * eps[np.asarray(indices)]
    errors = L @ (clean_y[:, None] + noise_y) - base.target_ricci_vector()[:, None]
    squared = np.einsum("ir,ij,jr->r", errors, base.TENSOR_METRIC, errors)
    return {
        "replicas": MC_REPLICAS,
        "mean_squared_error": float(squared.mean()),
        "standard_error": float(squared.std(ddof=1) / np.sqrt(MC_REPLICAS)),
    }


def run_pool(config):
    pool_seed = int(config["pool_seed"])
    pool_matrix, vertices = candidate_pool(
        seed=pool_seed, size=128, include_vertices=True
    )
    pool_matrix = np.asarray(pool_matrix, dtype=float)
    q_table = base.precompute_selection_q(vertices)
    d12 = greedy_d_optimal_design(pool_matrix, count=base.PROBE_COUNT)
    initializations = [{"kind": "D-optimal", "seed_indices": d12[:6]}]
    initializations += [
        {"kind": f"random-{i+1}", "seed_indices": ids}
        for i, ids in enumerate(random_full_rank_seeds(pool_matrix, pool_seed))
    ]

    def objective(ids, criterion):
        return base.cached_subset_objective(ids, criterion, pool_matrix, q_table)

    records = []
    for init in initializations:
        seed_ids = init["seed_indices"]
        for criterion in ("A", "risk"):
            selected = base.greedy_exact_augmentation(
                vertices, seed_ids, base.PROBE_COUNT,
                lambda ids, c=criterion: objective(ids, c),
            )
            chosen_vertices = vertices[np.asarray(selected)]
            summary = base.summarize_design(
                chosen_vertices, base.VALIDATION_SCALES, base.SIGMA_REL,
                base.EVALUATION_QUADRATURE_ORDER, base.EVALUATION_RK4_STEPS
            )
            minimum = next(
                row for row in summary["scale_records"]
                if row["scale"] == summary["minimum_risk_scale"]
            )
            mc = monte_carlo_at_minimum(
                chosen_vertices, selected, len(vertices),
                summary["minimum_risk_scale"],
                base.SEED + pool_seed % 100000 + len(records),
            )
            records.append({
                "initialization": init["kind"],
                "initial_seed_indices": seed_ids,
                "criterion": criterion,
                "selected_candidate_indices": selected,
                "probe_count": summary["probe_count"],
                "moment_rank": summary["moment_rank"],
                "moment_condition_number": summary["moment_condition_number"],
                "validation_minimum_scale": summary["minimum_risk_scale"],
                "bias_squared": minimum["bias_squared_frobenius"],
                "weighted_covariance_trace": minimum["weighted_covariance_trace"],
                "risk_squared": minimum["risk_squared_frobenius"],
                "rmse": float(np.sqrt(minimum["risk_squared_frobenius"])),
                "monte_carlo": mc,
            })

    by_criterion = {}
    for criterion in ("A", "risk"):
        subset = [r for r in records if r["criterion"] == criterion]
        values = np.asarray([r["risk_squared"] for r in subset])
        by_criterion[criterion] = {
            "initialization_count": len(subset),
            "best_risk_squared": float(values.min()),
            "median_risk_squared": float(np.median(values)),
            "worst_risk_squared": float(values.max()),
            "relative_spread_worst_to_best": float(values.max()/values.min()-1.0),
            "D_seed_risk_squared": next(
                r["risk_squared"] for r in subset
                if r["initialization"] == "D-optimal"
            ),
            "random_seeds_beating_D_seed": int(sum(
                r["risk_squared"] < next(
                    x["risk_squared"] for x in subset
                    if x["initialization"] == "D-optimal"
                )
                for r in subset if r["initialization"].startswith("random-")
            )),
        }
    return {
        "pool": config["label"],
        "pool_seed": pool_seed,
        "pool_size": len(vertices),
        "probe_budget": base.PROBE_COUNT,
        "selection_scales": base.SELECTION_SCALES.tolist(),
        "validation_scales": base.VALIDATION_SCALES.tolist(),
        "selection_quadrature_order": base.SELECTION_QUADRATURE_ORDER,
        "selection_rk4_steps": base.SELECTION_RK4_STEPS,
        "evaluation_quadrature_order": base.EVALUATION_QUADRATURE_ORDER,
        "evaluation_rk4_steps": base.EVALUATION_RK4_STEPS,
        "initialization_results": records,
        "criterion_summary": by_criterion,
    }


def run_audit():
    pools = [run_pool(config) for config in POOL_TRIALS]
    return {
        "audit": "T136 greedy six-probe initialization sensitivity",
        "fixed_model": "same nonquadratic conformal metric and exact Ricci target",
        "fixed_noise_sigma_relative": base.SIGMA_REL,
        "fixed_exact_probe_budget": base.PROBE_COUNT,
        "initialization_protocol": (
            "One D-optimal six-probe seed plus four independently generated "
            "uniform random full-rank six-subsets per fixed candidate pool. "
            "Random seeds are selected without evaluating A or risk objectives."
        ),
        "augmentation_protocol": (
            "For every seed, independently augment to 12 probes using the same "
            "greedy A or tensor-risk objective and the same cached selection data."
        ),
        "validation_protocol": (
            "Every completed design is evaluated on the same independent "
            "18-scale validation grid at the same higher numerical resolution."
        ),
        "pool_results": pools,
        "limitations": (
            "Three fixed pools and four random initializations per pool are a "
            "finite sensitivity experiment, not a probability guarantee. "
            "Random full-rank seeds are not optimized A-seeds. Greedy completion "
            "is not globally optimal; validation-grid minima are not continuous "
            "scale minima. Monte Carlo checks use 2000 replicas per completed design."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2))
