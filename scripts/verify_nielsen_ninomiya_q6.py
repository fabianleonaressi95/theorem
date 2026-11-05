#!/usr/bin/env python3
"""Verify exact finite Q6 identities; this is not a continuum no-go test."""
from itertools import product
import json
import numpy as np


def gamma_matrices():
    I=np.eye(2,dtype=complex)
    X=np.array([[0,1],[1,0]],complex)
    Y=np.array([[0,-1j],[1j,0]],complex)
    Z=np.array([[1,0],[0,-1]],complex)
    k=np.kron
    return [k(k(X,I),I),k(k(Y,I),I),k(k(Z,X),I),
            k(k(Z,Y),I),k(k(Z,Z),X),k(k(Z,Z),Y)]


def main():
    G=gamma_matrices()
    I8=np.eye(8,dtype=complex)
    herm=anti=spec=0.0
    for i,A in enumerate(G):
        herm=max(herm,float(np.linalg.norm(A.conj().T-A)))
        for j,B in enumerate(G):
            anti=max(anti,float(np.linalg.norm(A@B+B@A-2*(i==j)*I8)))
    by_weight={}
    zero_modes=0
    dimension=0
    for kbits in product((0,1),repeat=6):
        m=sum(kbits)
        D=sum((-2*kbits[i]*G[i] for i in range(6)),np.zeros((8,8),complex))
        spec=max(spec,float(np.linalg.norm(D@D-4*m*I8)))
        eig=np.linalg.eigvalsh(D)
        z=int(np.count_nonzero(np.abs(eig)<1e-10))
        zero_modes+=z
        dimension+=len(eig)
        row=by_weight.setdefault(str(m),{"characters":0,"zero_spin_modes":0})
        row["characters"]+=1
        row["zero_spin_modes"]+=z
    report={
        "graph":"Cayley(Z_2^6) = Q6","vertices":64,"edges":192,
        "spin_dimension":8,"total_spin_character_dimension":dimension,
        "zero_modes_spin_only":zero_modes,
        "expected_zero_modes_spin_only":8,
        "centered_difference_is_identically_zero":True,
        "clifford_hermiticity_residual":herm,
        "clifford_anticommutator_residual":anti,
        "Dplus_square_residual":spec,
        "spectrum_by_hamming_weight":by_weight,
        "scope":"Finite graph identities only; no continuum Weyl chirality count or no-go evasion."
    }
    assert dimension==512 and zero_modes==8
    assert max(herm,anti,spec)<1e-12
    print(json.dumps(report,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
