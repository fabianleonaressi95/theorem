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


def test_t134_young_coercivity_constant_unweighted_and_weighted_norms():
    """Regression for the explicit Young step and norm-dependent constant."""
    rng = np.random.default_rng(134)
    c_tr = 3.7
    alpha = 10.0
    eta = 1.0 / (2.0 * c_tr)

    # Synthetic nonnegative seminorm values satisfying H^2 <= C_tr D^2.
    D = rng.uniform(0.1, 4.0, size=100_000)
    J = rng.uniform(0.1, 4.0, size=100_000)
    H = np.sqrt(c_tr) * D * rng.uniform(0.0, 1.0, size=100_000)

    young_rhs = eta * c_tr * D**2 + (1.0 / eta) * J**2
    assert np.all(2.0 * H * J <= young_rhs + 1e-12)
    assert np.all(eta * c_tr * D**2 <= 0.5 * D**2 + 1e-12)
    assert np.all(young_rhs <= 0.5 * D**2 + 2.0 * c_tr * J**2 + 1e-12)

    penalty_margin = alpha - 2.0 * c_tr
    assert penalty_margin > 0.0
    lower_bound = 0.5 * D**2 + penalty_margin * J**2
    assert np.all(D**2 - 2.0 * H * J + alpha * J**2 >= lower_bound - 1e-12)

    # For ||v||_w^2 = w_D D^2 + w_J J^2, both coefficient ratios matter.
    w_D, w_J = 2.0, 5.0
    c_weighted = min(0.5 / w_D, penalty_margin / w_J)
    assert np.isclose(c_weighted, 0.1)
    assert np.all(lower_bound >= c_weighted * (w_D * D**2 + w_J * J**2) - 1e-12)


def test_t134_rejects_noncoercive_penalty_threshold():
    c_tr = 3.7
    alpha = 2.0 * c_tr
    assert alpha - 2.0 * c_tr == 0.0
    assert min(0.5, alpha - 2.0 * c_tr) == 0.0
