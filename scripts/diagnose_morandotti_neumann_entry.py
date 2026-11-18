#!/usr/bin/env python3
"""Isolate one curved-P3 volume entry and explain Neumann subdivision decisions."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from time import perf_counter

from mpi4py import MPI
import basix
from dolfinx import fem

from models.morandotti_certified_curved_p3_forms import (
    _cell_data, _add, _mul, _det_power,
)
from models.morandotti_certified_rational_integration import (
    integrate_rational_triangle_many,
    integrate_rational_triangle_bernstein_residual_many,
)
from scripts.rgs_morandotti_two_core_c0_ipdg import make_mesh


def encode(value):
    if isinstance(value, Fraction):
        return f"{value.numerator}/{value.denominator}"
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(v) for v in value]
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mesh-size", type=float, default=0.30)
    parser.add_argument("--distance", type=float, default=0.48)
    parser.add_argument("--seed", type=int, default=11)
    parser.add_argument("--cell", type=int, default=1, help="1-based mesh cell index")
    parser.add_argument("--entry", type=int, default=55, help="1-based upper-triangular P3 matrix entry")
    parser.add_argument("--tolerance", default="1/10000")
    parser.add_argument("--max-depth", type=int, default=24)
    parser.add_argument("--max-triangles", type=int, default=512)
    parser.add_argument("--out", default="artifacts/morandotti_neumann_diagnostic")
    args = parser.parse_args()

    if MPI.COMM_WORLD.size != 1:
        raise RuntimeError("diagnostic requires a serial mesh")
    tol = Fraction(args.tolerance)
    if tol <= 0:
        raise ValueError("tolerance must be positive")
    centers = ((-0.5 * args.distance, 0.0), (0.5 * args.distance, 0.0))
    mesh, _ = make_mesh(1.0, 0.12, centers, args.mesh_size,
                        MPI.COMM_WORLD, random_seed=args.seed)
    element = basix.create_element(
        basix.ElementFamily.P, basix.CellType.triangle, 3,
        basix.LagrangeVariant.equispaced,
    )
    points = element.points
    nc = mesh.topology.index_map(2).size_local
    if not 1 <= args.cell <= nc:
        raise ValueError(f"cell must lie in 1..{nc}")
    if not 1 <= args.entry <= 55:
        raise ValueError("entry must lie in 1..55")
    dofmaps = mesh.geometry.dofmaps[0]
    nodes = mesh.geometry.x[dofmaps[args.cell - 1], :2].copy()
    maps, basis, jac, adj, det, hessians, det5 = _cell_data(nodes, points)
    pairs = [(i, j) for i in range(10) for j in range(i, 10)]
    i, j = pairs[args.entry - 1]
    numerator = {}
    for a in range(2):
        for b in range(2):
            numerator = _add(numerator, _mul(hessians[i][a][b], hessians[j][a][b]))

    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)
    events_path = outdir / "neumann-events.jsonl"
    metadata = {
        "cell": args.cell, "cell_count": nc, "entry": args.entry,
        "basis_pair_zero_based": [i, j],
        "basis_pair_one_based": [i + 1, j + 1],
        "mesh_size": args.mesh_size, "distance": args.distance, "seed": args.seed,
        "tolerance": str(tol), "max_depth": args.max_depth,
        "max_triangles": args.max_triangles,
        "coordinate_nodes_hex": [[float(x).hex() for x in row] for row in nodes],
        "numerator_degree": max((a + b for a, b in numerator), default=0),
        "numerator_terms": len(numerator),
        "denominator_degree": max((a + b for a, b in det5), default=0),
        "denominator_terms": len(det5),
    }
    (outdir / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n")

    def diagnostic(event):
        with events_path.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(encode(event), sort_keys=True) + "\n")

    started = perf_counter()
    neumann = integrate_rational_triangle_many(
        [numerator], det5, absolute_tolerance=tol,
        max_depth=args.max_depth, max_triangles=args.max_triangles,
        diagnostic_callback=diagnostic,
    )[0]
    neumann_seconds = perf_counter() - started

    started = perf_counter()
    bernstein = integrate_rational_triangle_bernstein_residual_many(
        [numerator], det5, absolute_tolerance=tol,
        max_depth=args.max_depth,
    )[0]
    bernstein_seconds = perf_counter() - started

    result = {
        **metadata,
        "neumann": {
            "interval": [str(neumann[0]), str(neumann[1])],
            "accepted_leaves": neumann[2], "max_depth_used": neumann[3],
            "elapsed_seconds": neumann_seconds,
        },
        "bernstein_residual": {
            "interval": [str(bernstein[0]), str(bernstein[1])],
            "accepted_leaves": bernstein[2], "max_depth_used": bernstein[3],
            "elapsed_seconds": bernstein_seconds,
        },
        "intervals_overlap": max(neumann[0], bernstein[0]) <= min(neumann[1], bernstein[1]),
        "scope": "one cell and one local matrix entry only; no global IPDG certificate",
    }
    (outdir / "result.json").write_text(json.dumps(encode(result), indent=2) + "\n")
    print(json.dumps(encode(result), indent=2), flush=True)


if __name__ == "__main__":
    main()
