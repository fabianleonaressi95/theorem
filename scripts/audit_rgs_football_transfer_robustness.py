#!/usr/bin/env python3
"""Robustness audit for the RGS rotational triplet -> football shell transfer.

Varies the number of distinct source directions used by the local affine
transfer. Coincident directions at different radii are grouped and their
weights split equally. Quaternion checks are algebraic controls, not evidence
of a shared physical symmetry group.
"""
from __future__ import annotations
from pathlib import Path
import argparse, json, sys
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import numpy as np
from scipy.linalg import null_space,eigh
from models.football_shell import build_football_shell,solve_discrete_shell
from models.football_quaternion_bridge import (
    build_geometry_transfer,project_shell_tangent,principal_angle_audit,
    quaternionic_intertwiner_audit,quaternion_action_matrix)
from models.football_quaternion_tangent import (
    quaternion_from_matrix,qmul,qrotate,build_tangent_quaternion_audit)

def rotation(axis,angle):
    axis=np.asarray(axis,float); axis/=np.linalg.norm(axis)
    x,y,z=axis; c=np.cos(angle); s=np.sin(angle); C=1-c
    return np.array([[c+x*x*C,x*y*C-z*s,x*z*C+y*s],
                     [y*x*C+z*s,c+y*y*C,y*z*C-x*s],
                     [z*x*C-y*s,z*y*C+x*s,c+z*z*C]])

