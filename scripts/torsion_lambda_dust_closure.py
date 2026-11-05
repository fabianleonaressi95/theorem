"""Phenomenological dust-like torsion contribution to a flat FLRW background.

This module implements a bookkeeping closure, not a derivation of propagating
Einstein--Cartan torsion.  The assumed sector is rho_T = beta Omega_m0 a^-3,
so separate conservation fixes p_T = 0.
"""
from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class TorsionLambdaModel:
    """Dimensionless flat-FLRW parameters at a=1.

    Omega_r0 and Omega_m0 are non-negative reference densities; beta > -1
    keeps the combined dust coefficient non-negative.  Lambda is dimensionless
    and may have either sign for diagnostic purposes.
    """

    omega_r0: float
    omega_m0: float
    beta: float
    lambda_: float

    def __post_init__(self) -> None:
        values = (self.omega_r0, self.omega_m0, self.beta, self.lambda_)
        if not all(math.isfinite(x) for x in values):
            raise ValueError("all cosmological parameters must be finite")
        if self.omega_r0 < 0 or self.omega_m0 < 0:
            raise ValueError("radiation and matter densities must be non-negative")
        if self.beta <= -1:
            raise ValueError("beta must be greater than -1")

    @staticmethod
    def _check_scale_factor(a: float) -> float:
        a = float(a)
        if not math.isfinite(a) or a <= 0:
            raise ValueError("scale factor a must be finite and positive")
        return a

    @classmethod
    def flat(
        cls, omega_r0: float, omega_m0: float, beta: float
    ) -> "TorsionLambdaModel":
        """Construct the model with E(1)^2 = 1."""
        lambda_ = 1.0 - omega_r0 - omega_m0 * (1.0 + beta)
        return cls(omega_r0, omega_m0, beta, lambda_)

    @classmethod
    def einstein_cartan_lambda_zero(
        cls, omega_r0: float, beta: float
    ) -> "TorsionLambdaModel":
        """Return the lambda=0 flat boundary, solving for Omega_m0."""
        if beta <= -1:
            raise ValueError("beta must be greater than -1")
        omega_m0 = (1.0 - omega_r0) / (1.0 + beta)
        return cls(omega_r0, omega_m0, beta, 0.0)

    def rho_torsion(self, a: float) -> float:
        a = self._check_scale_factor(a)
        return self.beta * self.omega_m0 * a**-3

    def p_torsion(self, a: float) -> float:
        self._check_scale_factor(a)
        return 0.0

    def rho_matter(self, a: float) -> float:
        a = self._check_scale_factor(a)
        return self.omega_m0 * a**-3

    def rho_radiation(self, a: float) -> float:
        a = self._check_scale_factor(a)
        return self.omega_r0 * a**-4

    def rho_effective(self, a: float) -> float:
        a = self._check_scale_factor(a)
        return (
            self.omega_r0 * a**-4
            + self.omega_m0 * (1.0 + self.beta) * a**-3
            + self.lambda_
        )

    def p_effective(self, a: float) -> float:
        a = self._check_scale_factor(a)
        return self.omega_r0 * a**-4 / 3.0 - self.lambda_

    def e2(self, a: float) -> float:
        """Dimensionless Hubble rate squared, E(a)^2 = rho_effective(a)."""
        return self.rho_effective(a)

    def closure_residual(self) -> float:
        """E(1)^2 - 1; zero is the spatially-flat normalization."""
        return self.e2(1.0) - 1.0

    def torsion_continuity_residual(self, a: float) -> float:
        """Analytic d rho_T/d ln(a) + 3(rho_T+p_T), identically zero."""
        rho = self.rho_torsion(a)
        return -3.0 * rho + 3.0 * (rho + self.p_torsion(a))

    def w_torsion(self, a: float) -> float:
        """Return p_T/rho_T; undefined when the torsion density vanishes."""
        rho = self.rho_torsion(a)
        if rho == 0.0:
            raise ZeroDivisionError("w_T is undefined when rho_T is zero")
        return self.p_torsion(a) / rho
