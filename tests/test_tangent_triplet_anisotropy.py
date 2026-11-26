import numpy as np
import pytest

from models.tangent_triplet_anisotropy import (
    Q_G2, induce_local_channel_map, seam_fibre_stiffness,
    tangent_triplet_anisotropy, triplett_gram,
)


def test_g2_triplett_gram_is_psd_and_rank_at_most_two():
    R = np.array([[1.0, 0.0, 1.0], [0.0, 1.0, 1.0]])
    G = triplett_gram(R)
    assert np.allclose(G, G.T)
    assert np.linalg.eigvalsh(G)[0] >= -1e-12
    assert np.linalg.matrix_rank(G, tol=1e-10) <= 2


def test_anisotropy_lives_in_tangent_fibre_and_is_frame_covariant():
    n = np.array([0.0, 0.0, 1.0])
    U = np.array([[1.0, 0.2, 0.0], [0.1, 1.0, 0.0], [0.0, 0.0, 0.0]])
    R = np.array([[1.0, 0.0, 1.0], [0.0, 1.0, 1.0]])
    out = tangent_triplet_anisotropy(R, U, n)
    A = out["ambient_tangent_tensor"]
    assert np.allclose(A @ n, 0.0, atol=1e-12)
    assert out["rank"] == 2

    theta = 0.37
    O = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    F = out["tangent_frame"]
    changed_frame = F @ O
    changed = tangent_triplet_anisotropy(R, U, n, tangent_frame=changed_frame)
    assert np.allclose(changed["local_tangent_tensor"],
                       O.T @ out["local_tangent_tensor"] @ O, atol=1e-12)
    assert np.allclose(changed["eigenvalues"], out["eigenvalues"], atol=1e-12)


def test_seam_fibre_stiffness_keeps_normal_channel_separate():
    A = np.array([[2.0, 0.2], [0.2, 1.0]])
    K = seam_fibre_stiffness(A, isotropic_tangent=0.5,
                             normal_stiffness=3.0, anisotropy_scale=2.0)
    assert np.allclose(K[:2, :2], 0.5*np.eye(2) + 2*A)
    assert K[2, 2] == 3.0
    assert np.allclose(K[:2, 2], 0.0)


def test_q6_t2u_bridge_requires_explicit_rank_two_tangent_transfer():
    V = np.zeros((188, 3))
    V[:3, :] = np.eye(3)
    L = np.zeros((3, 188))
    L[0, 0] = 1.0
    L[1, 1] = 1.0
    n = np.array([0.0, 0.0, 1.0])
    U = induce_local_channel_map(V, L, n)
    assert np.linalg.matrix_rank(U) == 2
    with pytest.raises(ValueError):
        induce_local_channel_map(V, np.eye(3, 188), np.array([1.0, 0.0, 0.0]))
