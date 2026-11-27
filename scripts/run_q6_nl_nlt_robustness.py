#!/usr/bin/env python3
"""Numerical robustness controls for Q6 NL/NLT (dt halving and DOP853).

Uses matched initial conditions and one shared frequency realization. The
reference is RK4 at dt=0.025; comparisons are RK4 at dt=0.0125 and SciPy
DOP853 over the same physical time. This is a robustness audit, not a
bistability test by itself.
"""
from __future__ import annotations
import argparse, json, platform, subprocess
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from models.q6_topological_synchronization import (
    build_q6_complex, rhs, rk4_step, sample_intrinsic_frequencies,
    order_parameters,
)

MODELS=("NL","NLT")
DEFAULT_SEEDS=(11,23,37,51,67,79,97,109,127,139,151,163,179,191,211,223,239,251,263,277)
DEFAULT_SIGMAS=(.25,.50,.75,1.00,1.25,1.50,1.75,2.00)


def initial_state(seed,family):
    rng=np.random.default_rng(seed)
    if family=="aligned":
        return rng.normal(0,.025,64),rng.normal(0,.025,192)
    return rng.uniform(-np.pi,np.pi,64),rng.uniform(-np.pi,np.pi,192)


def flatten(th,ph):
    return np.concatenate((th,ph))


def unflatten(y):
    return y[:64],y[64:]


def integrate_dop853(K,model,th,ph,omega,omega_link,sigma,T,rtol,atol):
    def fun(t,y):
        a,b=unflatten(y)
        da,db=rhs(K,a,b,omega,omega_link,sigma,model)
        return flatten(da,db)
    sol=solve_ivp(fun,(0.,T),flatten(th,ph),method="DOP853",
                  rtol=rtol,atol=atol,t_eval=[T])
    if not sol.success:
        raise RuntimeError(f"DOP853 failed: {sol.message}")
    return unflatten(sol.y[:,-1]),int(sol.nfev)


def run_rk4(K,model,initial,omega,omega_link,sigma,dt,steps):
    th,ph=initial[0].copy(),initial[1].copy()
    for _ in range(steps):
        th,ph=rk4_step(K,th,ph,omega,omega_link,sigma,dt)
    return th,ph


def metrics(K,state):
    return order_parameters(K,state[0],state[1])


def discrepancy(reference,candidate):
    out={}
    for key in ("R0","R1_down","R1_up"):
        a=float(reference[key]); b=float(candidate[key])
        out[key]={"reference":a,"candidate":b,"absolute_difference":abs(a-b),
                  "relative_difference":abs(a-b)/max(abs(a),1e-12)}
    return out


def git_revision():
    try: return subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip()
    except Exception: return "unavailable"


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--seeds",default=",".join(map(str,DEFAULT_SEEDS)))
    p.add_argument("--sigmas",default=",".join(map(str,DEFAULT_SIGMAS)))
    p.add_argument("--T-steps",type=int,default=640)
    p.add_argument("--dt",type=float,default=.025)
    p.add_argument("--frequency-seed",type=int,default=20261109)
    p.add_argument("--omega0",type=float,default=2.); p.add_argument("--omega1",type=float,default=2.)
    p.add_argument("--tau0",type=float,default=1.); p.add_argument("--tau1",type=float,default=1.)
    p.add_argument("--rtol",type=float,default=1e-10); p.add_argument("--atol",type=float,default=1e-12)
    p.add_argument("--output",type=Path,default=Path("artifacts/q6_nl_nlt_robustness.json"))
    a=p.parse_args()
    seeds=[int(x) for x in a.seeds.split(",")]
    sigmas=[float(x) for x in a.sigmas.split(",")]
    if len(seeds)<20 or a.T_steps<1 or a.dt<=0 or any(x<0 or x>2 for x in sigmas):
        p.error("need >=20 seeds, positive T/dt and sigma in [0,2]")
    K=build_q6_complex()
    omega,omega_link=sample_intrinsic_frequencies(a.frequency_seed,64,192,
        a.omega0,a.omega1,a.tau0,a.tau1)
    rows=[]
    for model in MODELS:
        for sigma in sigmas:
            for seed in seeds:
                for family in ("aligned","random"):
                    initial=initial_state(seed,family)
                    ref=metrics(K,run_rk4(K,model,initial,omega,omega_link,sigma,a.dt,a.T_steps))
                    half=metrics(K,run_rk4(K,model,initial,omega,omega_link,sigma,a.dt/2,2*a.T_steps))
                    (dop_state,nfev)=integrate_dop853(K,model,*initial,omega,omega_link,
                        sigma,a.dt*a.T_steps,a.rtol,a.atol)
                    dop=metrics(K,dop_state)
                    dth=discrepancy(ref,half); ddop=discrepancy(ref,dop)
                    rows.append({"model":model,"sigma":sigma,"seed":seed,"family":family,
                        "physical_time":a.dt*a.T_steps,"rk4_dt":a.dt,"half_dt":a.dt/2,
                        "rk4_reference":ref,"rk4_half_dt":half,"dop853":dop,
                        "dt_halving":dth,"independent_integrator":ddop,"dop853_nfev":nfev,
                        "passes_dt_halving_10pct":all(v["relative_difference"]<=.10 for v in dth.values()),
                        "passes_dop853_10pct":all(v["relative_difference"]<=.10 for v in ddop.values())})
    report={"protocol":"Q6-NL-NLT-ROBUSTNESS-v1","code_revision":git_revision(),
        "python":platform.python_version(),"numpy":np.__version__,
        "design":{"seeds":seeds,"sigmas":sigmas,"frequency_seed":a.frequency_seed,
        "T_steps":a.T_steps,"dt":a.dt,"physical_time":a.dt*a.T_steps,
        "DOP853":{"rtol":a.rtol,"atol":a.atol},
        "same_initial_conditions":True,"same_frequency_realization":True},
        "thresholds":{"relative_observable_difference_max":.10},
        "rows":rows,
        "summary":{"cases":len(rows),
        "dt_halving_pass_fraction":float(np.mean([x["passes_dt_halving_10pct"] for x in rows])),
        "DOP853_pass_fraction":float(np.mean([x["passes_dop853_10pct"] for x in rows])),
        "all_dt_halving_pass":bool(all(x["passes_dt_halving_10pct"] for x in rows)),
        "all_DOP853_pass":bool(all(x["passes_dop853_10pct"] for x in rows))},
        "decision":"ROBUSTNESS NOT ESTABLISHED unless every required case passes; this audit does not establish bistability."}
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"output":str(a.output),"cases":len(rows),"summary":report["summary"],
        "decision":report["decision"]},indent=2))

if __name__=="__main__": main()
