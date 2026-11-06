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
from itertools import combinations, product
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
    """Audit whether parity-selected samples agree on each parent voxel.

    A parent-cell sampling rule is single-valued only if all eight children
    of one parent voxel sample the same parent source index. This is not a
    geometric cell map or a cubical chain map.  Boolean complement is tracked
    separately because it changes data, not coordinates.
    """
    """Check whether the eight parity children agree on their parent source voxel."""
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
        "single_parent_source_coordinate_per_parent": child_coordinate_consistent,
    }


# Source-faithful coordinate semantics of perfect-shuffle/fractal_3d_with_rotaions.js.
def rotated_voxel_coordinate(
    x: int, y: int, z: int, size: int, axis: int, angle: int
) -> tuple[int, int, int]:
    """Port the source's repeated quarter-turn formulas, in their exact order."""
    if size < 1 or axis not in (0, 1, 2, 3) or angle not in (0, 1, 2, 3):
        raise ValueError("invalid cube size, rotation axis, or quarter-turn count")
    for _ in range(angle):
        if axis == 1:
            x, y, z = x, size - 1 - z, y
        elif axis == 2:
            x, y, z = z, y, size - 1 - x
        elif axis == 3:
            x, y, z = size - 1 - y, x, z
        # axis == 0 deliberately means no rotation for every angle.
    return x, y, z


def rotation_generator_source_index(
    mode: int, x: int, y: int, z: int, size: int
) -> tuple[tuple[int, int, int], bool]:
    """Return source voxel and whether switchdraw increments its scalar value."""
    if not 0 <= mode <= 255 or size < 1:
        raise ValueError("mode must be in [0,255] and size positive")
    if not all(0 <= v < size for v in (x, y, z)):
        raise ValueError("voxel coordinate outside source cube")
    axis = (mode >> 4) & 3
    angle = (mode >> 6) & 3
    xr, yr, zr = rotated_voxel_coordinate(x, y, z, size, axis, angle)
    fx, fy, fz = _REFLECTIONS[mode & 7]
    coord = (
        size - 1 - xr if fx else xr,
        size - 1 - yr if fy else yr,
        size - 1 - zr if fz else zr,
    )
    # The source executes: if (!(mode & 8)) a++;
    increment = (mode & 8) == 0
    return coord, increment


def _det3(matrix: tuple[tuple[int, int, int], ...]) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def rotation_generator_affine_data(
    mode: int, size: int = 5
) -> tuple[tuple[tuple[int, int, int], ...], int]:
    """Recover signed-permutation linear part and orientation from exact samples."""
    if size < 2:
        raise ValueError("size must be at least 2")
    origin = rotation_generator_source_index(mode, 0, 0, 0, size)[0]
    columns = []
    for e in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
        image = rotation_generator_source_index(mode, *e, size)[0]
        columns.append(tuple(image[i] - origin[i] for i in range(3)))
    matrix = tuple(
        tuple(columns[j][i] for j in range(3)) for i in range(3)
    )
    return matrix, _det3(matrix)


def audit_rotation_generator(size: int = 4) -> dict[str, Any]:
    """Exhaust all 256 source modes and distinguish coordinate from value action."""
    if size < 2:
        raise ValueError("size must be at least 2")
    points = list(product(range(size), repeat=3))
    mode_reports = []
    coordinate_maps: dict[tuple[tuple[int, int, int], ...], list[int]] = {}
    orientation_counts = {"+1": 0, "-1": 0}
    increment_counts = {"increment": 0, "unchanged": 0}
    for mode in range(256):
        images = [rotation_generator_source_index(mode, *p, size)[0] for p in points]
        increment = rotation_generator_source_index(mode, 0, 0, 0, size)[1]
        matrix, determinant = rotation_generator_affine_data(mode, max(size, 3))
        bijective = len(set(images)) == size ** 3
        coordinate_maps.setdefault(tuple(images), []).append(mode)
        orientation_counts["+1" if determinant > 0 else "-1"] += 1
        increment_counts["increment" if increment else "unchanged"] += 1
        mode_reports.append({
            "mode": mode,
            "axis": (mode >> 4) & 3,
            "quarter_turns": (mode >> 6) & 3,
            "reflection_code": mode & 7,
            "signed_permutation_matrix": [list(row) for row in matrix],
            "orientation_determinant": determinant,
            "coordinate_bijection": bijective,
            "scalar_increment": increment,
        })
    multiplicities = {}
    for modes in coordinate_maps.values():
        key = str(len(modes))
        multiplicities[key] = multiplicities.get(key, 0) + 1
    bit3_coordinate_invariant = all(
        rotation_generator_source_index(mode, *p, size)[0]
        == rotation_generator_source_index(mode ^ 8, *p, size)[0]
        for mode in range(256) for p in points
    )
    bit3_toggles_scalar_increment = all(
        rotation_generator_source_index(mode, 0, 0, 0, size)[1]
        != rotation_generator_source_index(mode ^ 8, 0, 0, 0, size)[1]
        for mode in range(256)
    )
    return {
        "source": "fractal_3d_with_rotaions.js",
        "modes_exhausted": 256,
        "all_coordinate_maps_bijective": all(m["coordinate_bijection"] for m in mode_reports),
        "distinct_coordinate_maps": len(coordinate_maps),
        "map_multiplicity_histogram": multiplicities,
        "orientation_counts_over_modes": orientation_counts,
        "scalar_action_counts": increment_counts,
        "scalar_rule": "increment by one iff (mode & 8) == 0; otherwise unchanged",
        "no_boolean_complement": True,
        "bit3_preserves_coordinates": bit3_coordinate_invariant,
        "bit3_toggles_increment_rule": bit3_toggles_scalar_increment,
        "mode_reports": mode_reports,
    }


