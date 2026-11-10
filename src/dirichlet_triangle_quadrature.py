"""Duffy--Gauss-Jacobi quadrature for Dirichlet-weighted triangle integrals.

The barycentric map is
    lambda_0=(1-s)(1-t), lambda_1=s, lambda_2=(1-s)t,
with Jacobian (1-s). The Jacobi parameters follow the convention
roots_jacobi(n, alpha, beta) ~ (1-x)^alpha (1+x)^beta.
"""
from __future__ import annotations

import numpy as np
from scipy.special import gammaln, roots_jacobi


def _validate_vertices(vertices: np.ndarray) -> tuple[np.ndarray, float]:
    v = np.asarray(vertices, dtype=float)
    if v.shape != (3, 3) or not np.all(np.isfinite(v)):
        raise ValueError("vertices must be a finite array of shape (3, 3)")
    area = 0.5 * float(np.linalg.norm(np.cross(v[1] - v[0], v[2] - v[0])))
    if not np.isfinite(area) or area <= np.finfo(float).eps:
        raise ValueError("triangle must be nondegenerate")
    return v, area


def _validate_parameters(parameters: np.ndarray) -> np.ndarray:
    a = np.asarray(parameters, dtype=float)
    if a.shape != (3,) or not np.all(np.isfinite(a)) or np.any(a <= 0):
        raise ValueError("Dirichlet parameters must be three finite positive numbers")
    return a


def duffy_jacobi_rule(parameters, order: int = 8) -> tuple[np.ndarray, np.ndarray]:
    """Return barycentric nodes (order**2,3) and transformed weights.

    The weights integrate
      s**(a1-1) (1-s)**(a0+a2-1)
      t**(a2-1) (1-t)**(a0-1)
    over the unit square. The physical triangle factor 2*area is applied
    by the integration routines below.
    """
    a0, a1, a2 = _validate_parameters(parameters)
    if not isinstance(order, (int, np.integer)) or order < 1:
        raise ValueError("quadrature order must be a positive integer")

    alpha_s, beta_s = a0 + a2 - 1.0, a1 - 1.0
    alpha_t, beta_t = a0 - 1.0, a2 - 1.0
    xs, ws = roots_jacobi(order, alpha_s, beta_s)
    xt, wt = roots_jacobi(order, alpha_t, beta_t)

    # x -> (x+1)/2 contributes 2**(-(alpha+beta+1)) to each rule.
    s = 0.5 * (xs + 1.0)
    t = 0.5 * (xt + 1.0)
    ws = ws * 2.0 ** (-(alpha_s + beta_s + 1.0))
    wt = wt * 2.0 ** (-(alpha_t + beta_t + 1.0))

    ss, tt = np.meshgrid(s, t, indexing="ij")
    lam = np.column_stack((
        ((1.0 - ss) * (1.0 - tt)).ravel(),
        ss.ravel(),
        ((1.0 - ss) * tt).ravel(),
    ))
    weights = np.outer(ws, wt).ravel()
    return lam, weights


def dirichlet_partition_function(vertices, parameters, order: int = 8) -> dict:
    """Compute the quadrature and exact Gamma/Beta normalizations."""
    v, area = _validate_vertices(vertices)
    a = _validate_parameters(parameters)
    _, weights = duffy_jacobi_rule(a, order)
    z_quadrature = 2.0 * area * float(weights.sum())
    z_exact = 2.0 * area * float(np.exp(np.sum(gammaln(a)) - gammaln(np.sum(a))))
    return {
        "area": area,
        "Z_quadrature": z_quadrature,
        "Z_exact": z_exact,
        "normalization_abs_error": abs(z_quadrature - z_exact),
    }


def dirichlet_triangle_moments(vertices, parameters, order: int = 8) -> dict:
    """Return weighted centroid, raw second moment and true covariance.

    second_moment_lambda is E[lambda lambda^T], not the covariance.
    The covariance is formed by subtracting the outer product of the mean.
    """
    v, area = _validate_vertices(vertices)
    a = _validate_parameters(parameters)
    lam, weights = duffy_jacobi_rule(a, order)
    total = float(weights.sum())
    if not np.isfinite(total) or total <= 0:
        raise ArithmeticError("quadrature weights have invalid total mass")

    mean = np.einsum("n,ni->i", weights, lam) / total
    second = np.einsum("n,ni,nj->ij", weights, lam, lam) / total
    covariance = second - np.outer(mean, mean)
    centroid = mean @ v
    covariance_x = v.T @ covariance @ v
    z_quad = 2.0 * area * total
    z_exact = 2.0 * area * float(np.exp(np.sum(gammaln(a)) - gammaln(np.sum(a))))
    return {
        "area": area,
        "Z_quadrature": z_quad,
        "Z_exact": z_exact,
        "mean_lambda": mean,
        "second_moment_lambda": second,
        "covariance_lambda": covariance,
        "centroid": centroid,
        "covariance_x": covariance_x,
    }


def dirichlet_weighted_integral(vertices, parameters, function, order: int = 8) -> float:
    """Approximate integral_F function(x) prod(lambda_i**(a_i-1)) dA."""
    v, area = _validate_vertices(vertices)
    a = _validate_parameters(parameters)
    lam, weights = duffy_jacobi_rule(a, order)
    points = lam @ v
    values = np.asarray(function(points), dtype=float)
    if values.shape != (len(points),) or not np.all(np.isfinite(values)):
        raise ValueError("function must return one finite scalar per quadrature point")
    return float(2.0 * area * np.dot(weights, values))
