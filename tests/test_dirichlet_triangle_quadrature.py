import numpy as np
import pytest

from src.dirichlet_triangle_quadrature import (
    dirichlet_partition_function,
    dirichlet_triangle_moments,
    dirichlet_weighted_integral,
    duffy_jacobi_rule,
)

V = np.array([[0.0, 0.0, 0.0], [2.0, 0.0, 0.0], [0.0, 1.0, 0.0]])


def exact_dirichlet_moments(a):
    a = np.asarray(a, dtype=float)
    s = a.sum()
    mean = a / s
    covariance = (np.diag(a * s) - np.outer(a, a)) / (s * s * (s + 1.0))
    return mean, covariance


def test_a1_uniform_triangle_normalization_and_covariance():
    a = np.ones(3)
    out = dirichlet_triangle_moments(V, a, order=3)
    mean, covariance = exact_dirichlet_moments(a)
    assert out["Z_quadrature"] == pytest.approx(1.0)
    assert out["Z_quadrature"] == pytest.approx(out["Z_exact"], abs=2e-14)
    assert np.allclose(out["mean_lambda"], mean, atol=2e-14)
    assert np.allclose(out["covariance_lambda"], covariance, atol=2e-14)
    assert np.allclose(out["centroid"], V.mean(axis=0), atol=2e-14)


def test_a2_nonuniform_dirichlet_moments_match_closed_form():
    a = np.array([2.0, 3.0, 4.0])
    out = dirichlet_triangle_moments(V, a, order=5)
    mean, covariance = exact_dirichlet_moments(a)
    assert out["Z_quadrature"] == pytest.approx(out["Z_exact"], abs=2e-14)
    assert np.allclose(out["mean_lambda"], mean, atol=2e-13)
    assert np.allclose(out["covariance_lambda"], covariance, atol=2e-13)


def test_raw_second_moment_is_not_mislabelled_as_covariance():
    out = dirichlet_triangle_moments(V, [2.0, 3.0, 4.0], order=5)
    raw = out["second_moment_lambda"]
    covariance = out["covariance_lambda"]
    assert np.allclose(covariance, raw - np.outer(out["mean_lambda"], out["mean_lambda"]))
    assert not np.allclose(raw, covariance)


def test_a3_weighted_polynomial_integral_and_constant_normalization():
    a = np.array([1.5, 2.0, 3.5])
    constant = dirichlet_weighted_integral(V, a, lambda x: np.ones(len(x)), order=5)
    z = dirichlet_partition_function(V, a, order=5)
    assert constant == pytest.approx(z["Z_exact"], abs=2e-13)

    f = lambda x: 1.0 + 2.0*x[:, 0] - 0.5*x[:, 1] + x[:, 0]**2
    q1 = dirichlet_weighted_integral(V, a, f, order=5)
    q2 = dirichlet_weighted_integral(V, a, f, order=8)
    assert q1 == pytest.approx(q2, abs=2e-13)


def test_invalid_parameters_and_degenerate_triangle_rejected():
    with pytest.raises(ValueError, match="positive"):
        duffy_jacobi_rule([1.0, 0.0, 1.0])
    with pytest.raises(ValueError, match="nondegenerate"):
        dirichlet_triangle_moments(np.zeros((3, 3)), [1.0, 1.0, 1.0])
