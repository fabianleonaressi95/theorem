import numpy as np

from audits.purcell_swimmer_wall.q6_cut_project_interface import (
    Q6ShapeMap,
    audit_interface,
    golden_cut_project_frame,
    integrate_shape_edge,
    q6_edges,
    q6_states,
)


def test_golden_split_and_q6_graph_counts():
    p, q = golden_cut_project_frame()
    assert np.allclose(p @ p.T, np.eye(3), atol=1e-12)
    assert np.allclose(q @ q.T, np.eye(3), atol=1e-12)
    assert np.allclose(p @ q.T, np.zeros((3, 3)), atol=1e-12)
    assert q6_states().shape == (64, 6)
    edges = q6_edges()
    assert edges.shape == (192, 3)
    assert [np.count_nonzero(edges[:, 2] == j) for j in range(6)] == [32] * 6


def test_parameterized_map_retains_all_six_projected_axes():
    calibration = np.array([[1.0, 0.2, -0.1], [0.3, 0.8, 0.4]])
    mapping = Q6ShapeMap(calibration, scale=0.7)
    values = mapping.coordinates()
    increments = mapping.edge_increments()
    assert values.shape == (64, 2)
    assert increments.shape == (192, 5)
    assert set(increments[:, 2].astype(int)) == set(range(6))
    assert np.linalg.matrix_rank(increments[:, 3:]) == 2
    report = audit_interface(calibration)
    assert report["six_axes_retained"]
    assert report["edge_axis_counts"] == [32] * 6
    assert np.asarray(report["projected_axis_vectors_2d"]).shape == (2, 6)
    assert np.asarray(report["projected_axis_gram"]).shape == (6, 6)
    assert report["anisotropy_reported_not_constrained"]


def test_shape_edge_transport_for_constant_connection_and_reverse():
    A = np.array([[0.2, -0.1], [0.05, 0.3], [0.4, -0.2]])

    def connection(_shape, _pose):
        return A

    pose0 = np.array([0.1, -0.2, 0.3])
    s0 = np.array([0.0, 0.0])
    s1 = np.array([0.02, -0.01])
    pose1, forward = integrate_shape_edge(pose0, s0, s1, connection)
    pose2, backward = integrate_shape_edge(pose1, s1, s0, connection)
    assert np.allclose(pose1 - pose0, A @ (s1 - s0), atol=1e-10)
    assert np.allclose(pose2, pose0, atol=1e-10)
    assert np.allclose(backward @ forward, np.eye(3), atol=1e-10)
