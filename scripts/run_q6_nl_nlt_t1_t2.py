#!/usr/bin/env python3
"""Pre-registered Q6 NL/NLT verification: T1 homogeneous fixed points, T2 heterogeneous dynamics.

The NL/NLT vector fields are imported from the frozen model module.  T1 fixes
omega=omega_link=0 and removes the global theta phase gauge by pinning theta[0]=0.
T2 uses one fixed heterogeneous frequency realization shared by aligned/random
initial-condition families and records R0, R1_down and R1_up at T, 2T and 4T.
"""
from __future__ import annotations
import argparse
import json
import platform
import subprocess
from pathlib import Path

import numpy as np
from scipy.linalg import eigvals
from scipy.optimize import root

from models.q6_topological_synchronization import (
    build_q6_complex, audit_q6_complex, rhs, rk4_step,
    sample_intrinsic_frequencies, order_parameters,
)

MODELS = ("NL", "NLT")


def pack(theta, phi):
    return np.concatenate((theta, phi))


def unpack(x):
    return x[:64], x[64:]


def vector_field(K, x, omega, omega_link, sigma, model):
    th, ph = unpack(x)
    a, b = rhs(K, th, ph, omega, omega_link, sigma, model)
    return pack(a, b)


def reduced_to_full(y):
    """Reduced coordinates y=(theta[1:],phi), with theta[0]=0."""
    return np.concatenate(([0.0], y[:63], y[63:]))


def full_to_reduced(x):
    return np.concatenate((x[1:64], x[64:]))


def gauge_distance(x, y):
    """Euclidean wrapped distance modulo the common theta phase."""
    a, b = unpack(x.copy()), unpack(y.copy())
    dtheta = np.angle(np.exp(1j*(a[0]-b[0])))
    shift = np.angle(np.mean(np.exp(1j*dtheta)))
    dt = np.angle(np.exp(1j*(a[0]-b[0]-shift)))
    dp = np.angle(np.exp(1j*(a[1]-b[1])))
    return float(np.sqrt(np.mean(dt*dt)+np.mean(dp*dp)))


def finite_jacobian(fun, x, h=1e-6):
    n = len(x)
    J = np.empty((n, n), dtype=float)
    for j in range(n):
        step = h*max(1.0, abs(float(x[j])))
        xp=x.copy(); xm=x.copy()
        xp[j]+=step; xm[j]-=step
        J[:, j]=(fun(xp)-fun(xm))/(2*step)
    return J


def t1_for_model(K, model, sigmas, starts, seed, root_tol, dedup_tol):
    rng=np.random.default_rng(seed)
    zeros64=np.zeros(64); zeros192=np.zeros(192)
    results=[]
    for sigma in sigmas:
        found=[]
        attempts=[]
        for start_id in range(starts):
            theta=rng.uniform(-np.pi,np.pi,64)
            phi=rng.uniform(-np.pi,np.pi,192)
            y0=full_to_reduced(pack(theta,phi))
            fun=lambda y: vector_field(K,reduced_to_full(y),zeros64,zeros192,
                                      float(sigma),model)[1:]
            sol=root(fun,y0,method="hybr",options={"xtol":root_tol})
            residual=float(np.linalg.norm(fun(sol.x))/np.sqrt(255))
            row={"start":start_id,"solver_success":bool(sol.success),
                 "residual_rms":residual}
            if np.isfinite(residual) and residual < max(10*root_tol,1e-8):
                x=reduced_to_full(sol.x)
                if not any(gauge_distance(x,z["state"])<dedup_tol for z in found):
                    found.append({"state":x,"residual_rms":residual})
            attempts.append(row)
        fixed=[]
        for idx,item in enumerate(found):
            x=item["state"]
            J=finite_jacobian(lambda z:vector_field(
                K,z,zeros64,zeros192,float(sigma),model)[1:],full_to_reduced(x))
            ev=eigvals(J)
            maxreal=float(np.max(ev.real))
            fixed.append({"candidate":idx,"residual_rms":item["residual_rms"],
                "max_real_eigenvalue":maxreal,
                "stable_modulo_global_theta_phase":bool(maxreal < -1e-7),
                "marginal_or_unstable":bool(maxreal >= -1e-7),
                "orders":order_parameters(K,*unpack(x))})
        results.append({"model":model,"sigma":float(sigma),
            "initial_starts":starts,"converged_distinct_fixed_points":len(found),
            "stable_fixed_points":sum(x["stable_modulo_global_theta_phase"] for x in fixed),
            "fixed_points":fixed,
            "solver_success_count":sum(x["solver_success"] for x in attempts),
            "note":"Finite multistart gives a lower bound on discovered roots, not proof of completeness."})
    return results


def initialize_family(rng, family):
    if family=="aligned":
        theta=rng.normal(0.0,0.025,64)
        phi=rng.normal(0.0,0.025,192)
    else:
        theta=rng.uniform(-np.pi,np.pi,64)
        phi=rng.uniform(-np.pi,np.pi,192)
    return theta,phi


