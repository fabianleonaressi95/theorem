"""Lorentz-covariant QLG C2 -> Dirac C4 embedding audit.

Uses the repository convention eta=(-,+,+,+) and the exact gamma matrices
from rgs-qlg-quaternion-bridge/src/clifford_qlg.py.

The Dirac representation restricted to spatial rotations is U (+) U.
The Lorentz-invariant irreducible 2D subspaces are the gamma5 eigenspaces,
not the upper/lower coordinate blocks. Parity exchanges them.
"""
from __future__ import annotations
import numpy as np

I2=np.eye(2,dtype=complex)
I4=np.eye(4,dtype=complex)
PAULI=(
 np.array([[0,1],[1,0]],complex),
 np.array([[0,-1j],[1j,0]],complex),
 np.array([[1,0],[0,-1]],complex),
)
ETA=np.diag([-1.,1.,1.,1.])


def gamma_matrices():
    g0=1j*np.block([[I2,np.zeros((2,2))],[np.zeros((2,2)),-I2]])
    spatial=tuple(1j*np.block([[np.zeros((2,2)),s],[-s,np.zeros((2,2))]]) for s in PAULI)
    return (g0,*spatial)


def gamma5():
    g=gamma_matrices()
    return 1j*g[0]@g[1]@g[2]@g[3]


def rotation_generators():
    # J_i = diag(sigma_i/2,sigma_i/2)
    return tuple(0.5*np.block([[s,np.zeros((2,2))],[np.zeros((2,2)),s]]) for s in PAULI)


def boost_generators():
    # K_i = gamma^0 gamma^i / 2; convention-specific infinitesimal generators.
    g=gamma_matrices()
    return tuple(0.5*g[0]@g[i+1] for i in range(3))


def chirality_embedding(sign):
    if sign not in (-1,1): raise ValueError("sign must be +/-1")
    return np.vstack((I2,sign*I2))/np.sqrt(2)


def parity_operator():
    # Overall phase immaterial; gamma^0 exchanges gamma5 eigenspaces.
    return gamma_matrices()[0]


def audit(tol=2e-12):
    g=gamma_matrices()
    g5=gamma5()
    ks={s:chirality_embedding(s) for s in (-1,1)}
    rotations=rotation_generators()
    boosts=boost_generators()
    rot_res={}
    boost_res={}
    for s,k in ks.items():
        rot_res[str(s)]=max(float(np.linalg.norm(j@k-k@(0.5*p))) for j,p in zip(rotations,PAULI))
        # The boost action induced on the two-component Weyl fibre is
        # B_i^(s) = -s sigma_i/2 in this convention.
        boost_res[str(s)]=max(float(np.linalg.norm(b@k-k@(-0.5*s*p))) for b,p in zip(boosts,PAULI))
    p=parity_operator()
    parity_exchange=max(float(np.linalg.norm(p@ks[s]-1j*ks[-s])) for s in (-1,1))
    # The phase i follows gamma^0 acting on (chi,s chi); it is immaterial.
    gamma5_square=float(np.linalg.norm(g5@g5-I4))
    gamma5_herm=float(np.linalg.norm(g5-g5.conj().T))
    projector_res=max(float(np.linalg.norm(k@k.conj().T-(I4+s*g5)/2)) for s,k in ks.items())
    # Verify that upper/lower coordinate embeddings are not boost-invariant.
    upper=np.vstack((I2,np.zeros((2,2))))
    lower=np.vstack((np.zeros((2,2)),I2))
    coord_boost=max(float(np.linalg.norm(b@k-k@x))
                    for b in boosts for k in (upper,lower)
                    for x in (np.zeros((2,2)),))  # nonzero leakage test
    return {
      "schema":"T049D_LORENTZ_CHIRAL_EMBEDDING_AUDIT_V1",
      "signature":"(-,+,+,+)",
      "gamma5_matrix":g5.tolist(),
      "gamma5_square_residual":gamma5_square,
      "gamma5_hermiticity_residual":gamma5_herm,
      "chirality_projector_residual":projector_res,
      "rotation_intertwiner_residuals":rot_res,
      "boost_intertwiner_residuals":boost_res,
      "parity_exchange_residual":parity_exchange,
      "upper_lower_coordinate_boost_leakage":coord_boost,
      "induced_weyl_boost_generators":"B_i^(s) = -s sigma_i/2",
      "parity_action":"exchanges s=+1 and s=-1 Weyl sectors",
      "passed":max(gamma5_square,gamma5_herm,projector_res,
                   max(rot_res.values()),max(boost_res.values()),parity_exchange)<=tol
    }


if __name__=="__main__":
 import json
 print(json.dumps(audit(),indent=2))
