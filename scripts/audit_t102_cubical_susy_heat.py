#!/usr/bin/env python3
"""Exact combinatorial audit of the cubical SUSY/Hodge complex on the 6-cube."""
from __future__ import annotations
import json
import math
from itertools import product
from typing import Any

import numpy as np

N = 6
Cell = tuple[int, ...]  # 0, 1 are fixed coordinates; 2 denotes a free coordinate.


def cells_by_degree(n: int = N) -> list[list[Cell]]:
    groups: list[list[Cell]] = [[] for _ in range(n + 1)]
    for cell in product((0, 1, 2), repeat=n):
        groups[cell.count(2)].append(tuple(cell))
    return groups


def boundary_matrices(groups: list[list[Cell]]) -> list[np.ndarray]:
    """B[k] has shape (number of (k-1)-cells, number of k-cells)."""
    n = len(groups) - 1
    matrices = [np.zeros((0, len(groups[0])), dtype=np.int64)]
    for k in range(1, n + 1):
        lower_index = {cell: i for i, cell in enumerate(groups[k - 1])}
        B = np.zeros((len(groups[k - 1]), len(groups[k])), dtype=np.int64)
        for col, cell in enumerate(groups[k]):
            free = [i for i, value in enumerate(cell) if value == 2]
            for position, axis in enumerate(free):
                sign = -1 if position % 2 else 1
                low, high = list(cell), list(cell)
                low[axis], high[axis] = 0, 1
                B[lower_index[tuple(high)], col] += sign
                B[lower_index[tuple(low)], col] -= sign
        matrices.append(B)
    return matrices


def hodge_laplacians(boundaries: list[np.ndarray]) -> list[np.ndarray]:
    n = len(boundaries) - 1
    result = []
    for k in range(n + 1):
        size = boundaries[k].shape[1] if k < len(boundaries) else 0
        delta = np.zeros((size, size), dtype=np.int64)
        if k >= 1:
            delta += boundaries[k].T @ boundaries[k]
        if k < n:
            delta += boundaries[k + 1] @ boundaries[k + 1].T
        result.append(delta)
    return result


def heat_trace(matrix: np.ndarray, t: float) -> float:
    eigenvalues = np.linalg.eigvalsh(matrix.astype(float))
    return float(np.exp(-t * eigenvalues).sum())


def audit(times: tuple[float, ...] = (0.05, 0.2, 0.7, 1.5)) -> dict[str, Any]:
    groups = cells_by_degree()
    boundaries = boundary_matrices(groups)
    laplacians = hodge_laplacians(boundaries)
    chain_errors = []
    for k in range(2, N + 1):
        product_matrix = boundaries[k - 1] @ boundaries[k]
        chain_errors.append(int(np.max(np.abs(product_matrix))) if product_matrix.size else 0)

    expected_counts = [math.comb(N, k) * 2 ** (N - k) for k in range(N + 1)]
    graph_eigs = np.linalg.eigvalsh(laplacians[0].astype(float))
    graph_spectrum = {}
    for k in range(N + 1):
        count = int(np.count_nonzero(np.isclose(graph_eigs, 2 * k, atol=1e-9)))
        graph_spectrum[str(2 * k)] = count

    heat = {}
    for t in times:
        traces = [heat_trace(delta, t) for delta in laplacians]
        supertrace = sum(((-1) ** k) * traces[k] for k in range(N + 1))
        exact_vertex_trace = (1.0 + math.exp(-2.0 * t)) ** N
        heat[f"{t:g}"] = {
            "degree_traces": traces,
            "supertrace": supertrace,
            "supertrace_error_from_one": abs(supertrace - 1.0),
            "vertex_heat_trace": traces[0],
            "exact_vertex_heat_trace": exact_vertex_trace,
            "vertex_trace_error": abs(traces[0] - exact_vertex_trace),
        }

    return {
        "dimension": N,
        "cell_counts_by_degree": [len(x) for x in groups],
        "expected_cell_counts": expected_counts,
        "total_cells": sum(map(len, groups)),
        "boundary_squared_max_abs_by_degree_2_to_6": chain_errors,
        "graph_laplacian_eigenvalue_multiplicities": graph_spectrum,
        "heat_audit": heat,
        "topological_euler_characteristic": sum(
            (-1) ** k * len(groups[k]) for k in range(N + 1)
        ),
        "expected_betti_numbers_for_cube": [1, 0, 0, 0, 0, 0, 0],
        "interpretation": (
            "Finite cubical de Rham/Hodge supersymmetric quantum mechanics on a "
            "contractible 6-cube. This is not four-dimensional N=4 SYM and does "
            "not derive a Sakharov Einstein-Hilbert term."
        ),
    }


def main() -> None:
    print(json.dumps(audit(), indent=2))


if __name__ == "__main__":
    main()
