#!/usr/bin/env python3
"""Exact edge-index alignment between the RGS seed ordering and canonical Q6.

The RGS archive ordering is vertex-major with least-significant-bit axes.
The canonical Q6 complex uses lexicographically sorted endpoint pairs and
big-endian axis labels. This script constructs the permutation between them.
It does not load or reinterpret archived SO(3)/SU(2) transport payloads.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

from src.rgs_seed_64_reconstruction import load_rgs_seed_data

EXPECTED_RGS_EDGE_SHA256 = "da7854ca655577b629dc508208918326fde1d50563485f953ea0fdc1b2fb78e8"


def rgs_archive_edges() -> np.ndarray:
    """Reconstruct the archived (tail, head, LSB-axis) edge ordering."""
    edges = []
    for vertex in range(64):
        for axis_lsb in range(6):
            mask = 1 << axis_lsb
            if (vertex & mask) == 0:
                edges.append((vertex, vertex | mask, axis_lsb))
    return np.asarray(edges, dtype=np.int16)


def canonical_q6_edges() -> np.ndarray:
    """Canonical Q6 edges: lexicographic endpoint pairs, big-endian axes."""
    edge_set = set()
    for vertex in range(64):
        for axis_be in range(6):
            neighbour = vertex ^ (1 << (5 - axis_be))
            if vertex < neighbour:
                edge_set.add((vertex, neighbour))
    return np.asarray(sorted(edge_set), dtype=np.int16)


def audit_edge_order_alignment() -> dict:
    seed = load_rgs_seed_data()  # independently verifies the 64x3 coordinate hash
    if seed.coordinates.shape != (64, 3):
        raise AssertionError("unexpected RGS coordinate shape")

    rgs_edges = rgs_archive_edges()
    canonical_edges = canonical_q6_edges()
    if rgs_edges.shape != (192, 3) or canonical_edges.shape != (192, 2):
        raise AssertionError("unexpected Q6 edge count or shape")

    edge_digest = hashlib.sha256(
        np.ascontiguousarray(rgs_edges, dtype="<i8").tobytes(order="C")
    ).hexdigest()
    if edge_digest != EXPECTED_RGS_EDGE_SHA256:
        raise AssertionError(f"RGS edge-order hash mismatch: {edge_digest}")

    canonical_index = {
        (int(u), int(v)): index
        for index, (u, v) in enumerate(canonical_edges)
    }
    rgs_to_canonical = np.asarray([
        canonical_index[(int(u), int(v))]
        for u, v, _axis in rgs_edges
    ], dtype=np.int64)
    canonical_to_rgs = np.empty(192, dtype=np.int64)
    canonical_to_rgs[rgs_to_canonical] = np.arange(192, dtype=np.int64)

    if len(set(map(tuple, rgs_edges[:, :2].tolist()))) != 192:
        raise AssertionError("RGS edge list contains duplicates")
    if not np.array_equal(canonical_edges[rgs_to_canonical], rgs_edges[:, :2]):
        raise AssertionError("endpoint permutation does not align the edge lists")
    if not np.array_equal(canonical_to_rgs[rgs_to_canonical], np.arange(192)):
        raise AssertionError("edge-order permutations are not mutual inverses")

    axis_lsb = rgs_edges[:, 2].astype(np.int64)
    bit_positions = np.asarray([
        int((int(u) ^ int(v)).bit_length() - 1)
        for u, v in rgs_edges[:, :2]
    ], dtype=np.int64)
    if not np.array_equal(bit_positions, axis_lsb):
        raise AssertionError("RGS LSB axis labels do not match endpoint bit flips")
    axis_big_endian = 5 - axis_lsb
    if not np.array_equal(axis_big_endian, 5 - bit_positions):
        raise AssertionError("axis convention conversion failed")

    degrees = np.bincount(
        rgs_edges[:, 0].astype(np.int64), minlength=64
    ) + np.bincount(rgs_edges[:, 1].astype(np.int64), minlength=64)
    if not np.array_equal(degrees, np.full(64, 6)):
        raise AssertionError("Q6 vertex degree is not uniformly six")

    return {
        "status": "EXACT_FINITE_INDEX_ALIGNMENT",
        "coordinate_shape": list(seed.coordinates.shape),
        "coordinate_sha256": "6a158cb30a671a5c994d8ab223e9283b57ac703808041d46e67f286126e419cf",
        "rgs_edge_shape": list(rgs_edges.shape),
        "canonical_edge_shape": list(canonical_edges.shape),
        "rgs_edge_sha256_int64": edge_digest,
        "rgs_order": "vertex ascending, then LSB axis 0..5; edge (u,v,axis), u<v",
        "canonical_order": "lexicographically sorted endpoint pairs; big-endian axis labels",
        "axis_conversion": "axis_big_endian = 5 - axis_lsb",
        "rgs_to_canonical": rgs_to_canonical.tolist(),
        "canonical_to_rgs": canonical_to_rgs.tolist(),
        "degree_min": int(degrees.min()),
        "degree_max": int(degrees.max()),
        "edge_set_equal": True,
        "permutations_inverse": True,
        "transport_payload_alignment": "NOT_TESTED; binary A13 R_SO3/U_SU2 arrays not loaded",
        "transport_action_convention": "NOT_ASSUMED",
    }


if __name__ == "__main__":
    report = audit_edge_order_alignment()
    out = Path("audits/RGS_Q6_EDGE_ORDER_ALIGNMENT_2026-11-26.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))
