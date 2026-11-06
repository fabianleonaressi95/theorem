import pytest

from models.prism_cellular_automata import (
    BASE_FACTORS,
    LOCAL_INPUTS,
    RULE_BITS,
    PrismProductGraph,
    elementary_rules,
    local_input_index,
    observables,
    step,
    trajectory,
    validate_rule,
)


def small_graph():
    return PrismProductGraph((3, 3, 3, 3, 3))


def test_prism_graph_has_ten_oriented_neighbours_and_expected_counts():
    graph = PrismProductGraph()
    assert graph.factors == BASE_FACTORS
    assert graph.vertex_count == 69120
    assert graph.degree == 10
    assert sum(1 for _ in graph.positive_edges()) == 5 * graph.vertex_count


def test_small_graph_neighbourhood_order_and_periodic_wrap():
    graph = small_graph()
    neighbours = graph.neighbours((0, 0, 0, 0, 0))
    assert neighbours == (
        (2, 0, 0, 0, 0), (1, 0, 0, 0, 0),
        (0, 2, 0, 0, 0), (0, 1, 0, 0, 0),
        (0, 0, 2, 0, 0), (0, 0, 1, 0, 0),
        (0, 0, 0, 2, 0), (0, 0, 0, 1, 0),
        (0, 0, 0, 0, 2), (0, 0, 0, 0, 1),
    )


def test_local_input_index_uses_centre_then_ordered_neighbour_bits():
    assert local_input_index(1, [0] * 10) == 1 << 10
    assert local_input_index(0, [1] + [0] * 9) == 1 << 9
    assert LOCAL_INPUTS == 11
    assert RULE_BITS == 2048


def test_constant_zero_and_one_rules():
    graph = small_graph()
    state = bytearray((i % 2 for i in range(graph.vertex_count)))
    rules = elementary_rules()
    assert step(graph, state, rules["zero"]) == bytearray(graph.vertex_count)
    assert step(graph, state, rules["one"]) == bytearray([1]) * graph.vertex_count


def test_identity_and_negation_controls():
    graph = small_graph()
    state = bytearray((i % 2 for i in range(graph.vertex_count)))
    rules = elementary_rules()
    assert step(graph, state, rules["identity"]) == state
    assert step(graph, state, rules["negation"]) == bytearray(1 - bit for bit in state)


def test_trajectory_and_observables_are_deterministic():
    graph = small_graph()
    state = bytearray([0] * graph.vertex_count)
    states = trajectory(graph, state, elementary_rules()["one"], 2)
    assert len(states) == 3
    assert states[0] == state
    assert states[1] == bytearray([1]) * graph.vertex_count
    assert states[2] == states[1]
    obs = observables(graph, states[0], states[1])
    assert obs["density"] == 0.0
    assert obs["graph_dirichlet_energy"] == 0
    assert obs["temporal_activity"] == 1.0


@pytest.mark.parametrize("factors", [
    (3, 3, 3, 3), (2, 3, 3, 3, 3), (3, 3, 3, 3, True),
])
def test_invalid_factor_lists_rejected(factors):
    with pytest.raises(ValueError):
        PrismProductGraph(factors)


@pytest.mark.parametrize("rule", [-1, 1 << 2048, True, 1.5])
def test_invalid_rule_encoding_rejected(rule):
    with pytest.raises(ValueError):
        validate_rule(rule)


def test_invalid_state_and_wrong_length_rejected():
    graph = small_graph()
    with pytest.raises(ValueError):
        step(graph, bytearray(graph.vertex_count - 1), elementary_rules()["zero"])
    bad = bytearray(graph.vertex_count)
    bad[0] = 2
    with pytest.raises(ValueError):
        step(graph, bad, elementary_rules()["zero"])
    with pytest.raises(ValueError):
        step(graph, [0.0] * graph.vertex_count, elementary_rules()["zero"])


def test_graph_vertex_encoding_roundtrip():
    graph = small_graph()
    for point in ((0, 0, 0, 0, 0), (2, 2, 2, 2, 2), (1, 2, 0, 1, 2)):
        assert graph.decode(graph.encode(point)) == point
