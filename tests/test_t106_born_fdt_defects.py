import math
import pytest

from scripts.audit_t106_born_fdt_defects import (
    audit, born_probabilities, dirichlet_uniform_moments,
    hexagram_to_z4, integer_to_bits, z4_to_hexagram,
    phase_loop_winding, phase_loop_u1_holonomy,
)


def test_born_map_returns_normalized_probabilities():
    p = born_probabilities([0.5 + 0j, 0.5j, 0.5 + 0j, 0.5j])
    assert p == [0.25] * 4
    assert math.isclose(sum(p), 1.0)


def test_born_map_rejects_unnormalized_state():
    with pytest.raises(ValueError):
        born_probabilities([1 + 0j, 1 + 0j])


def test_dirichlet_64_exact_moments():
    m = dirichlet_uniform_moments(64)
    assert math.isclose(m["mean"], 1 / 64)
    assert math.isclose(m["variance"], 63 / (64**2 * 65))
    assert math.isclose(m["off_diagonal_covariance"], -1 / (64**2 * 65))


def test_hexagram_z4_cubed_is_bijection():
    images = set()
    for h in range(64):
        bits = integer_to_bits(h)
        k = hexagram_to_z4(bits)
        images.add(k)
        assert z4_to_hexagram(k) == bits
    assert len(images) == 64


def test_vertex_phase_branch_winding_is_not_nontrivial_u1_holonomy():
    phases = [0.0, 2 * math.pi / 3, 4 * math.pi / 3]
    assert phase_loop_winding(phases) == 1
    assert abs(phase_loop_u1_holonomy(phases) - 1.0) < 1e-12


def test_audit_passes_and_does_not_claim_physical_fdt_or_defects():
    result = audit()
    assert result["status"] == "PASS"
    assert "requires" in result["fdt"]
    assert "requires" in result["frank_burgers"]
