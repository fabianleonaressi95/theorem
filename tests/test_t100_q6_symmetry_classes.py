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
