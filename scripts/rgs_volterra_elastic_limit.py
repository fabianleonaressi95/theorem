#!/usr/bin/env python3
"""Periodic Airy elasticity test of the Volterra dipole-to-edge limit.

This is an elasticity-level comparison, not merely a comparison of source
profiles. It solves the same periodic biharmonic Airy problem for:
  (i) an opposite wedge-disclination pair, and
  (ii) its matched edge-dislocation source, b = Omega*d.

Both use the same normalized periodic Gaussian core in x and y, the same
plane-strain Lamé parameters, periodic boundary conditions, and Fourier
spectral operator. The only difference is the y-source profile.

Run:
  python scripts/rgs_volterra_elastic_limit.py --out artifacts/volterra_elastic_limit
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np

LENGTH = 4.0
LAM = 1.0
MU = 1.0
OMEGA = 0.01
D_OVER_H = (1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 8.0)
SIGMA_OVER_H = (2.0, 3.2, 4.0, 6.4)
RHO_OVER_H = 3.2
LEVELS = (64, 96, 128, 192, 256)


def periodic_gaussian(x: np.ndarray, centre: float, width: float,
                      length: float = LENGTH) -> tuple[np.ndarray, np.ndarray]:
    """Periodized normalized Gaussian and its derivative."""
    if width <= 0:
        raise ValueError("width must be positive")
    f = np.zeros_like(x, dtype=float)
    fp = np.zeros_like(x, dtype=float)
    for k in range(-4, 5):
        z = (x - centre + k * length) / width
        term = np.exp(-0.5 * z * z) / (np.sqrt(2.0 * np.pi) * width)
        f += term
        fp += -(z / width) * term
    # Normalize the sampled profile to unit integral on the periodic grid.
    h = length / len(x)
    mass = float(np.sum(f) * h)
    return f / mass, fp / mass


def elasticity_compliance(lam: float = LAM, mu: float = MU) -> np.ndarray:
    C = np.array([[lam + 2 * mu, lam, 0.0],
                  [lam, lam + 2 * mu, 0.0],
                  [0.0, 0.0, mu]], dtype=float)
    return np.linalg.inv(C)


def airy_from_incompatibility(zeta: np.ndarray, lam: float = LAM,
                              mu: float = MU) -> dict:
    """Solve c*Delta^2(phi) = -zeta and recover periodic Airy stress."""
    n = zeta.shape[0]
    if zeta.shape != (n, n):
        raise ValueError("zeta must be square")
    E = mu * (3 * lam + 2 * mu) / (lam + mu)
    nu = lam / (2 * (lam + mu))
    c = (1 - nu * nu) / E
    h = LENGTH / n
    k = 2 * np.pi * np.fft.fftfreq(n, d=h)
    kx = k[None, :]
    ky = k[:, None]
    k2 = kx * kx + ky * ky
    zhat = np.fft.fft2(zeta)
    phat = np.zeros_like(zhat, dtype=complex)
    mask = k2 > 0
    phat[mask] = -zhat[mask] / (c * k2[mask] ** 2)
    sxx = np.fft.ifft2(-(ky * ky) * phat).real
    syy = np.fft.ifft2(-(kx * kx) * phat).real
    sxy = np.fft.ifft2((kx * ky) * phat).real
    stress = np.stack((sxx, syy, sxy), axis=-1)
    strain = np.einsum("ab,ijb->ija", elasticity_compliance(lam, mu), stress)
    energy_density = 0.5 * np.einsum("...i,...i->...", stress, strain)
    energy = float(np.sum(energy_density) * h * h)
    residual = c * k2 * k2 * phat + zhat
    residual[~mask] = 0
    residual_rel = float(np.linalg.norm(residual) /
                         max(np.linalg.norm(zhat[mask]), 1e-30))
    return {"stress": stress, "strain": strain, "energy": energy,
            "compatibility_residual": residual_rel,
            "mean_source": float(np.mean(zeta))}


def solve_pair(n: int, d_over_h: float, sigma_over_h: float,
               rho_over_h: float = RHO_OVER_H) -> dict:
    h = LENGTH / n
    d = d_over_h * h
    sigma = sigma_over_h * h
    rho = rho_over_h * h
    if d >= LENGTH / 3 or sigma >= LENGTH / 6 or rho >= LENGTH / 6:
        raise ValueError("core/separation too large for this periodic-cell setup")
    c = (np.arange(n) + 0.5) * h
    x0 = LENGTH / 2
    fx, _ = periodic_gaussian(c, x0, rho)
    fy_plus, _ = periodic_gaussian(c, LENGTH / 2 + d / 2, sigma)
    fy_minus, _ = periodic_gaussian(c, LENGTH / 2 - d / 2, sigma)
    _, fy_derivative = periodic_gaussian(c, LENGTH / 2, sigma)
    delta_x = fx[:, None]
    # Opposite wedge-disclination pair: Omega * delta_x * (f+ - f-).
    zeta_dipole = OMEGA * delta_x * (fy_plus - fy_minus)[None, :]
    # Edge dislocation: -b * delta_x * f'(y), with b=Omega*d.
    burgers = OMEGA * d
    zeta_edge = -burgers * delta_x * fy_derivative[None, :]
    dip = airy_from_incompatibility(zeta_dipole)
    edge = airy_from_incompatibility(zeta_edge)
    ds = dip["stress"] - edge["stress"]
    de = dip["strain"] - edge["strain"]
    stress_rel = float(np.linalg.norm(ds) /
                       max(np.linalg.norm(edge["stress"]), 1e-30))
    strain_rel = float(np.linalg.norm(de) /
                       max(np.linalg.norm(edge["strain"]), 1e-30))
    energy_rel = abs(dip["energy"] - edge["energy"]) / max(
        abs(dip["energy"]), abs(edge["energy"]), 1e-30)
    return {
        "n": n, "h": h, "d_over_h": d_over_h,
        "sigma_over_h": sigma_over_h, "rho_over_h": rho_over_h,
        "d_over_sigma": d / sigma, "sigma": sigma, "rho": rho,
        "frank_magnitude": OMEGA, "burgers_magnitude": burgers,
        "dipole_energy": dip["energy"], "edge_energy": edge["energy"],
        "relative_energy_difference": float(energy_rel),
        "relative_stress_l2_difference": stress_rel,
        "relative_strain_l2_difference": strain_rel,
        "dipole_airy_residual": dip["compatibility_residual"],
        "edge_airy_residual": edge["compatibility_residual"],
        "dipole_source_mean": dip["mean_source"],
        "edge_source_mean": edge["mean_source"],
    }


def run(out: Path, levels=LEVELS) -> dict:
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    for n in levels:
        for sigma_h in SIGMA_OVER_H:
            for d_h in D_OVER_H:
                rows.append(solve_pair(n, d_h, sigma_h))
    # Fixed physical core and separation-refinement sequence:
    # this isolates the continuum d/sigma -> 0 limit from grid refinement.
    limit_rows = []
    n = max(levels)
    for d_h in (8.0, 4.0, 2.0, 1.0, 0.5, 0.25):
        limit_rows.append(solve_pair(n, d_h, 8.0))
    report = {
        "title": "Periodic Airy elasticity: Volterra dipole-to-edge limit",
        "status": "numerical spectral elasticity comparison; not a theorem",
        "domain": [0.0, LENGTH, 0.0, LENGTH],
        "material": {"lambda": LAM, "mu": MU, "plane_strain": True},
        "boundary_conditions": "periodic Airy stress; zero mean incompatibility; zero mean stress mode",
        "source_matching": "opposite wedge pair versus edge source with b=Omega*d",
        "sweeps": {"levels": list(levels), "d_over_h": list(D_OVER_H),
                   "sigma_over_h": list(SIGMA_OVER_H), "rho_over_h": RHO_OVER_H},
        "results": rows,
        "small_separation_limit": limit_rows,
        "limitations": [
            "Both fields solve the same periodic Airy elasticity operator; this is not yet a Q1/P1 displacement-FEM cross-check.",
            "The periodic Gaussian core is a regularized source, not a singular atomistic core.",
            "The zero Fourier mode is fixed to zero mean stress; no applied macroscopic stress is included.",
            "No singular-core renormalization or Mosco/Gamma convergence is claimed."
        ]
    }
    (out / "report.json").write_text(json.dumps(report, indent=2) + "\n")
    with (out / "stress_energy_sweep.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    with (out / "small_separation.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(limit_rows[0]))
        writer.writeheader()
        writer.writerows(limit_rows)
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="artifacts/volterra_elastic_limit")
    parser.add_argument("--levels", nargs="+", type=int, default=list(LEVELS))
    args = parser.parse_args()
    report = run(Path(args.out), tuple(args.levels))
    print(json.dumps({"rows": len(report["results"]),
                      "limit_rows": len(report["small_separation_limit"]),
                      "output": args.out}, indent=2))


if __name__ == "__main__":
    main()
