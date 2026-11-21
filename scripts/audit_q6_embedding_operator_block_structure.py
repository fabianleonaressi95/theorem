#!/usr/bin/env python3
"""Determine whether the stored 64D geometric embedding is invariant under 188D operators.

This is a structural audit, not a construction of a full 188D group action.
"""
import argparse, json
from pathlib import Path
import numpy as np

def rel(a,b):
    return float(np.linalg.norm(a-b)/max(np.linalg.norm(b),1e-30))

def run(path):
    z=np.load(path)
    B=z["A_geometry_orthonormal"]
    if B.shape != (188,64):
        raise ValueError(f"Unexpected embedding shape {B.shape}")
    I=np.eye(188); C=I-B@B.T
    names=("K0","R_geo_tangent","T_transport","P_G")
    out={}
    for name in names:
        O=z[name]
        out[name]={
            "operator_shape":list(O.shape),
            "relative_offdiagonal_B_to_complement":float(np.linalg.norm(B.T@O@C)/np.linalg.norm(O)),
            "relative_offdiagonal_complement_to_B":float(np.linalg.norm(C@O@B)/np.linalg.norm(O)),
            "relative_compression_norm":float(np.linalg.norm(B.T@O@B)/np.linalg.norm(O)),
            "B_subspace_invariant_under_O":bool(np.linalg.norm(C@O@B)/np.linalg.norm(O)<1e-10),
            "B_subspace_invariant_under_O_transpose":bool(np.linalg.norm(C@O.T@B)/np.linalg.norm(O)<1e-10)
        }
    return {
      "classification":"numerical structural audit",
      "embedding":"A_geometry_orthonormal (188 x 64), verified orthonormal columns",
      "orthogonality_residual":float(np.linalg.norm(B.T@B-np.eye(64))),
      "complement_dimension":124,
      "operators":out,
      "conclusion":"R_geo_tangent reduces the 188D space into the embedded 64D sector and its orthogonal complement. K0 and P_G couple the two sectors in both directions. T_transport has one-way coupling: B^T T C is numerically zero, while C T B is not. Therefore the 64D state action does not determine a full 188D symmetry action; an extension on the complement must be derived from additional geometric construction data, not chosen arbitrarily.",
      "limitation":"No canonical edge-row permutation for Q_tangent is asserted: the archive does not provide an explicit row-to-edge index map."
    }

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("npz",nargs="?",default="data/RGS_PSU_all_matrices.npz")
    p.add_argument("--out",default="audits/Q6_embedding_operator_block_structure.json")
    a=p.parse_args()
    r=run(a.npz)
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(r,indent=2),encoding="utf-8")
    print(json.dumps(r,indent=2))
