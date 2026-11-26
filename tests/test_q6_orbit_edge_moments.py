from audits.audit_q6_orbit_edge_moments import run_audit

def test_q6_orbit_edge_geometric_mass_and_bernoulli_moments():
    r=run_audit()
    assert r["counts"]["vertices"]==64
    assert r["counts"]["orbit_edges"]==256
    assert r["W0"]["shape"]==[64,64] and r["W0"]["symmetric_exact"]
    assert r["W1"]["shape"]==[256,256] and r["W1"]["positive_diagonal_exact"]
    assert r["segment_moments"]["2"]=="1/12"
    assert r["segment_moments"]["4"]=="1/80"
