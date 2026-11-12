import math

from scripts.audit_t107_gray_torus_gibbs_fdt import (
    audit, edge_coherence_susceptibility, edge_coherence_variance
)


def test_gray_torus_graph_and_chain_maps_are_exact():
    result = audit()
    assert result["status"] == "PASS"
    assert result["q6_vertices"] == 64
    assert result["q6_edges"] == 192
    assert result["gray_coordinates_unique"]
    assert result["gray_graph_isomorphism"]
    assert result["quotient_vertices"] == 16
    assert result["quotient_edges"] == 32
    assert result["quotient_faces"] == 16
    assert result["fibre_cardinality"] == 4
    assert result["vertex_chain_map_max_abs"] == 0
    assert result["face_chain_map_max_abs"] == 0


def test_haar_edge_coherence_variance_and_linear_susceptibility():
    assert math.isclose(edge_coherence_variance(64), 1 / 8320)
    assert math.isclose(edge_coherence_susceptibility(1.0, 64), 1 / 8320)
    assert math.isclose(edge_coherence_susceptibility(2.5, 64), 2.5 / 8320)


def test_invalid_parameters_are_rejected():
    try:
        edge_coherence_variance(1)
        assert False, "dimension one should be rejected"
    except ValueError:
        pass
    try:
        edge_coherence_susceptibility(0.0, 64)
        assert False, "nonpositive beta should be rejected"
    except ValueError:
        pass
