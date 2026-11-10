#!/usr/bin/env python3
"""Project membrane, panel-hinge and physical-seam stiffness onto the transferred RGS rotation triplet."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
import numpy as np
from scipy.linalg import null_space, eigh

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from models.football_shell import build_football_shell, solve_discrete_shell
from models.football_quaternion_bridge import build_geometry_transfer, project_shell_tangent
from models.football_quaternion_tangent import build_tangent_quaternion_audit

def orth(A,tol=1e-11):
    U,s,_=np.linalg.svd(A,full_matrices=False)
    return U[:,:int(np.sum(s>tol*s[0]))],s

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--source",default="data/rgs_188d/X_Oh_reconstructed.csv")
    p.add_argument("--out",default="reports/morandotti_triplet_energy_projection.json")
    p.add_argument("--neighbors",type=int,default=16)
    p.add_argument("--E1",type=float,default=1000.)
    p.add_argument("--E2",type=float,default=700.)
    p.add_argument("--nu12",type=float,default=.25)
    p.add_argument("--G12",type=float,default=300.)
    p.add_argument("--thickness",type=float,default=.02)
    p.add_argument("--seam-Et",type=float,default=0.)
    p.add_argument("--seam-bending-factor",type=float,default=4.)
    p.add_argument("--material-angle",type=float,default=0.)
    a=p.parse_args()
    dat=np.genfromtxt(ROOT/a.source,delimiter=",",names=True)
    X=np.column_stack([dat[k] for k in ("x","y","z")])
    C=np.zeros((4,192)); C[0,0::3]=1; C[1,1::3]=1; C[2,2::3]=1; C[3]=X.reshape(-1)
    Q=null_space(C)
    G=np.column_stack([np.cross(np.broadcast_to(e,(64,3)),X).reshape(-1) for e in np.eye(3)])
    Urot,_=orth(Q@(Q.T@G))
    mesh=build_football_shell()
    W,wdiag=build_geometry_transfer(X,mesh["nodes"],neighbors=a.neighbors)
    Uambient=project_shell_tangent(mesh,W@Urot)
    Uambient,_=orth(Uambient)
    if Uambient.shape[1]!=3: raise RuntimeError("transferred rotational triplet lost rank")
    # Node-wise quaternion frames define the 276 x 184 tangent embedding.
    _,_,Kfull0,_=solve_discrete_shell(mesh,pressure=0.,thickness=a.thickness,E1=a.E1,E2=a.E2,
        nu12=a.nu12,G12=a.G12,material_angle=a.material_angle,seam_Et=0.,
        seam_bending_factor=a.seam_bending_factor,panel_hinge_factor=1.)
    qa=build_tangent_quaternion_audit(mesh,Kfull0)
    T=qa["tangent_basis"]
    Bcoord,_=orth(T.T@Uambient)
    B=T@Bcoord
    # Exact additive ablation of the assembled stiffness terms.
    # The membrane-only shell has out-of-plane mechanisms. Keep a small positive
    # reference factor on both edge families, then remove it algebraically.
    eps=1e-3
    _,_,Keps,_=solve_discrete_shell(mesh,pressure=0.,thickness=a.thickness,E1=a.E1,E2=a.E2,
        nu12=a.nu12,G12=a.G12,material_angle=a.material_angle,seam_Et=0.,
        seam_bending_factor=eps,panel_hinge_factor=eps)
    _,_,Kpanel_ref,_=solve_discrete_shell(mesh,pressure=0.,thickness=a.thickness,E1=a.E1,E2=a.E2,
        nu12=a.nu12,G12=a.G12,material_angle=a.material_angle,seam_Et=0.,
        seam_bending_factor=eps,panel_hinge_factor=1.)
    Kpanel=(Kpanel_ref-Keps)/(1.-eps)
    _,_,Kwith_seam,_=solve_discrete_shell(mesh,pressure=0.,thickness=a.thickness,E1=a.E1,E2=a.E2,
        nu12=a.nu12,G12=a.G12,material_angle=a.material_angle,seam_Et=0.,
        seam_bending_factor=a.seam_bending_factor,panel_hinge_factor=1.)
    Kseam_hinge=(Kwith_seam-Kpanel_ref)/(a.seam_bending_factor-eps) if abs(a.seam_bending_factor-eps)>1e-14 else np.zeros_like(Keps)
    Kmem=Keps-eps*Kpanel-eps*Kseam_hinge
    Kseam_line=np.zeros_like(Kmem)
    if a.seam_Et:
        _,_,Kline,_=solve_discrete_shell(mesh,pressure=0.,thickness=a.thickness,E1=a.E1,E2=a.E2,
            nu12=a.nu12,G12=a.G12,material_angle=a.material_angle,seam_Et=a.seam_Et,
            seam_bending_factor=a.seam_bending_factor,panel_hinge_factor=1.)
        Kseam_line=Kline-Kwith_seam
    components={"membrane":Kmem,"panel_hinges":Kpanel,"seam_hinge_increment":a.seam_bending_factor*Kseam_hinge,
        "seam_line_reinforcement":Kseam_line}
    Ksum=sum(components.values())
    reconstruction=float(np.linalg.norm(Ksum-(Kwith_seam+Kseam_line))/max(np.linalg.norm(Kwith_seam+Kseam_line),1e-30))
    Ktan_total=T.T@(Kwith_seam+Kseam_line)@T
    eigvals,eigvecs=eigh(.5*(Ktan_total+Ktan_total.T))
    # Compare the transferred RGS rotation subspace with the lowest three shell tangent modes.
    low=eigvecs[:,:3]
    s=np.linalg.svd(Bcoord.T@low,compute_uv=False)
    angles=np.degrees(np.arccos(np.clip(s,-1.,1.)))
    projected={}
    for name,Ki in components.items():
        M=.5*(B.T@Ki@B+(B.T@Ki@B).T)
        projected[name]={"matrix_3x3":M.tolist(),"eigenvalues":np.linalg.eigvalsh(M).tolist(),
            "trace":float(np.trace(M)),"frobenius_norm":float(np.linalg.norm(M,"fro"))}
    total_trace=sum(v["trace"] for v in projected.values())
    for v in projected.values(): v["trace_fraction"]=v["trace"]/total_trace if abs(total_trace)>1e-30 else None
    report={"status":"COMPUTED_TRIPLET_ENERGY_ABLATION",
        "source":{"sites":64,"ambient_dof":192,"constraint_rank":int(np.linalg.matrix_rank(C)),
            "tangent_dof":int(Q.shape[1]),"rotation_triplet_rank":int(Urot.shape[1])},
        "shell":{"nodes":len(mesh["nodes"]),"ambient_dof":276,"node_tangent_dof":184,
            "tangent_basis_shape":list(T.shape),"tangent_stiffness_shape":list(qa["tangent_stiffness"].shape)},
        "transfer":{"neighbors_distinct_directions":a.neighbors,"matrix_shape":list(W.shape),
            "diagnostics":wdiag,"transferred_rank":int(Uambient.shape[1])},
        "comparison":{"principal_angles_degrees":angles.tolist(),"max_angle_degrees":float(np.max(angles)),
            "low3_to_next_eigenvalue_gap":float(eigvals[3]-eigvals[2]),
            "lowest_four_eigenvalues":eigvals[:4].tolist()},
        "material_parameters":{"E1":a.E1,"E2":a.E2,"nu12":a.nu12,"G12":a.G12,
            "thickness":a.thickness,"material_angle":a.material_angle,
            "seam_Et":a.seam_Et,"seam_bending_factor":a.seam_bending_factor},
        "triplet_energy_projection":projected,
        "stiffness_additive_reconstruction_relative_residual":reconstruction,
        "classification":"energy contributions projected onto the transferred geometric RGS rotation subspace; not a T2u identification or experimental validation",
        "caveats":["The shell model is linearised CST membrane plus signed-dihedral hinges.",
            "Material constants are illustrative unless replaced by measured coupon data.",
            "The transferred subspace is geometric; its basis orientation is arbitrary, so interpret its 3x3 spectrum and trace invariants, not individual basis columns.",
            "Ablation separates terms in this implemented stiffness, not all physical mechanisms in a real ball."]}
    out=ROOT/a.out; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(report,indent=2)+"\\n")
    np.savez_compressed(out.with_suffix(".npz"),B_ambient=B,B_coordinates=Bcoord,T=T,
        K_membrane=Kmem,K_panel_hinges=Kpanel,K_seam_hinges=Kseam_hinge,
        K_seam_line=Kseam_line,principal_angles_degrees=angles,eigenvalues=eigvals)
    print(json.dumps({"status":report["status"],"principal_angles_degrees":angles.tolist(),
        "low3_to_next_eigenvalue_gap":report["comparison"]["low3_to_next_eigenvalue_gap"],
        "energy_projection":{k:{"eigenvalues":v["eigenvalues"],"trace_fraction":v["trace_fraction"]}
            for k,v in projected.items()},"reconstruction_residual":reconstruction},indent=2))
if __name__=="__main__": main()
