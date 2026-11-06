"""Run symmetric two-population XOR co-evolution on a PRISM product graph."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from models.prism_ca_evolution import (
    EvolutionConfig,
    FitnessConfig,
    evolve_coupled_initial_states,
)
from models.prism_cellular_automata import PrismProductGraph


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--factors", nargs=5, type=int, default=(3, 3, 3, 3, 3))
    parser.add_argument("--fixed-rule", type=lambda value: int(value, 0), required=True)
    parser.add_argument("--population", type=int, default=6)
    parser.add_argument("--generations", type=int, default=3)
    parser.add_argument("--elites", type=int, default=1)
    parser.add_argument("--tournament", type=int, default=2)
    parser.add_argument("--mutation-rate", type=float, default=0.01)
    parser.add_argument("--steps", type=int, default=6)
    parser.add_argument("--seed-a", type=int, default=2026)
    parser.add_argument("--seed-b", type=int, default=2027)
    parser.add_argument("--target-density", type=float, default=0.5)
    parser.add_argument("--activity-weight", type=float, default=1.0)
    parser.add_argument("--density-weight", type=float, default=1.0)
    parser.add_argument("--boundary-weight", type=float, default=0.0)
    parser.add_argument("--interaction-weight", type=float, default=0.25)
    parser.add_argument("--output", type=Path, default=Path("prism_xor_coevolution.json"))
    return parser.parse_args()


def main():
    args = parse_args()
    graph = PrismProductGraph(tuple(args.factors))
    common = dict(
        population_size=args.population,
        generations=args.generations,
        elite_count=args.elites,
        tournament_size=args.tournament,
        mutation_rate=args.mutation_rate,
        seed_elementary_rules=False,
    )
    config_a = EvolutionConfig(seed=args.seed_a, **common)
    config_b = EvolutionConfig(seed=args.seed_b, **common)
    fitness = FitnessConfig(
        target_density=args.target_density,
        activity_weight=args.activity_weight,
        density_weight=args.density_weight,
        boundary_weight=args.boundary_weight,
    )
    result = evolve_coupled_initial_states(
        graph=graph,
        fixed_rule=args.fixed_rule,
        steps=args.steps,
        config_a=config_a,
        config_b=config_b,
        fitness=fitness,
        interaction_weight=args.interaction_weight,
    )
    result["graph"] = {
        "factors": list(graph.factors),
        "vertices": graph.vertex_count,
        "degree": graph.degree,
    }
    result["experiment"] = {
        "steps": args.steps,
        "seeds": {"population_a": args.seed_a, "population_b": args.seed_b},
        "fixed_rule_hex": hex(args.fixed_rule),
    }
    encoded = json.dumps(result, indent=2, sort_keys=True)
    args.output.write_text(encoded + "\n", encoding="utf-8")
    print(encoded)


if __name__ == "__main__":
    main()
