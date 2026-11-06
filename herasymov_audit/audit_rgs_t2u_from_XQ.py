#!/usr/bin/env python3
"""Reconstruct the O_h action on the 188D RGS tangent space and audit T2u.

Input: an NPZ containing X (64,3) and Q (192,188), or compatible aliases.
No group matrices are fabricated: O_h acts on the 64 vertex coordinates by
signed coordinate permutations, and the induced action is assembled explicitly.

Outputs: JSON report and NPZ containing U_tan, D_t2u, group, P_T2u and J.
Requires numpy only.
"""
from __future__ import annotations
import argparse, itertools, json
from pathlib import Path
import numpy as np

PERMS = list(itertools.permutations(range(3)))
SIGNS = list(itertools.product((-1.0, 1.0), repeat=3))


def signed_permutation_group():
    mats = []
    for p in PERMS:
        for s in SIGNS:
            g = np.zeros((3, 3), float)
            for i in range(3):
                g[i, p[i]] = s[i]
            mats.append(g)
    return mats


def get_array(z, names, shape):
    for name in names:
        if name in z and z[name].shape == shape:
            return np.asarray(z[name], float), name
    raise KeyError(f"NPZ needs one of {names} with shape {shape}; keys={list(z.keys())}")


def harmonic_t2u(x):
    a, b, c = np.moveaxis(np.asarray(x, float), -1, 0)
    return np.stack((a*(b*b-c*c), b*(c*c-a*a), c*(a*a-b*b)), axis=-1)


def representation_t2u(g, sample):
    # Least-squares realization of h(gx)=D(g)h(x).
    lhs = harmonic_t2u(sample @ g.T)
    rhs = harmonic_t2u(sample)
    d_t = np.linalg.lstsq(rhs, lhs, rcond=None)[0]
    d = d_t.T
    err = np.linalg.norm(lhs - rhs @ d.T) / max(np.linalg.norm(lhs), 1.0)
    return d, float(err)


def build_actions(X, Q, tol=1e-9):
    n = X.shape[0]
    actions, ds, groups = [], [], []
    # Deterministic generic sample for exact polynomial representation fitting.
    sample = np.array([[.31,.73,1.17], [-.82,.29,.51], [1.13,-.47,.67],
                       [.41,-1.21,.88], [-.63,-.91,1.39], [1.7,.23,-.38]])
    for g in signed_permutation_group():
        transformed = X @ g.T
        dist = np.linalg.norm(transformed[:, None, :] - X[None, :, :], axis=2)
        perm = np.argmin(dist, axis=1)
        err = np.max(dist[np.arange(n), perm])
        if err > tol or len(np.unique(perm)) != n:
            raise ValueError(f"vertex set not O_h invariant: max matching error={err:.3e}")
        # Ambient action: v_{perm(i)} = g v_i, flattened vertex-major.
        U = np.zeros((3*n, 3*n), float)
        for i, j in enumerate(perm):
            U[3*j:3*j+3, 3*i:3*i+3] = g
        Ut = Q.T @ U @ Q
        closure_leak = np.linalg.norm(U @ Q - Q @ Ut) / max(np.linalg.norm(Q), 1.0)
        if closure_leak > 1e-8:
            raise ValueError(f"tangent space not invariant: leakage={closure_leak:.3e}")
        D, derr = representation_t2u(g, sample)
        actions.append(Ut); ds.append(D); groups.append(g)
    return np.asarray(actions), np.asarray(ds), np.asarray(groups)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path, help="NPZ containing X and Q")
    ap.add_argument("--output", type=Path, default=Path("rgs_t2u_reconstruction"))
    ap.add_argument("--seed", type=int, default=20261106)
    ap.add_argument("--tol", type=float, default=1e-9)
    args = ap.parse_args()

    z = np.load(args.input, allow_pickle=False)
    X, xkey = get_array(z, ("X", "X_Oh", "X_reconstructed"), (64,3))
    Q, qkey = get_array(z, ("Q", "Q_archived", "Q_tangent_svd", "Q_tangent"), (192,188))
    qorth = float(np.linalg.norm(Q.T @ Q - np.eye(188)))
    if qorth > 1e-7:
        raise ValueError(f"Q is not orthonormal: residual={qorth:.3e}")

    U, D, G = build_actions(X, Q, args.tol)
    # Character projector for the complete T2u isotypic component.
    chi = np.trace(D, axis1=1, axis2=2)
    P = (3.0/48.0) * np.einsum("g,gij->ij", chi, U)
    P = 0.5*(P + P.T)
    idem = float(np.linalg.norm(P@P-P))
    prank = int(np.linalg.matrix_rank(P, tol=1e-7))
    # Source representation is ten copies of the 3D T2u carrier.
    S = np.asarray([np.kron(np.eye(10), d) for d in D])
    rng = np.random.default_rng(args.seed)
    J0 = rng.standard_normal((188,30))
    J = sum(U[k] @ J0 @ S[k].T for k in range(48))/48.0
    sing = np.linalg.svd(J, compute_uv=False)
    jrank = int(np.linalg.matrix_rank(J, tol=1e-8))
    inter = max(float(np.linalg.norm(U[k]@J-J@S[k])) for k in range(48))
    p_j = float(np.linalg.norm(P@J-J))
    rep_u = max(float(np.linalg.norm(U[a]@U[b]-U[c]))
                for a in range(48) for b in range(48)
                for c in [int(np.argmin([np.linalg.norm(G[t]-G[a]@G[b]) for t in range(48)]))])
    rep_d = max(float(np.linalg.norm(D[a]@D[b]-D[c]))
                for a in range(48) for b in range(48)
                for c in [int(np.argmin([np.linalg.norm(G[t]-G[a]@G[b]) for t in range(48)]))])
    report = {
        "status": "computed_from_original_X_and_Q",
        "input": str(args.input), "X_key": xkey, "Q_key": qkey,
        "group_order": 48, "ambient_dimension": 192, "tangent_dimension": 188,
        "Q_orthogonality_residual": qorth,
        "U_tan_shape": list(U.shape), "D_t2u_shape": list(D.shape),
        "max_U_tangent_invariance_residual": float(max(
            np.linalg.norm((np.eye(192)-Q@Q.T)@np.kron(np.eye(64),np.eye(3))@Q)
            for _ in [])) if False else None,
        "max_U_representation_residual": rep_u,
        "max_D_representation_residual": rep_d,
        "P_T2u_idempotence_residual": idem,
        "P_T2u_rank": prank,
        "expected_full_isotypic_rank_if_multiplicity_10": 30,
        "J_shape": list(J.shape), "J_rank": jrank,
        "J_singular_values": sing.tolist(),
        "max_intertwining_residual": inter,
        "P_T2u_J_residual": p_j,
        "interpretation": "J is one deterministic Reynolds-projected intertwiner; its rank is data-dependent."
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(str(args.output)+".npz", U_tan=U, D_t2u=D, group=G,
                        P_T2u=P, J=J, singular_values=sing)
    Path(str(args.output)+".json").write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
