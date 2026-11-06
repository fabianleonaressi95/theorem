"""Repeated-seed PRISM CA rule-search benchmark with elementary controls.

This benchmark is deliberately a small-graph protocol. It records each seed,
initial-condition-bank hashes, control-rule scores, the evolved best rule and
its exact local automorphism audit. It is a reproducibility scaffold, not a
claim of statistical significance or physical emergence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from statistics import mean, pstdev

from models.prism_ca_evolution import (
    EvolutionConfig,
    FitnessConfig,
    evaluate_rule,
    evolve_rules,
    random_initial_states,
    rule_symmetry_report,
)
from models.prism_cellular_automata import PrismProductGraph, elementary_rules


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--factors", nargs=5, type=int, default=(3, 3, 3, 3, 3))
    parser.add_argument("--seeds", nargs="+", type=int, default=tuple(range(10)))
    parser.add_argument("--population", type=int, default=8)
    parser.add_argument("--generations", type=int, default=3)
    parser.add_argument("--elites", type=int, default=2)
    parser.add_argument("--tournament", type=int, default=3)
    parser.add_argument("--mutation-rate", type=float, default=0.002)
    parser.add_argument("--steps", type=int, default=6)
    parser.add_argument("--initial-samples", type=int, default=3)
    parser.add_argument("--target-density", type=float, default=0.5)
    parser.add_argument("--activity-weight", type=float, default=1.0)
    parser.add_argument("--density-weight", type=float, default=1.0)
    parser.add_argument("--boundary-weight", type=float, default=0.0)
    parser.add_argument("--output", type=Path, default=Path("prism_ca_benchmark.json"))
    return parser.parse_args()


def main():
    args = parse_args()
    if not args.seeds:
        raise SystemExit("at least one seed is required")
    if len(set(args.seeds)) != len(args.seeds):
        raise SystemExit("seeds must be unique")
    graph = PrismProductGraph(tuple(args.factors))
    fitness = FitnessConfig(
        target_density=args.target_density,
        activity_weight=args.activity_weight,
        density_weight=args.density_weight,
        boundary_weight=args.boundary_weight,
    )
    controls = elementary_rules()
    runs = []

    for seed in args.seeds:
        bank_seed = seed + 100_003
        bank = random_initial_states(graph, args.initial_samples, bank_seed)
        config = EvolutionConfig(
            population_size=args.population,
            generations=args.generations,
            elite_count=args.elites,
            tournament_size=args.tournament,
            mutation_rate=args.mutation_rate,
            seed=seed,
            seed_elementary_rules=True,
        )
        result = evolve_rules(graph, bank, args.steps, config, fitness)
        control_scores = {
            name: evaluate_rule(graph, bank, rule, args.steps, fitness)
            for name, rule in controls.items()
        }
        runs.append({
            "seed": seed,
            "initial_bank_seed": bank_seed,
            "initial_bank_sha256": [hashlib.sha256(state).hexdigest() for state in bank],
            "best_score": result.best_score,
            "best_rule_integer": result.best_genome,
            "best_rule_hex": hex(result.best_genome),
            "best_metrics": result.history[-1],
            "best_rule_symmetry": rule_symmetry_report(graph, result.best_genome),
            "control_scores": control_scores,
            "history": result.history,
            "evaluations": result.evaluations,
        })

    control_names = tuple(controls)
    summary = {
        "best_score_mean": mean(row["best_score"] for row in runs),
        "best_score_population_std": pstdev(row["best_score"] for row in runs),
        "control_score_summary": {
            name: {
                "mean": mean(row["control_scores"][name]["score"] for row in runs),
                "population_std": pstdev(row["control_scores"][name]["score"] for row in runs),
            }
            for name in control_names
        },
        "runs": len(runs),
    }
    payload = {
        "protocol": "repeated-seed PRISM local-rule GA; fixed initial-condition bank within each run",
        "graph": {
            "factors": list(graph.factors),
            "vertices": graph.vertex_count,
            "degree": graph.degree,
        },
        "fitness": {
            "target_density": fitness.target_density,
            "activity_weight": fitness.activity_weight,
            "density_weight": fitness.density_weight,
            "boundary_weight": fitness.boundary_weight,
        },
        "search": {
            "population_size": args.population,
            "generations": args.generations,
            "elite_count": args.elites,
            "tournament_size": args.tournament,
            "mutation_rate": args.mutation_rate,
            "steps": args.steps,
            "initial_samples": args.initial_samples,
            "seeds": args.seeds,
        },
        "summary": summary,
        "runs": runs,
        "interpretation_limit": (
            "Finite-horizon benchmark on the specified finite graph only; "
            "not evidence of continuum convergence, physical emergence, "
            "universality, or statistical significance."
        ),
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True)
    args.output.write_text(encoded + "\n", encoding="utf-8")
    print(encoded)


if __name__ == "__main__":
    main()
