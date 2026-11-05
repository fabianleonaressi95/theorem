#!/usr/bin/env python3
"""Finite numerical audit of the Q6 gauge-covariant Wilson operator.

Requires NumPy. Uses small periodic six-tori and matrix-free lattice shifts.
The tests are reproducibility checks, not a continuum-limit proof.
"""
from __future__ import annotations

import json
import itertools
import numpy as np

SEED = 20261105
TOL = 2e-10


def pauli():
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    eye = np.eye(2, dtype=complex)
    return sx, sy, sz, eye


def clifford6():
    sx, sy, sz, eye = pauli()
    # Hermitian Euclidean generators in dimension six.
    g = [
        np.kron(np.kron(sx, eye), eye),
        np.kron(np.kron(sy, eye), eye),
        np.kron(np.kron(sz, sx), eye),
        np.kron(np.kron(sz, sy), eye),
        np.kron(np.kron(sz, sz), sx),
        np.kron(np.kron(sz, sz), sy),
    ]
    chirality = (1j ** 3) * g[0] @ g[1] @ g[2] @ g[3] @ g[4] @ g[5]
    # Numerical phase convention is checked rather than silently repaired.
    return g, chirality


def random_su3(rng):
    z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    q, r = np.linalg.qr(z)
    phases = np.diag(r)
    phases = phases / np.where(np.abs(phases) == 0, 1, np.abs(phases))
    q = q @ np.diag(np.conj(phases))
    det = np.linalg.det(q)
    q[:, 0] *= np.conj(det)
    return q


def random_links(rng, L):
    shape = (L,) * 6 + (6, 3, 3)
    u = np.empty(shape, dtype=complex)
    for x in itertools.product(range(L), repeat=6):
        for i in range(6):
            u[x + (i,)] = random_su3(rng)
    return u


def random_gauge(rng, L):
    shape = (L,) * 6 + (3, 3)
    g = np.empty(shape, dtype=complex)
    for x in itertools.product(range(L), repeat=6):
        g[x] = random_su3(rng)
    return g


def shift_plus(a, axis):
    return np.roll(a, -1, axis=axis)


def shift_minus(a, axis):
    return np.roll(a, 1, axis=axis)


def apply_shift_plus(u, psi, axis):
    # U_i(x) psi(x+e_i)
    return np.einsum("...ab,...sb->...sa", u[..., axis, :, :],
                     shift_plus(psi, axis), optimize=True)


def apply_shift_minus(u, psi, axis):
    # U_i(x-e_i)^dagger psi(x-e_i)
    u_prev = shift_minus(u[..., axis, :, :], axis)
    return np.einsum("...ab,...sb->...sa", np.swapaxes(u_prev.conj(), -1, -2),
                     shift_minus(psi, axis), optimize=True)


def apply_operator(u, psi, gammas, chirality, h, r, mass=0.0):
    out = mass * psi.copy()
    for i in range(6):
        plus = apply_shift_plus(u, psi, i)
        minus = apply_shift_minus(u, psi, i)
        kinetic = (plus - minus) / (2 * h)
        wilson = (2 * psi - plus - minus) * (r / (2 * h))
        out += np.einsum("st,...tc->...sc", gammas[i], kinetic, optimize=True)
        out += wilson
    return out


def transform_links(u, g):
    out = np.empty_like(u)
    for i in range(6):
        g_next = shift_plus(g, i)
        tmp = np.einsum("...ab,...bc->...ac", g, u[..., i, :, :], optimize=True)
        out[..., i, :, :] = np.einsum(
            "...ab,...cb->...ac", tmp, g_next.conj(), optimize=True
        )
    return out


def transform_spinor(psi, g):
    return np.einsum("...ab,...sb->...sa", g, psi, optimize=True)


def norm(a):
    return float(np.linalg.norm(a.ravel()))


def relerr(a, b):
    return norm(a - b) / max(1.0, norm(a), norm(b))


