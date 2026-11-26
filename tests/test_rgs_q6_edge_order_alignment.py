import numpy as np

from scripts.audit_rgs_q6_edge_order_alignment import (
    audit_edge_order_alignment,
    canonical_q6_edges,
    rgs_archive_edges,
)


def test_rgs_and_canonical_q6_edge_sets_align_exactly():
    rgs = rgs_archive_edges()
    canonical = canonical_q6_edges()
    report = audit_edge_order_alignment()
    permutation = np.asarray(report["rgs_to_canonical"], dtype=np.int64)
    inverse = np.asarray(report["canonical_to_rgs"], dtype=np.int64)

    assert rgs.shape == (192, 3)
    assert canonical.shape == (192, 2)
    assert np.array_equal(canonical[permutation], rgs[:, :2])
    assert np.array_equal(inverse[permutation], np.arange(192))
    assert report["degree_min"] == report["degree_max"] == 6
    assert report["edge_set_equal"] is True


def test_axis_labels_are_opposite_endian_conventions():
    rgs = rgs_archive_edges()
    assert np.array_equal(rgs[:, 2], np.asarray([
        (int(u) ^ int(v)).bit_length() - 1 for u, v in rgs[:, :2]
    ]))
