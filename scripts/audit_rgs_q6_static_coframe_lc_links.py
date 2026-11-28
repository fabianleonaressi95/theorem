#!/usr/bin/env python3
"""Audit a deterministic static 3+1 coframe extension and its Q6 link mismatch.

The 64 spatial coframes are reconstructed from the checked RGS seed. Their
symmetric logarithms are interpolated by an exact Gaussian RBF with width
equal to the median Q6 chord length. Exponentiating the interpolated logs
keeps the spatial coframe SPD. This is an explicit interpolation candidate,
not a uniquely determined continuum limit.

A torsion-free Levi-Civita connection is computed from the resulting first
jet. Its edge parallel transports are compared in the original coordinate
basis with the Q6 shortest-radial-rotation links. The script deliberately
reports mismatch rather than fitting the interpolation to the links.
Only NumPy is required.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

ELL2 = 7.035514834154695
C0 = 43.96495130838031
R0 = 0.8292
EXPECTED_X_SHA256 = "6a158cb30a671a5c994d8ab223e9283b57ac703808041d46e67f286126e419cf"
EXPECTED_EDGE_SHA256 = "da7854ca655577b629dc508208918326fde1d50563485f953ea0fdc1b2fb78e8"
I3 = np.eye(3)


def sha256_array(a: np.ndarray, dtype: str) -> str:
    return hashlib.sha256(np.ascontiguousarray(a, dtype=dtype).tobytes()).hexdigest()


def reconstruct_seed() -> tuple[np.ndarray, np.ndarray]:
    """Rebuild the exact 64-site seed and vertex-major Q6 edge order."""
    v = {
        "cube_inner": 0.47863916086470326,
        "small_1": 0.48042984818593559,
        "small_2": 0.48230704367200045,
        "cube_outer": 0.95183963342906408,
        "large_1": 1.5073116806169751,
        "large_2": 1.9039106736116611,
    }
    reps = [
        (v["cube_inner"],) * 3,
        (v["large_1"], v["large_1"], v["small_1"]),
        (v["large_1"], v["small_1"], v["large_1"]),
        (v["small_1"], v["large_1"], v["large_1"]),
        (v["large_2"], v["small_2"], v["small_2"]),
        (v["small_2"], v["large_2"], v["small_2"]),
        (v["small_2"], v["small_2"], v["large_2"]),
        (v["cube_outer"],) * 3,
    ]
    signs = [(sx, sy, sz) for sx in (-1.0, 1.0)
             for sy in (-1.0, 1.0) for sz in (-1.0, 1.0)]
    X = np.asarray([[s[0]*p[0], s[1]*p[1], s[2]*p[2]]
                    for p in reps for s in signs], dtype=np.float64)
    edges = np.asarray([
        (g, g | (1 << axis), axis)
        for g in range(64) for axis in range(6)
        if not ((g >> axis) & 1)
    ], dtype=np.int64)
    if X.shape != (64, 3) or edges.shape != (192, 3):
        raise AssertionError("unexpected reconstructed Q6 seed dimensions")
    x_hash = sha256_array(X, "<f8")
    edge_hash = sha256_array(edges, "<i8")
    if x_hash != EXPECTED_X_SHA256:
        raise AssertionError(f"RGS seed SHA-256 mismatch: {x_hash}")
    if edge_hash != EXPECTED_EDGE_SHA256:
        raise AssertionError(f"Q6 edge SHA-256 mismatch: {edge_hash}")
    return X, edges


def spatial_coframes(X: np.ndarray) -> np.ndarray:
    """Archived local covariance prescription and principal SPD square root."""
    E = np.empty((len(X), 3, 3), dtype=np.float64)
    for i, x in enumerate(X):
        delta = X - x
        weights = np.exp(-np.einsum("ij,ij->i", delta, delta) / ELL2)
        weights[i] = 0.0
        C = np.einsum("i,ia,ib->ab", weights, delta, delta) / C0
        lam, U = np.linalg.eigh(C)
        if lam[0] <= 0.0:
            raise ValueError(f"non-positive local covariance at vertex {i}")
        E[i] = (U * np.sqrt(lam)) @ U.T
    return E


def sym_log(A: np.ndarray) -> np.ndarray:
    lam, U = np.linalg.eigh(0.5 * (A + A.T))
    if lam[0] <= 0.0:
        raise ValueError("coframe must be SPD before taking its logarithm")
    return (U * np.log(lam)) @ U.T


def sym_exp(A: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return exp(A), eigenvalues and eigenvectors for symmetric A."""
    lam, U = np.linalg.eigh(0.5 * (A + A.T))
    return (U * np.exp(lam)) @ U.T, lam, U


