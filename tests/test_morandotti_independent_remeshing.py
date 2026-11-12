from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.rgs_morandotti_independent_remeshing import validate_realization_grid


MESH_SIZES = (0.08, 0.06, 0.045, 0.035)
DISTANCES = (0.48, 0.56)
SEEDS = (11, 17, 23, 29, 37, 47, 59)


def _records():
    rows = []
    for h in MESH_SIZES:
        for distance in DISTANCES:
            for seed in SEEDS:
                rows.append({
                    "h_target": h,
                    "distance": distance,
                    "mesh_seed": seed,
                    "fresh_mesh_fingerprint_sha256": f"{h}-{distance}-{seed}",
                    "fresh_mesh_generated_for_this_pair": True,
                })
    return rows


def test_accepts_exact_56_realizations_with_distinct_meshes():
    groups = validate_realization_grid(_records(), MESH_SIZES, DISTANCES, SEEDS)
    assert len(groups) == len(MESH_SIZES) * len(DISTANCES)
    assert all(len(samples) == len(SEEDS) for samples in groups.values())


def test_rejects_duplicate_mesh_fingerprints_across_seeds():
    rows = _records()
    rows[1]["fresh_mesh_fingerprint_sha256"] = rows[0]["fresh_mesh_fingerprint_sha256"]
    with pytest.raises(RuntimeError, match="duplicate mesh fingerprints"):
        validate_realization_grid(rows, MESH_SIZES, DISTANCES, SEEDS)


def test_rejects_missing_or_duplicated_seed_record():
    rows = _records()
    rows.pop()
    with pytest.raises(RuntimeError, match="realization grid mismatch"):
        validate_realization_grid(rows, MESH_SIZES, DISTANCES, SEEDS)


def test_rejects_single_seed_because_sample_std_is_undefined():
    with pytest.raises(ValueError):
        # CLI validation is intentionally tested via the grid contract's
        # minimum sample-size invariant in the companion validation test.
        validate_realization_grid(_records(), MESH_SIZES, DISTANCES, (SEEDS[0],))
