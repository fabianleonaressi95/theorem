#!/usr/bin/env python3
"""Non-destructive schema/quality audit for an experimental hysteresis CSV.

This tool deliberately does not guess channel semantics, units, cycle
boundaries or preprocessing. It reports the file structure so a dataset-
specific loader can be written only after the data dictionary is inspected.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path


def audit_csv(path):
    path = Path(path)
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames:
            raise ValueError("CSV must contain a header row")
        fields = [str(x).strip() if x is not None else "" for x in reader.fieldnames]
        if any(not x for x in fields) or len(set(fields)) != len(fields):
            raise ValueError("CSV headers must be non-empty and unique")
        stats = {name: {"nonempty": 0, "missing": 0, "numeric": True,
                        "finite": 0, "min": None, "max": None, "mean": None,
                        "_sum": 0.0} for name in fields}
        rows = 0
        for row in reader:
            rows += 1
            for name in fields:
                value = (row.get(name) or "").strip()
                item = stats[name]
                if not value:
                    item["missing"] += 1
                    continue
                item["nonempty"] += 1
                try:
                    number = float(value)
                except ValueError:
                    item["numeric"] = False
                    continue
                if not math.isfinite(number):
                    item["numeric"] = False
                    continue
                item["finite"] += 1
                item["min"] = number if item["min"] is None else min(item["min"], number)
                item["max"] = number if item["max"] is None else max(item["max"], number)
                item["_sum"] += number
    for item in stats.values():
        item["mean"] = item.pop("_sum") / item["finite"] if item["finite"] else None
        if not item["numeric"]:
            item["min"] = item["max"] = item["mean"] = None
    return {
        "file": path.name,
        "sha256": digest,
        "rows": rows,
        "columns": fields,
        "column_audit": stats,
        "interpretation": "schema/quality audit only; no units, channels, cycles or preprocessing inferred",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = audit_csv(args.csv)
    payload = json.dumps(report, indent=2) + "\\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
