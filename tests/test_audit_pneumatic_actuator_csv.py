import hashlib
import json

import pytest

from scripts.audit_pneumatic_actuator_csv import audit_csv


def _write_csv(path, rows):
    path.write_text(
        "Input,Output,Time\n" + "".join(f"{u},{y},{t}\n" for u, y, t in rows),
        encoding="utf-8",
    )


def test_audit_preserves_raw_checksum_and_does_not_assume_seconds(tmp_path):
    path = tmp_path / "actuator.csv"
    rows = [(0, 0.1, 0), (1, 0.8, 1), (0, 0.2, 2),
            (1, 0.9, 3), (0, 0.3, 4)]
    _write_csv(path, rows)
    report = audit_csv(path)
    assert report["rows"] == len(rows)
    assert report["md5"] == hashlib.md5(path.read_bytes()).hexdigest()
    assert report["sha256"] == hashlib.sha256(path.read_bytes()).hexdigest()
    assert report["time"]["unit"] == "UNSPECIFIED"
    assert report["time"]["frequency_hz"] is None
    assert report["source_article"]["frequency_comparison"] == "UNRESOLVED_TIME_UNIT"
    assert report["preprocessing"]["applied"] is False


def test_frequency_is_reported_only_after_explicit_seconds_confirmation(tmp_path):
    path = tmp_path / "actuator.csv"
    rows = [(0, 0.1, 0), (1, 0.8, 10), (0, 0.2, 20),
            (1, 0.9, 30), (0, 0.3, 40), (1, 1.0, 50)]
    _write_csv(path, rows)
    report = audit_csv(path, time_unit="s")
    assert report["time"]["frequency_hz"] == pytest.approx(0.05)


def test_wrong_schema_is_rejected(tmp_path):
    path = tmp_path / "wrong.csv"
    path.write_text("time,input,output\n0,0,1\n1,1,2\n", encoding="utf-8")
    with pytest.raises(ValueError, match="expected columns"):
        audit_csv(path)


def test_non_monotone_time_is_rejected(tmp_path):
    path = tmp_path / "bad-time.csv"
    _write_csv(path, [(0, 1, 0), (1, 2, 1), (0, 3, 1)])
    with pytest.raises(ValueError, match="strictly increasing"):
        audit_csv(path)
