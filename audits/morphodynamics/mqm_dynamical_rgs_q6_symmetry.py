"""Equivariance of the coupled MQM-1 flow under RGS-compatible Q6 symmetries.

The group and canonical edge/vertex labels are imported from the preceding
EQC-RGS-Q6 and MQM-Q6 audits. No new relabelling convention is introduced.
"""
from __future__ import annotations

import numpy as np

from audits.morphodynamics.eqc_rgs_q6_gates import generated_rgs_q6_group
from audits.morphodynamics.q6_mqm_symmetry import edge_permutation
from audits.morphodynamics.q6_quantum_geometry import (
    coupled_rhs,
    geometry_gradient,
    hamiltonian,
    joint_energy,
)


def transform_vertex_state(psi, vertex_map):
    """Apply (P psi)[p(v)] = psi[v]."""
    psi = np.asarray(psi, dtype=complex)
    if psi.shape != (64,) or len(vertex_map) != 64:
        raise ValueError("expected a 64-state and a 64-vertex permutation")
    out = np.empty_like(psi)
    out[np.asarray(vertex_map, dtype=int)] = psi
    return out


def transform_edge_field(values, edge_map):
    """Apply (rho x)[rho(e)] = x[e] to a 192-edge field."""
    values = np.asarray(values, dtype=float)
    if values.shape != (192,) or len(edge_map) != 192:
        raise ValueError("expected a 192-edge field and edge permutation")
    out = np.empty_like(values)
    out[np.asarray(edge_map, dtype=int)] = values
    return out


def rgs_mqm_stabilizer(x_reference, *, atol=0.0):
    """Return precisely those RGS-Q6 permutations fixing x_reference."""
    reference = np.asarray(x_reference, dtype=float)
    if reference.shape != (192,) or not np.all(np.isfinite(reference)):
        raise ValueError("x_reference must be a finite vector of length 192")
    survivors = []
    for vertex_map in generated_rgs_q6_group():
        edge_map = edge_permutation(vertex_map)
        if np.allclose(reference, transform_edge_field(reference, edge_map),
                       rtol=0.0, atol=atol):
            survivors.append(vertex_map)
    return frozenset(survivors)


def equivariance_residuals(x, psi, x_reference, vertex_map, *,
                           stiffness=1.0, coupling=1.0, mobility=1.0,
                           hbar=1.0):
    """Residuals for H, E, gradient and both components of the MQM-1 vector field.

    The reference configuration must be fixed by vertex_map; the function
    reports residuals even when it is not, making symmetry breaking visible.
    """
    x = np.asarray(x, dtype=float)
    psi = np.asarray(psi, dtype=complex)
    x_reference = np.asarray(x_reference, dtype=float)
    edge_map = edge_permutation(vertex_map)

    xp = transform_edge_field(x, edge_map)
    xrefp = transform_edge_field(x_reference, edge_map)
    psip = transform_vertex_state(psi, vertex_map)

    h = hamiltonian(x, coupling=coupling)
    hp = hamiltonian(xp, coupling=coupling)
    p = np.zeros((64, 64), dtype=float)
    p[np.asarray(vertex_map, dtype=int), np.arange(64)] = 1.0

    energy = joint_energy(x, psi, x_reference,
                          stiffness=stiffness, coupling=coupling)
    # Keep x_reference fixed: symmetry is tested for the same model parameters.
    energyp = joint_energy(xp, psip, x_reference,
                           stiffness=stiffness, coupling=coupling)
    grad = geometry_gradient(x, psi, x_reference,
                             stiffness=stiffness, coupling=coupling)
    gradp = geometry_gradient(xp, psip, x_reference,
                              stiffness=stiffness, coupling=coupling)
    xdot, psidot = coupled_rhs(
        x, psi, x_reference, stiffness=stiffness, coupling=coupling,
        mobility=mobility, hbar=hbar
    )
    xdotp, psidot_p = coupled_rhs(
        xp, psip, x_reference, stiffness=stiffness, coupling=coupling,
        mobility=mobility, hbar=hbar
    )

    return {
        "reference_invariance": float(np.max(np.abs(xrefp - x_reference))),
        "hamiltonian_covariance": float(np.max(np.abs(hp - p @ h @ p.T))),
        "energy_invariance": float(abs(energyp - energy)),
        "gradient_covariance": float(np.max(np.abs(
            gradp - transform_edge_field(grad, edge_map)
        ))),
        "geometry_rhs_equivariance": float(np.max(np.abs(
            xdotp - transform_edge_field(xdot, edge_map)
        ))),
        "quantum_rhs_equivariance": float(np.max(np.abs(
            psidot_p - transform_vertex_state(psidot, vertex_map)
        ))),
    }


def rk4_step(x, psi, x_reference, dt, *, stiffness=1.0, coupling=1.0,
             mobility=1.0, hbar=1.0):
    """One normalized-stage RK4 step on the MQM-1 unit-state manifold."""
    def normalize(state):
        norm = np.linalg.norm(state)
        if not np.isfinite(norm) or norm == 0.0:
            raise ValueError("intermediate quantum state has invalid norm")
        return state / norm

    def rhs(xx, pp):
        # The exact vector field is tangent to the unit sphere. Normalize
        # Runge-Kutta stage states to satisfy MQM-1's strict input contract.
        return coupled_rhs(
            xx, normalize(pp), x_reference, stiffness=stiffness,
            coupling=coupling, mobility=mobility, hbar=hbar
        )

    psi = normalize(np.asarray(psi, dtype=complex))
    k1x, k1p = rhs(x, psi)
    k2x, k2p = rhs(x + 0.5 * dt * k1x, normalize(psi + 0.5 * dt * k1p))
    k3x, k3p = rhs(x + 0.5 * dt * k2x, normalize(psi + 0.5 * dt * k2p))
    k4x, k4p = rhs(x + dt * k3x, normalize(psi + dt * k3p))
    x_next = x + (dt / 6.0) * (k1x + 2*k2x + 2*k3x + k4x)
    psi_next = psi + (dt / 6.0) * (k1p + 2*k2p + 2*k3p + k4p)
    return x_next, normalize(psi_next)


def integrate_rk4(x, psi, x_reference, *, steps, dt, stiffness=1.0,
                  coupling=1.0, mobility=1.0, hbar=1.0):
    """Small deterministic integrator used only for equivariance regression tests."""
    x = np.asarray(x, dtype=float).copy()
    psi = np.asarray(psi, dtype=complex).copy()
    for _ in range(steps):
        x, psi = rk4_step(
            x, psi, x_reference, dt, stiffness=stiffness, coupling=coupling,
            mobility=mobility, hbar=hbar
        )
    return x, psi
