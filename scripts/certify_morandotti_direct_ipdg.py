#!/usr/bin/env python3
"""Build a direct exact-interval coercivity certificate for one curved-P3 mesh."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from time import perf_counter

from mpi4py import MPI
import basix
import basix.ufl
from dolfinx import fem

from models.morandotti_direct_ipdg_certificate import (
    assemble_dolfinx_direct_ipdg_forms,
    certify_direct_ipdg_coercivity,
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
    parser.add_argument("--alpha", default="40")
    parser.add_argument("--kappa", default="1/1000")
    parser.add_argument("--tolerance", default="1/10000")
    parser.add_argument("--max-depth", type=int, default=24)
    parser.add_argument("--out", default="artifacts/morandotti_direct_ipdg/direct_coercivity.json")
    args = parser.parse_args()

    if MPI.COMM_WORLD.size != 1:
        raise RuntimeError("direct interval certificate currently requires a serial mesh")
    if not (0.24 < args.distance < 1.76):
        raise ValueError("two-core distance must satisfy 0.24 < distance < 1.76")
    tolerance, alpha, kappa = (
        Fraction(args.tolerance), Fraction(args.alpha), Fraction(args.kappa)
    )
    if tolerance <= 0 or alpha <= 0 or kappa <= 0:
        raise ValueError("tolerance, alpha and kappa must be positive")

    centers = ((-0.5*args.distance, 0.0), (0.5*args.distance, 0.0))
    mesh, _ = make_mesh(1.0, 0.12, centers, args.mesh_size,
                        MPI.COMM_WORLD, random_seed=args.seed)
    element = basix.ufl.element(
        "Lagrange", "triangle", 3,
        lagrange_variant=basix.LagrangeVariant.equispaced,
    )
    V = fem.functionspace(mesh, element)

    start = perf_counter()
    assembled = assemble_dolfinx_direct_ipdg_forms(
        mesh, V, absolute_tolerance=tolerance, max_depth=args.max_depth
    )
    assembly_seconds = perf_counter() - start
    certify_start = perf_counter()
    certificate = certify_direct_ipdg_coercivity(
        assembled["D_interval"], assembled["P_interval"],
        assembled["C_interval"], assembled["free_dofs"], alpha, kappa
    )
    certify_seconds = perf_counter() - certify_start
    certificate.update({
        "cell_count": assembled["cell_count"],
        "assembly_counts": assembled["assembly_counts"],
        "assembly_timings_seconds": assembled["assembly_timings_seconds"],
        "coordinate_hash": assembled["coordinate_hash"],
        "cell_dof_connectivity_hash": assembled["cell_dof_connectivity_hash"],
        "integration_absolute_tolerance": str(tolerance),
        "max_subdivision_depth": args.max_depth,
        "mesh_parameters": {
            "mesh_size_target": args.mesh_size,
            "core_distance": args.distance,
            "seed": args.seed,
        },
        "timings_seconds": {
            "assembly_and_interval_integration": assembly_seconds,
            "strict_interval_LDL": certify_seconds,
            "total": assembly_seconds + certify_seconds,
        },
        "scope": "one fixed generated curved-P3 mesh; no mesh-uniform conclusion",
    })
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(_jsonable(certificate), indent=2) + "\n",
                      encoding="utf-8")
    print(json.dumps(_jsonable(certificate), indent=2), flush=True)
    if not certificate["certified"]:
        raise SystemExit("direct finite-mesh coercivity certificate not established")


if __name__ == "__main__":
    main()
