"""Experiment driver: refinement sequences, stress tests, JSON output."""
from __future__ import annotations

import copy
import json
import os
import time

import numpy as np

from .mesh import CubicalMesh
from .geometry import PullbackGeometry
from . import hodge


def _resolve_map(map_spec, mesh):
    """Return a concrete map spec for this mesh (handles amplitude_h)."""
    s = dict(map_spec)
    ah = s.pop("amplitude_h", None)
    if ah is not None:
        a0, gamma = ah
        s["type"] = s.get("type", "sinusoid")
        s["amplitude"] = float(a0) * mesh.h_eff ** float(gamma)
    return s


def run_one(dim, N, map_spec, metric_spec, eig_opts=None, quad=None):
    """Build mesh+geometry+operators and return a result dict."""
    mesh = CubicalMesh(N, dim)
    ms = _resolve_map(map_spec, mesh)
    quad = quad or {}
    geo = PullbackGeometry(mesh, ms, metric_spec,
                           nq=quad.get("nq", 5), nqf=quad.get("nqf", 4))
    H = hodge.hodge_matrices(mesh, geo.M)
    res = hodge.algebraic_residuals(mesh, geo.M, H)
    beta, rk = hodge.betti_numbers(mesh)
    sp = hodge.spectrum(mesh, H, geo.M, **(eig_opts or {}))
    mstats = hodge.inner_product_stats(geo.M)

    spectra = {}
    for k, s in sp.items():
        spectra[str(k)] = {
            "n": s["n"],
            "eigs_small": s["eigs_small"],
            "eigs_large": s["eigs_large"],
            "kernel_num": s["kernel_num"],
            "betti": beta[k],
            "kernel_matches_betti": bool(s["kernel_num"] == beta[k]),
            "lambda_min_pos": s["lambda_min_pos"],
            "lambda_max": s["lambda_max"],
            "cond_effective": s["cond_effective"],
            "max_eig_resid": s["max_eig_resid"],
        }

    return {
        "dim": dim,
        "N": (list(mesh.Ns) if isinstance(N, (list, tuple)) else N),
        "h": mesh.h_eff,
        "nk": mesh.nk,
        "euler": mesh.euler_characteristic,
        "map_resolved": {k2: v for k2, v in ms.items()},
        "metric": metric_spec,
        "geometry": geo.geo,
        "inner_products": mstats,
        "algebraic_residuals": res,
        "betti": beta,
        "d_ranks": rk,
        "spectra": spectra,
    }


def run_experiment(exp, eig_opts=None, quad=None):
    """Run one experiment entry from the config.

    Supported keys
    --------------
    name        : str
    dim         : 2 or 3
    Ns          : list of refinement levels (or 'sweep' handled separately)
    map         : DomainMap spec (may contain amplitude_h)
    metric      : AmbientMetric spec
    sweep       : optional dict for parameter sweeps:
        {"param": "map.amplitude"|"metric.beta"|..., "values": [...]}
                  -> runs a single N (exp["N"]) per value
    """
    name = exp.get("name", "exp")
    dim = int(exp["dim"])
    metric = exp.get("metric", {"type": "identity"})
    base_map = exp.get("map", {"type": "identity"})
    runs = []

    if "sweep" in exp:
        sw = exp["sweep"]
        path = sw["param"].split(".")          # e.g. ["map","amplitude"]
        N = exp["N"]
        for val in sw["values"]:
            m = copy.deepcopy(base_map)
            mt = copy.deepcopy(metric)
            target = m if path[0] == "map" else mt
            target[path[1]] = val
            t0 = time.time()
            r = run_one(dim, N, m, mt, eig_opts, quad)
            r["sweep_param"] = sw["param"]
            r["sweep_value"] = val
            r["runtime_s"] = time.time() - t0
            runs.append(r)
    else:
        for N in exp["Ns"]:
            t0 = time.time()
            r = run_one(dim, N, base_map, metric, eig_opts, quad)
            r["runtime_s"] = time.time() - t0
            runs.append(r)

    return {"name": name, "dim": dim, "runs": runs}


def run_config(cfg, outdir):
    os.makedirs(outdir, exist_ok=True)
    eig_opts = cfg.get("eigen", {})
    quad = cfg.get("quadrature", {})
    results = []
    for exp in cfg["experiments"]:
        print(f"[run] {exp.get('name')}: dim={exp['dim']}", flush=True)
        results.append(run_experiment(exp, eig_opts=eig_opts, quad=quad))
        for r in results[-1]["runs"]:
            print(f"      N={r['N']} h={r['h']:.4g} "
                  f"min_detJ={r['geometry']['min_det_jac']:.4g} "
                  f"({r['runtime_s']:.1f}s)", flush=True)
    payload = {
        "config": cfg,
        "results": results,
        "notes": {
            "epistemic_status": (
                "All entries under 'algebraic_residuals', 'betti', "
                "'kernel_num', 'geometry' and 'spectra' are direct "
                "numerical observations on the discrete level. "
                "Convergence of eigenvalues with h is reported as an "
                "indicator only; it is NOT evidence of Mosco convergence "
                "of the underlying bilinear forms."
            ),
        },
    }
    path = os.path.join(outdir, "results.json")
    with open(path, "w") as f:
        json.dump(payload, f, indent=1, default=_json_default)
    print(f"[done] wrote {path}")
    return payload


def _json_default(o):
    if isinstance(o, (np.floating, np.integer)):
        return o.item()
    if isinstance(o, np.ndarray):
        return o.tolist()
    if isinstance(o, float) and (np.isnan(o) or np.isinf(o)):
        return str(o)
    raise TypeError(f"not serializable: {type(o)}")
