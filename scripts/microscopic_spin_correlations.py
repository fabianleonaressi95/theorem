"""Microscopic-to-macroscopic spin-correlation audit (T049).

This is a kinematic/statistical audit, not a Dirac-field solver and not a
derivation of the RGS-PSU spin correlator. It separates self and pair terms
and tests the cosmological scaling consequences of an explicit ansatz.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Iterable, Sequence


Vector3 = Sequence[float]


def spin_current_decomposition(
    spins: Iterable[Vector3], weights: Iterable[float] | None = None
) -> dict[str, float | tuple[float, float, float]]:
    """Return |sum_a w_a s_a|^2 split into self and pair contributions.

    The 3-vector is the spatial axial-spin representation in the local rest
    frame. Overall tensor-to-vector normalization is convention dependent.
    """
    vectors = [tuple(float(x) for x in s) for s in spins]
    if any(len(s) != 3 for s in vectors):
        raise ValueError("each spin must be a 3-vector")
    if any(not math.isfinite(x) for s in vectors for x in s):
        raise ValueError("spin components must be finite")
    if weights is None:
        ws = [1.0] * len(vectors)
    else:
        ws = [float(w) for w in weights]
    if len(ws) != len(vectors):
        raise ValueError("weights and spins must have equal length")
    if any(not math.isfinite(w) for w in ws):
        raise ValueError("weights must be finite")

    current = tuple(
        sum(w * s[k] for w, s in zip(ws, vectors)) for k in range(3)
    )
    self_term = sum(
        w * w * sum(x * x for x in s) for w, s in zip(ws, vectors)
    )
    pair_term = 2.0 * sum(
        ws[i] * ws[j] * sum(vectors[i][k] * vectors[j][k] for k in range(3))
        for i in range(len(vectors))
        for j in range(i + 1, len(vectors))
    )
    total = sum(x * x for x in current)
    return {
        "current": current,
        "self": self_term,
        "pair": pair_term,
        "total": total,
        "identity_residual": total - self_term - pair_term,
    }


@dataclass(frozen=True)
class SpinCorrelationScaling:
    """Two-channel ansatz: s2 = Cself*n + Cpair*n^2*a^(-gamma).

    n(a)=n0*a^-3. Coefficients are non-negative effective amplitudes.
    gamma=0 is the standard pair-scaling benchmark; gamma=-3 makes the
    pair channel scale as a^-3. This is a diagnostic parametrization only.
    """

    number_density_0: float
    self_amplitude: float = 0.0
    pair_amplitude: float = 1.0
    pair_correlation_exponent: float = 0.0
    coupling_A: float = 1.0

    def __post_init__(self) -> None:
        values = (
            self.number_density_0,
            self.self_amplitude,
            self.pair_amplitude,
            self.pair_correlation_exponent,
            self.coupling_A,
        )
        if not all(math.isfinite(v) for v in values):
            raise ValueError("all parameters must be finite")
        if self.number_density_0 < 0 or self.self_amplitude < 0:
            raise ValueError("density and self amplitude must be non-negative")
        if self.pair_amplitude < 0 or self.coupling_A < 0:
            raise ValueError("pair amplitude and coupling must be non-negative")

    @staticmethod
    def _a(a: float) -> float:
        a = float(a)
        if not math.isfinite(a) or a <= 0:
            raise ValueError("scale factor must be finite and positive")
        return a

    def number_density(self, a: float) -> float:
        return self.number_density_0 * self._a(a) ** -3

    def self_invariant(self, a: float) -> float:
        return self.self_amplitude * self.number_density(a)

    def pair_correlation(self, a: float) -> float:
        return self._a(a) ** (-self.pair_correlation_exponent)

    def pair_invariant(self, a: float) -> float:
        n = self.number_density(a)
        return self.pair_amplitude * n * n * self.pair_correlation(a)

    def spin_invariant(self, a: float) -> float:
        return self.self_invariant(a) + self.pair_invariant(a)

    def rho_spin_effective(self, a: float) -> float:
        return -self.coupling_A * self.spin_invariant(a)

    def effective_exponent(self, a: float) -> float:
        """q_eff=-d ln(s2)/d ln(a), for nonzero s2."""
        self_part = self.self_invariant(a)
        pair_part = self.pair_invariant(a)
        total = self_part + pair_part
        if total == 0:
            raise ZeroDivisionError("effective exponent undefined at zero spin")
        q_self = 3.0
        q_pair = 6.0 + self.pair_correlation_exponent
        return (q_self * self_part + q_pair * pair_part) / total

    def equation_of_state(self, a: float) -> float:
        """w implied by separate conservation of rho_spin=-A*s2."""
        return self.effective_exponent(a) / 3.0 - 1.0

    def pressure_spin_effective(self, a: float) -> float:
        return self.equation_of_state(a) * self.rho_spin_effective(a)

    def continuity_residual_over_H(self, a: float) -> float:
        """(dot(rho)+3H(rho+p))/H, evaluated analytically."""
        rho = self.rho_spin_effective(a)
        q = self.effective_exponent(a)
        pressure = self.pressure_spin_effective(a)
        return -q * rho + 3.0 * (rho + pressure)
