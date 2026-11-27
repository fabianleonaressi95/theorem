#!/usr/bin/env python3
"""Synchronise docs/UNIFIED_THEOREM_EDGES.json with the live theorems/ inventory.

The JSON graph predates several card additions; this script reconciles it
against the on-disk card set (the same inventory covered by
scripts/build_theorem_register.py). File paths are the stable identifiers:
node ids embed the filename stem, which is unique even where T-prefixes are
duplicated.

Policy for new cards:
  * A theorem-record node is created with id ``THM:<filename-stem>``.
  * Because the original hub assignments were made per-record (not by a
    reproducible keyword rule), new records are indexed under ``H-OTHER``
    with the standard provisional classification caveat. Hub assignment is
    reported for author review; it is NOT inferred.
  * Existing nodes, edges, ids and caveats are preserved verbatim.
  * Stale nodes (path no longer on disk) are reported and removed together
    with their incident edges.

Idempotent: running twice produces no further changes.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDGES_JSON = ROOT / "docs" / "UNIFIED_THEOREM_EDGES.json"
REPO = "fabianleonaressi95/theorem"
OTHER_HUB = "H-OTHER"


def theorem_files() -> dict[str, Path]:
    out = {}
    for path in sorted((ROOT / "theorems").rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        out[rel] = path
    return out


def main() -> int:
    graph = json.loads(EDGES_JSON.read_text(encoding="utf-8"))
    files = theorem_files()

    thm_nodes = [n for n in graph["nodes"] if n.get("kind") == "theorem-record"]
    by_path = {n["path"]: n for n in thm_nodes}

    added, stale = [], []
    for rel in files:
        if rel not in by_path:
            node_id = f"THM:{Path(rel).stem}"
            if any(n["id"] == node_id for n in graph["nodes"]):
                print(f"ERROR id collision for new node {node_id}")
                return 1
            graph["nodes"].append({
                "id": node_id,
                "kind": "theorem-record",
                "repository": REPO,
                "path": rel,
                "topic_hub": OTHER_HUB,
            })
            graph["edges"].append({
                "from": node_id,
                "to": OTHER_HUB,
                "relation": "thematic-index-classification",
                "status": "provisional",
                "caveat": (
                    "Added by post-reorg graph sync (2026-11-27); hub parked "
                    "at H-OTHER pending author topic assignment. Filename-only "
                    "index edge, not a proof dependency."
                ),
            })
            added.append(rel)

    live_paths = set(files)
    for n in list(thm_nodes):
        if n["path"] not in live_paths:
            stale.append(n["path"])
            graph["nodes"].remove(n)
            graph["edges"] = [
                e for e in graph["edges"]
                if e["from"] != n["id"] and e["to"] != n["id"]
            ]

    ids = {n["id"] for n in graph["nodes"]}
    dangling = [e for e in graph["edges"] if e["from"] not in ids or e["to"] not in ids]
    if dangling:
        print(f"ERROR {len(dangling)} dangling edges after sync")
        return 1

    # Coverage block.
    cls = [e for e in graph["edges"] if e["relation"] == "thematic-index-classification"]
    thm_count = sum(1 for n in graph["nodes"] if n.get("kind") == "theorem-record")
    graph["coverage"].update({
        "theorem_markdown_records": thm_count,
        "classification_edges": len(cls),
        "total_nodes": len(graph["nodes"]),
        "total_edges": len(graph["edges"]),
        "note": (
            "Synced 27-November-2026 against the post-reorganisation inventory "
            "(the same card set covered by THEOREM_MASTER_REGISTER). File paths "
            "are stable identifiers; node ids embed unique filename stems, so "
            "duplicated T-prefixes do not collide. Cards added since the "
            "previous snapshot are indexed under H-OTHER with provisional "
            "status pending author topic assignment; no dependency edges were "
            "invented."
        ),
    })

    EDGES_JSON.write_text(
        json.dumps(graph, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    print(f"theorem files on disk : {len(files)}")
    print(f"theorem-record nodes   : {thm_count} (+{len(added)} added)")
    print(f"nodes total            : {len(graph['nodes'])}")
    print(f"edges total            : {len(graph['edges'])}")
    print(f"stale nodes removed    : {len(stale)}")
    for rel in added:
        print(f"  + {rel}")
    for rel in stale:
        print(f"  - {rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
