"""Exact algebraic regression tests for the QAT quaternion/SU(2) bridge.

These tests establish finite-dimensional identities only; they do not validate
QAT dynamics, a continuum spin connection, or physical interpretation.
"""
import numpy as np


def qmul(a, b):
    """Quaternion product for (w,x,y,z), with i*j=k."""
    w, x, y, z = a
    W, X, Y, Z = b
    return np.array([
        w*W - x*X - y*Y - z*Z,
        w*X + x*W + y*W - z*Z,
        w*Y - x*Z + y*W + z*X,
        w*Z + x*Y - y*X + z*W,
    ], dtype=float)


def qconj(q):
    return np.array([q[0], -q[1], -q[2], -q[3]], dtype=float)


def q_to_su2(q):
    w, x, y, z = q
    return np.array([[w-1j*z, -y-1j*x],
                     [y-1j*x, w+1j*z]], dtype=complex)


def rotate_pure(q, v):
    p = np.array([0., *v])
    out = qmul(qmul(q, p), qconj(q))
    return out[1:]


def test_unit_quaternion_matrix_is_su2():
    rng = np.random.default_rng(63064)
    for _ in range(100):
        q = rng.normal(size=4); q /= np.linalg.norm(q)
        U = q_to_su2(q)
        assert np.linalg.norm(U.conj().T @ U - np.eye(2)) < 1e-12
        assert abs(np.linalg.det(U) - 1) < 1e-12


def test_quaternion_conjugation_preserves_scalar_and_vector_norm():
    rng = np.random.default_rng(63065)
    for _ in range(100):
        q = rng.normal(size=4); q /= np.linalg.norm(q)
        rho = rng.normal(); j = rng.normal(size=3)
        J = np.array([rho, *j])
        transformed = qmul(qmul(q, J), qconj(q))
        assert abs(transformed[0] - rho) < 1e-12
        assert abs(np.linalg.norm(transformed[1:]) - np.linalg.norm(j)) < 1e-12


def test_quaternion_rotation_is_orthogonal_and_orientation_preserving():
    rng = np.random.default_rng(63066)
    for _ in range(30):
        q = rng.normal(size=4); q /= np.linalg.norm(q)
        R = np.column_stack([rotate_pure(q, e) for e in np.eye(3)])
        assert np.linalg.norm(R.T @ R - np.eye(3)) < 1e-12
        assert abs(np.linalg.det(R) - 1) < 1e-12


def test_double_cover_q_and_minus_q_induce_same_rotation():
    rng = np.random.default_rng(63067)
    for _ in range(100):
        q = rng.normal(size=4); q /= np.linalg.norm(q)
        v = rng.normal(size=3)
        assert np.linalg.norm(rotate_pure(q, v) - rotate_pure(-q, v)) < 1e-12
        assert np.linalg.norm(q_to_su2(-q) + q_to_su2(q)) < 1e-12


def test_su2_map_respects_quaternion_product():
    rng = np.random.default_rng(63068)
    for _ in range(100):
        a = rng.normal(size=4); a /= np.linalg.norm(a)
        b = rng.normal(size=4); b /= np.linalg.norm(b)
        assert np.linalg.norm(q_to_su2(qmul(a, b)) -
                             q_to_su2(a) @ q_to_su2(b)) < 1e-12
