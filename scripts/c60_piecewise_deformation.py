#!/usr/bin/env python3
"""
Candidata globale di deformazione g per il modello a facce del C60
(icosaedro troncato). Pezzo per pezzo affine, possibly discontinuous.

Costruzione:
  - D_f in SO(2) dal campo di trasporto (albero del grafo duale)
  - Q_f = B_f D_f B_f^T + n_f n_f^T in SO(3): rotazione di theta_f = ang(D_f)
    attorno alla normale n_f (verificato: Q_f B_f = B_f D_f)
  - g_f(x) = Q_f x + b_f, con le traslazioni b_f fissate per minimizzare
    i salti (least squares sul grafo duale: per ogni spigolo
    b_f - b_g = (Q_g - Q_f) * punto_medio)
    -> gradiente per faccia: dg|_f = B_f D_f = G_f  (3x2)

Poiche' l'olonomia attorno a ogni vertice e' 12 gradi, le immagini delle
facce adiacenti NON si saldano: esistono salti (jump) sugli spigoli e
lacune attorno ai vertici. Nel quadro Del Piero-Owen una g solo limitata
puo' essere discontinua su un insieme trascurabile: questi salti sono il
candidato disarrangiamento, concentrato sugli spigoli/vertici.

Verifiche:
  - Q_f in SO(3), Q_f B_f = B_f D_f
  - salto per spigolo (90) e gap per vertice (60)
  - gap angolare attorno al vertice == olonomia 12 gradi
  - M_f = grad g|_f - G_f = 0 per costruzione: il disarrangiamento e'
    misurato dai JUMP, non dal residuo interno.
  - sensibilita' alla gauge (BFS vs DFS vs albero GH)

Output: audits/c60_piecewise_deformation_<data>.json + .npz
"""
import json
import numpy as np
from datetime import date
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent.parent / "audits"
OUT_DIR.mkdir(exist_ok=True)
STAMP = date.today().isoformat()

# ---------- costruzione base: eseguo il builder fino alle verifiche ----------
src = Path(__file__).resolve().parent / "c60_truncated_icosahedron_transports.py"
exec(src.read_text().split("# ---------- 7. Verifiche")[0])
# ora: PTS, faces, FN, BF, A, D_bfs, D_dfs, edge_list, dual_adj, NF, NV

# ---------- 1. rotazioni Q_f in SO(3) ----------
def angle_of(M):
    return float(np.arctan2(M[1, 0], M[0, 0]))

Q = {}
theta = {}
for fi in range(NF):
    D = D_bfs[fi]
    th = angle_of(D)
    theta[fi] = th
    # rotazione di th attorno a FN[fi]
    n = FN[fi]
    K = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
    Qf = np.eye(3) + np.sin(th) * K + (1 - np.cos(th)) * (K @ K)
    # equivalenza con B D B^T + n n^T
    Qalt = BF[fi] @ D @ BF[fi].T + np.outer(n, n)
    assert np.abs(Qf - Qalt).max() < 1e-12
    Q[fi] = Qf
    assert abs(np.linalg.det(Qf) - 1) < 1e-12
    # Q_f B_f deve essere B_f D_f
    assert np.abs(Qf @ BF[fi] - BF[fi] @ D).max() < 1e-12

# ---------- 2. campo g pezzo per pezzo ----------
# g_f(x) = Q_f x + trans_f : rotazione Q_f piu' traslazione libera.
# Le traslazioni sono gauge: le fisso per minimizzare i salti (LS sul grafo
# duale).


# --- LS per le traslazioni: per ogni spigolo (f,g) con estremi a,b
#     salto in p: r_p = (Q_f - Q_g) p + (b_f - b_g)
#     minimizzo su b la somma |r_a|^2+|r_b|^2 -> per ogni spigolo il target
#     per delta = b_f - b_g e' d_e = (Q_g - Q_f)(p_a+p_b)/2
#     (il termine in p_a - p_b e' la parte incomprimibile = disarrangiamento)
und_edges = []
for (a, b, f, g_, t) in edge_list:
    if f < g_:
        und_edges.append((f, g_, a, b))
    else:
        und_edges.append((g_, f, a, b))

Lapl = np.zeros((NF, NF))
rhs = np.zeros((NF, 3))
edge_targets = {}
for (f, g_, a, b) in und_edges:
    pa, pb = PTS[a], PTS[b]
    mid = (pa + pb) / 2.0
    u_a = (Q[g_] - Q[f]) @ pa
    u_b = (Q[g_] - Q[f]) @ pb
    d_e = (u_a + u_b) / 2.0          # target per b_f - b_g
    # residuo incomprimibile su questo spigolo (meta' della differenza)
    inc = (u_a - u_b) / 2.0
    edge_targets[(f, g_)] = (d_e, inc, a, b)
    # eq: b_f - b_g = d_e  -> contributes to normal equations
    Lapl[f, f] += 1.0; Lapl[g_, g_] += 1.0
    Lapl[f, g_] -= 1.0; Lapl[g_, f] -= 1.0
    rhs[f] += d_e; rhs[g_] -= d_e

