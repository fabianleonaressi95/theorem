from audits.audit_minkowski_q6_d4_cell_closure import run_audit


def test_minkowski_q6_d4_orbit_action_and_graph():
    report = run_audit()
    assert report["group"]["order"] == 8
    assert report["group"]["R4_identity"]
    assert report["group"]["S2_identity"]
    assert report["group"]["SRS_R_inverse"]
    assert report["graph_orbit"]["vertices"] == 64
    assert report["graph_orbit"]["direction_count"] == 8
    assert report["graph_orbit"]["edges"] == 256
    assert report["graph_orbit"]["degree_regular"] == 8


def test_minkowski_q6_d4_orbit_chain_identities():
    report = run_audit()
    assert report["chain_complex"]["B1B2_zero"]
    assert report["chain_complex"]["all_eight_D4_chain_maps_exact"]
    assert report["chain_complex"]["chain_map_count"] == 8


def test_minkowski_q6_d4_face_regularity_is_explicitly_reported():
    report = run_audit()
    square = report["square_orbit"]
    assert square["distinct_faces"] > 0
    assert square["regular_square_complex"] == (
        square["incompatible_cycles_on_same_vertex_set"] == 0
        and square["non_regular_intersections"] == 0
    )
