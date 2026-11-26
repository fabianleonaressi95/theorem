#!/usr/bin/env python3
"""MMFF94s relaxation and Coulomb tangent-Hessian audit for ideal C60.

The input is the exact truncated-icosahedron graph and coordinates.  The
molecular model is an explicitly declared all-aromatic C60 graph; it is a
computational model, not an experimental structure or a DFT calculation.
Requires numpy, scipy, and RDKit with MMFF94s parameters.
"""
from __future__ import annotations
import argparse, json
from itertools import combinations, product
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from scipy.spatial.distance import cdist
from scipy.linalg import null_space

PHI = (1.0 + np.sqrt(5.0)) / 2.0
TOL = 1e-8

def ico_vertices():
    v=[]
    for s,t in product((-1,1), repeat=2): v.append((0.,s,t*PHI))
    for s,t in product((-1,1), repeat=2): v.append((s,t*PHI,0.))
    for s,t in product((-1,1), repeat=2): v.append((t*PHI,0.,s))
    return np.asarray(v)

def c60_ideal():
    v=ico_vertices()
    h=ConvexHull(v)
    edges=set()
    for tri in h.simplices:
        for i,j in combinations(map(int,tri),2): edges.add(tuple(sorted((i,j))))
    xyz=[]; labels={}
    for i,j in sorted(edges):
        for a,b in ((i,j),(j,i)):
            labels[(a,b)]=len(xyz)
            xyz.append((2*v[a]+v[b])/3.0)
    xyz=np.asarray(xyz)
    bonds=set()
    for (a,b),i in labels.items():
        j=labels[(b,a)]
        bonds.add(tuple(sorted((i,j))))
    for i in range(len(xyz)):
        for j in range(i+1,len(xyz)):
            if abs(np.linalg.norm(xyz[i]-xyz[j])-2/3)<1e-7: bonds.add((i,j))
    # Graph from the 60 directed-edge points: each point joins the two points
    # on the same original edge and the point on each adjacent original edge.
    # The geometric nearest-neighbour test above gives the 90 fullerene bonds.
    bonds={tuple(sorted(e)) for e in bonds if e[0]!=e[1]}
    return xyz, sorted(bonds)

def mmff_relax(xyz,bonds,max_iters):
    try:
        from rdkit import Chem
        from rdkit.Chem import AllChem
    except Exception as e:
        raise RuntimeError("RDKit is required (pip install rdkit).") from e
    mol=Chem.RWMol()
    for _ in range(60):
        atom=Chem.Atom("C"); atom.SetIsAromatic(True); mol.AddAtom(atom)
    for i,j in bonds:
        mol.AddBond(int(i),int(j),Chem.BondType.AROMATIC)
    m=mol.GetMol()
    Chem.SanitizeMol(m)
    conf=Chem.Conformer(60)
    for i,p in enumerate(xyz): conf.SetAtomPosition(i,tuple(map(float,p)))
    m.AddConformer(conf)
    props=AllChem.MMFFGetMoleculeProperties(m,mmffVariant="MMFF94s")
    if props is None: raise RuntimeError("MMFF94s parameters unavailable for generated C60 model.")
    ff=AllChem.MMFFGetMoleculeForceField(m,props,ignoreInterfragInteractions=False)
    e0=float(ff.CalcEnergy())
    status=int(ff.Minimize(maxIts=max_iters))
    conf=m.GetConformer()
    out=np.asarray(conf.GetPositions(),float)
    ff2=AllChem.MMFFGetMoleculeForceField(m,props,ignoreInterfragInteractions=False)
    return out, {"model":"RDKit MMFF94s; neutral all-aromatic C60 graph",
                 "initial_mmff_energy":e0,"final_mmff_energy":float(ff2.CalcEnergy()),
                 "optimizer_status":status,"iterations_limit":max_iters,
                 "force_norm":float(np.linalg.norm(ff2.CalcGrad()))}

def coulomb_energy_gradient(x):
    n=len(x); g=np.zeros_like(x); e=0.0
    for i in range(n):
        d=x[i+1:]-x[i]
        r=np.linalg.norm(d,axis=1)
        if np.any(r<1e-10): raise ValueError("Coincident atoms.")
        e+=float(np.sum(1/r))
        z=d/(r[:,None]**3)
        g[i]+=np.sum(z,axis=0); g[i+1:]-=z
    return e,g

