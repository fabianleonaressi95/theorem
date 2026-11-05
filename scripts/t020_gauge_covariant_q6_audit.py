#!/usr/bin/env python3
"""Finite-lattice T020 audit with genuinely non-Abelian SU(3) links.

Dependencies: numpy only.
Run: python scripts/t020_gauge_covariant_q6_audit.py --n 2 3
The diagnostics are finite-dimensional numerical evidence, not a continuum proof.
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

# Hermitian, traceless Gell-Mann generators. Distinct directions use
# generators which do not all commute.
def gell_mann():
    z = np.zeros((3, 3), complex)
    mats = []
    a = z.copy(); a[0,1]=a[1,0]=1; mats.append(a)                 # lambda_1
    a = z.copy(); a[0,1]=-1j; a[1,0]=1j; mats.append(a)          # lambda_2
    a = z.copy(); a[0,0]=1; a[1,1]=-1; mats.append(a)            # lambda_3
    a = z.copy(); a[0,2]=a[2,0]=1; mats.append(a)                # lambda_4
    a = z.copy(); a[0,2]=-1j; a[2,0]=1j; mats.append(a)          # lambda_5
    a = z.copy(); a[1,2]=a[2,1]=1; mats.append(a)                # lambda_6
    a = z.copy(); a[1,2]=-1j; a[2,1]=1j; mats.append(a)          # lambda_7
    a = np.diag([1,-1,0]).astype(complex); mats.append(a)        # lambda_3
    a = np.diag([1,1,-2]).astype(complex)/np.sqrt(3); mats.append(a) # lambda_8
    return mats

LAM = gell_mann()
LINK_GENERATORS = [LAM[i] for i in [0,3,5,1,4,6]]

def gamma_apply(g, psi):
    return np.einsum("ab,...bc->...ac", g, psi, optimize=True)

def color_apply(u, psi):
    return np.einsum("...ab,...sb->...sa", u, psi, optimize=True)

def su3_exp_generator(generator, angle):
    """exp(i*angle*generator), with a fixed Hermitian generator."""
    vals, vecs = np.linalg.eigh(generator)
    phases = np.exp(1j * np.asarray(angle)[..., None] * vals)
    return (vecs * phases[..., None, :]) @ vecs.conj().T

def build_fields(n, alpha):
    L, h = 2*n, 1.0/n
    axes = [h*(np.arange(L)+0.5) for _ in range(6)]
    mesh = np.meshgrid(*axes, indexing="ij")
    links, hfields = [], []
    for i, generator in enumerate(LINK_GENERATORS):
        # Midpoint evaluation of a smooth periodic Hermitian su(3) potential.
        mid = [mesh[j] + (h/2 if j == i else 0.0) for j in range(6)]
        f = alpha * (
            np.sin(np.pi*mid[(i+1) % 6])
            + 0.31*np.cos(np.pi*mid[(i+2) % 6])
        )
        links.append(su3_exp_generator(generator, h*f))
        hfields.append(alpha * (
            np.sin(np.pi*mesh[(i+1) % 6])
            + 0.31*np.cos(np.pi*mesh[(i+2) % 6])
        )[..., None, None] * generator)
    return h, mesh, links, hfields

def apply_operator(psi, links, h, r, m0):
    out = m0*psi.copy()
    wilson_out = np.zeros_like(psi)
    q = 0.0
    for i, (gamma, u) in enumerate(zip(GAMMA, links)):
        psi_f = np.roll(psi, -1, axis=i)
        fwd = color_apply(u, psi_f)
        u_prev = np.roll(u, 1, axis=i)
        psi_prev = np.roll(psi, 1, axis=i)
        back = color_apply(u_prev.conj().swapaxes(-1,-2), psi_prev)
        out += gamma_apply(gamma, fwd-back)/(2*h)
        wterm = r*(2*psi-fwd-back)/(2*h)
        out += wterm
        wilson_out += wterm
        q += float(np.linalg.norm((psi-fwd).ravel())**2)*r/(2*h)
    q_operator_complex = np.vdot(psi, wilson_out)
    q_identity_residual = abs(q_operator_complex.real-q)/max(abs(q),1e-30)
    q_imaginary_residual = abs(q_operator_complex.imag)/max(abs(q),1e-30)
    return out, q, q_identity_residual, q_imaginary_residual

def gauge_transform(links, mesh, eps=0.23):
    # Product of three site-dependent SU(3) rotations about noncommuting
    # generators: this is not confined to a common Cartan subgroup.
    f1 = eps*np.sin(np.pi*mesh[0])
    f2 = eps*np.cos(np.pi*mesh[1])
    f3 = 0.7*eps*np.sin(np.pi*(mesh[2]+mesh[4]))
    g = (su3_exp_generator(LAM[1], f1)
         @ su3_exp_generator(LAM[4], f2)
         @ su3_exp_generator(LAM[6], f3))
    transformed = []
    for i, u in enumerate(links):
        gf = np.roll(g, -1, axis=i)
        transformed.append(g @ u @ gf.conj().swapaxes(-1,-2))
    return g, transformed

def relative(a, b):
    return float(np.linalg.norm((a-b).ravel()) /
                 max(np.linalg.norm(b.ravel()), 1e-30))

def one_level(n, alpha, r, m0):
    h, mesh, links, hfields = build_fields(n, alpha)
    centres = mesh
    phase = np.exp(1j*np.pi*sum(centres))
    spin = np.zeros(8, complex); spin[0] = 1.0
    colour = np.array([1.0, 0.3j, 0.2], complex)
    colour /= np.linalg.norm(colour)
    phi = (phase[..., None, None]
           * spin.reshape((1,)*6 + (8, 1))
           * colour.reshape((1,)*6 + (1, 3)))
    discrete, wilson_q, wilson_identity_residual, wilson_imaginary_residual = apply_operator(phi, links, h, r, m0)

    # Continuum covariant derivative: nabla_i = partial_i + i H_i(x).
    continuum = m0*phi.copy()
    for i, gamma in enumerate(GAMMA):
        dphi = 1j*np.pi*phi
        gauge_phi = 1j*color_apply(hfields[i], phi)
        continuum += gamma_apply(gamma, dphi + gauge_phi)
    consistency = relative(discrete, continuum)

    # Exact lattice covariance for arbitrary sitewise g(x):
    # U_i^g(x)=g(x) U_i(x) g(x+e_i)^dagger.
    g, links_g = gauge_transform(links, mesh)
    phi_g = color_apply(g, phi)
    lhs, _, _, _ = apply_operator(phi_g, links_g, h, r, m0)
    rhs0, _, _, _ = apply_operator(phi, links, h, r, m0)
    rhs = color_apply(g, rhs0)
    covariance = relative(lhs, rhs)

    # Unitarity, determinant-one and genuinely noncommuting diagnostics.
    unitary_res = max(
        float(np.max(np.linalg.norm((u.conj().swapaxes(-1,-2) @ u
                                    - np.eye(3)).reshape((-1,9)), axis=1)))
        for u in links
    )
    det_res = max(float(np.max(np.abs(np.linalg.det(u)-1))) for u in links)
    commutator_norm = float(np.linalg.norm(
        LINK_GENERATORS[0]@LINK_GENERATORS[1]
        - LINK_GENERATORS[1]@LINK_GENERATORS[0]
    ))
    link_commutator_norm = float(np.linalg.norm(
        links[0][(0,)*6]@links[1][(0,)*6]
        - links[1][(0,)*6]@links[0][(0,)*6]
    ))
    gauge_unitarity_res = float(np.max(np.linalg.norm(
        (g.conj().swapaxes(-1,-2)@g-np.eye(3)).reshape((-1,9)), axis=1
    )))
    gauge_det_res = float(np.max(np.abs(np.linalg.det(g)-1)))

    gamma_res = max(
        float(np.linalg.norm(GAMMA[i]@GAMMA[j]+GAMMA[j]@GAMMA[i]
                             -2*(i==j)*np.eye(8)))
        for i in range(6) for j in range(6)
    )
    return {
        "n": n, "h": h, "consistency_error": consistency,
        "wilson_quadratic_form": wilson_q,
        "wilson_nonnegative": bool(wilson_q >= -1e-12),
        "wilson_identity_relative_residual": wilson_identity_residual,
        "wilson_imaginary_form_relative_residual": wilson_imaginary_residual,
        "gauge_covariance_relative_residual": covariance,
        "link_unitarity_max_residual": unitary_res,
        "link_det_one_max_residual": det_res,
        "nonabelian_generator_commutator_norm": commutator_norm,
        "nonabelian_link_commutator_norm_at_origin": link_commutator_norm,
        "gauge_transform_unitarity_max_residual": gauge_unitarity_res,
        "gauge_transform_det_one_max_residual": gauge_det_res,
        "clifford_relations_max_residual": gamma_res,
    }

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--n", nargs="+", type=int, default=[2,3])
    p.add_argument("--alpha", type=float, default=0.35)
    p.add_argument("--r", type=float, default=1.0)
    p.add_argument("--m0", type=float, default=0.2)
    args = p.parse_args()
    if any(n < 2 for n in args.n):
        p.error("all n must be >= 2")
    rows = [one_level(n, args.alpha, args.r, args.m0) for n in args.n]
    for j, row in enumerate(rows):
        row["observed_order_vs_previous"] = (
            None if j == 0 else
            math.log(rows[j-1]["consistency_error"]/row["consistency_error"])
            / math.log(rows[j-1]["h"]/row["h"])
        )
    print(json.dumps({
        "audit": "T020 genuinely non-Abelian SU(3) link-field audit",
        "parameters": {"alpha": args.alpha, "r": args.r, "m0": args.m0,
                       "n": args.n},
        "results": rows,
        "interpretation": (
            "Finite-dimensional numerical diagnostics only. Exact covariance "
            "is tested for full SU(3) matrix links and noncommuting site gauge "
            "rotations; refinement data do not prove hypothesis (C), "
            "strong-resolvent convergence, or an interacting continuum limit."
        )
    }, indent=2))

if __name__ == "__main__":
    main()
