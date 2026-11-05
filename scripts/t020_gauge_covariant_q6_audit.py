#!/usr/bin/env python3
"""Reproducible finite-lattice audit for T020.

Dependencies: numpy only.
Run: python scripts/t020_gauge_covariant_q6_audit.py --n 2 3 4
The program reports measurements; it does not prove the continuum theorem.
"""
from __future__ import annotations
import argparse
import json
import math
import numpy as np

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
def kron3(a, b, c):
    return np.kron(np.kron(a, b), c)
GAMMA = [
    kron3(X, I2, I2), kron3(Y, I2, I2),
    kron3(Z, X, I2), kron3(Z, Y, I2),
    kron3(Z, Z, X), kron3(Z, Z, Y),
]
T3 = np.diag([0.5, -0.5, 0.0]).astype(complex)

def gamma_apply(g, psi):
    return np.einsum("ab,...bc->...ac", g, psi, optimize=True)

def build_fields(n, alpha):
    L, h = 2*n, 1.0/n
    axes = [h*np.arange(L) for _ in range(6)]
    mesh = np.meshgrid(*axes, indexing="ij")
    # A_1 is independent of x_1, so the edge integral is exact.
    phase = alpha*np.sin(np.pi*mesh[1])
    u1 = np.exp(1j*h*phase[..., None]*np.array([0.5, -0.5, 0.0]))
    links = [u1] + [np.ones((L,)*6+(3,), dtype=complex) for _ in range(5)]
    return h, mesh, links

def apply_operator(psi, links, h, r, m0):
    out = m0*psi.copy()
    wilson_q = 0.0
    for i, (gamma, u) in enumerate(zip(GAMMA, links)):
        fwd = np.roll(psi, -1, axis=i) * u[..., None, :]
        back = np.roll(psi*np.conjugate(u)[..., None, :], 1, axis=i)
        out += gamma_apply(gamma, fwd-back)/(2*h)
        out += r*(2*psi-fwd-back)/(2*h)
        wilson_q += float(np.vdot(psi, 2*psi-fwd-back).real)
    return out, wilson_q*r/(2*h)

def gauge_transform(links, mesh, eps=0.23):
    # A smooth, nonconstant SU(3) map, diagonal in the same Cartan generator.
    angle = eps*np.cos(np.pi*mesh[2])
    g = np.exp(1j*angle[..., None]*np.array([0.5, -0.5, 0.0]))
    transformed = []
    for i, u in enumerate(links):
        g_forward = np.roll(g, -1, axis=i)
        transformed.append(g*u*np.conjugate(g_forward))
    return g, transformed

def relative(a, b):
    return float(np.linalg.norm((a-b).ravel()) /
                 max(np.linalg.norm(b.ravel()), 1e-30))

def one_level(n, alpha, r, m0):
    h, mesh, links = build_fields(n, alpha)
    L = 2*n
    # Cell-centre samples; smooth periodic plane wave and fixed spin-colour vector.
    centres = [x + h/2 for x in mesh]
    phase = np.exp(1j*np.pi*sum(centres))
    spin = np.zeros(8, complex); spin[0] = 1.0
    colour = np.array([1.0, 0.3j, 0.2], complex)
    colour /= np.linalg.norm(colour)
    phi = (phase[..., None, None]
           * spin.reshape((1,)*6 + (8, 1))
           * colour.reshape((1,)*6 + (1, 3)))
    discrete, wilson_q = apply_operator(phi, links, h, r, m0)

    # Continuum action on this section: partial_i phi = i*pi*phi.
    continuum = m0*phi.copy()
    for gamma in GAMMA:
        continuum += gamma_apply(gamma, 1j*np.pi*phi)
    a1 = 1j*alpha*np.sin(np.pi*centres[1])[..., None]*np.array([0.5,-0.5,0.0])
    continuum += gamma_apply(GAMMA[0], phi*a1[..., None, :])
    consistency = relative(discrete, continuum)

    # Exact covariance test for a nonconstant sitewise gauge transform.
    g, links_g = gauge_transform(links, mesh)
    lhs, _ = apply_operator(phi*g[..., None, :], links_g, h, r, m0)
    rhs, _ = apply_operator(phi, links, h, r, m0)
    rhs = rhs*g[..., None, :]
    covariance = relative(lhs, rhs)

    # Direct Wilson quadratic form from the edge differences.
    q_direct = 0.0
    for i, u in enumerate(links):
        fwd = np.roll(phi, -1, axis=i)*u[..., None, :]
        q_direct += float(np.linalg.norm((phi-fwd).ravel())**2)*r/(2*h)
    positivity_residual = abs(wilson_q-q_direct)/max(q_direct, 1e-30)
    return {
        "n": n, "h": h, "consistency_error": consistency,
        "wilson_quadratic_form": q_direct,
        "wilson_nonnegative": bool(q_direct >= -1e-12),
        "wilson_identity_relative_residual": positivity_residual,
        "gauge_covariance_relative_residual": covariance,
        "clifford_relations_max_residual": max(
            float(np.linalg.norm(GAMMA[i]@GAMMA[j]+GAMMA[j]@GAMMA[i]
                                 -2*(i==j)*np.eye(8)))
            for i in range(6) for j in range(6)),
    }

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--n", nargs="+", type=int, default=[2,3,4])
    p.add_argument("--alpha", type=float, default=0.35)
    p.add_argument("--r", type=float, default=1.0)
    p.add_argument("--m0", type=float, default=0.2)
    args = p.parse_args()
    if any(n < 2 for n in args.n):
        p.error("all n must be >= 2")
    rows = [one_level(n, args.alpha, args.r, args.m0) for n in args.n]
    for j, row in enumerate(rows):
        if j:
            row["observed_order_vs_previous"] = (
                math.log(rows[j-1]["consistency_error"]/row["consistency_error"])
                / math.log(rows[j-1]["h"]/row["h"])
            )
        else:
            row["observed_order_vs_previous"] = None
    print(json.dumps({
        "audit": "T020 controlled SU(3) link-field consistency and covariance",
        "parameters": {"alpha": args.alpha, "r": args.r, "m0": args.m0,
                       "n": args.n},
        "results": rows,
        "interpretation": "Numerical diagnostics only; not a proof of (C) or of strong-resolvent convergence."
    }, indent=2))

if __name__ == "__main__":
    main()
