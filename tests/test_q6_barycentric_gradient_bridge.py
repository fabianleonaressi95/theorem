import numpy as np
import pytest

from audits.purcell_swimmer_wall.q6_cut_project_interface import Q6ShapeMap
from audits.q6_barycentric_gradient_bridge import (
    audit_q6_barycentric_gradient_bridge,
    barycentric_p1_vertex_projection,
    lift_shape_gradient_to_lorentzian_4d,
    q6_square_faces,
    q6_square_triangulation,
    triangle_p1_geometry,
    triangle_p1_gradient,
)


CALIBRATION = np.array([[1.0, 0.2, -0.1], [0.3, 0.8, 0.4]])


def test_q6_square_cells_and_triangle_split_have_expected_counts():
    faces = q6_square_faces()
    triangles = q6_square_triangulation()
    assert faces.shape == (240, 4)
    assert triangles.shape == (480, 3)
    assert np.all(np.sort(triangles[0::2], axis=1)[:, 0] >= 0)


def test_triangle_p1_gradient_is_exact_for_affine_fields():
    coords = Q6ShapeMap(CALIBRATION).coordinates()
    triangles = q6_square_triangulation()
    target = np.array([0.73, -1.21])
    values = coords @ target + 0.44
    for ids in triangles:
        area, centre, covariance = triangle_p1_geometry(coords[ids])
        assert area > 0 and np.all(np.linalg.eigvalsh(covariance) >= -1e-14)
        assert np.allclose(triangle_p1_gradient(coords[ids], values[ids]), target, atol=1e-10)


def test_t130_q6_gradient_commutes_with_barycentric_p1_on_affine_patch():
    report = audit_q6_barycentric_gradient_bridge(CALIBRATION)
    assert report["q6_vertices"] == 64
    assert report["q6_edges"] == 192
    assert report["q6_square_faces"] == 240
    assert report["p1_triangles"] == 480
    assert report["affine_patch_pass"]
    assert report["max_operator_residual"] < 1e-9


def test_non_affine_field_operator_mismatch_is_reported_not_hidden():
    values = np.asarray([(-1.0)**(v.bit_count()) * (1.0 + v / 64.0) for v in range(64)])
    report = audit_q6_barycentric_gradient_bridge(CALIBRATION, values)
    assert report["affine_patch_pass"] is None
    assert np.isfinite(report["max_operator_residual"])
    assert report["max_operator_residual"] >= 0


def test_lorentzian_gradient_lift_satisfies_tangent_duality():
    frame = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0], [0.0, 0.0]])
    eta = np.diag([1.0, -1.0, -1.0, -1.0])
    grad2 = np.array([0.7, -1.3])
    lifted = lift_shape_gradient_to_lorentzian_4d(grad2, frame, eta)
    assert np.allclose(frame.T @ eta @ lifted, grad2, atol=1e-13)
    assert np.allclose(lifted, [0.0, -0.7, 1.3, 0.0], atol=1e-13)


def test_lorentzian_gradient_lift_rejects_null_plane():
    frame = np.array([[1.0, 0.0], [1.0, 0.0], [0.0, 1.0], [0.0, 0.0]])
    with pytest.raises(ValueError):
        lift_shape_gradient_to_lorentzian_4d(np.ones(2), frame)
