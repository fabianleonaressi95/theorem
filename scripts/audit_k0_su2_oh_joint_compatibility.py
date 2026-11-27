#!/usr/bin/env python3
"""Joint SU(2) x O_h compatibility audit for the K0 spectral ladder.

Reconstructs the O_h character projectors P_T1u (rank 39) and P_T2u (rank 30)
on the 188D tangent space (same construction as
models/tangent_triplet_anisotropy.py), builds the canonical spin-61.5
ladder on the 124D complement of K0, and measures:

  * [K0, R_g] for all 48 cubic operations, decomposed into
    kernel/complement blocks;
  * off-diagonal cubic-sector blocks of K0;
  * Frobenius norms of ladder generators J_z,J_+,J_-,J_x,J_y and of
    Z_S,Z_A,T_transport in the T1u/T2u/rest block decomposition.

Writes audits/K0_SU2_OH_JOINT_COMPATIBILITY_2026-11-24.json.
"""
import json
from itertools import permutations, product

import numpy as np
from scipy.linalg import null_space


def t2g_character(R):
    value = 0.0
    for i, j in ((0, 1), (1, 2), (2, 0)):
        ii = int(np.argmax(np.abs(R[:, i])))
        jj = int(np.argmax(np.abs(R[:, j])))
        if {ii, jj} == {i, j}:
            value += R[ii, i] * R[jj, j]
    return float(value)


def build_oh_tangent(X):
    C = np.zeros((4, 192))
    C[0, 0::3] = 1.0
    C[1, 1::3] = 1.0
    C[2, 2::3] = 1.0
    C[3] = X.reshape(-1)
    Q = null_space(C)
    assert Q.shape == (192, 188)
    Rs, c1, c2 = [], [], []
    for perm_axes in permutations(range(3)):
        Pa = np.zeros((3, 3))
        for i, j in enumerate(perm_axes):
            Pa[j, i] = 1.0
        for signs in product((-1.0, 1.0), repeat=3):
            G = Pa @ np.diag(signs)
            parity = int(round(np.linalg.det(G)))
            Rp = parity * G
            c1.append(float(np.trace(G)))                    # T1u: polar vector
            c2.append(parity * t2g_character(Rp))            # T2u
            tr = X @ G.T
            dist = np.linalg.norm(tr[:, None, :] - X[None, :, :], axis=2)
            sm = np.argmin(dist, axis=1)
            assert np.max(dist[np.arange(64), sm]) < 1e-8
            D = np.zeros((192, 192))
            for s, t in enumerate(sm):
                D[3 * t:3 * t + 3, 3 * s:3 * s + 3] = G
            Rs.append(Q.T @ D @ Q)
    Rs = np.array(Rs)
    P1 = (3.0 / 48.0) * np.einsum("g,gij->ij", np.array(c1), Rs)
    P2 = (3.0 / 48.0) * np.einsum("g,gij->ij", np.array(c2), Rs)
    return (P1 + P1.T) / 2, (P2 + P2.T) / 2, Rs


def main():
    d = np.load("data/RGS_PSU_all_matrices.npz")
    K0, PG, T = d["K0"], d["P_G"], d["T_transport"]
    ZS = np.load("artifacts/Z_S.npy")
    ZA = np.load("artifacts/Z_A.npy")
    X = d["X_Oh_reconstructed"]

    P1, P2, Rs = build_oh_tangent(X)
    Pp = np.eye(188) - PG
    report = {"cubic_projectors": {}, "K0_vs_Oh": {}, "sector_mixing": {},
              "ladder_blocks": {}, "operator_blocks": {}}

    for name, P in (("T1u", P1), ("T2u", P2)):
        ev = np.linalg.eigvalsh(P)
        report["cubic_projectors"][name] = {
            "rank": int(np.sum(ev > 0.5)),
            "idempotence": float(np.linalg.norm(P @ P - P)),
        }

    comm_full = [float(np.linalg.norm(K0 @ R - R @ K0)) for R in Rs]
    comm_pp = [float(np.linalg.norm(Pp @ (K0 @ R - R @ K0) @ Pp)) for R in Rs]
    comm_gg = [float(np.linalg.norm(PG @ (K0 @ R - R @ K0) @ PG)) for R in Rs]
    report["K0_vs_Oh"] = {
        "max_commutator_full": max(comm_full),
        "max_commutator_Pperp_block": max(comm_pp),
        "mean_commutator_Pperp_block": float(np.mean(comm_pp)),
        "max_commutator_PG_block": max(comm_gg),
    }

    Pres = np.eye(188) - P1 - P2
    secs = {"1u": P1, "2u": P2, "rest": Pres}
    for sn, Pa in secs.items():
        for sm, Pb in secs.items():
            if sn != sm:
                report["sector_mixing"][f"K0_{sn}_to_{sm}"] = float(
                    np.linalg.norm(Pa @ K0 @ Pb))

    # spin-61.5 ladder on complement
    w, V = np.linalg.eigh((K0 + K0.T) / 2)
    idx = np.where(w > 1e-8)[0]
    U = V[:, idx].copy()
    for c in range(U.shape[1]):
        k = int(np.argmax(np.abs(U[:, c])))
        if U[k, c].real < 0:
            U[:, c] *= -1
    n, j = 124, 61.5
    m = -j + np.arange(n)
    Jp_b = np.zeros((n, n), complex)
    for a in range(n - 1):
        Jp_b[a + 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    ops = {
        "Jz": U @ np.diag(m).astype(complex) @ U.conj().T,
        "Jp": U @ Jp_b @ U.conj().T,
        "Jm": U @ Jp_b.conj().T @ U.conj().T,
        "Jx": U @ ((Jp_b + Jp_b.conj().T) / 2) @ U.conj().T,
        "Jy": U @ ((Jp_b - Jp_b.conj().T) / (2j)) @ U.conj().T,
    }
    for on, O in ops.items():
        report["ladder_blocks"][on] = {
            f"{sa}{sb}": float(np.linalg.norm(Pa @ O @ Pb))
            for sa, Pa in secs.items() for sb, Pb in secs.items()
        }
    for bn, B in (("Z_S", ZS), ("Z_A", ZA), ("T_transport", T)):
        report["operator_blocks"][bn] = {
            f"{sa}{sb}": float(np.linalg.norm(Pa @ B @ Pb))
            for sa, Pa in secs.items() for sb, Pb in secs.items()
        }

    # su(2) self-check
    Jz, Jp, Jm = ops["Jz"], ops["Jp"], ops["Jm"]
    report["su2_selfcheck"] = {
        "brackets": float(max(
            np.linalg.norm(Jz @ Jp - Jp @ Jz - Jp),
            np.linalg.norm(Jz @ Jm - Jm @ Jz + Jm),
            np.linalg.norm(Jp @ Jm - Jm @ Jp - 2 * Jz))),
    }

    out = "audits/K0_SU2_OH_JOINT_COMPATIBILITY_2026-11-24.json"
    with open(out, "w") as fh:
        json.dump(report, fh, indent=2)
    print(json.dumps({k: report[k] for k in
                      ("cubic_projectors", "K0_vs_Oh", "sector_mixing",
                       "su2_selfcheck")}, indent=2))
    print("wrote", out)


if __name__ == "__main__":
    main()
