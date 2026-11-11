from audits.audit_q6_reynolds_weighted_hodge import run_audit


def test_reynolds_hodge_has_exact_chain_and_symmetry():
    result = run_audit()
    assert result["D4_order"] == 8
    assert result["orbit_edges"] == 256
    assert result["orbit_faces_total"] == 384
    assert result["admissible_parallelogram_faces"] > 0
    assert result["B1B2_exact_zero"] is True
    assert result["D4_metric_invariance_exact"] is True
    assert result["incidence_equivariance_exact"] is True
    assert result["K1_symmetric_exact"] is True


def test_generalized_hodge_problem_uses_edge_mass():
    result = run_audit()
    assert result["K1_definition"] == "B1.T W0 B1 + B2 W2 B2.T"
    assert result["generalized_eigenproblem"] == "K1 x = lambda W1 x"
    assert result["spectrum_computed"] is False
