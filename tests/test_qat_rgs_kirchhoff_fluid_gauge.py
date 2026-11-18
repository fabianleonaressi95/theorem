import numpy as np

from scripts.audit_qat_rgs_kirchhoff_fluid_gauge import (
    covariant_laplacian, su2_random
)


def test_t118_gauge_covariance_on_small_algebraic_fixture():
    rng = np.random.default_rng(118)
    edges = np.array([[0, 1, 0], [1, 2, 1]], dtype=int)
    links = np.stack([su2_random(rng) for _ in range(2)])
    weights = np.array([0.7, 1.3])
    gauges = np.stack([su2_random(rng) for _ in range(3)])
    transformed = np.stack([
        gauges[h] @ links[k] @ gauges[g].conj().T
        for k, (g, h, _) in enumerate(edges)
    ])
    H = covariant_laplacian(3, edges, links, weights)
    HG = covariant_laplacian(3, edges, transformed, weights)
    G = np.zeros((6, 6), dtype=complex)
    for v in range(3):
        G[2*v:2*v+2, 2*v:2*v+2] = gauges[v]
    assert np.allclose(HG, G @ H @ G.conj().T, atol=1e-12)


def test_covariant_laplacian_is_hermitian_positive_semidefinite():
    rng = np.random.default_rng(64)
    edges = np.array([[0, 1, 0], [1, 2, 1], [0, 2, 2]], dtype=int)
    links = np.stack([su2_random(rng) for _ in range(3)])
    H = covariant_laplacian(3, edges, links, np.array([1.0, 0.5, 2.0]))
    assert np.allclose(H, H.conj().T, atol=1e-12)
    assert np.linalg.eigvalsh(H).min() >= -1e-12


def test_quaternion_matrix_lift_lands_in_su2():
    rng = np.random.default_rng(63)
    for _ in range(20):
        U = su2_random(rng)
        assert np.allclose(U.conj().T @ U, np.eye(2), atol=1e-12)
        assert abs(np.linalg.det(U) - 1) < 1e-12
