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


def test_largest_generalized_eigenvalue_rejects_singular_denominator():
    with pytest.raises(ValueError, match="positive definite"):
        largest_generalized_eigenvalue(np.eye(4), np.diag([1.0, 1.0, 1.0, 0.0]))


def test_largest_generalized_eigenvalue_reports_small_residual():
    value, diagnostics = largest_generalized_eigenvalue(
        np.diag([2.0, 9.0, 8.0, 1.0]),
        np.diag([1.0, 3.0, 2.0, 0.5]),
        return_diagnostics=True,
    )
    assert np.isclose(value, 4.0)
    assert np.isclose(diagnostics["rayleigh_quotient_check"], value)
    assert diagnostics["relative_generalized_eigenpair_residual"] < 1e-10


def test_largest_generalized_eigenvalue_is_invariant_under_diagonal_scaling():
    # Strongly graded coordinates mimic the coefficient scaling of curved
    # finite-element Hessian Gram matrices. Congruence must preserve the EVP.
    A = np.diag([2.0, 9.0, 8.0, 1.0, 5.0])
    B = np.diag([1.0, 3.0, 2.0, 0.5, 2.5])
    scale = np.diag([1e-5, 1e-2, 1.0, 1e2, 1e5])
    expected = largest_generalized_eigenvalue(A, B)
    observed = largest_generalized_eigenvalue(
        scale @ A @ scale, scale @ B @ scale
    )
    assert np.isclose(observed, expected, rtol=1e-8, atol=1e-10)


def test_largest_generalized_eigenvalue_certifies_denominator_spd():
    A = np.diag([2.0, 9.0, 8.0, 1.0, 5.0])
    B = np.array([
        [2.0, 0.2, 0.0, 0.0, 0.0],
        [0.2, 2.0, 0.1, 0.0, 0.0],
        [0.0, 0.1, 3.0, 0.1, 0.0],
        [0.0, 0.0, 0.1, 2.0, 0.1],
        [0.0, 0.0, 0.0, 0.1, 2.5],
    ])
    value, diagnostics = largest_generalized_eigenvalue(
        A, B, return_diagnostics=True
    )
    assert np.isfinite(value)
    assert diagnostics["denominator_numerically_positive_definite"]
    assert diagnostics["denominator_lambda_min_estimate"] > 0.0
    assert diagnostics["denominator_lambda_max_estimate"] >= diagnostics["denominator_lambda_min_estimate"]
    assert diagnostics["denominator_lambda_min_relative_residual"] < 1e-7
    assert diagnostics["denominator_lambda_max_relative_residual"] < 1e-7


def test_largest_generalized_eigenvalue_rejects_indefinite_positive_diagonal_denominator():
    A = np.eye(4)
    B = np.array([
        [1.0, 1.5, 0.0, 0.0],
        [1.5, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ])
    with pytest.raises(ValueError, match="positive definite"):
        largest_generalized_eigenvalue(A, B)
