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


def recursive_shift_shuffle(values: list[int], shift: int) -> list[int]:
    """Port of shuffle_and_billiard_isomorphism.js."""
    length = len(values)
    out = [0] * (2 * length)
    for i in range(length):
        out[2 * i] = values[(i + shift) % length]
        out[2 * i + 1] = values[i]
    return out


def audit_finite_shuffle_billiard_identity(
    size: int = 256, power: int = 7
) -> dict[str, Any]:
    """Reproduce the repository's exact 256x256 finite comparison."""
    if size < 1 or power < 0:
        raise ValueError("size must be positive and power nonnegative")
    scale = 2 ** power
    iterations = 2 * power + 1
    matches = 0
    mismatches = []
    for y in range(size):
        row = [0, 1]
        shift = y * scale
        for _ in range(iterations):
            row = recursive_shift_shuffle(row, shift)
        for x in range(size):
            billiard_bit = (((size - 1 - x) * y) // scale) % 2
            if row[x] == billiard_bit:
                matches += 1
            elif len(mismatches) < 8:
                mismatches.append([x, y, row[x], billiard_bit])
    return {
        "size": size,
        "power": power,
        "scale": scale,
        "shuffle_iterations": iterations,
        "matches": matches,
        "total": size * size,
        "mismatches": mismatches,
        "exact_finite_identity": matches == size * size,
        "scope": "one finite parameter choice; not a general identity proof",
    }


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



def parity_lattice_source_index(
    drawar: list[list[list[int]]], out_x: int, out_y: int, out_z: int, size: int
) -> tuple[tuple[int, int, int], bool]:
    """Exact index map used by permutation3D: parity selects a mode.

    The eight rules are NOT assigned to eight contiguous octants.  They are
    assigned to the eight parity classes (dx,dy,dz) of the doubled lattice.
    """
    if size < 1 or not all(0 <= v < 2 * size for v in (out_x, out_y, out_z)):
        raise ValueError("output voxel coordinate outside doubled cube")
    px, py, pz = out_x // 2, out_y // 2, out_z // 2
    dx, dy, dz = out_x % 2, out_y % 2, out_z % 2
    mode = int(drawar[dz][dy][dx])
    return voxel_source_index(mode, px, py, pz, size)


def audit_parity_lattice_refinement(
    drawar: list[list[list[int]]] | None = None, size: int = 4
) -> dict[str, Any]:
    """Audit whether parity-selected samples define one parent-to-child map.

    A geometric refinement map must send all eight children of one parent
    voxel to the same parent point/cell.  Boolean complement is tracked
    separately because it changes data, not coordinates.
    """
    if drawar is None:
        drawar = [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]
    if len(drawar) != 2 or any(
        len(plane) != 2 or any(len(row) != 2 for row in plane)
        for plane in drawar
    ):
        raise ValueError("drawar must have shape [2][2][2]")
    modes = [int(drawar[z][y][x]) for z in range(2) for y in range(2) for x in range(2)]
    if any(mode < 0 or mode > 15 for mode in modes):
        raise ValueError("Boolean generator modes must lie in [0,15]")

    child_coordinate_consistent = True
    child_value_consistent = True
    inconsistent_parent_count = 0
    for px, py, pz in product(range(size), repeat=3):
        images = []
        complements = []
        for dz, dy, dx in product(range(2), repeat=3):
            mode = int(drawar[dz][dy][dx])
            coord, complement = voxel_source_index(mode, px, py, pz, size)
            images.append(coord)
            complements.append(complement)
        if len(set(images)) != 1:
            child_coordinate_consistent = False
            inconsistent_parent_count += 1
        if len(set(zip(images, complements))) != 1:
            child_value_consistent = False

    # Neighbor jumps in the source-index map across all fine-grid edges.
    jump_histogram: dict[str, int] = {}
    max_l1_jump = 0
    for x, y, z in product(range(2 * size), repeat=3):
        source, _ = parity_lattice_source_index(drawar, x, y, z, size)
        for axis in range(3):
            q = [x, y, z]
            if q[axis] + 1 >= 2 * size:
                continue
            q[axis] += 1
            target, _ = parity_lattice_source_index(drawar, *q, size)
            jump = sum(abs(a - b) for a, b in zip(source, target))
            key = str(jump)
            jump_histogram[key] = jump_histogram.get(key, 0) + 1
            max_l1_jump = max(max_l1_jump, jump)

    return {
        "interpretation": "eight parity sublattices, not eight contiguous octants",
        "drawar_modes_dz_dy_dx": modes,
        "all_eight_children_share_one_source_coordinate": child_coordinate_consistent,
        "all_eight_children_share_one_source_value_rule": child_value_consistent,
        "parents_with_inconsistent_child_coordinates": inconsistent_parent_count,
        "source_index_edge_l1_jump_histogram": jump_histogram,
        "max_source_index_edge_l1_jump": max_l1_jump,
        "geometric_refinement_map_for_arbitrary_data": child_coordinate_consistent,
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

    # Exact finite equality documented in shuffle_and_billiard_isomorphism.js.
    shuffle_billiard = audit_finite_shuffle_billiard_identity()
    assert shuffle_billiard["exact_finite_identity"]
    assert shuffle_billiard["matches"] == 65536

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

    # Source-faithful 3D audit: drawar selects parity classes, not octants.
    parity_uniform = audit_parity_lattice_refinement(size=4)
    assert parity_uniform["all_eight_children_share_one_source_coordinate"]
    assert parity_uniform["geometric_refinement_map_for_arbitrary_data"]
    parity_mixed = audit_parity_lattice_refinement(
        [[[0, 5], [3, 6]], [[1, 4], [2, 7]]], size=4
    )
    assert not parity_mixed["geometric_refinement_map_for_arbitrary_data"]

    return {
        "self_test": "PASS",
        "shuffle_lengths_checked": [2 * n for n in range(1, 65)],
        "finite_shuffle_billiard_identity": shuffle_billiard,
        "fibonacci_last_pair": list(fib[-1]),
        "fibonacci_last_ratio": ratios[-1],
        "phi": phi,
        "symbolic_rows": rows,
        "surface_metric": metric,
        "voxel_reflections": vox,
        "parity_lattice_uniform_rules": parity_uniform,
        "parity_lattice_mixed_rules": parity_mixed,
        "scientific_limit": (
            "The Boolean generator is a parity-sublattice data transform, not "
            "an octant mesh refinement. No cubical incidence chain-map, FEEC "
            "stability, or Mosco convergence claim is established."
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