def coulomb_hessian(x):
    n=len(x); H=np.zeros((3*n,3*n))
    for i in range(n):
        for j in range(i+1,n):
            d=x[i]-x[j]; r=np.linalg.norm(d)
            B=3*np.outer(d,d)/r**5-np.eye(3)/r**3
            si=slice(3*i,3*i+3); sj=slice(3*j,3*j+3)
            H[si,si]+=B; H[sj,sj]+=B; H[si,sj]-=B; H[sj,si]-=B
    return H

def tangent_basis(x):
    n=len(x)
    C=np.zeros((4,3*n))
    C[0,0::3]=1; C[1,1::3]=1; C[2,2::3]=1
    C[3,:]=x.reshape(-1)
    return null_space(C)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out-dir",default="c60_mmff94s_audit")
    ap.add_argument("--max-iterations",type=int,default=10000)
    args=ap.parse_args()
    out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
    x0,bonds=c60_ideal()
    if len(x0)!=60 or len(bonds)!=90: raise RuntimeError(f"Bad C60 topology: {len(x0)} atoms, {len(bonds)} edges")
    x,model=mmff_relax(x0,bonds,args.max_iterations)
    e,g=coulomb_energy_gradient(x)
    Q=tangent_basis(x)
    H=coulomb_hessian(x)
    K=Q.T@H@Q
    eig=np.linalg.eigvalsh((K+K.T)/2)
    # The Coulomb gradient is not assumed to vanish at an MMFF stationary point.
    tangent_grad=Q.T@g.reshape(-1)
    lam=-float(np.dot(g.reshape(-1),x.reshape(-1))/np.dot(x.reshape(-1),x.reshape(-1)))
    radial_res=float(np.linalg.norm(g+lam*x))
    report={
      "status":"computed_by_script_when_run",
      "geometry":{"atoms":60,"bonds":len(bonds),"ideal_edge_length":2/3,
                  "relaxed_rms_radius":float(np.sqrt(np.mean(np.sum(x*x,axis=1)))),
                  "max_abs_bond_length_deviation_from_mean":float(np.max(np.abs(np.array([np.linalg.norm(x[i]-x[j]) for i,j in bonds])-np.mean([np.linalg.norm(x[i]-x[j]) for i,j in bonds]))))},
      "molecular_relaxation":model,
      "coulomb":{"energy":e,"gradient_norm":float(np.linalg.norm(g)),
                 "tangent_gradient_norm":float(np.linalg.norm(tangent_grad)),
                 "least_squares_radial_multiplier_diagnostic_only":lam,
                 "radial_stationarity_residual":radial_res,
                 "tangent_dimension":int(Q.shape[1]),
                 "hessian_min":float(eig[0]),"hessian_max":float(eig[-1]),
                 "negative_modes":int(np.sum(eig < -1e-8)),
                 "near_zero_modes":int(np.sum(np.abs(eig)<=1e-8)),
                 "positive_modes":int(np.sum(eig > 1e-8)),
                 "interpretation":"Raw Coulomb Hessian restricted to translations-and-scale-orthogonal tangent space. No Lagrange shift is applied unless Coulomb tangential stationarity is established."},
      "limitations":["MMFF94s is an empirical molecular mechanics model, not DFT or experimental refinement.",
                     "The all-aromatic graph is an explicit modelling choice; inspect RDKit sanitization and MMFF parameter availability.",
                     "The relaxed geometry need not retain exact Ih/Th symmetry. Symmetry sectors must be recomputed from the relaxed coordinates, not copied from the ideal cage."]
    }
    np.savez_compressed(out/"C60_MMFF94s_relaxed_coulomb.npz",X_ideal=x0,X_relaxed=x,
                        bonds=np.asarray(bonds,dtype=int),Q_tangent=Q,
                        H_coulomb=H,K_coulomb=K,eigenvalues=eig,gradient=g)
    (out/"report.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))

if __name__=="__main__": main()
