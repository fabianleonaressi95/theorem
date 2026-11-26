#!/usr/bin/env python3
"""Exact rational homology audit for the C60 cellulation.

The script does not fabricate Q6 or Kathara boundary matrices. Those must be
supplied from canonical archived artifacts before a cross-complex map is tested.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
from fractions import Fraction
import numpy as np
from audit_c60_stone_wales import c60_ideal, graph_from_bonds, oriented_faces, boundary


def exact_rank(matrix: np.ndarray) -> int:
    a = [[Fraction(int(x)) for x in row] for row in np.asarray(matrix).tolist()]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    rank = 0
    for col in range(n):
        pivot = next((r for r in range(rank, m) if a[r][col] != 0), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        p = a[rank][col]
        a[rank] = [x / p for x in a[rank]]
        for r in range(m):
            if r != rank and a[r][col] != 0:
                q = a[r][col]
                a[r] = [x - q*y for x, y in zip(a[r], a[rank])]
        rank += 1
        if rank == m:
            break
    return rank


def audit() -> dict:
    xyz, bonds = c60_ideal()
    graph = graph_from_bonds(len(xyz), bonds)
    faces = oriented_faces(graph)
    edges, b1, b2 = boundary(graph, faces)
    r1, r2 = exact_rank(b1), exact_rank(b2)
    n0, n1, n2 = graph.number_of_nodes(), len(edges), len(faces)
    return {
        "status": "exact_rational_cellular_homology",
        "cell_counts_C0_C1_C2": [n0, n1, n2],
        "boundary_shapes": {"B1": list(b1.shape), "B2": list(b2.shape)},
        "boundary_ranks_over_Q": {"rank_B1": r1, "rank_B2": r2},
        "betti_numbers": {"beta0": n0-r1, "beta1": n1-r1-r2, "beta2": n2-r2},
        "euler_characteristic": n0-n1+n2,
        "boundary_squared_zero": bool(np.all(b1 @ b2 == 0)),
        "dimension_contract": {
            "C60": {"C0": 60, "C1": 90, "C2": 32},
            "Kathara_recorded": {"C0": 12, "C1": 21, "C2": 10},
            "Q6_recorded": {"C0": 64, "C1": 192, "C2": 240}
        },
        "q6_graph_cycle_rank_recorded": 129,
        "q6_caveat": (
            "The Q6 graph cycle rank 129 is a 1-skeleton invariant. It is not "
            "the first Betti number of a 2-complex until the 240 plaquette "
            "boundary columns are specified and their rank is computed."
        ),
        "required_inputs": [
            "Canonical integer B1_Q6 and B2_Q6 matrices, including cell orientation and plaquette boundary convention.",
            "Canonical integer B1_K and B2_K matrices for the 12/21/10 Kathara complex.",
            "Actual R0/R1/R2 arrays; verify B1_Q6 R1 = R0 B1_K and B2_Q6 R2 = R1 B2_K exactly.",
            "Only then construct P0/P1/P2 from C60 to Kathara and test both chain-map equations.",
            "Test composed maps R_i P_i; do not infer them from matching dimensions or drawings."
        ]
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="c60_q6_bridge_audit.json")
    args = parser.parse_args()
    result = audit()
    Path(args.out).write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
