#!/usr/bin/env python3
"""Reconstruct and export the first 188D RGS/Q6 Coulomb T2u triplet."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import numpy as np
from models.tangent_triplet_anisotropy import reconstruct_rgs_t2u_triplet


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="data/rgs_188d/X_Oh_reconstructed.csv")
    parser.add_argument("--basis-out", default="reports/rgs_q6_t2u_first_triplet.npy")
    parser.add_argument("--report-out", default="reports/rgs_q6_t2u_reconstruction.json")
    args = parser.parse_args()

    source = ROOT / args.source
    data = np.genfromtxt(source, delimiter=",", names=True)
    X = np.column_stack([data[k] for k in ("x", "y", "z")])
    result = reconstruct_rgs_t2u_triplet(X)

    basis_path = ROOT / args.basis_out
    report_path = ROOT / args.report_out
    basis_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    np.save(basis_path, result["basis"])
    np.savez_compressed(
        basis_path.with_suffix(".npz"),
        basis=result["basis"],
        triplet_projector=result["triplet_projector"],
        t2u_isotypic_projector=result["t2u_isotypic_projector"],
        source_tangent_basis=result["source_tangent_basis"],
        constrained_coulomb_hessian=result["constrained_coulomb_hessian"],
        t2u_eigenvalues=result["t2u_eigenvalues"],
    )
    report = {
        "source": args.source,
        "basis_shape": list(result["basis"].shape),
        "basis_file": args.basis_out,
        "arrays_file": str(Path(args.basis_out).with_suffix(".npz")),
        **result["diagnostics"],
    }
    report_path.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
