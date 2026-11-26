import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from classify_c60_sw_orbits import classify


def test_c60_sw_isomorphism_and_ih_dual_edge_orbit_partition():
    result = classify()
    assert result["admissible_labelled_SW_5_6_moves"] == 30
    assert result["dual_graph_automorphism_group_order"] == 120
    assert result["unlabelled_postgraph_isomorphism_classes"] == 1
    assert result["isomorphism_class_sizes"] == [30]
    assert result["Ih_dual_edge_orbit_count"] == 1
    assert result["Ih_dual_edge_orbit_sizes"] == [30]
    assert sorted(i for orbit in result["Ih_dual_edge_orbits_move_indices_zero_based"] for i in orbit) == list(range(30))
