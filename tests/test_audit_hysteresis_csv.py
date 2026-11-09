import json
from scripts.audit_hysteresis_csv import audit_csv


def test_csv_audit_reports_schema_missing_and_numeric_ranges(tmp_path):
    path = tmp_path / "loop.csv"
    path.write_text("time,field,magnetization,label\n0,0.0,0.1,up\n1,1.0,0.4,up\n2,,0.2,down\n", encoding="utf-8")
    report = audit_csv(path)
    assert report["rows"] == 3
    assert report["columns"] == ["time", "field", "magnetization", "label"]
    assert report["column_audit"]["field"]["missing"] == 1
    assert report["column_audit"]["field"]["min"] == 0.0
    assert report["column_audit"]["field"]["max"] == 1.0
    assert report["column_audit"]["label"]["numeric"] is False
    assert len(report["sha256"]) == 64


def test_csv_audit_rejects_duplicate_headers(tmp_path):
    path = tmp_path / "bad.csv"
    path.write_text("x,x\n1,2\n", encoding="utf-8")
    import pytest
    with pytest.raises(ValueError):
        audit_csv(path)
