#!/usr/bin/env python3
"""Mesh-refined core-separation study for the Morandotti two-core C0-IPDG model."""
from __future__ import annotations
import argparse
import hashlib
import json
import sys
from pathlib import Path

import numpy as np
from mpi4py import MPI

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from models.morandotti_distance_refinement import summarize_distance_refinement
from scripts.rgs_morandotti_two_core_c0_ipdg import make_mesh, solve_level


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mesh-sizes", nargs="+", type=float, default=[0.08, 0.06, 0.045])
    parser.add_argument("--distance-values", nargs="+", type=float, default=[0.48, 0.56, 0.64, 0.72])
    parser.add_argument("--alpha", type=float, default=10.0)
    parser.add_argument("--young-modulus", type=float, default=1.0)
    parser.add_argument("--poisson-ratio", type=float, default=0.0)
    parser.add_argument("--out", default="artifacts/morandotti_distance_refinement/report.json")
    args = parser.parse_args()

    if not args.mesh_sizes or not np.isfinite(args.mesh_sizes).all() or any(h <= 0 for h in args.mesh_sizes):
        raise ValueError("mesh sizes must be finite and positive")
    if len(set(args.mesh_sizes)) != len(args.mesh_sizes):
        raise ValueError("mesh sizes must be unique")
    if not args.distance_values or not np.isfinite(args.distance_values).all():
        raise ValueError("distance values must be finite")
    if len(set(args.distance_values)) != len(args.distance_values):
        raise ValueError("distance values must be unique")
    if any(d <= 0.24 or d >= 1.76 for d in args.distance_values):
        raise ValueError("each separation must satisfy 2a < d < 2(R-a), with a=0.12 and R=1")

    records, mesh_metadata = [], []
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)

    for h in args.mesh_sizes:
        bundle = make_mesh(1.0, 0.12, ((-0.28, 0.0), (0.28, 0.0)), h, MPI.COMM_WORLD)
        mesh = bundle[0]
        reference_geometry = mesh.geometry.x.copy()
        dofmap_hash = hashlib.sha256(np.asarray(mesh.geometry.dofmap).tobytes()).hexdigest()
        level_rows = []
        for distance in args.distance_values:
            field_path = output.with_name(f"fields_h{h:.4f}_d{distance:.4f}.npz")
            result = solve_level(
                h, alpha=args.alpha, young_modulus=args.young_modulus,
                poisson_ratio=args.poisson_ratio, core_separation=distance,
                mesh_bundle=bundle, reference_geometry=reference_geometry,
                args_artifact_path=str(field_path),
            )
            matrix = np.asarray(result["M_laplacian"], dtype=float)
            records.append({"h": h, "distance": distance, "M_laplacian": matrix})
            level_rows.append({
                "distance": distance,
                "cells": result["cells"],
                "dofs": result["dofs"],
                "minimum_signed_corner_area": result["min_signed_corner_area"],
                "minimum_sampled_jacobian_determinant": result["min_sampled_jacobian_determinant"],
                "minimum_interaction_eigenvalue": result["min_eigenvalue_laplacian"],
                "interaction_matrix_symmetry_relative": result["laplacian_symmetry_relative"],
                "boundary_identity_relative_residual": result["boundary_identity_relative_residual"],
                "interior_facet_traction_jump_L2": {
                    name: case["interior_facet_traction_jump_L2"]
                    for name, case in result["reconstruction_cases"].items()
                },
                "field_export": str(field_path),
            })
            if result["min_signed_corner_area"] <= 0 or result["min_sampled_jacobian_determinant"] <= 0:
                raise RuntimeError(f"non-positive mesh Jacobian at h={h}, d={distance}")
            if result["laplacian_symmetry_relative"] > 1e-8:
                raise RuntimeError(f"interaction matrix lost symmetry at h={h}, d={distance}")
        mesh_metadata.append({
            "h_target": h,
            "cells_reference_mesh": int(mesh.topology.index_map(mesh.topology.dim).size_local),
            "geometry_dofmap_sha256": dofmap_hash,
            "reference_mesh_reused_for_all_distances": True,
            "levels": level_rows,
        })

    report = {
        "title": "Morandotti two-core interaction: mesh-refined separation sweep",
        "reference": "Cesana, Fabbrini, León Baldelli and Morandotti (2026), arXiv:2609.29614",
        "status": "finite-mesh numerical audit",
        "material": {
            "young_modulus": args.young_modulus, "poisson_ratio": args.poisson_ratio,
            "c0_ipdg_penalty_alpha": args.alpha, "core_radius": 0.12, "outer_radius": 1.0,
        },
        "protocol": {
            "mesh_sizes": args.mesh_sizes, "separations": args.distance_values,
            "reference_separation": 0.56, "reference_mesh_reused_at_each_h": True,
            "defect_data_orientation": "laboratory-fixed",
            "mpi": "serial only; distributed execution not audited",
        },
        "mesh_runs": mesh_metadata,
        "matrix_summary": summarize_distance_refinement(records),
        "limitations": [
            "finite set of mesh sizes and core separations only",
            "same reference mesh connectivity is deformed at fixed h; no remeshing comparison",
            "positive sampled Jacobians are not a formal all-points positivity certificate",
            "no continuum distance-decay law or mesh-independent limit is asserted",
            "no force-balance or material-validation claim is made",
        ],
    }
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
