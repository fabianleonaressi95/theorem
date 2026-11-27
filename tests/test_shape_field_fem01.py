"""FEM-01 verification tests — Shape-Field electrostatic benchmarks.

Protocol: docs/SHAPE_FIELD_CADFEM_ELECTROSTATIC_PROTOCOL_2026-11-26.md §8.
Backend: models/shape_field (NumPy/SciPy P1 elements, 1-D problems only).

Tolerances are the achieved/target values documented in
docs/SHAPE_FIELD_FEM01_BENCHMARK_2026-11-27.md — not aspirational claims.
"""
import numpy as np
import pytest

from models.shape_field.benchmarks import (
    solve_plate,
    solve_sphere_l1,
    sphere_convergence,
)


# ---------------- parallel plate ----------------

def test_plate_field_uniform_and_exact():
    r = solve_plate(gap=1.0, voltage=1.0, n_elem=8)
    assert r["E_rel_err"] < 1e-12          # P1 is exact for the linear solution
    assert abs(r["E_num"]) == pytest.approx(1.0)
    assert r["beta"] == pytest.approx(1.0)
    assert r["max_abs_phi_err"] < 1e-14


def test_plate_energy_consistency():
    r = solve_plate(gap=2.0, voltage=3.0, n_elem=4)
    assert r["energy_num"] == pytest.approx(r["energy_exact_per_area"], rel=1e-12)
    # scaling check: E = V/d on a non-unit gap
    assert abs(r["E_num"]) == pytest.approx(1.5)


# ---------------- sphere, exact outer BC (discretisation error only) ----

def test_sphere_exact_bc_beta_converges_to_3():
    conv = sphere_convergence(
        n_elems=(100, 200, 400, 800), outer_bc="exact", grading=6.0
    )
    errs = [c["beta_err"] for c in conv]
    assert errs == sorted(errs, reverse=True) or errs[-1] < errs[0]
    assert conv[-1]["beta_err"] < 1e-3          # achieved: ~1.3e-4
    assert conv[-1]["beta_recovered"] == pytest.approx(3.0, abs=1e-3)


def test_sphere_exact_bc_potential_converges():
    conv = sphere_convergence(
        n_elems=(100, 200, 400, 800), outer_bc="exact", grading=6.0
    )
    uerrs = [c["max_abs_u_err"] for c in conv]
    assert uerrs[-1] < uerrs[0]
    assert uerrs[-1] < 1e-5                     # achieved: ~5e-8 at n=800,g=6


def test_sphere_raw_gradient_is_first_order_beta():
    # Documented behaviour: the raw P1 boundary gradient converges only
    # ~O(h); the recovered derivative is the reported beta. This test pins
    # the distinction so nobody silently upgrades the raw value.
    r = solve_sphere_l1(n_elem=400, outer_bc="exact", grading=6.0)
    assert r["beta_raw_err"] > r["beta_err"]
    assert r["beta_raw"] == pytest.approx(3.0, abs=0.2)


# ---------------- sphere, far-field BC (domain truncation) -------------

def test_sphere_far_field_truncation_documented():
    r = solve_sphere_l1(a=1.0, r_far=20.0, n_elem=400,
                        outer_bc="far_field", grading=6.0)
    # phi = -E0 z is imposed at r_far instead of the exact multipole tail:
    # expected BC gap = E0 * a^3 / r_far^2 = 2.5e-3 for a=1, R=20.
    assert r["truncation_bc_gap"] == pytest.approx(2.5e-3, rel=1e-12)
    # potential error is dominated by this truncation, not the mesh:
    assert r["max_abs_u_err"] > 1e-3


def test_sphere_domain_independence():
    base = solve_sphere_l1(a=1.0, r_far=20.0, n_elem=400,
                           outer_bc="far_field", grading=6.0)
    wide = solve_sphere_l1(a=1.0, r_far=40.0, n_elem=800,
                           outer_bc="far_field", grading=6.0)
    # doubling the domain must move beta by < 1% (protocol §8.5)
    assert abs(wide["beta_recovered"] - base["beta_recovered"]) / 3.0 < 0.01
    # and the BC gap shrinks by ~8x (a^3/R^2 scaling)
    assert wide["truncation_bc_gap"] < base["truncation_bc_gap"] / 4.0


def test_sphere_beta_reference_is_E0_not_gap_average():
    # beta is defined against the incident uniform field E0 (protocol fix),
    # not V/d — there is no gap voltage in this benchmark.
    r = solve_sphere_l1(a=1.0, r_far=20.0, n_elem=800,
                        outer_bc="exact", grading=6.0)
    assert r["e0"] == 1.0
    assert r["beta_exact"] == pytest.approx(3.0)
