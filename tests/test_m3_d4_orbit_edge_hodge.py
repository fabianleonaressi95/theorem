from audits.audit_m3_d4_orbit_edge_hodge import run_audit


def test_m3_d4_orbit_edge_hodge_is_an_exact_chain_complex():
    result = run_audit()
    assert result["counts"]["vertices"] == 64
    assert result["counts"]["edges"] == 256
    assert result["boundary"]["B1B2_zero"]
    assert result["D4"]["order"] == 8
    assert result["D4"]["all_eight_signed_chain_maps_exact"]
    assert result["boundary"]["beta1"] >= 0


def test_every_reported_edge_hodge_eigenspace_is_d4_invariant():
    result = run_audit()
    for eigenspace in result["edge_hodge"]["eigenspaces"].values():
        assert eigenspace["D4_invariant"]