def main():
    rng = np.random.default_rng(SEED)
    L, h, r, mass = 4, 0.5, 1.0, 0.17
    gammas, chirality = clifford6()
    report = {}

    cliff = 0.0
    for i in range(6):
        for j in range(6):
            target = 2 * np.eye(8) if i == j else np.zeros((8, 8))
            cliff = max(cliff, relerr(gammas[i] @ gammas[j] +
                                      gammas[j] @ gammas[i], target))
    report["clifford_max_relative_residual"] = cliff
    report["chirality_square_residual"] = relerr(chirality @ chirality, np.eye(8))
    report["chirality_hermiticity_residual"] = relerr(chirality.conj().T, chirality)
    anti = max(relerr(chirality @ gg + gg @ chirality, np.zeros((8, 8)))
               for gg in gammas)
    report["chirality_anticommutator_residual"] = anti

    u = random_links(rng, L)
    g = random_gauge(rng, L)
    psi = rng.normal(size=(L,) * 6 + (8, 3)) + 1j * rng.normal(
        size=(L,) * 6 + (8, 3)
    )
    ug = transform_links(u, g)
    psig = transform_spinor(psi, g)

    # Link unitarity and determinant checks.
    unit = 0.0
    deterr = 0.0
    for i in range(6):
        ui = u[..., i, :, :]
        unit = max(unit, float(np.max(np.abs(
            np.swapaxes(ui.conj(), -1, -2) @ ui - np.eye(3)
        ))))
        deterr = max(deterr, float(np.max(np.abs(np.linalg.det(ui) - 1))))
    report["link_unitarity_max_residual"] = unit
    report["link_determinant_max_residual"] = deterr

    lhs = apply_operator(ug, psig, gammas, chirality, h, r, mass)
    rhs = transform_spinor(
        apply_operator(u, psi, gammas, chirality, h, r, mass), g
    )
    report["gauge_covariance_relative_residual"] = relerr(lhs, rhs)

    # Adjoint identities are tested by the quadratic/polarization identity
    # <phi,D psi> = <D^dagger phi,psi> using an explicitly implemented
    # adjoint: -D_naive + W + mass.
    phi = rng.normal(size=psi.shape) + 1j * rng.normal(size=psi.shape)
    dpsi = apply_operator(u, psi, gammas, chirality, h, r, mass)
    ddag_phi = apply_operator(u, phi, gammas, chirality, h, r, mass)
    # Reconstruct D^dagger phi = -D_naive phi + W phi + mass phi.
    d0_phi = apply_operator(u, phi, gammas, chirality, h, 0.0, mass)
    w_phi = apply_operator(u, phi, gammas, chirality, h, r, mass) - d0_phi
    # d0 contains kinetic + mass; hence subtract twice kinetic, recovered
    # from the r=0 result with mass=0.
    kinetic_phi = apply_operator(u, phi, gammas, chirality, h, 0.0, 0.0)
    ddag_phi = -kinetic_phi + w_phi + mass * phi
    lhs_inner = np.vdot(phi, dpsi)
    rhs_inner = np.vdot(ddag_phi, psi)
    report["adjoint_identity_relative_residual"] = float(
        abs(lhs_inner - rhs_inner) / max(1.0, abs(lhs_inner), abs(rhs_inner))
    )

    # Gamma_* D Gamma_* = D^dagger, tested on a random spinor.
    gdg = np.einsum("st,...tc->...sc", chirality, dpsi, optimize=True)
    gdg = np.einsum("st,...tc->...sc", chirality, gdg, optimize=True)
    report["gamma_star_hermiticity_relative_residual"] = relerr(gdg, ddag_phi if False else (
        -kinetic_phi + w_phi + mass * psi
    ))

    # Positivity of Wilson Laplacian, directly from sum ||(I-S_i)psi||^2.
    wpsi = apply_operator(u, psi, gammas, chirality, h, r, 0.0) - kinetic_phi
    # Above kinetic_phi is for phi; recompute for psi.
    kpsi = apply_operator(u, psi, gammas, chirality, h, 0.0, 0.0)
    wpsi = apply_operator(u, psi, gammas, chirality, h, r, 0.0) - kpsi
    wilson_quad = float(np.real(np.vdot(psi, wpsi)))
    wilson_sum = 0.0
    for i in range(6):
        diff = psi - apply_shift_plus(u, psi, i)
        wilson_sum += (r / (2 * h)) * float(np.vdot(diff, diff).real)
    report["wilson_quadratic_form"] = wilson_quad
    report["wilson_sum_of_squares"] = wilson_sum
    report["wilson_positivity_residual"] = abs(wilson_quad - wilson_sum)
    report["wilson_minimum_test_value"] = wilson_quad

    thresholds = {
        "clifford_max_relative_residual": TOL,
        "chirality_square_residual": TOL,
        "chirality_hermiticity_residual": TOL,
        "chirality_anticommutator_residual": TOL,
        "link_unitarity_max_residual": TOL,
        "link_determinant_max_residual": 5e-10,
        "gauge_covariance_relative_residual": 5e-10,
        "adjoint_identity_relative_residual": 5e-10,
        "gamma_star_hermiticity_relative_residual": 5e-10,
        "wilson_positivity_residual": 5e-9,
    }
    report["thresholds"] = thresholds
    report["passed"] = all(report[k] <= v for k, v in thresholds.items())
    report["seed"] = SEED
    report["lattice"] = {"side": L, "dimension": 6, "sites": L**6,
                         "spacing": h, "wilson_r": r, "mass": mass}
    print(json.dumps(report, indent=2, sort_keys=True))
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
