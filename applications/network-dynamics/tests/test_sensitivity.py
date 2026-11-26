from sensitivity import run_sensitivity


def test_sensitivity_grid_is_complete_and_reproducible():
    first = run_sensitivity(replicates=2, seed=17, steps=3, removal_repetitions=2)
    second = run_sensitivity(replicates=2, seed=17, steps=3, removal_repetitions=2)
    assert first == second
    assert len(first) == 3 * 3 * 3 * 2 * 2 * 3 * 4 * 2
    assert {row["removal_mode"] for row in first} == {"random", "highest_degree"}
    assert {"hierarchical", "matrix", "practices_like"} <= {row["architecture"] for row in first}
    assert "hierarchical_minus_matrix" in {row["architecture"] for row in first}
    assert all(row["replicates"] == 2 for row in first)
    assert all(row["ci95_normal_lower"] <= row["ci95_normal_upper"] for row in first)
