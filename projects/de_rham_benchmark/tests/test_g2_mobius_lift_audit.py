"""Regression tests for the standalone G2/Mobius algebraic audit."""
import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "audits" / "audit_g2_mobius_lift.py"
SPEC = importlib.util.spec_from_file_location("audit_g2_mobius_lift", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def test_synthetic_rank_completion_and_determinant():
    report = MODULE.self_test()
    assert report["self_test"] == "PASS"


def test_cofactor_vector_annihilates_planar_triple():
    import numpy as np
    R = np.array([[1., 0., 1.], [0., 1., 1.]])
    c = MODULE.cofactor_vector(R)
    assert np.linalg.norm(R @ c) < 1e-12


def test_mobius_boundary_map_is_involution():
    for level in range(1, 9):
        assert MODULE.mobius_seam_audit(level)["involution_ok"]


def test_zero_normal_component_does_not_complete_rank():
    triple = [[1., 0.], [0., 1.], [1., 1.]]
    row = MODULE.audit_one(triple, 1.618033988749895, 0.0, 1e-10)
    assert row["rank_R"] == 2
    assert row["rank_V"] == 2
    assert not row["positive_definite"]
