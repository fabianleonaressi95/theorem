#!/usr/bin/env python3
"""Reproducible finite verification suite for the Q6 laws used in T013-T015.

Requires: Python 3.10+, NumPy.
Run: python scripts/verify_q6_laws.py --seed 20261105
Outputs a JSON report to stdout (and optionally --output report.json).

This checks finite algebraic identities. It does not establish a continuum limit,
physical QCD, confinement, or the physical interpretation of RGS/PSU data.
"""
from __future__ import annotations
import argparse, json, math, platform
from itertools import combinations, product
import numpy as np

N = 64
D = 6
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)

def kron3(a, b, c):
    return np.kron(np.kron(a, b), c)

GAMMA = [
    kron3(X,I2,I2), kron3(Y,I2,I2),
    kron3(Z,X,I2), kron3(Z,Y,I2),
    kron3(Z,Z,X), kron3(Z,Z,Y),
]
I8 = np.eye(8, dtype=complex)
I3 = np.eye(3, dtype=complex)

def maxabs(a):
    return float(np.max(np.abs(a))) if np.size(a) else 0.0

def vertices():
    return list(range(64))

def bit(v, i):
    return (v >> i) & 1

def flip(v, i):
    return v ^ (1 << i)

def q6_edges():
    return [(v, flip(v,i), i) for v in vertices() for i in range(6) if bit(v,i)==0]

def q6_squares():
    # One positively oriented square for every pair of directions and assignment
    # of the remaining four coordinates: C(6,2)*2^4 = 240.
    out=[]
    for i,j in combinations(range(6),2):
        rest=[k for k in range(6) if k not in (i,j)]
        for vals in product((0,1), repeat=4):
            v=sum(vals[t] << rest[t] for t in range(4))
            vi, vij, vj = flip(v,i), flip(flip(v,i),j), flip(v,j)
            out.append((v,vi,vij,vj,i,j))
    return out

def boundary_matrices():
    edges=q6_edges(); squares=q6_squares()
    b1=np.zeros((64,len(edges)),dtype=np.int64)
    edge_index={}
    for e,(v,w,i) in enumerate(edges):
        b1[v,e]=-1; b1[w,e]=1; edge_index[(v,w)]=e
    b2=np.zeros((len(edges),len(squares)),dtype=np.int64)
    for s,(v,vi,vij,vj,i,j) in enumerate(squares):
        oriented=[(v,vi,1),(vi,vij,1),(vj,vij,-1),(v,vj,-1)]
        for a,b,sgn in oriented:
            if (a,b) in edge_index: b2[edge_index[(a,b)],s]+=sgn
            elif (b,a) in edge_index: b2[edge_index[(b,a)],s]-=sgn
            else: raise AssertionError("square boundary edge missing")
    return b1,b2

def clifford_audit():
    residuals=[]
    for i,gi in enumerate(GAMMA):
        residuals.append(maxabs(gi.conj().T-gi))
        for j,gj in enumerate(GAMMA):
            residuals.append(maxabs(gi@gj+gj@gi-2*(i==j)*I8))
    return max(residuals)

def free_spectrum_audit():
    # Each character k has D(k)=-2 sum_{i:k_i=1} Gamma_i.
    observed=[]; expected=[]
    for k in product((0,1), repeat=6):
        m=sum(k)
        dk=-2*sum((k[i]*GAMMA[i] for i in range(6)), start=np.zeros((8,8),complex))
        eig=np.linalg.eigvalsh(dk)
        observed.extend(eig.tolist())
        if m==0: expected.extend([0.0]*8)
        else: expected.extend([-2*math.sqrt(m)]*4+[2*math.sqrt(m)]*4)
    observed=np.sort(np.asarray(observed))
    expected=np.sort(np.asarray(expected))
    return maxabs(observed-expected), int(np.count_nonzero(np.abs(observed)<1e-10)), len(observed)

def random_su3(rng):
    z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
    q,r=np.linalg.qr(z)
    phases=np.diag(r)
    q=q @ np.diag(np.conj(phases/np.abs(phases)))
    det=np.linalg.det(q)
    q[:,0] *= np.conj(det)
    return q

def gauge_covariance_audit(rng):
    # D_U psi(x) = sum_i Gamma_i [ U_i(x) psi(x+e_i) - psi(x) ].
    # Arrays use [vertex, spin, color].
    psi=rng.normal(size=(64,8,3))+1j*rng.normal(size=(64,8,3))
    g=np.stack([random_su3(rng) for _ in range(64)])
    links=np.empty((64,6,3,3),dtype=complex)
    for v in range(64):
        for i in range(6):
            links[v,i]=random_su3(rng)
    def apply(field, U):
        out=np.zeros_like(field)
        for v in range(64):
            for i in range(6):
                w=flip(v,i)
                transported=np.einsum("sc,dc->sd",field[w],U[v,i])
                out[v]+=np.einsum("st,tc->sc",GAMMA[i],transported-field[v])
        return out
    transformed_psi=np.einsum("vsc,vdc->vsd",psi,g)
    transformed_links=np.empty_like(links)
    for v in range(64):
        for i in range(6):
            w=flip(v,i)
            transformed_links[v,i]=g[v] @ links[v,i] @ g[w].conj().T
    lhs=apply(transformed_psi,transformed_links)
    rhs=np.einsum("vsc,vdc->vsd",apply(psi,links),g)
    return maxabs(lhs-rhs), maxabs(np.linalg.det(g)-1)