def quaternion_consistency_audit():
    matrices=[rotation([1,0,0],.37),rotation([0,1,0],.51),rotation([0,0,1],.23)]
    quats=[quaternion_from_matrix(R) for R in matrices]
    vectors=np.array([[.3,-.7,.2],[-.4,.1,.8],[.6,.5,-.2]])
    rotate_error=double_error=action_error=0.
    for R,q,v in zip(matrices,quats,vectors):
        rotate_error=max(rotate_error,float(np.linalg.norm(qrotate(q,v)-R@v)))
        double_error=max(double_error,float(np.linalg.norm(qrotate(q,v)-qrotate(-q,v))))
        action_error=max(action_error,float(np.linalg.norm(quaternion_action_matrix(q)-R)))
    composition=float(np.linalg.norm(quaternion_action_matrix(qmul(quats[0],quats[1]))-matrices[0]@matrices[1]))
    inter=quaternionic_intertwiner_audit(matrices,matrices)
    return {"convention":"scalar-first unit quaternions; v -> q(0,v)q^{-1}",
        "rotation_action_max_residual":rotate_error,
        "double_cover_q_vs_minus_q_max_residual":double_error,
        "quaternion_action_matrix_max_residual":action_error,
        "composition_max_residual":composition,
        "abstract_vector_representation_intertwiner":inter,
        "interpretation":"SU(2)->SO(3) consistency and identity-intertwiner calibration only; no common physical symmetry of the RGS point set and football mesh is asserted"}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--source",default="data/rgs_188d/X_Oh_reconstructed.csv")
    p.add_argument("--out",default="reports/rgs_football_transfer_robustness.json")
    p.add_argument("--neighbors",type=int,nargs="+",default=[8,12,16,24,32])
    a=p.parse_args()
    if sorted(set(a.neighbors))!=sorted(a.neighbors): raise ValueError("neighbors must be unique and increasing")
    d=np.genfromtxt(a.source,delimiter=",",names=True)
    X=np.column_stack([d[k] for k in ("x","y","z")])
    C=np.zeros((4,192)); C[0,0::3]=1; C[1,1::3]=1; C[2,2::3]=1; C[3]=X.reshape(-1)
    Q=null_space(C)
    if Q.shape!=(192,188): raise RuntimeError(f"unexpected RGS tangent basis {Q.shape}")
    G=np.column_stack([np.cross(np.broadcast_to(e,(64,3)),X).reshape(-1) for e in np.eye(3)])
    Gtan=Q@(Q.T@G); U,s,_=np.linalg.svd(Gtan,full_matrices=False)
    if np.sum(s>1e-11*s[0])!=3: raise RuntimeError("RGS rotational triplet lost rank")
    RGS_modes=U[:,:3]
    mesh=build_football_shell()
    _,_,K,_=solve_discrete_shell(mesh,pressure=0.)
    qa=build_tangent_quaternion_audit(mesh,K)
    T=qa["tangent_basis"]; Ktan=qa["tangent_stiffness"]
    evals,evecs=eigh(Ktan); low_ambient=T@evecs[:,:3]
    rows=[]; angle_rows=[]
    for k in a.neighbors:
        W,diag=build_geometry_transfer(X,mesh["nodes"],neighbors=k)
        mapped=project_shell_tangent(mesh,W@RGS_modes)
        sv=np.linalg.svd(mapped,compute_uv=False)
        rank=int(np.sum(sv>1e-11*sv[0])) if len(sv) and sv[0]>0 else 0
        if rank!=3: raise RuntimeError(f"transferred triplet rank {rank} for neighbors={k}")
        angles=principal_angle_audit(mapped,low_ambient)
        rows.append({"neighbors":int(k),"transfer_diagnostics":diag,
            "transferred_triplet_rank":rank,
            "principal_angles_degrees":angles["principal_angles_degrees"],
            "max_angle_degrees":angles["max_angle_degrees"],
            "rms_angle_degrees":angles["rms_angle_degrees"],
            "transferred_singular_values":sv.tolist()})
        angle_rows.append(angles["principal_angles_degrees"])
    all_angles=np.asarray(angle_rows)
    report={"status":"COMPUTED_TRANSFER_ROBUSTNESS_AUDIT",
        "source":{"path":a.source,"points":int(len(X)),
            "constraint_rank":int(np.linalg.matrix_rank(C)),
            "tangent_basis_shape":list(Q.shape),
            "tangent_orthogonality":float(np.linalg.norm(Q.T@Q-np.eye(188))),
            "rotational_triplet_rank":int(np.linalg.matrix_rank(Gtan))},
        "football_shell":{"nodes":int(len(mesh["nodes"])),"tangent_dof":int(T.shape[1]),
            "tangent_basis_rank":int(qa["tangent_basis_rank"]),
            "lowest_4_eigenvalues":evals[:4].tolist(),
            "low3_to_next_gap":float(evals[3]-evals[2])},
        "robustness_grid":rows,
        "stability":{"per_mode_max_angle_spread_degrees":np.ptp(all_angles,axis=0).tolist(),
            "max_angle_spread_degrees":float(np.max(np.ptp(all_angles,axis=0))),
            "rms_angle_change_from_first_grid_point_degrees":float(np.sqrt(np.mean((all_angles-all_angles[0])**2))),
            "interpretation":"sensitivity across the declared neighbor grid; not a convergence proof"},
        "quaternionic_audit":quaternion_consistency_audit(),
        "classification":"numerical robustness of a geometry-based triplet transfer; not proof of common microscopic dynamics or a symmetry-protected eigenspace",
        "limitations":[
            "The source has coincident unit directions at distinct radii; directions are grouped and weights split equally while the original 64-coordinate source triplet is retained.",
            "The local affine transfer is not a symmetry intertwiner and does not preserve an unknown RGS stiffness energy automatically.",
            "The quaternionic intertwiner is an abstract vector-representation calibration, not an independently established action on shell nodes.",
            "The shell stiffness is the illustrative linearised CST-plus-hinge model; material identification and experimental validation remain open."]}
    out=Path(a.out); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,indent=2)+"\n")
    np.savez_compressed(out.with_suffix(".npz"),neighbor_grid=np.asarray(a.neighbors),
        principal_angles_degrees=all_angles,shell_eigenvalues=evals,
        source_tangent_basis=Q,source_rotational_triplet=RGS_modes)
    print(json.dumps(report,indent=2))

if __name__=="__main__": main()
