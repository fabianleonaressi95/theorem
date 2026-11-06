#!/usr/bin/env python3
"""Exact cubical subdivision chain map and symmetry-naturality audit.

The coarse grid is [0,N]^3 and the fine grid is [0,2N]^3.
A coarse k-cell is sent to the sum of its 2^k oriented fine subcells.
All calculations use integer chains; no metric or floating-point data enter.
"""
from __future__ import annotations

import argparse
import json
from itertools import combinations, permutations, product


Cell = tuple[tuple[int, int, int], tuple[int, ...]]
Chain = dict[Cell, int]
Matrix = tuple[tuple[int, int, int], ...]


def cells(size: int, degree: int):
    for axes in combinations(range(3), degree):
        ranges = [
            range(size) if axis in axes else range(size + 1)
            for axis in range(3)
        ]
        for lower in product(*ranges):
            yield (tuple(lower), tuple(axes))


def boundary(cell: Cell) -> Chain:
    lower, axes = cell
    out: Chain = {}
    for r, axis in enumerate(axes):
        face_axes = tuple(a for a in axes if a != axis)
        low = (lower, face_axes)
        high_lower = list(lower)
        high_lower[axis] += 1
        high = (tuple(high_lower), face_axes)
        out[low] = out.get(low, 0) - (-1) ** r
        out[high] = out.get(high, 0) + (-1) ** r
    return {c: v for c, v in out.items() if v}


def add(chain: Chain, cell: Cell, coefficient: int) -> None:
    if coefficient:
        chain[cell] = chain.get(cell, 0) + coefficient
        if chain[cell] == 0:
            del chain[cell]


def subdivision(cell: Cell) -> Chain:
    """The standard oriented cubical subdivision S_k: C_k(K_N)->C_k(K_2N)."""
    lower, axes = cell
    out: Chain = {}
    for bits in product((0, 1), repeat=len(axes)):
        fine_lower = [2 * x for x in lower]
        for axis, bit in zip(axes, bits):
            fine_lower[axis] += bit
        add(out, (tuple(fine_lower), axes), 1)
    return out


def permutation_sign(values: tuple[int, ...]) -> int:
    inv = sum(values[i] > values[j]
              for i in range(len(values)) for j in range(i + 1, len(values)))
    return -1 if inv % 2 else 1


def map_cell(cell: Cell, matrix: Matrix, size: int) -> tuple[Cell, int]:
    lower, axes = cell
    vertices = []
    for bits in product((0, 1), repeat=len(axes)):
        point = list(lower)
        for axis, bit in zip(axes, bits):
            point[axis] += bit
        image = []
        for row in matrix:
            j = next(q for q, value in enumerate(row) if value)
            image.append(point[j] if row[j] == 1 else size - point[j])
        vertices.append(tuple(image))
    target_lower = tuple(min(v[i] for v in vertices) for i in range(3))
    target_axes = tuple(i for i in range(3)
                        if max(v[i] for v in vertices) != min(v[i] for v in vertices))
    source_to_target = {
        j: next(i for i, row in enumerate(matrix) if row[j])
        for j in axes
    }
    ordered = [source_to_target[j] for j in axes]
    positions = tuple(target_axes.index(i) for i in ordered)
    orientation = permutation_sign(positions)
    for source_axis, target_axis in source_to_target.items():
        orientation *= matrix[target_axis][source_axis]
    return (target_lower, target_axes), orientation


def map_chain(chain: Chain, matrix: Matrix, size: int) -> Chain:
    out: Chain = {}
    for cell, coefficient in chain.items():
        image, sign = map_cell(cell, matrix, size)
        add(out, image, coefficient * sign)
    return out


def boundary_chain(chain: Chain) -> Chain:
    out: Chain = {}
    for cell, coefficient in chain.items():
        for face, sign in boundary(cell).items():
            add(out, face, coefficient * sign)
    return out


def subdivide_chain(chain: Chain) -> Chain:
    out: Chain = {}
    for cell, coefficient in chain.items():
        for fine_cell, sign in subdivision(cell).items():
            add(out, fine_cell, coefficient * sign)
    return out


def cube_symmetries() -> list[Matrix]:
    """All 3! * 2^3 signed permutation matrices (the full cube symmetry group)."""
    result = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = []
            for target_axis in range(3):
                row = [0, 0, 0]
                row[perm[target_axis]] = signs[target_axis]
                rows.append(tuple(row))
            result.append(tuple(rows))
    return result


def audit(size: int = 2) -> dict:
    if size < 1:
        raise ValueError("size must be positive")
    checked = {str(k): 0 for k in range(4)}
    chain_failures = []
    naturality_failures = []
    symmetries = cube_symmetries()

    for degree in range(4):
        for cell in cells(size, degree):
            checked[str(degree)] += 1
            lhs = boundary_chain(subdivision(cell))
            rhs = subdivide_chain(boundary(cell))
            if lhs != rhs:
                chain_failures.append({
                    "degree": degree, "cell": repr(cell),
                    "boundary_after_subdivision": repr(lhs),
                    "subdivision_after_boundary": repr(rhs),
                })
                break

            # T_(2N) S = S T_N for each signed coordinate permutation.
            for matrix in symmetries:
                left = map_chain(subdivision(cell), matrix, 2 * size)
                coarse_image, orientation = map_cell(cell, matrix, size)
                right = {
                    fine: coefficient * orientation
                    for fine, coefficient in subdivision(coarse_image).items()
                }
                if left != right:
                    naturality_failures.append({
                        "degree": degree, "cell": repr(cell),
                        "matrix": matrix,
                        "map_after_subdivision": repr(left),
                        "subdivision_after_map": repr(right),
                    })
                    break
            if naturality_failures:
                break
        if chain_failures or naturality_failures:
            break

    return {
        "coarse_grid": f"[0,{size}]^3",
        "fine_grid": f"[0,{2 * size}]^3",
        "cells_checked_by_degree": checked,
        "signed_permutation_symmetries_checked": len(symmetries),
        "subdivision_chain_identity": not chain_failures,
        "symmetry_naturality_identity": not naturality_failures,
        "chain_failures": chain_failures,
        "naturality_failures": naturality_failures,
        "interpretation": (
            "Exact integer chain map for standard cubical subdivision, "
            "equivariant under all 48 signed-permutation cube symmetries. "
            "This does not prove that Herasymov's mixed parity recursion "
            "equals this subdivision or defines a conforming geometric mesh."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--size", type=int, default=2)
    parser.add_argument("--output")
    args = parser.parse_args()
    report = audit(args.size)
    rendered = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as stream:
            stream.write(rendered + "\n")
    print(rendered)
    return 0 if report["subdivision_chain_identity"] and report["symmetry_naturality_identity"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
