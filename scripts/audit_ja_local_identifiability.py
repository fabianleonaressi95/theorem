#!/usr/bin/env python3
"""Local identifiability diagnostic for archived single-loop JA calibrations.

Consumes the JSON and point CSV emitted by audit_hysteresis_dataset.py.
It does not refit parameters or claim global/practical identifiability.
"""
import argparse, json
from pathlib import Path
import numpy as np
import pandas as pd

MU0_MILLI_T_PER_KA_M = 4*np.pi*1e-7*1e6
NAMES = ["Ms_kA_m", "a_kA_m", "alpha", "c", "k_kA_m"]

def simulate(H, p, M0):
    Ms,a,alpha,c,k = map(float,p); H=np.asarray(H,float); M=np.empty(len(H)); M[0]=M0
    def d(h,m,direction):
        z=(h+alpha*m)/a
        if abs(z)<1e-5: man=Ms*z/3; dm=Ms/(3*a)
        else:
            man=Ms*(1/np.tanh(z)-1/z)
            dm=(Ms/a)*(1/(z*z)-1/(np.sinh(z)**2))
        delta=1. if direction>=0 else -1.
        den=delta*k-alpha*(man-m)
        if abs(den)<1e-12: den=np.copysign(1e-12,den if den else 1.)
        q=c*dm+(1-c)*(man-m)/den
        den=1-alpha*q
        return q/den if abs(den)>1e-12 else np.nan
    for i in range(1,len(H)):
        dh=H[i]-H[i-1]
        if dh==0: M[i]=M[i-1]; continue
        h,m=H[i-1],M[i-1]
        k1=dh*d(h,m,dh); k2=dh*d(h+dh/2,m+k1/2,dh)
        k3=dh*d(h+dh/2,m+k2/2,dh); k4=dh*d(h+dh,m+k3,dh)
        M[i]=m+(k1+2*k2+2*k3+k4)/6
        if not np.isfinite(M[i]): return np.full(len(H),np.nan)
    return M

def jacobian(fun,x,rel=2e-5):
    x=np.asarray(x,float); J=np.empty((len(fun(x)),len(x)))
    for j in range(len(x)):
        h=rel*max(1.,abs(x[j])); xp=x.copy(); xm=x.copy()
        xp[j]+=h; xm[j]-=h; J[:,j]=(fun(xp)-fun(xm))/(2*h)
    return J

def audit(sheet, df, sr):
    fit=sr.get("JA_SINGLE_LOOP_CALIBRATION")
    if not fit or fit.get("status")!="IN_SAMPLE_CALIBRATION_ONLY":
        return {"status":"NOT_APPLICABLE"}
    df=df.sort_values("point"); H=df.H_kA_m.to_numpy(float)
    obs=df.J_mT.to_numpy(float)/MU0_MILLI_T_PER_KA_M
    p=np.array([fit["parameters"][n] for n in NAMES])
    hs=max(float(np.ptp(H)),1e-6); ms=max(float(np.max(np.abs(obs))),1e-3)
    lo=np.array([.2*ms,1e-4*hs,0,0,1e-4*hs])
    hi=np.array([4*ms,2*hs,.05,.95,2*hs])
    scale=np.array([max(p[0],1),max(p[1],1),.01,max(p[3],.1),max(p[4],1)])
    z=p/scale
    def residual(v):
        pred=simulate(H,v*scale,obs[0])
        return (pred-obs)/max(float(np.ptp(obs)),1e-6) if np.isfinite(pred).all() else np.full(len(H),1e6)
    J=jacobian(residual,z); s=np.linalg.svd(J,compute_uv=False)
    rank=int(np.sum(s>s[0]*1e-8)); cond=float(s[0]/s[-1]) if s[-1]>0 else None
    hits=[]
    for n,v,l,u in zip(NAMES,p,lo,hi):
        rel=min(v-l,u-v)/max(u-l,1e-30)
        if rel<.01: hits.append({"parameter":n,"bound":"lower" if v-l<=u-v else "upper","relative_distance":float(rel)})
    t=df.t_s.to_numpy(float) if "t_s" in df else np.array([])
    timing={}
    if len(t)>1 and np.isfinite(t).all():
        dt=np.diff(t); duration=float(t[-1]-t[0])
        timing={"duration_s":duration,"median_dt_s":float(np.median(dt)),
                "dt_cv":float(np.std(dt)/np.mean(dt)),"inverse_duration_hz":1/duration,
                "frequency_status":"derived from extracted max-to-max duration; not source-documented"}
    return {"status":"LOCAL_DIAGNOSTIC_ONLY","n_points":len(H),"rank":rank,
            "condition_number":cond,"singular_values":s.tolist(),"bound_hits":hits,
            "time_sampling":timing,
            "interpretation":"Full local numerical rank does not establish practical or physical identifiability; conditioning and active bounds remain decisive warnings."}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("report",type=Path); ap.add_argument("curves",type=Path)
    ap.add_argument("--out",type=Path,default=Path("ja_identifiability.json")); a=ap.parse_args()
    report=json.loads(a.report.read_text()); curves=pd.read_csv(a.curves)
    out={"method":"dimensionless central finite-difference residual Jacobian at archived in-sample JA optimum","sheets":{}}
    for name,sr in report["sheets"].items():
        if name=="Results": continue
        sub=curves[curves.sheet==name]
        out["sheets"][name]=audit(name,sub,sr) if len(sub) else {"status":"MISSING_CURVE"}
    a.out.parent.mkdir(parents=True,exist_ok=True); a.out.write_text(json.dumps(out,indent=2,allow_nan=False)+"\n")
    print(json.dumps({k:{"rank":v.get("rank"),"condition_number":v.get("condition_number"),"bound_hits":v.get("bound_hits")} for k,v in out["sheets"].items()},indent=2))
if __name__=="__main__": main()
