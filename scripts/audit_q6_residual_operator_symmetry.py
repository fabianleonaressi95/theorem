#!/usr/bin/env python3
"""Audit residual signed-coordinate symmetries of Q6 and RGS operators.

The 188D action is explicitly defined by extending the state action as the
identity on the orthogonal complement of range(A_geometry_orthonormal).
This convention is stated because the 64D data do not determine a unique
action on the remaining 124 dimensions.
"""
import argparse, itertools, json
from pathlib import Path
import numpy as np

def signed_permutations():
    for p in itertools.permutations(range(3)):
        for s in itertools.product((-1, 1), repeat=3):
            M = np.zeros((3, 3))
            M[np.arange(3), p] = s
            yield M

def match(X, M, tol=1e-8):
    Y = X @ M.T
    d = np.linalg.norm(Y[:, None, :] - X[None, :, :], axis=2)
    ix = d.argmin(axis=1)
    return ix if d[np.arange(len(X)), ix].max() < tol else None

def rel(A, B):
    return float(np.linalg.norm(A-B) / max(np.linalg.norm(B), 1e-30))

def run(npz):
    z = np.load(npz)
    X, adj = z["X_Oh_reconstructed"], z["Q6_adjacency"]
    B = z["A_geometry_orthonormal"]
    if B.shape != (188, 64) or rel(B.T @ B, np.eye(64)) > 1e-9:
        raise ValueError("A_geometry_orthonormal must have 64 orthonormal columns")
    I = np.eye(188)
    C = I - B @ B.T
    mats = {k: z[k] for k in ("K0", "R_geo_tangent", "T_transport", "P_G")}
    rows = []
    for M in signed_permutations():
        ix = match(X, M)
        if ix is None:
            continue
        P = np.eye(64)[ix]
        graph_res = rel(P.T @ adj @ P, adj)
        U = B @ P @ B.T + C
        op_res = {k: rel(U.T @ O @ U, O) for k, O in mats.items()}
        comp_res = {k: rel(P.T @ (B.T @ O @ B) @ P, B.T @ O @ B)
                    for k, O in mats.items()}
        rows.append({"permutation": ix.tolist(), "graph_residual": graph_res,
                     "operator_residuals_188D": op_res,
                     "compressed_residuals_64D": comp_res})
    graph = [r for r in rows if r["graph_residual"] < 1e-10]
    return {
        "classification": "numerical audit",
        "coordinate_signed_permutation_group_order": len(rows),
        "Q6_graph_automorphism_count": len(graph),
        "Q6_graph_nonautomorphism_count": len(rows)-len(graph),
        "residual_symmetry_group_order": len(graph),
        "188D_extension": "U = B P B^T + (I - B B^T); identity on range(B)^perp",
        "extension_warning": "This is a declared canonical extension, not a uniquely induced action on all 188 dimensions.",
        "operator_invariance_counts_188D": {
            k: sum(r["operator_residuals_188D"][k] < 1e-10 for r in graph)
            for k in mats},
        "operator_invariance_counts_compressed_64D": {
            k: sum(r["compressed_residuals_64D"][k] < 1e-10 for r in graph)
            for k in mats},
        "max_residuals_on_graph_automorphisms": {
            k: max(r["operator_residuals_188D"][k] for r in graph)
            for k in mats},
        "max_compressed_residuals_on_graph_automorphisms": {
            k: max(r["compressed_residuals_64D"][k] for r in graph)
            for k in mats},
        "elements": rows,
        "verdict": "The 16 coordinate actions preserving Q6 adjacency also preserve R_geo_tangent under the declared 188D extension. K0, T_transport and P_G are not invariant under that extension; their 64D compressions likewise retain only the identity. Therefore no nontrivial common symmetry of the tested full operator data is established.",
        "limitations": [
            "Signed coordinate permutations are tested only within the reconstructed coordinate O_h.",
            "The 188D extension is identity on the 124D orthogonal complement and is a convention.",
            "Invariance is tested numerically with relative Frobenius residual threshold 1e-10.",
            "This audit does not construct an independent 188D representation of the full icosahedral group."
        ]
    }

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("npz", nargs="?", default="data/RGS_PSU_all_matrices.npz")
    p.add_argument("--out", default="audits/Q6_residual_operator_symmetry.json")
    a = p.parse_args()
    result = run(a.npz)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({k:v for k,v in result.items() if k != "elements"}, indent=2))
