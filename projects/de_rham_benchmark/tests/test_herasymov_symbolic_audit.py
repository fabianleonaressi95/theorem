"""Regression tests for the source-faithful Herasymov symbolic audit."""
import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "audits" / "audit_herasymov_symbolic.py"
SPEC = importlib.util.spec_from_file_location("audit_herasymov_symbolic", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def test_complete_finite_audit():
    report = MODULE.self_test()
    assert report["self_test"] == "PASS"


def test_in_shuffle_is_modular_permutation():
    for n in range(1, 50):
        image = [MODULE.in_shuffle_forward(i, n) for i in range(2 * n)]
        assert sorted(image) == list(range(2 * n))
        assert MODULE.shuffle_period(n) == MODULE.multiplicative_order_two(2 * n + 1)


def test_graph_metric_identity():
    m = MODULE.surface_graph(0.2, 0.4, a=1.2, b=0.3, c=1.1, d=1.01, c4=0.8)
    assert abs(m["det_g"] - (1 + m["zx"] ** 2 + m["zy"] ** 2)) < 1e-12
    assert m["det_g"] > 0


def test_noninteger_power_rejects_negative_quadratic_domain():
    try:
        MODULE.surface_graph(0.0, 2.0, a=1.0, b=0.0, c=-1.0, d=1.01)
    except ValueError:
        pass
    else:
        raise AssertionError("negative q with noninteger exponent must be rejected")


def test_all_boolean_3d_reflections_are_bijections():
    report = MODULE.audit_voxel_reflections(3)
    assert report["all_coordinate_maps_bijective"]
    assert len(report["modes"]) == 16


def test_boolean_generator_uses_parity_sublattices_not_octants():
    # The source chooses drawar[dz][dy][dx] from output-index parity.
    rules = [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]
    for dz in range(2):
        for dy in range(2):
            for dx in range(2):
                coord, complement = MODULE.parity_lattice_source_index(
                    rules, dx, dy, dz, 3
                )
                assert coord == (0, 0, 0)
                assert complement is False


def test_uniform_rules_give_single_valued_parent_cell_sampling():
    report = MODULE.audit_parity_lattice_refinement(size=3)
    assert report["interpretation"] == "eight parity sublattices, not eight contiguous octants"
    assert report["single_parent_source_coordinate_per_parent"]
    assert report["max_source_index_edge_l1_jump"] <= 1


def test_mixed_reflection_rules_interleave_parent_samples():
    rules = [[[0, 5], [3, 6]], [[1, 4], [2, 7]]]
    report = MODULE.audit_parity_lattice_refinement(rules, size=3)
    assert not report["all_eight_children_share_one_source_coordinate"]
    assert not report["single_parent_source_coordinate_per_parent"]

def test_rotation_generator_all_256_modes_are_cube_bijections():
    report = MODULE.audit_rotation_generator(size=3)
    assert report["modes_exhausted"] == 256
    assert report["all_coordinate_maps_bijective"]
    assert report["distinct_coordinate_maps"] == 32
    assert report["orientation_counts_over_modes"] == {"+1": 128, "-1": 128}


def test_rotation_generator_scalar_increment_is_not_boolean_complement():
    report = MODULE.audit_rotation_generator(size=3)
    assert report["scalar_action_counts"] == {"increment": 128, "unchanged": 128}
    assert report["no_boolean_complement"] is True


def test_rotation_generator_parity_rules_must_agree_on_parent_samples():
    uniform = [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]
    mixed = [[[0, 16], [64, 80]], [[32, 48], [96, 112]]]
    assert MODULE.audit_rotation_parity_lattice(uniform, size=3)["single_parent_sample_rule"]
    assert not MODULE.audit_rotation_parity_lattice(mixed, size=3)["single_parent_sample_rule"]


def test_rotation_mode_bit_three_changes_scalar_action_not_coordinates():
    report = MODULE.audit_rotation_generator(size=3)
    assert report["bit3_preserves_coordinates"]
    assert report["bit3_toggles_increment_rule"]
