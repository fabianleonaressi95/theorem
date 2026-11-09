import numpy as np
import pytest

from models.football_seam_law import (
    seam_bending_law, seam_cohesive_law, quaternion_relative_rotation,
    seam_internal_force, seam_tangent_matrix,
)


def test_bending_law_energy_moment_and_stiffness():
    out = seam_bending_law(theta=0.3, theta0=0.1, Db=12.0, length=2.0, width=0.5)
    k = 12.0 * 2.0 / 0.5
    assert out["energy"] == pytest.approx(0.5*k*0.2**2)
    assert out["edge_moment"] == pytest.approx(k*0.2)
    assert out["tangent_stiffness"] == pytest.approx(k)


def test_bending_law_is_objective_under_zero_relative_rotation():
    out = seam_bending_law(theta=0.7, theta0=0.7, Db=3.0, length=1.0, width=0.2)
    assert out["energy"] == pytest.approx(0.0)
    assert out["edge_moment"] == pytest.approx(0.0)


def test_cohesive_interface_energy_and_resultant():
    K = np.diag([2.0, 4.0, 6.0])
    d = np.array([1.0, -2.0, 0.5])
    out = seam_cohesive_law(d, K, 3.0)
    assert out["energy"] == pytest.approx(0.5*3.0*d@K@d)
    assert np.allclose(out["resultant_per_length"], K@d)


def test_quaternion_relative_rotation_about_seam():
    a = 0.4
    q0 = np.array([1., 0., 0., 0.])
    q1 = np.array([np.cos(a/2), np.sin(a/2), 0., 0.])
    assert quaternion_relative_rotation(q0, q1, [1., 0., 0.]) == pytest.approx(a)
    assert quaternion_relative_rotation(-q0, q1, [1., 0., 0.]) == pytest.approx(a)


def test_internal_force_and_material_tangent():
    g = np.array([1., 2., -1.])
    f = seam_internal_force(3., g)
    K = seam_tangent_matrix(3., g)
    assert np.allclose(f, 3*g)
    assert np.allclose(K, 3*np.outer(g, g))
    assert np.linalg.eigvalsh(K)[0] >= -1e-10
