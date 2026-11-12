#!/usr/bin/env python3
"""XY model on periodic 2D/3D lattices: vortices, winding, and helicity.

Finite-size XY benchmark only. It is not a KTHNY elastic-dislocation
simulation and does not identify Q6 charges with XY vortices.
"""
from __future__ import annotations

import argparse
import json
import numpy as np


def wrap(angle: np.ndarray | float) -> np.ndarray:
    """Principal angle in (-pi, pi]."""
    return (np.asarray(angle) + np.pi) % (2.0 * np.pi) - np.pi


def metropolis_sweep(theta: np.ndarray, beta: float, rng: np.random.Generator,
                     coupling: float = 1.0, delta: float = 1.0) -> None:
    """One random-site Metropolis sweep; theta is a dim-dimensional array."""
    if theta.ndim not in (2, 3):
        raise ValueError("only 2D and 3D periodic lattices are supported")
    if beta <= 0 or coupling <= 0 or delta <= 0:
        raise ValueError("beta, coupling and proposal width must be positive")
    shape = theta.shape
    if len(set(shape)) != 1 or shape[0] < 3:
        raise ValueError("use a cubic/square lattice with L >= 3")
    dim, nsites = theta.ndim, theta.size
    for flat_index in rng.permutation(nsites):
        site = list(np.unravel_index(int(flat_index), shape))
        old = float(theta[tuple(site)])
        new = old + rng.uniform(-delta, delta)
        e_old = e_new = 0.0
        for axis in range(dim):
            for step in (-1, 1):
                nb = site.copy()
                nb[axis] = (nb[axis] + step) % shape[axis]
                value = float(theta[tuple(nb)])
                e_old -= coupling * np.cos(old - value)
                e_new -= coupling * np.cos(new - value)
        d_energy = e_new - e_old
        if d_energy <= 0.0 or rng.random() < np.exp(-beta * d_energy):
            theta[tuple(site)] = float(wrap(new))


def plaquette_vorticity(theta: np.ndarray, mu: int, nu: int) -> np.ndarray:
    """Integer winding on oriented (mu,nu) plaquettes based at each site."""
    if mu == nu or mu not in range(theta.ndim) or nu not in range(theta.ndim):
        raise ValueError("mu and nu must be distinct valid axes")
    dmu = wrap(np.roll(theta, -1, axis=mu) - theta)
    dnu = wrap(np.roll(theta, -1, axis=nu) - theta)
    circulation = dmu + np.roll(dnu, -1, axis=mu) \
        - np.roll(dmu, -1, axis=nu) - dnu
    return np.rint(circulation / (2.0 * np.pi)).astype(np.int64)


def vortex_field(theta: np.ndarray) -> np.ndarray:
    """2D: scalar plaquette charges. 3D: dual-link vector (qx,qy,qz).

    In 3D qx is the (y,z)-plaquette winding, qy the (z,x) winding,
    and qz the (x,y) winding. These are fluxes on dual links.
    """
    if theta.ndim == 2:
        return plaquette_vorticity(theta, 0, 1)
    if theta.ndim == 3:
        return np.stack((
            plaquette_vorticity(theta, 1, 2),
            plaquette_vorticity(theta, 2, 0),
            plaquette_vorticity(theta, 0, 1),
        ), axis=0)
    raise ValueError("only 2D and 3D lattices are supported")


def dual_vortex_divergence(q: np.ndarray) -> np.ndarray:
    """Discrete divergence of 3D dual vortex flux; must vanish identically."""
    if q.ndim != 4 or q.shape[0] != 3:
        raise ValueError("q must have shape (3,L,L,L)")
    return (np.roll(q[0], -1, axis=0) - q[0]
            + np.roll(q[1], -1, axis=1) - q[1]
            + np.roll(q[2], -1, axis=2) - q[2])


def winding_numbers(theta: np.ndarray) -> np.ndarray:
    """Integer phase winding along every periodic coordinate line."""
    out = []
    for axis in range(theta.ndim):
        increments = wrap(np.roll(theta, -1, axis=axis) - theta)
        line_sums = np.sum(increments, axis=axis) / (2.0 * np.pi)
        out.append(np.rint(line_sums).astype(np.int64))
    return np.stack(out, axis=0)


def helicity_modulus(theta: np.ndarray, beta: float,
                     coupling: float = 1.0) -> np.ndarray:
    """Directional finite-volume helicity modulus for the standard XY model."""
    if beta <= 0 or coupling <= 0:
        raise ValueError("beta and coupling must be positive")
    nsites = theta.size
    values = []
    for axis in range(theta.ndim):
        delta = wrap(np.roll(theta, -1, axis=axis) - theta)
        energy_term = coupling * np.sum(np.cos(delta)) / nsites
        current_term = beta * coupling**2 * np.sum(np.sin(delta))**2 / nsites
        values.append(float(energy_term - current_term))
    return np.asarray(values)


