#!/usr/bin/env python3
"""FEEC projection / discrete-adjoint benchmark driver (Phases A-D).

Reads a JSON config describing a list of cases; for every case and every
mesh level N it builds the cubical mesh, the global cell map, the
consistent FEEC masses, and runs ``ddr.feec_study.analyze_feec``.
Results are written to ``<out>/feec_results.json``.

Example:
    python run_feec_study.py configs/feec_default.json --out results/feec
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np

from ddr.mesh import CubicalMesh
from ddr.geometry import PullbackGeometry
from ddr.hodge import betti_numbers
from ddr.feec_mass import assemble_consistent_masses
from ddr.feec_study import analyze_feec


def run_case(case, outdir):
    dim = int(case["dim"])
    levels = [int(n) for n in case["levels"]]
    map_spec = case.get("map", {"type": "identity"})
    metric_spec = case.get("metric", {"type": "identity"})
    nq = int(case.get("nq", 4))
    nqf = int(case.get("nqf", 6))
    nq_l2 = int(case.get("nq_l2", 5))
    seed = int(case.get("seed", 0))
    spec_max = int(case.get("spectral_max_n", 500))
    entries = []
    for N in levels:
        t0 = time.time()
        mesh = CubicalMesh(N, dim)
        geometry = PullbackGeometry(mesh, map_spec, metric_spec,
                                    nq=nq, nqf=nqf)
        masses, mass_diag = assemble_consistent_masses(mesh, geometry)
        beta, _ = betti_numbers(mesh)
        spectral = max(mesh.nk) <= spec_max
        rec = analyze_feec(mesh, geometry, geometry.metric, masses, beta,
                           nqf=nqf, nq=nq_l2, seed=seed, spectral=spectral)
        rec["case"] = case.get("name", "case")
        rec["N"] = N
        rec["h"] = mesh.h_eff
        rec["betti"] = [int(b) for b in beta]
        rec["nk"] = mesh.nk
        rec["mass_assembly_diagnostics"] = mass_diag
        rec["spectral_enabled"] = spectral
        rec["elapsed_s"] = round(time.time() - t0, 3)
        entries.append(rec)
        print(f"  {case.get('name','case')} dim={dim} N={N}: "
              f"{rec['elapsed_s']}s spectral={spectral}", flush=True)
    return {"case": case.get("name", "case"), "dim": dim,
            "map": map_spec, "metric": metric_spec,
            "levels": entries}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("config")
    ap.add_argument("--out", default="results/feec")
    args = ap.parse_args()

    cfg = json.loads(Path(args.config).read_text())
    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)

    results = {"config": cfg, "cases": []}
    for case in cfg["cases"]:
        print(f"case {case.get('name','?')}: dim={case['dim']} "
              f"levels={case['levels']}", flush=True)
        results["cases"].append(run_case(case, outdir))

    path = outdir / "feec_results.json"
    path.write_text(json.dumps(results, indent=1, default=float))
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
