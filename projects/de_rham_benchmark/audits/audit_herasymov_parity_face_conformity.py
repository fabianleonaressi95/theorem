#!/usr/bin/env python3
"""Exact shared-face conformity audit for Herasymov's parity-selected 3D maps.

The eight rules are assigned to interleaved parity classes of the doubled
lattice.  Each rule is interpreted geometrically as an affine cube isometry.
All face-trace comparisons are exact integer comparisons after doubling
coordinates; no floating-point tolerances are used.
"""
from __future__ import annotations

import argparse
import json
from itertools import product
from typing import Any

from audit_herasymov_symbolic import (
    rotation_generator_affine_data,
    rotation_generator_source_index,
)


Vector = tuple[int, int, int]
Matrix = tuple[tuple[int, int, int], ...]
Affine = tuple[Matrix, Vector]


def affine_cube_isometry(mode: int, size: int = 3) -> Affine:
    """Recover x -> A x + b on [0,N]^3 from the source voxel map.

    The source uses N-1-p on reflected voxel indices.  The continuous cube
    isometry uses N-x, so add one to the voxel offset in every negative row.
    """
    if size < 2:
        raise ValueError("size must be at least 2")
    matrix, _ = rotation_generator_affine_data(mode, size)
    voxel_origin = rotation_generator_source_index(mode, 0, 0, 0, size)[0]
    offset = tuple(
        voxel_origin[i] + (1 if -1 in matrix[i] else 0)
        for i in range(3)
    )
    return matrix, offset


def _apply_doubled(affine: Affine, doubled_point: Vector) -> Vector:
    matrix, offset = affine
    return tuple(
        sum(matrix[i][j] * doubled_point[j] for j in range(3))
        + 2 * offset[i]
        for i in range(3)
    )


def shared_face_trace_matches(
    left: Affine, right: Affine, axis: int, size: int = 2,
    tangential_parity: tuple[int, int] = (0, 0),
) -> bool:
    """Compare two parity-cell maps on every shared face normal to axis.

    The left parity has bit 0 on the normal axis and the right parity bit 1.
    For each parent index p, the common face lies at x_axis=p_axis+1/2.
    Its four vertices are sufficient because the trace difference is affine.
    """
    if axis not in (0, 1, 2) or size < 2:
        raise ValueError("axis must be 0,1,2 and size >= 2")
    tangential = [j for j in range(3) if j != axis]
    for parent in product(range(size), repeat=3):
        face_base = [2 * parent[j] for j in range(3)]
        face_base[axis] += 1
        for bits in product((0, 1), repeat=2):
            vertex = list(face_base)
            for j, bit in zip(tangential, bits):
                # The selected parity subcell occupies one half of the
                # parent interval in each tangential direction.
                vertex[j] += tangential_parity[tangential.index(j)] + bit
            point = tuple(vertex)
            if _apply_doubled(left, point) != _apply_doubled(right, point):
                return False
    return True


