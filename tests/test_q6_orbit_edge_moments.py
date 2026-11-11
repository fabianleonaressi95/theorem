from audits.audit_q6_orbit_edge_moments import run_audit

def test_q6_orbit_edge_geometric_mass_and_bernoulli_moments():
    result=run_audit()
    assert result["counts"]["vertices"]==64
    assert result["counts"]["orbit_edges"]==256
    assert result["W0"]["shape"]==[64,64]
    assert result["W0"]["symmetric_exact"]
    assert result["W0"]["positive_diagonal_exact"]
    assert result["W1"]["shape"]==[256,256]
    assert result["W1"]["positive_diagonal_exact"]
    assert result["segment_moments"]["2"]=="1/12"
    assert result["segment_moments"]["4"]=="1/80"
