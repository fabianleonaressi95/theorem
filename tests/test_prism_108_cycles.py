from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from audit_prism_108_cycles import audit, construct_cycles, index


def test_constructive_108_cycle_cover():
    report = audit()
    assert report["vertices"] == 69120
    assert report["cycles"] == 108
    assert report["cycle_length"] == 640
    assert report["all_cycle_edges_valid"] is True
    assert report["each_cycle_simple"] is True
    assert report["cycles_pairwise_vertex_disjoint"] is True
    assert report["full_vertex_cover"] is True
    assert report["unique_vertices_covered"] == 69120


def test_index_is_bijective_on_coordinate_grid():
    values = {
        index(g, l, c, t, b)
        for g in range(64)
        for l in range(6)
        for c in range(6)
        for t in range(6)
        for b in range(5)
    }
    assert values == set(range(69120))


def test_each_constructed_cycle_has_640_distinct_vertices():
    cycles = construct_cycles()
    assert len(cycles) == 108
    assert all(len(cycle) == 640 and len(set(cycle)) == 640
               for cycle in cycles)
