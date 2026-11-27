#!/usr/bin/env python3
"""Build docs/NPZ_PROVENANCE_MANIFEST.json.

Groups every .npz/.npy artifact in the repository by MD5 hash and records
filename, hash, size, array names, shapes and dtypes (plus .npz-internal
metadata keys when present). Identical hashes are classified as
``alias-candidate`` (same bytes, different names — possibly repeated exports
or mislabeled artifacts). Nothing is deleted, renamed or modified; unresolved
provenance is marked explicitly for author review.
"""
from __future__ import annotations


import hashlib
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "NPZ_PROVENANCE_MANIFEST.json"
SCAN_DIRS = ["artifacts", "data", "audits", "archive", "results", "output"]
SKIP_DIRS = {".git", "__pycache__", "node_modules"}


def md5(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def describe(path: Path) -> dict:
    entry = {
        "path": path.relative_to(ROOT).as_posix(),
        "size_bytes": path.stat().st_size,
        "md5": md5(path),
    }
    try:
        if path.suffix == ".npz":
            with np.load(path, allow_pickle=False) as z:
                entry["arrays"] = {
                    k: {"shape": list(z[k].shape), "dtype": str(z[k].dtype)}
                    for k in z.files
                }
                entry["npz_metadata_keys"] = sorted(z.files)
        elif path.suffix == ".npy":
            arr = np.load(path, allow_pickle=False)
            entry["arrays"] = {path.name: {"shape": list(arr.shape), "dtype": str(arr.dtype)}}
    except Exception as exc:  # corrupt or pickle-guarded file: record, don't fail
        entry["load_error"] = f"{type(exc).__name__}: {exc}"
    return entry


def main() -> int:
    files: list[Path] = []
    for top in SCAN_DIRS:
        base = ROOT / top
        if not base.is_dir():
            continue
        for path in base.rglob("*"):
            if path.suffix in {".npz", ".npy"} and not any(
                part in SKIP_DIRS for part in path.parts
            ):
                files.append(path)

    by_hash: dict[str, list[dict]] = {}
    for path in sorted(files):
        by_hash.setdefault(md5(path), []).append(describe(path))

    duplicate_groups = [
        {"md5": h, "count": len(entries), "files": entries}
        for h, entries in sorted(by_hash.items())
        if len(entries) > 1
    ]
    payload = {
        "schema": "npz-provenance-manifest/v1",
        "generated": "2026-11-27",
        "scan_dirs": SCAN_DIRS,
        "total_files": len(files),
        "unique_hashes": len(by_hash),
        "duplicate_groups": len(duplicate_groups),
        "classification": (
            "alias-candidate: byte-identical files under different names. "
            "May be repeated exports, aliases or mislabeled artifacts; "
            "provenance unresolved pending author review. No file was "
            "deleted, renamed or modified."
        ),
        "groups": duplicate_groups,
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"scanned={len(files)} unique_md5={len(by_hash)} dup_groups={len(duplicate_groups)}")
    for g in duplicate_groups:
        names = ", ".join(f["path"] for f in g["files"])
        print(f"  md5={g['md5'][:12]} x{g['count']}: {names}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
