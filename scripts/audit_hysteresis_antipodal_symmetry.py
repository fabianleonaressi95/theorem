#!/usr/bin/env python3
"""Measure central-inversion defect of exported measured J-H loops.

The involution is a candidate Anti-Twin symmetry test, not evidence for the
RGS/Anti-Twin model. Minor field reversals are handled by sorting each branch
by H and averaging duplicate H values before interpolation.
"""
import argparse,json
from pathlib import Path
import numpy as np
import pandas as pd

def antipodal_defect(H,J,n_grid=500):
    H=np.asarray(H,float); J=np.asarray(J,float)
    if len(H)<12 or len(H)!=len(J) or not np.isfinite(H).all() or not np.isfinite(J).all():
        return {"status":"INVALID_INPUT"}
    imin=int(np.argmin(H))
    Hd,Jd=H[:imin+1][::-1],J[:imin+1][::-1]
    Ha,Ja=H[imin:],J[imin:]
    def sorted_branch(x,y):
        order=np.argsort(x); x=np.asarray(x)[order]; y=np.asarray(y)[order]
        unique,inv=np.unique(x,return_inverse=True)
        return unique,np.bincount(inv,weights=y)/np.bincount(inv)
    Hd,Jd=sorted_branch(Hd,Jd); Ha,Ja=sorted_branch(Ha,Ja)
    if len(Hd)<3 or len(Ha)<3: return {"status":"INSUFFICIENT_BRANCH_POINTS"}
    lo=max(float(Hd.min()),float(Ha.min()),-float(Hd.max()),-float(Ha.max()))
    hi=min(float(Hd.max()),float(Ha.max()),-float(Hd.min()),-float(Ha.min()))
    if hi<=lo: return {"status":"NO_SYMMETRIC_FIELD_OVERLAP"}
    h=np.linspace(lo,hi,n_grid)
    # Candidate central inversion: J_desc(H) + J_asc(-H) = 0.
    defect=np.interp(h,Hd,Jd)+np.interp(-h,Ha,Ja)
    rms=float(np.sqrt(np.mean(defect**2))); span=float(np.ptp(J))
    return {"status":"COMPUTED","field_overlap_kA_m":[lo,hi],"grid_points":int(n_grid),
            "antipodal_defect_rms_mT":rms,"antipodal_defect_mean_mT":float(np.mean(defect)),
            "J_peak_to_peak_mT":span,"antipodal_defect_nrmse_percent":100*rms/max(span,1e-12),
            "interpretation":"Descriptive central-inversion defect; no pass/fail threshold without repeated-loop and instrument uncertainty estimates."}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("curves",type=Path)
    ap.add_argument("--out",type=Path,default=Path("antipodal_symmetry.json")); a=ap.parse_args()
    df=pd.read_csv(a.curves)
    out={"definition":"RMS of J_desc(H)+J_asc(-H) on the common symmetric field interval","sheets":{}}
    for name,g in df.groupby("sheet"):
        g=g.sort_values("point"); out["sheets"][str(name)]=antipodal_defect(g.H_kA_m,g.J_mT)
    a.out.parent.mkdir(parents=True,exist_ok=True); a.out.write_text(json.dumps(out,indent=2,allow_nan=False)+"\n")
    print(json.dumps({k:{"rms_mT":v.get("antipodal_defect_rms_mT"),"nrmse_percent":v.get("antipodal_defect_nrmse_percent"),"status":v.get("status")} for k,v in out["sheets"].items()},indent=2))
if __name__=="__main__": main()
