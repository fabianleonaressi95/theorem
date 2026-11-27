#!/usr/bin/env python3
"""Finite-width developable Mobius-strip BVP benchmark for T156.

Implements the 15-dimensional boundary-value system of Starostin & van der
Heijden (2015), Eqs. (23)--(29), on the symmetric half-strip [0, L/2].
The switching point is regularized by prescribing kappa(L/2)=kappa_floor,
following their continuation strategy (they report values down to about
1e-3 rather than imposing the singular endpoint directly).

The Vesica-to-width map is explicitly a candidate modelling choice:
    L := perimeter of the Vesica lens = 4 R arccos(chi)
    w := half-height of the lens = R sqrt(1-chi**2).
At chi=1/2 and after scaling L=2*pi this gives w=3 sqrt(3)/4.
It is NOT a theorem that a lens boundary is the material centreline.

Run:
    python scripts/solve_t156_mobius_elastic_bvp.py
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import solve_bvp


L = 2.0 * math.pi
HALF_L = math.pi
CHI = 0.5
KAPPA_FLOORS = (5e-2, 2e-2, 1e-2, 5e-3)
EDGE_MARGIN = 1e-4
WIDTH_CONTINUATION = (1.0, 1.15)


def vesica_width_from_perimeter_map(chi: float = CHI) -> dict[str, float]:
    if not 0.0 < chi < 1.0:
        raise ValueError("chi must lie in (0,1)")
    b_over_r = math.sqrt(1.0 - chi * chi)
    perimeter_over_r = 4.0 * math.acos(chi)
    aspect = perimeter_over_r / (2.0 * b_over_r)
    # Rescale the perimeter to L=2*pi; w/L=b/P.
    w_scaled = L * b_over_r / perimeter_over_r
    return {
        "chi": chi,
        "b_over_R": b_over_r,
        "perimeter_over_R": perimeter_over_r,
        "w_over_L": b_over_r / perimeter_over_r,
        "L_over_2w": aspect,
        "w_when_L_2pi": w_scaled,
    }


def _v_and_derivatives(eta_prime: np.ndarray, width: float):
    """Return V, dV/d(eta'), d2V/d(eta')2 for V=atanh(z)/z, z=w*eta'."""
    z = width * eta_prime
    if np.any(np.abs(z) >= 1.0):
        raise ValueError("developable-strip edge singularity: |w eta'| >= 1")
    V = np.empty_like(z, dtype=float)
    Vp = np.empty_like(z, dtype=float)
    Vpp = np.empty_like(z, dtype=float)
    small = np.abs(z) < 1e-3
    zs = z[small]
    V[small] = 1.0 + zs**2/3.0 + zs**4/5.0 + zs**6/7.0 + zs**8/9.0
    Vz = 2.0*zs/3.0 + 4.0*zs**3/5.0 + 6.0*zs**5/7.0 + 8.0*zs**7/9.0
    Vzz = 2.0/3.0 + 12.0*zs**2/5.0 + 30.0*zs**4/7.0 + 56.0*zs**6/9.0
    Vp[small] = width * Vz
    Vpp[small] = width**2 * Vzz
    large = ~small
    zl = z[large]
    atanh = np.arctanh(zl)
    numerator = zl/(1.0-zl**2) - atanh
    V[large] = atanh/zl
    Vz_l = numerator/zl**2
    Vzz_l = 2.0/(1.0-zl**2)**2 - 2.0*numerator/zl**3
    Vp[large] = width * Vz_l
    Vpp[large] = width**2 * Vzz_l
    return V, Vp, Vpp


def wunderlich_coefficients(eta_prime: np.ndarray, width: float):
    V, Vp, Vpp = _v_and_derivatives(eta_prime, width)
    a1 = 0.25 * (2.0*Vp**2 - V*Vpp)
    a2 = V + eta_prime*Vp
    a3 = V*a2
    a4 = Vp
    b2 = 0.5 * (eta_prime*(Vp**2 - V*Vpp) - V*Vp)
    b3 = 0.5 * (2.0*Vp + eta_prime*Vpp)
    b4 = 0.5 * Vpp
    return a1, a2, a3, a4, b2, b3, b4, V