def audit_rotation_parity_lattice(
    drawar: list[list[list[int]]], size: int = 4
) -> dict[str, Any]:
    """Check parity-selected rotation rules as data samplers, not cell maps."""
    if len(drawar) != 2 or any(
        len(plane) != 2 or any(len(row) != 2 for row in plane)
        for plane in drawar
    ):
        raise ValueError("drawar must have shape [2][2][2]")
    modes = [int(drawar[z][y][x]) for z in range(2) for y in range(2) for x in range(2)]
    if any(mode < 0 or mode > 255 for mode in modes):
        raise ValueError("rotation generator modes must lie in [0,255]")
    coordinate_consistent = True
    scalar_rule_consistent = True
    for parent in product(range(size), repeat=3):
        samples = [
            rotation_generator_source_index(int(drawar[dz][dy][dx]), *parent, size)
            for dz, dy, dx in product(range(2), repeat=3)
        ]
        if len({coord for coord, _ in samples}) != 1:
            coordinate_consistent = False
        if len(set(samples)) != 1:
            scalar_rule_consistent = False
    return {
        "interpretation": "eight parity sublattices, not contiguous octants",
        "modes_dz_dy_dx": modes,
        "same_parent_source_coordinate_for_all_eight_children": coordinate_consistent,
        "same_coordinate_and_scalar_action_for_all_eight_children": scalar_rule_consistent,
        "single_parent_sample_rule": coordinate_consistent and scalar_rule_consistent,
    }


# Exact cubical chain complex and induced maps for uniform signed permutations.
def _cube_cells(size: int, degree: int):
    """Canonical positively oriented k-cells of the cubical grid [0,size]^3."""
    if size < 1 or degree not in (0, 1, 2, 3):
        raise ValueError("size must be positive and degree in {0,1,2,3}")
    for axes in combinations(range(3), degree):
        ranges = [
            range(size) if axis in axes else range(size + 1)
            for axis in range(3)
        ]
        for lower in product(*ranges):
            yield (tuple(lower), tuple(axes))


def _cube_boundary(cell):
    """Boundary of an oriented cubical cell, as an integer coefficient map."""
    lower, axes = cell
    out = {}
    for r, axis in enumerate(axes):
        face_axes = tuple(a for a in axes if a != axis)
        low_face = (lower, face_axes)
        high_lower = list(lower)
        high_lower[axis] += 1
        high_face = (tuple(high_lower), face_axes)
        out[low_face] = out.get(low_face, 0) - ((-1) ** r)
        out[high_face] = out.get(high_face, 0) + ((-1) ** r)
    return {cell: coeff for cell, coeff in out.items() if coeff}


def _permutation_sign(values):
    inversions = sum(
        values[i] > values[j]
        for i in range(len(values)) for j in range(i + 1, len(values))
    )
    return -1 if inversions % 2 else 1


def _map_cube_cell(cell, matrix, size: int):
    """Push an oriented cell through x -> signed-permutation(x) on [0,N]^3."""
    lower, axes = cell
    vertices = []
    for bits in product((0, 1), repeat=len(axes)):
        point = list(lower)
        for axis, bit in zip(axes, bits):
            point[axis] += bit
        image = []
        for row in matrix:
            source_axis = next(j for j, value in enumerate(row) if value)
            sign = row[source_axis]
            image.append(point[source_axis] if sign == 1 else size - point[source_axis])
        vertices.append(tuple(image))
    target_lower = tuple(min(v[i] for v in vertices) for i in range(3))
    target_axes = tuple(
        i for i in range(3)
        if max(v[i] for v in vertices) != min(v[i] for v in vertices)
    )
    source_to_target_axis = {
        j: next(i for i, row in enumerate(matrix) if row[j])
        for j in axes
    }
    ordered_target_axes = [source_to_target_axis[j] for j in axes]
    target_positions = [target_axes.index(i) for i in ordered_target_axes]
    orientation = _permutation_sign(target_positions)
    for source_axis, target_axis in source_to_target_axis.items():
        orientation *= matrix[target_axis][source_axis]
    return (target_lower, target_axes), orientation


