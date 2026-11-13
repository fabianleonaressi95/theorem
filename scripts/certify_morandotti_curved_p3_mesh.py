#!/usr/bin/env python3
"""Run the exact interval T134 certificate on one generated curved-P3 mesh."""
from __future__ import annotations

import argparse
import json
from time import perf_counter
from fractions import Fraction
from pathlib import Path

from mpi4py import MPI
import basix
import basix.ufl
from dolfinx import fem

from models.morandotti_certified_curved_p3_forms import (
    assemble_dolfinx_mesh_interval_forms,
    certify_global_trace_bound,
)
from scripts.rgs_morandotti_two_core_c0_ipdg import make_mesh


def _jsonable(value):
    if isinstance(value, Fraction):
        return f"{value.numerator}/{value.denominator}"
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [_jsonable(v) for v in value]
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mesh-size", type=float, default=0.30)
    parser.add_argument("--distance", type=float, default=0.48)
    parser.add_argument("--seed", type=int, default=11)
    parser.add_argument("--bound", default="20")
    parser.add_argument("--tolerance", default="1/10000")
    parser.add_argument("--max-depth", type=int, default=24)
    parser.add_argument("--out", default="artifacts/morandotti_trace_constant/exact_certificate.json")
    args = parser.parse_args()

    if MPI.COMM_WORLD.size != 1:
        raise RuntimeError("exact curved-P3 interval certificate currently requires a serial mesh")
    if not (0.24 < args.distance < 1.76):
        raise ValueError("two-core distance must satisfy 0.24 < distance < 1.76")
    tolerance = Fraction(args.tolerance)
    bound = Fraction(args.bound)
    if tolerance <= 0 or bound <= 0:
        raise ValueError("bound and integration tolerance must be positive")

    centers = ((-0.5*args.distance, 0.0), (0.5*args.distance, 0.0))
    mesh, _ = make_mesh(1.0, 0.12, centers, args.mesh_size,
                        MPI.COMM_WORLD, random_seed=args.seed)
    element = basix.ufl.element(
        "Lagrange", "triangle", 3,
        lagrange_variant=basix.LagrangeVariant.equispaced,
    )
    V = fem.functionspace(mesh, element)
    t0 = perf_counter()
    assembled = assemble_dolfinx_mesh_interval_forms(
        mesh, V, absolute_tolerance=tolerance, max_depth=args.max_depth,
    )
    assembly_seconds = perf_counter() - t0

    t1 = perf_counter()
    certificate = certify_global_trace_bound(
        assembled["D_interval"], assembled["H_interval"],
        assembled["free_dofs"], bound,
    )
    psd_seconds = perf_counter() - t1
    certificate.update({
        "cell_count": assembled["cell_count"],
        "interior_facet_count": assembled["interior_facet_count"],
        "boundary_facet_count": assembled["boundary_facet_count"],
        "assembly_timings_seconds": assembled.get("assembly_timings_seconds", {}),
        "assembly_counts": assembled.get("assembly_counts", {}),
        "assembly": "exact-rational local curved-P3 Hessian blocks with certified volume/facet integral enclosures",
    })
    payload = {
        "title": "T134 exact curved-P3 finite-mesh trace certificate",
        "status": "certified" if certificate["certified"] else "not_certified",
        "mesh_size_target": args.mesh_size,
        "core_distance": args.distance,
        "seed": args.seed,
        "profiling_mesh": args.mesh_size,
        "integration_absolute_tolerance": str(tolerance),
        "timings_seconds": {"assembly_and_interval_integration": assembly_seconds, "volume_cells": assembled.get("assembly_timings_seconds", {}).get("volume_cells"), "boundary_facets": assembled.get("assembly_timings_seconds", {}).get("boundary_facets"), "interior_facets": assembled.get("assembly_timings_seconds", {}).get("interior_facets"), "global_interval_PSD": psd_seconds, "LDL_exact_arithmetic": certificate.get("ldl_seconds"), "LDL_fill_updates": certificate.get("ldl_fill_updates"), "LDL_max_active_degree": certificate.get("ldl_max_active_degree"), "total": assembly_seconds + psd_seconds},
        **certificate,
        "scope": "one finite generated mesh; no mesh-uniform conclusion",
    }
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(_jsonable(payload), indent=2) + "\n",
                      encoding="utf-8")
    print(json.dumps(_jsonable(payload), indent=2), flush=True)
    if not certificate["certified"]:
        raise SystemExit("C_star*D-H interval PSD certificate not established")


if __name__ == "__main__":
    main()