def rhs(s: np.ndarray, y: np.ndarray, width: float) -> np.ndarray:
    """Starostin–van der Heijden Eqs. (23)--(29), with q=atanh(w eta')."""
    F1, F2, F3, M1, M2, M3 = y[0:6]
    kappa, eta, q = y[6], y[7], y[8]
    psi, theta, phi = y[9], y[10], y[11]
    del s
    exp_tail = np.exp(-2.0*np.minimum(np.abs(q), 350.0))
    tanh_q = np.sign(q)*(1.0-exp_tail)/(1.0+exp_tail)
    sech2_q = 4.0*exp_tail/(1.0+exp_tail)**2
    zeta = (1.0-EDGE_MARGIN)*tanh_q
    eta_prime = zeta / width
    a1, a2, a3, a4, b2, b3, b4, _ = wunderlich_coefficients(eta_prime, width)
    one_eta2 = 1.0 + eta**2
    denom_k = 4.0*a1*one_eta2**2
    denom_eta = denom_k*kappa
    if np.any(np.abs(denom_k) < 1e-14) or np.any(np.abs(denom_eta) < 1e-14):
        raise FloatingPointError("singular coefficient in the developable-strip BVP")
    kappa_prime = (
        -b3*M1 + b4*F2 - 8.0*b2*kappa*eta*one_eta2
    ) / denom_k
    eta_second = (
        a2*M1 - a4*F2 - 4.0*a3*kappa*eta*one_eta2
    ) / denom_eta
    q_prime = width*eta_second/((1.0-EDGE_MARGIN)*sech2_q)
    sin_theta = np.sin(theta)
    if np.any(np.abs(sin_theta) < 1e-8):
        raise FloatingPointError("Euler-angle chart singularity: sin(theta) is too small")
    cot_theta = np.cos(theta)/sin_theta
    out = np.zeros_like(y)
    out[0] = kappa*F2
    out[1] = -kappa*F1 + kappa*eta*F3
    out[2] = -kappa*eta*F2
    out[3] = kappa*M2
    out[4] = -kappa*M1 + kappa*eta*M3 + F3
    out[5] = -kappa*eta*M2 - F2
    out[6] = kappa_prime
    out[7] = eta_prime
    out[8] = q_prime
    out[9] = kappa*np.sin(phi)/sin_theta
    out[10] = kappa*np.cos(phi)
    out[11] = kappa*(eta - np.sin(phi)*cot_theta)
    out[12] = sin_theta*np.cos(psi)
    out[13] = sin_theta*np.sin(psi)
    out[14] = np.cos(theta)
    return out


def boundary_conditions(ya: np.ndarray, yb: np.ndarray, kappa_floor: float):
    # Conditions (30)--(39) of the symmetric Mobius BVP, plus Eq. (21) at s=0.
    eta0 = ya[7]
    kappa0 = ya[6]
    return np.array([
        ya[1],                              # F_2(0)=0
        ya[4],                              # M_2(0)=0
        yb[6] - kappa_floor,                # regularized kappa(L/2)
        ya[8],                              # eta'(0)=0 <=> q(0)=0
        ya[9] - math.pi,                    # psi(0)=pi
        yb[9] - 2.0*math.pi,                # psi(L/2)=2pi
        yb[10] - math.pi/2.0,               # theta(L/2)=pi/2
        ya[11] - math.pi/2.0,               # phi(0)=pi/2
        yb[11] - math.pi,                   # phi(L/2)=pi
        ya[12],                             # x(0)=0
        yb[12],                             # x(L/2)=0
        ya[13],                             # y(0)=0
        ya[14],                             # z(0)=0
        yb[14],                             # z(L/2)=0
        ya[5] + eta0*ya[3] + 2.0*kappa0*(1.0+eta0**2)**2,
    ])


def initial_guess(width: float, kappa_floor: float, mesh: np.ndarray) -> np.ndarray:
    eta0 = 1.8/width
    kappa = 0.20 + 0.30*np.sin(mesh) + (kappa_floor-0.20)*mesh/HALF_L
    eta = eta0*np.cos(mesh/2.0)
    q = np.arctanh(-0.90*np.sin(mesh/2.0))
    y = np.zeros((15, mesh.size))
    y[0] = 0.0
    y[1] = 0.0
    y[2] = 0.0
    y[3] = 0.0
    y[4] = 0.0
    y[5] = -2.0*kappa[0]*(1.0+eta[0]**2)**2
    y[6] = kappa
    y[7] = eta
    y[8] = q
    y[9] = math.pi + mesh
    y[10] = math.pi/2.0
    y[11] = math.pi/2.0 + mesh/2.0
    y[12] = -np.sin(mesh)
    y[13] = np.cos(mesh)-1.0
    y[14] = 0.0
    return y


def solve_width(width: float, seed=None, previous_width=None):
    mesh = np.linspace(0.0, HALF_L, 80)
    if seed is None:
        y_guess = initial_guess(width, KAPPA_FLOORS[0], mesh)
    else:
        mesh = seed.x.copy()
        y_guess = seed.y.copy()
        if previous_width is not None:
            y_guess[7] *= previous_width/width
    solution = None
    attempts = []
    for floor in KAPPA_FLOORS:
        if solution is None and seed is None:
            y_guess = initial_guess(width, floor, mesh)
        elif solution is not None:
            y_guess = solution.y.copy()
            y_guess[6] += floor - previous_floor
        try:
            result = solve_bvp(
                lambda s, y: rhs(s, y, width),
                lambda ya, yb: boundary_conditions(ya, yb, floor),
                mesh,
                y_guess,
                tol=2e-3,
                max_nodes=12000,
                verbose=0,
            )
        except Exception as exc:
            attempts.append({
                "kappa_floor": floor,
                "success": False,
                "status": -1,
                "message": f"{type(exc).__name__}: {exc}",
                "nodes": int(mesh.size),
                "max_rms_residual": None,
            })
            return None, attempts
        attempts.append({
            "kappa_floor": floor,
            "success": bool(result.success),
            "status": int(result.status),
            "message": str(result.message),
            "nodes": int(result.x.size),
            "max_rms_residual": float(np.max(result.rms_residuals)) if result.rms_residuals.size else None,
        })
        if not result.success:
            return None, attempts
        solution = result
        mesh = result.x
        y_guess = result.y
        previous_floor = floor
    return solution, attempts


