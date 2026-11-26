#!/usr/bin/env python3
"""Exact F_2 and numerical spectral audit for Z2 magnetic connections on Q6."""
from __future__ import annotations

import argparse
import json
from collections import deque
from pathlib import Path

import numpy as np

N = 6
N_VERTICES = 1 << N


def cells(k: int) -> list[tuple[int, int]]:
    """Return (free-coordinate mask, fixed-bit word) for all k-cells."""
    out = []
    for free in range(1 << N):
        if free.bit_count() != k:
            continue
        fixed_mask = ((1 << N) - 1) ^ free
        for fixed in range(N_VERTICES):
            if fixed & free == 0:
                out.append((free, fixed & fixed_mask))
    return out


def cell_boundary(cell: tuple[int, int]) -> list[tuple[int, int]]:
    free, fixed = cell
    out = []
    bits = [i for i in range(N) if (free >> i) & 1]
    for bit in bits:
        face_free = free ^ (1 << bit)
        out.append((face_free, fixed))
        out.append((face_free, fixed | (1 << bit)))
    return out


def gf2_rank(columns: list[int]) -> int:
    pivots: dict[int, int] = {}
    for value in columns:
        x = value
        while x:
            pivot = x.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = x
                break
            x ^= pivots[pivot]
    return len(pivots)


def boundary_columns(k: int) -> list[int]:
    lower = {cell: i for i, cell in enumerate(cells(k - 1))}
    columns = []
    for cell in cells(k):
        value = 0
        for face in cell_boundary(cell):
            value ^= 1 << lower[face]
        columns.append(value)
    return columns


def check_chain_identity(k: int) -> bool:
    lower = set(cells(k - 2))
    for cell in cells(k):
        total: set[tuple[int, int]] = set()
        for face in cell_boundary(cell):
            for subface in cell_boundary(face):
                if subface in total:
                    total.remove(subface)
                else:
                    total.add(subface)
        if total & lower:
            return False
        if total:
            return False
    return True


def q6_edges() -> list[tuple[int, int, int]]:
    edges = []
    for v in range(N_VERTICES):
        for bit in range(N):
            w = v ^ (1 << bit)
            if v < w:
                edges.append((v, w, bit))
    return edges


def q6_plaquettes() -> list[tuple[int, int]]:
    return cells(2)


def edge_index() -> dict[tuple[int, int], int]:
    return {(v, w): i for i, (v, w, _) in enumerate(q6_edges())}


def plaquette_edge_indices() -> list[list[int]]:
    lookup = edge_index()
    out = []
    for free, fixed in q6_plaquettes():
        bits = [i for i in range(N) if (free >> i) & 1]
        boundary = []
        for bit in bits:
            other = bits[0] if bits[1] == bit else bits[1]
            for other_value in (0, 1):
                v = fixed | (other_value << other)
                w = v | (1 << bit)
                boundary.append(lookup[(min(v, w), max(v, w))])
        out.append(boundary)
    return out


def plaquette_flux(edge_bits: np.ndarray) -> np.ndarray:
    return np.asarray([
        int(np.bitwise_xor.reduce(edge_bits[boundary]))
        for boundary in plaquette_edge_indices()
    ], dtype=np.uint8)


def three_cell_flux_constraints(face_bits: np.ndarray) -> np.ndarray:
    face_lookup = {cell: i for i, cell in enumerate(cells(2))}
    values = []
    for cube in cells(3):
        total = 0
        for face in cell_boundary(cube):
            total ^= int(face_bits[face_lookup[face]])
        values.append(total)
    return np.asarray(values, dtype=np.uint8)


def spanning_tree_edges() -> list[int]:
    edges = q6_edges()
    lookup = {(v, w): i for i, (v, w, _) in enumerate(edges)}
    seen = {0}
    queue = deque([0])
    tree = []
    while queue:
        v = queue.popleft()
        for bit in range(N):
            w = v ^ (1 << bit)
            if w not in seen:
                seen.add(w)
                queue.append(w)
                tree.append(lookup[(min(v, w), max(v, w))])
    assert len(seen) == N_VERTICES and len(tree) == N_VERTICES - 1
    return tree


