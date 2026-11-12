import math
import pytest

from scripts.audit_t101_trigram_phase_holonomy import (
    audit, complement_displacements, complement_residuals,
    enumerate_edges, enumerate_plaquettes, phase_point, plaquette_audit,
)


def test_q6_has_192_edges_split_96_96():
    edges = enumerate_edges()
    assert len(edges) == 192
    assert sum(bit < 3 for _, _, bit in edges) == 96
    assert sum(bit >= 3 for _, _, bit in edges) == 96


def test_q6_has_240_elementary_square_plaquettes():
    assert len(enumerate_plaquettes()) == math.comb(6, 2) * 16 == 240


def test_antipodal_complement_fixture_is_exact():
    phases = [0.0, 0.2, 0.4, 0.6, 0.6 + math.pi, 0.4 + math.pi, 0.2 + math.pi, math.pi]
    residuals = complement_residuals(phases)
    assert max(abs(x) for x in residuals) < 1e-12
    for displacement in complement_displacements(phases):
        assert all(math.isclose(abs(x), math.pi, abs_tol=1e-12)
                   for x in displacement)


def test_phase_map_uses_ordered_lower_upper_trigrams():
    phases = [0.17 * t for t in range(8)]
    assert phase_point(5 + 8 * 2, phases) == (phases[5] % (2*math.pi),
                                               phases[2] % (2*math.pi))


def test_all_endpoint_phase_plaquette_holonomies_are_trivial():
    phases = [0.31 * t + 0.07 * t * t for t in range(8)]
    records = plaquette_audit(phases)
    assert len(records) == 240
    assert max(abs(float(r["circulation_mod_2pi"])) for r in records) < 1e-12
    assert max(abs(float(r["holonomy_real"]) - 1.0) +
               abs(float(r["holonomy_imag"])) for r in records) < 1e-12


def test_audit_does_not_label_branch_winding_as_curvature():
    phases = [0.0, 2.8, -2.8, 2.9, -2.9, 2.7, -2.7, 3.0]
    result = audit(phases)
    assert result["edges"] == 192
    assert result["plaquettes"] == 240
    assert result["pure_gauge_holonomy_pass"] is True
    assert "not, by itself, a disclination" in result["interpretation"]


def test_invalid_phase_vector_is_rejected():
    with pytest.raises(ValueError):
        complement_residuals([0.0] * 7)
