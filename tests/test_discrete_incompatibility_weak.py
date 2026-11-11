import numpy as np

from models.discrete_incompatibility_weak import (
    assemble_burgers_frank_load,
    assemble_inc_weak,
    p1_triangle_symmetric_strain,
)


def _triangle_quadrature(vertices, order=8):
    z, w = np.polynomial.legendre.leggauss(order)
    z, w = (z + 1.0) / 2.0, w / 2.0
    v0, v1, v2 = vertices
    det = abs(np.linalg.det(np.column_stack((v1 - v0, v2 - v0))))
    points, weights = [], []
    for i, r in enumerate(z):
        for j, s in enumerate(z):
            x = v0 + r * (v1 - v0) + (1.0 - r) * s * (v2 - v0)
            points.append(x)
            weights.append(w[i] * w[j] * (1.0 - r) * det)
    return np.asarray(points), np.asarray(weights)


def _bubble_hessian(x, y):
    # phi=x^2(1-x)^2 y^2(1-y)^2 belongs to H^2_0((0,1)^2).
    px = x*x*(1-x)**2
    py = y*y*(1-y)**2
    dpx = 2*x - 6*x*x + 4*x**3
    dpy = 2*y - 6*y*y + 4*y**3
    ddpx = 2 - 12*x + 12*x*x
    ddpy = 2 - 12*y + 12*y*y
    return np.array([[ddpx*py, dpx*dpy], [dpx*dpy, px*ddpy]])


def test_weak_inc_annihilates_compatible_p1_symmetric_gradient():
    nodes = np.array([[0., 0.], [1., 0.], [1., 1.], [0., 1.]])
    triangles = np.array([[0, 1, 2], [0, 2, 3]])
    rng = np.random.default_rng(20261110)
    displacement = rng.normal(size=(4, 2))
    strain = p1_triangle_symmetric_strain(nodes, triangles, displacement)

    all_hessians, all_weights = [], []
    for ids in triangles:
        points, weights = _triangle_quadrature(nodes[ids])
        all_hessians.append(np.asarray([_bubble_hessian(x, y) for x, y in points]))
        all_weights.append(weights)
    hessians = np.asarray(all_hessians)
    weights = np.asarray(all_weights)
    ncell, nq = weights.shape

    # One strain field (the compatible P1 symmetric gradient), sampled
    # at the same quadrature points as the globally smooth H2_0 test.
    strain_basis = np.broadcast_to(
        strain[:, None, None, :, :], (ncell, nq, 1, 2, 2)
    ).copy()
    test_hessians = hessians[None, ...]
    A = assemble_inc_weak(strain_basis, test_hessians, weights)
    assert A.shape == (1, 1)
    assert abs(A[0, 0]) < 1e-12


def test_burgers_frank_weak_load_sign_and_components():
    test_values_d = np.zeros((2, 1))
    test_gradients_d = np.array([[[1., 2.]], [[-1., .5]]])
    burgers = np.array([[3., 4.]])
    test_values_f = np.array([[2.], [-1.]])
    frank = np.array([.5])
    load = assemble_burgers_frank_load(
        test_values_d, test_gradients_d, burgers, test_values_f, frank
    )
    assert np.allclose(load, np.array([-3., -5.]), atol=1e-14)


def test_p1_strain_rejects_degenerate_triangle():
    nodes = np.array([[0., 0.], [1., 0.], [2., 0.]])
    triangles = np.array([[0, 1, 2]])
    displacement = np.zeros_like(nodes)
    try:
        p1_triangle_symmetric_strain(nodes, triangles, displacement)
    except ValueError as exc:
        assert "degenerate" in str(exc)
    else:
        raise AssertionError("degenerate triangle must be rejected")


def test_p1_strain_recovers_affine_symmetric_gradient():
    nodes = np.array([[0., 0.], [1., 0.], [1., 1.], [0., 1.]])
    triangles = np.array([[0, 1, 2], [0, 2, 3]])
    grad = np.array([[2., 3.], [-1., 4.]])
    displacement = nodes @ grad.T + np.array([.3, -.7])
    strain = p1_triangle_symmetric_strain(nodes, triangles, displacement)
    expected = .5 * (grad + grad.T)
    assert np.allclose(strain, np.broadcast_to(expected, strain.shape), atol=1e-14)



def test_compliance_energy_matrix_is_symmetric_positive_definite():
    from models.discrete_incompatibility_weak import assemble_compliance_energy

    # Two independent constant symmetric strain modes on one unit cell.
    E = np.zeros((1, 1, 2, 2, 2))
    E[0, 0, 0, 0, 0] = 1.0
    E[0, 0, 1, 1, 1] = 1.0
    S = np.zeros((2, 2, 2, 2))
    S[0, 0, 0, 0] = 2.0
    S[1, 1, 1, 1] = 3.0
    M = assemble_compliance_energy(E, np.ones((1, 1)), S)
    assert np.allclose(M, np.diag([2.0, 3.0]))
    assert np.all(np.linalg.eigvalsh(M) > 0.0)


def test_kkt_solver_satisfies_constraint_stationarity_and_energy_identity():
    from models.discrete_incompatibility_weak import solve_constrained_energy

    M = np.diag([2.0, 3.0, 4.0])
    A = np.array([[1.0, 1.0, 0.0], [0.0, 1.0, 1.0]])
    z = np.array([1.0, 2.0])
    out = solve_constrained_energy(M, A, z)
    e = out["strain_coefficients"]
    lam = out["multiplier"]
    assert np.linalg.norm(A @ e - z) < 1e-12
    assert np.linalg.norm(M @ e + A.T @ lam) < 1e-12
    assert np.isclose(out["primal_energy"], out["dual_energy"], atol=1e-12)
    assert out["constraint_rank"] == 2
    assert out["kkt_condition_number"] > 0.0


def test_kkt_solver_rejects_infeasible_source():
    from models.discrete_incompatibility_weak import solve_constrained_energy

    M = np.eye(2)
    A = np.array([[1.0, 0.0], [2.0, 0.0]])
    # Redundant constraints are rejected before feasibility is considered.
    try:
        solve_constrained_energy(M, A, np.array([1.0, 3.0]))
    except ValueError as exc:
        assert "full row rank" in str(exc)
    else:
        raise AssertionError("rank-deficient constraints must be rejected")


def test_kkt_solver_rejects_non_positive_energy():
    from models.discrete_incompatibility_weak import solve_constrained_energy

    try:
        solve_constrained_energy(np.diag([1.0, 0.0]), np.array([[1.0, 0.0]]), np.array([1.0]))
    except ValueError as exc:
        assert "positive definite" in str(exc)
    else:
        raise AssertionError("non-positive energy must be rejected")
