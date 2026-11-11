import numpy as np
import pytest

from models.morandotti_cell_reconstruction import (
    build_defect_vector,
    reconstruct_airy_potential,
    solve_interaction_system,
)


def test_defect_vector_uses_published_frank_burgers_order_and_signs():
    centers = np.array([[-0.28, 0.0], [0.28, 0.0]])
    frank = np.array([0.2, 0.0])
    burgers = np.array([[0.0, 0.0], [0.03, -0.04]])
    phi = build_defect_vector(centers, frank, burgers)
    expected = np.array([0.2, -0.056, 0.0, 0.0, -0.04, -0.03])
    assert np.allclose(phi, expected, atol=1e-14)


def test_interaction_solve_and_airy_reconstruction():
    rng = np.random.default_rng(20261111)
    Q = rng.normal(size=(6, 6))
    M = Q.T @ Q + np.eye(6)
    phi = np.array([0.2, -0.056, 0.0, 0.0, -0.04, -0.03])
    coeff = solve_interaction_system(M, phi)
    assert np.linalg.norm(M @ coeff - phi) < 1e-12
    fields = rng.normal(size=(6, 2, 5))
    E, nu = 210.0, 0.29
    v = reconstruct_airy_potential(fields, coeff, E, nu)
    expected = -(E / (1.0 - nu**2)) * np.einsum("i,ijk->jk", coeff, fields)
    assert v.shape == (2, 5)
    assert np.allclose(v, expected, atol=1e-12)


def test_reconstruction_is_linear_in_defect_data():
    M = np.diag(np.arange(1.0, 7.0))
    phi1 = np.array([1., 0., 0., 0., 0., 0.])
    phi2 = np.array([0., 0., 0., 0., 1., -2.])
    fields = np.arange(6 * 3, dtype=float).reshape(6, 3)
    a1 = solve_interaction_system(M, phi1)
    a2 = solve_interaction_system(M, phi2)
    a12 = solve_interaction_system(M, phi1 + phi2)
    v1 = reconstruct_airy_potential(fields, a1, 1.0, 0.2)
    v2 = reconstruct_airy_potential(fields, a2, 1.0, 0.2)
    v12 = reconstruct_airy_potential(fields, a12, 1.0, 0.2)
    assert np.allclose(v12, v1 + v2, atol=1e-14)


def test_interaction_solver_rejects_non_symmetric_or_non_spd_matrix():
    phi = np.ones(2)
    with pytest.raises(ValueError, match="symmetric"):
        solve_interaction_system(np.array([[2., 1.], [0., 2.]]), phi)
    with pytest.raises(ValueError, match="positive definite"):
        solve_interaction_system(np.array([[1., 0.], [0., 0.]]), phi)


def test_defect_vector_rejects_inconsistent_shapes():
    with pytest.raises(ValueError, match="frank_angles"):
        build_defect_vector(np.zeros((2, 2)), np.zeros(1), np.zeros((2, 2)))

def test_defect_vector_is_rotation_equivariant():
    centers = np.array([[-0.28, 0.0], [0.28, 0.0]])
    frank = np.array([0.2, 0.0])
    burgers = np.array([[0.0, 0.0], [0.03, -0.04]])
    theta = np.deg2rad(37.0)
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    phi = build_defect_vector(centers, frank, burgers).reshape(2, 3)
    phi_rot = build_defect_vector(centers @ R.T, frank, burgers @ R.T).reshape(2, 3)
    expected = phi.copy()
    expected[:, 1:3] = phi[:, 1:3] @ R.T
    assert np.allclose(phi_rot[:, 0], phi[:, 0], atol=1e-14)
    assert np.allclose(phi_rot[:, 1:3], expected[:, 1:3], atol=1e-14)



