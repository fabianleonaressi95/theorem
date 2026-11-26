#!/usr/bin/env python3
"""Audit the induced U(1) curvature on the finite RGS/Q6 transverse bundle."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np

I2, I3 = np.eye(2), np.eye(3)
SIGMA = np.array([[[0,1],[1,0]], [[0,-1j],[1j,0]], [[1,0],[0,-1]]], complex)
def fn(a): return float(np.linalg.norm(a, ord="fro"))
def wrap(x): return float(np.angle(np.exp(1j*x)))
def rot2(t): return np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])

def audit(path: Path):
    with np.load(path, allow_pickle=False) as z:
        X=np.asarray(z["X"],float); edges=np.asarray(z["edges"],int)
        R=np.asarray(z["R_SO3"],float); U=np.asarray(z["U_SU2"],complex)
    if X.shape!=(64,3) or edges.shape!=(192,3) or R.shape!=(192,3,3) or U.shape!=(192,2,2):
        raise ValueError("Unexpected archive shapes")
    radii=np.linalg.norm(X,axis=1)
    if np.any(radii<1e-14): raise ValueError("Zero vertex radius")
    n=X/radii[:,None]
    links={}
    for q,(g,h,_) in enumerate(edges):
        links[(int(g),int(h))]=(R[q],U[q])
        links[(int(h),int(g))]=(R[q].T,U[q].conj().T)
    # Right-handed local frame E_g=(u_g,v_g,n_g); its SO(2) gauge is arbitrary.
    E=[]
    for ng in n:
        ref=np.eye(3)[int(np.argmin(np.abs(ng)))]
        u=np.cross(ref,ng); u/=np.linalg.norm(u); v=np.cross(ng,u)
        E.append(np.column_stack((u,v,ng)))
    E=np.asarray(E)
    A={}; edge_orth=[]; edge_off=[]; edge_n=[]
    for (g,h),(Rg,_) in links.items():
        M=E[h].T@Rg@E[g]; A[(g,h)]=M[:2,:2]
        edge_orth.append(fn(M[:2,:2].T@M[:2,:2]-I2))
        edge_off.append(float(np.linalg.norm(M[:2,2])+np.linalg.norm(M[2,:2])+abs(M[2,2]-1)))
        edge_n.append(float(np.linalg.norm(Rg@n[g]-n[h])))
    theta=[]; comm=[]; nfix=[]; edge_match=[]; dc=[]; records=[]
    for a in range(6):
        for b in range(a+1,6):
            for g in range(64):
                if ((g>>a)&1) or ((g>>b)&1): continue
                i=g; j=g^(1<<a); k=j^(1<<b); l=g^(1<<b)
                path=[(i,j),(j,k),(k,l),(l,i)]
                # Column-vector convention: every next link acts on the left.
                H=I3.copy(); Hu=I2.astype(complex); Ah=I2.copy()
                for s,t in path:
                    Rs,Us=links[(s,t)]
                    H=Rs@H; Hu=Us@Hu; Ah=A[(s,t)]@Ah
                Hb=E[i].T@H@E[i]
                ang=float(np.arctan2(Hb[1,0],Hb[0,0]))
                ang_edge=float(np.arctan2(Ah[1,0],Ah[0,0]))
                theta.append(ang); edge_match.append(abs(wrap(ang-ang_edge)))
                nfix.append(float(np.linalg.norm(H@n[i]-n[i])))
                sn=np.einsum("a,aij->ij",n[i],SIGMA)
                comm.append(fn(Hu@sn-sn@Hu))
                ev=np.linalg.eigvals(Hu); phi=float(np.max(np.abs(np.angle(ev))))
                so3=float(np.arccos(np.clip((np.trace(H)-1)/2,-1,1)))
                dc.append(abs(so3-min(2*phi,2*np.pi-2*phi)))
                records.append({"base":i,"axes":[a,b],"theta_rad":ang,"su2_eigenphases_rad":np.angle(ev).tolist()})
    # Random independent local SO(2) frame rotations test A'_gh=G_h^T A_gh G_g.
    rng=np.random.default_rng(20261126); G=np.asarray([rot2(t) for t in rng.uniform(-np.pi,np.pi,64)])
    Eg=np.empty_like(E)
    for g in range(64):
        Eg[g,:,:2]=E[g,:,:2]@G[g]; Eg[g,:,2]=E[g,:,2]
    gauge=[]
    for (g,h),(Rg,_) in links.items():
        got=(Eg[h].T@Rg@Eg[g])[:2,:2]
        gauge.append(fn(got-G[h].T@A[(g,h)]@G[g]))
    th=np.asarray(theta)
    res={
      "plaquette_count":len(th),
      "edge_SO2_orthogonality_max_fro":max(edge_orth),
      "edge_SO2_offblock_max":max(edge_off),
      "edge_normal_transport_max":max(edge_n),
      "plaquette_normal_fix_max":max(nfix),
      "plaquette_SU2_U1_commutator_max_fro":max(comm),
      "plaquette_edge_product_vs_holonomy_max_wrapped_rad":max(edge_match),
      "local_SO2_gauge_covariance_max_fro":max(gauge),
      "SO3_vs_SU2_double_cover_angle_max_abs_rad":max(dc),
      "curvature_angle_min_rad":float(th.min()),"curvature_angle_max_rad":float(th.max()),
      "curvature_angle_mean_rad":float(th.mean()),"curvature_angle_std_rad":float(th.std()),
      "curvature_angle_rms_rad":float(np.sqrt(np.mean(th**2))),
      "curvature_angle_sum_rad":float(th.sum())
    }
    checks={
      "all_240_Q6_square_plaquettes":res["plaquette_count"]==240,
      "edge_reduction_to_SO2":res["edge_SO2_orthogonality_max_fro"]<1e-10 and res["edge_SO2_offblock_max"]<1e-10,
      "radial_section_parallel":res["edge_normal_transport_max"]<1e-10 and res["plaquette_normal_fix_max"]<1e-10,
      "SU2_plaquette_stabilizer_U1":res["plaquette_SU2_U1_commutator_max_fro"]<1e-10,
      "edge_curvature_matches_holonomy":res["plaquette_edge_product_vs_holonomy_max_wrapped_rad"]<1e-10,
      "SO2_gauge_covariance":res["local_SO2_gauge_covariance_max_fro"]<1e-10,
      "SU2_SO3_double_cover":res["SO3_vs_SU2_double_cover_angle_max_abs_rad"]<1e-7
    }
    return {"title":"RGS/Q6 induced U(1) curvature audit","status":"PASS" if all(checks.values()) else "FAIL",
      "classification":"NUMERICAL_VERIFICATION_FINITE_GRAPH_ONLY",
      "connection":"A_gh = E_h^T R_gh E_g restricted to n_g^perp; A_gh in SO(2)",
      "curvature":"Theta_p = Arg(product of oriented SO(2) edge transports)",
      "spin_lift":"SU(2) plaquette eigenphases are the half-angle lift, modulo the central sign",
      "gauge":"E_g -> E_g G_g; A_gh -> G_h^T A_gh G_g; plaquette angle is gauge invariant",
      "residuals":res,"checks":checks,"plaquettes":records,
      "scope":["Finite Q6 transverse rank-2 bundle only.","Principal SO(2) plaquette angles are invariant under independent local frame rotations.",
      "SU(2) comparison uses the double-cover relation and allows the central sign.",
      "No continuum curvature 2-form, continuum manifold, or spacetime interpretation is established."]}

def main():
    p=argparse.ArgumentParser(); p.add_argument("archive",type=Path); p.add_argument("--output",type=Path)
    a=p.parse_args(); r=audit(a.archive); s=json.dumps(r,indent=2,ensure_ascii=False); print(s)
    if a.output: a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(s+"\n",encoding="utf-8")
    if r["status"]!="PASS": raise SystemExit(1)
if __name__=="__main__": main()
