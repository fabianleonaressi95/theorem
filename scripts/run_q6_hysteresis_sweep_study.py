#!/usr/bin/env python3
"""Multi-seed, multi-sweep-rate finite-size study for Q6 NL/NLT dynamics.

The effective sweep rate is Delta_sigma / (steps_per_sigma * dt).  This is
a protocol parameter, not a physical frequency.  Frequencies and the initial
state are reproducible for each seed and reused across dwell-time settings.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import numpy as np
from models.q6_topological_synchronization import (
    build_q6_complex, audit_q6_complex, simulate_branch,
)


def _curve(rows, key):
    return np.asarray([row[key] for row in rows], dtype=float)


def compare_branches(sigmas, forward, backward):
    """Compare forward and reverse branches at matching sigma values."""
    result = {}
    x = np.asarray(sigmas, dtype=float)
    for key in ("R0", "R1_down", "R1_up"):
        yf = _curve(forward, key)
        # backward rows are stored in descending sigma order; align them.
        yb = _curve(backward, key)[::-1]
        gap = np.abs(yf-yb)
        # Signed trapezoidal integrals around the closed path.
        area = abs(float(np.trapezoid(yf, x) + np.trapezoid(yb[::-1], x[::-1])))
        result[key] = {
            "mean_abs_branch_gap": float(np.mean(gap)),
            "max_abs_branch_gap": float(np.max(gap)),
            "loop_area_sigma_order": area,
        }
    return result


def run_study(seeds, dwell_steps, sigma_max, sigma_count, dt):
    K = build_q6_complex()
    sigmas = np.linspace(0.0, sigma_max, sigma_count)
    delta_sigma = float(sigmas[1]-sigmas[0])
    report = {
        "complex_audit": audit_q6_complex(K),
        "model": "Q6 cubical 2-skeleton; cubical extension of published simplicial NL/NLT equations",
        "protocol": {
            "seeds": list(seeds),
            "dwell_steps_per_sigma": list(dwell_steps),
            "sigma_min": 0.0,
            "sigma_max": float(sigma_max),
            "sigma_count": int(sigma_count),
            "delta_sigma": delta_sigma,
            "dt": float(dt),
            "effective_sweep_rate": {
                str(n): delta_sigma/(n*dt) for n in dwell_steps
            },
            "seed_controls": "same seed reproduces the same initial phases and intrinsic frequencies across dwell settings",
            "backward_initialization": "terminal state of corresponding forward sweep",
        },
        "runs": [],
        "summary": {},
        "interpretation": {
            "status": "finite-size numerical protocol study",
            "hysteresis_claim": "not established by protocol settings alone; inspect branch gaps, loop areas, seed dispersion and dwell-time dependence",
            "limitations": [
                "single fixed Q6 size (64 nodes, 192 links, 240 square faces)",
                "cubical Q6 extension, not the simplicial complexes used in the source paper",
                "seeds jointly vary initial phases and intrinsic frequencies",
                "backward branch starts from the forward terminal state; alternative attractor initialization is not yet exhausted",
                "no thermodynamic-limit or material-constitutive inference",
            ],
        },
    }

    for model in ("NL", "NLT"):
        for dwell in dwell_steps:
            per_seed = []
            for seed in seeds:
                forward, terminal = simulate_branch(
                    K, sigmas, model, seed=int(seed),
                    steps_per_sigma=int(dwell), dt=dt, return_final=True
                )
                backward = simulate_branch(
                    K, sigmas[::-1], model, seed=int(seed),
                    steps_per_sigma=int(dwell), dt=dt, initial=terminal
                )
                metrics = compare_branches(sigmas, forward, backward)
                run = {
                    "model": model,
                    "seed": int(seed),
                    "steps_per_sigma": int(dwell),
                    "effective_sweep_rate": delta_sigma/(int(dwell)*dt),
                    "forward": forward,
                    "backward": backward,
                    "metrics": metrics,
                }
                report["runs"].append(run)
                per_seed.append(metrics)

            summary = {}
            for key in ("R0", "R1_down", "R1_up"):
                summary[key] = {}
                for metric in ("mean_abs_branch_gap", "max_abs_branch_gap", "loop_area_sigma_order"):
                    values = np.asarray([m[key][metric] for m in per_seed], dtype=float)
                    summary[key][metric] = {
                        "mean": float(np.mean(values)),
                        "std": float(np.std(values, ddof=1)) if len(values)>1 else 0.0,
                        "per_seed": values.tolist(),
                    }
            report["summary"][f"{model}_dwell_{dwell}"] = summary
    return report


def plot_report(report, prefix):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    sigmas = np.linspace(
        report["protocol"]["sigma_min"],
        report["protocol"]["sigma_max"],
        report["protocol"]["sigma_count"],
    )
    dwells = report["protocol"]["dwell_steps_per_sigma"]
    seeds = report["protocol"]["seeds"]
    labels = ("R0", "R1_down", "R1_up")
    for model in ("NL", "NLT"):
        fig, axes = plt.subplots(1, 3, figsize=(15, 4.5), sharex=True)
        for ax, key in zip(axes, labels):
            for dwell in dwells:
                fcurves=[]; bcurves=[]
                for seed in seeds:
                    run=next(r for r in report["runs"]
                             if r["model"]==model and r["seed"]==seed
                             and r["steps_per_sigma"]==dwell)
                    fcurves.append(_curve(run["forward"],key))
                    bcurves.append(_curve(run["backward"],key)[::-1])
                fcurves=np.asarray(fcurves); bcurves=np.asarray(bcurves)
                rate=report["protocol"]["effective_sweep_rate"][str(dwell)]
                label=f"{dwell} steps/σ (rate={rate:.3g})"
                fm=fcurves.mean(axis=0); fs=fcurves.std(axis=0)
                bm=bcurves.mean(axis=0); bs=bcurves.std(axis=0)
                ax.plot(sigmas,fm,marker="o",markersize=2,label=f"forward {label}")
                ax.fill_between(sigmas,fm-fs,fm+fs,alpha=.10)
                ax.plot(sigmas,bm,marker="x",markersize=2,linestyle="--",
                        label=f"backward {label}")
                ax.fill_between(sigmas,bm-bs,bm+bs,alpha=.08)
            ax.set_title(key)
            ax.set_xlabel("coupling σ")
            ax.set_ylabel("order parameter")
            ax.set_ylim(-.03,1.03)
            ax.grid(True,alpha=.25)
        axes[-1].legend(fontsize=6,loc="best")
        fig.suptitle(f"Q6 {model}: forward/backward synchronization branches")
        fig.tight_layout()
        path=Path(f"{prefix}_{model.lower()}.png")
        path.parent.mkdir(parents=True,exist_ok=True)
        fig.savefig(path,dpi=180)
        plt.close(fig)


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--seeds",default="11,23,37,51,67")
    p.add_argument("--dwell-steps",default="10,40,160")
    p.add_argument("--sigma-max",type=float,default=2.0)
    p.add_argument("--sigma-count",type=int,default=21)
    p.add_argument("--dt",type=float,default=.025)
    p.add_argument("--output",type=Path,default=Path("q6_hysteresis_sweep_study.json"))
    p.add_argument("--plot-prefix",default="q6_hysteresis_sweep")
    p.add_argument("--no-plots",action="store_true")
    a=p.parse_args()
    seeds=[int(x) for x in a.seeds.split(",") if x.strip()]
    dwells=sorted({int(x) for x in a.dwell_steps.split(",") if x.strip()})
    if not seeds or not dwells or min(dwells)<1 or a.sigma_count<2 or a.sigma_max<=0 or a.dt<=0:
        p.error("provide seeds, positive dwell steps, sigma-count >= 2, sigma-max > 0 and dt > 0")
    report=run_study(seeds,dwells,a.sigma_max,a.sigma_count,a.dt)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    if not a.no_plots:
        plot_report(report,a.plot_prefix)
    print(json.dumps({"protocol":report["protocol"],"summary":report["summary"],
                      "output":str(a.output),"plots":None if a.no_plots else
                      [f"{a.plot_prefix}_nl.png",f"{a.plot_prefix}_nlt.png"]},indent=2))


if __name__=="__main__":
    main()
