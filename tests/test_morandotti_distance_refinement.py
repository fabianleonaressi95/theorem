from pathlib import Path
import sys
import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from models.morandotti_distance_refinement import summarize_distance_refinement


def _matrix(scale=1.0, coupling=0.2):
    matrix = np.eye(6) * (2.0 * scale)
    cross = np.array([[coupling, 0.03], [-0.01, 0.5 * coupling]])
    matrix[1:3, 4:6] = cross
    matrix[4:6, 1:3] = cross.T
    return matrix


def test_refinement_summary_tracks_each_distance_and_mesh_level():
    records = []
    for h, scale in ((0.08, 1.0), (0.06, 1.1), (0.045, 1.15)):
        for distance, coupling in ((0.48, 0.3), (0.56, 0.2), (0.64, 0.1)):
            records.append({"h": h, "distance": distance, "M_laplacian": _matrix(scale, coupling)})
    report = summarize_distance_refinement(records)
    assert report["mesh_sizes_coarse_to_fine"] == [0.08, 0.06, 0.045]
    assert report["distances"] == [0.48, 0.56, 0.64]
    assert len(report["results"]) == 9
    assert len(report["matrix_refinement_comparisons"]) == 6
    values = [row["normalized_coupling_C_d"] for row in report["results"]]
    assert max(values) > min(values)
    assert all(row["matrix_symmetry_relative"] < 1e-14 for row in report["results"])


def test_rejects_incomplete_mesh_distance_grid():
    with pytest.raises(ValueError, match="exactly one result"):
        summarize_distance_refinement([
            {"h": 0.08, "distance": 0.48, "M_laplacian": _matrix()},
            {"h": 0.06, "distance": 0.48, "M_laplacian": _matrix()},
            {"h": 0.08, "distance": 0.56, "M_laplacian": _matrix()},
        ])


def test_rejects_nonsymmetric_interaction_matrix():
    matrix = _matrix()
    matrix[0, 1] += 0.1
    with pytest.raises(ValueError, match="not symmetric"):
        summarize_distance_refinement([
            {"h": 0.08, "distance": 0.48, "M_laplacian": matrix},
        ])
