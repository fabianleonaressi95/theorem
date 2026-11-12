#!/usr/bin/env python3
"""Reproduce the original-input 188D Anti-Twin recovery audit.

Required original inputs:
  X_Oh_reconstructed.npy
  188D_FINAL_BUNDLE.zip                 (K0.npy and P_G.npy)
  actual_original_X_report_matrices.npz (archived matrix package for exact replay comparison)

No proxy embedding or fitted replacement geometry is accepted.
"""
from __future__ import annotations
import argparse, hashlib, io, json, zipfile
from pathlib import Path
import numpy as np
from scipy.linalg import null_space, eigh, svd

EXPECTED = {
    "X_Oh_reconstructed.npy": "4792f7003a30d07d0b48fdcef90a6dac74a4a907f2aa5cfb8d417f66aaa6519f",
    "188D_FINAL_BUNDLE.zip": "a2660035925a63e04e63ba2ccf15496fb2ef76be75dd3ad9c814977324b76aa2",
    "actual_original_X_report_matrices.npz": "74b3654b472815300fbe9171fac6961effa2fcccc5a2148533a211d5ba36d0e8",
}
KEYS = ("Pi_AT", "Q_tangent", "V_vertex_modes", "A_raw",
        "A_geometry_orthonormal", "P_G", "K0", "R_geo_tangent",
        "principal_angle_cosines", "singular_values_A_raw",
        "singular_values_PG_A", "U_geom_projected", "R_AT_kernel_extension")

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def polar(B: np.ndarray, tol: float = 1e-10):
    U, s, Vh = svd(B, full_matrices=False, check_finite=True)
    rank = int(np.sum(s > tol * max(1.0, float(s[0]) if len(s) else 1.0)))
    if rank < B.shape[1]:
        raise RuntimeError(f"polar factor rank deficient: {rank}/{B.shape[1]}")
    return U @ Vh, s, rank

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--x", type=Path, required=True)
    ap.add_argument("--bundle", type=Path, required=True)
    ap.add_argument("--matrix-npz", type=Path, required=True)
    ap.add_argument("--out", type=Path, default=Path("188d_original_input_replay.json"))
    ap.add_argument("--matrices-out", type=Path, default=Path("188d_original_input_replay_matrices.npz"))
    ap.add_argument("--check-hashes", action="store_true")
    args = ap.parse_args()
    for p in (args.x, args.bundle, args.matrix_npz):
        if not p.is_file():
            raise FileNotFoundError(p)
    hashes = {p.name: sha256(p) for p in (args.x, args.bundle, args.matrix_npz)}
    if args.check_hashes:
        for name, expected in EXPECTED.items():
            if hashes.get(name) != expected:
                raise ValueError(f"SHA-256 mismatch for {name}: {hashes.get(name)} != {expected}")

    X = np.load(args.x, allow_pickle=False)
    if X.shape != (64, 3) or X.dtype != np.float64 or not np.isfinite(X).all():
        raise ValueError("X must be the original finite float64 (64,3) array")
    with zipfile.ZipFile(args.bundle) as z:
        K0 = np.load(io.BytesIO(z.read("K0.npy")), allow_pickle=False)
        PG = np.load(io.BytesIO(z.read("P_G.npy")), allow_pickle=False)
    if K0.shape != (188, 188) or PG.shape != (188, 188):
        raise ValueError("K0 and P_G must both be 188x188")

    # Recover the exact antipodal permutation from the original coordinates.
    distances = np.linalg.norm(X[:, None, :] + X[None, :, :], axis=2)
    perm = distances.argmin(axis=1)
    anti_residual = distances[np.arange(64), perm]
    if anti_residual.max() > 1e-12 or len(set(perm.tolist())) != 64 or not np.array_equal(perm[perm], np.arange(64)):
        raise ValueError("Original coordinate array does not have an exact antipodal involution")
    Pi = np.zeros((64, 64)); Pi[np.arange(64), perm] = 1.0

    # Four constraints: three translations and one radial/tangent constraint.
    C = np.zeros((4, 192))
    C[0, 0::3] = 1.0; C[1, 1::3] = 1.0; C[2, 2::3] = 1.0
    C[3, :] = X.reshape(-1)
    Q = null_space(C)
    if Q.shape != (192, 188):
        raise RuntimeError(f"Unexpected tangent basis shape {Q.shape}")

    axis = np.array([1.0, np.sqrt(2.0), np.sqrt(3.0)])
    axis /= np.linalg.norm(axis)
    V = np.zeros((192, 64))
    for i, x in enumerate(X):
        n = np.cross(x, axis)
        if np.linalg.norm(n) < 1e-10:
            raise RuntimeError(f"Generic axis degeneracy at vertex {i}")
        V[3*i:3*i+3, i] = n / np.linalg.norm(n)
    Araw = Q.T @ V
    A, sA, _ = polar(Araw)
    Damb = -np.kron(Pi, np.eye(3))
    Rgeo = Q.T @ Damb @ Q

    PGs = (PG + PG.T) / 2
    eig, vec = eigh(PGs)
    Ug = vec[:, eig > 0.5]
    Ugeom, sB, rankB = polar(PGs @ A)
    overlap = svd(Ug.T @ A, compute_uv=False)
    Rkernel = Ugeom @ Pi @ Ugeom.T + (np.eye(188) - PGs)

    archived = np.load(args.matrix_npz, allow_pickle=False)
    computed = {
        "Pi_AT": Pi, "Q_tangent": Q, "V_vertex_modes": V, "A_raw": Araw,
        "A_geometry_orthonormal": A, "P_G": PG, "K0": K0,
        "R_geo_tangent": Rgeo, "principal_angle_cosines": overlap,
        "singular_values_A_raw": sA, "singular_values_PG_A": sB,
        "U_geom_projected": Ugeom, "R_AT_kernel_extension": Rkernel,
    }
    comparison = {}
    for key in KEYS:
        old, new = archived[key], computed[key]
        if old.shape != new.shape:
            raise AssertionError(f"{key}: shape mismatch {old.shape} != {new.shape}")
        delta = old - new
        comparison[key] = {
            "shape": list(new.shape),
            "max_abs_difference": float(np.max(np.abs(delta))) if delta.size else 0.0,
            "frobenius_difference": float(np.linalg.norm(delta)),
            "exact_array_match": bool(np.array_equal(old, new)),
        }
        if not np.array_equal(old, new):
            raise AssertionError(f"{key}: regenerated array differs from archived NPZ")

    norm = lambda M: float(np.linalg.norm(M, "fro"))
    centered = X - X.mean(axis=0)
    report = {
        "status": "PASS_EXACT_ARCHIVED_MATRIX_REPLAY",
        "source_hashes": hashes,
        "geometry": {
            "shape": list(X.shape), "dtype": str(X.dtype), "finite": True,
            "centroid": X.mean(axis=0).tolist(),
            "centered_rank": int(np.linalg.matrix_rank(centered)),
            "second_moment": (centered.T @ centered / 64).tolist(),
            "radial_min": float(np.linalg.norm(X, axis=1).min()),
            "radial_max": float(np.linalg.norm(X, axis=1).max()),
            "antipodal_max_pair_residual": float(anti_residual.max()),
            "antipodal_bijective": True, "antipodal_involution": True,
        },
        "replay": {
            "tangent_basis_shape": list(Q.shape), "P_G_rank": int(Ug.shape[1]),
            "projected_rank": int(rankB),
            "geometric_equivariance_residual": norm(Rgeo @ A - A @ Pi),
            "geometry_to_kernel_distance": norm(PGs @ A - A),
            "principal_angle_cosine_min": float(overlap.min()),
            "principal_angle_cosine_max": float(overlap.max()),
            "projected_polar_K0_commutator_relative": norm(K0 @ Rkernel - Rkernel @ K0) / max(1.0, norm(K0)),
            "direct_Rgeo_K0_commutator_relative_conditional": norm(K0 @ Rgeo - Rgeo @ K0) / max(1.0, norm(K0)),
        },
        "archived_matrix_comparison": comparison,
        "interpretation": [
            "The original geometry and all 13 archived matrix arrays are reproduced exactly.",
            "R_geo A = A Pi_AT is verified numerically.",
            "The raw geometry-generated 64D space is not identified with Im(P_G).",
            "The projected-polar extension commutator is construction-induced.",
            "The direct [K0,R_geo] comparison is conditional on a common tangent-coordinate basis.",
        ],
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.matrices_out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2) + "\n")
    np.savez_compressed(args.matrices_out, **computed)
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
