from scripts.audit_mobius_brownian import (
    audit, block_statistics, block_sums, mertens_prefix, mobius_sieve, squarefree_signs,
)


def test_mobius_values_through_ten_are_exact():
    assert mobius_sieve(10)[1:] == [1, -1, -1, 0, -1, 1, -1, 0, 0, 1]


def test_mertens_prefix_through_ten_is_exact():
    assert mertens_prefix(mobius_sieve(10))[1:] == [1, 0, -1, -1, -2, -1, -2, -2, -2, -1]


def test_squarefree_sign_sequence_uses_increasing_squarefree_integers():
    assert squarefree_signs(mobius_sieve(14)) == [1, -1, -1, -1, 1, -1, 1, -1, -1, 1]


def test_block_sums_discard_incomplete_tail():
    assert block_sums([1, -1, 1, 1, -1], 2) == [0, 2]


def test_block_statistics_handle_zero_variance():
    result = block_statistics([1, -1, 1, -1, 1, -1, 1, -1], 2)
    assert result["block_count"] == 4
    assert result["variance"] == 0.0
    assert result["standardized_fourth_moment"] is None
    assert result["lag1_correlation"] is None


def test_audit_reports_finite_scope_and_known_mertens_value():
    result = audit(100, [4, 8])
    assert result["mertens_M_n"] == 1
    assert result["squarefree_count"] == 61
    assert "not a proof" in result["scope"]
