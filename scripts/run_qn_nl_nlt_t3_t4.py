#!/usr/bin/env python3
"""Q4/Q5/Q6 NL/NLT hysteresis and size-persistence audit (T3/T4).

Uses the frozen rhs/rk4_step implementation. Each (dimension, model, seed,
dwell) run uses one frequency realization for both sweep directions. The
reverse sweep starts from the forward terminal state. No bistability claim is
made by this protocol alone.
"""
from __future__ import annotations
import argparse, json, platform, subprocess
from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path
import numpy as np
from models.q6_topological_synchronization import rhs, rk4_step, order_parameters

MODELS=("NL","NLT")
DEFAULT_SEEDS=(11,23,37,51,67,79,97,109,127,139,151,163,179,191,211,223,239,251,263,277)
DEFAULT_DWELLS=(640,2560,10240)

@dataclass(frozen=True)
class Cubical2:
    n: int
    vertices: tuple
    edges: tuple
    faces: tuple
    B1: np.ndarray
    B2: np.ndarray


def build_qn_2_skeleton(n: int) -> Cubical2:
    if n < 2:
        raise ValueError("n must be >= 2")
    vertices=tuple(product((0,1), repeat=n))
    vi={v:i for i,v in enumerate(vertices)}
    edges=[]
    for v in vertices:
        for axis in range(n):
            if v[axis]==0:
                w=list(v); w[axis]=1
                edges.append((vi[v],vi[tuple(w)]))
    edges=tuple(sorted(edges)); ei={e:i for i,e in enumerate(edges)}
    faces=[]
    for axes in combinations(range(n),2):
        fixed_axes=[a for a in range(n) if a not in axes]
        for fixed in product((0,1), repeat=n-2):
            base=[0]*n
            for a,bit in zip(fixed_axes,fixed): base[a]=bit
            a,b=axes
            v00=tuple(base)
            v10=base.copy(); v10[a]=1
            v11=v10.copy(); v11[b]=1
            v01=base.copy(); v01[b]=1
            faces.append(tuple(vi[x] for x in (v00,tuple(v10),tuple(v11),tuple(v01))))
    faces=tuple(faces)
    B1=np.zeros((len(vertices),len(edges)),dtype=np.int8)
    for j,(u,v) in enumerate(edges): B1[u,j],B1[v,j]=-1,1
    B2=np.zeros((len(edges),len(faces)),dtype=np.int8)
    for f,cycle in enumerate(faces):
        for u,v in zip(cycle,cycle[1:]+cycle[:1]):
            B2[ei[(min(u,v),max(u,v))],f] += 1 if u<v else -1
    if np.count_nonzero(B1@B2):
        raise AssertionError(f"boundary-of-boundary failed for Q{n}")
    return Cubical2(n,vertices,edges,faces,B1,B2)


def sample_frequencies(seed,nv,ne,omega0,omega1,tau0,tau1):
    if tau0<=0 or tau1<=0: raise ValueError("tau0 and tau1 must be positive")
    rng=np.random.default_rng(seed)
    # Same frame convention as the frozen Q6 protocol: remove node mean Omega0,
    # retain the link-frequency mean Omega1.
    return (rng.normal(omega0,1/tau0,nv)-omega0,
            rng.normal(omega1,1/tau1,ne))


def init_state(seed,nv,ne):
    rng=np.random.default_rng(seed+1_000_003)
    return (rng.uniform(-np.pi,np.pi,nv),rng.uniform(-np.pi,np.pi,ne))


def run_sweep(K,model,sigmas,dwell,dt,omega,omega_link,initial):
    th,ph=(initial[0].copy(),initial[1].copy())
    rows=[]
    for sigma in sigmas:
        for _ in range(dwell):
            th,ph=rk4_step(K,th,ph,omega,omega_link,float(sigma),model,dt)
        rows.append({"sigma":float(sigma),**order_parameters(K,th,ph)})
    return rows,(th,ph)


def one_hysteresis(K,model,seed,frequency_seed,dwell,sigmas,dt,
                   omega0,omega1,tau0,tau1):
    nv=len(K.vertices); ne=len(K.edges)
    omega,omega_link=sample_frequencies(frequency_seed,nv,ne,omega0,omega1,tau0,tau1)
    initial=init_state(seed,nv,ne)
    forward,terminal=run_sweep(K,model,sigmas,dwell,dt,omega,omega_link,initial)
    backward,_=run_sweep(K,model,list(reversed(sigmas)),dwell,dt,omega,omega_link,terminal)
    backward=list(reversed(backward))
    gaps={}
    for key in ("R0","R1_down","R1_up"):
        vals=[abs(a[key]-b[key]) for a,b in zip(forward,backward)]
        gaps[key]={"mean_abs_gap":float(np.mean(vals)),
                   "max_abs_gap":float(np.max(vals)),
                   "by_sigma":vals}
    return {"model":model,"seed":seed,"frequency_seed":frequency_seed,
            "dwell_steps":dwell,"physical_dwell_time":dwell*dt,
            "forward":forward,"backward":backward,"gaps":gaps}


