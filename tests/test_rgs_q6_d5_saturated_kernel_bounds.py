import math
import numpy as np
import sympy as sp

from src.rgs_q6_d5_saturated_kernel_bounds import (
    build_q6_d5_saturated_integer_kernel,
    q6_d5_certified_fiber_tail_bound,
    audit_q6_d5_saturated_kernel_and_tail,
    q6_d5_unimodular_lattice_splitting,
    q6_d5_split_integer_cycle_coordinates,
)


def test_smith_hnf_returns_saturated_integer_kernel():
    result = build_q6_d5_saturated_integer_kernel()
    basis = result["kernel_basis"]
    integer_map = result["integer_map"]
    assert basis.shape == (124, 129)
    assert basis.rank() == 124
    assert basis * integer_map.T == sp.zeros(124, 5)
    assert all(result["exact_checks"].values())
    # Saturation is certified by the unimodular Smith right transform:
    # the last 124 columns form the full integral kernel, not a sublattice.
    assert result["smith_right_transform"].det() in (sp.Integer(1), sp.Integer(-1))


def test_certified_factorial_tail_bound_is_finite_and_decreases():
    coarse = q6_d5_certified_fiber_tail_bound(2.0, 500)
    tighter = q6_d5_certified_fiber_tail_bound(2.0, 600)
    assert math.isfinite(coarse["log_upper_bound"])
    assert math.isfinite(tighter["log_upper_bound"])
    assert tighter["log_upper_bound"] < coarse["log_upper_bound"]
    assert tighter["bound_method"].startswith("all_Z^192")


def test_tail_bound_handles_invalid_inputs():
    import pytest
    with pytest.raises(ValueError):
        q6_d5_certified_fiber_tail_bound(0.0, 100)
    with pytest.raises(ValueError):
        q6_d5_certified_fiber_tail_bound(1.0, -1)


def test_combined_audit_reports_proved_scope():
    report = audit_q6_d5_saturated_kernel_and_tail(beta_time=2.0, edge_l1_cutoff=100)
    assert report["all_checks_passed"], report["checks"]
    assert report["kernel"]["saturated"]
    assert report["kernel"]["rank"] == 124



def test_explicit_unimodular_quotient_fiber_splitting():
    split = q6_d5_unimodular_lattice_splitting()
    assert split["determinant"] in (sp.Integer(1), sp.Integer(-1))
    assert all(split["checks"].values())
    assert split["quotient_complement_columns"].shape == (129, 5)
    assert split["saturated_kernel_columns"].shape == (129, 124)

    # A deterministic nontrivial integer vector is reconstructed exactly.
    z = sp.Matrix([(-1) ** i * (i % 7) for i in range(129)])
    coordinates = q6_d5_split_integer_cycle_coordinates(z, split)
    assert coordinates["reconstruction_exact"]
    assert coordinates["all_coordinates"].shape == (129, 1)
    assert coordinates["quotient_coordinates"].shape == (5, 1)
    assert coordinates["fiber_coordinates"].shape == (124, 1)


def test_kernel_translation_changes_only_fiber_coordinates():
    split = q6_d5_unimodular_lattice_splitting()
    k = split["saturated_kernel_columns"][:, 0]
    z = sp.Matrix([i % 5 for i in range(129)])
    before = q6_d5_split_integer_cycle_coordinates(z, split)
    after = q6_d5_split_integer_cycle_coordinates(z + k, split)
    assert after["quotient_coordinates"] == before["quotient_coordinates"]
    assert after["fiber_coordinates"] - before["fiber_coordinates"] == sp.eye(124)[:, 0]
