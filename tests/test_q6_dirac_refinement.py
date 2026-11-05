import numpy as np

from scripts.verify_q6_dirac_refinement import audit, gamma_matrices


def test_six_dimensional_clifford_relations():
    gs = gamma_matrices()
    eye = np.eye(8)
    for j in range(6):
        for k in range(6):
            target = 2 * eye if j == k else np.zeros((8, 8))
            assert np.linalg.norm(gs[j] @ gs[k] + gs[k] @ gs[j] - target) < 1e-12


def test_q6_centered_difference_degeneracy_and_doublers():
    result = audit(n_values=(1, 2))
    q6, refined = result["refinements"]
    assert q6["centered_operator_identically_zero"] is True
    assert q6["naive_zero_corners"] == 64
    assert refined["centered_operator_identically_zero"] is False
    assert refined["naive_zero_corners"] == 64
    assert q6["orientation_sum"] == refined["orientation_sum"] == 0


def test_wilson_lifts_all_but_origin_corner():
    result = audit(n_values=(1, 2), r=1.0)
    for row in result["refinements"]:
        assert row["wilson_zero_corners"] == 1
        assert row["wilson_nonzero_corner_mass_min"] > 0


def test_fixed_momentum_error_respects_remainder_bound():
    result = audit()
    for row in result["fixed_momentum_convergence"]:
        assert row["coefficient_l1_error"] <= row["proved_l1_upper_bound"] + 1e-14