def summarize(rows, dwells):
    out=[]
    dims=sorted({r["dimension"] for r in rows})
    for n in dims:
        for model in MODELS:
            for dwell in dwells:
                ss=[r for r in rows if r["dimension"]==n and r["model"]==model and r["dwell_steps"]==dwell]
                if not ss: continue
                out.append({"dimension":n,"model":model,"dwell_steps":dwell,
                    "seed_count":len(ss),
                    "mean_abs_hysteresis_R0":float(np.mean([x["gaps"]["R0"]["mean_abs_gap"] for x in ss])),
                    "mean_abs_hysteresis_R1_down":float(np.mean([x["gaps"]["R1_down"]["mean_abs_gap"] for x in ss])),
                    "mean_abs_hysteresis_R1_up":float(np.mean([x["gaps"]["R1_up"]["mean_abs_gap"] for x in ss]))})
    # Preregistered T3 persistence: gap at longest dwell >= half the shortest
    # dwell gap, and non-decreasing over all three dwell values.
    for n in dims:
        for model in MODELS:
            q=[x for x in out if x["dimension"]==n and x["model"]==model]
            q.sort(key=lambda x:x["dwell_steps"])
            if len(q)==3:
                g=[x["mean_abs_hysteresis_R0"] for x in q]
                q[-1]["ratio_10240_over_640"]=g[-1]/g[0] if g[0]>0 else None
                q[-1]["nondecreasing_with_dwell"]=bool(g[0]<=g[1]<=g[2])
                q[-1]["passes_T3_dwell_persistence"]=bool(g[0]>0 and g[-1]>=.5*g[0] and g[0]<=g[1]<=g[2])
    # T4: Q6 R0 gap must be >= 50% of Q4 at each model/dwell.
    for model in MODELS:
        for dwell in dwells:
            a=next((x for x in out if x["dimension"]==4 and x["model"]==model and x["dwell_steps"]==dwell),None)
            c=next((x for x in out if x["dimension"]==6 and x["model"]==model and x["dwell_steps"]==dwell),None)
            if a and c:
                c["Q6_over_Q4_R0_gap"]=c["mean_abs_hysteresis_R0"]/a["mean_abs_hysteresis_R0"] if a["mean_abs_hysteresis_R0"]>0 else None
                c["passes_T4_size_persistence"]=bool(c["Q6_over_Q4_R0_gap"] is not None and c["Q6_over_Q4_R0_gap"]>=.5)
    return out


def git_revision():
    try: return subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip()
    except Exception: return "unavailable"


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--dimensions",default="4,5,6")
    p.add_argument("--sigmas",default=",".join(f"{x/20:.2f}" for x in range(41)))
    p.add_argument("--seeds",default=",".join(map(str,DEFAULT_SEEDS)))
    p.add_argument("--frequency-seed",type=int,default=20261109)
    p.add_argument("--dwells",default="640,2560,10240")
    p.add_argument("--dt",type=float,default=.025)
    p.add_argument("--omega0",type=float,default=2.); p.add_argument("--omega1",type=float,default=2.)
    p.add_argument("--tau0",type=float,default=1.); p.add_argument("--tau1",type=float,default=1.)
    p.add_argument("--output",type=Path,default=Path("artifacts/q6_nl_nlt_t3_t4.json"))
    a=p.parse_args()
    dims=[int(x) for x in a.dimensions.split(",")]
    sigmas=[float(x) for x in a.sigmas.split(",")]
    seeds=[int(x) for x in a.seeds.split(",")]
    dwells=[int(x) for x in a.dwells.split(",")]
    if any(n not in (4,5,6) for n in dims) or any(x<0 or x>2 for x in sigmas) or any(x<1 for x in dwells) or a.dt<=0:
        p.error("invalid dimensions, sigma, dwell or dt")
    rows=[]; audits={}
    for n in dims:
        K=build_qn_2_skeleton(n)
        audits[str(n)]={"vertices":len(K.vertices),"edges":len(K.edges),"faces":len(K.faces),
            "B1B2_exact_zero":bool(np.count_nonzero(K.B1@K.B2)==0)}
        for model in MODELS:
            for seed in seeds:
                for dwell in dwells:
                    row=one_hysteresis(K,model,seed,a.frequency_seed,dwell,sigmas,a.dt,
                        a.omega0,a.omega1,a.tau0,a.tau1)
                    row["dimension"]=n
                    rows.append(row)
    summary=summarize(rows,dwells)
    report={"protocol":"Q4-Q6-NL-NLT-T3-T4-v1","code_revision":git_revision(),
        "python":platform.python_version(),"numpy":np.__version__,
        "complex_audits":audits,"design":{"dimensions":dims,"sigmas":sigmas,
        "seeds":seeds,"frequency_seed":a.frequency_seed,"dwells":dwells,"dt":a.dt,
        "frequency_law":{"omega0":a.omega0,"omega1":a.omega1,"tau0":a.tau0,"tau1":a.tau1,
        "node_mean_removed":True,"link_mean_removed":False},
        "sweep":"forward ascending; reverse descending from forward terminal state"},
        "thresholds":{"T3_long_over_short_at_least":.5,"T3_non_decreasing_all_dwells":True,
        "T4_Q6_over_Q4_at_least":.5},
        "runs":rows,"summary":summary,
        "decision":"NON DIMOSTRATA: T1/T2 and numerical robustness controls (dt/2 and independent integrator) must also pass; no run is inferred from script creation."}
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"output":str(a.output),"runs":len(rows),"summary_rows":len(summary),
        "decision":report["decision"]},indent=2))

if __name__=="__main__": main()
