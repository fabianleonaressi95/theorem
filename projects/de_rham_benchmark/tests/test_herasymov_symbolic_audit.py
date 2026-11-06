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
