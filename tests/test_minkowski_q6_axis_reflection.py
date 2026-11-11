from audits.audit_minkowski_q6_axis_reflection import run_audit


def test_minkowski_q6_one_axis_reflection():
    report = run_audit()
    assert all(report["checks"].values())
    assert report["one_axis_sector_results"]["4"]["even"]["betti"] == [1, 0, 31]
    assert report["one_axis_sector_results"]["4"]["odd"]["betti"] == [0, 0, 80]
    assert report["full_three_axis_inversion_sector_results"]["even"]["betti"] == [1, 0, 55]
    assert report["full_three_axis_inversion_sector_results"]["odd"]["betti"] == [0, 0, 56]
    assert report["canonical_q6_graph_antipode_sector_results"]["even"]["betti"] == [1, 0, 55]
    assert report["canonical_q6_graph_antipode_sector_results"]["odd"]["betti"] == [0, 0, 56]
