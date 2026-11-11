from audits.audit_q6_d5_m3_d4_intertwiner_obstruction import run_audit


def test_original_q6_d5_sector_has_no_m3_d4_intertwiner():
    result = run_audit()
    assert result["all_exact_checks_passed"]
    assert result["transport"]["R_outside_old_edge_subspace_rank"] == 2
    assert result["transport"]["S_outside_old_edge_subspace_rank"] == 0
    assert result["S_representations"]["old_q6_rho_S"] == [
        [-1, 0, 0, 0, 0],
        [0, -1, 0, 0, 0],
        [0, 0, -1, 0, 0],
        [0, 0, 0, -1, 0],
        [0, 0, 0, 0, -1],
    ]
    assert result["S_representations"]["orbit_spectrum"] == [-1, -1, 1, 1, 1]
    assert not result["S_representations"]["invertible_intertwiner_exists"]
