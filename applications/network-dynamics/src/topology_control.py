"""Topology-only controls for the synthetic network-dynamics prototype.

Controls separate profile-informed edge selection from graph structure:
- profile-blind G(n,m) baseline;
- degree-preserving edge-swap rewires of each profile-informed architecture.

These are computational controls, not empirically calibrated organizational models.
"""
from __future__ import annotations

import argparse
import csv
import json
import itertools
from pathlib import Path

import numpy as np

from network_dynamics import (
    DEFAULT_SEED, N_AGENTS, N_EDGES, N_SKILLS, adjacency_matrix,
    build_networks, connected_components, make_skill_profiles,
    neighbor_mixing_matrix, robustness_score, simulate_knowledge,
)

ARCHITECTURES = ("hierarchical", "matrix", "practices_like")


def degree_preserving_rewire(edges: set[tuple[int, int]], n_agents: int,
                             rng: np.random.Generator,
                             swaps_per_edge: int = 20) -> set[tuple[int, int]]:
    """Randomize endpoints by valid double-edge swaps; preserve every degree."""
    current = set(edges)
    if swaps_per_edge < 1:
        raise ValueError("swaps_per_edge must be positive")
    target = swaps_per_edge * len(current)
    accepted = 0
    attempts = 0
    max_attempts = max(100, target * 30)
    edge_list = sorted(current)
    while accepted < target and attempts < max_attempts:
        attempts += 1
        a, b = edge_list[int(rng.integers(len(edge_list)))]
        c, d = edge_list[int(rng.integers(len(edge_list)))]
        if len({a, b, c, d}) < 4:
            continue
        if rng.random() < 0.5:
            new1, new2 = (min(a, d), max(a, d)), (min(c, b), max(c, b))
        else:
            new1, new2 = (min(a, c), max(a, c)), (min(b, d), max(b, d))
        if new1 == new2 or new1 in current or new2 in current:
            continue
        current.remove((a, b))
        current.remove((c, d))
        current.add(new1)
        current.add(new2)
        accepted += 1
        edge_list = sorted(current)
    return current


def profile_blind_graph(n_agents: int, n_edges: int,
                        rng: np.random.Generator) -> set[tuple[int, int]]:
    pairs = [(i, j) for i in range(n_agents) for j in range(i + 1, n_agents)]
    chosen = rng.choice(len(pairs), size=n_edges, replace=False)
    return {pairs[int(index)] for index in chosen}


def evaluate(edges: set[tuple[int, int]], profiles: np.ndarray,
             initial: np.ndarray, steps: int, eta: float, rho: float,
             seed: int, removal_repetitions: int) -> dict:
    n_agents = profiles.shape[0]
    adjacency = adjacency_matrix(n_agents, edges)
    final_state = simulate_knowledge(
        neighbor_mixing_matrix(adjacency), initial, profiles,
        steps=steps, eta=eta, rho=rho,
    )
    degree = adjacency.sum(axis=1).astype(int)
    return {
        "nodes": n_agents,
        "edges": len(edges),
        "components": len(connected_components(adjacency)),
        "degree_sequence": ",".join(map(str, sorted(degree.tolist()))),
        "skill_coverage_threshold_0_60": float(np.mean(final_state > 0.60)),
        "mean_knowledge_state": float(final_state.mean()),
        "within_skill_dispersion": float(np.mean(np.std(final_state, axis=0))),
        "random_removal_largest_component": robustness_score(
            adjacency, np.random.default_rng(seed + 700),
            removal_fraction=0.20, repetitions=removal_repetitions,
        ),
        "targeted_removal_largest_component": _targeted_robustness(
            adjacency, removal_fraction=0.20,
        ),
    }


def _targeted_robustness(adjacency: np.ndarray, removal_fraction: float) -> float:
    n = adjacency.shape[0]
    count = max(1, int(round(n * removal_fraction)))
    removed = np.argsort(-adjacency.sum(axis=1))[:count]
    keep = np.ones(n, dtype=bool)
    keep[removed] = False
    reduced = adjacency[np.ix_(keep, keep)]
    return max(map(len, connected_components(reduced))) / int(keep.sum())


