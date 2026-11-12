#!/usr/bin/env python3
"""Exact algebraic audit for T106; no physical data or FDT fit is implied."""
from __future__ import annotations

import cmath
import math
from typing import Sequence

D = 64


def born_probabilities(amplitudes: Sequence[complex], tol: float = 1e-10) -> list[float]:
    if not amplitudes:
        raise ValueError("at least one amplitude is required")
    norm2 = sum(abs(z) ** 2 for z in amplitudes)
    if abs(norm2 - 1.0) > tol:
        raise ValueError("amplitudes must be normalized to unit norm")
    return [abs(z) ** 2 for z in amplitudes]


def dirichlet_uniform_moments(d: int) -> dict[str, float]:
    if d < 2:
        raise ValueError("dimension must be at least 2")
    return {
        "mean": 1.0 / d,
        "variance": (d - 1) / (d * d * (d + 1)),
        "off_diagonal_covariance": -1.0 / (d * d * (d + 1)),
        "marginal_beta_alpha": 1.0,
        "marginal_beta_beta": float(d - 1),
    }


def hexagram_to_z4(bits: Sequence[int]) -> tuple[int, int, int]:
    if len(bits) != 6 or any(bit not in (0, 1) for bit in bits):
        raise ValueError("a hexagram is exactly six binary entries")
    return (2 * bits[0] + bits[1],
            2 * bits[2] + bits[3],
            2 * bits[4] + bits[5])


def integer_to_bits(h: int) -> tuple[int, ...]:
    if not 0 <= h < 64:
        raise ValueError("hexagram index must lie in [0, 63]")
    return tuple((h >> i) & 1 for i in range(6))


def z4_to_hexagram(k: Sequence[int]) -> tuple[int, ...]:
    if len(k) != 3 or any(not 0 <= x < 4 for x in k):
        raise ValueError("Z4^3 coordinate must have three entries in {0,1,2,3}")
    bits = []
    for x in k:
        bits.extend((x // 2, x % 2))
    return tuple(bits)


def principal_increment(delta: float) -> float:
    return (delta + math.pi) % (2.0 * math.pi) - math.pi


def phase_loop_winding(phases: Sequence[float]) -> int:
    """Integer branch winding on a closed list of vertex phases."""
    if len(phases) < 3:
        raise ValueError("a closed loop needs at least three phase samples")
    increments = [
        principal_increment(phases[(i + 1) % len(phases)] - phases[i])
        for i in range(len(phases))
    ]
    total = sum(increments)
    winding = round(total / (2.0 * math.pi))
    if abs(total - 2.0 * math.pi * winding) > 1e-9:
        raise ArithmeticError("loop sum is not quantized within tolerance")
    return winding


def phase_loop_u1_holonomy(phases: Sequence[float]) -> complex:
    """Wilson product of the exact vertex-phase coboundary; equals one."""
    product = 1.0 + 0.0j
    for i, theta in enumerate(phases):
        nxt = phases[(i + 1) % len(phases)]
        product *= cmath.exp(1j * (nxt - theta))
    return product


def audit() -> dict[str, object]:
    mapping = {
        hexagram_to_z4(integer_to_bits(h))
        for h in range(D)
    }
    inverse = {
        z4_to_hexagram(k)
        for k in ((a, b, c) for a in range(4)
                  for b in range(4) for c in range(4))
    }
    assert len(mapping) == D and len(inverse) == D
    assert all(hexagram_to_z4(z4_to_hexagram(k)) == k
               for k in mapping)

    moments = dirichlet_uniform_moments(D)
    assert math.isclose(moments["mean"], 1 / 64)
    assert math.isclose(
        moments["variance"], 63 / (64**2 * 65))
    assert math.isclose(
        moments["off_diagonal_covariance"], -1 / (64**2 * 65))

    p = born_probabilities([1 / 8] * 64)
    assert len(p) == 64 and math.isclose(sum(p), 1.0)

    loop = [0.0, 2 * math.pi / 3, 4 * math.pi / 3]
    winding = phase_loop_winding(loop)
    holonomy = phase_loop_u1_holonomy(loop)
    assert winding == 1
    assert abs(holonomy - 1.0) < 1e-12

    return {
        "status": "PASS",
        "outcomes": D,
        "born_target": "Dirichlet(1,...,1), uniform on Delta^63",
        "dirichlet_moments": moments,
        "z4_cubed_bijection": True,
        "phase_branch_winding_example": winding,
        "same_loop_u1_coboundary_holonomy": [holonomy.real, holonomy.imag],
        "fdt": "not numerically asserted; requires a specified equilibrium dynamics",
        "frank_burgers": "not numerically asserted; requires calibrated spatial/frame fields",
    }


if __name__ == "__main__":
    import json
    print(json.dumps(audit(), indent=2))
