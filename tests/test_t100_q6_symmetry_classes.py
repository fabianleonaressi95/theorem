from scripts.audit_t100_q6_symmetry_classes import (
    complement_yin_yang, line_reversal_orbits, permutation_orbits,
    project_to_orbit_invariant, reversal_and_complement_orbits,
    reverse_lines, symmetry_audit,
)

def test_line_reversal_has_36_orbits():
    assert len(line_reversal_orbits()) == 36

def test_reversal_and_global_complement_have_20_orbits():
    assert len(reversal_and_complement_orbits()) == 20

def test_arbitrary_line_permutations_have_seven_orbits():
    assert len(permutation_orbits()) == 7
    assert [len(o) for o in permutation_orbits()] == [1,6,15,20,15,6,1]

def test_transformations_are_involutions():
    for h in range(64):
        assert reverse_lines(reverse_lines(h)) == h
        assert complement_yin_yang(complement_yin_yang(h)) == h

def test_projection_is_constant_on_each_orbit():
    values = [float(h*h-3*h) for h in range(64)]
    for orbits in (line_reversal_orbits(), reversal_and_complement_orbits(),
                   permutation_orbits()):
        projected = project_to_orbit_invariant(values, orbits)
        for orbit in orbits:
            assert len({projected[h] for h in orbit}) == 1

def test_exact_symmetry_audit_passes():
    assert symmetry_audit()["status"] == "PASS"

from scripts.audit_t100_q6_symmetry_classes import analyze_measured_vector

def test_measured_vector_comparison_distinguishes_symmetry_models():
    constant = [2.5] * 64
    result = analyze_measured_vector(constant)
    assert all(item["residual_l2"] < 1e-12 for item in result.values())
    arbitrary = [float(h) for h in range(64)]
    result = analyze_measured_vector(arbitrary)
    assert result["unrestricted"]["residual_l2"] == 0.0
    assert result["full_cube_automorphisms"]["residual_l2"] > 0.0

from scripts.audit_t100_q6_symmetry_classes import (
    net_polarity_charge, net_polarity_degeneracies,
    net_polarity_random_walk_correlation, net_polarity_commutator_frobenius,
)

def test_net_polarity_candidate_has_seven_levels_and_binomial_degeneracies():
    values = [net_polarity_charge(h) for h in range(64)]
    assert sorted(set(values)) == [-6,-4,-2,0,2,4,6]
    assert list(net_polarity_degeneracies().values()) == [1,6,15,20,15,6,1]

def test_net_polarity_is_permutation_and_reversal_invariant_but_sign_flips_on_complement():
    for h in range(64):
        assert net_polarity_charge(reverse_lines(h)) == net_polarity_charge(h)
        assert net_polarity_charge(complement_yin_yang(h)) == -net_polarity_charge(h)

def test_random_walk_autocorrelation_has_correct_variance_and_decay():
    assert abs(net_polarity_random_walk_correlation(0, 1.0, 2.0)-24.0) < 1e-12
    assert abs(net_polarity_random_walk_correlation(0.5, 1.0, 2.0)-24.0*__import__("math").exp(-1)) < 1e-12

def test_net_polarity_candidate_is_not_conserved_by_q6_hopping():
    assert abs(net_polarity_commutator_frobenius(1.0)-16.0*(6.0**0.5)) < 1e-12
