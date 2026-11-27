"""Consistency guarantees introduced by the post-reorg pass (2026-11-27).

These tests are deliberately lightweight: they check inventory coverage and
referential integrity of the machine-readable registries, not scientific
content.
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _theorem_files():
    return {
        p.relative_to(ROOT).as_posix()
        for p in (ROOT / "theorems").rglob("*.md")
    }


def test_every_card_in_master_register():
    rows = list(csv.DictReader((ROOT / "docs/THEOREM_MASTER_REGISTER.csv").open()))
    registered = {r["file"] for r in rows}
    missing = _theorem_files() - registered
    assert not missing, f"cards missing from register: {sorted(missing)}"


def test_register_taxonomy_only():
    allowed = {
        "PROVED", "EXACT_CERTIFICATE", "NUMERICALLY_VERIFIED", "CONDITIONAL",
        "CANDIDATE", "HYPOTHESIS", "OPEN", "SUPERSEDED", "QUARANTINED",
    }
    rows = list(csv.DictReader((ROOT / "docs/THEOREM_MASTER_REGISTER.csv").open()))
    bad = [r["file"] for r in rows if r["status"] not in allowed]
    assert not bad, f"statuses outside taxonomy: {bad}"


def test_no_duplicate_register_file_keys():
    rows = list(csv.DictReader((ROOT / "docs/THEOREM_MASTER_REGISTER.csv").open()))
    files = [r["file"] for r in rows]
    assert len(files) == len(set(files))


def test_graph_covers_every_card_by_path():
    graph = json.loads((ROOT / "docs/UNIFIED_THEOREM_EDGES.json").read_text())
    node_paths = {
        n["path"] for n in graph["nodes"] if n.get("kind") == "theorem-record"
    }
    missing = _theorem_files() - node_paths
    assert not missing, f"cards missing from dependency graph: {sorted(missing)}"


def test_graph_node_ids_unique_and_edges_resolve():
    graph = json.loads((ROOT / "docs/UNIFIED_THEOREM_EDGES.json").read_text())
    ids = [n["id"] for n in graph["nodes"]]
    assert len(ids) == len(set(ids)), "duplicate node ids in graph"
    id_set = set(ids)
    dangling = [
        e for e in graph["edges"]
        if e["from"] not in id_set or e["to"] not in id_set
    ]
    assert not dangling, f"dangling edges: {dangling[:5]}"


def test_graph_counts_match_coverage_block():
    graph = json.loads((ROOT / "docs/UNIFIED_THEOREM_EDGES.json").read_text())
    cov = graph["coverage"]
    thm = sum(1 for n in graph["nodes"] if n.get("kind") == "theorem-record")
    assert cov["theorem_markdown_records"] == thm == len(_theorem_files())
    assert cov["total_nodes"] == len(graph["nodes"])
    assert cov["total_edges"] == len(graph["edges"])


def test_duplicate_id_map_covers_all_duplicates():
    import sys
    sys.path.insert(0, str(ROOT / "scripts"))
    from build_theorem_register import card_id

    groups = {}
    for p in (ROOT / "theorems").rglob("*.md"):
        groups.setdefault(card_id(p), []).append(
            p.relative_to(ROOT).as_posix()
        )
    expected = {
        cid: sorted(paths) for cid, paths in groups.items() if len(paths) > 1
    }
    payload = json.loads(
        (ROOT / "docs/project/DUPLICATE_CARD_ID_MAP.json").read_text()
    )
    assert payload["duplicates"] == expected


def test_npz_manifest_groups_match_filesystem():
    manifest = json.loads(
        (ROOT / "docs/NPZ_PROVENANCE_MANIFEST.json").read_text()
    )
    listed = {
        f["path"]
        for g in manifest["groups"]
        for f in g["files"]
    }
    # every listed duplicate-group member must still exist on disk
    for rel in listed:
        assert (ROOT / rel).is_file(), f"manifest lists missing file {rel}"
    # no group may contain a single file
    assert all(g["count"] > 1 for g in manifest["groups"])
