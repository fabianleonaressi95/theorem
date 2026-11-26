from scripts.audit_t099_shao_yong_q6 import (
    audit, edge_partition, neighbours, validate_circular_order, vertex,
)


def test_q6_is_product_of_two_trigram_cubes():
    result = audit()
    assert result["vertices"] == 64
    assert result["lower_line_edges"] == 96
    assert result["upper_line_edges"] == 96
    assert result["edges_total"] == 192


def test_every_hexagram_has_six_one_line_neighbours():
    assert all(len(neighbours(v)) == 6 for v in range(64))


def test_edge_families_are_disjoint_and_complete():
    lower, upper = edge_partition()
    assert len(lower) == len(upper) == 96
    assert lower.isdisjoint(upper)
    assert len(lower | upper) == 192


def test_matrix_indexing_is_bijective():
    labels = {vertex(lower, upper) for lower in range(8) for upper in range(8)}
    assert labels == set(range(64))


def test_circular_order_validator_does_not_assume_an_order():
    assert validate_circular_order(list(range(64)))
    assert not validate_circular_order(list(range(63)))
    assert not validate_circular_order([0] * 64)
