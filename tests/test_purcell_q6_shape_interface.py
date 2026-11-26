import numpy as np
import pytest

from audits.purcell_swimmer_wall.q6_shape_interface import (
    audit_q6_shape_map,
    build_q6_shape_map,
    local_edge_transport,
    se2_exp,
    window_diameter,
)


FRAME = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])


def test_golden_q6_shape_map_retains_all_192_edges_and_six_axes():
    data = build_q6_shape_map(FRAME, angle_scale=1e-3)
    report = audit_q6_shape_map(data)
    assert len(data.internal_coordinates) == 64
    assert len(data.edges) == 192
    assert np.array_equal(np.bincount(data.edges[:, 2], minlength=6),
                          np.full(6, 32))
    assert report["all_six_cut_project_axes_retained"]
    assert report["edge_increment_rank"] == 2


def test_shape_increment_is_exact_vertex_potential_difference():
    data = build_q6_shape_map(FRAME, angle_scale=0.03)
    for index, (u, v, _axis) in enumerate(data.edges):
        expected = (data.shape_coordinates_unwrapped[v]
                    - data.shape_coordinates_unwrapped[u])
        assert np.allclose(data.edge_shape_increments[index], expected,
                           atol=1e-13)


def test_invalid_calibration_is_rejected():
    with pytest.raises(ValueError):
        build_q6_shape_map(np.eye(2, 3) * 2.0, angle_scale=1e-3)
    with pytest.raises(ValueError):
        build_q6_shape_map(FRAME, angle_scale=0.0)


def test_projected_cube_window_diameter_is_positive():
    assert window_diameter() > 0.0


def test_se2_exponential_is_a_proper_rigid_motion():
    transform = se2_exp((0.2, -0.1, 0.03))
    rotation = transform[:2, :2]
    assert np.allclose(rotation.T @ rotation, np.eye(2), atol=1e-12)
    assert np.isclose(np.linalg.det(rotation), 1.0, atol=1e-12)
    assert np.allclose(transform[2], [0.0, 0.0, 1.0])


def test_q6_edge_transport_is_in_se2():
    data = build_q6_shape_map(FRAME, angle_scale=1e-3)
    transform = local_edge_transport(data, 0, quadrature_order=32)
    rotation = transform[:2, :2]
    assert np.allclose(rotation.T @ rotation, np.eye(2), atol=1e-10)
    assert np.isclose(np.linalg.det(rotation), 1.0, atol=1e-10)
    assert np.allclose(transform[2], [0.0, 0.0, 1.0], atol=1e-12)
