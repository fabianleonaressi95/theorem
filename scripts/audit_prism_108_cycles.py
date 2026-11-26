#!/usr/bin/env python3
"""Exact constructive certificate for a 108-cycle cover of PRISM.

Graph: C64 □ C6 □ C6 □ C6 □ C5, with coordinates (g,l,c,t,b)
and the repository's mixed-radix indexing.

Construction:
- Build a Hamiltonian 320-cycle H in C64 □ C5 by a column snake.
- For each fixed (l,t) and each adjacent pair (c=0,1), (2,3), (4,5),
  take two copies of H, delete the same edge (h0,h1), and cross-connect
  the two copies at h0 and h1. This gives one 640-cycle.
- The 3*6*6 cycles partition the full 69,120-vertex set.

This proves existence of a deterministic cycle cover for the specified
Cartesian-product graph. It does NOT identify this construction with any
historical/Pellis cycle-selection rule unless that provenance is supplied.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import struct
from pathlib import Path

MODS = (64, 6, 6, 6, 5)
VERTICES = 69_120
CYCLE_COUNT = 108
CYCLE_LENGTH = 640


def index(g: int, l: int, c: int, t: int, b: int) -> int:
    if not (0 <= g < 64 and 0 <= l < 6 and 0 <= c < 6
            and 0 <= t < 6 and 0 <= b < 5):
        raise ValueError("coordinate outside PRISM factor range")
    return ((((g * 6 + l) * 6 + c) * 6 + t) * 5 + b)


def base_hamiltonian_cycle() -> list[tuple[int, int]]:
    """Hamiltonian cycle of C64 □ C5, ordered as (g,b)."""
    cycle: list[tuple[int, int]] = []
    for g in range(64):
        bs = range(5) if g % 2 == 0 else range(4, -1, -1)
        cycle.extend((g, b) for b in bs)
    if len(cycle) != 320 or len(set(cycle)) != 320:
        raise AssertionError("base cycle is not a 320-vertex listing")
    return cycle


def prism_vertex(gb: tuple[int, int], l: int, c: int, t: int) -> tuple[int, ...]:
    g, b = gb
    return (g, l, c, t, b)


def adjacent(u: tuple[int, ...], v: tuple[int, ...]) -> bool:
    changed = 0
    for a, z, n in zip(u, v, MODS):
        if a == z:
            continue
        if (z - a) % n not in (1, n - 1):
            return False
        changed += 1
    return changed == 1


def construct_cycles() -> list[list[tuple[int, ...]]]:
    h = base_hamiltonian_cycle()
    cycles = []
    for l in range(6):
        for t in range(6):
            for pair in range(3):
                c0, c1 = 2 * pair, 2 * pair + 1
                # Remove h[0]-h[1] from both layers. The remaining paths
                # are cross-connected at h[0] and h[1], yielding one cycle.
                cycle = [
                    prism_vertex(h[0], l, c0, t),
                    prism_vertex(h[0], l, c1, t),
                ]
                cycle.extend(prism_vertex(gb, l, c1, t)
                             for gb in reversed(h[1:]))
                cycle.append(prism_vertex(h[1], l, c0, t))
                cycle.extend(prism_vertex(gb, l, c0, t) for gb in h[2:])
                cycles.append(cycle)
    return cycles


def audit(include_cycles: bool = False) -> dict:
    cycles = construct_cycles()
    if len(cycles) != CYCLE_COUNT:
        raise AssertionError(f"expected {CYCLE_COUNT} cycles, got {len(cycles)}")

    seen: set[int] = set()
    flat: list[int] = []
    for r, cycle in enumerate(cycles):
        if len(cycle) != CYCLE_LENGTH:
            raise AssertionError(f"cycle {r}: wrong length {len(cycle)}")
        encoded = [index(*v) for v in cycle]
        if len(set(encoded)) != CYCLE_LENGTH:
            raise AssertionError(f"cycle {r}: repeated vertex")
        for i, u in enumerate(cycle):
            v = cycle[(i + 1) % CYCLE_LENGTH]
            if not adjacent(u, v):
                raise AssertionError(f"cycle {r}: invalid edge at position {i}")
        overlap = seen.intersection(encoded)
        if overlap:
            raise AssertionError(f"cycle {r}: overlaps previous cycles")
        seen.update(encoded)
        flat.extend(encoded)

    if len(seen) != VERTICES or seen != set(range(VERTICES)):
        raise AssertionError("cycles do not cover the complete PRISM vertex set")

    digest = hashlib.sha256()
    for value in flat:
        digest.update(struct.pack("<I", value))

    result = {
        "graph": "C64 x C6 x C6 x C6 x C5",
        "coordinate_order": ["g", "l", "c", "t", "b"],
        "mixed_radix_index": "((((g*6+l)*6+c)*6+t)*5+b)",
        "vertices": VERTICES,
        "cycles": CYCLE_COUNT,
        "cycle_length": CYCLE_LENGTH,
        "construction": "3 adjacent c-pairs x 6 l-values x 6 t-values",
        "base_cycle": "column snake on C64 x C5, length 320",
        "all_cycle_edges_valid": True,
        "each_cycle_simple": True,
        "cycles_pairwise_vertex_disjoint": True,
        "full_vertex_cover": True,
        "unique_vertices_covered": len(seen),
        "flattened_order_sha256": digest.hexdigest(),
        "provenance_scope": (
            "Constructive certificate for a valid deterministic cycle cover; "
            "not evidence that this is the historical Pellis selection rule."
        ),
    }
    if include_cycles:
        result["cycles_as_mixed_radix_indices"] = flat
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--include-cycles", action="store_true",
                        help="include all 69,120 ordered vertex indices in JSON")
    args = parser.parse_args()
    report = audit(include_cycles=args.include_cycles)
    payload = json.dumps(report, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload + "\n", encoding="utf-8")
    print(payload)


if __name__ == "__main__":
    main()
