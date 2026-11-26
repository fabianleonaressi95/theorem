from fractions import Fraction

from scripts.audit_t108_boolean_influence_q6 import (
    SIZE,
    audit,
    face_curl,
    influences,
    variance,
    walsh_coefficients,
)


def test_exact_walsh_influence_identity():
    values = [Fraction((17 * x + 3 * x.bit_count() ** 2) % 29) for x in range(SIZE)]
    coeffs = walsh_coefficients(values)
    lhs = sum(influences(values))
    rhs = 4 * sum(
        Fraction(mask.bit_count()) * coeffs[mask] ** 2
        for mask in range(1, SIZE)
    )
    assert lhs == rhs


def test_six_dimensional_poincare_influence_bound():
    values = [Fraction((31 * x + 7 * (x ^ (x >> 1))) % 43) for x in range(SIZE)]
    assert max(influences(values)) >= Fraction(2, 3) * variance(values)


def test_exact_gradient_has_zero_square_curl():
    values = [Fraction((x * x + 5 * x + 1) % 37) for x in range(SIZE)]
    curls = face_curl(values)
    assert len(curls) == 15 * 16
    assert all(curl == 0 for curl in curls)


def test_audit_passes_with_exact_arithmetic():
    result = audit()
    assert result["status"] == "PASS"
    assert result["arithmetic"] == "exact rational"
    assert result["all_square_curls_zero"]