def t2_for_model(K, model, sigmas, seeds, frequency_seed, omega0, omega1,
                 tau0, tau1, dt, T_steps):
    omega,omega_link=sample_intrinsic_frequencies(
        frequency_seed,64,192,omega0,omega1,tau0,tau1)
    rows=[]
    for sigma in sigmas:
        for seed in seeds:
            rng=np.random.default_rng(seed)
            states={fam:initialize_family(rng,fam) for fam in ("aligned","random")}
            snapshots={fam:{} for fam in states}
            targets={T_steps,2*T_steps,4*T_steps}
            for step in range(1,4*T_steps+1):
                for fam,(th,ph) in list(states.items()):
                    states[fam]=rk4_step(K,th,ph,omega,omega_link,
                                         float(sigma),model,dt)
                if step in targets:
                    for fam,(th,ph) in states.items():
                        snapshots[fam][step]=order_parameters(K,th,ph)
            for step in sorted(targets):
                a=snapshots["aligned"][step]; r=snapshots["random"][step]
                rows.append({"model":model,"sigma":float(sigma),"seed":int(seed),
                    "steps":step,"physical_time":float(step*dt),
                    "aligned":a,"random":r,
                    "paired_delta_R0":float(a["R0"]-r["R0"])})
    summary=[]
    for sigma in sigmas:
        for steps in sorted({T_steps,2*T_steps,4*T_steps}):
            subset=[x for x in rows if x["sigma"]==float(sigma) and x["steps"]==steps]
            d=np.asarray([x["paired_delta_R0"] for x in subset])
            mean=float(np.mean(d)); sd=float(np.std(d,ddof=1)) if len(d)>1 else 0.0
            summary.append({"model":model,"sigma":float(sigma),"steps":steps,
                "seed_count":len(d),"mean_delta_R0":mean,"sd_paired_delta_R0":sd,
                "absolute_family_separation":abs(mean),
                "separation_over_sd":abs(mean)/sd if sd>0 else None,
                "passes_T2_at_this_time":bool(abs(mean)>0.2 and sd>0 and abs(mean)>3*sd)})
    return {"frequency_realization":{"seed":frequency_seed,"omega0":omega0,
            "omega1":omega1,"tau0":tau0,"tau1":tau1,
            "node_mean_removed":True,"link_mean_removed":False},
            "trajectories":rows,"summary":summary}


def git_revision():
    try:
        return subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip()
    except Exception:
        return "unavailable"


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--sigmas",default=",".join(f"{x/20:.2f}" for x in range(0,41)))
    p.add_argument("--t1-starts",type=int,default=200)
    p.add_argument("--t1-seed",type=int,default=20261109)
    p.add_argument("--root-tol",type=float,default=1e-9)
    p.add_argument("--dedup-tol",type=float,default=1e-5)
    p.add_argument("--t2-seeds",default="11,23,37,51,67,79,97,109,127,139,151,163,179,191,211,223,239,251,263,277")
    p.add_argument("--frequency-seed",type=int,default=20261109)
    p.add_argument("--omega0",type=float,default=2.0); p.add_argument("--omega1",type=float,default=2.0)
    p.add_argument("--tau0",type=float,default=1.0); p.add_argument("--tau1",type=float,default=1.0)
    p.add_argument("--dt",type=float,default=0.025)
    p.add_argument("--T-steps",type=int,default=640)
    p.add_argument("--skip-t1",action="store_true")
    p.add_argument("--skip-t2",action="store_true")
    p.add_argument("--output",type=Path,default=Path("artifacts/q6_nl_nlt_t1_t2.json"))
    a=p.parse_args()
    sigmas=[float(x) for x in a.sigmas.split(",")]
    seeds=[int(x) for x in a.t2_seeds.split(",")]
    if not sigmas or any(x<0 or x>2 for x in sigmas) or a.t1_starts<1 or a.T_steps<1 or a.dt<=0:
        p.error("invalid sigma grid, starts, T_steps or dt")
    K=build_q6_complex()
    report={"protocol":"Q6-NL/NLT-T1-T2-v1",
        "code_revision":git_revision(),"python":platform.python_version(),
        "numpy":np.__version__,"complex_audit":audit_q6_complex(K),
        "frozen_equations":"models/q6_topological_synchronization.py::rhs",
        "frame_convention":{"homogeneous":"omega=omega_link=0",
            "heterogeneous":"node mean removed; link mean retained; no link-frame shift"},
        "thresholds":{"T2_mean_R0_separation_gt":0.2,
            "T2_separation_over_paired_sd_gt":3.0,
            "T2_seed_minimum":20},
        "design":{"sigmas":sigmas,"t1_starts_per_sigma":a.t1_starts,
            "t2_seeds":seeds,"frequency_seed":a.frequency_seed,
            "dt":a.dt,"T_steps":a.T_steps,"times_steps":[a.T_steps,2*a.T_steps,4*a.T_steps]},
        "T1":[],"T2":{}}
    if not a.skip_t1:
        for model in MODELS:
            report["T1"].extend(t1_for_model(K,model,sigmas,a.t1_starts,
                a.t1_seed,a.root_tol,a.dedup_tol))
    if not a.skip_t2:
        for model in MODELS:
            report["T2"][model]=t2_for_model(K,model,sigmas,seeds,
                a.frequency_seed,a.omega0,a.omega1,a.tau0,a.tau1,a.dt,a.T_steps)
    report["decision"]="NON DIMOSTRATA: T1/T2 are numerical tests; T3/T4, dt-halving and independent-integrator controls remain outstanding."
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"output":str(a.output),"T1_rows":len(report["T1"]),
        "T2_summary_rows":sum(len(v["summary"]) for v in report["T2"].values()),
        "decision":report["decision"]},indent=2))


if __name__=="__main__":
    main()
