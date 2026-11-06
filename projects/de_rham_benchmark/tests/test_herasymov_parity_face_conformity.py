"""Exact shared-face compatibility tests for Herasymov parity-selected maps."""
import importlib.util
import sys
from pathlib import Path

AUDITS = Path(__file__).parents[1] / "audits"
sys.path.insert(0, str(AUDITS))
SCRIPT = AUDITS / "audit_herasymov_parity_face_conformity.py"
SPEC = importlib.util.spec_from_file_location("audit_herasymov_parity_face_conformity", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def test_uniform_coordinate_rule_is_face_conforming():
    rules = [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]
    report = MODULE.parity_face_audit(rules, size=2)
    assert report["interfaces_checked"] == 12
    assert report["all_shared_face_traces_match"]
    assert report["all_eight_affine_cube_maps_identical"]
    assert report["necessary_sufficient_criterion_holds"]


def test_bit_three_changes_scalar_rule_but_not_geometric_face_traces():
    rules = [[[0, 8], [8, 0]], [[8, 0], [0, 8]]]
    report = MODULE.parity_face_audit(rules, size=2)
    assert report["all_shared_face_traces_match"]
    assert report["all_eight_affine_cube_maps_identical"]
    assert not report["scalar_increment_rule_is_uniform"]


def test_mixed_reflection_rules_fail_shared_face_conformity():
    rules = [[[0, 1], [0, 1]], [[0, 1], [0, 1]]]
    report = MODULE.parity_face_audit(rules, size=2)
    assert not report["all_shared_face_traces_match"]
    assert not report["all_eight_affine_cube_maps_identical"]


def test_pairwise_face_criterion_exhausts_all_source_coordinate_maps():
    report = MODULE.audit_pairwise_criterion(size=2)
    assert report["source_modes_exhausted"] == 256
    assert report["distinct_affine_cube_maps"] == 32
    assert report["pair_axis_checks"] == 32 * 32 * 3
    assert report["mode_equivalence_class_sizes"] == [4] * 24 + [20] * 8
    assert sorted(len(item["source_modes"]) for item in report["mode_equivalence_classes"]) == [4] * 24 + [20] * 8
    assert report["face_compatibility_iff_same_affine_map"]


def test_self_test_keeps_geometry_and_scalar_action_separate():
    report = MODULE.self_test()
    assert report["self_test_passed"]
