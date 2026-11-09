#!/usr/bin/env python3
"""Side-by-side Q1 reference vs edge-cochain P1 defect benchmark."""
from __future__ import annotations
import argparse, csv, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from scripts.rgs_defect_benchmark import solve_case as solve_q1
from scripts.rgs_cochain_defect_benchmark import solve_cochain

def compare(levels=(9,17,33,65)):
    rows=[]
    for n in levels:
        for case in ("affine","none","single","dipole","volterra_edge","wedge_disclination","wedge_dipole"):
            q=solve_q1(n,case)
            for diagonal in ("sw_ne","se_nw"):
                r=solve_cochain(n,case,diagonal=diagonal)
                delta=abs(q["energy"]-r["energy"])
                scale=max(abs(q["energy"]),abs(r["energy"]),1e-30)
                rows.append({"n":n,"h":q["h"],"case":case,"diagonal":diagonal,
                    "q1_energy":q["energy"],"cochain_energy":r["energy"],
                    "absolute_energy_difference":delta,
                    "relative_energy_difference":delta/scale,
                    "q1_relative_residual":q["relative_free_residual"],
                    "cochain_relative_residual":r["relative_free_residual"]})
    return {"title":"Q1 reference versus edge-cochain P1 comparator",
      "interpretation":"same domain, material, eigenstrain source, and boundary data; different discretization families",
      "warning":"energy agreement is a numerical comparison, not a proof of equivalence or Mosco/Gamma convergence",
      "levels":list(levels),"orientation_audit":"both SW-NE and SE-NW diagonals","results":rows}

def main():
    p=argparse.ArgumentParser();p.add_argument("--out",default="artifacts/rgs_defect_comparison")
    a=p.parse_args();out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    report=compare();(out/"comparison.json").write_text(json.dumps(report,indent=2)+"\n")
    with (out/"comparison.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(report["results"][0]));w.writeheader();w.writerows(report["results"])
    print(json.dumps({"output":str(out),"rows":len(report["results"]),"levels":report["levels"]},indent=2))
if __name__=="__main__":main()
