from scripts.audit_q6_square_handlebody_t167 import q6_square_complex_audit


def test_q6_square_complex_handlebody_invariants():
    assert q6_square_complex_audit() == {
        "vertices": 64,
        "edges": 192,
        "squares": 240,
        "rank_d1_mod2": 63,
        "rank_d2_mod2": 129,
        "euler_characteristic": 112,
        "b2_from_integral_exactness": 111,
    }
