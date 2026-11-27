"""Independent audit invariants for the post-reorg consistency pass.

These tests deliberately re-derive every fact from primary sources
(theorems/ files on disk, JSON/CSV/Markdown artifacts) without importing or
calling scripts/build_unified_theorem_graph.py,
scripts/build_theorem_register.py or scripts/build_duplicate_id_map.py.
They encode the acceptance criteria of the 2026-11-27 independent audit.
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _disk_cards():
    return {
        p.relative_to(ROOT).as_posix()
        for p in (ROOT / "theorems").rglob("*.md")
    }


def _graph():
    return json.loads((ROOT / "docs/UNIFIED_THEOREM_EDGES.json").read_text())


def _register_rows():
    return list(
        csv.DictReader((ROOT / "docs/THEOREM_MASTER_REGISTER.csv").open())
    )


# ---------- graph invariants (independent reconstruction) ----------

def test_graph_theorem_nodes_bijective_with_disk():
    g = _graph()
    thm = [n for n in g["nodes"] if n.get("kind") == "theorem-record"]
    paths = [n["path"] for n in thm]
    assert len(paths) == len(set(paths)), "duplicate theorem node paths"
    assert set(paths) == _disk_cards()


def test_graph_node_ids_unique_and_derived_from_stems():
    g = _graph()
    ids = [n["id"] for n in g["nodes"]]
    assert len(ids) == len(set(ids))
    for n in g["nodes"]:
        if n.get("kind") == "theorem-record":
            assert n["id"] == "THM:" + Path(n["path"]).stem


def test_graph_every_card_has_exactly_one_hub_edge():
    g = _graph()
    hubs = {n["id"] for n in g["nodes"] if n.get("kind") == "thematic-hub"}
    cls = [
        e for e in g["edges"]
        if e.get("relation") == "thematic-index-classification"
    ]
    thm_ids = {n["id"] for n in g["nodes"] if n.get("kind") == "theorem-record"}
    counts = {}
    for e in cls:
        counts[e["from"]] = counts.get(e["from"], 0) + 1
        assert e["to"] in hubs, f"classification edge to non-hub: {e['to']}"
        assert e["status"] == "provisional"
    assert set(counts) == thm_ids
    assert all(c == 1 for c in counts.values())


def test_graph_no_dangling_edges_and_coverage_consistent():
    g = _graph()
    ids = {n["id"] for n in g["nodes"]}
    assert all(e["from"] in ids and e["to"] in ids for e in g["edges"])
    cov = g["coverage"]
    assert cov["total_nodes"] == len(g["nodes"])
    assert cov["total_edges"] == len(g["edges"])
    thm = sum(1 for n in g["nodes"] if n.get("kind") == "theorem-record")
    assert cov["theorem_markdown_records"] == thm == len(_disk_cards())
    cls = sum(
        1 for e in g["edges"]
        if e.get("relation") == "thematic-index-classification"
    )
    assert cov["classification_edges"] == cls


def test_graph_sync_added_nodes_parked_at_other_hub_pending_author():
    """Cards added by graph-sync runs must remain provisional H-OTHER.

    The count grows if main gains new cards between syncs; the invariant is
    that every sync-added classification edge is provisional and parked at
    H-OTHER (never an invented topical assignment).
    """
    g = _graph()
    sync_edges = [
        e for e in g["edges"]
        if e.get("relation") == "thematic-index-classification"
        and "post-reorg graph sync" in e.get("caveat", "")
    ]
    assert len(sync_edges) >= 16
    for e in sync_edges:
        assert e["to"] == "H-OTHER"
        assert e["status"] == "provisional"


def test_graph_markdown_counts_match_json():
    md = (ROOT / "docs/UNIFIED_THEOREM_DEPENDENCY_GRAPH.md").read_text()
    g = _graph()
    assert md.count(
        "This file records **directed, typed edges**"
    ) == 1, "duplicate intro paragraph detected"
    m = re.search(r"(\d+) nodes and (\d+) directed edges", md)
    assert m and (int(m.group(1)), int(m.group(2))) == (
        g["coverage"]["total_nodes"], g["coverage"]["total_edges"],
    )
    m2 = re.search(r"all (\d+) Markdown theorem records", md)
    assert m2 and int(m2.group(1)) == g["coverage"]["theorem_markdown_records"]


# ---------- register invariants (independent reconstruction) ----------

def test_register_bijective_and_taxonomy():
    rows = _register_rows()
    files = {r["file"] for r in rows}
    assert files == _disk_cards()
    allowed = {
        "PROVED", "EXACT_CERTIFICATE", "NUMERICALLY_VERIFIED", "CONDITIONAL",
        "CANDIDATE", "HYPOTHESIS", "OPEN", "SUPERSEDED", "QUARANTINED",
    }
    assert all(r["status"] in allowed for r in rows)


def test_register_proved_requires_explicit_claim_note():
    """No heuristic classification may surface as PROVED."""
    for r in _register_rows():
        if r["status"] == "PROVED":
            note = r["status_note"].lower()
            assert "explicit proof claim" in note, (
                f"PROVED without explicit-claim note: {r['file']}"
            )
            assert "heuristic" not in note and "no status" not in note


def test_register_markdown_header_has_signoff_caveat():
    md = (ROOT / "docs/THEOREM_MASTER_REGISTER.md").read_text()
    assert "author" in md.lower() and "sign-off" in md
    # generated counts agree with CSV
    m = re.search(r"\((\d+) cards\)", md)
    assert m and int(m.group(1)) == len(_register_rows())


# ---------- duplicate-ID map invariants ----------

def test_duplicate_map_independent_reconciliation():
    payload = json.loads(
        (ROOT / "docs/project/DUPLICATE_CARD_ID_MAP.json").read_text()
    )
    # independent prefix extraction: filename stem up to first '-'/ '_'
    # is NOT reliable; instead verify every listed path exists and groups
    # are exactly the files sharing the same register 'id' column.
    reg_ids = {}
    for r in _register_rows():
        reg_ids.setdefault(r["id"], []).append(r["file"])
    expected = {
        cid: sorted(paths)
        for cid, paths in reg_ids.items()
        if len(paths) > 1
    }
    assert payload["duplicates"] == expected
    for paths in payload["duplicates"].values():
        for p in paths:
            assert (ROOT / p).is_file()


# ---------- NPZ manifest invariants ----------

def test_npz_manifest_hash_groups_reverified():
    import hashlib

    manifest = json.loads(
        (ROOT / "docs/NPZ_PROVENANCE_MANIFEST.json").read_text()
    )
    for group in manifest["groups"]:
        assert group["count"] == len(group["files"]) > 1
        digests = set()
        for f in group["files"]:
            p = ROOT / f["path"]
            assert p.is_file()
            digests.add(hashlib.md5(p.read_bytes()).hexdigest())
        # all members share the group md5 and it matches disk
        for f in group["files"]:
            p = ROOT / f["path"]
            assert hashlib.md5(p.read_bytes()).hexdigest() == group["md5"]
            assert f["md5"] == group["md5"]
        assert len(digests) == 1
