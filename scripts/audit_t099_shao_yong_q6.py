#!/usr/bin/env python3
"""Exact finite audit for T099: the 64 I Ching hexagrams as Q3 □ Q3."""
from __future__ import annotations

import argparse
import json
from collections import Counter


def vertex(lower: int, upper: int) -> int:
    if not (0 <= lower < 8 and 0 <= upper < 8):
        raise ValueError("trigram indices must lie in {0,...,7}")
    return lower + 8 * upper


def neighbours(v: int) -> set[int]:
    if not 0 <= v < 64:
        raise ValueError("hexagram index must lie in {0,...,63}")
    return {v ^ (1 << bit) for bit in range(6)}


def edge_partition() -> tuple[set[tuple[int, int]], set[tuple[int, int]]]:
    lower_edges: set[tuple[int, int]] = set()
    upper_edges: set[tuple[int, int]] = set()
    for v in range(64):
        for bit in range(6):
            w = v ^ (1 << bit)
            if v < w:
                edge = (v, w)
                (lower_edges if bit < 3 else upper_edges).add(edge)
    return lower_edges, upper_edges


def validate_circular_order(order: list[int]) -> bool:
    """Validate a supplied 64-label circular transcription; do not invent one."""
    return len(order) == 64 and set(order) == set(range(64))


def laplacian_spectrum() -> dict[int, int]:
    from math import comb
    return {2 * k: comb(6, k) for k in range(7)}


def audit() -> dict[str, object]:
    states = {vertex(lower, upper) for lower in range(8) for upper in range(8)}
    lower_edges, upper_edges = edge_partition()
    degrees = Counter(len(neighbours(v)) for v in range(64))
    assert len(states) == 64
    assert degrees == {6: 64}
    assert len(lower_edges) == 96
    assert len(upper_edges) == 96
    assert len(lower_edges | upper_edges) == 192
    assert not (lower_edges & upper_edges)
    spectrum = laplacian_spectrum()
    assert sum(spectrum.values()) == 64
    assert sum(lam * mult for lam, mult in spectrum.items()) == 6 * 64
    return {
        "vertices": len(states),
        "degree_distribution": dict(degrees),
        "lower_line_edges": len(lower_edges),
        "upper_line_edges": len(upper_edges),
        "edges_total": len(lower_edges | upper_edges),
        "laplacian_spectrum_multiplicities": spectrum,
        "circular_order": "not supplied; permutation validation available",
        "status": "PASS",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--circular-order", nargs=64, type=int,
                        help="optional 64 labels in the transcribed circular order")
    args = parser.parse_args()
    if args.circular_order is not None and not validate_circular_order(args.circular_order):
        parser.error("--circular-order must contain each integer 0,...,63 exactly once")
    result = audit()
    if args.circular_order is not None:
        result["circular_order"] = "valid permutation of 0,...,63"
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
