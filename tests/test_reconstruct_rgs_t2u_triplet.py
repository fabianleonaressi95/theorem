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
