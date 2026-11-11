from audits.audit_toroid_q6_spectral_bridge import run_audit


def test_torus_grid_is_a_closed_exact_cell_complex():
    result = run_audit()
    torus = result["torus_cellulation"]
    assert torus["vertices"] == 64
    assert torus["edges"] == 128
    assert torus["faces"] == 64
    assert torus["B1B2_exact_zero"] is True
    assert torus["betti1_exact"] == 2
    assert torus["betti2_exact"] == 1


def test_d4_comparison_does_not_assume_raw_invariance():
    result = run_audit()
    assert result["D4"]["order"] == 8
    assert sum(result["D4"]["vertex_representation_sector_dimensions"].values()) == 64
    assert result["interpretation"]["raw_spectral_match_claimed"] is False
    assert result["interpretation"]["intertwiner_claimed"] is False
    assert result["interpretation"]["chain_map_between_torus_and_q6_claimed"] is False


def test_both_raw_spectra_are_reported_separately():
    result = run_audit()
    spectra = result["spectra"]
    assert len(spectra["torus_raw_generalized_eigenvalues"]) == 64
    assert len(spectra["q6_raw_graph_eigenvalues"]) == 64
