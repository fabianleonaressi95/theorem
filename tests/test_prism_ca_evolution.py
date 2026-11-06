import pytest

import json

from models.prism_ca_evolution import (
    EvolutionConfig,
    FitnessConfig,
    evolve_initial_states,
    evolve_coupled_initial_states,
    _coupled_pair_metrics,
    evolve_rules,
    random_initial_states,
    rule_symmetry_report,
)
from models.prism_cellular_automata import PrismProductGraph, elementary_rules


def test_rule_search_is_reproducible_and_keeps_a_complete_history():
    graph = PrismProductGraph((3, 3, 3, 3, 3))
    initial = random_initial_states(graph, count=2, seed=91)
    config = EvolutionConfig(
        population_size=6,
        generations=2,
        elite_count=2,
        tournament_size=3,
        mutation_rate=0.002,
        seed=17,
    )
    first = evolve_rules(graph, initial, steps=2, config=config)
    second = evolve_rules(graph, initial, steps=2, config=config)
    assert first.to_dict() == second.to_dict()
    assert first.mode == "rule_search"
    assert isinstance(first.best_genome, int)
    assert 0 <= first.best_genome < (1 << 2048)
    assert len(first.history) == 3
    assert first.evaluations == 6 * 3
    assert first.history[-1]["best_score"] >= first.history[0]["best_score"]


def test_rule_search_accepts_fixed_population_and_zero_generations():
    graph = PrismProductGraph((3, 3, 3, 3, 3))
    initial = [bytes(graph.vertex_count), bytes([1]) * graph.vertex_count]
    population = [elementary_rules()["zero"], elementary_rules()["one"]]
    config = EvolutionConfig(
        population_size=2, generations=0, elite_count=1,
        tournament_size=1, seed_elementary_rules=False,
    )
    result = evolve_rules(graph, initial, steps=1, config=config, initial_population=population)
    assert result.evaluations == 2
    assert result.best_genome in population
    assert len(result.history) == 1


def test_initial_state_search_keeps_rule_fixed_and_is_reproducible():
    graph = PrismProductGraph((3, 3, 3, 3, 3))
    config = EvolutionConfig(
        population_size=5,
        generations=2,
        elite_count=1,
        tournament_size=2,
        mutation_rate=0.01,
        seed=31,
        seed_elementary_rules=False,
    )
    rule = elementary_rules()["zero"]
    first = evolve_initial_states(graph, rule, steps=2, config=config)
    second = evolve_initial_states(graph, rule, steps=2, config=config)
    assert first.to_dict() == second.to_dict()
    assert first.mode == "initial_state_search"
    assert isinstance(first.best_genome, bytes)
    assert len(first.best_genome) == graph.vertex_count
    assert set(first.best_genome) <= {0, 1}
    assert first.evaluations == 5 * 3
    assert len(first.history) == 3


def test_fitness_components_are_reported_separately():
    graph = PrismProductGraph((3, 3, 3, 3, 3))
    initial = random_initial_states(graph, count=1, seed=5)
    result = evolve_rules(
        graph,
        initial,
        steps=2,
        config=EvolutionConfig(
            population_size=2, generations=0, elite_count=1,
            tournament_size=1, seed_elementary_rules=False,
        ),
        fitness=FitnessConfig(
            target_density=0.4,
            activity_weight=1.0,
            density_weight=0.5,
            boundary_weight=0.25,
        ),
        initial_population=[elementary_rules()["zero"], elementary_rules()["one"]],
    )
    row = result.history[0]
    assert "best_mean_density" in row
    assert "best_mean_activity" in row
    assert "best_mean_boundary_fraction" in row


def test_invalid_configurations_and_empty_initial_bank_are_rejected():
    graph = PrismProductGraph((3, 3, 3, 3, 3))
    with pytest.raises(ValueError):
        EvolutionConfig(population_size=1).validate()
    with pytest.raises(ValueError):
        EvolutionConfig(population_size=4, elite_count=4).validate()
    with pytest.raises(ValueError):
        EvolutionConfig(population_size=4, mutation_rate=1.1).validate()
    with pytest.raises(ValueError):
        FitnessConfig(target_density=1.1).validate()
    with pytest.raises(ValueError):
        FitnessConfig(activity_weight=float("nan")).validate()
    with pytest.raises(ValueError):
        EvolutionConfig(population_size=4, mutation_rate=float("nan")).validate()
    with pytest.raises(ValueError):
        evolve_rules(graph, [], steps=1)
    with pytest.raises(ValueError):
        evolve_initial_states(graph, -1, steps=1)


