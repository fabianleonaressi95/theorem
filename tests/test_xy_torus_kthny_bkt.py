import numpy as np

from scripts.audit_xy_torus_kthny_bkt import (
    dual_vortex_divergence, helicity_modulus, metropolis_sweep,
    radial_charge_correlator, run, vortex_field, winding_numbers,
)


def test_2d_torus_vorticity_is_integer_and_globally_neutral():
    rng = np.random.default_rng(201)
    theta = rng.uniform(-np.pi, np.pi, size=(6, 6))
    q = vortex_field(theta)
    assert q.shape == (6, 6)
    assert np.issubdtype(q.dtype, np.integer)
    assert int(q.sum()) == 0


def test_3d_vortex_flux_is_closed_on_dual_lattice():
    rng = np.random.default_rng(202)
    theta = rng.uniform(-np.pi, np.pi, size=(4, 4, 4))
    q = vortex_field(theta)
    assert q.shape == (3, 4, 4, 4)
    assert np.array_equal(dual_vortex_divergence(q), np.zeros((4, 4, 4), dtype=int))
    assert all(int(component.sum()) == 0 for component in q)


def test_winding_numbers_are_integer_and_have_expected_shape():
    rng = np.random.default_rng(203)
    for dim in (2, 3):
        theta = rng.uniform(-np.pi, np.pi, size=(4,) * dim)
        winding = winding_numbers(theta)
        assert winding.shape == (dim,) + (4,) * (dim - 1)
        assert np.issubdtype(winding.dtype, np.integer)


def test_metropolis_and_helicity_work_in_both_dimensions():
    rng = np.random.default_rng(204)
    for dim in (2, 3):
        theta = rng.uniform(-np.pi, np.pi, size=(4,) * dim)
        metropolis_sweep(theta, beta=1.1, rng=rng)
        assert np.isfinite(theta).all()
        assert helicity_modulus(theta, beta=1.1).shape == (dim,)


def test_correlator_and_small_runs_return_finite_values():
    rng = np.random.default_rng(205)
    for dim in (2, 3):
        theta = rng.uniform(-np.pi, np.pi, size=(4,) * dim)
        corr = radial_charge_correlator(vortex_field(theta))
        assert len(corr["r"]) == 3
        assert np.isfinite(corr["Cq"]).all()
        result = run(L=4, dim=dim, beta=1.0, thermalization=2,
                     measurements=3, seed=dim)
        assert result["dimension"] == dim
        assert np.isfinite(result["beta_helicity_mean_by_axis"]).all()
        if dim == 3:
            assert max(result["max_abs_dual_vortex_divergence"]) == 0