def _add_chain_term(chain, cell, coefficient):
    if coefficient:
        chain[cell] = chain.get(cell, 0) + coefficient
        if chain[cell] == 0:
            del chain[cell]


def _mapped_boundary(cell, matrix, size: int):
    """Apply P_{k-1} to boundary(cell)."""
    out = {}
    for face, coefficient in _cube_boundary(cell).items():
        image, orientation = _map_cube_cell(face, matrix, size)
        _add_chain_term(out, image, coefficient * orientation)
    return out


def _boundary_of_mapped_cell(cell, matrix, size: int):
    """Apply boundary after P_k to cell."""
    image, orientation = _map_cube_cell(cell, matrix, size)
    return {
        face: coefficient * orientation
        for face, coefficient in _cube_boundary(image).items()
    }


def audit_uniform_cubical_chain_maps(size: int = 2) -> dict[str, Any]:
    """Exhaust the distinct rotation-generator signed permutations.

    This proves an automorphism of the fixed cubical grid, not a refinement
    operator between different mesh levels.
    """
    if size < 1:
        raise ValueError("size must be positive")
    matrices = {}
    for mode in range(256):
        matrix, determinant = rotation_generator_affine_data(mode, max(size, 3))
        matrices[matrix] = determinant
    checked = {str(k): 0 for k in range(4)}
    failures = []
    for matrix, determinant in matrices.items():
        for degree in range(4):
            for cell in _cube_cells(size, degree):
                checked[str(degree)] += 1
                lhs = _boundary_of_mapped_cell(cell, matrix, size)
                rhs = _mapped_boundary(cell, matrix, size)
                if lhs != rhs:
                    failures.append({
                        "matrix": [list(row) for row in matrix],
                        "degree": degree,
                        "cell": repr(cell),
                        "boundary_after_map": repr(lhs),
                        "map_after_boundary": repr(rhs),
                    })
                    if len(failures) >= 5:
                        break
            if failures:
                break
        if failures:
            break
    return {
        "grid": f"[0,{size}]^3",
        "distinct_signed_permutation_maps": len(matrices),
        "orientation_determinants": {
            "+1": sum(det == 1 for det in matrices.values()),
            "-1": sum(det == -1 for det in matrices.values()),
        },
        "cells_checked_by_degree_across_all_maps": checked,
        "chain_map_identity_holds": not failures,
        "failures": failures,
        "interpretation": (
            "Each uniform signed-permutation mode induces an exact cubical "
            "chain automorphism on the fixed grid. This is not a coarse-to-fine "
            "refinement/prolongation map."
        ),
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
    assert parity_uniform["single_parent_source_coordinate_per_parent"]
    parity_mixed = audit_parity_lattice_refinement(
        [[[0, 5], [3, 6]], [[1, 4], [2, 7]]], size=4
    )
    assert not parity_mixed["single_parent_source_coordinate_per_parent"]

    rotation = audit_rotation_generator(size=3)
    assert rotation["modes_exhausted"] == 256
    assert rotation["all_coordinate_maps_bijective"]
    assert rotation["distinct_coordinate_maps"] == 32
    assert rotation["orientation_counts_over_modes"] == {"+1": 128, "-1": 128}
    assert rotation["scalar_action_counts"] == {"increment": 128, "unchanged": 128}
    assert rotation["bit3_preserves_coordinates"]
    assert rotation["bit3_toggles_increment_rule"]
    uniform_rotation = audit_rotation_parity_lattice(
        [[[0, 0], [0, 0]], [[0, 0], [0, 0]]], size=3
    )
    mixed_rotation = audit_rotation_parity_lattice(
        [[[0, 16], [64, 80]], [[32, 48], [96, 112]]], size=3
    )
    assert uniform_rotation["single_parent_sample_rule"]
    assert not mixed_rotation["single_parent_sample_rule"]

    cubical_chain = audit_uniform_cubical_chain_maps(size=2)
    assert cubical_chain["distinct_signed_permutation_maps"] == 32
    assert cubical_chain["chain_map_identity_holds"]

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
        "rotation_generator": rotation,
        "rotation_parity_uniform_rules": uniform_rotation,
        "rotation_parity_mixed_rules": mixed_rotation,
        "scientific_limit": (
            "The Boolean generator is a parity-sublattice data transform, not "
            "an octant mesh refinement. No cubical incidence chain-map, FEEC "
            "stability, or Mosco convergence claim is established."
        "uniform_cubical_chain_maps": cubical_chain,
        "scientific_limit": (
            "Uniform signed-permutation modes induce exact chain automorphisms "
            "of the fixed cubical grid. The mixed parity generator still has no "
            "proved coarse-to-fine cubical refinement map; FEEC stability and "
            "Mosco convergence remain open."
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
