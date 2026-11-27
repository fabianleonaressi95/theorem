#!/usr/bin/env python3
"""Build docs/project/DUPLICATE_CARD_ID_MAP.json.

Maps every duplicated card-id prefix to the full list of card file paths that
share it. File paths are the stable identifiers; prefixes are NOT unique and
must not be used as keys until the author approves a canonical numbering
policy. No card is renumbered and no cross-reference is rewritten.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_theorem_register import card_id  # noqa: E402

OUT = ROOT / "docs" / "project" / "DUPLICATE_CARD_ID_MAP.json"


def main() -> int:
    groups: dict[str, list[str]] = defaultdict(list)
    for path in sorted((ROOT / "theorems").rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        groups[card_id(path)].append(rel)

    duplicates = {
        cid: sorted(paths)
        for cid, paths in sorted(groups.items())
        if len(paths) > 1
    }
    payload = {
        "schema": "duplicate-card-id-map/v1",
        "generated": "2026-11-27",
        "policy": (
            "File paths under theorems/ are the stable identifiers. Card-id "
            "prefixes are reused across distinct records and are NOT unique; "
            "do not use them as primary keys. Renumbering and cross-reference "
            "rewrites require explicit author approval."
        ),
        "total_cards": sum(len(v) for v in groups.values()),
        "unique_ids": len(groups),
        "duplicated_ids": len(duplicates),
        "cards_in_duplicate_groups": sum(len(v) for v in duplicates.values()),
        "duplicates": duplicates,
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"cards={payload['total_cards']} unique_ids={payload['unique_ids']} "
          f"duplicated_ids={payload['duplicated_ids']} "
          f"cards_in_dup_groups={payload['cards_in_duplicate_groups']}")
    for cid, paths in duplicates.items():
        print(f"  {cid}: {len(paths)} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