def summarize(solution, width: float, attempts: list[dict]) -> dict:
    s = solution.x
    y = solution.y
    F1, F2, F3, M1, M2, M3 = y[0:6]
    kappa, eta, q = y[6], y[7], y[8]
    exp_tail = np.exp(-2.0*np.minimum(np.abs(q), 350.0))
    tanh_q = np.sign(q)*(1.0-exp_tail)/(1.0+exp_tail)
    zeta = (1.0-EDGE_MARGIN)*tanh_q
    eta_prime = zeta/width
    _, _, _, _, _, _, _, V = wunderlich_coefficients(eta_prime, width)
    density = kappa**2*(1.0+eta**2)**2*V
    energy = float(np.trapezoid(density, s))
    force_norm_sq = F1**2+F2**2+F3**2
    force_dot_moment = F1*M1+F2*M2+F3*M3
    hamiltonian = (
        kappa*(M1*eta+M3)
        + kappa**2*(1.0+eta**2)**2*(1.0/(1.0-zeta**2)-2.0*V)
        + F1
    )
    def relative_spread(values):
        scale = max(float(np.max(np.abs(values))), 1e-12)
        return float((np.max(values)-np.min(values))/scale)
    bc = boundary_conditions(y[:, 0], y[:, -1], KAPPA_FLOORS[-1])
    torsion = eta*kappa
    return {
        "width": width,
        "aspect_ratio_L_over_2w": L/(2.0*width),
        "kappa_floor": KAPPA_FLOORS[-1],
        "solver_success": bool(solution.success),
        "solver_message": str(solution.message),
        "mesh_nodes": int(s.size),
        "max_rms_collocation_residual": float(np.max(solution.rms_residuals)),
        "max_abs_w_eta_prime": float(np.max(np.abs(zeta))),
        "edge_singularity_margin": EDGE_MARGIN,
        "minimum_kappa": float(np.min(kappa)),
        "endpoint_eta": float(eta[-1]),
        "endpoint_torsion": float(torsion[-1]),
        "normalized_wunderlich_energy_half_strip": energy,
        "force_norm_squared_relative_spread": relative_spread(force_norm_sq),
        "force_dot_moment_relative_spread": relative_spread(force_dot_moment),
        "hamiltonian_relative_spread": relative_spread(hamiltonian),
        "boundary_residual_max": float(np.max(np.abs(bc))),
        "switching_point_regularized_at_half_interval": True,
        "linking_number_selected_by_mobius_bvp_boundary_class": 0.5,
        "linking_number_independently_reconstructed": False,
        "continuation_attempts": attempts,
    }


def run():
    vesica = vesica_width_from_perimeter_map(CHI)
    target_width = vesica["w_when_L_2pi"]
    widths = list(WIDTH_CONTINUATION) + [target_width]
    seed = None
    previous_width = None
    width_reports = []
    target_solution = None
    target_attempts = []
    for width in widths:
        solution, attempts = solve_width(width, seed=seed, previous_width=previous_width)
        width_reports.append({
            "width": width,
            "attempts": attempts,
            "success": solution is not None,
        })
        if solution is None:
            report = {
                "record": "T156",
                "status": "BVP_FAILED",
                "vesica_candidate_map": vesica,
                "width_continuation": width_reports,
                "scientific_limit": (
                    "No elastic equilibrium is claimed. The solve_bvp attempt did not "
                    "converge under the documented continuation/regularization."
                ),
            }
            return report, 2
        seed = solution
        previous_width = width
        target_solution = solution
        target_attempts = attempts
    report = {
        "record": "T156",
        "status": "BVP_CONVERGED_REGULARIZED",
        "source_model": "Starostin–van der Heijden 2015, Eqs. (23)–(29), symmetric Mobius BVP",
        "vesica_candidate_map": vesica,
        "target_solution": summarize(target_solution, target_width, target_attempts),
        "width_continuation": width_reports,
        "scientific_limit": (
            "Finite-width symmetric BVP solved only with kappa(L/2)>0 regularization. "
            "The exact singular switching-point limit, independent linking-number "
            "reconstruction, and selection of this width by Vesica physics remain open."
        ),
    }
    return report, 0


if __name__ == "__main__":
    report, code = run()
    output = Path("results/t156_mobius_elastic_bvp.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    raise SystemExit(code)
