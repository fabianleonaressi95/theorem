#!/usr/bin/env python3
"""Non-destructive audit for the pneumatic actuator CSV in Issue #113.

No physical unit is inferred from bare column names. Frequency in Hz is only
reported when the caller explicitly confirms that Time is measured in seconds.
The source CSV is never modified.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
from statistics import median

EXPECTED = ("Input", "Output", "Time")
PAPER_FREQUENCY_HZ = 0.05


def _finite_float(value: str, column: str, row: int) -> float:
    try:
        x = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"non-numeric {column!r} at CSV row {row}: {value!r}") from exc
    if not math.isfinite(x):
        raise ValueError(f"non-finite {column!r} at CSV row {row}: {value!r}")
    return x


def _turning_points(values: list[float]) -> list[dict]:
    """Return extrema indices, ignoring flat steps and preserving plateau centres."""
    diffs = [b - a for a, b in zip(values, values[1:])]
    signs = [1 if d > 0 else (-1 if d < 0 else 0) for d in diffs]
    extrema = []
    previous = 0
    for i, sign in enumerate(signs):
        if sign == 0:
            continue
        if previous and sign != previous:
            # The reversal is between the previous non-flat segment and this one.
            extrema.append({"index": i + 1, "kind": "maximum" if previous > 0 else "minimum"})
        previous = sign
    return extrema


def audit_csv(path: str | Path, time_unit: str | None = None) -> dict:
    path = Path(path)
    raw = path.read_bytes()
    md5 = hashlib.md5(raw).hexdigest()
    sha256 = hashlib.sha256(raw).hexdigest()

    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames is None:
            raise ValueError("CSV has no header")
        fields = tuple((x or "").strip() for x in reader.fieldnames)
        if fields != EXPECTED:
            raise ValueError(f"expected columns {EXPECTED!r}, found {fields!r}")
        rows = list(reader)

    if not rows:
        raise ValueError("CSV contains no data rows")

    x, y, t = [], [], []
    for row_number, row in enumerate(rows, start=2):
        x.append(_finite_float(row["Input"], "Input", row_number))
        y.append(_finite_float(row["Output"], "Output", row_number))
        t.append(_finite_float(row["Time"], "Time", row_number))

    if len(t) < 3:
        raise ValueError("at least three samples are required")
    dt = [b - a for a, b in zip(t, t[1:])]
    strictly_increasing = all(d > 0 for d in dt)
    if not strictly_increasing:
        raise ValueError("Time must be strictly increasing; inspect ordering/duplicates")

    dt_med = median(dt)
    dt_max_dev = max(abs(d - dt_med) for d in dt)
    extrema = _turning_points(x)
    maxima = [t[e["index"]] for e in extrema if e["kind"] == "maximum"]
    minima = [t[e["index"]] for e in extrema if e["kind"] == "minimum"]
    periods = [b - a for a, b in zip(maxima, maxima[1:])]
    if not periods:
        periods = [b - a for a, b in zip(minima, minima[1:])]
    period_units = median(periods) if periods else None

    frequency_hz = None
    if time_unit == "s" and period_units and period_units > 0:
        frequency_hz = 1.0 / period_units

    report = {
        "dataset": "Zenodo 10.5281/zenodo.15584329 — pneumatic bending actuator",
        "file": path.name,
        "size_bytes": len(raw),
        "md5": md5,
        "sha256": sha256,
        "rows": len(rows),
        "columns": list(fields),
        "time": {
            "unit": time_unit or "UNSPECIFIED",
            "start": t[0],
            "end": t[-1],
            "median_step": dt_med,
            "max_abs_step_deviation": dt_max_dev,
            "strictly_increasing": strictly_increasing,
            "median_peak_to_peak_period_in_time_units": period_units,
            "frequency_hz": frequency_hz,
        },
        "channels": {
            "Input": {"min": min(x), "max": max(x)},
            "Output": {"min": min(y), "max": max(y)},
        },
        "reversals": extrema,
        "source_article": {
            "doi": "10.3390/act14070321",
            "reported_frequency_hz": PAPER_FREQUENCY_HZ,
            "reported_period_s": 1.0 / PAPER_FREQUENCY_HZ,
            "frequency_comparison": (
                "COMPARABLE_IN_SECONDS"
                if time_unit == "s" and frequency_hz is not None
                else "UNRESOLVED_TIME_UNIT"
            ),
        },
        "preprocessing": {
            "applied": False,
            "raw_values_preserved": True,
            "normalization": "not applied; article states both channels were normalized for its fits",
            "output_semantics": "curvature according to source article; not force",
        },
        "interpretation": (
            "Structural audit only. Bare Time column does not establish seconds. "
            "Do not infer physical frequency or compare with 0.05 Hz until the time unit "
            "is independently documented."
        ),
    }
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path)
    parser.add_argument("--time-unit", choices=("s",), default=None,
                        help="confirm Time is in seconds; omitted means unknown")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = json.dumps(audit_csv(args.csv, args.time_unit), indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
