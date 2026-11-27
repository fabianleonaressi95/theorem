import numpy as np

from audits.morphodynamics import mq005_rgs_tetrahedron_flux as audit


def test_rgs_tetrahedron_is_nondegenerate_and_flux_closed():
    result = audit.build_audit()
    assert result["oriented_volume"] > 0.1
    assert result["closure_residual_l2"] < 1e-12
    assert len(result["faces"]) == 4
    assert all(face["area"] > 0.0 for face in result["faces"])


def test_selected_carrier_points_are_not_a_q6_k4():
    result = audit.build_audit()
    assert result["q6_induced_edge_count"] == 2
    assert result["q6_complete_graph_k4"] is False
    assert result["q6_graph_bipartite"] is True
    assert result["q6_global_k4_obstruction"] is True
    assert sorted(edge["q6_hamming_distance"] for edge in result["edges"]) == [
        1, 1, 2, 2, 2, 3
    ]


def test_area_vectors_rotate_covariantly_and_preserve_closure():
    result = audit.build_audit()
    vectors = np.asarray([face["area_vector"] for face in result["faces"]])
    rng = np.random.default_rng(20261127)
    for _ in range(20):
        q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
        if np.linalg.det(q) < 0:
            q[:, 0] *= -1
        rotated = vectors @ q.T
        assert np.linalg.norm(rotated.sum(axis=0)) < 1e-12
        assert np.allclose(
            np.linalg.norm(rotated, axis=1),
            np.linalg.norm(vectors, axis=1),
            atol=1e-12,
            rtol=0.0,
        )


def test_audit_does_not_assign_quantum_spins():
    result = audit.build_audit()
    assert result["classification"]["su2_spin_assignment"] == "open_not_assigned"
    assert result["classification"]["physical_area_scale"] == "open_not_assigned"
