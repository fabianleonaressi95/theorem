#!/usr/bin/env python3
"""Compare archived 188D K0/Q arrays across the RGS bundles.

This is a local binary audit: it does not regenerate K0 and never substitutes a
mock. It compares arrays extracted from A13/188D ZIPs with the canonical NPZ.
"""
from __future__ import annotations
import argparse, io, json, zipfile
from pathlib import Path
import numpy as np


def load_zip_arrays(path: Path) -> dict[str, np.ndarray]:
    out: dict[str, np.ndarray] = {}
    with zipfile.ZipFile(path) as zf:
        names = zf.namelist()
        # Direct NPY members (the historical 188D bundle commonly uses these).
        for name in names:
            base = Path(name).name
            if base in {"K0.npy", "Q.npy", "Q_tangent.npy"}:
                key = "K0" if base == "K0.npy" else ("Q" if base == "Q.npy" else "Q_tangent")
                try:
                    out.setdefault(key, np.load(io.BytesIO(zf.read(name)), allow_pickle=False))
                except Exception:
                    pass
        # A13 stores the tangent frame and operator in a nested NPZ.
        for name in names:
            if Path(name).suffix.lower() != ".npz":
                continue
            try:
                nested = np.load(io.BytesIO(zf.read(name)), allow_pickle=False)
                for key in ("K0", "Q", "Q_tangent"):
                    if key in nested and key not in out:
                        out[key] = np.asarray(nested[key])
            except Exception:
                continue
    return out


def compare(a: np.ndarray, b: np.ndarray) -> dict:
    if a.shape != b.shape:
        return {"same_shape": False, "shape_a": list(a.shape), "shape_b": list(b.shape)}
    d = np.asarray(a, dtype=np.float64) - np.asarray(b, dtype=np.float64)
    return {
        "same_shape": True,
        "dtype_a": str(a.dtype), "dtype_b": str(b.dtype),
        "exact_array_match": bool(np.array_equal(a, b)),
        "frobenius_difference": float(np.linalg.norm(d)),
        "max_abs_difference": float(np.max(np.abs(d))) if d.size else 0.0,
        "relative_frobenius_difference": float(np.linalg.norm(d) / max(1.0, np.linalg.norm(a))),
    }


def compare_q(a: np.ndarray, b: np.ndarray) -> dict:
    result = compare(a, b)
    if a.shape != b.shape or a.ndim != 2 or a.shape[0] != 192:
        return result
    Pa, Pb = a @ a.T, b @ b.T
    result["tangent_projector_frobenius_difference"] = float(np.linalg.norm(Pa - Pb))
    # If both are orthonormal bases of the same subspace, O=a.T@b is orthogonal
    # and b ~= a@O. This explicitly detects a basis rotation.
    O = a.T @ b
    result["basis_change_orthogonality_residual"] = float(np.linalg.norm(O.T @ O - np.eye(O.shape[0])))
    result["basis_change_reconstruction_residual"] = float(np.linalg.norm(b - a @ O))
    result["basis_change_matrix"] = O.tolist()
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--canonical-npz", type=Path, required=True,
                    help="RGS_PSU_all_matrices.npz containing K0 and Q_tangent")
    ap.add_argument("--a13-zip", type=Path, required=True,
                    help="A13_RGS_PSU_QLG_KAGGLE_BUNDLE.zip")
    ap.add_argument("--188d-zip", type=Path, required=True,
                    help="188D_FINAL_BUNDLE.zip")
    ap.add_argument("--out", type=Path, default=Path("K0_bundle_comparison.json"))
    args = ap.parse_args()

    with np.load(args.canonical_npz, allow_pickle=False) as z:
        target_k = np.asarray(z["K0"])
        target_q = np.asarray(z["Q_tangent"]) if "Q_tangent" in z else None

    report = {"status": "COMPLETED_BINARY_COMPARISON", "canonical_npz": str(args.canonical_npz),
              "bundles": {}, "target": {"K0_shape": list(target_k.shape),
              "K0_dtype": str(target_k.dtype),
              "Q_tangent_shape": list(target_q.shape) if target_q is not None else None}}
    for label, path in (("A13", args.a13_zip), ("188D_FINAL", args.__dict__["188d_zip"])):
        arrays = load_zip_arrays(path)
        entry = {"archive": str(path), "available_arrays": {k: list(v.shape) for k, v in arrays.items()}}
        if "K0" in arrays:
            entry["K0_vs_canonical"] = compare(target_k, arrays["K0"])
        else:
            entry["K0_vs_canonical"] = {"status": "K0_NOT_FOUND_IN_ARCHIVE"}
        q = arrays.get("Q_tangent", arrays.get("Q"))
        if target_q is not None and q is not None:
            entry["Q_vs_canonical"] = compare_q(target_q, q)
        else:
            entry["Q_vs_canonical"] = {"status": "Q_NOT_AVAILABLE_IN_BOTH"}
        report["bundles"][label] = entry

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
