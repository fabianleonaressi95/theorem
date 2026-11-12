import math
import pytest
from scripts.audit_t105_hexagram_moire_circuit import (
    audit, edges, hexagram_pair, phase_lift, branch_currents,
    continuity_residual, charge_covariance, phase_charge_cross,
    green_kubo_trapezoid,
)


def test_q6_has_64_distinct_sites_and_96_plus_96_edges():
    assert len({hexagram_pair(h) for h in range(64)}) == 64
    es = edges()
    assert len(es) == 192
    assert sum(bit < 3 for _, _, bit in es) == 96
    assert sum(bit >= 3 for _, _, bit in es) == 96


def test_two_circle_fields_lift_to_64_ordered_pairs():
    lift = phase_lift([0.0]*8, [0.0]*8)
    assert len(lift) == 64
    assert all(len(pair) == 2 for pair in lift)
    assert lift[0] == [0.0, 0.0]


def test_phase_lift_rejects_missing_trigram_measurements():
    with pytest.raises(ValueError):
        phase_lift([0.0]*7, [0.0]*8)


def test_kirchhoff_continuity_for_source_free_relaxation():
    g = [1.0]*192
    V = [math.sin(h) for h in range(64)]
    j = branch_currents(V, g)
    es = edges()
    # dot(Q) = -B j, with B(tail)=+1 and B(head)=-1.
    dQ = [0.0]*64
    for current, (tail, head, _) in zip(j, es):
        dQ[tail] -= current
        dQ[head] += current
    residual = continuity_residual(dQ, V, g, [0.0]*64)
    assert max(abs(x) for x in residual) < 1e-10
    assert abs(sum(dQ)) < 1e-10


def test_charge_covariance_is_64_by_64():
    samples = [[float((t+h) % 7) for h in range(64)] for t in range(5)]
    C = charge_covariance(samples)
    assert len(C) == 64 and all(len(row) == 64 for row in C)
    assert math.isclose(C[0][1], C[1][0], abs_tol=1e-12)


def test_phase_charge_cross_correlation_is_64_by_2():
    samples = [[float(t+h) for h in range(64)] for t in range(4)]
    lift = [[0.1*h, -0.07*h] for h in range(64)]
    K = phase_charge_cross(samples, lift)
    assert len(K) == 64 and all(len(row) == 2 for row in K)


def test_green_kubo_finite_window_integral():
    result = green_kubo_trapezoid([[1.0], [1.0], [1.0]], 0.1, 1.0, 1.0)
    assert len(result) == 1 and math.isfinite(result[0][0])


def test_audit_passes():
    assert audit()["status"] == "PASS"
