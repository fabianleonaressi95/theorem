#!/usr/bin/env python3
"""Reproducible audit of the Zenodo magnetic-powder hysteresis workbook.

The script deliberately refuses to invent cycle labels, units, frequencies, or
Bertotti inputs. It inventories every sheet, detects the documented H/J/B/t
schema, segments cycles from field reversals, exports loop metrics and a JSON
report. Jiles-Atherton fitting is only enabled for sheets with unambiguous
columns and at least two complete cycles; validation holds out whole cycles.
"""
from __future__ import annotations
import argparse, hashlib, json, re, sys
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import least_squares
from scipy.signal import find_peaks

MU0 = 4*np.pi*1e-7
MU0_MILLI_T_PER_KA_M = MU0*1e6  # 1.256637... mT per kA/m

ALIASES = {
    "H": ["H [kA/m]", "H (kA/m)", "H_kA_m", "H"],
    "J": ["J [mT]", "J (mT)", "J_mT", "J"],
    "B": ["B [mT]", "B (mT)", "B_mT", "B"],
    "t": ["t [s]", "t (s)", "time [s]", "time_s", "t"],
    "f": ["f [Hz]", "frequency [Hz]", "frequency_hz", "f"],
}

def colmap(df):
    norm = {str(c).strip().lower(): c for c in df.columns}
    out = {}
    for key, names in ALIASES.items():
        for n in names:
            if n.lower() in norm:
                out[key] = norm[n.lower()]
                break
    return out

def finite_runs(df, cm):
    required = [k for k in ("H", "J", "B") if k in cm]
    if len(required) < 2:
        return []
    x = df[[cm[k] for k in required]].apply(pd.to_numeric, errors="coerce")
    good = np.isfinite(x.to_numpy()).all(axis=1)
    ids = np.flatnonzero(good)
    if len(ids) == 0: return []
    # Keep contiguous finite runs; never bridge missing samples.
    cuts = np.where(np.diff(ids) > 1)[0] + 1
    return [z for z in np.split(ids, cuts) if len(z) >= 12]

