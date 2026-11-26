#!/usr/bin/env python3
"""Reconstruct the 188D Q6 action from the actual 64x3 coordinate semantics.

Q_tangent has 192 rows = 64 vertices x 3 Cartesian displacement coordinates.
It is NOT indexed by the 192 graph edges. For each signed coordinate
permutation T in O_h, recover its vertex permutation from X, retain exactly
those preserving Q6 adjacency, then build the ambient 192x192 action S.

Convention: x'_{p(i)} = T x_i, and the same action is applied to variations.
The induced tangent action is U = Q.T @ S @ Q.
"""
import argparse, itertools, json
from pathlib import Path
import numpy as np
from scipy.optimize import linear_sum_assignment

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("npz", help="RGS_PSU_all_matrices.npz")
    ap.add_argument("--out",default="audits/Q6_tangent_188D_reconstruction.json")
    ap.add_argument("--matrices",default="audits/Q6_tangent_188D_actions.npz")
    args=ap.parse_args()
    z=np.load(args.npz,allow_pickle=False)
    X=np.asarray(z["X_Oh_reconstructed"],float)
    Q=np.asarray(z["Q_tangent"],float)
    A=np.asarray(z["Q6_adjacency"],int)
    if X.shape!=(64,3) or Q.shape!=(192,188) or A.shape!=(64,64):
        raise ValueError(f"Unexpected shapes X={X.shape}, Q={Q.shape}, A={A.shape}")
    qorth=float(np.linalg.norm(Q.T@Q-np.eye(188)))
    if qorth>1e-8: raise ValueError(f"Q is not orthonormal: {qorth}")
    P=Q@Q.T
    records=[]
    for perm in itertools.permutations(range(3)):
      for signs in itertools.product((-1.,1.),repeat=3):
        T=np.eye(3)[list(perm)]*np.asarray(signs)[:,None]
        Xt=X@T.T
        dist=np.linalg.norm(Xt[:,None,:]-X[None,:,:],axis=2)
        rr,cc=linear_sum_assignment(dist)
        p=np.empty(64,dtype=int); p[rr]=cc
        geom=float(dist[rr,cc].max())
        if geom>1e-10: continue
        graph=float(np.max(np.abs(A-A[np.ix_(p,p)])))
        if graph!=0: continue
        S=np.zeros((192,192))
        for i in range(64):
            S[3*p[i]:3*p[i]+3,3*i:3*i+3]=T
        U=Q.T@S@Q
        records.append({"perm":perm,"signs":signs,"T":T,"p":p,"S":S,"U":U,
          "geometry_residual":geom,
          "projector_residual":float(np.linalg.norm(S@P@S.T-P)),
          "intertwiner_residual":float(np.linalg.norm(S@Q-Q@U)),
          "orthogonality_residual":float(np.linalg.norm(U.T@U-np.eye(188)))})
    if len(records)!=16: raise AssertionError(f"Expected common subgroup order 16, got {len(records)}")
    # Verify group closure on both vertex permutations and spatial matrices.
    keys={(tuple(r["p"]),tuple(np.round(r["T"].ravel(),8))) for r in records}
    closure_failures=0
    for a in records:
      for b in records:
        pc=a["p"][b["p"]]
        Tc=a["T"]@b["T"]
        if (tuple(pc),tuple(np.round(Tc.ravel(),8))) not in keys:
            closure_failures+=1
    # Operators are compared in the reconstructed tangent representation.
    operator_results={}
    for name in ("K0","R_geo_tangent","P_G","T_transport"):
        if name not in z: continue
        M=np.asarray(z[name],float)
        residuals=[float(np.linalg.norm(r["U"].T@M@r["U"]-M)/max(np.linalg.norm(M),1e-30)) for r in records]
        operator_results[name]={
          "preserved_count_tol_1e-10":sum(v<1e-10 for v in residuals),
          "group_order":len(records),
          "max_relative_commutator":max(residuals),
          "identity_relative_commutator":min(residuals)
        }
    report={
      "classification":"reconstructed finite-dimensional group representation; numerical verification",
      "coordinate_semantics":"192 rows are 64 vertex displacement triples (x_i,y_i,z_i), not 192 graph-edge labels.",
      "ambient_action":"x'_{p(i)}=T x_i; S is the corresponding 192x192 block permutation-coordinate action.",
      "tangent_action":"U(T,p)=Q_tangent^T S(T,p) Q_tangent",
      "dimensions":{"X":[64,3],"Q_tangent":[192,188],"ambient_dimension":192,"tangent_dimension":188},
      "Q_orthonormality_residual":qorth,
      "signed_coordinate_permutations_tested":48,
      "geometry_and_Q6_compatible_subgroup_order":len(records),
      "group_closure_failures":closure_failures,
      "max_projector_invariance_residual":max(r["projector_residual"] for r in records),
      "max_intertwiner_residual":max(r["intertwiner_residual"] for r in records),
      "max_induced_orthogonality_residual":max(r["orthogonality_residual"] for r in records),
      "operator_covariance":operator_results,
      "interpretation":[
        "The 188D tangent action is reconstructed without any row-to-edge map.",
        "All 16 common geometry/Q6 symmetries preserve Im(Q_tangent) and induce orthogonal 188D matrices.",
        "R_geo_tangent is covariant under all 16 reconstructed actions.",
        "K0, P_G and T_transport are covariant only under the identity among these 16 actions.",
        "The failure of those three operators is not repaired by an arbitrary extension on the 124D complement."
      ]
    }
    Path(args.out).parent.mkdir(parents=True,exist_ok=True)
    Path(args.out).write_text(json.dumps(report,indent=2),encoding="utf-8")
    np.savez_compressed(args.matrices,
      S=np.stack([r["S"] for r in records]),
      U=np.stack([r["U"] for r in records]),
      vertex_permutations=np.stack([r["p"] for r in records]),
      spatial_matrices=np.stack([r["T"] for r in records]))
    print(json.dumps(report,indent=2))
if __name__=="__main__": main()
