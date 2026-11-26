#!/usr/bin/env python3
"""End-to-end RGS rigid-rotation triplet -> football tangent spectrum comparison.

This deliberately tests the geometrically defined rotational triplet (T1g-like),
not the unverified T2u eigenspace. The source 188D tangent basis is reconstructed
from the exact four constraints documented in the recovered A14 source.
"""
from pathlib import Path
import argparse,json
import sys

# Direct execution puts scripts/, not the repository root, on sys.path.
# Add the root explicitly so the sibling models package is importable.
REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

import numpy as np
from scipy.linalg import null_space,eigh
from models.football_shell import build_football_shell,solve_discrete_shell
from models.football_quaternion_bridge import build_geometry_transfer,project_shell_tangent,principal_angle_audit
from models.football_quaternion_tangent import build_tangent_quaternion_audit,quaternion_from_matrix

def polar(A,tol=1e-11):
 U,s,_=np.linalg.svd(A,full_matrices=False)
 return U[:,:int(np.sum(s>tol*s[0]))],s

def main():
 p=argparse.ArgumentParser()
 p.add_argument("--source",default="data/rgs_188d/X_Oh_reconstructed.csv")
 p.add_argument("--out",default="reports/rgs_football_triplet_spectral_comparison.json")
 p.add_argument("--neighbors",type=int,default=16)
 a=p.parse_args()
 dat=np.genfromtxt(a.source,delimiter=",",names=True); X=np.column_stack([dat[k] for k in ("x","y","z")])
 C=np.zeros((4,192)); C[0,0::3]=1; C[1,1::3]=1; C[2,2::3]=1; C[3]=X.reshape(-1)
 Q=null_space(C)
 if Q.shape!=(192,188): raise RuntimeError(f"RGS tangent basis shape {Q.shape}")
 # Infinitesimal global rotations omega x X; these satisfy all four constraints.
 G=np.column_stack([np.cross(np.broadcast_to(e,(64,3)),X).reshape(-1) for e in np.eye(3)])
 Gtan=Q@(Q.T@G); RGS_modes,_=polar(Gtan)
 mesh=build_football_shell()
 W,wdiag=build_geometry_transfer(X,mesh["nodes"],neighbors=a.neighbors)
 transferred=project_shell_tangent(mesh,W@RGS_modes)
 RGS_shell_modes,_=polar(transferred)
 # Shell tangent stiffness eigenproblem.
 _,_,K,mech=solve_discrete_shell(mesh,pressure=0.0)
 qa=build_tangent_quaternion_audit(mesh,K)
 T=qa["tangent_basis"]; Ktan=qa["tangent_stiffness"]
 # Restrict transferred field to local tangent coordinates by least squares.
 shell_coords=T.T@transferred
 shell_coords,_=polar(shell_coords)
 evals,evecs=eigh(Ktan)
 # identify the three lowest modes; report the next gap, not just the match.
 low=evecs[:,:3]
 # compare in ambient tangent coordinates, using the same T embedding.
 low_ambient=T@low
 angle=principal_angle_audit(RGS_shell_modes,low_ambient)
 # Verify expected rotational modes are near-null for the unpinned shell energy.
 rot_res=float(np.linalg.norm(Ktan@shell_coords)/max(np.linalg.norm(Ktan,2)*np.linalg.norm(shell_coords),1e-30))
 # Quaternion lift of three global Cartesian rotation generators.
 qgens=[quaternion_from_matrix(np.eye(3))] # identity gauge reference
 report={"status":"COMPUTED_RGS_ROTATIONAL_TRIPLET_COMPARISON",
 "RGS":{"source":a.source,"X_shape":list(X.shape),"constraint_rank":int(np.linalg.matrix_rank(C)),
 "tangent_basis_shape":list(Q.shape),"tangent_orthogonality":float(np.linalg.norm(Q.T@Q-np.eye(188))),
 "triplet_definition":"infinitesimal rigid rotations omega x X, projected into the exact 188D constraint tangent space",
 "triplet_rank":int(np.linalg.matrix_rank(Gtan))},
 "transfer":{"shape":list(W.shape),"diagnostics":wdiag,"projected_transfer_rank":int(np.linalg.matrix_rank(transferred))},
 "football_shell":{"nodes":int(len(mesh["nodes"])),"ambient_dof":276,"tangent_dof":184,
 "tangent_basis_rank":qa["tangent_basis_rank"],"Ktan_symmetry":float(np.linalg.norm(Ktan-Ktan.T)),
 "lowest_10_eigenvalues":evals[:10].tolist(),"low3_to_next_gap":float(evals[3]-evals[2]),
 "rotational_triplet_residual":rot_res},
 "comparison":{"principal_angles_degrees":angle["principal_angles_degrees"],
 "max_angle_degrees":angle["max_angle_degrees"],"rms_angle_degrees":angle["rms_angle_degrees"]},
 "classification":"geometric rotational triplet comparison; not the T2u mode and not yet a symmetry-protected eigenspace",
 "quaternionic_structure":{"SU2_double_cover":"q and -q represent the same SO(3) rotation",
 "global_generator_quaternion_reference":qgens[0].tolist(),
 "local_node_quaternions":qa["quaternion_frames"]},
 "caveats":["The rotational triplet is defined from geometry, not selected from the unavailable original RGS Hessian.",
 "The shell stiffness is the current linearised CST-plus-hinge model; material parameters are illustrative.",
 "A small principal angle is a geometric/spectral alignment result, not proof of common microscopic physics."]}
 out=Path(a.out);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(report,indent=2)+"\n")
 np.savez_compressed(out.with_suffix(".npz"),Q_RGS=Q,RGS_triplet=RGS_modes,W=W,
 transferred_tangent=transferred,K_shell=K,Ktan=Ktan,shell_eigenvalues=evals,
 shell_low3_eigenvectors=low,principal_angles=np.asarray(angle["principal_angles_degrees"]))
 print(json.dumps({k:v for k,v in report.items() if k!="quaternionic_structure"},indent=2))
if __name__=="__main__": main()