def epsilon_tensor():
    eps=np.zeros((3,3,3),dtype=int)
    eps[0,1,2]=eps[1,2,0]=eps[2,0,1]=1
    eps[0,2,1]=eps[2,1,0]=eps[1,0,2]=-1
    return eps

def baryon_color_singlet_audit(rng):
    # Verify epsilon_{abc} g_ai g_bj g_ck = epsilon_{ijk}.
    g=random_su3(rng)
    lhs=np.einsum("abc,ai,bj,ck->ijk",epsilon_tensor(),g,g,g)
    return maxabs(lhs-epsilon_tensor()), abs(np.linalg.det(g)-1)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--seed",type=int,default=20261105)
    ap.add_argument("--output",type=str,default="")
    args=ap.parse_args()
    rng=np.random.default_rng(args.seed)

    edges=q6_edges(); squares=q6_squares()
    b1,b2=boundary_matrices()
    chain_residual=maxabs(b1@b2)
    # Graph cycle rank = E - V + connected_components = 192-64+1 = 129.
    graph_cycle_rank=len(edges)-64+1
    # Rank-based first Betti number of the 2-skeleton, using numerical SVD
    # only as a diagnostic; exact integer rank certificates are a separate task.
    rank_b1=int(np.linalg.matrix_rank(b1.astype(float)))
    rank_b2=int(np.linalg.matrix_rank(b2.astype(float)))
    b1_two_skeleton=len(edges)-rank_b1-rank_b2

    cliff=clifford_audit()
    spectral,zero_modes,spectral_dim=free_spectrum_audit()
    gauge_res,det_res=gauge_covariance_audit(rng)
    baryon_res,baryon_det=baryon_color_singlet_audit(rng)

    checks={
      "q6_vertex_count": N==64,
      "q6_edge_count": len(edges)==192,
      "q6_square_count": len(squares)==240,
      "boundary_squared_zero": chain_residual==0.0,
      "graph_cycle_rank_129": graph_cycle_rank==129,
      "clifford_relations": cliff<1e-12,
      "free_spectrum_matches_T015": spectral<1e-10 and zero_modes==8 and spectral_dim==512,
      "local_su3_gauge_covariance": gauge_res<1e-11 and det_res<1e-11,
      "epsilon_color_singlet": baryon_res<1e-11 and baryon_det<1e-11,
    }
    report={
      "schema":"rgs-q6-law-verification/v1",
      "seed":args.seed,
      "environment":{"python":platform.python_version(),"numpy":np.__version__},
      "definitions":{"graph":"Q6 = Cayley graph of Z2^6","operator":"D_U psi(x)=sum_i Gamma_i(U_i(x)psi(x+e_i)-psi(x))","free_operator":"D_+=sum_i Gamma_i(T_i-I)"},
      "counts":{"vertices":64,"edges":len(edges),"squares":len(squares),"graph_cycle_rank":graph_cycle_rank,
                "rank_boundary_1_float_svd":rank_b1,"rank_boundary_2_float_svd":rank_b2,
                "b1_of_square_filled_2_skeleton_float_svd":b1_two_skeleton},
      "residuals":{"boundary_squared":chain_residual,"clifford_max":cliff,"free_spectrum_max_abs":spectral,
                   "gauge_covariance_max_abs":gauge_res,"random_su3_det_max_abs":det_res,
                   "baryon_epsilon_invariance_max_abs":baryon_res,"baryon_test_det_abs":baryon_det},
      "free_spectrum":{"dimension_spin_only":spectral_dim,"zero_modes_spin_only":zero_modes,
                       "zero_modes_with_three_colors":3*zero_modes,
                       "eigenvalues_by_hamming_weight":{"0":"0 (multiplicity 8)","m=1..6":"±2 sqrt(m), four each per character"}},
      "checks":checks,
      "all_checks_pass":all(checks.values()),
      "limitations":[
        "SVD ranks are numerical diagnostics, not exact rank certificates.",
        "The 129 graph cycle rank and the first Betti number after filling square 2-cells are different invariants.",
        "The Q6 forward Clifford spectrum is a finite graph spectrum, not a continuum Dirac spectrum.",
        "One random-gauge covariance test supplements but does not replace the algebraic proof in T014.",
        "No Yang-Mills action, fermion determinant, transfer matrix, confinement, baryon masses, or continuum limit is established."
      ]
    }
    rendered=json.dumps(report,indent=2,sort_keys=True)
    if args.output:
        with open(args.output,"w",encoding="utf-8") as f: f.write(rendered+"\n")
    print(rendered)
    if not report["all_checks_pass"]: raise SystemExit(1)

if __name__=="__main__":
    main()
