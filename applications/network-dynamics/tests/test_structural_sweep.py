"""Tests for structural diagnostics and the rewiring-intensity sweep."""
import json
import numpy as np

from structural_sweep import structural_metrics, run_structural_sweep


def test_structural_metrics_are_finite_and_consistent():
    profiles = np.array([[1, 0], [1, 1], [0, 1], [1, 0]], dtype=float)
    edges = {(0, 1), (1, 2), (2, 3), (3, 0)}
    metrics = structural_metrics(edges, profiles)
    assert metrics["nodes"] == 4
    assert metrics["edges"] == 4
    assert metrics["components"] == 1
    assert metrics["largest_component_fraction"] == 1.0
    assert 0.0 <= metrics["mean_local_clustering"] <= 1.0
    assert -1.0 <= metrics["greedy_modularity"] <= 1.0
    assert 0.0 <= metrics["mean_edge_competence_jaccard"] <= 1.0
    assert metrics["largest_component_average_path"] > 0


def test_sweep_reproducible_and_degree_preserving_at_every_intensity():
    a = run_structural_sweep(replicates=2, seed=29, intensities=(0, 1, 3))
    b = run_structural_sweep(replicates=2, seed=29, intensities=(0, 1, 3))
    assert json.dumps(a, sort_keys=True, allow_nan=True) == json.dumps(b, sort_keys=True, allow_nan=True)
    assert len(a) == 3 * 3 * 7
    assert all(row["degree_sequence_preserved"] for row in a)
    assert all(row["replicates"] == 2 for row in a)
    assert all(row["mean_accepted_swap_fraction"] == 1.0 for row in a if row["swaps_per_edge"] == 0)
