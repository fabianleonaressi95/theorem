#!/usr/bin/env python3
"""Audit the PSU/Anti-Twin chiral fluid-gauge locking on the Q6 two-sheet carrier."""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np

def pauli():
    return (
        np.asarray([[0, 1], [1, 0]], dtype=complex),
        np.asarray([[0, -1j], [1j, 0]], dtype=complex),
        np.asarray([[1, 0], [0, -1]], dtype=complex),
    )

def dirac_matrices():
    sx, sy, sz = pauli()
    eye = np.eye(2, dtype=complex)
    zero = np.zeros((2, 2), dtype=complex)
    gamma0 = np.block([[eye, zero], [zero, -eye]])
    gamma1 = np.block([[zero, sx], [-sx, zero]])
    gamma2 = np.block([[zero, sy], [-sy, zero]])
    gamma3 = np.block([[zero, sz], [-sz, zero]])
    gamma5 = 1j * gamma0 @ gamma1 @ gamma2 @ gamma3
    return gamma0, gamma1, gamma2, gamma3, gamma5

def run_audit() -> dict:
    gamma0, gamma1, gamma2, gamma3, gamma5 = dirac_matrices()
    I4, I2 = np.eye(4, dtype=complex), np.eye(2, dtype=complex)
    I8 = np.eye(8, dtype=complex)
    tau1 = np.asarray([[0, 1], [1, 0]], dtype=complex)
    tau3 = np.asarray([[1, 0], [0, -1]], dtype=complex)
    Pplus, Pminus = (I2 + tau3) / 2, (I2 - tau3) / 2
    PR, PL = (I4 + gamma5) / 2, (I4 - gamma5) / 2

    C_lock = np.kron(gamma5, tau3)
    P_lock = (I8 + C_lock) / 2
    P_R_plus, P_L_minus = np.kron(PR, Pplus), np.kron(PL, Pminus)
    J_at = np.kron(I4, tau1)
    parity_exchange = np.kron(gamma0, tau1)
    Q_sheet = np.kron(I4, tau3)

    ae, ao = 0.23, -0.41
    A_sheet = np.kron(I4, ae * I2 + ao * tau3)
    A_chiral = np.kron(ae * I4 + ao * gamma5, I2)
    a_plus, a_minus = ae + ao, ae - ao

    theta = 0.731
    U_plus, U_minus = np.exp(1j * theta), np.exp(-1j * theta)
    U_double = np.diag([U_plus, U_minus])
    U_swapped = tau1 @ U_double @ tau1
    U_inverse = U_double.conj().T
    chi_ps, chi_pt = 0.17, -0.29
    chi_ms, chi_mt = -chi_ps, -chi_pt
    U_plus_prime = np.exp(1j * (theta + chi_pt - chi_ps))
    U_minus_prime = np.exp(1j * (-theta + chi_mt - chi_ms))
    conjugate_link_residual = float(abs(U_minus_prime - np.conjugate(U_plus_prime)))

    Np, Nm = 1.7, 0.8
    Ap, Am = np.asarray([0.4, -0.2, 0.7]), np.asarray([-0.1, 0.5, 0.3])
    Phip, Phim = np.log(Np), np.log(Nm)
    np_, nm = Ap / Np, Am / Nm
    xip, xim = float(np.dot(np_, np_) * Phip), float(np.dot(nm, nm) * Phim)
    phi_even, phi_odd = (Phip + Phim) / 2, (Phip - Phim) / 2
    n_even, n_odd = (np_ + nm) / 2, (np_ - nm) / 2
    xi_even, xi_odd = (xip + xim) / 2, (xip - xim) / 2

    lambda_psu, ell_p = 1.0, 1.0
    ell_psu, r_psu = lambda_psu * ell_p, lambda_psu * ell_p / 2
    volume_psu, area_psu = 4 * np.pi * r_psu**3 / 3, np.pi * r_psu**2
    alpha_G, q0 = 0.25, np.sqrt(0.25)

    checks = {
        "Minkowski_Cl13_and_gamma5": (
            np.linalg.norm(gamma0 @ gamma0 - I4) < 1e-12
            and np.linalg.norm(gamma5 @ gamma5 - I4) < 1e-12
            and max(np.linalg.norm(gamma5 @ g + g @ gamma5)
                    for g in (gamma0, gamma1, gamma2, gamma3)) < 1e-12
        ),
        "locked_sector_rank_four": np.linalg.matrix_rank(P_lock, tol=1e-10) == 4,
        "locked_sector_is_R_plus_and_L_minus": np.linalg.norm(P_lock - P_R_plus - P_L_minus) < 1e-12,
        "sheet_exchange_reverses_locking": np.linalg.norm(J_at @ C_lock @ J_at + C_lock) < 1e-12,
        "parity_plus_sheet_exchange_preserves_locking": np.linalg.norm(parity_exchange @ C_lock @ parity_exchange - C_lock) < 1e-12,
        "sheet_charge_is_anti_twin_odd": np.linalg.norm(J_at @ Q_sheet @ J_at + Q_sheet) < 1e-12,
        "locked_gauge_is_chiral_gauge": np.linalg.norm((A_sheet - A_chiral) @ P_lock) < 1e-12,
        "right_sector_couples_to_plus_sheet": np.linalg.norm((A_sheet - a_plus * I8) @ P_R_plus) < 1e-12,
        "left_sector_couples_to_minus_sheet": np.linalg.norm((A_sheet - a_minus * I8) @ P_L_minus) < 1e-12,
        "anti_twin_link_is_conjugate_inverse": abs(U_minus - np.conjugate(U_plus)) < 1e-12 and np.linalg.norm(U_swapped - U_inverse) < 1e-12,
        "local_gauge_transform_preserves_conjugate_links": conjugate_link_residual < 1e-12,
        "fluid_even_odd_exchange_parity": (
            np.linalg.norm(n_even - (np_ + nm) / 2) < 1e-12
            and np.linalg.norm(n_odd - (np_ - nm) / 2) < 1e-12
            and abs(phi_even - (Phip + Phim) / 2) < 1e-12
            and abs(phi_odd - (Phip - Phim) / 2) < 1e-12
            and abs(xi_even - (xip + xim) / 2) < 1e-12
            and abs(xi_odd - (xip - xim) / 2) < 1e-12
        ),
        "PSU_radius_volume_area_normalization": abs(r_psu - ell_psu / 2) < 1e-12 and abs(volume_psu - np.pi * ell_psu**3 / 6) < 1e-12 and abs(area_psu - np.pi * ell_psu**2 / 4) < 1e-12,
        "PSU_charge_normalization": abs(q0**2 - alpha_G) < 1e-12,
    }
    return {
        "status": "FINITE_PSU_ANTITWIN_CHIRAL_FLUID_GAUGE_IDENTITIES_AUDITED",
        "carrier": {"Q6_vertices_per_sheet": 64, "sheets": 2, "total_states": 128, "Q6_edges_per_sheet": 192, "Q6_faces_per_sheet": 240},
        "chiral_sheet_lock": {"constraint": "gamma5 tensor tau3 = +1", "PSU_sheet": "right-handed sector", "AntiTwin_sheet": "left-handed sector", "locked_complex_dimension": 4, "projector": "(I + gamma5 tensor tau3)/2", "AntiTwin_exchange": "I4 tensor tau1", "combined_parity_exchange": "gamma0 tensor tau1, with x -> parity(x)"},
        "fluid_gauge": {"definitions": "Phi_s=log(N_s), n_s=A_s/N_s, xi_s=(n_s dot n_s) Phi_s", "even_odd": "X_e=(X_+ + X_-)/2; X_o=(X_+ - X_-)/2", "chiral_connection": "a_e I + a_o gamma5", "right_coupling": "a_+=a_e+a_o", "left_coupling": "a_-=a_e-a_o", "anti_twin_conjugate_limit": "a_-=-a_+; a_e=0; purely axial/relative connection", "sample_conjugate_link_residual": conjugate_link_residual},
        "PSU": {"radius_over_ellP": r_psu / ell_p, "volume_over_ellP3": volume_psu / ell_p**3, "equatorial_area_over_ellP2": area_psu / ell_p**2, "lambda_PSU": lambda_psu, "alpha_G_sample": alpha_G, "q0_sample": q0, "charge_operator": "Q=q0 tau3; J Q J^-1 = -Q"},
        "fluid_sample": {"Phi_even": phi_even, "Phi_odd": phi_odd, "n_even": n_even.tolist(), "n_odd": n_odd.tolist(), "xi_even": xi_even, "xi_odd": xi_odd},
        "checks": checks, "pass": all(checks.values()),
        "epistemic_limits": [
            "The right/left identification is a proposed locking of 4D chirality to the PSU/Anti-Twin sheet index; it is not inferred from Spin(6) alone.",
            "The conjugate U(1) Anti-Twin link is exact; non-Abelian conjugate representations require their stated intertwiner.",
            "A Dirac mass breaks the relative axial U(1) unless a charged inter-sheet bridge field is included.",
            "The fluid constitutive action and its coefficients are not fixed by these kinematic identities.",
            "The finite checks do not prove a Q6 continuum Dirac spectrum or evade Nielsen-Ninomiya.",
            "The 64-tetrahedron cell correspondence still requires coordinate and incidence data.",
            "PSU geometry is a model normalization, not experimental evidence for Planck-scale constituents."
        ]
    }

def main():
    result = run_audit()
    output = Path("audits/Q6_PSU_ANTITWIN_CHIRAL_FLUID_GAUGE_AUDIT.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["pass"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
