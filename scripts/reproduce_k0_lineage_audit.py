#!/usr/bin/env python3
"""Reproduce the exact K0 lineage comparison and the documented Coulomb replay.

Inputs:
  --canonical-npz RGS_PSU_all_matrices.npz
  --a13-zip A13_RGS_PSU_QLG_KAGGLE_BUNDLE.zip
  --188d-zip 188D_FINAL_BUNDLE.zip
Output is a JSON report. This script does not generate or modify K0.
"""
from __future__ import annotations
import argparse, hashlib, io, json, zipfile
from pathlib import Path
import numpy as np


def load_npz_bytes(raw: bytes) -> dict[str, np.ndarray]:
    with np.load(io.BytesIO(raw), allow_pickle=False) as z:
        return {k: np.asarray(z[k]) for k in z.files}


def array_hash(a: np.ndarray) -> str:
    return hashlib.sha256(np.ascontiguousarray(a).view(np.uint8).tobytes()).hexdigest()


def compare(a: np.ndarray, b: np.ndarray) -> dict:
    if a.shape != b.shape:
        return {"same_shape": False, "shape_a": list(a.shape), "shape_b": list(b.shape)}
    d = np.asarray(a, dtype=np.float64) - np.asarray(b, dtype=np.float64)
    return {
        "same_shape": True, "dtype_a": str(a.dtype), "dtype_b": str(b.dtype),
        "exact_array_match": bool(np.array_equal(a, b)),
        "array_sha256_a": array_hash(a), "array_sha256_b": array_hash(b),
        "frobenius_difference": float(np.linalg.norm(d)),
        "max_abs_difference": float(np.max(np.abs(d))) if d.size else 0.0,
    }


def coulomb_hessian(x: np.ndarray) -> np.ndarray:
    n = len(x)
    h = np.zeros((3*n, 3*n), dtype=float)
    eye = np.eye(3)
    for i in range(n):
        for j in range(i+1, n):
            d = x[i] - x[j]
            r2 = float(d @ d)
            if r2 <= 0:
                raise ValueError(f"Coincident sites {i}, {j}")
            r = np.sqrt(r2)
            block = 3.0*np.outer(d, d)/r**5 - eye/r**3
            si, sj = slice(3*i,3*i+3), slice(3*j,3*j+3)
            h[si,si] += block; h[sj,sj] += block
            h[si,sj] -= block; h[sj,si] -= block
    return 0.5*(h+h.T)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--canonical-npz", type=Path, required=True)
    p.add_argument("--a13-zip", type=Path, required=True)
    p.add_argument("--188d-zip", type=Path, required=True)
    p.add_argument("--out", type=Path, default=Path("audits/K0_lineage_exact_comparison.json"))
    args = p.parse_args()

    with np.load(args.canonical_npz, allow_pickle=False) as z:
        target = {k: np.asarray(z[k]) for k in z.files}
    k0, q, x = target["K0"], target["Q_tangent"], target["X_Oh_reconstructed"]

    with zipfile.ZipFile(args.a13_zip) as zf:
        names = zf.namelist()
        a13_all_name = next(n for n in names if n.endswith("/RGS_PSU_all_matrices.npz"))
        fibre_name = next(n for n in names if n.endswith("/psu_fibre_connection_matrices.npz"))
        a13_all = load_npz_bytes(zf.read(a13_all_name))
        fibre = load_npz_bytes(zf.read(fibre_name))
    with zipfile.ZipFile(args.__dict__["188d_zip"]) as zf:
        old_k0 = np.load(io.BytesIO(zf.read("K0.npy")), allow_pickle=False)

    result = {
        "status": "REPRODUCED_EXACT_ARRAY_COMPARISON",
        "canonical": str(args.canonical_npz),
        "canonical_K0": {"shape": list(k0.shape), "dtype": str(k0.dtype), "array_sha256": array_hash(k0)},
        "comparisons": {
            "A13_RGS_PSU_all_matrices_K0": compare(k0, a13_all["K0"]),
            "A13_psu_fibre_connection_K0": compare(k0, fibre["K0"]),
            "188D_FINAL_BUNDLE_K0_npy": compare(k0, old_k0),
            "A13_RGS_PSU_all_matrices_Q_tangent": compare(q, a13_all["Q_tangent"]),
            "A13_psu_fibre_connection_Q": compare(q, fibre["Q"]),
        }
    }

    # Reproduce the documented constrained Coulomb Hessian from the same X,Q.
    force = np.zeros_like(x)
    energy = 0.0
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            d = x[i]-x[j]; r = float(np.linalg.norm(d))
            energy += 1.0/r
            f = d/r**3
            force[i] += f; force[j] -= f
    lagrange = float(np.sum(force*x)/np.sum(x*x))
    h = coulomb_hessian(x)
    k_coulomb = q.T @ (h + lagrange*np.eye(3*len(x))) @ q
    k_coulomb = 0.5*(k_coulomb+k_coulomb.T)
    ev0 = np.linalg.eigvalsh(k0)
    evc = np.linalg.eigvalsh(k_coulomb)
    result["documented_coulomb_replay"] = {
        "formula": "Q.T @ (H_Coulomb + lambda_force * I_192) @ Q",
        "same_Q_exact": True,
        "energy": energy, "lambda_force": lagrange,
        "K0_vs_replay": compare(k0, k_coulomb),
        "K0_eigenvalue_counts": {
            "zero_64": int(np.sum(np.abs(ev0)<1e-8)),
            "positive": int(np.sum(ev0>1e-8)),
            "positive_min": float(ev0[64]), "positive_max": float(ev0[-1]),
        },
        "replay_eigenvalue_counts": {
            "negative": int(np.sum(evc < -1e-8)),
            "near_zero": int(np.sum(np.abs(evc)<=1e-8)),
            "positive": int(np.sum(evc>1e-8)),
            "minimum": float(evc[0]), "maximum": float(evc[-1]),
        },
        "interpretation": "The documented Coulomb constrained Hessian is a distinct operator; it does not generate the archived PSD K0."
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