class LogGaussianCoframe:
    """Exact Gaussian RBF interpolation in the symmetric-log coframe chart."""

    def __init__(self, X: np.ndarray, E: np.ndarray, edges: np.ndarray):
        lengths = np.linalg.norm(X[edges[:, 1]] - X[edges[:, 0]], axis=1)
        self.sigma = float(np.median(lengths))
        if self.sigma <= 0.0:
            raise ValueError("Q6 median edge length must be positive")
        delta = X[:, None, :] - X[None, :, :]
        self.K = np.exp(-np.einsum("ijk,ijk->ij", delta, delta) / self.sigma**2)
        self.condition = float(np.linalg.cond(self.K))
        self.X = X
        self.coefficients = np.linalg.solve(
            self.K, np.asarray([sym_log(e) for e in E]).reshape(len(X), 9)
        ).reshape(len(X), 3, 3)
        self.training_residual = max(
            float(np.linalg.norm(self.evaluate(x, derivatives=False) - E[i]))
            for i, x in enumerate(X)
        )

    @staticmethod
    def _frechet_exp(lam: np.ndarray, U: np.ndarray, H: np.ndarray) -> np.ndarray:
        """Frechet derivative of exp at symmetric A, applied to symmetric H."""
        Hhat = U.T @ H @ U
        f = np.empty((3, 3), dtype=np.float64)
        for i in range(3):
            for j in range(3):
                if abs(lam[i] - lam[j]) < 1e-10:
                    f[i, j] = np.exp(0.5 * (lam[i] + lam[j]))
                else:
                    f[i, j] = (np.exp(lam[i]) - np.exp(lam[j])) / (lam[i] - lam[j])
        return U @ (f * Hhat) @ U.T

    def evaluate(self, x: np.ndarray, derivatives: bool = True):
        x = np.asarray(x, dtype=np.float64)
        delta = x[None, :] - self.X
        k = np.exp(-np.einsum("ij,ij->i", delta, delta) / self.sigma**2)
        L = np.einsum("i,ijk->jk", k, self.coefficients)
        L = 0.5 * (L + L.T)
        E, lam, U = sym_exp(L)
        if not derivatives:
            return E
        dE = np.empty((3, 3, 3), dtype=np.float64)
        for mu in range(3):
            dk = (-2.0 * delta[:, mu] / self.sigma**2) * k
            dL = np.einsum("i,ijk->jk", dk, self.coefficients)
            dL = 0.5 * (dL + dL.T)
            dE[:, :, mu] = self._frechet_exp(lam, U, dL)
        return E, dE


def levi_civita_spin3(E: np.ndarray, dE: np.ndarray):
    """Compute spatial Christoffel symbols and mixed orthonormal spin connection."""
    metric = E.T @ E
    inverse_metric = np.linalg.inv(metric)
    inverse_coframe = np.linalg.inv(E)
    dg = np.empty((3, 3, 3), dtype=np.float64)
    for mu in range(3):
        dm = dE[:, :, mu]
        dg[:, :, mu] = dm.T @ E + E.T @ dm
    christoffel = np.zeros((3, 3, 3), dtype=np.float64)
    for rho in range(3):
        for mu in range(3):
            for nu in range(3):
                christoffel[rho, mu, nu] = 0.5 * sum(
                    inverse_metric[rho, s] *
                    (dg[s, nu, mu] + dg[s, mu, nu] - dg[mu, nu, s])
                    for s in range(3)
                )
    omega = np.zeros((3, 3, 3), dtype=np.float64)
    for a in range(3):
        for b in range(3):
            for mu in range(3):
                omega[a, b, mu] = sum(
                    (sum(christoffel[rho, mu, nu] * E[a, rho]
                         for rho in range(3)) - dE[a, nu, mu])
                    * inverse_coframe[nu, b]
                    for nu in range(3)
                )
    antisymmetry = float(np.linalg.norm(omega + omega.swapaxes(0, 1)))
    return metric, christoffel, omega, antisymmetry


