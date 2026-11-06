import numpy as np
from scripts.q6_qlg_dirac_lorentz_chirality import (
    audit, boost_generators, chirality_embedding, gamma5,
    parity_operator, rotation_generators,
)


def test_gamma5_is_hermitian_involution_and_projectors():
    g5=gamma5()
    assert np.linalg.norm(g5@g5-np.eye(4)) < 1e-12
    assert np.linalg.norm(g5-g5.conj().T) < 1e-12
    for s in (-1,1):
        k=chirality_embedding(s)
        assert np.linalg.norm(k@k.conj().T-(np.eye(4)+s*g5)/2) < 1e-12


def test_chiral_embeddings_intertwine_rotations_and_boosts():
    for s in (-1,1):
        k=chirality_embedding(s)
        for j,p in zip(rotation_generators(),(
            np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),
            np.array([[1,0],[0,-1]]))):
            assert np.linalg.norm(j@k-k@p/2) < 1e-12
        for b,p in zip(boost_generators(),(
            np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),
            np.array([[1,0],[0,-1]]))):
            assert np.linalg.norm(b@k-k@(-s*p/2)) < 1e-12


def test_parity_exchanges_chiral_sectors():
    p=parity_operator()
    for s in (-1,1):
        assert np.linalg.norm(p@chirality_embedding(s)-1j*chirality_embedding(-s)) < 1e-12


def test_audit_passes():
    result=audit()
    assert result["passed"]
    assert result["parity_action"].startswith("exchanges")
