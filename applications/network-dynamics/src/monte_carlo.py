"""Paired-seed Monte Carlo audit for the synthetic Network Dynamics baseline.

Each replicate uses one seed to generate the same agent profiles and initial
knowledge state for all three architectures. Intervals describe synthetic
between-seed variability, not empirical uncertainty.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Sequence

import numpy as np

from network_dynamics import DEFAULT_SEED, run_experiment

METRICS = (
    "skill_coverage_threshold_0_60",
    "mean_knowledge_state",
    "within_skill_dispersion",
    "robustness_largest_component_after_random_removal",
)


def monte_carlo(replicates: int = 100, seed: int = DEFAULT_SEED,
                steps: int = 160) -> list[dict]:
    if replicates < 2:
        raise ValueError("replicates must be at least 2")
    samples: dict[str, dict[str, list[float]]] = {}
    for replicate in range(replicates):
        rows = run_experiment(seed=seed + replicate, steps=steps)
        for row in rows:
            architecture = row["architecture"]
            samples.setdefault(architecture, {metric: [] for metric in METRICS})
            for metric in METRICS:
                samples[architecture][metric].append(float(row[metric]))

    summary: list[dict] = []
    for architecture in sorted(samples):
        for metric in METRICS:
            values = np.asarray(samples[architecture][metric], dtype=float)
            mean = float(values.mean())
            sample_std = float(values.std(ddof=1))
            standard_error = sample_std / np.sqrt(replicates)
            summary.append({
                "architecture": architecture,
                "metric": metric,
                "replicates": replicates,
                "mean": mean,
                "sample_std": sample_std,
                "ci95_normal_lower": mean - 1.96 * standard_error,
                "ci95_normal_upper": mean + 1.96 * standard_error,
                "seed_start": seed,
                "seed_end": seed + replicates - 1,
                "steps": steps,
                "interval_note": "normal-approximation CI over synthetic seed replicates",
            })
    return summary


def write_summary(rows: Sequence[dict], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "monte_carlo.json").write_text(
        json.dumps(list(rows), indent=2) + "\n", encoding="utf-8"
    )
    if rows:
        with (output_dir / "monte_carlo.csv").open(
            "w", newline="", encoding="utf-8"
        ) as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replicates", type=int, default=100)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--steps", type=int, default=160)
    parser.add_argument("--output", type=Path, default=Path("results"))
    args = parser.parse_args()
    rows = monte_carlo(args.replicates, args.seed, args.steps)
    write_summary(rows, args.output)
    print(f"Wrote {len(rows)} architecture-metric summaries from "
          f"{args.replicates} paired-seed replicates to {args.output}")


if __name__ == "__main__":
    main()
