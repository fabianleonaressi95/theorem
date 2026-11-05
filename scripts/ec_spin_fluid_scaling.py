"""Minimal scaling audit for an algebraic Einstein-Cartan Weyssenhoff spin fluid.

The module encodes the standard minimally coupled, isotropized closure:
n ~ a^-3, s^2 ~ n^2, rho_spin = p_spin = -A*s^2.
It is a scaling audit, not a solver for the full EC field equations.
"""
from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class WeyssenhoffScaling:
    number_density_0: float
    spin_invariant_0: float
    coupling_A: float

    def __post_init__(self) -> None:
        vals = (self.number_density_0, self.spin_invariant_0, self.coupling_A)
        if not all(math.isfinite(v) for v in vals):
            raise ValueError("initial data and coupling must be finite")
        if self.number_density_0 < 0 or self.spin_invariant_0 < 0:
            raise ValueError("number and spin-squared densities must be non-negative")
        if self.coupling_A < 0:
            raise ValueError("coupling_A must be non-negative")

    @staticmethod
    def _a(a: float) -> float:
        a = float(a)
        if not math.isfinite(a) or a <= 0:
            raise ValueError("scale factor must be finite and positive")
        return a

    def number_density(self, a: float) -> float:
        a = self._a(a)
        return self.number_density_0 * a**-3

    def spin_invariant(self, a: float) -> float:
        a = self._a(a)
        return self.spin_invariant_0 * a**-6

    def rho_spin_effective(self, a: float) -> float:
        return -self.coupling_A * self.spin_invariant(a)

    def p_spin_effective(self, a: float) -> float:
        return self.rho_spin_effective(a)

    def continuity_residual_over_H(self, a: float) -> float:
        """Return (dot(rho)+3H(rho+p))/H for H != 0."""
        rho = self.rho_spin_effective(a)
        # d rho / d ln(a) = -6 rho
        return -6.0 * rho + 3.0 * (rho + self.p_spin_effective(a))

    def equation_of_state(self, a: float) -> float:
        rho = self.rho_spin_effective(a)
        if rho == 0.0:
            raise ZeroDivisionError("w is undefined for a vanishing spin correction")
        return self.p_spin_effective(a) / rho

    def dust_identification_ratio(self, a: float, beta_rho_m0: float) -> float:
        """EC spin correction divided by a proposed beta*rho_m0*a^-3 term."""
        a = self._a(a)
        denominator = beta_rho_m0 * a**-3
        if denominator == 0.0:
            raise ZeroDivisionError("dust comparison term vanishes")
        return self.rho_spin_effective(a) / denominator
