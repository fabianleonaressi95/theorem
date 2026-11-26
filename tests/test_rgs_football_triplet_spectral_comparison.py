import sys
from pathlib import Path

import numpy as np
from scipy.linalg import null_space

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from models.football_shell import build_football_shell
from models.football_quaternion_bridge import (
    build_geometry_transfer,
    project_shell_tangent,
)


def _source_geometry():
    data = np.genfromtxt(
        ROOT / "data/rgs_188d/X_Oh_reconstructed.csv",
        delimiter=",",
        names=True,
    )
    points = np.column_stack([data[key] for key in ("x", "y", "z")])
    constraints = np.zeros((4, 192))
    constraints[0, 0::3] = 1
    constraints[1, 1::3] = 1
    constraints[2, 2::3] = 1
    constraints[3] = points.reshape(-1)
    tangent_basis = null_space(constraints)
    generators = np.column_stack(
        [
            np.cross(np.broadcast_to(axis, points.shape), points).reshape(-1)
            for axis in np.eye(3)
        ]
    )
    return points, constraints, tangent_basis, generators


def test_rgs_rotation_triplet_lies_in_exact_tangent_space():
    points, constraints, tangent_basis, generators = _source_geometry()
    assert tangent_basis.shape == (192, 188)
    assert np.linalg.norm(constraints @ generators) < 1e-10
    assert np.linalg.matrix_rank(tangent_basis.T @ generators) == 3


def test_transferred_rotation_triplet_has_rank_three():
    points, _, tangent_basis, generators = _source_geometry()
    mesh = build_football_shell()
    transfer, _ = build_geometry_transfer(points, mesh["nodes"], neighbors=16)
    source_triplet = tangent_basis @ np.linalg.svd(
        tangent_basis.T @ generators, full_matrices=False
    )[0][:, :3]
    mapped = project_shell_tangent(mesh, transfer @ source_triplet)
    assert np.linalg.matrix_rank(mapped, tol=1e-9) == 3


def test_direction_grouped_transfer_has_stable_full_rank_triplet():
    points, _, tangent_basis, generators = _source_geometry()
    mesh = build_football_shell()
    source_triplet = tangent_basis @ np.linalg.svd(
        tangent_basis.T @ generators, full_matrices=False
    )[0][:, :3]

    for neighbors in (8, 12, 16, 24, 32):
        transfer, diagnostics = build_geometry_transfer(
            points, mesh["nodes"], neighbors=neighbors
        )
        assert diagnostics["distinct_source_direction_count"] == 56
        assert diagnostics["duplicate_direction_group_count"] == 8
        assert diagnostics["duplicate_direction_group_sizes"] == [2] * 8
        assert diagnostics["source_direction_min_separation_unique"] > 0
        assert diagnostics["affine_direction_reproduction_frobenius"] < 1e-8
        mapped = project_shell_tangent(mesh, transfer @ source_triplet)
        assert np.linalg.matrix_rank(mapped, tol=1e-9) == 3


def test_quaternion_double_cover_and_rotation_action():
    from models.football_quaternion_tangent import quaternion_from_matrix, qrotate

    angle = 0.41
    rotation = np.array(
        [
            [np.cos(angle), -np.sin(angle), 0],
            [np.sin(angle), np.cos(angle), 0],
            [0, 0, 1.0],
        ]
    )
    quaternion = quaternion_from_matrix(rotation)
    vector = np.array([0.2, -0.5, 0.7])
    assert np.linalg.norm(qrotate(quaternion, vector) - rotation @ vector) < 1e-12
    assert np.linalg.norm(qrotate(quaternion, vector) - qrotate(-quaternion, vector)) < 1e-12


def test_full_transfer_robustness_grid_executes(tmp_path):
    import json
    import subprocess

    output = tmp_path / "robustness.json"
    script = ROOT / "scripts/audit_rgs_football_transfer_robustness.py"
    subprocess.run(
        [sys.executable, str(script), "--out", str(output)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    report = json.loads(output.read_text())
    assert report["status"] == "COMPUTED_TRANSFER_ROBUSTNESS_AUDIT"
    assert [row["neighbors"] for row in report["robustness_grid"]] == [8, 12, 16, 24, 32]
    assert all(row["transferred_triplet_rank"] == 3 for row in report["robustness_grid"])
    assert report["source"]["tangent_basis_shape"] == [192, 188]
    quaternion_audit = report["quaternionic_audit"]
    assert quaternion_audit["rotation_action_max_residual"] < 1e-10
    assert quaternion_audit["double_cover_q_vs_minus_q_max_residual"] < 1e-10
    assert quaternion_audit["composition_max_residual"] < 1e-10
    assert output.with_suffix(".npz").exists()
