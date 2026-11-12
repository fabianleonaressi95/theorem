#!/usr/bin/env python3
"""Cycle/cocycle decomposition for the Q6 graph and its cubical completion."""
from __future__ import annotations

import json
from collections import deque
from pathlib import Path
import argparse

from scripts.audit_t103_q6_z2_magnetic_holonomy import (
    cells, q6_edges, plaquette_edge_indices, gf2_rank, boundary_columns,
)


def bit_vector(indices: list[int]) -> int:
    value = 0
    for i in indices:
        value ^= 1 << i
    return value


def tree_data():
    edges = q6_edges()
    lookup = {(v, w): i for i, (v, w, _) in enumerate(edges)}
    adjacency = [[] for _ in range(64)]
    for i, (v, w, _) in enumerate(edges):
        adjacency[v].append((w, i))
        adjacency[w].append((v, i))
    parent = [-1] * 64
    parent_edge = [-1] * 64
    parent[0] = 0
    queue = deque([0])
    order = []
    while queue:
        v = queue.popleft()
        for w, edge_i in adjacency[v]:
            if parent[w] == -1:
                parent[w] = v
                parent_edge[w] = edge_i
                queue.append(w)
                order.append(w)
    assert len(order) == 63
    tree_edges = set(parent_edge[1:])
    return edges, adjacency, parent, parent_edge, tree_edges


def tree_path_edges(u: int, v: int, parent: list[int], parent_edge: list[int]) -> list[int]:
    ancestors_u = {}
    path_u = []
    x = u
    while x != 0:
        ancestors_u[x] = len(path_u)
        path_u.append(parent_edge[x])
        x = parent[x]
    ancestors_u[0] = len(path_u)
    path_v = []
    x = v
    while x not in ancestors_u:
        path_v.append(parent_edge[x])
        x = parent[x]
    lca = x
    return path_u[:ancestors_u[lca]] + path_v


def fundamental_cycle_basis() -> list[int]:
    edges, _, parent, parent_edge, tree_edges = tree_data()
    basis = []
    for i, (u, v, _) in enumerate(edges):
        if i not in tree_edges:
            basis.append(bit_vector(tree_path_edges(u, v, parent, parent_edge) + [i]))
    assert len(basis) == 129
    return basis


def cut_cocycle_basis() -> list[int]:
    """Coboundaries delta(vertex) for all non-root vertices."""
    edges = q6_edges()
    rows = []
    for vertex in range(1, 64):
        rows.append(bit_vector([
            i for i, (u, v, _) in enumerate(edges)
            if u == vertex or v == vertex
        ]))
    assert len(rows) == 63
    return rows


def square_boundary_vectors() -> list[int]:
    return [bit_vector(indices) for indices in plaquette_edge_indices()]


def dot_f2(a: int, b: int) -> int:
    return (a & b).bit_count() & 1


def audit_cycle_cocycle() -> dict:
    cycles = fundamental_cycle_basis()
    cocycles = cut_cocycle_basis()
    square_boundaries = square_boundary_vectors()

    cycle_rank = gf2_rank(cycles)
    cocycle_rank = gf2_rank(cocycles)
    square_span_rank = gf2_rank(square_boundaries)
    orthogonal = all(dot_f2(c, z) == 0 for c in cycles for z in cocycles)

    # A 1-cycle has even incidence at every vertex; a 1-cocycle is
    # orthogonal to every square boundary, i.e. ker(delta_1).
    edges = q6_edges()
    cycle_even_degree = True
    for c in cycles:
        degrees = [0] * 64
        for i, (u, v, _) in enumerate(edges):
            if (c >> i) & 1:
                degrees[u] ^= 1
                degrees[v] ^= 1
        cycle_even_degree &= not any(degrees)

    cocycle_closed = all(
        dot_f2(z, p) == 0 for z in cocycles for p in square_boundaries
    )

    # Cubical chain/cochain homology in degree one.
    rank_d1 = gf2_rank(boundary_columns(1))
    rank_d2 = gf2_rank(boundary_columns(2))
    dim_ker_d1 = 192 - rank_d1
    dim_ker_delta1 = 192 - rank_d2
    h1_dimension = dim_ker_d1 - rank_d2
    h1_co_dimension = dim_ker_delta1 - rank_d1

    result = {
        "edge_count": 192,
        "fundamental_cycle_basis_size": len(cycles),
        "cycle_space_dimension": cycle_rank,
        "cut_cocycle_basis_size": len(cocycles),
        "cocycle_space_dimension": cocycle_rank,
        "square_boundary_count": len(square_boundaries),
        "span_of_square_boundaries_dimension": square_span_rank,
        "cycle_cocycle_pairing": "orthogonal over F2" if orthogonal else "FAILED",
        "cycle_basis_even_vertex_degree": bool(cycle_even_degree),
        "coboundaries_are_cocycles": bool(cocycle_closed),
        "dim_ker_d1": dim_ker_d1,
        "rank_d2": rank_d2,
        "H1_dimension": h1_dimension,
        "dim_ker_delta1": dim_ker_delta1,
        "rank_delta0": rank_d1,
        "H1_cohomology_dimension": h1_co_dimension,
        "conclusions": {
            "cycle_space_equals_square_boundary_span": cycle_rank == square_span_rank == 129,
            "cocycle_space_equals_cut_space": cocycle_rank == rank_d1 == 63,
            "H1_trivial": h1_dimension == 0,
            "H1_cohomology_trivial": h1_co_dimension == 0,
        },
    }
    assert cycle_rank == square_span_rank == 129
    assert cocycle_rank == rank_d1 == 63
    assert orthogonal and cycle_even_degree and cocycle_closed
    assert h1_dimension == h1_co_dimension == 0
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = audit_cycle_cocycle()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
