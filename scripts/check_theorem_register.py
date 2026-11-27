#!/usr/bin/env python3
"""Lightweight consistency check for docs/THEOREM_MASTER_REGISTER.csv.

Verifies:
- every theorems/**/*.md card has a register row (matched on `file`);
- no missing/extra rows;
- every status belongs to the allowed taxonomy;
- referenced scripts/tests paths exist;
- T### dependencies resolve to at least one card id;
- duplicate card ids are reported (known issue — see audit report).

Exit code 0 on success; warnings do not fail the check.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / "docs" / "THEOREM_MASTER_REGISTER.csv"
THEOREMS = ROOT / "theorems"

TAXONOMY = {
    "PROVED", "EXACT_CERTIFICATE", "NUMERICALLY_VERIFIED", "CONDITIONAL",
    "CANDIDATE", "HYPOTHESIS", "OPEN", "SUPERSEDED", "QUARANTINED",
}


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    cards = sorted(THEOREMS.rglob("*.md"))
    card_paths = {p.relative_to(ROOT).as_posix() for p in cards}

    if not CSV.is_file():
        print(f"ERROR: missing {CSV}")
        return 1
    with CSV.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    reg_paths = {r["file"] for r in rows}
    missing = card_paths - reg_paths
    extra = reg_paths - card_paths
    for m in sorted(missing):
        errors.append(f"card not in register: {m}")
    for e in sorted(extra):
        errors.append(f"register row without card: {e}")

    bad_status = [r["id"] for r in rows if r["status"] not in TAXONOMY]
    for b in bad_status:
        errors.append(f"status outside taxonomy: {b} -> {next(r['status'] for r in rows if r['id']==b)}")

    for r in rows:
        for col in ("scripts", "tests"):
            for ref in filter(None, r[col].split(";")):
                ref = ref.strip()
                if ref and not (ROOT / ref).exists():
                    warnings.append(f"{r['id']}: referenced {col} path missing: {ref}")
        for dep in filter(None, r["dependencies"].split(";")):
            dep = dep.strip()
            if dep and not any(x["id"] == dep for x in rows):
                warnings.append(f"{r['id']}: unresolved dependency {dep}")

    ids = {}
    record_keys = {}
    for r in rows:
        ids.setdefault(r["id"], []).append(r["file"])
        key = r.get("record_key", "").strip()
        if not key:
            errors.append(f"missing unique record_key for {r['file']}")
        else:
            record_keys.setdefault(key, []).append(r["file"])
    for key, files in record_keys.items():
        if len(files) > 1:
            errors.append(f"duplicate record_key {key}: {', '.join(sorted(files))}")
    for cid, files in ids.items():
        if len(files) > 1:
            warnings.append(f"duplicate card id {cid}: {len(files)} files "
                            f"({', '.join(sorted(files)[:3])}{'...' if len(files)>3 else ''})")

    counts = {}
    for r in rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1

    print(f"cards={len(cards)} rows={len(rows)}")
    for s in sorted(TAXONOMY):
        print(f"  {s}: {counts.get(s, 0)}")
    for w in warnings:
        print(f"WARN {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"errors={len(errors)} warnings={len(warnings)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
