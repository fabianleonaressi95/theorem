"""Finite normal-mode and Green–Kubo utilities for T131.

These routines operate on supplied model matrices and sampled stress data.
They do not generate a material potential, phason kinetics, or a transport
coefficient without a physically justified trajectory.
"""
from __future__ import annotations

import numpy as np


def generalized_normal_modes(stiffness, mass, *, stability_tolerance=1e-10):
    """Solve K e = omega_squared M e with M positive definite.

    Returns omega_squared, mass-normalized eigenvectors (columns), and a
    Boolean stability mask. Negative eigenvalues are retained and flagged.
    """
    k = np.asarray(stiffness, dtype=float)
    m = np.asarray(mass, dtype=float)
    if k.ndim != 2 or k.shape[0] != k.shape[1] or m.shape != k.shape:
        raise ValueError("stiffness and mass must be square matrices of equal size")
    if not np.all(np.isfinite(k)) or not np.all(np.isfinite(m)):
        raise ValueError("matrices must be finite")
    if not np.allclose(k, k.T, atol=1e-11, rtol=1e-11):
        raise ValueError("stiffness must be symmetric")
    if not np.allclose(m, m.T, atol=1e-11, rtol=1e-11):
        raise ValueError("mass must be symmetric")
    try:
        lower = np.linalg.cholesky(m)
    except np.linalg.LinAlgError as exc:
        raise ValueError("mass must be positive definite") from exc
    left = np.linalg.solve(lower, k)
    whitened = np.linalg.solve(lower, left.T).T
    whitened = 0.5 * (whitened + whitened.T)
    omega_squared, z = np.linalg.eigh(whitened)
    modes = np.linalg.solve(lower.T, z)
    scale = max(1.0, float(np.max(np.abs(omega_squared))))
    stable = omega_squared >= -stability_tolerance * scale
    return omega_squared, modes, stable


def polarization_weights(mode, propagation_direction):
    """Return longitudinal/transverse weights for (n_sites, dimension) mode."""
    e = np.asarray(mode)
    direction = np.asarray(propagation_direction, dtype=float)
    if e.ndim != 2 or direction.shape != (e.shape[1],):
        raise ValueError("mode must be (n_sites, dimension), direction dimension must match")
    if not np.all(np.isfinite(e)) or not np.all(np.isfinite(direction)):
        raise ValueError("mode and direction must be finite")
    norm = float(np.linalg.norm(direction))
    total = float(np.vdot(e, e).real)
    if norm == 0 or total == 0:
        raise ValueError("direction and mode must be nonzero")
    unit = direction / norm
    longitudinal = float(np.sum(np.abs(e @ unit) ** 2) / total)
    longitudinal = min(1.0, max(0.0, longitudinal))
    return {"longitudinal": longitudinal, "transverse": 1.0 - longitudinal}


def green_kubo_stress(stress, dt, temperature, volume, *, max_lag=None):
    """Estimate finite-window viscosity from sampled extensive stress.

    stress has shape (n_samples,) or (n_samples, n_components). The returned
    correlation uses all available time origins at each lag and is centered
    by the sample mean. The integral is deliberately finite-window.
    """
    values = np.asarray(stress, dtype=float)
    if values.ndim == 1:
        values = values[:, None]
        scalar = True
    elif values.ndim == 2:
        scalar = False
    else:
        raise ValueError("stress must have shape (n_samples,) or (n_samples, n_components)")
    if values.shape[0] < 2 or values.shape[1] < 1 or not np.all(np.isfinite(values)):
        raise ValueError("stress must contain at least two finite samples")
    if not np.isfinite(dt) or dt <= 0 or not np.isfinite(temperature) or temperature <= 0:
        raise ValueError("dt and temperature must be finite and positive")
    if not np.isfinite(volume) or volume <= 0:
        raise ValueError("volume must be finite and positive")
    n = values.shape[0]
    if max_lag is None:
        lag = n - 1
    else:
        if int(max_lag) != max_lag or max_lag < 1 or max_lag >= n:
            raise ValueError("max_lag must be an integer in [1, n_samples-1]")
        lag = int(max_lag)
    centered = values - values.mean(axis=0, keepdims=True)
    corr = np.empty((lag + 1, values.shape[1], values.shape[1]), dtype=float)
    for j in range(lag + 1):
        corr[j] = centered[j:].T @ centered[:n-j] / (n-j)
    integral = np.trapezoid(corr, dx=float(dt), axis=0)
    viscosity = integral / (8.617333262145e-5 * temperature * volume)
    if scalar:
        return {"correlation": corr[:, 0, 0], "integral": float(integral[0, 0]),
                "viscosity": float(viscosity[0, 0]), "max_lag": lag}
    return {"correlation": corr, "integral": integral, "viscosity": viscosity,
            "max_lag": lag}
