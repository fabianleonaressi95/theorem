"""Finite calibration for discrete Dirichlet forms on periodic cycles.

This is a toy consistency check for the h -> 0 scaling, not a proof of
Mosco convergence for an arbitrary graph sequence or for RGS-PRISM.
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class PeriodicCycle:
    n: int

    def __post_init__(self) -> None:
        if isinstance(self.n, bool) or self.n < 3:
            raise ValueError("n must be an integer >= 3")

    @property
    def mass(self) -> float:
        return 1.0 / self.n

    @property
    def conductance(self) -> float:
        return float(self.n)

    def sample_mode(self, k: int, phase: float = 0.0) -> np.ndarray:
        if k < 0 or k >= self.n:
            raise ValueError("mode must satisfy 0 <= k < n")
        x = np.arange(self.n, dtype=float) / self.n
        return np.cos(2.0 * math.pi * k * x + phase)

    def norm_squared(self, u: np.ndarray) -> float:
        u = self._validate(u)
        return float(self.mass * np.dot(u, u))

    def energy(self, u: np.ndarray) -> float:
        u = self._validate(u)
        differences = np.roll(u, -1) - u
        return float(self.conductance * np.dot(differences, differences))

    def eigenvalue(self, k: int) -> float:
        if k < 0 or k >= self.n:
            raise ValueError("mode must satisfy 0 <= k < n")
        return float(4.0 * self.n**2 * math.sin(math.pi * k / self.n) ** 2)

    @staticmethod
    def _validate(u: np.ndarray) -> np.ndarray:
        arr = np.asarray(u, dtype=float)
        if arr.ndim != 1 or not np.all(np.isfinite(arr)):
            raise ValueError("u must be a finite one-dimensional array")
        return arr


def continuum_mode_energy(k: int, amplitude: float = 1.0) -> float:
    """Integral over [0,1] of |d/dx (A cos(2 pi k x))|^2 dx."""
    if k < 0 or not math.isfinite(amplitude):
        raise ValueError("k must be non-negative and amplitude finite")
    return 2.0 * math.pi**2 * k**2 * amplitude**2


def audit_cycle(n_values: list[int], mode: int = 1) -> dict:
    rows = []
    for n in n_values:
        graph = PeriodicCycle(n)
        if mode >= n:
            raise ValueError(f"mode {mode} must be smaller than n={n}")
        u = graph.sample_mode(mode)
        exact = continuum_mode_energy(mode)
        discrete = graph.energy(u)
        rows.append({
            "n": n,
            "h": 1.0 / n,
            "mass_norm_squared": graph.norm_squared(u),
            "discrete_energy": discrete,
            "continuum_energy": exact,
            "relative_energy_error": abs(discrete - exact) / max(1.0, abs(exact)),
            "discrete_eigenvalue": graph.eigenvalue(mode),
            "continuum_eigenvalue": (2.0 * math.pi * mode) ** 2,
        })
    return {
        "model": "periodic_cycle_finite_difference_calibration",
        "mode": mode,
        "status": "calibration_only_not_a_general_Mosco_proof",
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, nargs="+", default=[32, 64, 128, 256])
    parser.add_argument("--mode", type=int, default=1)
    args = parser.parse_args()
    print(json.dumps(audit_cycle(args.n, args.mode), indent=2))


if __name__ == "__main__":
    main()
