#!/usr/bin/env python3
"""Reproducible audit of the discrete RGS -> football tangent-fibre maps."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import numpy as np
from models.football_shell import build_football_shell
from models.tangent_triplet_anisotropy import (
    build_rgs_shell_tangent_fibre_maps,
    push_triplett_to_shell_nodes,
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="data/rgs_188d/X_Oh_reconstructed.csv")
    parser.add_argument("--neighbors", type=int, default=16)
    parser.add_argument("--t2u-basis", default=None,
                        help="optional .npy file containing the audited 188x3 T2u basis")
    parser.add_argument("--triplett", default=None,
                        help="optional .npy file containing a 2x3 PRISM/G2 triplett")
    parser.add_argument("--out", default="reports/rgs_shell_tangent_fibre_transfer.json")
    args = parser.parse_args()

    data = np.genfromtxt(ROOT / args.source, delimiter=",", names=True)
    points = np.column_stack([data[k] for k in ("x", "y", "z")])
    mesh = build_football_shell()
    result = build_rgs_shell_tangent_fibre_maps(
        points, mesh, neighbors=args.neighbors
    )
    report = {
        "status": "COMPUTED_DISCRETE_TANGENT_FIBRE_MAP",
        "source": args.source,
        "source_points": int(len(points)),
        "shell_nodes": int(len(mesh["nodes"])),
        "shell_triangles": int(len(mesh["triangles"])),
        "neighbors": int(args.neighbors),
        "nodewise_rank": result["nodewise_ranks"],
        "minimum_nodewise_rank": result["minimum_nodewise_rank"],
        "maximum_tangency_residual": result["maximum_tangency_residual"],
        "source_constraint_residual": result["source_constraint_residual"],
        "source_basis_orthogonality": result["source_basis_orthogonality"],
        "transfer_diagnostics": result["transfer_diagnostics"],
        "classification": (
            "finite-mesh nodal bundle map; no continuum connection-preservation "
            "or physical constitutive validation is claimed"
        ),
    }
    tensors = None
    if args.t2u_basis:
        V = np.load(ROOT / args.t2u_basis)
        if args.triplett:
            T = np.load(ROOT / args.triplett)
            pushed = push_triplett_to_shell_nodes(T, result, V)
            tensors = pushed["tangent_tensors"]
            report["t2u_basis_shape"] = list(V.shape)
            report["triplett_gram"] = pushed["triplett_gram"].tolist()
            report["channel_map_ranks"] = [
                int(np.linalg.matrix_rank(U, tol=1e-9))
                for U in pushed["channel_maps"]
            ]
            report["pushed_tensor_min_eigenvalue"] = float(
                min(np.linalg.eigvalsh(A)[0] for A in tensors)
            )
        else:
            report["t2u_basis_shape"] = list(V.shape)
            report["note"] = "T2u basis loaded; supply --triplett to push a G2 Gram form."
    out = ROOT / args.out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n")
    np.savez_compressed(
        out.with_suffix(".npz"),
        ambient_maps=result["ambient_maps"],
        local_maps=result["local_maps"],
        tangent_frames=result["tangent_frames"],
        shell_normals=result["shell_normals"],
        source_tangent_basis=result["source_tangent_basis"],
        cartesian_transfer=result["cartesian_transfer"],
        **({"tangent_anisotropy_tensors": tensors} if tensors is not None else {}),
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
