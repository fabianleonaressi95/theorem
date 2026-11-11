"""Geometry and reconstruction primitives for the bicircular-annular audit.

The module deliberately separates exact two-disk geometry from sampled
kinematic reconstruction. No physical constitutive law is inferred here.
"""
from __future__ import annotations

import math
from typing import Callable

import numpy as np


def _validate_lens(r1: float, r2: float, d: float) -> None:
    if min(r1, r2, d) <= 0:
        raise ValueError("r1, r2 and d must be positive")
    if not abs(r1 - r2) < d < r1 + r2:
        raise ValueError("the disks must intersect in a proper lens")


def lens_geometry(r1: float, r2: float, d: float) -> dict[str, float]:
    """Return the common-chord geometry for centres (0,0) and (d,0)."""
    _validate_lens(r1, r2, d)
    x_star = (d * d + r1 * r1 - r2 * r2) / (2.0 * d)
    h2 = max(0.0, r1 * r1 - x_star * x_star)
    h = math.sqrt(h2)
    x_lo = max(-r1, d - r2)
    x_hi = min(r1, d + r2)
    return {
        "x_star": x_star,
        "half_chord": h,
        "chord": 2.0 * h,
        "x_lo": x_lo,
        "x_hi": x_hi,
    }


def lens_area_exact(r1: float, r2: float, d: float) -> float:
    """Exact area of intersection of two disks."""
    _validate_lens(r1, r2, d)
    a1 = (d * d + r1 * r1 - r2 * r2) / (2.0 * d * r1)
    a2 = (d * d + r2 * r2 - r1 * r1) / (2.0 * d * r2)
    a1 = min(1.0, max(-1.0, a1))
    a2 = min(1.0, max(-1.0, a2))
    radicand = (
        (-d + r1 + r2) * (d + r1 - r2)
        * (d - r1 + r2) * (d + r1 + r2)
    )
    return r1 * r1 * math.acos(a1) + r2 * r2 * math.acos(a2) - 0.5 * math.sqrt(max(0.0, radicand))


def lens_area_centroid(r1: float, r2: float, d: float, order: int = 160) -> tuple[float, float, float]:
    """Gauss-Legendre area and centroid; y-centroid is zero by symmetry."""
    g = lens_geometry(r1, r2, d)
    nodes, weights = np.polynomial.legendre.leggauss(order)
    # The sin^2 map removes the square-root endpoint singularities of the
    # circular caps, giving spectral convergence for the area and first moment.
    t = 0.25 * math.pi * (nodes + 1.0)
    wt = 0.25 * math.pi * weights
    x_star, x_lo, x_hi = g["x_star"], g["x_lo"], g["x_hi"]

    def integrate(a: float, b: float, which: int, moment: bool) -> float:
        if b <= a:
            return 0.0
        x = a + (b - a) * np.sin(t) ** 2
        jac = 2.0 * (b - a) * np.sin(t) * np.cos(t)
        if which == 2:
            y = np.sqrt(np.maximum(0.0, r2 * r2 - (x - d) ** 2))
        else:
            y = np.sqrt(np.maximum(0.0, r1 * r1 - x ** 2))
        f = 2.0 * y * (x if moment else 1.0) * jac
        return float(np.dot(wt, f))

    area = integrate(x_lo, x_star, 2, False) + integrate(x_star, x_hi, 1, False)
    first = integrate(x_lo, x_star, 2, True) + integrate(x_star, x_hi, 1, True)
    return area, first / area, 0.0


def annular_points(
    centre: tuple[float, float],
    r_inner: float,
    r_outer: float,
    n_radial: int = 4,
    n_angular: int = 64,
) -> np.ndarray:
    """Midpoint samples on a uniform radial/angular annular grid."""
    if not 0 <= r_inner < r_outer or n_radial < 1 or n_angular < 3:
        raise ValueError("invalid annular sampling parameters")
    radii = r_inner + (np.arange(n_radial) + 0.5) * (r_outer - r_inner) / n_radial
    theta = 2.0 * np.pi * np.arange(n_angular) / n_angular
    rr, tt = np.meshgrid(radii, theta, indexing="ij")
    return np.column_stack((
        centre[0] + (rr * np.cos(tt)).ravel(),
        centre[1] + (rr * np.sin(tt)).ravel(),
    ))


def fit_affine_deformation(points: np.ndarray, displacements: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Least-squares fit u(x)=A(x-xbar)+ubar; return F=I+A and intercept."""
    x = np.asarray(points, dtype=float)
    u = np.asarray(displacements, dtype=float)
    if x.ndim != 2 or u.shape != x.shape or x.shape[1] != 2 or len(x) < 3:
        raise ValueError("points and displacements must be matching (N,2) arrays")
    xc = x - x.mean(axis=0)
    uc = u - u.mean(axis=0)
    if np.linalg.matrix_rank(xc) < 2:
        raise ValueError("sample points do not span the plane")
    coeff, *_ = np.linalg.lstsq(xc, uc, rcond=None)
    grad_u = coeff.T
    return np.eye(2) + grad_u, u.mean(axis=0) - grad_u @ x.mean(axis=0)


def green_strain(F: np.ndarray) -> np.ndarray:
    F = np.asarray(F, dtype=float)
    if F.shape != (2, 2):
        raise ValueError("F must be 2x2")
    return 0.5 * (F.T @ F - np.eye(2))


def strain_anisotropy(E: np.ndarray) -> float:
    """Half-difference magnitude of the two eigenvalues of a symmetric 2x2 strain."""
    E = np.asarray(E, dtype=float)
    if E.shape != (2, 2):
        raise ValueError("E must be 2x2")
    return float(math.sqrt(((E[0, 0] - E[1, 1]) / 2.0) ** 2 + E[0, 1] ** 2))


def sample_loop_closure(
    radius: float,
    n: int,
    burgers: tuple[float, float] = (1.0, 0.0),
    frank: float = 1.0,
) -> tuple[np.ndarray, float]:
    """Polygonal loop integrals for a manufactured Burgers/Frank 1/r field.

    The field is a controlled closure witness, not a solved elasticity field.
    """
    if radius <= 0 or n < 8:
        raise ValueError("radius must be positive and n at least 8")
    theta = 2.0 * np.pi * np.arange(n) / n
    points = radius * np.column_stack((np.cos(theta), np.sin(theta)))
    increments = np.roll(points, -1, axis=0) - points
    mids = points + 0.5 * increments
    r2 = np.sum(mids * mids, axis=1)
    b = np.asarray(burgers, dtype=float)
    # Vector-valued one-form: each component has circulation b_component.
    tangent_field = np.column_stack((-mids[:, 1], mids[:, 0])) / (2.0 * np.pi * r2[:, None])
    circulation = float(np.sum(np.einsum("ij,ij->i", tangent_field, increments)))\n    b_measured = b * circulation
    # Scalar rotational connection with circulation frank.
    omega = frank * tangent_field
    frank_measured = float(np.sum(np.einsum("ij,ij->i", omega, increments)))
    return b_measured, frank_measured
