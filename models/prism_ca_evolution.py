"""Deterministic genetic searches over PRISM CA rules and initial fields.

The rule-search and initial-state-search paths are deliberately separate:
the former evolves 2048-bit local truth tables while fixing initial fields;
the latter evolves binary fields while keeping one local rule fixed.
Fitness is an explicit, configurable finite-horizon diagnostic, not a
mathematical measure of physical emergence or complexity.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from itertools import permutations, product as cartesian_product
import random
from math import isfinite
from statistics import median
from typing import Sequence

from models.prism_cellular_automata import (
    RULE_BITS,
    RULE_MASK,
    DIMENSION,
    PrismProductGraph,
    elementary_rules,
    observables,
    step,
    validate_rule,
)


@dataclass(frozen=True)
class EvolutionConfig:
    population_size: int = 12
    generations: int = 5
    elite_count: int = 2
    tournament_size: int = 3
    mutation_rate: float = 0.01
    seed: int = 2026
    seed_elementary_rules: bool = True

    def validate(self) -> None:
        if isinstance(self.population_size, bool) or not isinstance(self.population_size, int) or self.population_size < 2:
            raise ValueError("population_size must be an integer >= 2")
        if isinstance(self.generations, bool) or not isinstance(self.generations, int) or self.generations < 0:
            raise ValueError("generations must be a nonnegative integer")
        if isinstance(self.elite_count, bool) or not isinstance(self.elite_count, int) or not 1 <= self.elite_count < self.population_size:
            raise ValueError("elite_count must be in [1, population_size)")
        if isinstance(self.tournament_size, bool) or not isinstance(self.tournament_size, int) or not 1 <= self.tournament_size <= self.population_size:
            raise ValueError("tournament_size must be in [1, population_size]")
        if isinstance(self.mutation_rate, bool) or not isinstance(self.mutation_rate, (int, float)) or not isfinite(float(self.mutation_rate)) or not 0.0 <= self.mutation_rate <= 1.0:
            raise ValueError("mutation_rate must be finite and lie in [0, 1]")
        if isinstance(self.seed, bool) or not isinstance(self.seed, int):
            raise ValueError("seed must be an integer")
        if not isinstance(self.seed_elementary_rules, bool):
            raise ValueError("seed_elementary_rules must be boolean")


@dataclass(frozen=True)
class FitnessConfig:
    """Transparent finite-horizon objective; all terms are reported separately."""

    target_density: float = 0.5
    activity_weight: float = 1.0
    density_weight: float = 1.0
    boundary_weight: float = 0.0

    def validate(self) -> None:
        for name in ("target_density", "activity_weight", "density_weight", "boundary_weight"):
            value = getattr(self, name)
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError(f"{name} must be numeric")
            if not isfinite(float(value)):
                raise ValueError(f"{name} must be finite")
            if not 0.0 <= float(value) <= 1.0 and name == "target_density":
                raise ValueError("target_density must lie in [0, 1]")
            if float(value) < 0.0:
                raise ValueError(f"{name} must be nonnegative")


@dataclass
class EvolutionResult:
    mode: str
    best_genome: int | bytes
    best_score: float
    history: list[dict]
    config: dict
    fitness_config: dict
    evaluations: int

    def to_dict(self) -> dict:
        genome = self.best_genome
        if isinstance(genome, bytes):
            genome = list(genome)
        return {
            "mode": self.mode,
            "best_genome": genome,
            "best_score": self.best_score,
            "history": self.history,
            "config": self.config,
            "fitness_config": self.fitness_config,
            "evaluations": self.evaluations,
        }


def random_initial_states(graph: PrismProductGraph, count: int, seed: int = 2026) -> tuple[bytes, ...]:
    if isinstance(count, bool) or not isinstance(count, int) or count < 1:
        raise ValueError("count must be a positive integer")
    if isinstance(seed, bool) or not isinstance(seed, int):
        raise ValueError("seed must be an integer")
    rng = random.Random(seed)
    return tuple(bytes(rng.getrandbits(1) for _ in range(graph.vertex_count)) for _ in range(count))


def _validate_states(graph: PrismProductGraph, states: Sequence[Sequence[int]]) -> tuple[bytes, ...]:
    if not states:
        raise ValueError("at least one initial state is required")
    validated = []
    for state in states:
        if len(state) != graph.vertex_count or any(
            isinstance(bit, bool) or not isinstance(bit, int) or bit not in (0, 1)
            for bit in state
        ):
            raise ValueError("every initial state must be a binary vector of graph vertex count")
        validated.append(bytes(state))
    return tuple(validated)


def _score_trajectory(
    graph: PrismProductGraph,
    initial: Sequence[int],
    rule: int,
    steps: int,
    fitness: FitnessConfig,
) -> dict:
    current = bytearray(initial)
    densities = []
    activities = []
    boundary_fractions = []
    edge_count = graph.vertex_count * graph.degree // 2
    for _ in range(steps):
        nxt = step(graph, current, rule)
        obs = observables(graph, current, nxt)
        densities.append(sum(nxt) / graph.vertex_count)
        activities.append(obs["temporal_activity"])
        boundary_fractions.append(obs["graph_dirichlet_energy"] / edge_count)
        current = nxt
    if steps == 0:
        densities = [sum(current) / graph.vertex_count]
        activities = [0.0]
        boundary_fractions = [0.0]
    mean_density = sum(densities) / len(densities)
    mean_activity = sum(activities) / len(activities)
    mean_boundary = sum(boundary_fractions) / len(boundary_fractions)
    score = (
        fitness.activity_weight * mean_activity
        - fitness.density_weight * abs(mean_density - fitness.target_density)
        - fitness.boundary_weight * mean_boundary
    )
    return {
        "score": score,
        "mean_density": mean_density,
        "mean_activity": mean_activity,
        "mean_boundary_fraction": mean_boundary,
    }


def evaluate_rule(
    graph: PrismProductGraph,
    initial_states: Sequence[Sequence[int]],
    rule: int,
    steps: int,
    fitness: FitnessConfig = FitnessConfig(),
) -> dict:
    rule = validate_rule(rule)
    fitness.validate()
    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 0:
        raise ValueError("steps must be a nonnegative integer")
    states = _validate_states(graph, initial_states)
    scores = [_score_trajectory(graph, state, rule, steps, fitness) for state in states]
    keys = ("score", "mean_density", "mean_activity", "mean_boundary_fraction")
    return {key: sum(row[key] for row in scores) / len(scores) for key in keys}


def _tournament(population: list, scores: list[float], size: int, rng: random.Random):
    candidates = [rng.randrange(len(population)) for _ in range(size)]
    winner = max(candidates, key=lambda i: (scores[i], -i))
    return population[winner]


def _mutate_rule(genome: int, rate: float, rng: random.Random) -> int:
    if rate <= 0.0:
        return genome
    if rate >= 1.0:
        return RULE_MASK ^ genome
    mask = 0
    for bit in range(RULE_BITS):
        if rng.random() < rate:
            mask |= 1 << bit
    return genome ^ mask


def _cross_rule(parent_a: int, parent_b: int, rng: random.Random) -> int:
    mask = rng.getrandbits(RULE_BITS)
    return (parent_a & mask) | (parent_b & (RULE_MASK ^ mask))


def _initial_rule_population(config: EvolutionConfig, rng: random.Random, supplied: Sequence[int] | None) -> list[int]:
    if supplied is not None:
        population = [validate_rule(rule) for rule in supplied]
        if len(population) != config.population_size:
            raise ValueError("initial rule population must equal population_size")
        return population
    population = []
    if config.seed_elementary_rules:
        controls = elementary_rules()
        for name in ("zero", "one", "identity", "negation"):
            if len(population) < config.population_size:
                population.append(controls[name])
    while len(population) < config.population_size:
        population.append(rng.getrandbits(RULE_BITS))
    return population



def rule_symmetry_report(graph: PrismProductGraph, rule: int) -> dict:
    """Audit local-rule invariance under the product-graph automorphisms.

    The tested subgroup consists of independent reflections of each cycle and
    permutations of axes having equal cycle lengths. A local truth table is
    equivariant under such a graph automorphism exactly when its output is
    unchanged after the corresponding reordering of the ten oriented inputs.
    """
    rule = validate_rule(rule)
    axis_permutations = [
        perm for perm in permutations(range(DIMENSION))
        if all(graph.factors[j] == graph.factors[perm[j]] for j in range(DIMENSION))
    ]
    reflections = tuple(cartesian_product((False, True), repeat=DIMENSION))
    invariant = 0
    total = len(axis_permutations) * len(reflections)
    for perm in axis_permutations:
        for flips in reflections:
            preserves = True
            for local_index in range(1 << 11):
                bits = [(local_index >> shift) & 1 for shift in range(10, -1, -1)]
                centre, neighbours = bits[0], bits[1:]
                transformed = []
                for new_axis in range(DIMENSION):
                    old_axis = perm[new_axis]
                    flip = int(flips[new_axis])
                    transformed.extend((
                        neighbours[2 * old_axis + flip],
                        neighbours[2 * old_axis + (1 - flip)],
                    ))
                transformed_index = centre
                for bit in transformed:
                    transformed_index = (transformed_index << 1) | bit
                if ((rule >> local_index) & 1) != ((rule >> transformed_index) & 1):
                    preserves = False
                    break
            if preserves:
                invariant += 1
    return {
        "automorphism_subgroup_order": total,
        "invariant_transformations": invariant,
        "equivariance_fraction": invariant / total,
        "axis_permutation_count": len(axis_permutations),
        "reflection_count": len(reflections),
        "scope": "local rule under axis permutations preserving cycle lengths and independent cycle reflections",
    }

def evolve_rules(
    graph: PrismProductGraph,
    initial_states: Sequence[Sequence[int]],
    steps: int,
    config: EvolutionConfig = EvolutionConfig(),
    fitness: FitnessConfig = FitnessConfig(),
    initial_population: Sequence[int] | None = None,
) -> EvolutionResult:
    """Evolve rule truth tables with a fixed, shared bank of initial fields."""
    config.validate()
    fitness.validate()
    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 0:
        raise ValueError("steps must be a nonnegative integer")
    fixed_states = _validate_states(graph, initial_states)
    rng = random.Random(config.seed)
    population = _initial_rule_population(config, rng, initial_population)
    history = []
    evaluations = 0

    for generation in range(config.generations + 1):
        metrics = [evaluate_rule(graph, fixed_states, genome, steps, fitness) for genome in population]
        evaluations += len(population)
        scores = [item["score"] for item in metrics]
        ranked = sorted(range(len(population)), key=lambda i: (-scores[i], population[i]))
        best_i = ranked[0]
        history.append({
            "generation": generation,
            "best_score": scores[best_i],
            "mean_score": sum(scores) / len(scores),
            "median_score": float(median(scores)),
            "best_mean_density": metrics[best_i]["mean_density"],
            "best_mean_activity": metrics[best_i]["mean_activity"],
            "best_mean_boundary_fraction": metrics[best_i]["mean_boundary_fraction"],
        })
        if generation == config.generations:
            best = population[best_i]
            return EvolutionResult(
                "rule_search", best, scores[best_i], history,
                asdict(config), asdict(fitness), evaluations,
            )
        next_population = [population[i] for i in ranked[:config.elite_count]]
        while len(next_population) < config.population_size:
            parent_a = _tournament(population, scores, config.tournament_size, rng)
            parent_b = _tournament(population, scores, config.tournament_size, rng)
            child = _cross_rule(parent_a, parent_b, rng)
            next_population.append(_mutate_rule(child, config.mutation_rate, rng))
        population = next_population
    raise RuntimeError("unreachable")


def _initial_population(
    graph: PrismProductGraph,
    config: EvolutionConfig,
    rng: random.Random,
    supplied: Sequence[Sequence[int]] | None,
) -> list[bytes]:
    if supplied is not None:
        population = list(_validate_states(graph, supplied))
        if len(population) != config.population_size:
            raise ValueError("initial state population must equal population_size")
        return population
    return [
        bytes(rng.getrandbits(1) for _ in range(graph.vertex_count))
        for _ in range(config.population_size)
    ]


def _cross_state(parent_a: bytes, parent_b: bytes, rng: random.Random) -> bytes:
    return bytes(a if rng.getrandbits(1) else b for a, b in zip(parent_a, parent_b))


def _mutate_state(genome: bytes, rate: float, rng: random.Random) -> bytes:
    if rate <= 0.0:
        return genome
    if rate >= 1.0:
        return bytes(1 - bit for bit in genome)
    return bytes(1 - bit if rng.random() < rate else bit for bit in genome)


def evolve_initial_states(
    graph: PrismProductGraph,
    fixed_rule: int,
    steps: int,
    config: EvolutionConfig = EvolutionConfig(seed_elementary_rules=False),
    fitness: FitnessConfig = FitnessConfig(),
    initial_population: Sequence[Sequence[int]] | None = None,
) -> EvolutionResult:
    """Evolve binary initial fields while holding the CA rule fixed."""
    fixed_rule = validate_rule(fixed_rule)
    config.validate()
    fitness.validate()
    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 0:
        raise ValueError("steps must be a nonnegative integer")
    rng = random.Random(config.seed)
    population = _initial_population(graph, config, rng, initial_population)
    history = []
    evaluations = 0

    for generation in range(config.generations + 1):
        metrics = [_score_trajectory(graph, state, fixed_rule, steps, fitness) for state in population]
        evaluations += len(population)
        scores = [item["score"] for item in metrics]
        ranked = sorted(range(len(population)), key=lambda i: (-scores[i], population[i]))
        best_i = ranked[0]
        history.append({
            "generation": generation,
            "best_score": scores[best_i],
            "mean_score": sum(scores) / len(scores),
            "median_score": float(median(scores)),
            "best_mean_density": metrics[best_i]["mean_density"],
            "best_mean_activity": metrics[best_i]["mean_activity"],
            "best_mean_boundary_fraction": metrics[best_i]["mean_boundary_fraction"],
        })
        if generation == config.generations:
            best = population[best_i]
            return EvolutionResult(
                "initial_state_search", best, scores[best_i], history,
                asdict(config), asdict(fitness), evaluations,
            )
        next_population = [population[i] for i in ranked[:config.elite_count]]
        while len(next_population) < config.population_size:
            parent_a = _tournament(population, scores, config.tournament_size, rng)
            parent_b = _tournament(population, scores, config.tournament_size, rng)
            child = _cross_state(parent_a, parent_b, rng)
            next_population.append(_mutate_state(child, config.mutation_rate, rng))
        population = next_population
    raise RuntimeError("unreachable")


def _coupled_pair_metrics(
    graph: PrismProductGraph,
    initial_a: Sequence[int],
    initial_b: Sequence[int],
    fixed_rule: int,
    steps: int,
    fitness: FitnessConfig,
) -> tuple[dict, dict, float]:
    """Symmetric XOR-coupled fields; both updates use the other field at t.

    A[t+1] = F(A[t]) XOR B[t], B[t+1] = F(B[t]) XOR A[t].
    The interaction observable is the fraction of vertices where A[t] != B[t].
    """
    a, b = bytearray(initial_a), bytearray(initial_b)
    densities_a, activities_a, boundaries_a = [], [], []
    densities_b, activities_b, boundaries_b = [], [], []
    interactions = []
    edge_count = graph.vertex_count * graph.degree // 2
    for _ in range(steps):
        base_a = step(graph, a, fixed_rule)
        base_b = step(graph, b, fixed_rule)
        next_a = bytearray(x ^ y for x, y in zip(base_a, b))
        next_b = bytearray(x ^ y for x, y in zip(base_b, a))
        obs_a = observables(graph, a, next_a)
        obs_b = observables(graph, b, next_b)
        densities_a.append(sum(next_a) / graph.vertex_count)
        activities_a.append(obs_a["temporal_activity"])
        boundaries_a.append(obs_a["graph_dirichlet_energy"] / edge_count)
        densities_b.append(sum(next_b) / graph.vertex_count)
        activities_b.append(obs_b["temporal_activity"])
        boundaries_b.append(obs_b["graph_dirichlet_energy"] / edge_count)
        interactions.append(sum(x != y for x, y in zip(next_a, next_b)) / graph.vertex_count)
        a, b = next_a, next_b

    def score(densities, activities, boundaries):
        if not densities:
            densities = [sum(a) / graph.vertex_count]
            activities, boundaries = [0.0], [0.0]
        rho = sum(densities) / len(densities)
        activity = sum(activities) / len(activities)
        boundary = sum(boundaries) / len(boundaries)
        value = (
            fitness.activity_weight * activity
            - fitness.density_weight * abs(rho - fitness.target_density)
            - fitness.boundary_weight * boundary
        )
        return {
            "score": value,
            "mean_density": rho,
            "mean_activity": activity,
            "mean_boundary_fraction": boundary,
        }

    interaction = sum(interactions) / len(interactions) if interactions else (
        sum(x != y for x, y in zip(a, b)) / graph.vertex_count
    )
    return score(densities_a, activities_a, boundaries_a), score(densities_b, activities_b, boundaries_b), interaction


def evolve_coupled_initial_states(
    graph: PrismProductGraph,
    fixed_rule: int,
    steps: int,
    config_a: EvolutionConfig = EvolutionConfig(seed=2026, seed_elementary_rules=False),
    config_b: EvolutionConfig = EvolutionConfig(seed=2027, seed_elementary_rules=False),
    fitness: FitnessConfig = FitnessConfig(),
    interaction_weight: float = 0.25,
    initial_population_a: Sequence[Sequence[int]] | None = None,
    initial_population_b: Sequence[Sequence[int]] | None = None,
) -> dict:
    """Co-evolve two independent populations under symmetric pointwise XOR coupling.

    Every candidate is evaluated against every member of the opposing
    population (mean opponent score), avoiding a single arbitrary pairing.
    The fixed local CA rule is shared; each population has its own GA seed.
    """
    fixed_rule = validate_rule(fixed_rule)
    config_a.validate()
    config_b.validate()
    fitness.validate()
    if config_a.population_size != config_b.population_size:
        raise ValueError("the two populations must have equal sizes for symmetric evaluation")
    if config_a.generations != config_b.generations:
        raise ValueError("the two populations must use the same generation count")
    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 0:
        raise ValueError("steps must be a nonnegative integer")
    if isinstance(interaction_weight, bool) or not isinstance(interaction_weight, (int, float)) or not isfinite(float(interaction_weight)) or interaction_weight < 0:
        raise ValueError("interaction_weight must be finite and nonnegative")

    rng_a, rng_b = random.Random(config_a.seed), random.Random(config_b.seed)
    pop_a = _initial_population(graph, config_a, rng_a, initial_population_a)
    pop_b = _initial_population(graph, config_b, rng_b, initial_population_b)
    history = []
    evaluations = 0

    for generation in range(config_a.generations + 1):
        matrix_a = [[None] * len(pop_b) for _ in pop_a]
        matrix_b = [[None] * len(pop_b) for _ in pop_a]
        interaction_matrix = [[0.0] * len(pop_b) for _ in pop_a]
        for i, genome_a in enumerate(pop_a):
            for j, genome_b in enumerate(pop_b):
                ma, mb, interaction = _coupled_pair_metrics(
                    graph, genome_a, genome_b, fixed_rule, steps, fitness
                )
                matrix_a[i][j], matrix_b[i][j] = ma, mb
                interaction_matrix[i][j] = interaction
                evaluations += 1

        scores_a = [
            sum(matrix_a[i][j]["score"] + interaction_weight * interaction_matrix[i][j]
                for j in range(len(pop_b))) / len(pop_b)
            for i in range(len(pop_a))
        ]
        scores_b = [
            sum(matrix_b[i][j]["score"] + interaction_weight * interaction_matrix[i][j]
                for i in range(len(pop_a))) / len(pop_a)
            for j in range(len(pop_a))
        ]
        ranked_a = sorted(range(len(pop_a)), key=lambda i: (-scores_a[i], pop_a[i]))
        ranked_b = sorted(range(len(pop_b)), key=lambda j: (-scores_b[j], pop_b[j]))
        best_a, best_b = ranked_a[0], ranked_b[0]
        history.append({
            "generation": generation,
            "population_a_best": scores_a[best_a],
            "population_a_mean": sum(scores_a) / len(scores_a),
            "population_b_best": scores_b[best_b],
            "population_b_mean": sum(scores_b) / len(scores_b),
            "best_pair_interaction_fraction": interaction_matrix[best_a][best_b],
            "mean_pair_interaction_fraction": sum(map(sum, interaction_matrix)) / (len(pop_a) * len(pop_b)),
            "population_a_best_metrics": matrix_a[best_a][best_b],
            "population_b_best_metrics": matrix_b[best_a][best_b],
        })
        if generation == config_a.generations:
            return {
                "mode": "two_population_xor_coevolution",
                "fixed_rule": fixed_rule,
                "best_genome_a": list(pop_a[best_a]),
                "best_genome_b": list(pop_b[best_b]),
                "best_score_a": scores_a[best_a],
                "best_score_b": scores_b[best_b],
                "history": history,
                "config_a": asdict(config_a),
                "config_b": asdict(config_b),
                "fitness_config": asdict(fitness),
                "interaction": {
                    "map": "A[t+1] = F(A[t]) XOR B[t]; B[t+1] = F(B[t]) XOR A[t]",
                    "weight": float(interaction_weight),
                    "evaluation": "each candidate averaged against every opponent in the other population",
                },
                "evaluations": evaluations,
            }

        def next_generation(population, scores, ranked, config, rng):
            children = [population[i] for i in ranked[:config.elite_count]]
            while len(children) < config.population_size:
                pa = _tournament(population, scores, config.tournament_size, rng)
                pb = _tournament(population, scores, config.tournament_size, rng)
                child = _cross_state(pa, pb, rng)
                children.append(_mutate_state(child, config.mutation_rate, rng))
            return children

        pop_a = next_generation(pop_a, scores_a, ranked_a, config_a, rng_a)
        pop_b = next_generation(pop_b, scores_b, ranked_b, config_b, rng_b)
    raise RuntimeError("unreachable")
