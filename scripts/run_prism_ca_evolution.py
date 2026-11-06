"""Run a small, reproducible PRISM cellular-automaton genetic search.

Examples:
  python -m scripts.run_prism_ca_evolution --mode rules
  python -m scripts.run_prism_ca_evolution --mode initial --fixed-rule 0x...
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from models.prism_ca_evolution import (
    EvolutionConfig,
    FitnessConfig,
    evolve_initial_states,
    evolve_rules,
    random_initial_states,
)
from models.prism_cellular_automata import PrismProductGraph


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("rules", "initial"), default="rules")
    parser.add_argument("--factors", nargs=5, type=int, default=(3, 3, 3, 3, 3))
    parser.add_argument("--population", type=int, default=8)
    parser.add_argument("--generations", type=int, default=3)
    parser.add_argument("--elites", type=int, default=2)
    parser.add_argument("--tournament", type=int, default=3)
    parser.add_argument("--mutation-rate", type=float, default=0.002)
    parser.add_argument("--steps", type=int, default=6)
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument("--initial-samples", type=int, default=3)
    parser.add_argument("--target-density", type=float, default=0.5)
    parser.add_argument("--activity-weight", type=float, default=1.0)
    parser.add_argument("--density-weight", type=float, default=1.0)
    parser.add_argument("--boundary-weight", type=float, default=0.0)
    parser.add_argument("--fixed-rule", type=lambda value: int(value, 0))
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main():
    args = parse_args()
    graph = PrismProductGraph(tuple(args.factors))
    config = EvolutionConfig(
        population_size=args.population,
        generations=args.generations,
        elite_count=args.elites,
        tournament_size=args.tournament,
        mutation_rate=args.mutation_rate,
        seed=args.seed,
        seed_elementary_rules=(args.mode == "rules"),
    )
    fitness = FitnessConfig(
        target_density=args.target_density,
        activity_weight=args.activity_weight,
        density_weight=args.density_weight,
        boundary_weight=args.boundary_weight,
    )
    experiment = {"mode": args.mode, "steps": args.steps}
    if args.mode == "rules":
        bank_seed = args.seed + 1
        bank = random_initial_states(graph, args.initial_samples, bank_seed)
        result = evolve_rules(graph, bank, args.steps, config, fitness)
        experiment["initial_state_bank"] = {
            "count": len(bank),
            "seed": bank_seed,
            "sha256": [hashlib.sha256(state).hexdigest() for state in bank],
        }
    else:
        if args.fixed_rule is None:
            raise SystemExit("--fixed-rule is required when --mode initial")
        result = evolve_initial_states(graph, args.fixed_rule, args.steps, config, fitness)
        experiment["fixed_rule_integer"] = args.fixed_rule
        experiment["initial_population_seed"] = args.seed
    payload = result.to_dict()
    payload["experiment"] = experiment
    payload["graph"] = {
        "factors": list(graph.factors),
        "vertices": graph.vertex_count,
        "degree": graph.degree,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(encoded + "\n", encoding="utf-8")
    print(encoded)


if __name__ == "__main__":
    main()
