"""Finite Q6 geometry--quantum backreaction model (MQM-1).

The 64 Q6 vertices carry a normalized complex state. Positive edge
conductances are parameterized by x=log(w). The Hamiltonian is the
weighted graph Laplacian H(x)=hbar*omega0*B diag(exp(x)) B.T.
The geometry follows a declared gradient flow of the joint energy.

This is a finite-dimensional mathematical model, not a calibrated
physical theory or a continuum limit.
"""
from __future__ import annotations

import numpy as np


def q6_incidence():
    """Return the oriented vertex-edge incidence matrix of the 6-cube.

    Vertices are integers 0..63. For each bit i, include the edge v->v+2**i
    exactly when bit i of v is zero. Thus there are 64 vertices and 192 edges.
    """
    edges = []
    for v in range(64):
        for i in range(6):
            if ((v >> i) & 1) == 0:
                edges.append((v, v ^ (1 << i)))
    b = np.zeros((64, len(edges)), dtype=float)
    for j, (v, w) in enumerate(edges):
        b[v, j] = -1.0
        b[w, j] = 1.0
    return b


def _validate(x, psi, stiffness, coupling, mobility, hbar):
    x = np.asarray(x, dtype=float)
    psi = np.asarray(psi, dtype=complex)
    if x.shape != (192,) or not np.all(np.isfinite(x)):
        raise ValueError("x must be a finite real vector of length 192")
    if psi.shape != (64,) or not np.all(np.isfinite(psi)):
        raise ValueError("psi must be a finite complex vector of length 64")
    norm = float(np.vdot(psi, psi).real)
    if not np.isclose(norm, 1.0, atol=1e-10, rtol=1e-10):
        raise ValueError("psi must have unit norm")
    for value, name in ((stiffness, "stiffness"), (coupling, "coupling"),
                        (mobility, "mobility"), (hbar, "hbar")):
        if not np.isfinite(value) or value <= 0:
            raise ValueError(f"{name} must be finite and positive")
    return x, psi


def hamiltonian(x, *, coupling=1.0):
    """Hermitian positive-semidefinite weighted Q6 graph Hamiltonian."""
    x = np.asarray(x, dtype=float)
    if x.shape != (192,) or not np.all(np.isfinite(x)):
        raise ValueError("x must be a finite real vector of length 192")
    if not np.isfinite(coupling) or coupling <= 0:
        raise ValueError("coupling must be finite and positive")
    b = q6_incidence()
    weights = np.exp(x)
    return float(coupling) * (b * weights) @ b.T


def joint_energy(x, psi, x_reference, *, stiffness=1.0, coupling=1.0):
    """E= k/2 ||x-x_ref||^2 + <psi,H(x)psi>, for ||psi||=1."""
    x = np.asarray(x, dtype=float)
    psi = np.asarray(psi, dtype=complex)
    x_reference = np.asarray(x_reference, dtype=float)
    if x.shape != (192,) or x_reference.shape != (192,):
        raise ValueError("x and x_reference must have length 192")
    if psi.shape != (64,) or not np.all(np.isfinite(psi)):
        raise ValueError("psi must be a finite vector of length 64")
    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(x_reference)):
        raise ValueError("geometry vectors must be finite")
    if not np.isclose(np.vdot(psi, psi).real, 1.0, atol=1e-10):
        raise ValueError("psi must have unit norm")
    if not np.isfinite(stiffness) or stiffness <= 0:
        raise ValueError("stiffness must be finite and positive")
    h = hamiltonian(x, coupling=coupling)
    value = 0.5 * stiffness * np.dot(x - x_reference, x - x_reference)
    return float(value + np.vdot(psi, h @ psi).real)


def geometry_gradient(x, psi, x_reference, *, stiffness=1.0, coupling=1.0):
    """Exact derivative dE/dx_e = k(x_e-x*_e)+g exp(x_e)|B_e.T psi|^2."""
    x = np.asarray(x, dtype=float)
    psi = np.asarray(psi, dtype=complex)
    x_reference = np.asarray(x_reference, dtype=float)
    if x.shape != (192,) or x_reference.shape != (192,) or psi.shape != (64,):
        raise ValueError("expected x,x_reference in R^192 and psi in C^64")
    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(x_reference)):
        raise ValueError("geometry vectors must be finite")
    if not np.all(np.isfinite(psi)) or not np.isclose(
        np.vdot(psi, psi).real, 1.0, atol=1e-10
    ):
        raise ValueError("psi must be finite and normalized")
    if not np.isfinite(stiffness) or stiffness <= 0:
        raise ValueError("stiffness must be finite and positive")
    if not np.isfinite(coupling) or coupling <= 0:
        raise ValueError("coupling must be finite and positive")
    edge_difference = q6_incidence().T @ psi
    return (float(stiffness) * (x - x_reference)
            + float(coupling) * np.exp(x) * np.abs(edge_difference) ** 2)


def coupled_rhs(x, psi, x_reference, *, stiffness=1.0, coupling=1.0,
                mobility=1.0, hbar=1.0):
    """Return (xdot, psidot) for gradient geometry + Schrödinger state flow."""
    x, psi = _validate(x, psi, stiffness, coupling, mobility, hbar)
    x_reference = np.asarray(x_reference, dtype=float)
    if x_reference.shape != (192,) or not np.all(np.isfinite(x_reference)):
        raise ValueError("x_reference must be a finite vector of length 192")
    grad = geometry_gradient(
        x, psi, x_reference, stiffness=stiffness, coupling=coupling
    )
    h = hamiltonian(x, coupling=coupling)
    xdot = -float(mobility) * grad
    psidot = -1j * (h @ psi) / float(hbar)
    return xdot, psidot


def energy_dissipation_rate(x, psi, x_reference, *, stiffness=1.0,
                            coupling=1.0, mobility=1.0):
    """Exact instantaneous dE/dt=-mobility*||grad_x E||^2."""
    grad = geometry_gradient(
        x, psi, x_reference, stiffness=stiffness, coupling=coupling
    )
    return -float(mobility) * float(np.dot(grad, grad))
