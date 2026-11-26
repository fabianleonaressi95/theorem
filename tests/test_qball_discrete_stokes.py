from scripts.audit_qball_discrete_stokes import run


def test_qball_closed_shell_incidence_and_discrete_stokes():
    result = run()
    mesh = result["mesh"]
    inc = result["incidence"]
    stokes = result["discrete_stokes"]
    assert mesh["physical_shell_vertices"] == 60
    assert mesh["panels"] == 32
    assert mesh["triangles"] == 180
    assert mesh["edges"] == 270
    assert mesh["physical_seams"] == 90
    assert mesh["euler_characteristic"] == 2
    assert inc["rank_B1_over_Q_topologically_certified"] == 91
    assert inc["rank_B2_over_Q_topologically_certified"] == 179
    assert inc["first_betti_number"] == 0
    assert inc["max_abs_B1B2"] == 0
    assert stokes["max_abs_residual_R3_edge_cochain"] < 1e-11
    assert stokes["gradient_decomposition_curl_residual"] < 1e-11
