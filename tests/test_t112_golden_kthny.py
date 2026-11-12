import numpy as np

from scripts.audit_t112_golden_kthny import A, audit, fibonacci_matrix


def test_golden_matrix_is_unimodular():
    assert round(np.linalg.det(A)) == -1


def test_golden_eigenvalues():
    phi = (1 + np.sqrt(5)) / 2
    values = np.sort(np.linalg.eigvals(A.astype(float)))
    assert np.allclose(values, [-1 / phi, phi], atol=1e-12)


def test_fibonacci_power_identity():
    fib = [0, 1]
    for _ in range(2, 14):
        fib.append(fib[-1] + fib[-2])
    for n in range(1, 13):
        expected = np.array([[fib[n + 1], fib[n]],
                             [fib[n], fib[n - 1]]])
        assert np.array_equal(fibonacci_matrix(n), expected)


def test_coordinate_covariance_is_null_control():
    result = audit(8)
    assert result["coordinate_covariance_residual"] < 1e-12
