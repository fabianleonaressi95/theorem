import math
import pytest

from scripts.audit_t101_trigram_phase_holonomy import (
    audit, complement_residuals, enumerate_edges, enumerate_plaquettes,
    hexagram_complement_mismatches, plaquette_audit,
)


def test_q6_has_192_edges_split_96_96():
    edges = enumerate_edges()
    assert len(edges) == 192
    assert sum(bit < 3 for _, _, bit in edges) == 96
    assert sum(bit >= 3 for _, _, bit in edges) == 96


def test_q6_has_240_elementary_square_plaquettes():
    assert len(enumerate_plaquettes()) == math.comb(6, 2) * 16 == 240


def test_opposite_circle_complement_registration():
    plus = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4]
    offset, sigma = math.pi, -1
    minus = [0.0] * 8
    for t in range(8):
        minus[t ^ 7] = (sigma * plus[t] + offset) % (2 * math.pi)
    assert max(abs(x) for x in complement_residuals(plus, minus, offset, sigma)) < 1e-12
    assert all(max(abs(x) for x in pair) < 1e-12
               for pair in hexagram_complement_mismatches(plus, minus, offset, sigma))


def test_both_layers_have_trivial_endpoint_phase_holonomy():
    plus = [0.31 * t + 0.07 * t * t for t in range(8)]
    minus = [0.17 * t - 0.03 * t * t for t in range(8)]
    for phases in (plus, minus):
        records = plaquette_audit(phases)
        assert len(records) == 240
        assert max(abs(float(r["circulation_mod_2pi"])) for r in records) < 1e-12
        assert max(abs(float(r["holonomy_real"]) - 1.0) +
                   abs(float(r["holonomy_imag"])) for r in records) < 1e-12


def test_audit_keeps_cross_circle_mismatch_separate_from_holonomy():
    plus = [0.0, 2.8, -2.8, 2.9, -2.9, 2.7, -2.7, 3.0]
    minus = [0.3 * t for t in range(8)]
    result = audit(plus, minus, offset=0.4, orientation=-1)
    assert result["edges_per_layer"] == 192
    assert result["plus_layer"]["plaquettes"] == 240
    assert result["minus_layer"]["plaquettes"] == 240
    assert result["plus_layer"]["pure_gauge_holonomy_pass"] is True
    assert result["minus_layer"]["pure_gauge_holonomy_pass"] is True
    assert len(result["hexagram_complement_mismatches"]) == 64


def test_invalid_phase_vectors_and_frame_orientation_are_rejected():
    with pytest.raises(ValueError):
        complement_residuals([0.0] * 7, [0.0] * 8)
    with pytest.raises(ValueError):
        complement_residuals([0.0] * 8, [0.0] * 8, orientation=0)
