#!/usr/bin/env python3
"""Independent finite/algebraic checks of selected Herasymov constructions.

This is a source-faithful audit of the public billiard-fractals and
perfect-shuffle implementations. It deliberately does not claim that their
voxel recursions are conforming geometric meshes or FEEC chain maps.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from itertools import product
from typing import Any


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)


def herasymov_sequence(m: int, n: int) -> list[int]:
    """Port of billiard-fractals/js/sequences.js sequence(m,n)."""
    if m <= 0 or m % 2:
        raise ValueError("the source routine requires positive even m")
    out = [1] * (m // 2)
    for k in range(m // 2):
        if ((2 * k * n) // m) % 2 == 0:
            out[((2 * k * n) % m) // 2] = 0
    return out


def in_shuffle_forward(i: int, n: int) -> int:
    """Source element at i moves to 2*i+1 modulo 2*n+1."""
    if n < 1 or not 0 <= i < 2 * n:
        raise ValueError("require n>=1 and 0<=i<2n")
    return (2 * i + 1) % (2 * n + 1)


def multiplicative_order_two(modulus: int) -> int:
    if modulus <= 1 or gcd(2, modulus) != 1:
        raise ValueError("2 must be invertible modulo modulus > 1")
    value, order = 2 % modulus, 1
    while value != 1:
        value = (2 * value) % modulus
        order += 1
        if order > modulus * 2:
            raise AssertionError("unexpected failure to find multiplicative order")
    return order


def shuffle_period(n: int) -> int:
    return multiplicative_order_two(2 * n + 1)


def fibonacci_pair(k: int) -> tuple[int, int]:
    if k < 1:
        raise ValueError("k must be >=1")
    a, b = 1, 1
    for _ in range(k - 1):
        a, b = b, a + b
    return a, b


def surface_graph(
    x: float, y: float, *, a: float, b: float, c: float,
    d: float, c4: float = 0.0
) -> dict[str, float]:
    """Source-code convention z=a*(c4^2+x^2+b*x*y+c*y^2)^(1/d)."""
    if d == 0:
        raise ValueError("d must be nonzero")
    q = c4 * c4 + x * x + b * x * y + c * y * y
    p = 1.0 / d
    if q <= 0 and not float(p).is_integer():
        raise ValueError("fractional power requires q>0 in the real branch")
    if q == 0 and p < 1:
        raise ValueError("graph derivative may be singular at q=0")
    z = a * (q ** p)
    if q == 0:
        zx = 0.0 if p > 1 else float("nan")
        zy = 0.0 if p > 1 else float("nan")
    else:
        factor = a * p * (q ** (p - 1.0))
        zx = factor * (2.0 * x + b * y)
        zy = factor * (b * x + 2.0 * c * y)
    g11 = 1.0 + zx * zx
    g12 = zx * zy
    g22 = 1.0 + zy * zy
    detg = g11 * g22 - g12 * g12
    return {
        "q": q, "z": z, "zx": zx, "zy": zy,
        "g11": g11, "g12": g12, "g22": g22,
        "det_g": detg, "det_g_expected": 1.0 + zx * zx + zy * zy,
    }


# Source-faithful coordinate maps from perfect-shuffle/fractal_3d_2.js.
# Mode 8..15 repeats the corresponding coordinate reflection and complements
# the Boolean value. Coordinate maps are indexed by mode modulo eight.
_REFLECTIONS = (
    (False, False, False),  # 0: x,y,z
    (False, False, True),   # 1: x,y,N-1-z
    (False, True, True),    # 2: x,N-1-y,N-1-z
    (False, True, False),   # 3: x,N-1-y,z
    (True, True, False),    # 4: N-1-x,N-1-y,z
    (True, False, False),   # 5: N-1-x,y,z
    (True, False, True),    # 6: N-1-x,y,N-1-z
    (True, True, True),     # 7: N-1-x,N-1-y,N-1-z
)


def voxel_source_index(
    mode: int, x: int, y: int, z: int, size: int
) -> tuple[tuple[int, int, int], bool]:
    if not 0 <= mode < 16 or size < 1:
        raise ValueError("mode must be in [0,15] and size positive")
    if not all(0 <= v < size for v in (x, y, z)):
        raise ValueError("voxel coordinate outside source cube")
    fx, fy, fz = _REFLECTIONS[mode % 8]
    coord = (
        size - 1 - x if fx else x,
        size - 1 - y if fy else y,
        size - 1 - z if fz else z,
    )
    return coord, mode >= 8


def audit_voxel_reflections(size: int = 4) -> dict[str, Any]:
    coords = list(product(range(size), repeat=3))
    modes = []
    for mode in range(16):
        images = [voxel_source_index(mode, *p, size)[0] for p in coords]
        modes.append({
            "mode": mode,
            "is_bijection": len(set(images)) == size ** 3,
            "boolean_complement": mode >= 8,
            "reflection_determinant": (
                -1 if sum(_REFLECTIONS[mode % 8]) % 2 else 1
            ),
        })
    return {
        "source_cube_size": size,
        "modes": modes,
        "all_coordinate_maps_bijective": all(m["is_bijection"] for m in modes),
        "orientation_reversing_modes": [
            m["mode"] for m in modes if m["reflection_determinant"] < 0
        ],
    }


def self_test() -> dict[str, Any]:
    # Finite in-shuffle permutation and its multiplicative-order period.
    shuffle_checks = []
    for n in range(1, 65):
        image = [in_shuffle_forward(i, n) for i in range(2 * n)]
        assert len(set(image)) == 2 * n
        period = shuffle_period(n)
        assert all(
            pow(2, period, 2 * n + 1) == 1
            for _ in (0,)
        )
        # Verify the permutation itself returns after the claimed period.
        current = list(range(2 * n))
        for _ in range(period):
            nxt = [None] * (2 * n)
            for old, value in enumerate(current):
                nxt[in_shuffle_forward(old, n)] = value
            current = nxt
        assert current == list(range(2 * n))
        shuffle_checks.append({"n": n, "length": 2 * n, "period": period})

    # Fibonacci aspect ratios converge to phi.
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    fib = [fibonacci_pair(k) for k in range(1, 18)]
    ratios = [b / a for a, b in fib]
    assert abs(ratios[-1] - phi) < 1e-6

    # Port of the finite symbolic row routine; preserve exact outputs.
    rows = {
        f"{m},{n}": herasymov_sequence(m, n)
        for m, n in ((8, 13), (14, 21), (16, 21), (34, 55))
    }
    assert all(len(v) == int(k.split(",")[0]) // 2 for k, v in rows.items())
    assert all(set(v) <= {0, 1} for v in rows.values())

    # Induced metric identity on a positive-domain graph patch.
    metric = surface_graph(
        0.3, -0.2, a=0.7, b=0.4, c=1.2, d=1.01, c4=0.5
    )
    assert abs(metric["det_g"] - metric["det_g_expected"]) < 1e-12
    assert metric["det_g"] > 0

    vox = audit_voxel_reflections(4)
    assert vox["all_coordinate_maps_bijective"]
    assert len(vox["modes"]) == 16

    return {
        "self_test": "PASS",
        "shuffle_lengths_checked": [2 * n for n in range(1, 65)],
        "fibonacci_last_pair": list(fib[-1]),
        "fibonacci_last_ratio": ratios[-1],
        "phi": phi,
        "symbolic_rows": rows,
        "surface_metric": metric,
        "voxel_reflections": vox,
        "scientific_limit": (
            "No shared-octant face-trace, geometric mesh conformity, chain-map, "
            "FEEC stability, or Mosco convergence claim is tested."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--output")
    args = parser.parse_args()
    if not args.self_test:
        parser.error("run with --self-test")
    report = self_test()
    rendered = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(rendered + "\n")
    print(rendered)
    return 0


if __name__ == "__main__":
    sys.exit(main())
