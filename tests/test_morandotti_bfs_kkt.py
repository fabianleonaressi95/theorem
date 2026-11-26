import numpy as np

from models.morandotti_bfs_kkt import (
    assemble_bfs_rectangular,
    assemble_bfs_defect_source,
    evaluate_bfs_test_basis,
    plane_stress_stiffness,
    solve_bfs_kkt,
)


def test_plane_stress_stiffness_has_elastic_symmetries_and_positive_modes():
    S = plane_stress_stiffness(young_modulus=210.0, poisson_ratio=0.3)
    assert np.allclose(S, S.swapaxes(0, 1))
    assert np.allclose(S, S.swapaxes(2, 3))
    assert np.allclose(S, S.transpose(2, 3, 0, 1))
    dev = np.diag([1.0, -1.0])
    vol = np.eye(2)
    assert np.allclose(np.einsum('ijkl,kl->ij', S, dev), 210.0/1.3*dev)
    assert np.allclose(np.einsum('ijkl,kl->ij', S, vol), 210.0/0.7*vol)


def test_bfs_assembly_is_h2_conforming_dimensionally_and_full_row_rank():
    out = assemble_bfs_rectangular(nx=2, ny=2, quadrature_order=3)
    A, M = out["A"], out["M"]
    assert A.shape == (4, 12)
    assert M.shape == (12, 12)
    assert out["test_hessians"].shape == (4, 4, 9, 2, 2)
    assert out["strain_basis"].shape == (4, 9, 12, 2, 2)
    assert np.linalg.matrix_rank(A) == A.shape[0]
    assert np.allclose(M, M.T, atol=1e-13)
    eig = np.linalg.eigvalsh(M)
    assert eig.min() > 0.0
    assert np.allclose(eig, np.array([1.0/(4.0*1.3)]*8 + [1.0/(4.0*0.7)]*4), atol=1e-10)
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
        plane_stress_stiffness(1.0, 1.0)
    except ValueError as exc:
        assert "poisson_ratio" in str(exc)
    else:
        raise AssertionError("invalid Poisson ratio must be rejected")



def test_bfs_basis_values_and_gradients_at_interior_vertex():
    values, gradients = evaluate_bfs_test_basis(np.array([[0.5, 0.5]]), nx=2, ny=2)
    assert values.shape == (4, 1)
    assert gradients.shape == (4, 1, 2)
    assert np.allclose(values[:, 0], np.array([1.0, 0.0, 0.0, 0.0]), atol=1e-13)
    assert np.allclose(gradients[:, 0], np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0], [0.0, 0.0]]), atol=1e-13)


def test_bfs_point_and_finite_core_defect_sources_are_finite_and_distinct():
    xd = np.array([[0.35, 0.45]])
    burgers = np.array([[1.0, 0.0]])
    xf = np.array([[0.65, 0.55]])
    frank = np.array([0.2])
    point = assemble_bfs_defect_source(xd, burgers, xf, frank, nx=2, ny=2)
    core = assemble_bfs_defect_source(
        xd, burgers, xf, frank, nx=2, ny=2, core_radius=0.12,
        quadrature_order=3,
    )
    assert point.shape == (4,)
    assert core.shape == (4,)
    assert np.isfinite(point).all() and np.isfinite(core).all()
    assert np.linalg.norm(point) > 0.0
    assert np.linalg.norm(core) > 0.0
    assert not np.allclose(point, core)



def test_bfs_dislocation_and_disclination_loads_separately_feed_kkt():
    empty2 = np.empty((0, 2))
    empty1 = np.empty((0,))
    d1 = assemble_bfs_defect_source(
        np.array([[0.35, 0.45]]), np.array([[1.0, 0.0]]),
        empty2, empty1, nx=2, ny=2, core_radius=0.12,
    )
    d2 = assemble_bfs_defect_source(
        empty2, empty2, np.array([[0.65, 0.55]]), np.array([0.2]),
        nx=2, ny=2, core_radius=0.12,
    )
    for source in (d1, d2):
        out = solve_bfs_kkt(source, nx=2, ny=2)
        assert np.linalg.norm(source) > 0.0
        assert out["constraint_residual"] < 1e-10
        assert out["stationarity_residual"] < 1e-10
        assert np.isclose(out["primal_energy"], out["dual_energy"], atol=1e-10)


def test_disclination_dipole_load_converges_to_edge_dislocation_load():
    """Symmetric Frank dipole tends to a Burgers source in the weak load."""
    center = np.array([0.5, 0.5])
    burgers = np.array([[0.6, 0.8]])
    magnitude = float(np.linalg.norm(burgers[0]))
    normal = np.array([-burgers[0, 1], burgers[0, 0]]) / magnitude

    empty2 = np.empty((0, 2))
    empty1 = np.empty((0,))
    target = assemble_bfs_defect_source(
        center[None, :], burgers, empty2, empty1,
        nx=4, ny=4, core_radius=0.10, quadrature_order=6,
    )

    errors = []
    for separation in (0.24, 0.12, 0.06):
        # zeta_dip = -s delta_(x+d n/2) + s delta_(x-d n/2),
        # with s*d=|b|. The symmetric pair has the same first moment
        # as the edge-dislocation source.
        frank_strength = magnitude / separation
        positions = np.stack((
            center + 0.5*separation*normal,
            center - 0.5*separation*normal,
        ))
        dipole = assemble_bfs_defect_source(
            empty2, empty2, positions,
            np.array([frank_strength, -frank_strength]),
            nx=4, ny=4, core_radius=0.10, quadrature_order=6,
        )
        errors.append(np.linalg.norm(dipole - target))

    assert errors[2] < errors[1] < errors[0]