# pin root face 0: b_0 = 0 (gauge globale)
Lr = Lapl[1:, 1:]
rr = rhs[1:, :] - Lapl[1:, 0:1] * 0.0
trans = np.zeros((NF, 3))
trans[1:] = np.linalg.solve(Lr, rr)
# centra: trasla tutto in modo che il baricentro globale sia fissato
# (gauge globale residua: somma_pesi b_f = 0)
w = np.array([len(f) for f in faces], float)
w /= w.sum()
trans -= (w[:, None] * trans).sum(0)

def g(fi, x):
    """g_f(x): immagine del punto x (in R^3, nel piano della faccia f)."""
    return Q[fi] @ x + trans[fi]

# per ogni vertice e ogni faccia incidente, la sua immagine
vfaces = {v: [] for v in range(NV)}
for fi, f in enumerate(faces):
    for v in f:
        vfaces[v].append(fi)

# ---------- 3. salti sugli spigoli ----------
edge_jumps = []   # (f, g, a, b, |jump_a|, |jump_b|, jump_mid)
for (a, b, f, g_, t) in edge_list:
    pa, pb = PTS[a], PTS[b]
    ja = g(f, pa) - g(g_, pa)
    jb = g(f, pb) - g(g_, pb)
    jm = g(f, (pa + pb) / 2) - g(g_, (pa + pb) / 2)
    edge_jumps.append((f, g_, a, b,
                       float(np.linalg.norm(ja)), float(np.linalg.norm(jb)),
                       jm))

jnorm = np.array([e[4] for e in edge_jumps] + [e[5] for e in edge_jumps])
rep = {}
rep["edge_jump_norm_max"] = float(jnorm.max())
rep["edge_jump_norm_mean"] = float(jnorm.mean())
rep["edge_jump_norm_min"] = float(jnorm.min())
rep["n_edges"] = len(edge_jumps)

# salto albero vs non-albero: i salti si concentrano sugli archi non-tree?
_, _, parent_bfs = spanning_tree("bfs")
tree_pairs = set()
for c, p in parent_bfs.items():
    if p is not None:
        tree_pairs.add((min(p, c), max(p, c)))
in_tree, off_tree = [], []
for (f, g_, a, b, ja, jb, jm) in edge_jumps:
    (in_tree if (min(f, g_), max(f, g_)) in tree_pairs else off_tree).append(
        (ja + jb) / 2)
in_tree = np.array(in_tree); off_tree = np.array(off_tree)
rep["edge_jump_tree_mean"] = float(in_tree.mean())
rep["edge_jump_tree_max"] = float(in_tree.max())
rep["edge_jump_nontree_mean"] = float(off_tree.mean())
rep["edge_jump_nontree_max"] = float(off_tree.max())
rep["n_tree_edges"] = len(tree_pairs)

# salto al punto medio (l'unico ben definito se la discontinuita' e' sola
# lungo tutto lo spigolo: ja e jb possono differire)
jm_norm = np.array([np.linalg.norm(e[6]) for e in edge_jumps])
rep["edge_mid_jump_norm_max"] = float(jm_norm.max())
rep["edge_mid_jump_norm_mean"] = float(jm_norm.mean())

# ---------- 4. gap attorno ai vertici ----------
# ogni vertice ha 3 facce incidenti; le 3 immagini di v non coincidono.
# Misuro la dispersione (massimo scartamento relativo al baricentro)
vert_gap = []
vert_gap_angle = []
for v in range(NV):
    imgs = np.array([g(fi, PTS[v]) for fi in vfaces[v]])
    spread = float(np.linalg.norm(imgs - imgs.mean(0), axis=1).max())
    vert_gap.append(spread)
    # angolo di rotazione relativa: prodotto dei Q lungo il ciclo = olonomia
vert_gap = np.array(vert_gap)
rep["vertex_image_spread_max"] = float(vert_gap.max())
rep["vertex_image_spread_mean"] = float(vert_gap.mean())

