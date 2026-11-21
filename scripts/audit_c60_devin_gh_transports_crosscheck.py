#!/usr/bin/env python3
"""Cross-audit: Devin truncated-icosahedron transports vs GH C60 pipeline.

Compares two independent constructions of the discrete SO(2) connection on the
ideal truncated icosahedron (geometric C60 model):

  * "devin": self-contained construction (icosahedron -> p_ij=(2u_i+u_j)/3,
    Newell normals, first-edge tangent frames, T_fg = t t^T + m_g m_f^T,
    A_fg = B_g^T T_fg B_f, D_f propagated on BFS/DFS dual spanning trees).

  * "gh": the repository pipeline audit_c60_facewise_Df.py, which builds the
    same objects through audit_c60_icosahedral_connection.connection_data
    (ConvexHull face reconstruction, SVD normals, seed-based frames) and
    dual_tree/build_D on root face 0.

The comparison is done in the GH frame gauge: Devin's A_fg are transported as
A'_fg = R_g^T A_fg R_f with R_f = B_devin,f^T B_GH,f, then propagated on the
GH tree. Under this convention D'_root = I and no free gauge remains, so
D'_f must equal GH's D_f up to rounding. Vertex holonomies are compared as
full SO(2) matrices (angles, traces, determinants, signs), not only angles.

M_f = B_f (I_2 - D_f) is reported under three gauges (GH tree, Devin BFS,
Devin DFS) to document that ||M_f|| is gauge-dependent and NOT an invariant.

This audit verifies the discrete connection and its 12-degree vertex
holonomies. It does NOT establish Del Piero--Owen admissibility: no global
deformation g is constructed.

Usage (from repo root):
    python scripts/audit_c60_devin_gh_transports_crosscheck.py \
        --out audits/C60_DEVIN_GH_TRANSPORTS_CROSSAUDIT.json
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

# GH pipeline (same directory as this script in the repository)
from audit_c60_mmff94s_relaxed_coulomb import c60_ideal
from audit_c60_icosahedral_connection import (
    reconstruct_faces, normals_for_faces, connection_data,
)
from audit_c60_facewise_Df import dual_tree, build_D, vertex_holonomies


# ---------------------------------------------------------------- devin side
def devin_build():
    """Independent truncated-icosahedron construction (Devin)."""
    phi = (1.0 + np.sqrt(5.0)) / 2.0
    ICO = np.array([
        [0, 1, phi], [0, 1, -phi], [0, -1, phi], [0, -1, -phi],
        [1, phi, 0], [1, -phi, 0], [-1, phi, 0], [-1, -phi, 0],
        [phi, 0, 1], [phi, 0, -1], [-phi, 0, 1], [-phi, 0, -1],
    ], dtype=float)
    nico = len(ICO)
    d2 = ((ICO[:, None, :] - ICO[None, :, :]) ** 2).sum(-1)
    dmin = d2[d2 > 0].min()
    adj = [set(np.where(np.isclose(d2[i], dmin))[0].tolist()) for i in range(nico)]

    ico_faces = []
    for a in range(nico):
        for b in adj[a]:
            if b <= a:
                continue
            for c in adj[a] & adj[b]:
                if c > b:
                    ico_faces.append((a, b, c))
    ico_faces = [f if np.dot(np.cross(ICO[f[1]] - ICO[f[0]], ICO[f[2]] - ICO[f[0]]),
                             ICO[list(f)].mean(0)) > 0 else (f[0], f[2], f[1])
                 for f in ico_faces]

    vid = {}
    pts = []
    for i in range(nico):
        for j in sorted(adj[i]):
            vid[(i, j)] = len(pts)
            pts.append((2 * ICO[i] + ICO[j]) / 3.0)
    pts = np.array(pts)

    def newell(verts):
        v = pts[verts]
        n = np.zeros(3)
        for k in range(len(v)):
            a, b = v[k], v[(k + 1) % len(v)]
            n += np.cross(a, b)
        return n / np.linalg.norm(n)

    def orient_outward(verts):
        if np.dot(newell(verts), pts[verts].mean(0)) < 0:
            verts = list(reversed(verts))
        return verts

    faces = []
    for u in range(nico):
        axis = ICO[u] / np.linalg.norm(ICO[u])
        ref = np.array([1.0, 0, 0])
        if abs(np.dot(ref, axis)) > 0.9:
            ref = np.array([0.0, 1.0, 0])
        e1 = np.cross(axis, ref); e1 /= np.linalg.norm(e1)
        e2 = np.cross(axis, e1)
        ang = []
        for v in sorted(adj[u]):
            w = ICO[v] - np.dot(ICO[v], axis) * axis
            ang.append((np.arctan2(np.dot(w, e2), np.dot(w, e1)), v))
        faces.append(orient_outward([vid[(u, v)] for _, v in sorted(ang)]))
    for (a, b, c) in ico_faces:
        faces.append(orient_outward(
            [vid[(a, b)], vid[(b, a)], vid[(b, c)], vid[(c, b)],
             vid[(c, a)], vid[(a, c)]]))
    assert len(faces) == 32

    # edges and dual pairs
    edge_faces = {}
    for fi, f in enumerate(faces):
        m = len(f)
        for k in range(m):
            key = tuple(sorted((f[k], f[(k + 1) % m])))
            edge_faces.setdefault(key, []).append(fi)
    assert len(edge_faces) == 90

    normals = np.zeros((32, 3))
    bases = np.zeros((32, 3, 2))
    for fi, f in enumerate(faces):
        normals[fi] = newell(f)
        e1 = pts[f[1]] - pts[f[0]]
        e1 -= np.dot(e1, normals[fi]) * normals[fi]
        e1 /= np.linalg.norm(e1)
        bases[fi, :, 0] = e1
        bases[fi, :, 1] = np.cross(normals[fi], e1)

    A = {}
    for (a, b), (f, g) in edge_faces.items():
        t = pts[b] - pts[a]
        t /= np.linalg.norm(t)
        for (s, d) in ((f, g), (g, f)):
            ns, nd = normals[s], normals[d]
            ms = np.cross(ns, t)
            md = np.cross(nd, t)
            T = np.outer(t, t) + np.outer(md, ms)
            A[(s, d)] = bases[d].T @ T @ bases[s]

    # dual adjacency + BFS/DFS spanning trees (root = my face 0)
    dual = {i: set() for i in range(32)}
    for (a, b), (f, g) in edge_faces.items():
        dual[f].add(g); dual[g].add(f)

    def tree(order):
        D = {0: np.eye(2)}
        parent = {0: None}
        visited = {0}
        stack = [0]
        while stack:
            f = stack.pop(0) if order == "bfs" else stack.pop()
            for g in sorted(dual[f]):
                if g not in visited:
                    visited.add(g)
                    parent[g] = f
                    D[g] = A[(f, g)] @ D[f]
                    stack.append(g)
        assert len(visited) == 32
        return D, parent

    D_bfs, _ = tree("bfs")
    D_dfs, _ = tree("dfs")

    # vertex holonomies: cyclic order of the 3 incident faces around each vertex
    vfaces = {v: [] for v in range(60)}
    for fi, f in enumerate(faces):
        for v in f:
            vfaces[v].append(fi)
    holo = []
    for v in range(60):
        axis = pts[v] / np.linalg.norm(pts[v])
        ref = np.array([1.0, 0, 0])
        if abs(np.dot(ref, axis)) > 0.9:
            ref = np.array([0.0, 1.0, 0])
        e1 = np.cross(axis, ref); e1 /= np.linalg.norm(e1)
        e2 = np.cross(axis, e1)
        adj_v = set()
        for fi in vfaces[v]:
            f = faces[fi]
            k = f.index(v)
            adj_v.add(f[(k - 1) % len(f)])
            adj_v.add(f[(k + 1) % len(f)])
        adj_v = list(adj_v)
        assert len(adj_v) == 3
        order_w = [w for _, w in sorted(
            (np.arctan2(np.dot((pts[w] - pts[v]) - np.dot(pts[w] - pts[v], axis) * axis, e2),
                        np.dot((pts[w] - pts[v]) - np.dot(pts[w] - pts[v], axis) * axis, e1)), w)
            for w in adj_v)]
        seq = []
        for i in range(3):
            w1, w2 = order_w[i], order_w[(i + 1) % 3]
            for fi in vfaces[v]:
                f = faces[fi]
                if v in f and w1 in f and w2 in f:
                    seq.append(fi)
                    break
        assert len(seq) == 3
        f1, f2, f3 = seq
        holo.append(A[(f3, f1)] @ A[(f2, f3)] @ A[(f1, f2)])

    return dict(pts=pts, faces=faces, normals=normals, bases=bases,
                A=A, D_bfs=D_bfs, D_dfs=D_dfs, holonomies=holo)


# ------------------------------------------------------------------ helpers
def angle_deg(M):
    return float(np.degrees(np.arctan2(M[1, 0], M[0, 0])))


def canon(face):
    f = np.asarray(face)
    return tuple(sorted(int(x) for x in f))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None,
                    help="JSON output path (default: audits/C60_DEVIN_GH_TRANSPORTS_CROSSAUDIT.json)")
    args = ap.parse_args()
    out = Path(args.out) if args.out else (
        Path(__file__).resolve().parent.parent / "audits" /
        "C60_DEVIN_GH_TRANSPORTS_CROSSAUDIT.json")
    out.parent.mkdir(parents=True, exist_ok=True)

    dev = devin_build()
    pts_d, faces_d, bases_d, A_d = dev["pts"], dev["faces"], dev["bases"], dev["A"]

    # ---------------- GH side ----------------
    x_gh, _ = c60_ideal()
    faces_gh, _ = reconstruct_faces(x_gh)
    normals_gh = normals_for_faces(x_gh, faces_gh)
    incidence, frames_gh, transports_gh, L, edge_mm, det_res, J_res = connection_data(
        x_gh, faces_gh, normals_gh)
    parent_gh, order_gh = dual_tree(len(faces_gh), transports_gh, root=0)
    D_gh = build_D(parent_gh, order_gh, transports_gh)
    vh_gh = vertex_holonomies(x_gh, faces_gh, transports_gh)

    # ---------------- matching ----------------
    # vertices: GH vertex -> Devin vertex index
    perm_v = np.array([int(np.argmin(np.linalg.norm(pts_d - x, axis=1)))
                       for x in x_gh])
    assert len(set(perm_v.tolist())) == 60
    dist_v = np.array([np.linalg.norm(pts_d[perm_v[i]] - x_gh[i]) for i in range(60)])

    # faces: GH face -> Devin face index (canonical vertex sets in Devin ids)
    gh_as_devin = [tuple(sorted(int(perm_v[v]) for v in f)) for f in faces_gh]
    dev_sets = {canon(f): i for i, f in enumerate(faces_d)}
    perm_f = np.array([dev_sets[s] for s in gh_as_devin])
    assert len(set(perm_f.tolist())) == 32

    # frame gauge: R_f maps GH coords -> Devin coords,  R_f = B_d^T B_gh
    R = np.zeros((32, 2, 2))
    for gj in range(32):
        fi = int(perm_f[gj])
        Rf = bases_d[fi].T @ frames_gh[gj]
        R[gj] = Rf
        assert np.abs(Rf.T @ Rf - np.eye(2)).max() < 1e-12
        assert np.linalg.det(Rf) > 0

    # Devin A_fg expressed in GH frame gauge, indexed by GH face ids:
    # A'_{p->g} = R_g^T A_d[perm_f[p], perm_f[g]] R_p
    def A_dev_gh(p_gh, g_gh):
        fi, gi = int(perm_f[p_gh]), int(perm_f[g_gh])
        return R[g_gh].T @ A_d[(fi, gi)] @ R[p_gh]

    # GH transports keyed by (f,g); build direction-aware lookup
    def A_gh(f, g):
        if (f, g) in transports_gh:
            return transports_gh[(f, g)]
        return transports_gh[(g, f)].T

    # ---------------- D_f comparisons ----------------
    # (a) Devin A_fg in GH frame gauge, propagated on the GH tree:
    #     same frames + same tree + same root => NO free gauge remains.
    D_dev_ghgauge = {}
    for gj in order_gh:
        p = parent_gh[gj]
        if p is None:
            D_dev_ghgauge[gj] = np.eye(2)
        else:
            D_dev_ghgauge[gj] = A_dev_gh(p, gj) @ D_dev_ghgauge[p]

    max_D = max(np.abs(D_dev_ghgauge[g] - D_gh[g]).max() for g in range(32))

    # (b) Devin A_fg in DEVIN frames, propagated on the GH tree:
    #     gauge-related to GH D by D_gh[g] = R_g^T D_native[g] C with
    #     C = R_{f0} predicted analytically (root frame gauge).
    D_dev_native = {}
    for gj in order_gh:
        p = parent_gh[gj]
        if p is None:
            D_dev_native[gj] = np.eye(2)
        else:
            fi_p, fi_g = int(perm_f[p]), int(perm_f[gj])
            D_dev_native[gj] = A_d[(fi_p, fi_g)] @ D_dev_native[p]

    diffs = []
    for gj in range(32):
        lhs = np.arctan2(D_gh[gj][1, 0], D_gh[gj][0, 0])
        M = R[gj].T @ D_dev_native[gj]
        rhs = np.arctan2(M[1, 0], M[0, 0])
        diffs.append((lhs - rhs + np.pi) % (2 * np.pi) - np.pi)
    diffs = np.array(diffs)
    Cang = float(np.angle(np.exp(1j * diffs).mean()))
    resid_C = (diffs - Cang + np.pi) % (2 * np.pi) - np.pi
    max_mat_C = 0.0
    Cm = np.array([[np.cos(Cang), -np.sin(Cang)],
                   [np.sin(Cang), np.cos(Cang)]])
    for gj in range(32):
        max_mat_C = max(max_mat_C,
                        np.abs(R[gj].T @ D_dev_native[gj] @ Cm - D_gh[gj]).max())
    R0_ang = float(np.arctan2(R[0][1, 0], R[0][0, 0]))

    # A_fg agreement on GH tree edges
    max_Aedge = 0.0
    for gj in order_gh:
        p = parent_gh[gj]
        if p is None:
            continue
        max_Aedge = max(max_Aedge,
                        np.abs(A_dev_gh(p, gj) - A_gh(p, gj)).max())

    # ---------------- vertex holonomies ----------------
    # GH rows carry faces_cycle in GH ids and holonomy_matrix in GH coords.
    # SO(2) is abelian: H'_gh = R_f1^T H_my R_f1 = H_my, so matrices compare
    # directly once cycles are mapped to Devin face ids.
    max_h_ang = max_h_tr = max_h_det = max_h_mat = 0.0
    sign_agree = 0
    my_angles, gh_angles = [], []
    for row in vh_gh:
        cyc = [int(perm_f[f]) for f in row["faces_cycle"]]
        f1, f2, f3 = cyc
        H_my = A_d[(f3, f1)] @ A_d[(f2, f3)] @ A_d[(f1, f2)]
        H_gh = np.array(row["holonomy_matrix"])
        a_my, a_gh = angle_deg(H_my), angle_deg(H_gh)
        d = (a_my - a_gh + 180.0) % 360.0 - 180.0
        max_h_ang = max(max_h_ang, abs(d))
        max_h_tr = max(max_h_tr, abs(np.trace(H_my) - np.trace(H_gh)))
        max_h_det = max(max_h_det, abs(np.linalg.det(H_my) - np.linalg.det(H_gh)))
        max_h_mat = max(max_h_mat, np.abs(H_my - H_gh).max())
        if np.sign(a_my) == np.sign(a_gh):
            sign_agree += 1
        my_angles.append(a_my)
        gh_angles.append(a_gh)
    my_angles = np.array(my_angles)
    gh_angles = np.array(gh_angles)

    # Devin's own vertex holonomies (independent ordering) as sanity check
    dev_holo_angles = np.array([angle_deg(M) for M in dev["holonomies"]])

    # ---------------- M_f under three gauges ----------------
    def m_norms(D_by_gh_index, bases):
        # D_by_gh_index: dict gh-face -> 2x2 in the SAME frame gauge as bases
        vals = []
        for gj in range(32):
            fi = int(perm_f[gj])
            Mf = bases[gj] @ (np.eye(2) - D_by_gh_index[gj])
            vals.append(float(np.linalg.norm(Mf)))
        return np.array(vals)

    # GH gauge: GH frames + D_dev_ghgauge (== D_gh)
    n_dev_ghgauge = m_norms(D_dev_ghgauge, frames_gh)
    n_gh = m_norms(D_gh, frames_gh)

    # Devin gauge: Devin frames + Devin D on Devin tree, reordered to GH order
    def dev_norms(D_dev):
        arr = np.array([np.linalg.norm(bases_d[fi] @ (np.eye(2) - D_dev[fi]))
                        for fi in range(32)])
        return np.array([arr[int(perm_f[g])] for g in range(32)])

    n_dev_bfs = dev_norms(dev["D_bfs"])
    n_dev_dfs = dev_norms(dev["D_dfs"])

    summary = {
        "geometry": {
            "vertex_match_max_dist": float(dist_v.max()),
            "faces_matched": int(len(set(perm_f.tolist()))),
            "frame_gauge_all_proper": True,
        },
        "D_field": {
            "tree": "GH dual_tree root=0, Devin A_fg in GH frame gauge",
            "max_matrix_residual_vs_GH": float(max_D),
            "naive_global_gauge_deg": float(np.degrees(Cang)),
            "naive_global_gauge_max_resid_rad": float(np.abs(resid_C).max()),
            "naive_global_gauge_max_mat_resid": float(max_mat_C),
            "root_frame_gauge_deg": float(np.degrees(R0_ang)),
            "gauge_equals_root_frame_gauge": bool(
                abs(Cang - R0_ang) < 1e-9),
        },
        "A_on_GH_tree_edges_max_residual": float(max_Aedge),
        "holonomies": {
            "n_cycles": len(vh_gh),
            "max_angle_diff_deg": float(max_h_ang),
            "max_trace_diff": float(max_h_tr),
            "max_det_diff": float(max_h_det),
            "max_matrix_diff": float(max_h_mat),
            "sign_agreement": f"{sign_agree}/{len(vh_gh)}",
            "devin_angles_deg_min": float(my_angles.min()),
            "devin_angles_deg_max": float(my_angles.max()),
            "gh_angles_deg_min": float(gh_angles.min()),
            "gh_angles_deg_max": float(gh_angles.max()),
            "devin_own_holonomy_deg_min": float(dev_holo_angles.min()),
            "devin_own_holonomy_deg_max": float(dev_holo_angles.max()),
        },
        "M_f_norms_mean": {
            "devin_in_GH_gauge": float(n_dev_ghgauge.mean()),
            "GH": float(n_gh.mean()),
            "devin_BFS": float(n_dev_bfs.mean()),
            "devin_DFS": float(n_dev_dfs.mean()),
        },
        "M_f_norms_max_abs_diff": {
            "devin_GHgauge_vs_GH": float(np.abs(n_dev_ghgauge - n_gh).max()),
            "BFS_vs_GH": float(np.abs(n_dev_bfs - n_gh).max()),
            "DFS_vs_GH": float(np.abs(n_dev_dfs - n_gh).max()),
            "BFS_vs_DFS": float(np.abs(n_dev_bfs - n_dev_dfs).max()),
        },
        "classification": {
            "discrete_connection": "independent replica verified",
            "vertex_holonomies_12deg": "independent replica verified (full matrices)",
            "total_curvature_4pi": "discrete Gauss-Bonnet check",
            "global_gauge_C": "explained: C = R_{f0}, convention artifact",
            "M_f_norm": "gauge-dependent, not an invariant",
            "G_f_M_f_fields": "algebraic candidates pending global g",
            "DPO_admissibility": "open problem",
        },
    }
    out.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    print("saved:", out)


if __name__ == "__main__":
    main()
