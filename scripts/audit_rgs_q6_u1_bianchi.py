#!/usr/bin/env python3
"""Discrete U(1) Bianchi and integer cube-charge audit for RGS/Q6."""
from __future__ import annotations
import argparse, json
from collections import Counter
from pathlib import Path
import numpy as np

def wrap(x): return float(np.angle(np.exp(1j*x)))

def audit(path: Path):
    with np.load(path, allow_pickle=False) as z:
        X=np.asarray(z["X"],float); edges=np.asarray(z["edges"],int); R=np.asarray(z["R_SO3"],float)
    if X.shape!=(64,3) or edges.shape!=(192,3) or R.shape!=(192,3,3):
        raise ValueError("Unexpected Q6 archive shapes")
    n=X/np.linalg.norm(X,axis=1)[:,None]
    links={}
    for q,(g,h,_) in enumerate(edges):
        g=int(g);h=int(h);links[g,h]=R[q];links[h,g]=R[q].T
    E=[]
    for ng in n:
        ref=np.eye(3)[int(np.argmin(np.abs(ng)))]
        u=np.cross(ref,ng);u/=np.linalg.norm(u);v=np.cross(ng,u)
        E.append(np.column_stack((u,v,ng)))
    E=np.asarray(E)
    A={(g,h):(E[h].T@Rg@E[g])[:2,:2] for (g,h),Rg in links.items()}
    # Positive (a,b) face orientation: +a,+b,-a,-b.
    face={}
    for a in range(6):
      for b in range(a+1,6):
       for g in range(64):
        if (g>>a)&1 or (g>>b)&1: continue
        j=g^(1<<a); k=j^(1<<b); l=g^(1<<b)
        H=A[l,g]@A[k,l]@A[j,k]@A[g,j]
        face[g,a,b]=float(np.arctan2(H[1,0],H[0,0]))
    cubes=[]; charge={}
    for a in range(6):
     for b in range(a+1,6):
      for c in range(b+1,6):
       for g in range(64):
        if any((g>>q)&1 for q in (a,b,c)): continue
        ga=g^(1<<a);gb=g^(1<<b);gc=g^(1<<c)
        s=(face[ga,b,c]-face[g,b,c]-face[gb,a,c]+face[g,a,c]
           +face[gc,a,b]-face[g,a,b])
        m=int(round(s/(2*np.pi)))
        if abs(s-2*np.pi*m)>1e-8: raise ArithmeticError("Cube boundary not quantized in 2pi units")
        charge[g,a,b,c]=m
        cubes.append({"base_vertex":g,"axes":[a,b,c],"oriented_angle_sum_rad":float(s),
          "wrapped_bianchi_residual_rad":wrap(s),"integer_cube_charge":m})
    four=[]
    for a in range(6):
     for b in range(a+1,6):
      for c in range(b+1,6):
       for d in range(c+1,6):
        for g in range(64):
         if any((g>>q)&1 for q in (a,b,c,d)): continue
         ga=g^(1<<a);gb=g^(1<<b);gc=g^(1<<c);gd=g^(1<<d)
         dm=(charge[ga,b,c,d]-charge[g,b,c,d]-charge[gb,a,c,d]+charge[g,a,c,d]
             +charge[gc,a,b,d]-charge[g,a,b,d]-charge[gd,a,b,c]+charge[g,a,b,c])
         four.append({"base_vertex":g,"axes":[a,b,c,d],"integer_charge_boundary":int(dm)})
    vals=np.asarray([x["oriented_angle_sum_rad"] for x in cubes])
    wrapped=np.asarray([x["wrapped_bianchi_residual_rad"] for x in cubes])
    hist=Counter(charge.values())
    res={"cube_count":len(cubes),"four_cell_count":len(four),
      "max_abs_wrapped_bianchi_residual_rad":float(np.max(np.abs(wrapped))),
      "max_abs_quantization_error_rad":float(np.max(np.abs(vals-2*np.pi*np.rint(vals/(2*np.pi))))),
      "max_abs_four_cell_integer_boundary":max(abs(x["integer_charge_boundary"]) for x in four),
      "nonzero_four_cell_boundaries":sum(x["integer_charge_boundary"]!=0 for x in four),
      "cube_charge_histogram":{str(k):int(hist.get(k,0)) for k in (-2,-1,0,1,2)},
      "nonzero_cube_charges":sum(v!=0 for v in charge.values()),
      "oriented_angle_sum_min_rad":float(vals.min()),"oriented_angle_sum_max_rad":float(vals.max()),
      "oriented_angle_sum_rms_rad":float(np.sqrt(np.mean(vals**2))),
      "total_integer_cube_charge":int(sum(charge.values()))}
    checks={"all_160_cube_bianchi_identities_mod_2pi":len(cubes)==160 and res["max_abs_wrapped_bianchi_residual_rad"]<1e-10,
      "cube_defects_quantized_in_2pi":res["max_abs_quantization_error_rad"]<1e-10,
      "integer_defect_current_closed_on_all_60_four_cells":len(four)==60 and res["max_abs_four_cell_integer_boundary"]==0}
    return {"title":"RGS/Q6 discrete U(1) Bianchi audit","status":"PASS" if all(checks.values()) else "FAIL",
      "classification":"NUMERICAL_VERIFICATION_FINITE_CUBICAL_COMPLEX",
      "conventions":{"face_orientation":"positive (a,b): +a,+b,-a,-b",
       "cube_boundary":"dF = Delta_a F_bc - Delta_b F_ac + Delta_c F_ab",
       "cube_integer_charge":"m = oriented sum of principal plaquette angles divided by 2pi",
       "warning":"A nonzero integer charge is a compact-angle/branch defect candidate, not by itself a physical monopole."},
      "residuals":res,"checks":checks,"cube_records":cubes,"four_cell_records":four,
      "interpretation":["The compact U(1) Bianchi identity holds on every 3-cube modulo 2pi.",
       "Principal plaquette angles produce nonzero integer cube charges on some cubes because of the principal branch.",
       "These integer charges form a closed integer cochain: their oriented boundary vanishes on every 4-cube.",
       "No continuum magnetic monopole, continuum Bianchi equation, or physical source is established."]}

def main():
    p=argparse.ArgumentParser();p.add_argument("archive",type=Path);p.add_argument("--output",type=Path);a=p.parse_args()
    r=audit(a.archive);s=json.dumps(r,indent=2,ensure_ascii=False);print(s)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(s+"\n",encoding="utf-8")
    if r["status"]!="PASS":raise SystemExit(1)
if __name__=="__main__":main()
