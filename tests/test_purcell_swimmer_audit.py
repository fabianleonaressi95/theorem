import numpy as np

from audits.purcell_swimmer_wall.benchmark import (
    resistance_matrix,
    simulate_square_gait,
)


def test_resistance_matrix_is_symmetric_positive_definite():
    q = np.array([0.0, 1e-2, 0.0, 0.0, 0.0])
    matrix = resistance_matrix(q, quadrature_order=24)
    assert np.allclose(matrix, matrix.T, atol=1e-12)
    assert np.linalg.eigvalsh(matrix).min() > 0.0


def test_quadrature_refinement_stabilizes_preliminary_cycle_output():
    amplitude = 1e-3
    initial = np.array([0.0, 1e-2, 0.0, 0.0, 0.0])
    q32 = simulate_square_gait(amplitude, quadrature_order=32)
    q64 = simulate_square_gait(amplitude, quadrature_order=64)
    dx32 = (q32[0] - initial[0]) / amplitude**2
    dx64 = (q64[0] - initial[0]) / amplitude**2
    assert abs(dx64 - dx32) < 1e-9
