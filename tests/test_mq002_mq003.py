import numpy as np

from scripts.audit_mq002_mq003 import (
    GENERATORS,
    glue_one_fundamental_leg,
    intertwiner_basis,
    run_audit,
    total_generator,
)


def test_four_valent_intertwiner_basis_is_orthonormal_and_invariant():
    basis = intertwiner_basis()
    assert basis.shape == (16, 2)
    assert np.linalg.norm(basis.conj().T @ basis - np.eye(2)) < 1e-12
    for generator in GENERATORS:
        assert np.linalg.norm(total_generator(generator, 4) @ basis) < 1e-12


def test_two_node_gluing_preserves_global_su2_invariance():
    basis = intertwiner_basis()
    for a in range(2):
        for b in range(2):
            glued = glue_one_fundamental_leg(basis[:, a], basis[:, b])
            assert abs(np.linalg.norm(glued) - 0.5) < 1e-12
            for generator in GENERATORS:
                assert np.linalg.norm(total_generator(generator, 6) @ glued) < 1e-12


def test_complete_audit_passes():
    result = run_audit()
    assert result["intertwiner_dimension"] == 2
    assert result["max_numerical_residual"] < 1e-12
    assert result["two_node_gluing"]["area_matching"] is True
    assert result["two_node_gluing"]["shape_matching_imposed"] is False
