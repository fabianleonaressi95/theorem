from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.rgs_morandotti_independent_remeshing import validate_realization_grid


def _records():
    rows = []
    for h in (0.08, 0.06, 0.045):
        for distance in (0.48, 0.56):
            for seed in (11, 29, 47):
                rows.append({
                    "h_target": h,
                    "distance": distance,
                    "mesh_seed": seed,
                    "fresh_mesh_fingerprint_sha256": f"{h}-{distance}-{seed}",
                    "fresh_mesh_generated_for_this_pair": True,
                })
    return rows


def test_accepts_exact_18_realizations_with_distinct_meshes():
    groups = validate_realization_grid(
        _records(), (0.08, 0.06, 0.045), (0.48, 0.56), (11, 29, 47)
    )
    assert len(groups) == 6
    assert all(len(samples) == 3 for samples in groups.values())


def test_rejects_duplicate_mesh_fingerprints_across_seeds():
    rows = _records()
    rows[1]["fresh_mesh_fingerprint_sha256"] = rows[0]["fresh_mesh_fingerprint_sha256"]
    with pytest.raises(RuntimeError, match="duplicate mesh fingerprints"):
        validate_realization_grid(rows, (0.08, 0.06, 0.045), (0.48, 0.56), (11, 29, 47))


def test_rejects_missing_or_duplicated_seed_record():
    rows = _records()
    rows.pop()
    with pytest.raises(RuntimeError, match="realization grid mismatch"):
        validate_realization_grid(rows, (0.08, 0.06, 0.045), (0.48, 0.56), (11, 29, 47))
