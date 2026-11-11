import numpy as np
import pytest

J = np.array([[0.0, -1.0], [1.0, 0.0]])

def polar_angle_2d(G):
    G = np.asarray(G, dtype=float)
    if G.shape != (2, 2) or not np.isfinite(G).all() or np.linalg.det(G) <= 0:
        raise ValueError("G must be finite, 2x2 and orientation preserving")
    return float(np.arctan2(G[1, 0] - G[0, 1], G[0, 0] + G[1, 1]))

def test_polar_angle_recovers_rotation_in_right_polar_decomposition():
    theta = 0.73
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    U = np.array([[2.0, 0.3], [0.3, 1.2]])
    assert np.isclose(polar_angle_2d(R @ U), theta)

def test_polar_angle_rejects_orientation_reversal():
    with pytest.raises(ValueError):
        polar_angle_2d(np.diag([1.0, -1.0]))

def test_barycentric_covariance_is_psd_and_tangent_to_triangle():
    V = np.array([[0., 0., 0.], [1., 0., 0.], [0.2, 0.8, 0.]])
    a = np.array([2., 3., 4.])
    S = a.sum()
    C = (np.diag(a) * S - np.outer(a, a)) / (S*S*(S+1))
    Sigma = V.T @ C @ V
    assert np.linalg.eigvalsh(Sigma).min() > -1e-13
    assert np.allclose(Sigma[2], 0.0, atol=1e-13)
    assert np.isclose(np.trace(C), 0.0, atol=1e-13) is False

def test_semidirect_product_rotation_transports_translation():
    theta = np.pi / 2
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    b1, b2 = np.array([1., 0.]), np.array([0., 0.])
    composed = b2 + R @ b1
    assert np.allclose(composed, [0., 1.], atol=1e-14)
