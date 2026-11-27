from scripts.audit_t156_jitterbug_incidence import run_audit


def test_exactly_two_alternating_diagonal_patterns_match_snub_cube():
    result = run_audit()
    assert result["assignments_tested"] == 2**12
    assert result["incidence_isomorphism_count"] == 2
    assert result["patterns"] == ["010101010101", "101010101010"]
    assert result["split_square_count"] == 12
    assert result["retained_square_count"] == 6