def test_json_friendly_result_serialization():
    graph = PrismProductGraph((3, 3, 3, 3, 3))
    config = EvolutionConfig(
        population_size=2, generations=0, elite_count=1,
        tournament_size=1, seed_elementary_rules=False,
    )
    result = evolve_initial_states(graph, elementary_rules()["zero"], 1, config)
    encoded = json.dumps(result.to_dict())
    assert '"mode": "initial_state_search"' in encoded



def test_product_graph_automorphism_equivariance_audit():
    graph = PrismProductGraph()
    identity = elementary_rules()["identity"]
    report = rule_symmetry_report(graph, identity)
    assert report["automorphism_subgroup_order"] == 192
    assert report["axis_permutation_count"] == 6
    assert report["reflection_count"] == 32
    assert report["invariant_transformations"] == 192
    assert report["equivariance_fraction"] == 1.0


def test_rule_symmetry_audit_detects_oriented_neighbour_dependence():
    graph = PrismProductGraph()
    # A truth table that reads only the first oriented neighbour slot.
    rule = sum(1 << i for i in range(1 << 11) if ((i >> 9) & 1))
    report = rule_symmetry_report(graph, rule)
    assert report["automorphism_subgroup_order"] == 192
    assert report["invariant_transformations"] < 192
    assert 0.0 <= report["equivariance_fraction"] < 1.0



def test_two_population_xor_coevolution_is_reproducible_and_auditable():
    graph = PrismProductGraph((3, 3, 3, 3, 3))
    config_a = EvolutionConfig(
        population_size=3, generations=1, elite_count=1,
        tournament_size=2, mutation_rate=0.01, seed=101,
        seed_elementary_rules=False,
    )
    config_b = EvolutionConfig(
        population_size=3, generations=1, elite_count=1,
        tournament_size=2, mutation_rate=0.01, seed=202,
        seed_elementary_rules=False,
    )
    initial_a = [bytes(graph.vertex_count), bytes([1]) * graph.vertex_count,
                 bytes([i % 2 for i in range(graph.vertex_count)])]
    initial_b = [bytes([1 - (i % 2) for i in range(graph.vertex_count)]),
                 bytes([1]) * graph.vertex_count, bytes(graph.vertex_count)]
    kwargs = dict(
        graph=graph,
        fixed_rule=elementary_rules()["identity"],
        steps=2,
        config_a=config_a,
        config_b=config_b,
        interaction_weight=0.4,
        initial_population_a=initial_a,
        initial_population_b=initial_b,
    )
    first = evolve_coupled_initial_states(**kwargs)
    second = evolve_coupled_initial_states(**kwargs)
    assert first == second
    assert first["mode"] == "two_population_xor_coevolution"
    assert len(first["best_genome_a"]) == graph.vertex_count
    assert len(first["best_genome_b"]) == graph.vertex_count
    assert len(first["history"]) == 2
    assert first["evaluations"] == 3 * 3 * 2
    assert first["interaction"]["map"].startswith("A[t+1] = F(A[t]) XOR B[t]")
    assert 0.0 <= first["history"][-1]["mean_pair_interaction_fraction"] <= 1.0


def test_two_population_coevolution_rejects_incompatible_populations():
    graph = PrismProductGraph((3, 3, 3, 3, 3))
    a = EvolutionConfig(population_size=2, generations=0, elite_count=1,
                        tournament_size=1, seed_elementary_rules=False)
    b = EvolutionConfig(population_size=3, generations=0, elite_count=1,
                        tournament_size=1, seed_elementary_rules=False)
    with pytest.raises(ValueError):
        evolve_coupled_initial_states(graph, 0, 1, a, b)
    with pytest.raises(ValueError):
        evolve_coupled_initial_states(graph, 0, 1, a, a, interaction_weight=-0.1)



def test_xor_coupling_map_exchanges_complementary_fields_under_zero_rule():
    graph = PrismProductGraph((3, 3, 3, 3, 3))
    a = bytes(graph.vertex_count)
    b = bytes([1]) * graph.vertex_count
    metrics_a, metrics_b, interaction = _coupled_pair_metrics(
        graph, a, b, fixed_rule=elementary_rules()["zero"], steps=1,
        fitness=FitnessConfig(),
    )
    # With F=0, A'=B and B'=A: the two fields remain complementary.
    assert interaction == 1.0
    assert metrics_a["mean_density"] == 1.0
    assert metrics_b["mean_density"] == 0.0
