import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from classify_c60_sw_orbits import classify


def test_c60_sw_isomorphism_and_ih_orbit_partition():
    result = classify()
    assert result["admissible_labelled_moves"] == 30
    assert result["automorphism_group_order"] == 120
    assert sum(result["isomorphism_class_sizes"]) == 30
    assert sum(result["Ih_orbit_sizes"]) == 30
    assert len(result["isomorphism_classes_move_indices_zero_based"]) == len(result["isomorphism_class_sizes"])
    assert len(result["Ih_orbits_move_indices_zero_based"]) == len(result["Ih_orbit_sizes"])
    assert sorted(i for orbit in result["Ih_orbits_move_indices_zero_based"] for i in orbit) == list(range(30))
