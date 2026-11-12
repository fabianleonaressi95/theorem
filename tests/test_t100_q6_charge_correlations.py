import math
from scripts.audit_t100_q6_charge_correlations import (
    audit, hypercube_distance, rc_charge_correlation,
    walsh_character, walsh_inverse, walsh_transform,
)

def test_walsh_transform_is_invertible():
    q = [float((h*h + 3*h + 7) % 19) for h in range(64)]
    rec = walsh_inverse(walsh_transform(q))
    assert max(abs(a-b) for a,b in zip(q,rec)) < 1e-12

def test_walsh_characters_diagonalize_q6_laplacian():
    for subset in range(64):
        weight = subset.bit_count()
        for h in range(64):
            action = sum(walsh_character(h,subset) -
                         walsh_character(h ^ (1 << bit),subset)
                         for bit in range(6))
            assert action == 2*weight*walsh_character(h,subset)

def test_rc_covariance_depends_only_on_hamming_distance():
    by_distance = {d: rc_charge_correlation(0,(1<<d)-1,0.3,2,1.5,4)
                   for d in range(7)}
    for h in range(64):
        for hp in range(64):
            assert math.isclose(
                rc_charge_correlation(h,hp,0.3,2,1.5,4),
                by_distance[hypercube_distance(h,hp)], rel_tol=1e-12, abs_tol=1e-12)

def test_projected_covariance_has_zero_row_sum():
    for tau in (0.0,0.2,2.0):
        total = sum(rc_charge_correlation(0,hp,tau,1,1,1) for hp in range(64))
        assert abs(total) < 1e-10

def test_exact_audit_passes():
    assert audit()["status"] == "PASS"