def test_two_core_coordinate_deformation_moves_core_boundaries_and_fixes_outer_nodes():
    from models.morandotti_cell_reconstruction import deform_two_core_coordinates
    reference = np.array([[-0.28, 0.0], [0.28, 0.0]])
    target = np.array([[-0.32, 0.0], [0.32, 0.0]])
    points = np.array([
        [-0.28 + 0.12, 0.0], [0.28 - 0.12, 0.0],
        [0.0, 0.0], [0.0, 1.0],
    ])
    moved = deform_two_core_coordinates(points, reference, target, 0.12, 0.50)
    assert np.allclose(moved[0], [-0.32 + 0.12, 0.0], atol=1e-13)
    assert np.allclose(moved[1], [0.32 - 0.12, 0.0], atol=1e-13)
    assert np.allclose(moved[3], points[3], atol=1e-14)
    assert np.isfinite(moved).all()


def test_symmetric_separation_change_keeps_pair_midpoint_fixed():
    from models.morandotti_cell_reconstruction import deform_two_core_coordinates
    reference = np.array([[-0.28, 0.0], [0.28, 0.0]])
    target = np.array([[-0.34, 0.0], [0.34, 0.0]])
    points = np.array([[0.0, 0.0], [0.0, 0.25], [0.0, 0.8]])
    moved = deform_two_core_coordinates(points, reference, target, 0.12, 0.32)
    assert np.allclose(moved, points, atol=1e-14)


def test_two_core_support_radius_is_based_on_reference_separation():
    from models.morandotti_cell_reconstruction import two_core_support_radius
    assert two_core_support_radius(0.12, 0.56, 0.50) == pytest.approx(0.44)
    assert two_core_support_radius(0.12, 0.80, 0.50) == pytest.approx(0.50)
    with pytest.raises(ValueError):
        two_core_support_radius(0.12, 0.24, 0.50)


def test_compressed_pair_keeps_each_reference_core_boundary_independent():
    from models.morandotti_cell_reconstruction import deform_two_core_coordinates
    reference = np.array([[-0.28, 0.0], [0.28, 0.0]])
    target = np.array([[-0.24, 0.0], [0.24, 0.0]])  # target separation 0.48
    boundary_points = np.array([[-0.16, 0.0], [0.16, 0.0]])
    moved = deform_two_core_coordinates(boundary_points, reference, target, 0.12, 0.50)
    assert np.allclose(moved, [[-0.12, 0.0], [0.12, 0.0]], atol=1e-13)



def test_defect_source_split_reconstructs_total_and_mixed_quadratic_term():
    from models.morandotti_cell_reconstruction import (
        build_defect_components, defect_quadratic_decomposition,
    )
    centers = np.array([[-0.28, 0.0], [0.28, 0.0]])
    frank = np.array([0.2, -0.1])
    burgers = np.array([[0.01, -0.02], [0.03, -0.04]])
    phi_f, phi_b, phi = build_defect_components(centers, frank, burgers)
    assert np.allclose(phi, phi_f + phi_b, atol=1e-14)
    M0 = np.arange(36, dtype=float).reshape(6, 6)
    M = M0.T @ M0 + np.eye(6)
    parts = defect_quadratic_decomposition(M, phi_f, phi_b)
    assert abs(parts["additivity_residual"]) < 1e-12
    assert np.isclose(parts["total_quadratic"],
                      0.5 * phi @ np.linalg.solve(M, phi), atol=1e-12)


def test_deformation_metric_is_rotation_invariant_and_detects_stretch():
    from models.morandotti_cell_reconstruction import deformation_metric
    J0 = np.broadcast_to(np.eye(2), (2, 3, 2, 2)).copy()
    F = np.array([[2.0, 0.0], [0.0, 0.5]])
    J1 = np.einsum("ij,...jk->...ik", F, J0)
    result = deformation_metric(J0, J1)
    assert np.allclose(result["metric"][0, 0], np.diag([4.0, 0.25]))
    assert np.allclose(result["anisotropy"], (4.0 - 0.25) / (4.0 + 0.25))
    theta = 0.71
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    rotated = deformation_metric(J0, np.einsum("ij,...jk->...ik", R, J1))
    assert np.allclose(rotated["metric"], result["metric"], atol=1e-12)


def test_deformation_metric_rejects_inverted_current_jacobian():
    from models.morandotti_cell_reconstruction import deformation_metric
    with pytest.raises(ValueError, match="positive orientation"):
        deformation_metric(np.eye(2), np.diag([-1.0, 1.0]))
