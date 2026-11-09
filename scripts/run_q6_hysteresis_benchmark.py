#!/usr/bin/env python3
"""Run exact Q6 cellular audit and finite NL/NLT continuation sweeps."""
import argparse,json
from pathlib import Path
import numpy as np
from models.q6_topological_synchronization import build_q6_complex,audit_q6_complex,simulate_branch

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--steps-per-sigma",type=int,default=40)
    p.add_argument("--sigma-max",type=float,default=2.0)
    p.add_argument("--sigma-count",type=int,default=9)
    p.add_argument("--seed",type=int,default=20261109)
    p.add_argument("--output",type=Path,default=Path("q6_hysteresis_results.json"))
    a=p.parse_args()
    if a.steps_per_sigma<1 or a.sigma_count<2 or a.sigma_max<=0:
        p.error("steps-per-sigma >= 1, sigma-count >= 2, sigma-max > 0 required")
    K=build_q6_complex()
    report={"complex_audit":audit_q6_complex(K),"protocol":{
        "steps_per_sigma":a.steps_per_sigma,"sigma_max":a.sigma_max,
        "sigma_count":a.sigma_count,"seed":a.seed}}
    sigmas=np.linspace(0,a.sigma_max,a.sigma_count)
    for model in ("NL","NLT"):
        forward,terminal=simulate_branch(K,sigmas,model,a.seed,a.steps_per_sigma,return_final=True)
        backward=simulate_branch(K,sigmas[::-1],model,a.seed,a.steps_per_sigma,initial=terminal)
        report[model]={"forward":forward,"backward":backward}
    report["interpretation"]={
        "status":"exploratory finite-size numerical benchmark",
        "hysteresis_claim":"not established; inspect branch separation and refine protocol",
        "limitations":["finite Q6 only; no thermodynamic-limit result",
          "no experimental industrial data loaded",
          "no Preisach/Prandtl-Ishlinskii/Bouc-Wen/Jiles-Atherton fitting",
          "cubical extension is not the simplicial model studied in the 2021 paper"]}
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(report,indent=2)+"\\n",encoding="utf-8")
    print(json.dumps(report["complex_audit"],indent=2))
    print("wrote",a.output)

if __name__=="__main__": main()
