"""Structural diagnostics and degree-preserving rewiring-intensity sweep.

All outputs are synthetic graph diagnostics. No empirical organizational inference.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np

from network_dynamics import DEFAULT_SEED, N_AGENTS, N_EDGES, N_SKILLS, build_networks, make_skill_profiles
from topology_control import ARCHITECTURES, degree_preserving_rewire, adjacency_matrix, connected_components

INTENSITIES = (0, 1, 5, 20, 50, 100)


def _degrees(edges: set[tuple[int, int]], n: int) -> np.ndarray:
    if not edges:
        return np.zeros(n, dtype=float)
    return np.bincount(np.asarray(sorted(edges)).reshape(-1), minlength=n).astype(float)


def _local_clustering(adjacency: np.ndarray) -> float:
    values = []
    for i in range(len(adjacency)):
        neighbors = np.flatnonzero(adjacency[i])
        k = len(neighbors)
        if k < 2:
            values.append(0.0)
            continue
        links = float(adjacency[np.ix_(neighbors, neighbors)].sum()) / 2.0
        values.append(2.0 * links / (k * (k - 1)))
    return float(np.mean(values))


def _degree_assortativity(adjacency: np.ndarray) -> float:
    u, v = np.where(np.triu(adjacency, 1) > 0)
    if len(u) < 2:
        return float("nan")
    degree = adjacency.sum(axis=1)
    x, y = degree[u], degree[v]
    if np.std(x) == 0 or np.std(y) == 0:
        return float("nan")
    return float(np.corrcoef(x, y)[0, 1])


def _competence_edge_similarity(edges: set[tuple[int, int]], profiles: np.ndarray) -> float:
    if not edges:
        return float("nan")
    scores = []
    for i, j in edges:
        union = np.logical_or(profiles[i] > 0, profiles[j] > 0).sum()
        intersection = np.logical_and(profiles[i] > 0, profiles[j] > 0).sum()
        scores.append(float(intersection / union) if union else 0.0)
    return float(np.mean(scores))


def _largest_component_average_path(adjacency: np.ndarray) -> float:
    components = connected_components(adjacency)
    largest = max(components, key=len)
    if len(largest) < 2:
        return 0.0
    sub = adjacency[np.ix_(largest, largest)]
    distances = []
    for source in range(len(largest)):
        dist = np.full(len(largest), -1, dtype=int)
        dist[source] = 0
        queue = [source]
        for node in queue:
            for neighbor in np.flatnonzero(sub[node]):
                neighbor = int(neighbor)
                if dist[neighbor] < 0:
                    dist[neighbor] = dist[node] + 1
                    queue.append(neighbor)
        distances.extend(dist[dist > 0].tolist())
    return float(np.mean(distances)) if distances else 0.0


def _greedy_modularity(adjacency: np.ndarray) -> float:
    """Maximum modularity reached by deterministic greedy community merging."""
    m2 = float(adjacency.sum())
    if m2 == 0:
        return 0.0
    n = len(adjacency)
    degree = adjacency.sum(axis=1)
    communities = [{i} for i in range(n)]

    def q(partition):
        total = 0.0
        for group in partition:
            idx = sorted(group)
            internal = float(adjacency[np.ix_(idx, idx)].sum())
            volume = float(degree[idx].sum())
            total += internal / m2 - (volume / m2) ** 2
        return total

    best = q(communities)
    while len(communities) > 1:
        candidate = None
        candidate_q = best
        for i in range(len(communities)):
            for j in range(i + 1, len(communities)):
                merged = communities[i] | communities[j]
                trial = [g for k, g in enumerate(communities) if k not in (i, j)] + [merged]
                value = q(trial)
                if value > candidate_q + 1e-12:
                    candidate_q, candidate = value, (i, j, merged)
        if candidate is None:
            break
        i, j, merged = candidate
        communities = [g for k, g in enumerate(communities) if k not in (i, j)] + [merged]
        best = candidate_q
    return float(best)


def structural_metrics(edges: set[tuple[int, int]], profiles: np.ndarray) -> dict:
    n = profiles.shape[0]
    adjacency = adjacency_matrix(n, edges)
    degree = _degrees(edges, n)
    return {
        "nodes": n,
        "edges": len(edges),
        "components": len(connected_components(adjacency)),
        "largest_component_fraction": max(map(len, connected_components(adjacency))) / n,
        "mean_degree": float(degree.mean()),
        "degree_variance": float(degree.var()),
        "mean_local_clustering": _local_clustering(adjacency),
        "greedy_modularity": _greedy_modularity(adjacency),
        "degree_assortativity": _degree_assortativity(adjacency),
        "mean_edge_competence_jaccard": _competence_edge_similarity(edges, profiles),
        "largest_component_average_path": _largest_component_average_path(adjacency),
    }


def run_structural_sweep(replicates: int = 30, seed: int = DEFAULT_SEED,
                         intensities: tuple[int, ...] = INTENSITIES) -> list[dict]:
    if replicates < 2:
        raise ValueError("replicates must be >=2")
    if any(x < 0 for x in intensities):
        raise ValueError("rewiring intensities must be non-negative")
    metric_names = (
        "largest_component_fraction", "degree_variance", "mean_local_clustering",
        "greedy_modularity", "degree_assortativity",
        "mean_edge_competence_jaccard", "largest_component_average_path",
    )
    observations: dict[tuple[str, int, str], list[float]] = {}
    acceptance: dict[tuple[str, int], list[float]] = {}
    degree_ok: dict[tuple[str, int], bool] = {}
    for rep in range(replicates):
        rep_seed = seed + rep
        rng = np.random.default_rng(rep_seed)
        profiles = make_skill_profiles(rng, N_AGENTS, N_SKILLS)
        graphs = build_networks(profiles, seed=rep_seed + 1, n_edges=N_EDGES)
        for arch in ARCHITECTURES:
            original = set(graphs[arch])
            original_degree = _degrees(original, N_AGENTS)
            for intensity in intensities:
                if intensity == 0:
                    candidate = set(original)
                    accepted = 0
                else:
                    # Independent stream per replicate/architecture/intensity:
                    # every point starts from the same original graph.
                    rng_rewire = np.random.default_rng(
                        seed + rep * 1_000_003 + ARCHITECTURES.index(arch) * 100_003 + intensity * 997
                    )
                    candidate = degree_preserving_rewire(
                        original, N_AGENTS, rng_rewire, swaps_per_edge=intensity,
                    )
                    # Edge symmetric difference counts twice the number of accepted swaps.
                    accepted = len(original.symmetric_difference(candidate)) // 2
                key = (arch, intensity)
                degree_ok[key] = degree_ok.get(key, True) and np.array_equal(
                    original_degree, _degrees(candidate, N_AGENTS)
                )
                acceptance.setdefault(key, []).append(accepted / max(1, len(original) * intensity) if intensity else 1.0)
                metrics = structural_metrics(candidate, profiles)
                for metric in metric_names:
                    observations.setdefault((arch, intensity, metric), []).append(metrics[metric])

    rows = []
    for (arch, intensity, metric), values in sorted(observations.items()):
        arr = np.asarray(values, dtype=float)
        finite = arr[np.isfinite(arr)]
        mean = float(finite.mean()) if len(finite) else float("nan")
        se = float(finite.std(ddof=1) / np.sqrt(len(finite))) if len(finite) > 1 else float("nan")
        rows.append({
            "architecture": arch, "swaps_per_edge": intensity, "metric": metric,
            "replicates": replicates, "finite_replicates": len(finite),
            "mean": mean, "sample_std": float(finite.std(ddof=1)) if len(finite) else float("nan"),
            "ci95_normal_lower": mean - 1.96 * se if np.isfinite(se) else float("nan"),
            "ci95_normal_upper": mean + 1.96 * se if np.isfinite(se) else float("nan"),
            "mean_accepted_swap_fraction": float(np.mean(acceptance[(arch, intensity)])),
            "degree_sequence_preserved": degree_ok[(arch, intensity)],
        })
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replicates", type=int, default=30)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--intensities", type=int, nargs="+", default=list(INTENSITIES))
    parser.add_argument("--output", type=Path, default=Path("results"))
    args = parser.parse_args()
    rows = run_structural_sweep(args.replicates, args.seed, tuple(args.intensities))
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "structural_sweep.json").write_text(json.dumps(rows, indent=2, allow_nan=True) + "\n", encoding="utf-8")
    with (args.output / "structural_sweep.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} structural summaries from {args.replicates} paired synthetic replicates")


if __name__ == "__main__":
    main()
