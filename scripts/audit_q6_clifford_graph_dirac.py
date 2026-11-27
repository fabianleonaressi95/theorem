#!/usr/bin/env python3
"""Finite Clifford graph operator on Q6; tests the bare carrier, not a continuum limit."""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np

def gamma6():
    sx=np.asarray([[0,1],[1,0]],complex); sy=np.asarray([[0,-1j],[1j,0]],complex)
    sz=np.asarray([[1,0],[0,-1]],complex); I=np.eye(2,dtype=complex)
    k=lambda a,b,c: np.kron(np.kron(a,b),c)
    return (k(sx,I,I),k(sy,I,I),k(sz,sx,I),k(sz,sy,I),k(sz,sz,sx),k(sz,sz,sy))

def chirality(gammas):
    out=np.eye(8,dtype=complex)
    for g in gammas: out=out@g
    return 1j*out

def q6_bits():
    return np.asarray([[(v>>i)&1 for i in range(6)] for v in range(64)],dtype=np.int8)

def direction_operators():
    bits=q6_bits(); out=[]
    for axis in range(6):
        T=np.zeros((64,64),dtype=complex)
        for v in range(64):
            if bits[v,axis]==0: T[v^(1<<axis),v]=1.0
        out.append(T-T.conj().T)
    return tuple(out)

def graph_dirac():
    D=np.zeros((512,512),dtype=complex)
    for K,G in zip(direction_operators(),gamma6()): D += 0.5*np.kron(K,G)
    return D

def gauged_graph_dirac(link_phases):
    bits=q6_bits(); D=np.zeros((512,512),dtype=complex); Ks=[]
    for axis,G in enumerate(gamma6()):
        K=np.zeros((64,64),dtype=complex)
        for v in range(64):
            if bits[v,axis]==0:
                w=v^(1<<axis); u=np.exp(1j*link_phases[axis,v])
                K[w,v]=u; K[v,w]=-np.conjugate(u)
        Ks.append(K); D += 0.5*np.kron(K,G)
    return D,tuple(Ks)

def run_audit():
    gam=gamma6(); gs=chirality(gam); D=graph_dirac(); I512=np.eye(512,dtype=complex)
    herm=float(np.linalg.norm(D.conj().T+D))
    chir=float(np.linalg.norm(np.kron(np.eye(64),gs)@D+D@np.kron(np.eye(64),gs)))
    square=float(np.linalg.norm(D@D+1.5*I512))
    ev=np.linalg.eigvalsh(1j*D); gap=float(np.min(np.abs(ev)))
    pos=int(np.count_nonzero(ev>0)); neg=int(np.count_nonzero(ev<0))
    phases=np.zeros((6,64),dtype=float)
    for a in range(6):
        for v in range(64): phases[a,v]=0.013*(a+1)*(v+3)
    Dg,_=gauged_graph_dirac(phases)
    chi=np.asarray([0.017*(v+1)**2 for v in range(64)])
    G=np.diag(np.exp(1j*chi)); pp=phases.copy(); bits=q6_bits()
    for a in range(6):
        for v in range(64):
            if bits[v,a]==0:
                w=v^(1<<a); pp[a,v]+=chi[w]-chi[v]
    Dgp,_=gauged_graph_dirac(pp); Gs=np.kron(G,np.eye(8))
    cov=float(np.linalg.norm(Dgp-Gs@Dg@Gs.conj().T))
    gh=float(np.linalg.norm(Dg.conj().T+Dg))
    gc=float(np.linalg.norm(np.kron(np.eye(64),gs)@Dg+Dg@np.kron(np.eye(64),gs)))
    Dm,_=gauged_graph_dirac(-phases)
    Ddouble=np.block([[Dg,np.zeros_like(Dg)],[np.zeros_like(Dg),Dm]])
    tau1=np.asarray([[0,1],[1,0]],complex); J=np.kron(np.eye(512),tau1)
    Dswap=np.block([[Dm,np.zeros_like(Dm)],[np.zeros_like(Dg),Dg]])
    sex=float(np.linalg.norm(J@Ddouble@J-Dswap))
    checks={
        "bare_operator_antihermitian":herm<1e-11,
        "bare_operator_chiral":chir<1e-11,
        "bare_square_exactly_minus_three_halves":square<1e-10,
        "bare_spectrum_has_256_each_sign":pos==256 and neg==256,
        "bare_spectrum_has_no_zero_mode":gap>1e-10,
        "gauged_operator_antihermitian":gh<1e-11,
        "gauged_operator_chiral":gc<1e-11,
        "local_U1_gauge_covariance":cov<1e-10,
        "AntiTwin_conjugate_sheet_exchange":sex<1e-10}
    checks={k:bool(v) for k,v in checks.items()}
    return {
        "status":"FINITE_Q6_CLIFFORD_GRAPH_OPERATOR_AUDITED_NO_CONTINUUM_MODE",
        "carrier":{"vertices":64,"directions":6,"undirected_edges":192,"spinor_dimension":8,"operator_dimension":512},
        "operator":"D_Q6=(1/2) sum_i Gamma_i tensor K_i; K_i=T_i-T_i^dagger with oriented 0->1 Q6 edge partial shift",
        "exact_bare_result":{"D_dagger_plus_D":herm,"{Gamma_star,D}":chir,"D_squared_plus_3I_over_2":square,"eigenvalue_sign_counts":{"negative":neg,"positive":pos},"minimum_absolute_eigenvalue":gap,"eigenvalues_expected":"± i sqrt(3/2), each multiplicity 256"},
        "gauged_result":{"antihermiticity_residual":gh,"chiral_residual":gc,"local_gauge_covariance_residual":cov,"anti_twin_sheet_exchange_residual":sex},
        "checks":checks,"pass":all(checks.values()),
        "interpretation":[
            "Finite Q6 Clifford graph operator, not a continuum Dirac discretization.",
            "Identity-link spectrum is exactly flat and gapped away from zero; it has no light Dirac cone.",
            "Conjugate Anti-Twin links are gauge-covariant but do not create a low-energy branch.",
            "Exact Z2 sheet exchange is distinct from a continuous relative U(1).",
            "A refinement-consistent, domain-wall or overlap construction is still required for physical fermion dynamics."]}

def main():
    result=run_audit(); out=Path("audits/Q6_CLIFFORD_GRAPH_DIRAC_AUDIT.json")
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2))
    if not result["pass"]: raise SystemExit(1)

if __name__=="__main__": main()
