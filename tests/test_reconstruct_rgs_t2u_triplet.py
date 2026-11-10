from pathlib import Path
import numpy as np

from models.tangent_triplet_anisotropy import reconstruct_rgs_t2u_triplet


def test_reconstruct_original_oh_t2u_first_triplet():
    root = Path(__file__).resolve().parents[1]
    data = np.genfromtxt(root / "data/rgs_188d/X_Oh_reconstructed.csv",
                         delimiter=",", names=True)
    X = np.column_stack([data[k] for k in ("x", "y", "z")])
    result = reconstruct_rgs_t2u_triplet(X)
    V = result["basis"]
    report = result["diagnostics"]

    assert V.shape == (188, 3)
    assert np.linalg.norm(V.T @ V - np.eye(3)) < 1e-10
    assert report["t2u_isotypic_rank"] == 30
    assert report["triplet_rank"] == 3
    assert np.max(np.abs(np.asarray(report["triplet_eigenvalues"])
                         - (-0.06994933008401777))) < 1e-10
    assert report["gap_to_next_t2u_eigenvalue"] > 0.3
    assert report["projector_idempotence_residual"] < 1e-9
    assert report["K_T2u_commutator_residual"] < 1e-9
    assert report["triplet_eigen_residual"] < 1e-9
    assert report["tangent_constraint_residual"] < 1e-9


def test_reconstructed_t2u_channels_land_in_all_92_shell_tangent_fibres():
    from models.football_shell import build_football_shell
    from models.tangent_triplet_anisotropy import (
        build_rgs_shell_tangent_fibre_maps,
        push_triplett_to_shell_nodes,
    )

    root = Path(__file__).resolve().parents[1]
    data = np.genfromtxt(root / "data/rgs_188d/X_Oh_reconstructed.csv",
                         delimiter=",", names=True)
    X = np.column_stack([data[k] for k in ("x", "y", "z")])
    V = reconstruct_rgs_t2u_triplet(X)["basis"]
    maps = build_rgs_shell_tangent_fibre_maps(X, build_football_shell(), neighbors=16)

    # Algebraic representative used to test the push-forward; this is not
    # asserted to be one of the archived 216 physical PRISM tripletti.
    triplett = np.array([[1.0, 0.0, 1.0], [0.0, 1.0, 1.0]])
    pushed = push_triplett_to_shell_nodes(triplett, maps, V)

    assert pushed["channel_maps"].shape == (92, 3, 3)
    assert pushed["tangent_tensors"].shape == (92, 3, 3)
    for U, A, n in zip(pushed["channel_maps"], pushed["tangent_tensors"],
                       maps["shell_normals"]):
        assert np.linalg.matrix_rank(U, tol=1e-9) == 2
        assert np.linalg.norm(U.T @ n) < 1e-8
        assert np.allclose(A, A.T, atol=1e-10)
        assert np.linalg.eigvalsh(A)[0] >= -1e-9
        assert np.linalg.norm(A @ n) < 1e-8
