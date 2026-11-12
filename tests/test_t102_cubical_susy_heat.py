import math

import numpy as np

from scripts.audit_t102_cubical_susy_heat import (
    audit, boundary_matrices, cells_by_degree, hodge_laplacians,
)


def test_six_cube_cell_counts_and_q6_skeleton():
    groups = cells_by_degree()
    assert [len(x) for x in groups] == [64, 192, 240, 160, 60, 12, 1]


def test_cubical_boundary_squares_to_zero():
    groups = cells_by_degree()
    boundaries = boundary_matrices(groups)
    for k in range(2, 7):
        assert np.array_equal(boundaries[k - 1] @ boundaries[k],
                              np.zeros((len(groups[k - 2]), len(groups[k])), dtype=int))


def test_hodge_laplacians_are_symmetric_positive_semidefinite():
    groups = cells_by_degree()
    deltas = hodge_laplacians(boundary_matrices(groups))
    for delta in deltas:
        assert np.array_equal(delta, delta.T)
        assert np.linalg.eigvalsh(delta.astype(float)).min() > -1e-9


def test_q6_vertex_laplacian_spectrum_and_heat_trace():
    result = audit(times=(0.2, 0.7))
    assert result["graph_laplacian_eigenvalue_multiplicities"] == {
        "0": 1, "2": 6, "4": 15, "6": 20, "8": 15, "10": 6, "12": 1
    }
    for entry in result["heat_audit"].values():
        assert entry["vertex_trace_error"] < 1e-9


def test_cubical_heat_supertrace_is_euler_characteristic():
    result = audit(times=(0.05, 0.2, 0.7, 1.5))
    assert result["topological_euler_characteristic"] == 1
    for entry in result["heat_audit"].values():
        assert entry["supertrace_error_from_one"] < 1e-8
