import numpy as np
import pytest

from audits.purcell_swimmer_wall.discrete_geometry import (
    assemble_local_resistance, evaluate_local_loads, q6_least_squares_gradient,
    resistance_connection, weighted_barycentre,
)
from audits.purcell_swimmer_wall.q6_cut_project_interface import Q6ShapeMap, q6_edges


def test_q6_least_squares_recovers_affine_gradient():
    calibration = np.array([[1.0, 0.2, -0.1], [0.3, 0.8, 0.4]])
    coords = Q6ShapeMap(calibration).coordinates()
    values = coords @ np.array([1.7, -0.6]) + 2.3
    gradients, condition = q6_least_squares_gradient(coords, q6_edges()[:, :2], values)
    assert np.allclose(gradients, [1.7, -0.6], atol=1e-10)
    assert np.all(np.isfinite(condition)) and np.all(condition >= 1.0)


def test_barycentre_and_moment_origin_shift():
    points = np.array([[0., 0.], [2., 0.], [0., 1.]])
    weights = np.array([1., 2., 1.])
    centre = weighted_barycentre(points, weights)
    assert np.allclose(centre, [1., .25])
    force = np.array([.4, -.7])
    tractions = np.array([[.2, .1], [-.3, .4], [.1, -.5]])
    moment_o = sum(w*np.cross(x, t) for w, x, t in zip(weights, points, tractions))
    resultant = np.einsum("i,ij->j", weights, tractions)
    moment_c = sum(w*np.cross(x-centre, t) for w, x, t in zip(weights, points, tractions))
    assert np.isclose(moment_c, moment_o - np.cross(centre, resultant))


def test_local_resistance_schur_and_force_free_loads():
    points = np.array([[0., 0.], [1., 0.], [.2, .8], [.8, .7]])
    weights = np.full(4, .25)
    drag = np.repeat(np.eye(2)[None, :, :], 4, axis=0)
    shape_jac = np.zeros((4, 2, 2))
    shape_jac[:, 0, 0] = [0., .1, .2, .1]
    shape_jac[:, 1, 1] = [.1, 0., -.1, 0.]
    assembly = assemble_local_resistance(points, weights, drag, shape_jac)
    resistance = assembly["resistance"]
    assert np.allclose(resistance, resistance.T, atol=1e-12)
    assert np.min(np.linalg.eigvalsh(resistance)) >= -1e-12
    connection, metric = resistance_connection(resistance, 2)
    assert np.min(np.linalg.eigvalsh(metric)) >= -1e-10
    shape_rate = np.array([.3, -.2])
    qdot = np.concatenate((connection @ shape_rate, shape_rate))
    loads = evaluate_local_loads(assembly, qdot, points, weights, drag)
    assert np.linalg.norm(loads["force"]) < 1e-10
    assert abs(loads["moment_about_reference"]) < 1e-10
    assert loads["dissipation"] >= 0.


def test_rank_deficient_shape_star_is_rejected():
    coords = np.array([[0., 0.], [1., 0.], [2., 0.]])
    edges = np.array([[0, 1], [1, 2]])
    with pytest.raises(ValueError):
        q6_least_squares_gradient(coords, edges, np.array([0., 1., 2.]))
