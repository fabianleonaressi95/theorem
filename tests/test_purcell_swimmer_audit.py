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


def test_quadrature_refinement_and_published_leading_coefficient():
    amplitude = 1e-3
    initial = np.array([0.0, 1e-2, 0.0, 0.0, 0.0])
    q32 = simulate_square_gait(amplitude, quadrature_order=32)
    q64 = simulate_square_gait(amplitude, quadrature_order=64)
    dx32 = (q32[0] - initial[0]) / amplitude**2
    dx64 = (q64[0] - initial[0]) / amplitude**2
    assert abs(dx64 - dx32) < 1e-9
    assert abs(dx64 - 5.0 / 81.0) < 1e-4


def test_initial_control_fields_match_published_values():
    q = np.array([0.0, 1e-2, 0.0, 0.0, 0.0])
    resistance = resistance_matrix(q, quadrature_order=64)
    expected = (
        np.array([0.0, 1.0 / 6.0, -7.0 / 27.0, 1.0, 0.0]),
        np.array([0.0, -1.0 / 6.0, -7.0 / 27.0, 0.0, 1.0]),
    )
    for index, control in enumerate(((1.0, 0.0), (0.0, 1.0))):
        body = np.linalg.solve(
            resistance[:3, :3],
            -resistance[:3, 3:] @ np.asarray(control),
        )
        field = np.concatenate((body, np.asarray(control)))
        assert np.allclose(field, expected[index], atol=1e-10)