def skew(v: np.ndarray) -> np.ndarray:
    x, y, z = v
    return np.array([[0.0, -z, y], [z, 0.0, -x], [-y, x, 0.0]])


def minimal_rotation(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    a = a / np.linalg.norm(a)
    b = b / np.linalg.norm(b)
    c = float(np.clip(a @ b, -1.0, 1.0))
    v = np.cross(a, b)
    s = float(np.linalg.norm(v))
    if s < 1e-14:
        if c > 0.0:
            return I3.copy()
        ref = np.array([1.0, 0.0, 0.0]) if abs(a[0]) < 0.8 else np.array([0.0, 1.0, 0.0])
        axis = np.cross(a, ref)
        axis /= np.linalg.norm(axis)
        return 2.0 * np.outer(axis, axis) - I3
    V = skew(v / s)
    return I3 + V * s + (V @ V) * (1.0 - c)


def lc_edge_transport(X, Efun, g: int, h: int, steps: int):
    """RK4 parallel transport along the straight Q6 chord, returned in coordinates."""
    x0, x1 = X[g], X[h]
    dx = x1 - x0
    P = I3.copy()

    def rhs(s, value):
        E, dE = Efun.evaluate(x0 + s * dx, derivatives=True)
        _, _, omega, _ = levi_civita_spin3(E, dE)
        A = np.einsum("abi,i->ab", omega, dx)
        return -A @ value

    dt = 1.0 / steps
    for j in range(steps):
        s = j * dt
        k1 = rhs(s, P)
        k2 = rhs(s + dt/2.0, P + dt*k1/2.0)
        k3 = rhs(s + dt/2.0, P + dt*k2/2.0)
        k4 = rhs(s + dt, P + dt*k3)
        P += (dt/6.0) * (k1 + 2*k2 + 2*k3 + k4)
    Eg = Efun.evaluate(x0, derivatives=False)
    Eh = Efun.evaluate(x1, derivatives=False)
    # Convert orthonormal-frame transport to the common coordinate basis.
    Rcoord = np.linalg.solve(Eh, P @ Eg)
    return P, Rcoord


def q6_squares() -> list[tuple[int, int, int, int]]:
    squares = []
    for a in range(6):
        for b in range(a + 1, 6):
            for g in range(64):
                if ((g >> a) & 1) or ((g >> b) & 1):
                    continue
                j = g ^ (1 << a)
                k = j ^ (1 << b)
                l = g ^ (1 << b)
                squares.append((g, j, k, l))
    if len(squares) != 240:
        raise AssertionError("Q6 must have exactly 240 coordinate squares")
    return squares


def face_holonomy(square, links, edge_index, edges):
    H = I3.copy()
    for a, b in zip(square, square[1:] + square[:1]):
        k = edge_index[(min(a, b), max(a, b))]
        g, h = map(int, edges[k, :2])
        link = links[k] if (a, b) == (g, h) else np.linalg.inv(links[k])
        H = link @ H
    return H


def summarize(values: np.ndarray) -> dict:
    return {
        "mean": float(np.mean(values)),
        "rms": float(np.sqrt(np.mean(values**2))),
        "max": float(np.max(values)),
        "p95": float(np.quantile(values, 0.95)),
    }


def tesla_rotating_frame_audit() -> dict:
    """Audit rotating tetrad, Tesla sequence orientation and quaternionic spin lift."""
    omega_el = 2.3
    B0 = np.array([1.0, 0.0, 0.0])
    Jz = np.array([[0.0, -1.0, 0.0],
                   [1.0, 0.0, 0.0],
                   [0.0, 0.0, 0.0]])
    I2 = np.eye(2, dtype=complex)
    pauli = (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )
    times = np.linspace(0.0, 2.0*np.pi/omega_el, 33, endpoint=True)
    plus_rates, minus_rates = [], []
    gauge_residuals, temporal_torsion_residuals = [], []
    su2_unitarity, su2_adjoint = [], []

    def rz(theta):
        c, s = np.cos(theta), np.sin(theta)
        return np.array([[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]])

    def su2_from_angle(theta):
        q = np.array([np.cos(theta/2.0), 0.0, 0.0, np.sin(theta/2.0)])
        return q[0]*I2 - 1j*sum(q[k+1]*pauli[k] for k in range(3))

    def so3_from_su2(U):
        return np.asarray([
            [np.real(np.trace(pauli[i] @ U @ pauli[j] @ U.conj().T) / 2.0)
             for j in range(3)] for i in range(3)
        ])

    for t in times:
        theta = omega_el*t
        Rplus = rz(theta)
        Bplus = Rplus @ B0
        dBplus = omega_el * Jz @ Bplus
        Bminus = rz(-theta) @ B0
        dBminus = -omega_el * Jz @ Bminus
        plus_rates.append(float((Bplus[0]*dBplus[1] - Bplus[1]*dBplus[0])
                                / (Bplus @ Bplus)))
        minus_rates.append(float((Bminus[0]*dBminus[1] - Bminus[1]*dBminus[0])
                                 / (Bminus @ Bminus)))

        # Co-rotating coframe S(t)=R_z(-Omega t), with omega_t=-dot(S)S^{-1}.
        S = rz(-theta)
        dS = -omega_el * Jz @ S
        omega_t = -dS @ S.T
        B_frame = S @ Bplus
        dB_frame = dS @ Bplus + S @ dBplus
        D_frame = dB_frame + omega_t @ B_frame
        gauge_residuals.append(float(np.linalg.norm(D_frame - S @ dBplus)))
        temporal_torsion_residuals.append(float(np.linalg.norm(dS + omega_t @ S)))

        U = su2_from_angle(theta)
        su2_unitarity.append(float(np.linalg.norm(U.conj().T @ U - I2)))
        su2_adjoint.append(float(np.linalg.norm(so3_from_su2(U) - Rplus)))

    U_2pi = su2_from_angle(2.0*np.pi)
    U_4pi = su2_from_angle(4.0*np.pi)
    return {
        "electrical_angular_frequency": omega_el,
        "positive_sequence_rotation_rate": summarize(np.asarray(plus_rates)),
        "negative_sequence_rotation_rate": summarize(np.asarray(minus_rates)),
        "co_rotating_frame_covariance_residual": summarize(np.asarray(gauge_residuals)),
        "rotating_tetrad_temporal_torsion_residual": summarize(np.asarray(temporal_torsion_residuals)),
        "quaternionic_spin_lift": {
            "convention": "q=(cos(theta/2),0,0,sin(theta/2)); U=q0 I - i q.sigma",
            "max_SU2_unitarity_residual": float(np.max(su2_unitarity)),
            "max_SU2_to_SO3_adjoint_residual": float(np.max(su2_adjoint)),
            "U_at_2pi_equals_minus_I_residual": float(np.linalg.norm(U_2pi + I2)),
            "U_at_4pi_equals_plus_I_residual": float(np.linalg.norm(U_4pi - I2)),
            "status": "SPIN_DOUBLE_COVER_AUDITED",
        },
        "interpretation": (
            "positive/negative phase sequence reverses the rotating-field orientation; "
            "the time-dependent coframe rotation contributes omega_t=-dot(S)S^{-1}; "
            "its temporal Cartan torsion cancels exactly, and the quaternionic SU(2) "
            "lift has the expected 2pi sign and 4pi periodicity"
        ),
        "status": "TESLA_ROTATING_TETRAD_AND_QUATERNIONIC_COVARIANCE_AUDITED",
    }


def run_audit(steps: tuple[int, ...] = (8, 16)) -> dict:
    X, edges = reconstruct_seed()
    E = spatial_coframes(X)
    metrics = np.einsum("...ki,...kj->...ij", E, E)
    lengths = np.linalg.norm(X[edges[:, 1]] - X[edges[:, 0]], axis=1)
    directions = X / np.linalg.norm(X, axis=1)[:, None]
    R_q6 = np.asarray([minimal_rotation(directions[g], directions[h])
                       for g, h, _ in edges])
    interp = LogGaussianCoframe(X, E, edges)

    site_antisym = []
    site_postulate = []
    site_torsion = []
    for i, x in enumerate(X):
        Ei, dEi = interp.evaluate(x, derivatives=True)
        _, Gamma, omega, anti = levi_civita_spin3(Ei, dEi)
        site_antisym.append(anti)
        # Re-evaluate the spatial tetrad postulate and Cartan torsion.
        inverse = np.linalg.inv(Ei)
        post = np.zeros((3, 3, 3))
        tors = np.zeros((3, 3, 3))
        for a in range(3):
            for mu in range(3):
                for nu in range(3):
                    post[a, mu, nu] = (
                        dEi[a, nu, mu]
                        + sum(omega[a, b, mu] * Ei[b, nu] for b in range(3))
                        - sum(Gamma[rho, mu, nu] * Ei[a, rho] for rho in range(3))
                    )
                    tors[a, mu, nu] = (
                        dEi[a, nu, mu] - dEi[a, mu, nu]
                        + sum(omega[a, b, mu] * Ei[b, nu]
                              - omega[a, b, nu] * Ei[b, mu] for b in range(3))
                    )
        site_postulate.append(float(np.linalg.norm(post)))
        site_torsion.append(float(np.linalg.norm(tors)))

    # The static spacetime lift is e^0=dt, e^a=E^a_i(x)dx^i, N=1, shift=0.
    # Its temporal spin-connection components vanish; the spatial block is above.
    links_by_steps = {}
    integration_convergence = None
    for nsteps in steps:
        coordinate_links = []
        metric_preservation = []
        q6_metric_defect = []
        link_difference = []
        for k, (g0, h0, _) in enumerate(edges):
            g, h = int(g0), int(h0)
            _, Rlc = lc_edge_transport(X, interp, g, h, nsteps)
            coordinate_links.append(Rlc)
            metric_preservation.append(np.linalg.norm(
                Rlc.T @ metrics[h] @ Rlc - metrics[g], ord="fro"
            ))
            q6_metric_defect.append(np.linalg.norm(
                R_q6[k].T @ metrics[h] @ R_q6[k] - metrics[g], ord="fro"
            ))
            link_difference.append(np.linalg.norm(Rlc - R_q6[k], ord="fro"))
        links_by_steps[nsteps] = np.asarray(coordinate_links)
        if len(steps) > 1 and nsteps == steps[-1]:
            integration_convergence = np.asarray([
                np.linalg.norm(links_by_steps[steps[-1]][k] - links_by_steps[steps[-2]][k])
                for k in range(len(edges))
            ])
        if nsteps == steps[-1]:
            final_metric_preservation = np.asarray(metric_preservation)
            final_q6_metric_defect = np.asarray(q6_metric_defect)
            final_link_difference = np.asarray(link_difference)

    edge_index = {(min(int(g), int(h)), max(int(g), int(h))): k
                  for k, (g, h, _) in enumerate(edges)}
    squares = q6_squares()
    H_q6 = np.asarray([face_holonomy(sq, R_q6, edge_index, edges) for sq in squares])
    H_lc = np.asarray([
        face_holonomy(sq, links_by_steps[steps[-1]], edge_index, edges)
        for sq in squares
    ])
    face_matrix_difference = np.linalg.norm(H_lc - H_q6, axis=(1, 2))
    face_trace_difference = np.abs(
        np.trace(H_lc, axis1=1, axis2=2) - np.trace(H_q6, axis1=1, axis2=2)
    )

    return {
        "status": "STATIC_3PLUS1_COFRAME_INTERPOLATION_CANDIDATE; LC_LINK_MISMATCH_MEASURED",
        "provenance": {
            "seed_coordinate_sha256": EXPECTED_X_SHA256,
            "q6_edge_sha256": EXPECTED_EDGE_SHA256,
            "coframe_rule": "principal SPD square root of archived local Gaussian covariance",
            "interpolation": "exact Gaussian RBF of symmetric matrix logarithms",
            "rbf_width_rule": "median Euclidean length of the 192 Q6 edges",
            "rbf_sigma": interp.sigma,
            "rbf_kernel_condition_number": interp.condition,
            "rbf_site_interpolation_residual": interp.training_residual,
            "edge_path": "straight chord in the reconstructed X_Oh coordinate chart",
            "q6_link": "minimal SO(3) rotation from X_g/|X_g| to X_h/|X_h|",
        },
        "tesla_rotating_field": tesla_rotating_frame_audit(),
        "static_spacetime_lift": {
            "coframe": "e^0=dt; e^a=E^a_i(x)dx^i",
            "lapse": 1.0,
            "shift": [0.0, 0.0, 0.0],
            "time_derivatives": "zero by static ansatz; no dynamical lapse/shift derived",
            "metric_signature": "(-,+,+,+)",
            "interpretation": "static Lorentzian extension, not a solution of gravitational field equations",
        },
        "site_coframe": {
            "shape": list(E.shape),
            "determinant_min": float(np.min(np.linalg.det(E))),
            "determinant_max": float(np.max(np.linalg.det(E))),
            "metric_condition_max": float(max(np.linalg.cond(m) for m in metrics)),
            "max_site_omega_antisymmetry_residual": float(np.max(site_antisym)),
            "max_site_tetrad_postulate_residual": float(np.max(site_postulate)),
            "max_site_cartan_torsion_residual": float(np.max(site_torsion)),
        },
        "edge_transport": {
            "integration_steps": list(steps),
            "max_RK4_refinement_difference": (
                summarize(integration_convergence) if integration_convergence is not None else None
            ),
            "LC_metric_preservation": summarize(final_metric_preservation),
            "Q6_link_metric_compatibility_defect": summarize(final_q6_metric_defect),
            "LC_vs_Q6_coordinate_link_difference": summarize(final_link_difference),
            "comparison_contract": (
                "LC transport is converted from orthonormal-frame to coordinate components "
                "as E_h^{-1} P_LC E_g; it is compared directly with the Q6 SO(3) coordinate link"
            ),
        },
        "face_holonomy": {
            "face_count": len(squares),
            "LC_vs_Q6_matrix_difference": summarize(face_matrix_difference),
            "absolute_Wilson_trace_difference": summarize(face_trace_difference),
        },
        "epistemic_limits": [
            "The log-Gaussian interpolation is a declared candidate, not uniquely determined by the 64 samples.",
            "The static lift has N=1 and zero shift; it does not derive physical time evolution.",
            "The Q6 minimal-radial-rotation links are not metric-compatible with the interpolated RGS coframe metric in general.",
            "The measured link/holonomy mismatch means these Q6 links are not the Levi-Civita holonomies of this interpolated metric under the declared straight-edge paths.",
            "No TEGR, Einstein-Cartan, Maxwell/QHD coupled solution, or continuum/Mosco convergence is established.",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=Path("audits/RGS_Q6_STATIC_COFRAME_LC_LINK_AUDIT.json"))
    parser.add_argument("--steps", type=int, nargs="+", default=[8, 16])
    args = parser.parse_args()
    if not args.steps or any(n < 2 for n in args.steps):
        parser.error("--steps requires integers >= 2")
    report = run_audit(tuple(args.steps))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
