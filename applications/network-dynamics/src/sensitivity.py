"""Factorial sensitivity audit for synthetic organizational network models.

Uses paired seeds and shared agent profiles/initial states across architectures.
All conclusions are conditional on these stylized graph and update rules.
"""
from __future__ import annotations

import argparse
import csv
import itertools
import json
from pathlib import Path

import numpy as np

from network_dynamics import (
    DEFAULT_SEED, adjacency_matrix, build_networks, connected_components,
    neighbor_mixing_matrix, simulate_knowledge,
)

ETAS = (0.05, 0.22, 0.50)
RHOS = (0.0, 0.008, 0.05)
SKILL_RANGES = ((1, 2), (2, 3), (4, 5))
REMOVAL_FRACTIONS = (0.10, 0.30)
REMOVAL_MODES = ("random", "highest_degree")
ARCHITECTURES = ("hierarchical", "matrix", "practices_like")


def skill_profiles(rng: np.random.Generator, n_agents: int, n_skills: int,
                   low: int, high: int) -> np.ndarray:
    result = np.zeros((n_agents, n_skills), dtype=float)
    for agent in range(n_agents):
        count = int(rng.integers(low, min(high, n_skills) + 1))
        result[agent, rng.choice(n_skills, size=count, replace=False)] = 1.0
    return result


def largest_component_after_removal(adjacency: np.ndarray, removed: np.ndarray) -> float:
    retained = np.flatnonzero(~removed)
    if retained.size == 0:
        return 0.0
    reduced = adjacency[np.ix_(retained, retained)]
    return max(map(len, connected_components(reduced))) / retained.size


def removal_masks(adjacency: np.ndarray, fraction: float, mode: str,
                  rng: np.random.Generator, repetitions: int) -> list[np.ndarray]:
    n = adjacency.shape[0]
    count = max(1, int(round(fraction * n)))
    masks = []
    for _ in range(repetitions):
        removed = np.zeros(n, dtype=bool)
        if mode == "random":
            removed[rng.choice(n, size=count, replace=False)] = True
        else:
            # Break degree ties with seeded random jitter, then remove highest degree.
            priority = adjacency.sum(axis=1) + rng.random(n) * 1e-6
            removed[np.argsort(-priority)[:count]] = True
        masks.append(removed)
    return masks


def run_sensitivity(replicates: int = 20, seed: int = DEFAULT_SEED,
                    steps: int = 160, removal_repetitions: int = 20) -> list[dict]:
    if replicates < 2 or removal_repetitions < 1:
        raise ValueError("replicates must be >=2 and removal_repetitions >=1")
    scenarios = list(itertools.product(ETAS, RHOS, SKILL_RANGES,
                                       REMOVAL_FRACTIONS, REMOVAL_MODES))
    observations: dict[tuple, list[float]] = {}
    for scenario_index, (eta, rho, skill_range, fraction, mode) in enumerate(scenarios):
        low, high = skill_range
        for replicate in range(replicates):
            run_seed = seed + scenario_index * 100_000 + replicate
            rng = np.random.default_rng(run_seed)
            profiles = skill_profiles(rng, 30, 8, low, high)
            initial = profiles * rng.uniform(0.15, 0.55, size=profiles.shape)
            networks = build_networks(profiles, seed=run_seed + 1, n_edges=45)
            for architecture_index, architecture in enumerate(ARCHITECTURES):
                adjacency = adjacency_matrix(30, networks[architecture])
                mixing = neighbor_mixing_matrix(adjacency)
                final_state = simulate_knowledge(
                    mixing, initial, profiles, steps=steps, eta=eta, rho=rho
                )
                masks = removal_masks(
                    adjacency, fraction, mode,
                    np.random.default_rng(run_seed + 5000 + architecture_index),
                    removal_repetitions,
                )
                robustness = float(np.mean([
                    largest_component_after_removal(adjacency, mask) for mask in masks
                ]))
                values = (
                    float(np.mean(final_state > 0.60)),
                    float(final_state.mean()),
                    float(np.mean(np.std(final_state, axis=0))),
                    robustness,
                )
                keys = (
                    (eta, rho, low, high, fraction, mode, architecture, "skill_coverage"),
                    (eta, rho, low, high, fraction, mode, architecture, "mean_knowledge"),
                    (eta, rho, low, high, fraction, mode, architecture, "within_skill_dispersion"),
                    (eta, rho, low, high, fraction, mode, architecture, "largest_component_retained"),
                )
                for key, value in zip(keys, values):
                    observations.setdefault(key, []).append(value)

    rows = []
    for key, values_list in sorted(observations.items(), key=lambda item: str(item[0])):
        eta, rho, low, high, fraction, mode, architecture, metric = key
        values = np.asarray(values_list, dtype=float)
        mean = float(values.mean())
        se = float(values.std(ddof=1) / np.sqrt(replicates))
        rows.append({
            "eta": eta, "rho": rho, "skills_per_agent_min": low,
            "skills_per_agent_max": high, "removal_fraction": fraction,
            "removal_mode": mode, "architecture": architecture, "metric": metric,
            "replicates": replicates, "mean": mean,
            "sample_std": float(values.std(ddof=1)),
            "ci95_normal_lower": mean - 1.96 * se,
            "ci95_normal_upper": mean + 1.96 * se,
            "steps": steps, "removal_repetitions_per_replicate": removal_repetitions,
        })
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replicates", type=int, default=20)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--steps", type=int, default=160)
    parser.add_argument("--removal-repetitions", type=int, default=20)
    parser.add_argument("--output", type=Path, default=Path("results"))
    args = parser.parse_args()
    rows = run_sensitivity(args.replicates, args.seed, args.steps,
                           args.removal_repetitions)
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "sensitivity.json").write_text(
        json.dumps(rows, indent=2) + "\n", encoding="utf-8"
    )
    with (args.output / "sensitivity.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} sensitivity summaries from {args.replicates} replicates")


if __name__ == "__main__":
    main()
