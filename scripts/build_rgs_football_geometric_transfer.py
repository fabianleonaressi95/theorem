#!/usr/bin/env python3
"""Construct and audit the geometry-driven RGS(64x3)->football(92x3) transfer."""
from pathlib import Path
import argparse, json, sys
import numpy as np

# Running a file under scripts/ puts that directory, not the repository root,
# at sys.path[0]. Add the project root so the models namespace is importable.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from models.football_shell import build_football_shell
from models.football_quaternion_bridge import build_geometry_transfer, project_shell_tangent

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",default="data/rgs_188d/X_Oh_reconstructed.csv")
    ap.add_argument("--radius",type=float,default=1.)
    ap.add_argument("--neighbors",type=int,default=12)
    ap.add_argument("--out",default="reports/rgs_football_geometric_transfer.json")
    args=ap.parse_args()
    X=np.genfromtxt(args.source,delimiter=",",names=True)
    X=np.column_stack([X[k] for k in ("x","y","z")])
    mesh=build_football_shell(radius=args.radius)
    W,diag=build_geometry_transfer(X,mesh["nodes"],neighbors=args.neighbors)
    # Constant Cartesian vector fields must be reproduced exactly.
    constants=np.tile(np.eye(3),(64,1))
    const_error=float(np.linalg.norm(W@constants-np.tile(np.eye(3),(92,1))))
    # Projected output is the actual 184-dimensional shell tangent lift.
    P_modes=project_shell_tangent(mesh,W)
    rank=int(np.linalg.matrix_rank(P_modes,tol=1e-10))
    report={"status":"COMPUTED_GEOMETRIC_TRANSFER",
      "source_file":args.source,"source_shape":list(X.shape),
      "target_nodes":int(len(mesh["nodes"])),"target_shape":[276,192],
      "transfer":diag,"constant_vector_reproduction":const_error,
      "projected_transfer_shape":list(P_modes.shape),
      "projected_transfer_rank":rank,
      "shell_tangent_dof":184,
      "interpretation":"A geometry-based interpolation from 64 RGS sites to 92 shell nodes. It is not a symmetry intertwiner and does not establish physical equivalence.",
      "limitations":["RGS points and shell nodes are not one-to-one physical sites.",
        "The interpolation is local affine in direction and does not preserve an unknown RGS stiffness energy automatically.",
        "A dynamical comparison requires importing the actual RGS spectral triplet and shell eigenmodes, then evaluating principal angles after this transfer."]}
    out=Path(args.out); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,indent=2))
    np.savez_compressed(out.with_suffix(".npz"),W= W, W_tangent=P_modes,
      source_points=X,target_nodes=mesh["nodes"])
    print(json.dumps(report,indent=2))
if __name__=="__main__": main()
