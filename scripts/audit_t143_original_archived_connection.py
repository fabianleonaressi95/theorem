#!/usr/bin/env python3
"""Replay the archived RGS fibre links under p(g)=g xor 7.

This audit reads the ORIGINAL edges, R_SO3 and U_SU2 arrays.  It does not
reconstruct rotations from X.  Edge rows are interpreted as stored oriented
links edges[k,:2]; the third column is retained as metadata only.
"""
import argparse, json
from pathlib import Path
import numpy as np

N = 64
P = np.arange(N, dtype=int) ^ 7
I3, I2 = np.eye(3), np.eye(2, dtype=complex)


def norm(a):
    return float(np.linalg.norm(a, ord="fro"))


def audit(edges, R, U, X=None, squares=None):
    edges = np.asarray(edges, dtype=int)
    R = np.asarray(R, dtype=float)
    U = np.asarray(U, dtype=complex)
    if edges.shape != (192, 3) or R.shape != (192, 3, 3) or U.shape != (192, 2, 2):
        raise ValueError(f"bad shapes: edges={edges.shape}, R={R.shape}, U={U.shape}")
    if np.any(edges[:, :2] < 0) or np.any(edges[:, :2] >= N):
        raise ValueError("edge endpoint outside 0..63")
    lookup = {}
    for k, (g, h, _) in enumerate(edges):
        key = (int(g), int(h))
        if key in lookup or (key[1], key[0]) in lookup:
            raise ValueError(f"duplicate undirected edge {key}")
        lookup[key] = k

    rows = []
    missing = []
    for k, (g0, h0, _) in enumerate(edges):
        g, h = int(g0), int(h0)
        pg, ph = int(P[g]), int(P[h])
        if (pg, ph) in lookup:
            kp, reversed_orientation = lookup[(pg, ph)], False
        elif (ph, pg) in lookup:
            kp, reversed_orientation = lookup[(ph, pg)], True
        else:
            missing.append([g, h, pg, ph])
            continue
        Rp = R[kp].T if reversed_orientation else R[kp]
        Up = U[kp].conj().T if reversed_orientation else U[kp]
        er = norm(Rp - R[k])
        eu = min(norm(Up-U[k]), norm(Up+U[k]))
        # The sign relating the two SU(2) lifts, after orientation correction.
        sign = 1 if norm(Up-U[k]) <= norm(Up+U[k]) else -1
        rows.append((k, kp, reversed_orientation, er, eu, sign))

    if missing:
        raise ValueError(f"antipodal image missing for {len(missing)} links: {missing[:5]}")
    so3 = np.array([x[3] for x in rows])
    spin = np.array([x[4] for x in rows])
    signs = np.array([x[5] for x in rows], dtype=int)
    result = {
      "status": "DIRECT_ARCHIVED_LINK_REPLAY",
      "source_arrays": {"edges": list(edges.shape), "R_SO3": list(R.shape), "U_SU2": list(U.shape)},
      "antipode": "p(g)=g xor 7",
      "links": {
        "count": len(rows),
        "orientation_reversed_count": int(sum(x[2] for x in rows)),
        "SO3_max_frobenius_residual": float(so3.max()),
        "SO3_rms_frobenius_residual": float(np.sqrt(np.mean(so3**2))),
        "SU2_projective_max_frobenius_residual": float(spin.max()),
        "SU2_projective_rms_frobenius_residual": float(np.sqrt(np.mean(spin**2))),
        "lift_sign_plus_count": int(np.sum(signs == 1)),
        "lift_sign_minus_count": int(np.sum(signs == -1)),
        "single_global_lift_sign": bool(np.all(signs == signs[0])),
        "edge_map_is_involution": bool(all(rows[rows[k][1]][1] == k for k in range(len(rows))))
      },
      "matrix_integrity": {
        "SO3_orthogonality_max": float(max(norm(r.T@r-I3) for r in R)),
        "SO3_determinant_max_residual": float(max(abs(np.linalg.det(r)-1) for r in R)),
        "SU2_unitarity_max": float(max(norm(u.conj().T@u-I2) for u in U)),
        "SU2_determinant_max_residual": float(max(abs(np.linalg.det(u)-1) for u in U))
      },
      "scope": [
        "SO3 and SU2 comparisons use the stored archive matrices, not reconstructed links.",
        "Reverse-oriented links are compared using transpose and Hermitian adjoint.",
        "SU2 comparison is projective modulo the central sign ±I.",
        "A varying edgewise sign is not by itself a failure: it can reflect lift choices.",
        "Plaquette-level comparison requires oriented square boundary paths and is not inferred from edge data alone."
      ]
    }
    if X is not None:
        X = np.asarray(X, float)
        if X.shape != (64,3):
            raise ValueError("X must have shape (64,3)")
        result["embedding"] = {
          "max_antipodal_residual": float(np.max(np.linalg.norm(X[P]+X, axis=1))),
          "antipodal_map_matches_archive": bool(np.max(np.linalg.norm(X[P]+X, axis=1)) < 1e-10)
        }
    if squares is not None:
        # Accepted format: (n,4) ordered vertex cycles. Build oriented link lookup.
        sq = np.asarray(squares, dtype=int)
        if sq.ndim != 2 or sq.shape[1] != 4:
            raise ValueError("squares must have shape (n,4), ordered vertex cycles")
        def link(g,h):
            if (g,h) in lookup: return R[lookup[(g,h)]], U[lookup[(g,h)]]
            if (h,g) in lookup:
                k=lookup[(h,g)]; return R[k].T, U[k].conj().T
            raise ValueError(f"missing oriented boundary edge {(g,h)}")
        def product(cycle, arr_index):
            mats=[]
            for a,b in zip(cycle, np.roll(cycle,-1)):
                rr,uu=link(int(a),int(b)); mats.append(rr if arr_index==0 else uu)
            out=mats[0]
            for m in mats[1:]: out=out@m
            return out
        re=[]; ue=[]
        for cyc in sq:
            image=cyc ^ 7
            Hr, Hu=product(cyc,0), product(cyc,1)
            Hpr, Hpu=product(image,0), product(image,1)
            re.append(norm(Hpr-Hr))
            ue.append(min(norm(Hpu-Hu),norm(Hpu+Hu)))
        result["plaquettes"] = {
          "count": len(sq),
          "SO3_holonomy_max_residual": float(max(re)),
          "SU2_holonomy_projective_max_residual": float(max(ue))
        }
    else:
        result["plaquettes"] = {"status": "NOT_RUN", "reason": "supply --squares with oriented (n,4) vertex cycles"}
    result["checks"] = {
      "all_192_antipodal_links_found": len(rows) == 192,
      "SO3_equivariant": bool(so3.max() < 1e-10),
      "SU2_projectively_equivariant": bool(spin.max() < 1e-10),
      "matrix_integrity": bool(result["matrix_integrity"]["SO3_orthogonality_max"] < 1e-10 and result["matrix_integrity"]["SU2_unitarity_max"] < 1e-10)
    }
    if squares is not None:
        result["checks"]["SO3_plaquettes_equivariant"] = result["plaquettes"]["SO3_holonomy_max_residual"] < 1e-10
        result["checks"]["SU2_plaquettes_projectively_equivariant"] = result["plaquettes"]["SU2_holonomy_projective_max_residual"] < 1e-10
    result["checks_pass"] = all(result["checks"].values())
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fibre", required=True, help="NPZ containing edges, R_SO3, U_SU2")
    ap.add_argument("--embedding", help="optional NPZ containing X_Oh_reconstructed")
    ap.add_argument("--squares", help="optional NPZ containing ordered square vertex cycles under key squares")
    ap.add_argument("--out", default="T143_original_connection_antipodal_replay.json")
    a = ap.parse_args()
    with np.load(a.fibre) as z:
        edges, R, U = z["edges"], z["R_SO3"], z["U_SU2"]
    X = None
    if a.embedding:
        with np.load(a.embedding) as z: X = z["X_Oh_reconstructed"]
    squares = None
    if a.squares:
        with np.load(a.squares) as z: squares = z["squares"]
    report = audit(edges, R, U, X, squares)
    Path(a.out).write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["checks_pass"] else 1)


if __name__ == "__main__":
    main()
