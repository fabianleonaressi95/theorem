#!/usr/bin/env python3
"""Build a direct exact-interval coercivity certificate for one curved-P3 mesh."""
from __future__ import annotations

import argparse
import hashlib
import json
import threading
from fractions import Fraction
from pathlib import Path
from time import perf_counter

from mpi4py import MPI
import basix
import basix.ufl
import numpy as np
from dolfinx import fem

from models.morandotti_direct_ipdg_certificate import (
    assemble_dolfinx_direct_ipdg_forms,
    certify_direct_ipdg_coercivity,
)
from models.morandotti_certified_curved_p3_forms import assemble_cell_volume_interval
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
    parser.add_argument(
        "--integration-method", choices=("neumann", "bernstein_residual"),
        default="neumann",
        help="certified rational volume integrator (T135 Bernstein residual is opt-in)",
    )
    parser.add_argument("--residual-expansion-order", type=int, default=2)
    parser.add_argument("--out", default="artifacts/morandotti_direct_ipdg/direct_coercivity.json")
    parser.add_argument("--diagnostic-cell", type=int, default=0,
                        help="profile this 1-based cell from the production-generated mesh and exit")
    parser.add_argument("--diagnostic-entry", type=int, default=55,
                        help="1-based upper-triangular P3 matrix entry to profile")
    parser.add_argument("--diagnostic-out", default="artifacts/morandotti_direct_ipdg/entry-diagnostic")
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

    # Diagnostic mode deliberately runs inside the production entry point:
    # it uses this exact make_mesh call, the same generated DOLFINx mesh,
    # and the same coordinate dofmap extraction as the global assembler.
    if args.diagnostic_cell:
        nc = mesh.topology.index_map(mesh.topology.dim).size_local
        if not 1 <= args.diagnostic_cell <= nc:
            raise ValueError(f"diagnostic cell must lie in 1..{nc}")
        if not 1 <= args.diagnostic_entry <= 55:
            raise ValueError("diagnostic entry must lie in 1..55")
        if args.integration_method != "neumann":
            raise ValueError("entry timing diagnostic currently profiles the production Neumann method")
        coordinate_dofmap = np.asarray(mesh.geometry.dofmaps[0], dtype=np.int32)
        cell_nodes = mesh.geometry.x[coordinate_dofmap[args.diagnostic_cell - 1], :2].copy()
        coordinate_hash = hashlib.sha256(
            np.ascontiguousarray(mesh.geometry.x).view(np.uint8)
        ).hexdigest()
        connectivity_hash = hashlib.sha256(
            np.ascontiguousarray(coordinate_dofmap).view(np.uint8)
        ).hexdigest()
        diagnostic_dir = Path(args.diagnostic_out)
        diagnostic_dir.mkdir(parents=True, exist_ok=True)
        events_path = diagnostic_dir / "events.jsonl"
        events_path.write_text("", encoding="utf-8")
        def emit(event):
            payload = {"cell": args.diagnostic_cell, **_jsonable(event)}
            line = json.dumps(payload, sort_keys=True)
            with events_path.open("a", encoding="utf-8") as stream:
                stream.write(line + "\\n")
            print("DIAGNOSTIC " + line, flush=True)
        def progress(event):
            if event.get("integration_numerator_index") in (None, args.diagnostic_entry):
                emit({"stage": "progress", **event})
        def timing(event):
            if event.get("numerator_index") in (None, args.diagnostic_entry):
                emit(event)
        metadata = {
            "mesh_parameters": {"radius": 1.0, "core_radius": 0.12,
                                "mesh_size": args.mesh_size, "distance": args.distance,
                                "seed": args.seed},
            "cell_count": nc, "cell_one_based": args.diagnostic_cell,
            "entry_one_based": args.diagnostic_entry,
            "coordinate_hash": coordinate_hash,
            "cell_dof_connectivity_hash": connectivity_hash,
            "cell_coordinate_nodes_hex": [[float(x).hex() for x in row] for row in cell_nodes],
            "scope": "one cell of the production-generated mesh; no global certificate",
        }
        (diagnostic_dir / "metadata.json").write_text(
            json.dumps(metadata, indent=2) + "\\n", encoding="utf-8")
        points = basix.create_element(
            basix.ElementFamily.P, basix.CellType.triangle, 3,
            basix.LagrangeVariant.equispaced,
        ).points
        started = perf_counter()
        try:
            local = assemble_cell_volume_interval(
                cell_nodes, points, absolute_tolerance=tolerance,
                max_depth=args.max_depth, progress_callback=progress,
                diagnostic_callback=timing, integration_method="neumann",
            )
            result = {
                **metadata, "status": "completed",
                "entry_interval": [str(local["matrix_interval"][
                    [(i, j) for i in range(10) for j in range(i, 10)][args.diagnostic_entry-1][0]
                ][
                    [(i, j) for i in range(10) for j in range(i, 10)][args.diagnostic_entry-1][1]
                ][0]), str(local["matrix_interval"][
                    [(i, j) for i in range(10) for j in range(i, 10)][args.diagnostic_entry-1][0]
                ][
                    [(i, j) for i in range(10) for j in range(i, 10)][args.diagnostic_entry-1][1]
                ][1])],
            }
        except Exception as exc:
            result = {**metadata, "status": "error",
                      "error_type": type(exc).__name__, "error": str(exc)}
        result["elapsed_seconds"] = perf_counter() - started
        (diagnostic_dir / "result.json").write_text(
            json.dumps(result, indent=2) + "\\n", encoding="utf-8")
        print(json.dumps(result, indent=2), flush=True)
        return

    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    progress_path = output.with_name("progress.json")
    phase = {"phase": "mesh_ready", "completed": 0, "total": 1}
    progress_lock = threading.Lock()
    def checkpoint(update):
        phase.update(update)
        payload = {**phase, "elapsed_seconds": perf_counter() - run_started}
        with progress_lock:
            progress_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        print("PROGRESS " + json.dumps(payload), flush=True)
    run_started = perf_counter()
    checkpoint(phase)
    stop_heartbeat = threading.Event()
    def heartbeat():
        while not stop_heartbeat.wait(15):
            checkpoint({"heartbeat": True})
    heartbeat_thread = threading.Thread(target=heartbeat, daemon=True)
    heartbeat_thread.start()
    try:
        start = perf_counter()
        checkpoint({"phase": "assembly_start"})
        assembled = assemble_dolfinx_direct_ipdg_forms(
            mesh, V, absolute_tolerance=tolerance, max_depth=args.max_depth,
            progress_callback=checkpoint,
            integration_method=args.integration_method,
            residual_expansion_order=args.residual_expansion_order,
        )
        assembly_seconds = perf_counter() - start
        checkpoint({"phase": "assembly_complete", "assembly_seconds": assembly_seconds,
                    "assembly_timings_seconds": assembled["assembly_timings_seconds"],
                    "assembly_counts": assembled["assembly_counts"]})
        certify_start = perf_counter()
        checkpoint({"phase": "ldl_start"})
        certificate = certify_direct_ipdg_coercivity(
            assembled["D_interval"], assembled["P_interval"],
            assembled["C_interval"], assembled["free_dofs"], alpha, kappa,
            progress_callback=checkpoint
        )
        certify_seconds = perf_counter() - certify_start
    finally:
        stop_heartbeat.set()
        heartbeat_thread.join(timeout=2)
    certify_seconds = perf_counter() - certify_start
    certificate.update({
        "cell_count": assembled["cell_count"],
        "assembly_counts": assembled["assembly_counts"],
        "assembly_timings_seconds": assembled["assembly_timings_seconds"],
        "coordinate_hash": assembled["coordinate_hash"],
        "cell_dof_connectivity_hash": assembled["cell_dof_connectivity_hash"],
        "integration_absolute_tolerance": str(tolerance),
        "integration_method": args.integration_method,
        "residual_expansion_order": args.residual_expansion_order,
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
    output.write_text(json.dumps(_jsonable(certificate), indent=2) + "\n",
                      encoding="utf-8")
    print(json.dumps(_jsonable(certificate), indent=2), flush=True)
    if not certificate["certified"]:
        raise SystemExit("direct finite-mesh coercivity certificate not established")


if __name__ == "__main__":
    main()
