import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from audit_c60_sw_pi_density import audit


def test_pi_huckel_population_is_normalized_and_sw_changes_spectrum():
    result = audit()
    before = result["starting_C60"]["pi_model"]
    after = result["SW_5_6"]["selected_postgraph_pi_model"]
    assert abs(before["electron_count_trace_P"] - 60.0) < 1e-8
    assert abs(after["electron_count_trace_P"] - 60.0) < 1e-8
    assert before["site_population_covariance"]["population_std"] < 1e-10
    assert after["site_population_covariance"]["population_std"] > 1e-3
    gap0 = before["H_minus_adjacency_hopping_t_1"]["HOMO_LUMO_gap_over_t"]
    gap1 = after["H_minus_adjacency_hopping_t_1"]["HOMO_LUMO_gap_over_t"]
    assert gap1 < gap0
    assert result["SW_5_6"]["all_30_labelled_moves"]["HOMO_LUMO_gap_over_t_spread"] < 1e-10
    assert result["SW_5_6"]["all_30_labelled_moves"]["site_population_anisotropy_spread"] < 1e-10


def test_post_sw_stabilizer_is_v4_and_q6_direct_graph_map_is_impossible():
    result = audit()
    assert result["SW_5_6"]["postgraph_automorphism_group"]["order"] == 4
    assert result["SW_5_6"]["postgraph_automorphism_group"]["is_klein_four_V4"] is True
    obstruction = result["Q6_graph_map_obstruction"]
    assert obstruction["Q6_is_bipartite"] is True
    assert obstruction["C60_contains_pentagonal_odd_cycle"] is True
    assert obstruction["direct_C60_carbon_graph_to_Q6_1_skeleton_graph_homomorphism_exists"] is False
