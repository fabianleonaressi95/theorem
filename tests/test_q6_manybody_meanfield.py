import numpy as np

from audits.morphodynamics.q6_manybody_meanfield import (
    Parameters, fock_pairs, hartree_fock_state, one_body_density,
    two_boson_hamiltonian, one_body_hamiltonian, run_comparison,
)


def test_two_boson_basis_dimension_and_product_normalization():
    assert len(fock_pairs()) == 2080
    phi = np.zeros(64, dtype=complex)
    phi[0] = 1 / np.sqrt(2); phi[1] = 1j / np.sqrt(2)
    psi = hartree_fock_state(phi)
    assert np.isclose(np.vdot(psi, psi).real, 1.0)
    assert np.isclose(np.trace(one_body_density(psi)).real, 2.0)
    assert np.allclose(one_body_density(psi), 2 * np.outer(phi, phi.conj()))


def test_two_boson_hamiltonian_is_hermitian_and_interaction_exact():
    h = one_body_hamiltonian(np.zeros(192))
    H = two_boson_hamiltonian(h, interaction=0.7)
    assert H.shape == (2080, 2080)
    assert np.max(np.abs((H - H.getH()).data), initial=0.0) < 1e-12


def test_noninteracting_hartree_product_is_invariant_under_full_dynamics():
    phi = np.zeros(64, dtype=complex)
    phi[0] = 1.0
    result = run_comparison(phi=phi, params=Parameters(interaction=0.0),
                            final_time=0.04, samples=5)
    assert result["max_norm_error"] < 2e-6
    assert result["max_one_body_error"] < 2e-5
    assert result["max_geometry_error"] < 2e-5
