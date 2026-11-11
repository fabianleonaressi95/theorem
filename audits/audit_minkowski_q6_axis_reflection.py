"""Exact-rational audit of a one-spatial-axis Minkowski reflection on Q6.

The RGS seed convention is big-endian: the last three bits encode signs
(s1,s2,s3). Flipping s1 is integer mask 0b000100 (4). The script checks
the seed reflection, signed cubical chain maps, sector ranks and Betti
numbers. SymPy is used only for exact rational ranks.
"""
from __future__ import annotations

import json
from itertools import combinations, product

import numpy as np
import sympy as sp

from models.q6_topological_synchronization import build_q6_complex
from src.rgs_seed_64_reconstruction import load_rgs_seed_data


def _mask_flip(bits: tuple[int, ...], mask: int) -> tuple[int, ...]:
    return tuple(bit ^ ((mask >> (5 - axis)) & 1)
                 for axis, bit in enumerate(bits))


def _chain_involutions(K, mask: int):
    J0 = np.zeros((64, 64), dtype=np.int64)
    J1 = np.zeros((192, 192), dtype=np.int64)
    J2 = np.zeros((240, 240), dtype=np.int64)

    vertex_map = {
        i: K.vertex_index[_mask_flip(v, mask)]
        for i, v in enumerate(K.vertices)
    }
    for i, j in vertex_map.items():
        J0[j, i] = 1

    for i, (u, v) in enumerate(K.edges):
        ju, jv = vertex_map[u], vertex_map[v]
        target = K.edge_index[(min(ju, jv), max(ju, jv))]
        J1[target, i] = 1 if ju < jv else -1

    face_lookup = {frozenset(cycle): i for i, cycle in enumerate(K.faces)}
    for f, cycle in enumerate(K.faces):
        mapped = tuple(vertex_map[v] for v in cycle)
        target = face_lookup[frozenset(mapped)]
        mapped_boundary = J1 @ K.B2[:, f]
        target_boundary = K.B2[:, target]
        sign = int((mapped_boundary @ target_boundary) // 4)
        if sign not in (-1, 1) or not np.array_equal(
            mapped_boundary, sign * target_boundary
        ):
            raise AssertionError("mapped square boundary has inconsistent orientation")
        J2[target, f] = sign

    return tuple(sp.Matrix(J) for J in (J0, J1, J2))


def _eigenspace_basis(J: sp.Matrix, sign: int) -> sp.Matrix:
    projector_numerator = sp.eye(J.rows) + sign * J
    columns = projector_numerator.columnspace()
    return sp.Matrix.hstack(*columns) if columns else sp.zeros(J.rows, 0)


def _sector_data(B1: sp.Matrix, B2: sp.Matrix, Js, sign: int):
    V0, V1, V2 = (_eigenspace_basis(J, sign) for J in Js)
    d0, d1, d2 = V0.cols, V1.cols, V2.cols
    r1 = (B1 * V1).rank()
    r2 = (B2 * V2).rank()
    return {
        "chain_dimensions": [d0, d1, d2],
        "boundary_ranks": [r1, r2],
        "betti": [d0 - r1, d1 - r1 - r2, d2 - r2],
    }


def run_audit() -> dict:
    K = build_q6_complex()
    B1, B2 = sp.Matrix(K.B1), sp.Matrix(K.B2)
    assert np.count_nonzero(K.B1 @ K.B2) == 0

    seed = load_rgs_seed_data().coordinates
    labels = np.arange(64, dtype=np.int64)
    axis_masks = (4, 2, 1)  # s1, s2, s3 in big-endian sign-fibre order
    seed_reflection_residuals = {}
    sector_results = {}

    for axis, mask in enumerate(axis_masks):
        reflected = seed.copy()
        reflected[:, axis] *= -1.0
        residual = float(np.max(np.abs(seed[labels ^ mask] - reflected)))
        seed_reflection_residuals[str(axis)] = residual

        Js = _chain_involutions(K, mask)
        J0, J1, J2 = Js
        assert all(J * J == sp.eye(J.rows) for J in Js)
        assert J0 * B1 == B1 * J1
        assert J1 * B2 == B2 * J2

        sectors = {
            "even": _sector_data(B1, B2, Js, +1),
            "odd": _sector_data(B1, B2, Js, -1),
        }
        sector_results[str(mask)] = sectors

    # Full inversion is a distinct operation: it flips all three sign bits.
    J_full = _chain_involutions(K, 7)
    full_sectors = {
        "even": _sector_data(B1, B2, J_full, +1),
        "odd": _sector_data(B1, B2, J_full, -1),
    }

    expected = {
        "chain_dimensions": [32, 80, 80],
        "boundary_ranks": [31, 49],
        "betti": [1, 0, 31],
    }
    for mask in axis_masks:
        assert sector_results[str(mask)]["even"] == expected
        assert sector_results[str(mask)]["odd"] == {
            "chain_dimensions": [32, 112, 160],
            "boundary_ranks": [32, 80],
            "betti": [0, 0, 80],
        }
    assert all(value < 1e-12 for value in seed_reflection_residuals.values())
    assert full_sectors["even"]["betti"] == [1, 0, 55]
    assert full_sectors["odd"]["betti"] == [0, 0, 56]

    return {
        "audit": "M2_MINKOWSKI_Q6_ONE_AXIS_REFLECTION_V1",
        "base_complex": {"vertices": 64, "edges": 192, "squares": 240},
        "coordinate_convention": "big-endian labels; last three bits encode (s1,s2,s3)",
        "minkowski_reflection": "X=ct fixed; one selected spatial coordinate changes sign",
        "axis_masks": list(axis_masks),
        "seed_reflection_residuals": seed_reflection_residuals,
        "one_axis_sector_results": sector_results,
        "full_three_axis_inversion_sector_results": full_sectors,
        "checks": {
            "B1B2_zero": bool(np.count_nonzero(K.B1 @ K.B2) == 0),
            "all_three_seed_reflections_exact": all(
                value < 1e-12 for value in seed_reflection_residuals.values()
            ),
            "all_one_axis_chain_maps_exact": True,
            "one_axis_betti_31_80": all(
                sector_results[str(mask)]["even"]["betti"] == [1, 0, 31]
                and sector_results[str(mask)]["odd"]["betti"] == [0, 0, 80]
                for mask in axis_masks
            ),
            "full_inversion_betti_55_56": (
                full_sectors["even"]["betti"] == [1, 0, 55]
                and full_sectors["odd"]["betti"] == [0, 0, 56]
            ),
        },
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
