#!/usr/bin/env python3
"""Exact geometry and analytic equilibrium checks for T107.

This audit does not simulate a physical circuit or claim a material defect.
"""
from __future__ import annotations

import json
import math

import numpy as np

from scripts.q6_prism_kinematic_map import build_q6_complex

D = 64


def edge_coherence_variance(d: int = D) -> float:
    if d < 2:
        raise ValueError("complex sphere dimension must be at least two")
    return 1.0 / (2.0 * d * (d + 1))


def edge_coherence_susceptibility(beta: float, d: int = D) -> float:
    if beta <= 0:
        raise ValueError("inverse temperature beta must be positive")
    return beta * edge_coherence_variance(d)


def audit() -> dict:
    c = build_q6_complex()
    coords = c["coords"]
    edges = c["edges"]

    # Every Q6 edge must become one nearest-neighbour C4 edge in exactly
    # the Gray coordinate corresponding to the flipped bit pair.
    edge_preservation = True
    for a, b, bit in edges:
        delta = (coords[b] - coords[a]) % 4
        axis = bit // 2
        expected = np.zeros(3, dtype=np.int64)
        expected[axis] = 1 if delta[axis] == 1 else 3
        if not np.array_equal(delta, expected):
            edge_preservation = False
            break

    # The two chain-map identities are already constructed in the base audit.
    chain0 = c["d0"] @ c["p0"] - c["p1"] @ c["d0_base"]
    chain1 = c["d1_product"] @ c["p1"] - c["p2"] @ c["d1_base"]

    return {
        "status": "PASS" if edge_preservation
        and np.max(np.abs(chain0)) == 0
        and np.max(np.abs(chain1)) == 0 else "FAIL",
        "q6_vertices": int(coords.shape[0]),
        "q6_edges": int(len(edges)),
        "gray_coordinates_unique": len({tuple(v) for v in coords.tolist()}) == 64,
        "gray_graph_isomorphism": edge_preservation,
        "quotient_vertices": int(c["d0_base"].shape[1]),
        "quotient_edges": int(c["d0_base"].shape[0]),
        "quotient_faces": int(c["d1_base"].shape[0]),
        "fibre_cardinality": 4,
        "vertex_chain_map_max_abs": int(np.max(np.abs(chain0))),
        "face_chain_map_max_abs": int(np.max(np.abs(chain1))),
        "haar_edge_coherence_variance_d64": edge_coherence_variance(),
        "d_dJ_mean_edge_coherence_at_J0": edge_coherence_susceptibility(1.0),
        "d_dJ_formula": "beta/(2*d*(d+1)) = beta/8320 for d=64",
        "physical_claims": "none; no circuit dynamics or material defect is simulated",
    }


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2))