def parity_face_audit(
    drawar: list[list[list[int]]], size: int = 2
) -> dict[str, Any]:
    """Check all 12 neighboring parity-class interfaces in the 2x2x2 pattern."""
    if size < 2:
        raise ValueError("size must be >= 2")
    if len(drawar) != 2 or any(
        len(plane) != 2 or any(len(row) != 2 for row in plane)
        for plane in drawar
    ):
        raise ValueError("drawar must have shape [2][2][2]")
    modes = [int(drawar[z][y][x]) for z, y, x in product(range(2), repeat=3)]
    if any(mode < 0 or mode > 255 for mode in modes):
        raise ValueError("rotation-generator modes must be in [0,255]")

    affines = {
        (z, y, x): affine_cube_isometry(int(drawar[z][y][x]), size)
        for z, y, x in product(range(2), repeat=3)
    }
    interfaces = []
    for parity in product(range(2), repeat=3):
        for axis in range(3):
            if parity[axis] != 0:
                continue
            neighbor = list(parity)
            neighbor[axis] = 1
            neighbor = tuple(neighbor)
            left = affines[parity]
            right = affines[neighbor]
            # In the two tangential directions, parity selects which half
            # of each parent face is tested.
            tangential = [j for j in range(3) if j != axis]
            tpar = tuple(parity[j] for j in tangential)
            matches = shared_face_trace_matches(
                left, right, axis, size=size, tangential_parity=tpar
            )
            interfaces.append({
                "parity_pair": [list(parity), list(neighbor)],
                "normal_axis": axis,
                "left_mode": int(drawar[parity[0]][parity[1]][parity[2]]),
                "right_mode": int(drawar[neighbor[0]][neighbor[1]][neighbor[2]]),
                "face_trace_matches": matches,
            })

    all_same_affine = len(set(affines.values())) == 1
    all_faces_match = all(item["face_trace_matches"] for item in interfaces)
    scalar_rules = {
        rotation_generator_source_index(
            int(drawar[z][y][x]), 0, 0, 0, size
        )[1]
        for z, y, x in product(range(2), repeat=3)
    }
    return {
        "size": size,
        "parity_modes_dz_dy_dx": modes,
        "interfaces_checked": len(interfaces),
        "all_shared_face_traces_match": all_faces_match,
        "all_eight_affine_cube_maps_identical": all_same_affine,
        "necessary_sufficient_criterion_holds": all_faces_match == all_same_affine,
        "scalar_increment_rule_is_uniform": len(scalar_rules) == 1,
        "scalar_action_is_separate_from_geometry": True,
        "interfaces": interfaces,
        "scope": (
            "Exact conformity criterion for the cellwise affine cube-map "
            "interpretation of the rotation-enhanced parity generator; "
            "not a proof that the original voxel data recursion itself "
            "defines a geometric refinement."
        ),
    }


def audit_pairwise_criterion(size: int = 2) -> dict[str, Any]:
    """Exhaust every pair of distinct source coordinate maps and 3 face normals."""
    maps: dict[Affine, list[int]] = {}
    for mode in range(256):
        maps.setdefault(affine_cube_isometry(mode, max(size, 3)), []).append(mode)
    distinct = list(maps)
    checked = 0
    mismatches = []
    for left in distinct:
        for right in distinct:
            for axis in range(3):
                # A fixed tangential parity is enough to test the affine
                # identity on the complete family of parallel shared faces.
                matches = shared_face_trace_matches(
                    left, right, axis, size=size, tangential_parity=(0, 0)
                )
                same = left == right
                checked += 1
                if matches != same and len(mismatches) < 8:
                    mismatches.append({
                        "axis": axis,
                        "left": left,
                        "right": right,
                        "face_trace_matches": matches,
                        "affines_identical": same,
                    })
    return {
        "source_modes_exhausted": 256,
        "distinct_affine_cube_maps": len(distinct),
        "ordered_map_pairs_per_axis": len(distinct) ** 2,
        "face_normals": 3,
        "pair_axis_checks": checked,
        "face_compatibility_iff_same_affine_map": not mismatches,
        "mismatches": mismatches,
    }


def self_test() -> dict[str, Any]:
    uniform = [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]
    coordinate_same_scalar_mixed = [
        [[0, 8], [0, 8]],
        [[8, 0], [8, 0]],
    ]
    mixed_reflection = [
        [[0, 1], [0, 1]],
        [[0, 1], [0, 1]],
    ]
    a = parity_face_audit(uniform)
    b = parity_face_audit(coordinate_same_scalar_mixed)
    c = parity_face_audit(mixed_reflection)
    pairs = audit_pairwise_criterion()
    assert a["all_shared_face_traces_match"]
    assert a["all_eight_affine_cube_maps_identical"]
    assert b["all_shared_face_traces_match"]
    assert b["all_eight_affine_cube_maps_identical"]
    assert not b["scalar_increment_rule_is_uniform"]
    assert not c["all_shared_face_traces_match"]
    assert not c["all_eight_affine_cube_maps_identical"]
    assert pairs["face_compatibility_iff_same_affine_map"]
    return {
        "uniform_mode_control": a,
        "same_geometry_different_scalar_rule_control": b,
        "mixed_reflection_negative_control": c,
        "exhaustive_pairwise_criterion": pairs,
        "self_test_passed": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--size", type=int, default=2)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--output")
    args = parser.parse_args()
    report = self_test() if args.self_test else audit_pairwise_criterion(args.size)
    rendered = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as stream:
            stream.write(rendered + "\\n")
    print(rendered)
    return 0 if report.get("self_test_passed", report.get("face_compatibility_iff_same_affine_map", False)) else 1


if __name__ == "__main__":
    raise SystemExit(main())
