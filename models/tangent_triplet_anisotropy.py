"""Bundle-valued tangent anisotropy induced by PRISM/G2 tripletti.

The G2 triplett supplies a positive-semidefinite 3x3 Gram form. A separately
specified rank-two map sends its three channels into a shell tangent fibre.
No identification between Q6's 188D tangent space and a football tangent
fibre is implicit: that transfer map is explicit input and remains a
mathematical/data obligation.
"""
from __future__ import annotations
import numpy as np

Q_G2 = np.array([[2.0, -3.0], [-3.0, 6.0]])


def triplett_gram(triplett, q_g2=Q_G2):
    """Return Gamma=R.T Q_G2 R for three column vectors in R^2."""
    R = np.asarray(triplett, dtype=float)
    Q = np.asarray(q_g2, dtype=float)
    if R.shape != (2, 3) or Q.shape != (2, 2):
        raise ValueError("triplett must be 2x3 and q_g2 must be 2x2")
    if not np.allclose(Q, Q.T, atol=1e-12):
        raise ValueError("q_g2 must be symmetric")
    G = R.T @ Q @ R
    return 0.5 * (G + G.T)


def tangent_triplet_anisotropy(triplett, channel_to_ambient, normal,
                               tangent_frame=None, q_g2=Q_G2, tol=1e-9):
    """Push a triplett Gram form into one shell tangent fibre.

    channel_to_ambient is a 3x3 map from the three triplett channels to
    ambient displacement vectors. Its image must lie in n-perp and have
    rank two. The output A is the ambient representative of an endomorphism
    of T_x S; in a local orthonormal tangent frame its matrix is F.T A F.
    """
    U = np.asarray(channel_to_ambient, dtype=float)
    n = np.asarray(normal, dtype=float)
    if U.shape != (3, 3) or n.shape != (3,):
        raise ValueError("channel map must be 3x3 and normal must be length 3")
    nn = np.linalg.norm(n)
    if nn <= tol:
        raise ValueError("normal must be nonzero")
    n = n / nn
    P = np.eye(3) - np.outer(n, n)
    if np.linalg.norm(P @ U - U) > tol * max(1.0, np.linalg.norm(U)):
        raise ValueError("channel map image is not contained in the tangent plane")
    if np.linalg.matrix_rank(U, tol=tol) != 2:
        raise ValueError("channel map must have rank two")
    G = triplett_gram(triplett, q_g2)
    A = U @ G @ U.T
    A = 0.5 * (A + A.T)
    if np.linalg.norm(P @ A @ P - A) > 10 * tol * max(1.0, np.linalg.norm(A)):
        raise ArithmeticError("pushed anisotropy failed tangent-fibre constraint")
    if tangent_frame is None:
        seed = np.array([1.0, 0.0, 0.0])
        if abs(seed @ n) > 0.9:
            seed = np.array([0.0, 1.0, 0.0])
        f1 = seed - (seed @ n) * n
        f1 /= np.linalg.norm(f1)
        f2 = np.cross(n, f1)
        F = np.column_stack((f1, f2))
    else:
        F = np.asarray(tangent_frame, dtype=float)
        if F.shape != (3, 2):
            raise ValueError("tangent_frame must be 3x2")
        if not np.allclose(F.T @ F, np.eye(2), atol=tol):
            raise ValueError("tangent_frame must be orthonormal")
        if np.linalg.norm(F.T @ n) > tol:
            raise ValueError("tangent_frame must span the tangent plane")
    A_local = F.T @ A @ F
    vals = np.linalg.eigvalsh(A_local)
    return {
        "gram": G,
        "ambient_tangent_tensor": A,
        "local_tangent_tensor": A_local,
        "tangent_frame": F,
        "eigenvalues": vals,
        "anisotropy_ratio": float(vals[-1] / vals[0]) if vals[0] > tol else float("inf"),
        "rank": int(np.linalg.matrix_rank(A_local, tol=tol)),
    }


def seam_fibre_stiffness(tangent_tensor, isotropic_tangent=0.0,
                         normal_stiffness=0.0, anisotropy_scale=1.0):
    """Build K_e on E|_Gamma = T S|_Gamma (+) N S|_Gamma.

    Returns diag(K_T, k_N) in a local orthonormal (tangent, normal) frame.
    Tangent anisotropy acts only on TS; the normal/peel channel is separate.
    """
    A = np.asarray(tangent_tensor, dtype=float)
    if A.shape != (2, 2) or not np.allclose(A, A.T, atol=1e-10):
        raise ValueError("tangent_tensor must be a symmetric 2x2 matrix")
    if min(isotropic_tangent, normal_stiffness, anisotropy_scale) < 0:
        raise ValueError("stiffness parameters must be non-negative")
    KT = isotropic_tangent * np.eye(2) + anisotropy_scale * A
    K = np.zeros((3, 3))
    K[:2, :2] = KT
    K[2, 2] = normal_stiffness
    if np.linalg.eigvalsh(K)[0] < -1e-10:
        raise ValueError("fibre stiffness must be positive semidefinite")
    return K


def induce_local_channel_map(t2u_basis, q6_to_shell_tangent, normal, tol=1e-9):
    """Compose the established Q6 T2u triplet with an explicit shell transfer.

    t2u_basis is V in R^(188x3); q6_to_shell_tangent is a pointwise
    3x188 map. Their composition U_x=P_x V must have rank two and image
    in the shell tangent plane. The transfer P_x is not inferred here.
    """
    V = np.asarray(t2u_basis, dtype=float)
    L = np.asarray(q6_to_shell_tangent, dtype=float)
    n = np.asarray(normal, dtype=float)
    if V.shape != (188, 3) or L.shape != (3, 188) or n.shape != (3,):
        raise ValueError("expected V(188x3), transfer(3x188), normal(3,)")
    if not np.allclose(V.T @ V, np.eye(3), atol=tol):
        raise ValueError("T2u triplet basis must be orthonormal")
    U = L @ V
    n = n / np.linalg.norm(n)
    Ptan = np.eye(3) - np.outer(n, n)
    if np.linalg.norm(Ptan @ U - U) > tol * max(1.0, np.linalg.norm(U)):
        raise ValueError("Q6-to-shell transfer does not land in the tangent fibre")
    if np.linalg.matrix_rank(U, tol=tol) != 2:
        raise ValueError("transferred T2u triplet must have local rank two")
    return U
