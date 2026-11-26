"""Regression tests for the 3D Jitterbug rigidity/Hessian audit."""
from audits.jitterbug_mechanical_hessian import audit


def test_jitterbug_rigidity_and_hessian_spectrum():
    result = audit()
    assert result["vertices"] == 12
    assert result["rods"] == 24
    assert result["triangular_panels"] == 8
    assert result["panel_union_equals_rod_set"] is True
    assert result["panel_shared_vertex_contacts"] == 12
    assert result["panel_contact_hamming_distances"] == [1] * 12
    assert result["degrees_of_freedom"] == 36
    assert result["rigidity_rank"] == 24
    assert result["hessian_rank"] == 24
    assert result["nullity"] == 12
    assert result["rigid_body_zero_modes"] == 6
    assert result["internal_mechanisms"] == 6
    assert result["rigid_body_residual_frobenius"] < 1e-10
    assert result["positive_spectrum_exact_form"] == {
        "2-sqrt(2)": 3, "1": 5, "2": 9, "3": 3,
        "2+sqrt(2)": 3, "4": 1,
    }


def test_audit_keeps_physical_phason_identification_open():
    result = audit()
    assert result["classification"]["physical_phonon_phason_identification"] == "[O]"
    assert "no physical phason sector" in result["interpretation"]