def segment_cycles(h):
    """Return full max-to-max cycles, including a measured cycle whose
    positive-field maximum lies at the first or last recorded sample."""
    h = np.asarray(h, float)
    if len(h) < 12: return []
    span = np.ptp(h)
    if not np.isfinite(span) or span <= 0: return []
    distance = max(3, len(h)//300)
    prom = max(span*0.005, np.finfo(float).eps)
    peaks, _ = find_peaks(h, distance=distance, prominence=prom)
    maxima = list(map(int, peaks))
    # scipy.find_peaks intentionally excludes endpoints. Magnetometer exports
    # often start/end at the positive-field turning point, so retain those
    # boundaries only when they are genuine one-sided maxima near the global
    # maximum (within 2% of the full field span).
    edge_tol = 0.02*span
    if h[0] >= h[1] and h[0] >= np.max(h)-edge_tol:
        maxima.append(0)
    if h[-1] >= h[-2] and h[-1] >= np.max(h)-edge_tol:
        maxima.append(len(h)-1)
    maxima = np.array(sorted(set(maxima)), dtype=int)
    cycles = []
    for a,b in zip(maxima[:-1], maxima[1:]):
        if b-a >= 12:
            seg = np.arange(a,b+1)
            if np.ptp(h[seg]) >= 0.5*span:
                cycles.append(seg)
    return cycles

def ja_simulate(H, p, M0):
    """Implicit differential Jiles-Atherton integration, RK4 in H."""
    Ms, a, alpha, c, k = p
    H = np.asarray(H, float)
    M = np.empty(len(H)); M[0] = M0
    def deriv(h, m, direction):
        he = h + alpha*m
        z = he/a
        if abs(z) < 1e-5:
            man = Ms*z/3
            dman = Ms/(3*a)
        else:
            coth = 1/np.tanh(z)
            man = Ms*(coth - 1/z)
            dman = (Ms/a)*(1/(z*z) - 1/(np.sinh(z)**2))
        delta = 1.0 if direction >= 0 else -1.0
        irr_den = delta*k - alpha*(man-m)
        if abs(irr_den) < 1e-12: irr_den = np.copysign(1e-12, irr_den or 1)
        irr = (man-m)/irr_den
        q = c*dman + (1-c)*irr
        den = 1-alpha*q
        return q/den if abs(den)>1e-12 else np.nan
    for i in range(1,len(H)):
        dh=H[i]-H[i-1]
        if dh == 0: M[i]=M[i-1]; continue
        h0,m0=H[i-1],M[i-1]; d=dh
        k1=d*deriv(h0,m0,d)
        k2=d*deriv(h0+d/2,m0+k1/2,d)
        k3=d*deriv(h0+d/2,m0+k2/2,d)
        k4=d*deriv(h0+d,m0+k3,d)
        M[i]=m0+(k1+2*k2+2*k3+k4)/6
        if not np.isfinite(M[i]): return np.full(len(H),np.nan)
    return M

def fit_ja(H, J_mT, max_nfev=250):
    # Convert polarization J [mT] to magnetization M [kA/m].
    Mobs = np.asarray(J_mT,float)/MU0_MILLI_T_PER_KA_M
    hspan=max(float(np.ptp(H)),1e-6)
    mscale=max(float(np.nanmax(np.abs(Mobs))),1e-3)
    # Optimize scaled parameters to improve conditioning.
    x0=np.array([1.15*mscale, .12*hspan, 1e-4, .15, .08*hspan])
    lo=np.array([.2*mscale, 1e-4*hspan, 0, 0, 1e-4*hspan])
    hi=np.array([4*mscale, 2*hspan, .05, .95, 2*hspan])
    def residual(x):
        pred=ja_simulate(H,x,Mobs[0])
        if not np.all(np.isfinite(pred)): return np.full(len(H),1e6)
        return (pred-Mobs)/mscale
    res=least_squares(residual,x0,bounds=(lo,hi),max_nfev=max_nfev,
                      loss="soft_l1",f_scale=.03)
    pred=ja_simulate(H,res.x,Mobs[0])
    rmse=float(np.sqrt(np.mean((pred-Mobs)**2)))
    nrmse=rmse/max(float(np.ptp(Mobs)),1e-12)
    return res.x, pred, {"success":bool(res.success),"message":res.message,
        "rmse_kA_m":rmse,"nrmse_percent":100*nrmse,"cost":float(res.cost)}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("workbook",nargs="?",default="Hysteresis_datasets.xlsx")
    ap.add_argument("--out",default="hysteresis_audit")
    args=ap.parse_args()
    path=Path(args.workbook)
    if not path.is_file(): raise FileNotFoundError(path)
    out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
    raw=path.read_bytes()
    report={"file":path.name,"size_bytes":len(raw),
            "md5":hashlib.md5(raw).hexdigest(),"sheets":{},
            "physical_model":{"mu0_mT_per_kA_m":MU0_MILLI_T_PER_KA_M},
            "bertotti":{"status":"NOT_FIT","reason":
                "Requires independently documented frequency, density, conductivity, geometry/thickness and waveform; no values are inferred."}}
    xls=pd.ExcelFile(path)
    report["sheet_names"]=xls.sheet_names
    curves=[]
    for sheet in xls.sheet_names:
        df=pd.read_excel(path,sheet_name=sheet)
        cm=colmap(df)
        info={"rows":int(len(df)),"columns":[str(c) for c in df.columns],
              "dtypes":{str(c):str(t) for c,t in df.dtypes.items()},
              "missing_by_column":{str(k):int(v) for k,v in df.isna().sum().items()},
              "duplicate_rows":int(df.duplicated().sum()),"recognized_columns":cm}
        if all(k in cm for k in ("H","J","B")):
            H=pd.to_numeric(df[cm["H"]],errors="coerce").to_numpy(float)
            J=pd.to_numeric(df[cm["J"]],errors="coerce").to_numpy(float)
            B=pd.to_numeric(df[cm["B"]],errors="coerce").to_numpy(float)
            valid=np.isfinite(H)&np.isfinite(J)&np.isfinite(B)
            err=B-(J+MU0_MILLI_T_PER_KA_M*H)
            info["B_equals_J_plus_mu0H"]={
                "valid_samples":int(valid.sum()),
                "max_abs_error_mT":float(np.max(np.abs(err[valid]))) if valid.any() else None,
                "rmse_mT":float(np.sqrt(np.mean(err[valid]**2))) if valid.any() else None}
            info["ranges"]={"H": [float(np.nanmin(H)),float(np.nanmax(H))],
                            "J_mT":[float(np.nanmin(J)),float(np.nanmax(J))],
                            "B_mT":[float(np.nanmin(B)),float(np.nanmax(B))]}
            if "t" in cm:
                t=pd.to_numeric(df[cm["t"]],errors="coerce").to_numpy(float)
                info["time_s"]={"min":float(np.nanmin(t)),"max":float(np.nanmax(t)),
                                "monotonic_increasing":bool(np.all(np.diff(t[np.isfinite(t)])>=0))}
            else: t=None
            segs=[]
            for run in finite_runs(df,cm):
                local=segment_cycles(H[run])
                segs.extend([run[s] for s in local])
            info["complete_max_to_max_cycles_detected"]=len(segs)
            info["cycle_segmentation"]="successive positive H maxima; full cycles only"
            for ci,idx in enumerate(segs):
                hh,jj,bb=H[idx],J[idx],B[idx]
                # ∮ H dB: kA/m * mT = J/m3 numerically.
                area=float(abs(np.trapezoid(hh,bb)))
                tt = (pd.to_numeric(df[cm["t"]],errors="coerce").to_numpy(float)[idx]
                      if "t" in cm else None)
                duration = (float(tt[-1]-tt[0]) if tt is not None and
                            np.all(np.isfinite(tt)) and tt[-1]>tt[0] else None)
                curves.append({"sheet":sheet,"cycle":ci+1,"n":len(idx),
                    "H":hh,"J":jj,"B":bb,"t":tt,"duration_s":duration,
                    "frequency_hz":(1.0/duration if duration else None),
                    "area_J_m3":area})
        else:
            info["analysis_status"]="Required H/J/B columns not unambiguously identified; no physical fit attempted."
        report["sheets"][sheet]=info

    # Cycle-level data export and true leave-one-cycle-out fitting.
    cycle_rows=[]
    curve_points=[]
    for c0 in curves:
        cycle_rows.append({k:c0[k] for k in ("sheet","cycle","n","area_J_m3","duration_s","frequency_hz")})
        for point_i,(hh,jj,bb) in enumerate(zip(c0["H"],c0["J"],c0["B"])):
            point={"sheet":c0["sheet"],"cycle":c0["cycle"],
                "point":point_i,"H_kA_m":float(hh),"J_mT":float(jj),"B_mT":float(bb)}
            if c0["t"] is not None: point["t_s"]=float(c0["t"][point_i])
            curve_points.append(point)
    pd.DataFrame(cycle_rows).to_csv(out/"cycle_metrics.csv",index=False)
    pd.DataFrame(curve_points).to_csv(out/"reconstructed_BH_loops.csv",index=False)
    for sheet in xls.sheet_names:
        cs=[c for c in curves if c["sheet"]==sheet]
        if len(cs)==0:
            report["sheets"][sheet]["JA_LOCO"]={"status":"NOT_RUN",
                "reason":"No complete measured loop detected."}
            continue
        if len(cs)==1:
            # One measured loop per material permits calibration, not an
            # independent held-out-loop validation. Keep that distinction
            # explicit and never relabel the in-sample residual as validation.
            only=cs[0]
            params,pred,fit_info=fit_ja(only["H"],only["J"])
            report["sheets"][sheet]["JA_SINGLE_LOOP_CALIBRATION"]={
                "status":"IN_SAMPLE_CALIBRATION_ONLY",
                "validation_status":"NOT_VALIDATED",
                "reason":"Only one complete loop is present for this material; no independent loop remains for hold-out testing.",
                "fit":fit_info,
                "parameters":{"Ms_kA_m":float(params[0]),"a_kA_m":float(params[1]),
                    "alpha":float(params[2]),"c":float(params[3]),"k_kA_m":float(params[4])}}
            report["sheets"][sheet]["JA_LOCO"]={"status":"NOT_RUN",
                "reason":"One loop per material: leave-one-cycle-out validation is impossible."}
            continue
        fold_results=[]
        for test_i,test in enumerate(cs):
            train=[c for i,c in enumerate(cs) if i!=test_i]
            # Fit on concatenated training loops with separate initial states,
            # but optimize a common parameter vector across all loops.
            def objective(p):
                rr=[]
                for tr in train:
                    m0=tr["J"][0]/MU0_MILLI_T_PER_KA_M
                    pred=ja_simulate(tr["H"],p,m0)
                    if not np.all(np.isfinite(pred)): return np.full(1000,1e6)
                    obs=tr["J"]/MU0_MILLI_T_PER_KA_M
                    rr.extend(((pred-obs)/max(np.ptp(obs),1e-6)).tolist())
                return np.asarray(rr)
            # pooled fit with bounded least squares, initial scale from training.
            hspan=max(np.ptp(np.concatenate([x["H"] for x in train])),1e-6)
            mscale=max(np.max(np.abs(np.concatenate([x["J"] for x in train])))/MU0_MILLI_T_PER_KA_M,1e-3)
            x0=[1.15*mscale,.12*hspan,1e-4,.15,.08*hspan]
            lo=[.2*mscale,1e-4*hspan,0,0,1e-4*hspan]
            hi=[4*mscale,2*hspan,.05,.95,2*hspan]
            fit=least_squares(objective,x0,bounds=(lo,hi),max_nfev=200,loss="soft_l1")
            obs=test["J"]/MU0_MILLI_T_PER_KA_M
            pred=ja_simulate(test["H"],fit.x,obs[0])
            rmse=float(np.sqrt(np.mean((pred-obs)**2)))
            fold_results.append({"held_out_cycle":test_i+1,"n_test":len(obs),
                "rmse_kA_m":rmse,"nrmse_percent":100*rmse/max(float(np.ptp(obs)),1e-12),
                "parameters":{"Ms_kA_m":float(fit.x[0]),"a_kA_m":float(fit.x[1]),
                    "alpha":float(fit.x[2]),"c":float(fit.x[3]),"k_kA_m":float(fit.x[4])}})
        report["sheets"][sheet]["JA_LOCO"]={"status":"COMPLETED",
            "validation":"Each complete cycle held out once; parameters fitted only on remaining cycles.",
            "folds":fold_results,
            "mean_test_nrmse_percent":float(np.mean([f["nrmse_percent"] for f in fold_results]))}
    report["summary"]={"total_complete_cycles":len(curves),
        "Bertotti_fit":"not performed without verified physical inputs"}
    (out/"hysteresis_analysis_report.json").write_text(json.dumps(report,indent=2,allow_nan=False))
    print(json.dumps(report,indent=2))
    print(f"\nWrote {out/'hysteresis_analysis_report.json'} and {out/'cycle_metrics.csv'}")

if __name__=="__main__":
    main()
