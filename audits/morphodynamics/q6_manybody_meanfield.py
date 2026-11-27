"""Exact two-boson vs Hartree mean-field dynamics on Q6.

The graph geometry is the existing 64-vertex/192-edge Q6. The interaction
is an explicitly declared on-site Bose-Hubbard term. Geometry backreaction
is driven by the one-body density matrix in both descriptions, so the only
comparison is quantum correlation/closure error, not a change of force law.

Finite-dimensional numerical benchmark; not a continuum or physical claim.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
import numpy as np
from scipy.integrate import solve_ivp
from scipy.sparse import coo_matrix, csr_matrix

from audits.morphodynamics.q6_quantum_geometry import q6_incidence


@dataclass(frozen=True)
class Parameters:
    interaction: float = 0.5
    hopping: float = 1.0
    stiffness: float = 2.0
    mobility: float = 0.15
    hbar: float = 1.0


def fock_pairs():
    """Normalized two-boson occupation basis |i,j>, 0 <= i <= j < 64."""
    return tuple((i, j) for i in range(64) for j in range(i, 64))


def one_body_hamiltonian(x, *, hopping=1.0):
    x = np.asarray(x, dtype=float)
    if x.shape != (192,) or not np.all(np.isfinite(x)):
        raise ValueError("x must be a finite vector of length 192")
    if hopping <= 0 or not np.isfinite(hopping):
        raise ValueError("hopping must be finite and positive")
    b = q6_incidence()
    return float(hopping) * (b * np.exp(x)) @ b.T


def two_boson_hamiltonian(h, interaction):
    """Fock-space matrix for dGamma(h) + U/2 sum_v n_v(n_v-1)."""
    h = np.asarray(h, dtype=float)
    if h.shape != (64, 64) or not np.allclose(h, h.T, atol=1e-12):
        raise ValueError("h must be a real symmetric 64x64 matrix")
    if not np.isfinite(interaction):
        raise ValueError("interaction must be finite")
    pairs = fock_pairs()
    lookup = {pair: k for k, pair in enumerate(pairs)}
    rows, cols, vals = [], [], []
    for col, (i, j) in enumerate(pairs):
        occ = np.zeros(64, dtype=int)
        occ[i] += 1
        occ[j] += 1
        if i == j:
            rows.append(col); cols.append(col); vals.append(float(interaction))
        for q in sorted(set((i, j))):
            nq = int(occ[q])
            if nq == 0:
                continue
            for p in np.flatnonzero(np.abs(h[:, q]) > 1e-14):
                np2 = int(occ[p] + (p != q))
                amp = np.sqrt(nq * np2) * h[p, q]
                new_occ = occ.copy()
                new_occ[q] -= 1
                new_occ[p] += 1
                occupied = np.flatnonzero(new_occ)
                dest = tuple(int(v) for v in occupied for _ in range(new_occ[v]))
                rows.append(lookup[dest]); cols.append(col); vals.append(float(amp))
    out = coo_matrix((vals, (rows, cols)), shape=(len(pairs), len(pairs))).tocsr()
    out.sum_duplicates()
    return out


def hartree_fock_state(phi):
    """Map normalized one-particle phi to its normalized N=2 product state."""
    phi = np.asarray(phi, dtype=complex)
    if phi.shape != (64,) or not np.isclose(np.vdot(phi, phi).real, 1.0):
        raise ValueError("phi must be a normalized 64-component state")
    out = np.empty(2080, dtype=complex)
    for k, (i, j) in enumerate(fock_pairs()):
        out[k] = phi[i] * phi[i] if i == j else np.sqrt(2.0) * phi[i] * phi[j]
    return out


def one_body_density(psi):
    """Unnormalized 1-RDM gamma[p,q]=<a_p^dagger a_q>, trace(gamma)=2."""
    psi = np.asarray(psi, dtype=complex)
    if psi.shape != (2080,) or not np.isclose(np.vdot(psi, psi).real, 1.0,
                                               atol=1e-8):
        raise ValueError("psi must be a normalized two-boson Fock state")
    pairs = fock_pairs()
    lookup = {pair: k for k, pair in enumerate(pairs)}
    gamma = np.zeros((64, 64), dtype=complex)
    for col, (i, j) in enumerate(pairs):
        occ = np.zeros(64, dtype=int)
        occ[i] += 1; occ[j] += 1
        for q in sorted(set((i, j))):
            nq = int(occ[q])
            if nq == 0:
                continue
            for p in range(64):
                if p == q:
                    amp = float(nq)
                else:
                    amp = float(np.sqrt(nq * (occ[p] + 1)))
                new_occ = occ.copy()
                new_occ[q] -= 1
                new_occ[p] += 1
                occupied = np.flatnonzero(new_occ)
                dest = tuple(int(v) for v in occupied for _ in range(new_occ[v]))
                row = lookup[dest]
                gamma[p, q] += np.conjugate(psi[row]) * psi[col] * amp
    return 0.5 * (gamma + gamma.conj().T)


def geometry_gradient_from_density(x, gamma, x_reference, *, stiffness=2.0,
                                   hopping=1.0):
    """dE/dx_e = k(x-x*) + t exp(x_e) b_e^T gamma b_e."""
    x = np.asarray(x, dtype=float)
    gamma = np.asarray(gamma, dtype=complex)
    x_reference = np.asarray(x_reference, dtype=float)
    if x.shape != (192,) or x_reference.shape != (192,) or gamma.shape != (64, 64):
        raise ValueError("expected x,x_reference in R^192 and gamma in C^(64x64)")
    b = q6_incidence()
    edge_densities = np.einsum("ve,vw,we->e", b, gamma, b, optimize=True).real
    return stiffness * (x - x_reference) + hopping * np.exp(x) * edge_densities


def _validate_initial(phi, x0, xref):
    phi = np.asarray(phi, dtype=complex)
    x0 = np.asarray(x0, dtype=float)
    xref = np.asarray(xref, dtype=float)
    if phi.shape != (64,) or not np.isclose(np.vdot(phi, phi).real, 1.0):
        raise ValueError("phi must be normalized in C^64")
    if x0.shape != (192,) or xref.shape != (192,):
        raise ValueError("x0 and x_reference must have length 192")
    return phi, x0, xref


def run_comparison(*, phi=None, x0=None, x_reference=None, params=Parameters(),
                   final_time=0.25, samples=26, rtol=2e-8, atol=2e-10):
    """Integrate full N=2 and Hartree closures with the same initial product state."""
    if phi is None:
        phi = np.zeros(64, dtype=complex); phi[0] = 1.0
    if x0 is None:
        x0 = np.zeros(192)
    if x_reference is None:
        x_reference = np.zeros(192)
    phi, x0, xref = _validate_initial(phi, x0, x_reference)
    if final_time <= 0 or samples < 2:
        raise ValueError("final_time must be positive and samples >= 2")

    psi0 = hartree_fock_state(phi)
    y0_full = np.r_[x0.astype(complex), psi0]
    y0_mf = np.r_[x0.astype(complex), phi]
    times = np.linspace(0.0, final_time, samples)

    def full_rhs(_t, y):
        x = y[:192].real
        psi = y[192:]
        h = one_body_hamiltonian(x, hopping=params.hopping)
        H2 = two_boson_hamiltonian(h, params.interaction)
        gamma = one_body_density(psi)
        gx = geometry_gradient_from_density(
            x, gamma, xref, stiffness=params.stiffness, hopping=params.hopping
        )
        return np.r_[-params.mobility * gx,
                     -1j * (H2 @ psi) / params.hbar]

    def mf_rhs(_t, y):
        x = y[:192].real
        z = y[192:]
        h = one_body_hamiltonian(x, hopping=params.hopping)
        gamma = 2.0 * np.outer(z, z.conj())
        gx = geometry_gradient_from_density(
            x, gamma, xref, stiffness=params.stiffness, hopping=params.hopping
        )
        dz = -1j * (h @ z + params.interaction * np.abs(z)**2 * z) / params.hbar
        return np.r_[-params.mobility * gx, dz]

    full = solve_ivp(full_rhs, (0.0, final_time), y0_full, t_eval=times,
                     method="DOP853", rtol=rtol, atol=atol)
    mf = solve_ivp(mf_rhs, (0.0, final_time), y0_mf, t_eval=times,
                   method="DOP853", rtol=rtol, atol=atol)
    if not full.success or not mf.success:
        raise RuntimeError(f"integration failed: full={full.message}; mean-field={mf.message}")

    one_rdm_errors, geometry_errors, norm_errors = [], [], []
    for k in range(samples):
        xf, psif = full.y[:192, k].real, full.y[192:, k]
        xm, phim = mf.y[:192, k].real, mf.y[192:, k]
        gf = one_body_density(psif) / 2.0
        gm = np.outer(phim, phim.conj())
        one_rdm_errors.append(float(np.linalg.norm(gf - gm, ord="fro")))
        geometry_errors.append(float(np.linalg.norm(xf - xm)))
        norm_errors.append(abs(float(np.vdot(psif, psif).real) - 1.0))
    return {
        "schema": "q6-two-boson-mean-field/v1",
        "model": "N=2 Bose-Hubbard on Q6; on-site U; common gradient-flow metric backreaction",
        "parameters": params.__dict__,
        "times": times.tolist(),
        "one_body_trace_distance_frobenius": one_rdm_errors,
        "geometry_l2_error": geometry_errors,
        "full_state_norm_error": norm_errors,
        "max_one_body_error": max(one_rdm_errors),
        "max_geometry_error": max(geometry_errors),
        "max_norm_error": max(norm_errors),
        "classification": "finite-dimensional numerical comparison; no mean-field limit theorem",
    }


def interaction_sweep(interactions=(0.0, 0.1, 0.5, 1.0), *, params=Parameters(), **kwargs):
    """Run the same initial-value problem over an explicit interaction grid."""
    records = []
    for value in interactions:
        if not np.isfinite(value):
            raise ValueError("all interaction values must be finite")
        result = run_comparison(params=replace(params, interaction=float(value)),
                                **kwargs)
        records.append({
            "interaction": float(value),
            "max_one_body_error": result["max_one_body_error"],
            "max_geometry_error": result["max_geometry_error"],
            "max_norm_error": result["max_norm_error"],
            "classification": result["classification"],
        })
    return {
        "schema": "q6-two-boson-interaction-sweep/v1",
        "records": records,
        "interpretation": (
            "The U=0 row is the product-state regression. Growth of the "
            "finite-N discrepancy with U measures this benchmark's closure "
            "error; it is not a mean-field convergence theorem."
        ),
    }
