import numpy as np

from scripts.audit_vesica_anisotropic_dtn import (
    coefficient_matrices,
    direct_energy,
    geometric_matrices,
    hamiltonian_matrix,
    reduced_energy,
    transfer_dtn,
)


def test_geometric_matrix_symmetries():
    C, G, B, D, _ = geometric_matrices(0.137, 4)
    assert np.linalg.norm(C + C.T) < 1e-11
    assert np.linalg.norm(B + B.T) < 1e-11
    assert np.linalg.norm(G - G.T) < 1e-11
    assert np.linalg.norm(D - D.T) > 1e-6


def test_reduced_energy_matches_original_two_dimensional_integral():
    rng = np.random.default_rng(271828)
    for modes in (1, 2, 4):
        f = rng.normal(size=modes)
        fp = rng.normal(size=modes)
        q2d = direct_energy(0.137, f, fp, modes)
        qred = reduced_energy(0.137, f, fp, modes)
        assert abs(q2d - qred) < 2e-10 * max(1.0, abs(q2d))


def test_hamiltonian_generator_is_hamiltonian():
    modes = 3
    F = hamiltonian_matrix(0.137, modes, lam=0.0)
    J = np.block(
        [
            [np.zeros((modes, modes)), np.eye(modes)],
            [-np.eye(modes), np.zeros((modes, modes))],
        ]
    )
    assert np.linalg.norm(F.T @ J + J @ F, ord=2) < 1e-10


def test_transfer_and_dtn_for_low_mode_truncation():
    M, dtn, symplectic, symmetry, _ = transfer_dtn(2)
    assert np.linalg.norm(M.T @ np.block(
        [[np.zeros((2, 2)), np.eye(2)], [-np.eye(2), np.zeros((2, 2))]]
    ) @ M - np.block(
        [[np.zeros((2, 2)), np.eye(2)], [-np.eye(2), np.zeros((2, 2))]]
    ), ord=2) < 1e-6
    assert symplectic < 1e-6
    assert symmetry < 1e-7
    assert np.linalg.norm(dtn - dtn.T, ord=2) < 1e-7