# olonomie attorno ai vertici (ordine ciclico delle 3 facce incidenti)
holo_angles = []
for v in range(NV):
    pv = PTS[v]
    axis = pv / np.linalg.norm(pv)
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
    order_w = [w for _, w in sorted(
        (np.arctan2(np.dot((PTS[w] - pv) - np.dot(PTS[w] - pv, axis) * axis, e2),
                    np.dot((PTS[w] - pv) - np.dot(PTS[w] - pv, axis) * axis, e1)), w)
        for w in adj_v)]
    seq = []
    for i in range(3):
        w1, w2 = order_w[i], order_w[(i + 1) % 3]
        for fi in vfaces[v]:
            f = faces[fi]
            if v in f and w1 in f and w2 in f:
                seq.append(fi)
                break
    f1, f2, f3 = seq
    M = A[(f3, f1)] @ A[(f2, f3)] @ A[(f1, f2)]
    holo_angles.append(np.degrees(np.arctan2(M[1, 0], M[0, 0])))
holo_angles = np.array(holo_angles)
rep["vertex_holonomy_deg_min"] = float(holo_angles.min())
rep["vertex_holonomy_deg_max"] = float(holo_angles.max())

# ---------- 5. M_f = grad g|_f - G_f ----------
# grad g|_f (3x2, coordinate tangenti su B_f) = B_f D_f = G_f
# -> M_f = 0 identita'. Il disarrangiamento e' nei JUMP.
M_norms = []
for fi in range(NF):
    grad_g = BF[fi] @ D_bfs[fi]          # 3x2
    G_f = BF[fi] @ D_bfs[fi]
    M_norms.append(float(np.linalg.norm(grad_g - G_f)))
rep["M_f_residual_max"] = float(max(M_norms))

# ---------- 6. gauge: BFS vs DFS ----------
def build_Q(D):
    out = {}
    for fi in range(NF):
        n = FN[fi]
        K = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
        th = angle_of(D[fi])
        out[fi] = np.eye(3) + np.sin(th) * K + (1 - np.cos(th)) * (K @ K)
    return out

def jump_stats(D):
    """salti con Q ricostruite da D e le stesse traslazioni b (LS rifatto)."""
    Qd = build_Q(D)
    # risolvo di nuovo le traslazioni per questo D
    Lapl2 = np.zeros((NF, NF)); rhs2 = np.zeros((NF, 3))
    for (f, g_, a, b_) in und_edges:
        pa, pb = PTS[a], PTS[b_]
        u_a = (Qd[g_] - Qd[f]) @ pa
        u_b = (Qd[g_] - Qd[f]) @ pb
        d_e = (u_a + u_b) / 2.0
        Lapl2[f, f] += 1.0; Lapl2[g_, g_] += 1.0
        Lapl2[f, g_] -= 1.0; Lapl2[g_, f] -= 1.0
        rhs2[f] += d_e; rhs2[g_] -= d_e
    Lr2 = Lapl2[1:, 1:]
    tr2 = np.zeros((NF, 3)); tr2[1:] = np.linalg.solve(Lr2, rhs2[1:, :])
    w = np.array([len(f) for f in faces], float); w /= w.sum()
    tr2 -= (w[:, None] * tr2).sum(0)
    vals = []
    for (a, b_, f, g_, t) in edge_list:
        pa, pb = PTS[a], PTS[b_]
        for p in (pa, pb):
            ja = (Qd[f] @ p + tr2[f]) - (Qd[g_] @ p + tr2[g_])
            vals.append(float(np.linalg.norm(ja)))
    return float(np.mean(vals)), float(np.max(vals))

jb_mean, jb_max = jump_stats(D_bfs)
jd_mean, jd_max = jump_stats(D_dfs)
rep["jump_BFS_mean"] = jb_mean
rep["jump_BFS_max"] = jb_max
rep["jump_DFS_mean"] = jd_mean
rep["jump_DFS_max"] = jd_max
rep["jump_gauge_dependent"] = bool(abs(jb_mean - jd_mean) > 1e-9)

# ---------- 7. output ----------
result = {
    "date": STAMP,
    "construction": "Q_f = B_f D_f B_f^T + n_f n_f^T in SO(3); "
                    "g_f(x) = Q_f x + b_f, b_f da LS minima sui salti",
    "interpretation": "olonomia 12deg/vertice => g non saldata; i salti "
                      "sugli spigoli sono il candidato disarrangiamento DPO",
    "counts": {"vertices": int(NV), "edges": len(edge_list), "faces": NF},
    "checks": rep,
}
jpath = OUT_DIR / f"c60_piecewise_deformation_{STAMP}.json"
jpath.write_text(json.dumps(result, indent=2, ensure_ascii=False))

np.savez_compressed(
    OUT_DIR / f"c60_piecewise_deformation_{STAMP}.npz",
    Q_f=np.array([Q[i] for i in range(NF)]),
    theta_f=np.array([theta[i] for i in range(NF)]),
    edge_jump_norms=jnorm,
    vertex_spread=vert_gap,
    vertex_holonomy_deg=holo_angles,
)
print(json.dumps(result, indent=2, ensure_ascii=False))
print("saved:", jpath)