def gauge_fix(edge_bits: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Set all deterministic BFS-tree links to +1; return fixed links and vertex gauge."""
    edges = q6_edges()
    tree = set(spanning_tree_edges())
    adjacency = [[] for _ in range(N_VERTICES)]
    for i in tree:
        v, w, _ = edges[i]
        adjacency[v].append((w, i))
        adjacency[w].append((v, i))
    gauge = np.zeros(N_VERTICES, dtype=np.uint8)
    seen = {0}
    queue = deque([0])
    while queue:
        v = queue.popleft()
        for w, i in adjacency[v]:
            if w not in seen:
                gauge[w] = gauge[v] ^ edge_bits[i]
                seen.add(w)
                queue.append(w)
    fixed = np.asarray([
        edge_bits[i] ^ gauge[v] ^ gauge[w]
        for i, (v, w, _) in enumerate(edges)
    ], dtype=np.uint8)
    assert all(fixed[i] == 0 for i in tree)
    return fixed, gauge


def gauge_transform(edge_bits: np.ndarray, vertex_gauge: np.ndarray) -> np.ndarray:
    return np.asarray([
        edge_bits[i] ^ vertex_gauge[v] ^ vertex_gauge[w]
        for i, (v, w, _) in enumerate(q6_edges())
    ], dtype=np.uint8)


def magnetic_laplacian(edge_bits: np.ndarray) -> np.ndarray:
    matrix = 6.0 * np.eye(N_VERTICES)
    for bit, (v, w, _) in zip(edge_bits, q6_edges()):
        link = 1.0 if int(bit) == 0 else -1.0
        matrix[v, w] = -link
        matrix[w, v] = -link
    return matrix


def spectrum_and_heat(edge_bits: np.ndarray, times: list[float]) -> tuple[list[float], list[float]]:
    eigenvalues = np.linalg.eigvalsh(magnetic_laplacian(edge_bits))
    heat = [float(np.exp(-t * eigenvalues).sum()) for t in times]
    return [float(x) for x in eigenvalues], heat


def audit() -> dict:
    c0, c1, c2, c3 = (cells(k) for k in range(4))
    ranks = {
        "rank_d1": gf2_rank(boundary_columns(1)),
        "rank_d2": gf2_rank(boundary_columns(2)),
        "rank_d3": gf2_rank(boundary_columns(3)),
    }
    assert (len(c0), len(c1), len(c2), len(c3)) == (64, 192, 240, 160)
    assert ranks == {"rank_d1": 63, "rank_d2": 129, "rank_d3": 111}
    assert check_chain_identity(2) and check_chain_identity(3)

    flux_map_columns = []
    for edge_i in range(len(q6_edges())):
        basis = np.zeros(len(q6_edges()), dtype=np.uint8)
        basis[edge_i] = 1
        flux_map_columns.append(sum(
            int(bit) << j for j, bit in enumerate(plaquette_flux(basis))
        ))
    flux_rank = gf2_rank(flux_map_columns)
    assert flux_rank == 129

    times = [0.0, 0.1, 0.5, 1.0, 2.0]
    trivial = np.zeros(len(q6_edges()), dtype=np.uint8)
    edges = q6_edges()
    one_link = trivial.copy()
    one_link[0] = 1
    two_links = trivial.copy()
    two_links[0] = 1
    two_links[-1] = 1

    rng = np.random.default_rng(103)
    random_gauge = rng.integers(0, 2, size=N_VERTICES, dtype=np.uint8)
    gauge_equivalent = gauge_transform(one_link, random_gauge)
    fixed_one, _ = gauge_fix(one_link)
    fixed_gauge_equivalent, _ = gauge_fix(gauge_equivalent)
    assert np.array_equal(fixed_one, fixed_gauge_equivalent)
    assert np.array_equal(plaquette_flux(one_link), plaquette_flux(gauge_equivalent))

    samples = {}
    for name, connection in (
        ("trivial", trivial),
        ("one_negative_link", one_link),
        ("two_negative_links", two_links),
    ):
        flux = plaquette_flux(connection)
        constraints = three_cell_flux_constraints(flux)
        assert not np.any(constraints)
        eigenvalues, heat = spectrum_and_heat(connection, times)
        samples[name] = {
            "negative_links": int(connection.sum()),
            "negative_plaquettes": int(flux.sum()),
            "eigenvalues": eigenvalues,
            "heat_trace": heat,
        }

    expected_trivial = [float((1.0 + np.exp(-2.0 * t)) ** 6) for t in times]
    assert np.allclose(samples["trivial"]["heat_trace"], expected_trivial, atol=1e-10)
    eig_gauge, heat_gauge = spectrum_and_heat(gauge_equivalent, times)
    eig_one, heat_one = spectrum_and_heat(one_link, times)
    assert np.allclose(eig_gauge, eig_one, atol=1e-10)
    assert np.allclose(heat_gauge, heat_one, atol=1e-10)

    return {
        "status": "computed",
        "cell_counts": {"C0": len(c0), "C1": len(c1), "C2": len(c2), "C3": len(c3)},
        "gf2_boundary_ranks": ranks,
        "chain_identities": {"d1_d2_zero": True, "d2_d3_zero": True},
        "gauge_orbits": 2 ** 129,
        "plaquette_flux_map_rank": flux_rank,
        "independent_face_constraints": len(c2) - flux_rank,
        "gauge_fix": "deterministic BFS spanning tree; 129 chord bits",
        "heat_times": times,
        "representatives": samples,
        "gauge_invariance_check": "passed",
        "exhaustive_spectral_enumeration": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = audit()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
