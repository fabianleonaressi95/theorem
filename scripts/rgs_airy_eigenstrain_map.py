#!/usr/bin/env python3
"""Airy-to-eigenstrain source map for a controlled plane-strain transfer test.

Convention:
  sigma_xx = phi_yy, sigma_yy = phi_xx, sigma_xy = -phi_xy
  inc(eps) = d_yy eps_xx + d_xx eps_yy - d_xy gamma_xy

The returned eigenstrain is minus the elastic compliance applied to the
Airy stress. Consequently C:eps_star = -sigma_Airy, so the zero-displacement
stress C:(eps(0)-eps_star) equals sigma_Airy. This is a stress-equivalent
source map, not an independently prescribed physical defect eigenstrain.
"""
from __future__ import annotations

import numpy as np


def _validate(phi, dx, dy, young_modulus, poisson_ratio):
    phi = np.asarray(phi, dtype=float)
    if phi.ndim != 2 or min(phi.shape) < 4:
        raise ValueError("phi must be a 2D array with at least four points per axis")
    if not np.isfinite(phi).all():
        raise ValueError("phi must be finite")
    if not (np.isfinite(dx) and np.isfinite(dy) and dx > 0 and dy > 0):
        raise ValueError("dx and dy must be finite and positive")
    if not (np.isfinite(young_modulus) and young_modulus > 0):
        raise ValueError("Young's modulus must be finite and positive")
    if not (np.isfinite(poisson_ratio) and -1 < poisson_ratio < 0.5):
        raise ValueError("plane-strain Poisson ratio must lie in (-1, 1/2)")
    return phi


def spectral_derivatives(phi, dx, dy):
    """Return phi_x, phi_y, phi_xx, phi_xy, phi_yy on a periodic grid."""
    phi = np.asarray(phi, dtype=float)
    if phi.ndim != 2 or min(phi.shape) < 4 or not np.isfinite(phi).all():
        raise ValueError("phi must be a finite 2D array with at least four points per axis")
    kx = 2.0 * np.pi * np.fft.fftfreq(phi.shape[1], d=dx)
    ky = 2.0 * np.pi * np.fft.fftfreq(phi.shape[0], d=dy)
    ky2, kx2 = np.meshgrid(ky, kx, indexing="ij")
    ph = np.fft.fft2(phi)
    def deriv(multiplier):
        return np.fft.ifft2(multiplier * ph).real
    return {
        "phi_x": deriv(1j * kx2),
        "phi_y": deriv(1j * ky2),
        "phi_xx": deriv(-(kx2 ** 2)),
        "phi_xy": deriv(-(kx2 * ky2)),
        "phi_yy": deriv(-(ky2 ** 2)),
    }


def airy_stress(phi, dx, dy):
    """Airy stress in engineering component order (sigma_xx, sigma_yy, sigma_xy)."""
    d = spectral_derivatives(phi, dx, dy)
    return np.stack((d["phi_yy"], d["phi_xx"], -d["phi_xy"]), axis=-1)


def plane_strain_compliance(stress, young_modulus, poisson_ratio):
    """Apply isotropic plane-strain compliance to (sxx, syy, sxy)."""
    s = np.asarray(stress, dtype=float)
    if s.ndim < 1 or s.shape[-1] != 3 or not np.isfinite(s).all():
        raise ValueError("stress must be finite with final component axis of length 3")
    E, nu = float(young_modulus), float(poisson_ratio)
    if not (np.isfinite(E) and E > 0 and np.isfinite(nu) and -1 < nu < 0.5):
        raise ValueError("require E > 0 and -1 < nu < 1/2")
    sxx, syy, sxy = np.moveaxis(s, -1, 0)
    factor = (1.0 + nu) / E
    exx = factor * ((1.0 - nu) * sxx - nu * syy)
    eyy = factor * ((1.0 - nu) * syy - nu * sxx)
    gamma = 2.0 * factor * sxy
    return np.stack((exx, eyy, gamma), axis=-1)


def airy_to_eigenstrain(phi, dx, dy, young_modulus, poisson_ratio):
    """Return Airy stress and stress-equivalent plastic eigenstrain.

    For the returned eps_star, C:eps_star = -sigma_Airy. Hence a displacement
    formulation with u=0 reproduces sigma_Airy exactly at the constitutive
    level. The map is useful for transfer/consistency tests but is not an
    independent defect-source validation.
    """
    phi = _validate(phi, dx, dy, young_modulus, poisson_ratio)
    stress = airy_stress(phi, dx, dy)
    elastic_strain = plane_strain_compliance(stress, young_modulus, poisson_ratio)
    return {"stress": stress, "elastic_strain": elastic_strain,
            "eigenstrain": -elastic_strain,
            "airy_biharmonic_coefficient": (1.0 - poisson_ratio**2) / young_modulus}


def spectral_incompatibility(strain, dx, dy):
    """Compute inc(eps)=d_yy exx+d_xx eyy-d_xy gamma for periodic arrays."""
    e = np.asarray(strain, dtype=float)
    if e.ndim != 3 or e.shape[-1] != 3 or not np.isfinite(e).all():
        raise ValueError("strain must have shape (ny, nx, 3) and be finite")
    ny, nx, _ = e.shape
    kx = 2.0 * np.pi * np.fft.fftfreq(nx, d=dx)
    ky = 2.0 * np.pi * np.fft.fftfreq(ny, d=dy)
    ky2, kx2 = np.meshgrid(ky, kx, indexing="ij")
    exx, eyy, gamma = np.moveaxis(e, -1, 0)
    exx_h, eyy_h, gamma_h = map(np.fft.fft2, (exx, eyy, gamma))
    inc_h = -(ky2**2) * exx_h - (kx2**2) * eyy_h + (kx2*ky2) * gamma_h
    return np.fft.ifft2(inc_h).real


def spectral_biharmonic(phi, dx, dy):
    """Return Delta^2 phi using periodic spectral differentiation."""
    phi = np.asarray(phi, dtype=float)
    ny, nx = phi.shape
    kx = 2.0 * np.pi * np.fft.fftfreq(nx, d=dx)
    ky = 2.0 * np.pi * np.fft.fftfreq(ny, d=dy)
    ky2, kx2 = np.meshgrid(ky, kx, indexing="ij")
    return np.fft.ifft2((kx2**2 + ky2**2)**2 * np.fft.fft2(phi)).real
