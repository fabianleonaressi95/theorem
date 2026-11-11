from audits.audit_q6_admissible_face_w2 import run_audit


def test_admissible_face_w2_has_exact_chain_closure():
    result = run_audit()
    assert result["D4_order"] == 8
    assert result["orbit_edge_count"] == 256
    assert result["orbit_face_count"] == 384
    assert result["admissible_face_count"] > 0
    assert result["B2_admissible_shape"] == [256, result["admissible_face_count"]]
    assert result["W2_shape"] == [result["admissible_face_count"]] * 2
    assert result["B1B2_exact_zero"] is True
    assert result["W2_positive_definite"] is True


def test_admissible_faces_have_positive_exact_area():
    result = run_audit()
    assert result["area_squared_values"]
    assert all(value > 0 for value in result["area_squared_values"])
    assert all(face["W2_diagonal"].startswith("1/") or
               face["W2_diagonal"].startswith("sqrt(") or
               face["W2_diagonal"].isdigit()
               for face in result["faces"])
