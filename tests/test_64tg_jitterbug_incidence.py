"""Regression test for the FCC/Jitterbug incidence distinction."""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "audit_64tg_jitterbug_incidence",
    ROOT / "audits" / "audit_64tg_jitterbug_incidence.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_cuboctahedral_points_are_not_a_fcc_edge_subgraph():
    report = MODULE.audit()
    assert report["cuboctahedral_point_set"] == 12
    assert report["jitterbug_rods"] == 24
    assert report["jitterbug_rod_degree"] == [4]
    assert report["fcc_edge_squared_distance_n"] == [2]
    assert report["jitterbug_rod_squared_distance_n"] == [8]
    assert report["rod_edges_shared_with_fcc_graph"] == 0
