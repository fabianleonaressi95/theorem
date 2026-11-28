from scripts.audit_q6_vertex_link_t166 import audit_q6_vertex_link


def test_q6_raw_vertex_link_exact_homology_obstruction():
    result = audit_q6_vertex_link()
    assert result["f_vector"] == (6, 15, 20, 15)
    assert result["boundary_ranks"] == {1: 5, 2: 10, 3: 10}
    assert result["betti_numbers_over_q"] == {0: 1, 1: 0, 2: 0, 3: 5}
    assert result["euler_characteristic"] == -4
    assert result["is_s3_homology"] is False
    assert result["is_3_ball_homology"] is False
