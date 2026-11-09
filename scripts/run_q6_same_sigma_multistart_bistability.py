#!/usr/bin/env python3
"""Same-sigma multistart attractor test for Q6 NL/NLT.

All initial conditions in a replicate share the same intrinsic-frequency
realization. Only initial phases differ. A terminal state is called locked
only if both the final vector-field norm and late-time drift are small.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np
from scipy.linalg import eigvals
from models.q6_topological_synchronization import (
    build_q6_complex, audit_q6_complex, rhs, rk4_step,
    sample_intrinsic_frequencies, order_parameters,
)


def integrate(K, model, sigma, omega, omega_link, theta, phi, steps, dt):
    tail = []
    for k in range(steps):
        theta, phi = rk4_step(K, theta, phi, omega, omega_link,
                              float(sigma), model, dt)
        if k >= steps - max(100, steps // 10):
            tail.append((theta.copy(), phi.copy()))
    return theta, phi, tail


def flatten(theta, phi):
    return np.concatenate([theta, phi])


def unflatten(x):
    return x[:64], x[64:]


def field(K, x, omega, omega_link, sigma, model):
    th, ph = unflatten(x)
    a, b = rhs(K, th, ph, omega, omega_link, sigma, model)
    return flatten(a, b)


def centered_jacobian(fun, x, step=2e-6):
    n = x.size
    J = np.empty((n, n), dtype=float)
    for j in range(n):
        h = step * max(1.0, abs(float(x[j])))
        xp=x.copy(); xm=x.copy()
        xp[j]+=h; xm[j]-=h
        J[:,j]=(fun(xp)-fun(xm))/(2*h)
    return J


def assess(K, model, sigma, omega, omega_link, theta, phi, tail, dt,
           jacobian=True):
    x=flatten(theta,phi)
    f=field(K,x,omega,omega_link,sigma,model)
    field_rms=float(np.linalg.norm(f)/np.sqrt(x.size))
    # Unwrapped coordinate drift over the stored tail; remove the global
    # theta phase gauge by subtracting its mean increment.
    if len(tail)>=2:
        x0=flatten(*tail[0]); x1=flatten(*tail[-1])
        delta=(x1-x0)/max(1,len(tail)-1)
        delta[:64]-=np.mean(delta[:64])
        drift_rms=float(np.linalg.norm(delta)/np.sqrt(x.size))
    else:
        drift_rms=float("nan")
    out={"field_rms":field_rms,"late_drift_rms_per_step":drift_rms,
         "orders":order_parameters(K,theta,phi)}
    if jacobian and field_rms < 2e-3 and drift_rms < 2e-3:
        J=centered_jacobian(lambda z:field(K,z,omega,omega_link,sigma,model),x)
        ev=eigvals(J)
        # The common shift of all vertex phases is an exact gauge-neutral mode.
        nonneutral=np.abs(ev)>1e-7
        out["jacobian"]={
            "max_real_eigenvalue":float(np.max(ev[nonneutral].real)) if np.any(nonneutral) else 0.0,
            "neutral_modes_abs_lt_1e-7":int(np.sum(~nonneutral)),
            "linearly_stable_modulo_global_phase":bool(
                np.max(ev[nonneutral].real)<1e-6 if np.any(nonneutral) else True),
        }
    else:
        out["jacobian"]={"computed":False,"reason":"candidate not sufficiently stationary"}
    return out


def run(args):
    K=build_q6_complex()
    report={"complex_audit":audit_q6_complex(K),
      "design":{"models":["NL","NLT"],"sigma_values":args.sigmas,
        "dwell_steps":args.dwells,"dt":args.dt,"frequency_seed":args.frequency_seed,
        "initial_phase_seeds":args.phase_seeds,
        "control":"same intrinsic frequencies at each sigma/model; vary only initial phases",
        "decision_rule":"bistability requires >=2 distinct terminal order clusters at same sigma, each stationary and linearly stable modulo global theta phase",
        "limitations":["one Q6 size only","finite multistart cannot prove absence of other attractors",
          "finite-time convergence thresholds are numerical diagnostics, not a theorem"]},
      "results":[]}
    omega,omega_link=sample_intrinsic_frequencies(args.frequency_seed,64,192,
        args.omega0,args.omega1,args.tau0,args.tau1)
    rng=np.random.default_rng(args.phase_seed_base)
    initials=[(rng.uniform(-np.pi,np.pi,64),rng.uniform(-np.pi,np.pi,192))
              for _ in args.phase_seeds]
    for model in ("NL","NLT"):
      for sigma in args.sigmas:
       for dwell in args.dwells:
        for idx,(th0,ph0) in enumerate(initials):
          th,ph,tail=integrate(K,model,sigma,omega,omega_link,
              th0.copy(),ph0.copy(),dwell,args.dt)
          metrics=assess(K,model,sigma,omega,omega_link,th,ph,tail,args.dt,
                         jacobian=(idx < args.jacobian_candidates))
          report["results"].append({"model":model,"sigma":sigma,"dwell_steps":dwell,
              "phase_seed":args.phase_seeds[idx],"metrics":metrics})
    # Cluster terminal order triples at each fixed model/sigma/dwell.
    for model in ("NL","NLT"):
      for sigma in args.sigmas:
       for dwell in args.dwells:
        rows=[r for r in report["results"] if r["model"]==model and
              r["sigma"]==sigma and r["dwell_steps"]==dwell]
        vectors=np.array([[r["metrics"]["orders"][k] for k in
                          ("R0","R1_down","R1_up")] for r in rows])
        labels=[]; centers=[]
        for v in vectors:
          found=None
          for j,c in enumerate(centers):
            if np.linalg.norm(v-c)<args.cluster_tol: found=j; break
          if found is None: centers.append(v.copy()); labels.append(len(centers)-1)
          else: labels.append(found)
        report.setdefault("clusters",[]).append({"model":model,"sigma":sigma,
          "dwell_steps":dwell,"count":len(centers),
          "centers":[c.tolist() for c in centers],"labels":labels,
          "warning":"distinct order triples alone are not bistability; inspect stationarity and Jacobian stability of each cluster"})
    return report


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--sigmas",default="0.75,1.0,1.25,1.5,1.75,2.0")
    p.add_argument("--dwells",default="2560,10240")
    p.add_argument("--phase-seeds",default="11,23,37,51,67,79,97,109")
    p.add_argument("--frequency-seed",type=int,default=20261109)
    p.add_argument("--phase-seed-base",type=int,default=20261110)
    p.add_argument("--dt",type=float,default=0.025)
    p.add_argument("--omega0",type=float,default=2.0); p.add_argument("--omega1",type=float,default=2.0)
    p.add_argument("--tau0",type=float,default=1.0); p.add_argument("--tau1",type=float,default=1.0)
    p.add_argument("--jacobian-candidates",type=int,default=2)
    p.add_argument("--cluster-tol",type=float,default=0.025)
    p.add_argument("--output",type=Path,default=Path("q6_same_sigma_multistart.json"))
    a=p.parse_args()
    a.sigmas=[float(x) for x in a.sigmas.split(",")]
    a.dwells=[int(x) for x in a.dwells.split(",")]
    a.phase_seeds=[int(x) for x in a.phase_seeds.split(",")]
    if not a.sigmas or not a.dwells or not a.phase_seeds or min(a.dwells)<=0 or a.dt<=0:
        p.error("invalid sigma, dwell, seed or dt")
    report=run(a)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"output":str(a.output),"complex_audit":report["complex_audit"],
       "clusters":report["clusters"]},indent=2))


if __name__=="__main__": main()
