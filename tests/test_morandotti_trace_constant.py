import numpy as np
import pytest
from scipy.sparse import csr_matrix

from models.morandotti_trace_constant import largest_generalized_eigenvalue


def test_largest_generalized_eigenvalue_matches_diagonal_ratio():
    A = np.diag([2.0, 9.0, 8.0, 1.0])
    B = np.diag([1.0, 3.0, 2.0, 0.5])
    assert np.isclose(largest_generalized_eigenvalue(csr_matrix(A), csr_matrix(B)), 4.0)


def test_largest_generalized_eigenvalue_is_basis_invariant():
    A = np.diag([1.0, 4.0, 9.0, 16.0])
    B = np.diag([2.0, 2.0, 3.0, 4.0])
    Q, _ = np.linalg.qr(np.array([
        [1.0, 2.0, 0.0, 1.0],
        [0.0, 1.0, 3.0, 2.0],
        [2.0, 0.0, 1.0, 1.0],
        [1.0, 1.0, 1.0, 3.0],
    ]))
    expected = largest_generalized_eigenvalue(A, B)
    observed = largest_generalized_eigenvalue(Q.T @ A @ Q, Q.T @ B @ Q)
    assert np.isclose(observed, expected, rtol=1e-9, atol=1e-10)


def test_largest_generalized_eigenvalue_rejects_nonsymmetric_matrix():
    A = np.array([[1.0, 2.0], [0.0, 1.0]])
    with pytest.raises(ValueError, match="not symmetric"):
        largest_generalized_eigenvalue(A, np.eye(2))


def test_largest_generalized_eigenvalue_rejects_shape_mismatch():
    with pytest.raises(ValueError, match="equal"):
        largest_generalized_eigenvalue(np.eye(2), np.eye(3))
