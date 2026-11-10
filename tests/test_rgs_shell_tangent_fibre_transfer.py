import numpy as np
from pathlib import Path

from models.football_shell import build_football_shell
from models.tangent_triplet_anisotropy import (
    build_rgs_shell_tangent_fibre_maps,
    push_triplett_to_shell_nodes,
)


def test_construct_actual_92_node_rank_two_fibre_transfer():
    root = Path(__file__).resolve().parents[1]
    data = np.genfromtxt(root / "data/rgs_188d/X_Oh_reconstructed.csv",
                         delimiter=",", names=True)
    X = np.column_stack([data[k] for k in ("x", "y", "z")])
    mesh = build_football_shell()
    result = build_rgs_shell_tangent_fibre_maps(X, mesh, neighbors=16)

    assert result["ambient_maps"].shape == (92, 3, 188)
    assert result["local_maps"].shape == (92, 2, 188)
    assert result["minimum_nodewise_rank"] == 2
    assert result["maximum_tangency_residual"] < 1e-9
    assert result["source_constraint_residual"] < 1e-9
    assert result["source_basis_orthogonality"] < 1e-9
    assert result["transfer_diagnostics"]["distinct_source_direction_count"] == 56
    assert result["transfer_diagnostics"]["duplicate_direction_group_count"] == 8


def test_triplett_pushforward_is_psd_and_tangent_at_every_shell_node():
    root = Path(__file__).resolve().parents[1]
    data = np.genfromtxt(root / "data/rgs_188d/X_Oh_reconstructed.csv",
                         delimiter=",", names=True)
    X = np.column_stack([data[k] for k in ("x", "y", "z")])
    mesh = build_football_shell()
    maps = build_rgs_shell_tangent_fibre_maps(X, mesh, neighbors=16)
    triplett = np.array([[1.0, 0.0, 1.0], [0.0, 1.0, 1.0]])
    tensors = push_triplett_to_shell_nodes(triplett, maps)

    assert tensors.shape == (92, 3, 3)
    for A, n in zip(tensors, maps["shell_normals"]):
        assert np.allclose(A, A.T, atol=1e-10)
        assert np.linalg.eigvalsh(A)[0] >= -1e-9
        assert np.linalg.norm(A @ n) < 1e-8


def test_local_fibre_matrix_changes_by_gauge_conjugation_only():
    root = Path(__file__).resolve().parents[1]
    data = np.genfromtxt(root / "data/rgs_188d/X_Oh_reconstructed.csv",
                         delimiter=",", names=True)
    X = np.column_stack([data[k] for k in ("x", "y", "z")])
    mesh = build_football_shell()
    maps = build_rgs_shell_tangent_fibre_maps(X, mesh, neighbors=16)
    triplett = np.array([[1.0, 0.0, 1.0], [0.0, 1.0, 1.0]])
    Gamma = np.array([[2.0, -3.0], [-3.0, 6.0]])
    R = triplett.T @ Gamma @ triplett
    i = 17
    Llocal = maps["local_maps"][i]
    A = Llocal @ R @ Llocal.T

    theta = 0.413
    O = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    Lchanged = O.T @ Llocal
    Achanged = Lchanged @ R @ Lchanged.T
    assert np.allclose(Achanged, O.T @ A @ O, atol=1e-10)
    assert np.allclose(np.linalg.eigvalsh(Achanged),
                       np.linalg.eigvalsh(A), atol=1e-10)