def run_topology_control(replicates: int = 100, seed: int = DEFAULT_SEED,
                         steps: int = 160, eta: float = 0.22,
                         rho: float = 0.008, n_agents: int = N_AGENTS,
                         n_skills: int = N_SKILLS, n_edges: int = N_EDGES,
                         swaps_per_edge: int = 20,
                         removal_repetitions: int = 40) -> list[dict]:
    if replicates < 2:
        raise ValueError("replicates must be >=2")
    if n_edges < n_agents - 1 or n_edges > n_agents * (n_agents - 1) // 2:
        raise ValueError("invalid edge count for simple connected-capable graph")
    records: dict[tuple[str, str], list[float]] = {}
    paired_records: dict[tuple[str, str, str], list[float]] = {}
    degree_checks: dict[str, bool] = {}
    metric_names = (
        "skill_coverage_threshold_0_60", "mean_knowledge_state",
        "within_skill_dispersion", "random_removal_largest_component",
        "targeted_removal_largest_component",
    )
    for rep in range(replicates):
        rep_seed = seed + rep
        rng = np.random.default_rng(rep_seed)
        profiles = make_skill_profiles(rng, n_agents, n_skills)
        initial = profiles * rng.uniform(0.15, 0.55, size=profiles.shape)
        graphs = build_networks(profiles, seed=rep_seed + 1, n_edges=n_edges)
        controls: dict[str, set[tuple[int, int]]] = {
            "profile_blind_random": profile_blind_graph(
                n_agents, n_edges, np.random.default_rng(rep_seed + 200)
            )
        }
        for name in ARCHITECTURES:
            controls[f"{name}_original_profile_informed"] = set(graphs[name])
            controls[f"{name}_degree_preserving_rewire"] = degree_preserving_rewire(
                graphs[name], n_agents, np.random.default_rng(rep_seed + 300 + ARCHITECTURES.index(name)),
                swaps_per_edge=swaps_per_edge,
            )
            before = np.bincount(
                np.array(list(graphs[name])).reshape(-1), minlength=n_agents
            )
            after = np.bincount(
                np.array(list(controls[f"{name}_degree_preserving_rewire"])).reshape(-1),
                minlength=n_agents,
            )
            degree_checks[name] = degree_checks.get(name, True) and np.array_equal(before, after)
        replicate_metrics: dict[str, dict[str, float]] = {}
        for name, edges in controls.items():
            result = evaluate(
                edges, profiles, initial, steps, eta, rho,
                rep_seed + 1000, removal_repetitions,
            )
            replicate_metrics[name] = {metric: result[metric] for metric in metric_names}
            for metric in metric_names:
                records.setdefault((name, metric), []).append(result[metric])
        for left, right in itertools.combinations(sorted(controls), 2):
            for metric in metric_names:
                paired_records.setdefault((left, right, metric), []).append(
                    replicate_metrics[left][metric] - replicate_metrics[right][metric]
                )

    rows = []
    for (control, metric), vals in sorted(records.items()):
        arr = np.asarray(vals, dtype=float)
        mean = float(arr.mean())
        se = float(arr.std(ddof=1) / np.sqrt(replicates))
        rows.append({
            "control": control, "metric": metric, "replicates": replicates,
            "mean": mean, "sample_std": float(arr.std(ddof=1)),
            "ci95_normal_lower": mean - 1.96 * se,
            "ci95_normal_upper": mean + 1.96 * se,
            "degree_sequence_preserved": (
                degree_checks.get(control.removesuffix("_degree_preserving_rewire"), False)
                if control.endswith("_degree_preserving_rewire") else False
            ),
            "swaps_per_edge": swaps_per_edge, "steps": steps,
            "eta": eta, "rho": rho, "nodes": n_agents, "edges": n_edges,
        })
    for (left, right, metric), vals in sorted(paired_records.items()):
        arr = np.asarray(vals, dtype=float)
        mean = float(arr.mean())
        se = float(arr.std(ddof=1) / np.sqrt(replicates))
        rows.append({
            "control": f"{left}_minus_{right}", "metric": metric,
            "replicates": replicates, "mean": mean,
            "sample_std": float(arr.std(ddof=1)),
            "ci95_normal_lower": mean - 1.96 * se,
            "ci95_normal_upper": mean + 1.96 * se,
            "degree_sequence_preserved": False,
            "swaps_per_edge": swaps_per_edge, "steps": steps,
            "eta": eta, "rho": rho, "nodes": n_agents, "edges": n_edges,
        })
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replicates", type=int, default=100)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--steps", type=int, default=160)
    parser.add_argument("--swaps-per-edge", type=int, default=20)
    parser.add_argument("--removal-repetitions", type=int, default=40)
    parser.add_argument("--output", type=Path, default=Path("results"))
    args = parser.parse_args()
    rows = run_topology_control(
        replicates=args.replicates, seed=args.seed, steps=args.steps,
        swaps_per_edge=args.swaps_per_edge,
        removal_repetitions=args.removal_repetitions,
    )
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "topology_control.json").write_text(
        json.dumps(rows, indent=2) + "\n", encoding="utf-8"
    )
    with (args.output / "topology_control.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} topology-control summaries from {args.replicates} paired replicates")


if __name__ == "__main__":
    main()