def radial_charge_correlator(q: np.ndarray) -> dict:
    """Periodic radial-bin correlation: scalar q in 2D, q dot q in 3D."""
    if q.ndim == 2:
        fields = q[None, ...].astype(float)
    elif q.ndim == 4 and q.shape[0] == 3:
        fields = q.astype(float)
    else:
        raise ValueError("q must be a 2D scalar field or 3D vector field")
    dim, L = fields.ndim - 1, fields.shape[1]
    max_r = L // 2
    sums = np.zeros(max_r + 1, dtype=float)
    counts = np.zeros(max_r + 1, dtype=np.int64)
    for shift in np.ndindex(*([L] * dim)):
        disp = np.asarray([min(s, L - s) for s in shift], dtype=float)
        rbin = int(np.rint(np.linalg.norm(disp)))
        if rbin > max_r:
            continue
        shifted = fields
        for axis, amount in enumerate(shift):
            shifted = np.roll(shifted, -int(amount), axis=axis + 1)
        corr = np.sum(fields * shifted, axis=0)
        sums[rbin] += float(np.mean(corr))
        counts[rbin] += 1
    vals = np.divide(sums, counts, out=np.zeros_like(sums), where=counts > 0)
    return {"r": list(range(max_r + 1)), "Cq": vals.tolist(),
            "displacement_counts": counts.tolist()}


def run(L: int = 8, dim: int = 2, beta: float = 1.2, coupling: float = 1.0,
        thermalization: int = 500, measurements: int = 500,
        seed: int = 0, delta: float = 1.0) -> dict:
    if dim not in (2, 3) or L < 3:
        raise ValueError("dim must be 2 or 3 and L must be at least 3")
    if thermalization < 0 or measurements < 1:
        raise ValueError("thermalization must be nonnegative and measurements positive")
    rng = np.random.default_rng(seed)
    theta = rng.uniform(-np.pi, np.pi, size=(L,) * dim)
    for _ in range(thermalization):
        metropolis_sweep(theta, beta, rng, coupling, delta)

    corr_acc = None
    helicity, total_vorticity, max_divergence = [], [], []
    winding_samples = []
    for _ in range(measurements):
        metropolis_sweep(theta, beta, rng, coupling, delta)
        q = vortex_field(theta)
        corr = radial_charge_correlator(q)
        if corr_acc is None:
            corr_acc = np.zeros(len(corr["Cq"]), dtype=float)
        corr_acc += np.asarray(corr["Cq"])
        helicity.append(helicity_modulus(theta, beta, coupling))
        if dim == 2:
            total_vorticity.append(int(np.sum(q)))
        else:
            total_vorticity.append([int(np.sum(qi)) for qi in q])
            max_divergence.append(int(np.max(np.abs(dual_vortex_divergence(q)))))
        winding_samples.append(winding_numbers(theta).tolist())

    result = {
        "model": "classical nearest-neighbour XY",
        "dimension": dim, "L": L, "beta": beta, "J": coupling,
        "thermalization_sweeps": thermalization,
        "measurement_sweeps": measurements, "seed": seed,
        "helicity_modulus_mean_by_axis": np.mean(helicity, axis=0).tolist(),
        "beta_helicity_mean_by_axis": (beta * np.mean(helicity, axis=0)).tolist(),
        "vortex_correlator": {
            "r": corr["r"], "Cq_mean": (corr_acc / measurements).tolist()},
        "winding_number_samples": winding_samples,
        "total_plaquette_vorticity": total_vorticity,
        "physical_scope": (
            "2D XY/BKT finite-size diagnostic; not KTHNY dislocation melting"
            if dim == 2 else
            "3D XY vortex-loop flux diagnostic; not a 2D KTHNY transition"),
    }
    if dim == 3:
        result["max_abs_dual_vortex_divergence"] = max_divergence
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--L", type=int, default=8)
    parser.add_argument("--dim", type=int, choices=(2, 3), default=2)
    parser.add_argument("--beta", type=float, default=1.2)
    parser.add_argument("--J", type=float, default=1.0)
    parser.add_argument("--therm", type=int, default=500)
    parser.add_argument("--meas", type=int, default=500)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()
    print(json.dumps(run(args.L, args.dim, args.beta, args.J,
                         args.therm, args.meas, args.seed), indent=2))


if __name__ == "__main__":
    main()
