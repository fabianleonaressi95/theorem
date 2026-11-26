from topology_control import degree_preserving_rewire, run_topology_control
import numpy as np


def test_degree_preserving_rewire_keeps_degree_sequence_and_edge_count():
    edges = {(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (0, 3), (1, 4)}
    rewired = degree_preserving_rewire(edges, 6, np.random.default_rng(4), swaps_per_edge=8)
    degree = lambda es: np.bincount(np.array(list(es)).reshape(-1), minlength=6)
    assert len(rewired) == len(edges)
    assert np.array_equal(degree(edges), degree(rewired))


def test_topology_control_reproducible_and_has_all_controls():
    a = run_topology_control(replicates=2, seed=13, steps=3,
                             swaps_per_edge=2, removal_repetitions=2)
    b = run_topology_control(replicates=2, seed=13, steps=3,
                             swaps_per_edge=2, removal_repetitions=2)
    assert a == b
    controls = {row["control"] for row in a if "_minus_" not in row["control"]}
    assert controls == {
        "profile_blind_random",
        "hierarchical_original_profile_informed",
        "matrix_original_profile_informed",
        "practices_like_original_profile_informed",
        "hierarchical_degree_preserving_rewire",
        "matrix_degree_preserving_rewire",
        "practices_like_degree_preserving_rewire",
    }
    assert all(row["replicates"] == 2 for row in a)
    assert all(row["ci95_normal_lower"] <= row["ci95_normal_upper"] for row in a)
    assert all(row["degree_sequence_preserved"] for row in a
               if "_minus_" not in row["control"] and row["control"].endswith("_degree_preserving_rewire"))
