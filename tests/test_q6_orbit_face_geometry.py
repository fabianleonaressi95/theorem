from audits.audit_q6_orbit_face_geometry import run_audit


def test_q6_orbit_face_geometry_is_exactly_partitioned():
    result = run_audit()
    assert result["D4_order"] == 8
    assert result["face_count"] == 384
    counts = result["classification_counts"]
    assert counts["planar_nonzero_area"] + counts["planar_degenerate"] + counts["nonplanar"] == 384
    assert len(result["records"]) == 384
    assert all(record["affine_rank"] in (2, 3) for record in result["records"])
    assert result["W2"]["assigned"] is False


def test_parallelogram_certificate_is_exact():
    result = run_audit()
    for record in result["records"]:
        if record["parallelogram"]:
            assert record["planar"]
            assert record["category"] == "planar_nonzero_area"
