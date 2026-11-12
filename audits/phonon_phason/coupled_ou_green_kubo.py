"""Exact two-sector coupled Gaussian benchmark for T132.

This is a finite-dimensional reversible Ornstein-Uhlenbeck (OU) model.
It is a verification benchmark for sector bookkeeping and Green-Kubo
correlations, not a calibrated material model or a material viscosity.
"""
from __future__ import annotations

import numpy as np


def _symmetric_matrix(value, name):
    matrix = np.asarray(value, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError(f"{name} must be a square matrix")
    if not np.all(np.isfinite(matrix)) or not np.allclose(
        matrix, matrix.T, atol=1e-12, rtol=1e-12
    ):
        raise ValueError(f"{name} must be finite and symmetric")
    return matrix


def _model(stiffness, stress_matrices, temperature, mobility):
    k = _symmetric_matrix(stiffness, "stiffness")
    if np.linalg.eigvalsh(k)[0] <= 0:
        raise ValueError("stiffness must be positive definite")
    if not np.isfinite(temperature) or temperature <= 0:
        raise ValueError("temperature must be finite and positive")
    if not np.isfinite(mobility) or mobility <= 0:
        raise ValueError("mobility must be finite and positive")
    if not stress_matrices:
        raise ValueError("at least one sector stress matrix is required")
    sectors = {}
    for name, value in stress_matrices.items():
        s = _symmetric_matrix(value, f"stress matrix {name}")
        if s.shape != k.shape:
            raise ValueError("all stress matrices must match stiffness dimension")
        sectors[str(name)] = s
    values, vectors = np.linalg.eigh(k)
    covariance = float(temperature) * (vectors / values) @ vectors.T
    return k, sectors, float(temperature), float(mobility), values, vectors, covariance


def _propagator(eigenvalues, eigenvectors, time, mobility):
    decay = np.exp(-mobility * eigenvalues * float(time))
    return (eigenvectors * decay) @ eigenvectors.T


def sector_stress_correlations(
    stiffness, stress_matrices, times, *, temperature=1.0, mobility=1.0
):
    """Return exact C_ab(t) for centered quadratic sector stresses.

    H(q)=q.T K q/2, dq=-mobility*K*q dt + sqrt(2 mobility kBT) dW,
    Pi_a(q)=q.T S_a q/2. For equilibrium covariance C=kBT K^-1,
    C_ab(t)=1/2 tr[S_a E(t) S_b E(t).T], E(t)=exp(-mobility K t) C.
    Output has shape (n_times, n_sectors, n_sectors).
    """
    _, sectors, temp, mob, eig, vec, covariance = _model(
        stiffness, stress_matrices, temperature, mobility
    )
    t = np.asarray(times, dtype=float)
    if t.ndim != 1 or t.size == 0 or not np.all(np.isfinite(t)) or np.any(t < 0):
        raise ValueError("times must be a nonempty finite nonnegative vector")
    names = list(sectors)
    result = np.empty((t.size, len(names), len(names)), dtype=float)
    for index, time in enumerate(t):
        propagator = _propagator(eig, vec, time, mob)
        cross_covariance = propagator @ covariance
        for a, name_a in enumerate(names):
            for b, name_b in enumerate(names):
                result[index, a, b] = 0.5 * np.trace(
                    sectors[name_a] @ cross_covariance
                    @ sectors[name_b] @ cross_covariance.T
                )
    return {"sectors": tuple(names), "correlation": result}


def green_kubo_blocks(times, correlations, *, kbt=1.0):
    """Trapezoidal finite-window integral of every ordered sector pair."""
    t = np.asarray(times, dtype=float)
    c = np.asarray(correlations, dtype=float)
    if t.ndim != 1 or t.size < 2 or not np.all(np.isfinite(t)):
        raise ValueError("times must contain at least two finite values")
    if np.any(np.diff(t) <= 0):
        raise ValueError("times must be strictly increasing")
    if c.ndim != 3 or c.shape[0] != t.size or c.shape[1] != c.shape[2]:
        raise ValueError("correlations must have shape (n_times, n_sectors, n_sectors)")
    if not np.all(np.isfinite(c)) or not np.isfinite(kbt) or kbt <= 0:
        raise ValueError("correlations and kbt must be finite; kbt must be positive")
    return np.trapezoid(c, x=t, axis=0) / float(kbt)


def simulate_ou(
    stiffness, stress_matrices, *, dt, n_steps, temperature=1.0,
    mobility=1.0, seed=0
):
    """Exact-step stationary OU trajectory and empirical sector correlations.

    The transition is sampled exactly for each time step (not Euler-Maruyama).
    The returned empirical correlations are centered, all-time-origin estimates.
    """
    _, sectors, temp, mob, eig, vec, covariance = _model(
        stiffness, stress_matrices, temperature, mobility
    )
    if not np.isfinite(dt) or dt <= 0:
        raise ValueError("dt must be finite and positive")
    if int(n_steps) != n_steps or n_steps < 2:
        raise ValueError("n_steps must be an integer >= 2")
    propagator = _propagator(eig, vec, dt, mob)
    innovation = covariance - propagator @ covariance @ propagator.T
    innovation = 0.5 * (innovation + innovation.T)
    # Roundoff can create tiny negative eigenvalues in an otherwise PSD matrix.
    ivals, ivecs = np.linalg.eigh(innovation)
    if ivals[0] < -1e-10 * max(1.0, float(ivals[-1])):
        raise ValueError("OU innovation covariance is not positive semidefinite")
    noise_factor = ivecs @ np.diag(np.sqrt(np.maximum(ivals, 0.0)))
    rng = np.random.default_rng(seed)
    q = np.empty((int(n_steps), covariance.shape[0]), dtype=float)
    q[0] = rng.multivariate_normal(np.zeros(covariance.shape[0]), covariance)
    noise = rng.standard_normal((int(n_steps) - 1, covariance.shape[0]))
    for i in range(1, int(n_steps)):
        q[i] = propagator @ q[i - 1] + noise_factor @ noise[i - 1]
    names = list(sectors)
    observables = np.column_stack([
        0.5 * np.einsum("ni,ij,nj->n", q, sectors[name], q)
        for name in names
    ])
    observables -= observables.mean(axis=0, keepdims=True)
    empirical = observables.T @ observables / int(n_steps)
    return {
        "trajectory": q,
        "sectors": tuple(names),
        "lag0_correlation": empirical,
    }


def total_correlation(correlations):
    """Sum all ordered sector-pair blocks into the total stress correlation."""
    c = np.asarray(correlations, dtype=float)
    if c.ndim != 3 or c.shape[1] != c.shape[2]:
        raise ValueError("correlations must have shape (n_times, n_sectors, n_sectors)")
    return c.sum(axis=(1, 2))
