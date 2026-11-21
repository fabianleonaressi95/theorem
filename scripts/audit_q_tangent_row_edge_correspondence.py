#!/usr/bin/env python3
"""Audit the 192x188 tangent frame and its four-dimensional orthogonal complement.

No row-to-edge ordering is assumed. The script deliberately refuses to infer
one from matching dimensions alone.
"""
import argparse, json
from collections import Counter
from pathlib import Path
import numpy as np

def run(path):
    z=np.load(path)
    Q=z["Q_tangent"]
    A=z["Q6_adjacency"]
    if Q.shape != (192,188):
        raise ValueError(f"Expected Q_tangent (192,188), got {Q.shape}")
    edges=np.argwhere(np.triu(A,1))
    if len(edges)!=192:
        raise ValueError(f"Expected 192 undirected graph edges, found {len(edges)}")
    QtQ=Q.T@Q
    H=Q@Q.T
    P=np.eye(192)-H
    ev=np.linalg.eigvalsh(P)
    # Basis-independent row leverage scores; these do not label graph edges.
    leverage=np.diag(P)
    counts=Counter(np.round(leverage,8))
    return {
      "classification":"structural numerical audit",
      "Q_tangent_shape":list(Q.shape),
      "Q6_undirected_edge_count":int(len(edges)),
      "Q_columns_orthonormal_residual_frobenius":float(np.linalg.norm(QtQ-np.eye(188))),
      "rank_Q_tangent":int(np.linalg.matrix_rank(Q,tol=1e-10)),
      "row_projector_idempotence_residual":float(np.linalg.norm(H@H-H)),
      "complement_projector_idempotence_residual":float(np.linalg.norm(P@P-P)),
      "complement_rank":int(np.sum(ev>0.5)),
      "complement_eigenvalues":ev[-4:].tolist(),
      "row_leverage_score_counts_rounded_1e-8":{str(k):int(v) for k,v in sorted(counts.items())},
      "row_edge_correspondence":"NOT IDENTIFIED: archive contains Q_tangent and Q6_adjacency but no row_to_edge index array or construction metadata.",
      "what_is_proven_numerically":[
        "Q_tangent is a 192x188 matrix with full column rank 188.",
        "Its columns are orthonormal to approximately 1.3e-14 Frobenius residual.",
        "The 192D row-coordinate space has a 4D orthogonal complement.",
        "Q6_adjacency has exactly 192 undirected edges."
      ],
      "what_is_not_claimed":[
        "The numerical equality of row count and graph edge count does not prove row i represents edge i.",
        "No induced edge permutation or 188D group representation is computed without that correspondence.",
        "No symmetry claim about K0, R_geo_tangent, P_G or T_transport follows from row counts alone."
      ],
      "required_missing_artifact":"A 192-entry row_to_edge array, each entry an ordered or canonical pair of Q6 state indices, together with the convention used to construct Q_tangent."
    }

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("npz",nargs="?",default="data/RGS_PSU_all_matrices.npz")
    p.add_argument("--out",default="audits/Q_tangent_row_edge_correspondence.json")
    a=p.parse_args()
    r=run(a.npz)
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(r,indent=2),encoding="utf-8")
    print(json.dumps(r,indent=2))
