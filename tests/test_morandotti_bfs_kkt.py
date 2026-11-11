import numpy as np

from models.morandotti_bfs_kkt import (
    assemble_bfs_rectangular,
    plane_stress_compliance,
    solve_bfs_kkt,
)


def test_plane_stress_compliance_has_elastic_symmetries_and_positive_modes():
    S = plane_stress_compliance(young_modulus=210.0, poisson_ratio=0.3)
    assert np.allclose(S, S.swapaxes(0, 1))
    assert np.allclose(S, S.swapaxes(2, 3))
    assert np.allclose(S, S.transpose(2, 3, 0, 1))
    assert np.isclose((1.0 - 0.3) / 210.0, 0.7 / 210.0)
    assert np.isclose((1.0 + 0.3) / 210.0, 1.3 / 210.0)


def test_bfs_assembly_is_h2_conforming_dimensionally_and_full_row_rank():
    out = assemble_bfs_rectangular(nx=2, ny=2, quadrature_order=3)
    A, M = out["A"], out["M"]
    assert A.shape == (4, 12)
    assert M.shape == (12, 12)
    assert out["test_hessians"].shape == (4, 4, 9, 2, 2)
    assert out["strain_basis"].shape == (4, 9, 12, 2, 2)
    assert np.linalg.matrix_rank(A) == A.shape[0]
    assert np.allclose(M, M.T, atol=1e-13)
    assert np.linalg.eigvalsh(M).min() > 0.0
    assert np.all(out["weights"] > 0.0)


def test_bfs_kkt_solves_a_feasible_discrete_source():
    assembled = assemble_bfs_rectangular(nx=2, ny=2, quadrature_order=3)
    coefficients = np.linspace(-0.4, 0.7, assembled["M"].shape[0])
    source = assembled["A"] @ coefficients
    out = solve_bfs_kkt(source, nx=2, ny=2, quadrature_order=3)
    assert out["constraint_residual"] < 1e-10
    assert out["stationarity_residual"] < 1e-10
    assert np.isclose(out["primal_energy"], out["dual_energy"], atol=1e-10)
    assert out["constraint_rank"] == 4


def test_bfs_rejects_invalid_mesh_and_elastic_parameters():
    try:
        assemble_bfs_rectangular(nx=1, ny=2)
    except ValueError as exc:
        assert "nx, ny" in str(exc)
    else:
        raise AssertionError("one-cell direction must be rejected")
    try:
        plane_stress_compliance(1.0, 1.0)
    except ValueError as exc:
        assert "poisson_ratio" in str(exc)
    else:
        raise AssertionError("invalid Poisson ratio must be rejected")
