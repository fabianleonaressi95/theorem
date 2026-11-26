import numpy as np
import pytest
from scripts.rgs_airystress_holonomy_identifiability import (
    audit_rotation_ambiguity, elastic_distortion, plane_strain_from_stress,
)

def test_plane_strain_constitutive_recovery_is_symmetric_and_finite():
    sigma = np.array([[3.0, 0.4], [0.4, -1.0]])
    eps = plane_strain_from_stress(sigma, 200.0, 0.25)
    assert np.allclose(eps, eps.T)
    assert np.isfinite(eps).all()

def test_skew_rotation_does_not_change_symmetric_strain():
    eps = np.array([[0.2, 0.03], [0.03, -0.1]])
    beta = elastic_distortion(eps, np.asarray(0.7))
    assert np.allclose(0.5 * (beta + beta.T), eps, atol=1e-14)

def test_same_strain_can_have_different_burgers_loop_closure():
    report = audit_rotation_ambiguity(0.2, 256, 1.3)
    assert report["same_symmetric_strain"] is True
    assert report["closure_difference_norm"] > 1e-3
    assert report["quadrature_identity_residual"] < 1e-12
    assert np.allclose(report["burgers_closure_zero_rotation"], [0.0, 0.0], atol=1e-14)

def test_invalid_plane_strain_parameters_are_rejected():
    with pytest.raises(ValueError, match="young_modulus"):
        plane_strain_from_stress(np.eye(2), 0.0, 0.2)
