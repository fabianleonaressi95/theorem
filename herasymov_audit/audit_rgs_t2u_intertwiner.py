#!/usr/bin/env python3
"""Construct and audit O_h intertwiners Hom_G(CA_T2u, RGS_tangent).

Input NPZ contract:
  U_tan: (48,188,188), real orthogonal representation of O_h on RGS tangent.
  D_t2u: (48,3,3), real orthogonal T2u representation in the SAME group order.
  group: (48,3,3), integer signed-permutation matrices in matching order.
Optional:
  P_T2u: (188,188), independently computed RGS isotypic projector.
  B_T2u_TAN: (188,3), one selected carrier basis (not an isotypic basis).

This script does not fabricate missing RGS actions. It projects random maps by
the Reynolds operator, checks all representation/intertwining residuals, and
reports the rank of the resulting maps. A random seed is only a numerical
probe of Hom_G; it is not a physically selected coupling.
"""
import argparse, json
from pathlib import Path
import numpy as np

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",required=True,help="NPZ satisfying the documented contract")
    ap.add_argument("--output",default="rgs_t2u_intertwiner_audit.json")
    ap.add_argument("--trials",type=int,default=8)
    ap.add_argument("--seed",type=int,default=20261106)
    ap.add_argument("--tol",type=float,default=1e-9)
    a=ap.parse_args()
    z=np.load(a.input,allow_pickle=False)
    required=("U_tan","D_t2u","group")
    missing=[k for k in required if k not in z]
    if missing: raise KeyError(f"missing required arrays: {missing}")
    U=np.asarray(z["U_tan"],float); D=np.asarray(z["D_t2u"],float); G=np.asarray(z["group"],int)
    if U.shape!=(48,188,188) or D.shape!=(48,3,3) or G.shape!=(48,3,3):
        raise ValueError(f"bad shapes U={U.shape}, D={D.shape}, group={G.shape}")
    I188=np.eye(188); I3=np.eye(3)
    orthU=max(np.linalg.norm(x.T@x-I188) for x in U)
    orthD=max(np.linalg.norm(x.T@x-I3) for x in D)
    # Exact finite group multiplication table by signed-permutation matrices.
    lookup={tuple(x.ravel()):i for i,x in enumerate(G)}
    if len(lookup)!=48: raise ValueError("group array does not contain 48 distinct elements")
    mult=np.empty((48,48),int)
    for i,x in enumerate(G):
        for j,y in enumerate(G):
            key=tuple((x@y).ravel())
            if key not in lookup: raise ValueError("group is not closed")
            mult[i,j]=lookup[key]
    repU=max(np.linalg.norm(U[mult[i,j]]-U[i]@U[j]) for i in range(48) for j in range(48))
    repD=max(np.linalg.norm(D[mult[i,j]]-D[i]@D[j]) for i in range(48) for j in range(48))
    rng=np.random.default_rng(a.seed); trials=[]
    for k in range(a.trials):
        J0=rng.normal(size=(188,30))
        # Reynolds projector on Hom(source,target): rho(g) J sigma(g)^T.
        J=sum(U[g]@J0@np.kron(np.eye(10),D[g]).T for g in range(48))/48.0
        inter=max(np.linalg.norm(U[g]@J-J@np.kron(np.eye(10),D[g])) for g in range(48))
        s=np.linalg.svd(J,compute_uv=False)
        rank=int(np.sum(s> a.tol*max(1.0,s[0])))
        row={"trial":k,"rank":rank,"singular_values":s.tolist(),"intertwining_max_residual":float(inter)}
        if "P_T2u" in z:
            P=np.asarray(z["P_T2u"],float)
            if P.shape!=(188,188): raise ValueError("P_T2u must be (188,188)")
            row["P_T2u_J_residual"]=float(np.linalg.norm(P@J-J))
        trials.append(row)
    report={
      "status":"COMPUTED_FROM_SUPPLIED_GROUP_ACTIONS",
      "input":str(Path(a.input)),
      "group_order":48,"target_dimension":188,"source_dimension":30,
      "source_representation":"10 copies of the supplied 3D T2u representation",
      "orthogonality_U_max":float(orthU),"orthogonality_D_max":float(orthD),
      "representation_law_U_max":float(repU),"representation_law_D_max":float(repD),
      "trials":trials,
      "warning":"Reynolds-projected random intertwiners characterize the algebraic intertwiner space; they do not select a physical CA-to-RGS coupling. A data-defined cross-covariance or variational criterion is still required.",
      "selected_triplet_warning":"If only B_T2U_TAN (188,3) is supplied, it is one carrier triplet, not the full 30D isotypic component. It cannot certify a 10-copy embedding."
    }
    Path(a.output).write_text(json.dumps(report,indent=2)); print(json.dumps(report,indent=2))
    if max(orthU,orthD,repU,repD)>a.tol: raise SystemExit("FAIL: supplied group actions are not verified representations")
    if max(t["intertwining_max_residual"] for t in trials)>100*a.tol: raise SystemExit("FAIL: intertwiner residual")

if __name__=="__main__": main()
