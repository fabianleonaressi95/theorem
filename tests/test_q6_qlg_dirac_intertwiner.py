import numpy as np
from scripts.q6_qlg_dirac_intertwiner import (
    audit, embed_fibre_field, intertwiner, numerical_intertwiner_dimension,
    su2_from_unit_quaternion, dirac_spatial_restriction,
)


def test_intertwiner_space_has_complex_dimension_two():
    rng = np.random.default_rng(49)
    qs = rng.normal(size=(18, 4))
    dimension, _ = numerical_intertwiner_dimension(qs)
    assert dimension == 2


def test_family_is_equivariant_for_arbitrary_coefficients():
    rng = np.random.default_rng(50)
    for q in rng.normal(size=(12, 4)):
        u = su2_from_unit_quaternion(q)
        for alpha, beta in ((1, 0), (0, 1), (1, 1j), (0.3, 0.7j)):
            k = intertwiner(alpha, beta)
            assert np.linalg.norm(dirac_spatial_restriction(u) @ k-k @ u) < 1e-12


def test_isometric_normalization_and_field_shape():
    k = intertwiner(2+1j, -0.4j)
    assert np.linalg.norm(k.conj().T @ k-np.eye(2)) < 1e-12
    x = np.ones((64, 2), dtype=complex)
    assert embed_fibre_field(x).shape == (64, 4)


def test_zero_map_rejected():
    import pytest
    with pytest.raises(ValueError):
        intertwiner(0, 0)


def test_full_audit_passes_and_does_not_claim_lorentz_covariance():
    result = audit()
    assert result["passed"]
    assert result["computed_intertwiner_dimension"] == 2
    assert "no boost" in result["scope"]
