#!/usr/bin/env python3
"""Independent-Gmsh-remeshing audit for selected Morandotti two-core separations.

Unlike the fixed-connectivity refinement study, every (h, d) pair gets a
fresh Gmsh mesh generated directly at that core separation.
"""
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

from scripts.rgs_morandotti_two_core_c0_ipdg import make_mesh, solve_level


def mesh_fingerprint(mesh):
    """Fingerprint coordinates and geometry connectivity of one fresh mesh."""
    digest = hashlib.sha256()
    digest.update(np.ascontiguousarray(mesh.geometry.x).tobytes())
    digest.update(np.ascontiguousarray(mesh.geometry.dofmap).tobytes())
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mesh-sizes", nargs="+", type=float, default=[0.08, 0.06, 0.045])
    parser.add_argument("--distance-values", nargs="+", type=float, default=[0.48, 0.56])
    parser.add_argument("--mesh-seeds", nargs="+", type=int, default=[11, 29, 47])
    parser.add_argument("--alpha", type=float, default=10.0)
    parser.add_argument("--young-modulus", type=float, default=1.0)
    parser.add_argument("--poisson-ratio", type=float, default=0.0)
    parser.add_argument("--out", default="artifacts/morandotti_independent_remeshing/report.json")
    args = parser.parse_args()

    if MPI.COMM_WORLD.size != 1:
        raise RuntimeError("independent-remeshing audit is serial; distributed execution is not audited")
    if not args.mesh_sizes or not np.isfinite(args.mesh_sizes).all() or any(h <= 0 for h in args.mesh_sizes):
        raise ValueError("mesh sizes must be finite and positive")
    if len(set(args.mesh_sizes)) != len(args.mesh_sizes):
        raise ValueError("mesh sizes must be unique")
    if not args.distance_values or not np.isfinite(args.distance_values).all():
        raise ValueError("distance values must be finite")
    if len(set(args.distance_values)) != len(args.distance_values):
        raise ValueError("distance values must be unique")
    if not args.mesh_seeds or len(set(args.mesh_seeds)) != len(args.mesh_seeds):
        raise ValueError("mesh seeds must be a non-empty list of unique integers")
    if any(d <= 0.24 or d >= 1.76 for d in args.distance_values):
        raise ValueError("each separation must satisfy 2a < d < 2(R-a), with a=0.12 and R=1")

    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    runs, groups = [], {}

    # A new Gmsh model and mesh are constructed for every (h, d) pair.
    for distance in args.distance_values:
        centers = ((-0.5 * distance, 0.0), (0.5 * distance, 0.0))
        for h in args.mesh_sizes:
            for seed in args.mesh_seeds:
                bundle = make_mesh(1.0, 0.12, centers, h, MPI.COMM_WORLD, random_seed=seed)
                mesh = bundle[0]
                reference_geometry = mesh.geometry.x.copy()
                fingerprint = mesh_fingerprint(mesh)
                field_path = output.with_name(f"fields_h{h:.4f}_d{distance:.4f}_seed{seed}.npz")

            result = solve_level(
                h,
                alpha=args.alpha,
                young_modulus=args.young_modulus,
                poisson_ratio=args.poisson_ratio,
                centers=centers,
                core_separation=None,
                mesh_bundle=bundle,
                reference_geometry=reference_geometry,
                args_artifact_path=str(field_path),
            )
            matrix = np.asarray(result["M_laplacian"], dtype=float)
            key = f"d{distance:.4f}_h{h:.4f}"
            groups.setdefault(key, []).append({"seed": seed, "matrix": matrix})
            cross = matrix[1:3, 4:6]
            self_block = matrix[1:3, 1:3]
            denominator = abs(matrix[1, 4]) + abs(matrix[2, 5])
            anisotropy = float((matrix[1, 4] - matrix[2, 5]) / denominator) if denominator else 0.0
            runs.append({
                "h_target": h,
                "mesh_seed": seed,
                "signed_anisotropy_A_d": anisotropy,
                "normalized_coupling_C_d": float(np.linalg.norm(cross, "fro") / max(np.linalg.norm(self_block, "fro"), 1e-300)),
                "distance": distance,
                "cells": result["cells"],
                "dofs": result["dofs"],
                "fresh_mesh_fingerprint_sha256": fingerprint,
                "fresh_mesh_generated_for_this_pair": True,
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

    ensemble_summary = {}
    for key, samples in groups.items():
        matrices = np.stack([sample["matrix"] for sample in samples])
        mean_matrix = np.mean(matrices, axis=0)
        deviations = [
            float(np.linalg.norm(matrix - mean_matrix, "fro") / max(np.linalg.norm(mean_matrix, "fro"), 1e-300))
            for matrix in matrices
        ]
        ensemble_summary[key] = {
            "realization_count": len(samples),
            "seeds": [sample["seed"] for sample in samples],
            "matrix_mean": mean_matrix.tolist(),
            "matrix_entrywise_std": np.std(matrices, axis=0, ddof=1).tolist() if len(samples) > 1 else np.zeros_like(mean_matrix).tolist(),
            "relative_frobenius_deviation_from_ensemble_mean": deviations,
            "relative_frobenius_deviation_max": max(deviations),
            "relative_frobenius_deviation_rms": float(np.sqrt(np.mean(np.square(deviations)))),
        }

    report = {
        "title": "Morandotti two-core interaction: independent remeshing audit",
        "reference": "Cesana, Fabbrini, León Baldelli and Morandotti (2026), arXiv:2609.29614",
        "status": "finite-mesh numerical audit with independent Gmsh meshes",
        "material": {
            "young_modulus": args.young_modulus,
            "poisson_ratio": args.poisson_ratio,
            "c0_ipdg_penalty_alpha": args.alpha,
            "core_radius": 0.12,
            "outer_radius": 1.0,
        },
        "protocol": {
            "mesh_sizes": args.mesh_sizes,
            "separations": args.distance_values,
            "fresh_mesh_per_pair_and_seed": True,
            "mesh_seeds": args.mesh_seeds,
            "realizations_per_mesh_size_and_separation": len(args.mesh_seeds),
            "mesh_generation": "Gmsh is initialized and a new geometry/mesh is generated independently for every (h, d) pair",
            "geometry_mapping": "identity reference-to-target center map; no inherited connectivity from another separation or mesh level",
            "defect_data_orientation": "laboratory-fixed",
            "mpi": "serial only; distributed execution not audited",
        },
        "runs": runs,
        "independent_realization_ensemble": ensemble_summary,
        "limitations": [
            "finite set of mesh sizes and core separations only",
            "independent remeshing changes mesh topology and node placement; differences combine discretization and mesh-realization effects",
            "positive sampled Jacobians are not a formal all-points positivity certificate",
            "no continuum distance-decay law or mesh-independent limit is asserted",
            "no force-balance, Frank-Burgers constitutive, or material-validation claim is made",
        ],
    }
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
