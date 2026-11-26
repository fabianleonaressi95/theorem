#!/usr/bin/env python3
"""
Trasporti discreti sull'icosaedro troncato (modello geometrico C60).

Costruzione:
  - 12 vertici di icosaedro -> 60 vertici troncati p_ij = (2u_i + u_j)/3
  - 32 facce (12 pentagoni + 20 esagoni), 90 spigoli
  - per ogni coppia di facce adiacenti: A_fg = B_g^T T_fg B_f in SO(2)
  - campo D_f in SO(2) da albero ricoprente del grafo duale
  - verifica: isometria, orientazione, inversa, ricorrenza, olonomia
    (cicli attorno ai vertici -> 12 gradi), indipendenza di gauge.

Output: audits/truncated_icosahedron_transports_<data>.json + .npz
"""
import json
import numpy as np
from datetime import date
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent.parent / "audits"
OUT_DIR.mkdir(exist_ok=True)
STAMP = date.today().isoformat()

# ---------- 1. Icosaedro ----------
phi = (1.0 + np.sqrt(5.0)) / 2.0
ICO = np.array([
    [0, 1, phi], [0, 1, -phi], [0, -1, phi], [0, -1, -phi],
    [1, phi, 0], [1, -phi, 0], [-1, phi, 0], [-1, -phi, 0],
    [phi, 0, 1], [phi, 0, -1], [-phi, 0, 1], [-phi, 0, -1],
], dtype=float)
NICO = len(ICO)

d2 = ((ICO[:, None, :] - ICO[None, :, :]) ** 2).sum(-1)
DMIN = d2[d2 > 0].min()
ADJ = [set(np.where(np.isclose(d2[i], DMIN))[0].tolist()) for i in range(NICO)]
assert all(len(a) == 5 for a in ADJ)

# facce dell'icosaedro: terne mutuamente adiacenti
ico_faces = []
for a in range(NICO):
    for b in ADJ[a]:
        if b <= a:
            continue
        for c in ADJ[a] & ADJ[b]:
            if c > b:
                ico_faces.append((a, b, c))
assert len(ico_faces) == 20
# orientazione esterna: se la normale e' entrante si scambiano b e c
ico_faces = [f if np.dot(np.cross(ICO[f[1]] - ICO[f[0]], ICO[f[2]] - ICO[f[0]]),
                        ICO[list(f)].mean(0)) > 0 else (f[0], f[2], f[1])
             for f in ico_faces]
assert len(ico_faces) == 20

# ---------- 2. Vertici troncati ----------
# id vertice troncato = (i,j) con i->j spigolo orientato
VID = {}
PTS = []
for i in range(NICO):
    for j in sorted(ADJ[i]):
        VID[(i, j)] = len(PTS)
        PTS.append((2 * ICO[i] + ICO[j]) / 3.0)
PTS = np.array(PTS)
NV = len(PTS)
assert NV == 60
RADIUS = np.linalg.norm(PTS, axis=1)
assert np.allclose(RADIUS, RADIUS[0])

# ---------- 3. Facce del troncato ----------
def newell_normal(verts):
    v = PTS[verts]
    n = np.zeros(3)
    for k in range(len(v)):
        a, b = v[k], v[(k + 1) % len(v)]
        n += np.cross(a, b)
    n /= np.linalg.norm(n)
    return n

def orient_outward(verts):
    """Ordina ciclicamente i vertici di una faccia e la orienta verso l'esterno."""
    # i vertici sono gia' in ordine ciclico; si prova entrambe le orientazioni
    n1 = newell_normal(verts)
    c = PTS[verts].mean(0)
    if np.dot(n1, c) < 0:
        verts = list(reversed(verts))
    return verts

faces = []  # lista di liste di vid, orientate esternamente

# 12 pentagoni: uno per vertice dell'icosaedro
for u in range(NICO):
    # ordine ciclico dei vicini di u: proietta sul piano perp a u
    nb = sorted(ADJ[u])
    axis = ICO[u] / np.linalg.norm(ICO[u])
    ref = np.array([1.0, 0, 0])
    if abs(np.dot(ref, axis)) > 0.9:
        ref = np.array([0.0, 1.0, 0])
    e1 = np.cross(axis, ref); e1 /= np.linalg.norm(e1)
    e2 = np.cross(axis, e1)
    ang = []
    for v in nb:
        w = ICO[v] - np.dot(ICO[v], axis) * axis
        ang.append((np.arctan2(np.dot(w, e2), np.dot(w, e1)), v))
    order = [v for _, v in sorted(ang)]
    pent = [VID[(u, v)] for v in order]
    faces.append(orient_outward(pent))

# 20 esagoni: uno per faccia dell'icosaedro
for (a, b, c) in ico_faces:
    hexv = [VID[(a, b)], VID[(b, a)], VID[(b, c)], VID[(c, b)],
            VID[(c, a)], VID[(a, c)]]
    faces.append(orient_outward(hexv))

NF = len(faces)
assert NF == 32
sizes = sorted(len(f) for f in faces)
assert sizes.count(5) == 12 and sizes.count(6) == 20

# spigoli: coppie consecutive nelle facce
edge_set = {}
for fi, f in enumerate(faces):
    m = len(f)
    for k in range(m):
        a, b = f[k], f[(k + 1) % m]
        key = (min(a, b), max(a, b))
        edge_set.setdefault(key, []).append(fi)
assert len(edge_set) == 90
assert all(len(v) == 2 for v in edge_set.values())

# mappa: spigolo -> (f,g) con f,g le due facce; e vertici dell'estremo
# per ogni spigolo serve la direzione t: usiamo il versore geometrico
# dello spigolo (indipendente dall'orientamento: T_fg non dipende dal segno di t)
edge_list = []
for (a, b), (f, g) in edge_set.items():
    pa, pb = PTS[a], PTS[b]
    t = (pb - pa) / np.linalg.norm(pb - pa)
    edge_list.append((a, b, f, g, t))

# ---------- 4. Basi facciali e normali ----------
FN = np.zeros((NF, 3))
BF = np.zeros((NF, 3, 2))
for fi, f in enumerate(faces):
    FN[fi] = newell_normal(f)
    # e1 = direzione del primo spigolo (gia' tangente), e2 = n x e1
    a, b = f[0], f[1]
    e1 = PTS[b] - PTS[a]
    e1 -= np.dot(e1, FN[fi]) * FN[fi]
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(FN[fi], e1)
    BF[fi, :, 0] = e1
    BF[fi, :, 1] = e2
    assert np.allclose(np.cross(BF[fi,:,0], BF[fi,:,1]), FN[fi])

# ---------- 5. Matrici di trasporto A_fg ----------
def transport(f, g, t):
    """A_fg in SO(2): ruota il piano tangente di f in quello di g."""
    nf, ng = FN[f], FN[g]
    mf = np.cross(nf, t)
    mg = np.cross(ng, t)
    T = np.outer(t, t) + np.outer(mg, mf)
    return BF[g].T @ T @ BF[f]

A = {}  # (f,g) -> matrice 2x2
for (a, b, f, g, t) in edge_list:
    Afg = transport(f, g, t)
    Agf = transport(g, f, t)
    A[(f, g)] = Afg
    A[(g, f)] = Agf

# ---------- 6. Grafo duale, albero, D_f ----------
dual_adj = {i: set() for i in range(NF)}
for (a, b, f, g, t) in edge_list:
    dual_adj[f].add(g)
    dual_adj[g].add(f)

def spanning_tree(order):
    """BFS/DFS da f0; ritorna D_f e il cammino albero."""
    f0 = 0
    D = {f0: np.eye(2)}
    parent = {f0: None}
    # cammini: lista di archi (f,g) nell'ordine di visita
    visited = {f0}
    stack = [f0] if order == "dfs" else [f0]
    paths = {f0: []}
    while stack:
        f = stack.pop(0) if order == "bfs" else stack.pop()
        for g in sorted(dual_adj[f]):
            if g not in visited:
                visited.add(g)
                parent[g] = f
                D[g] = A[(f, g)] @ D[f]
                paths[g] = paths[f] + [(f, g)]
                stack.append(g)
    assert len(visited) == NF
    return D, paths, parent

D_bfs, paths_bfs, _ = spanning_tree("bfs")
D_dfs, paths_dfs, _ = spanning_tree("dfs")

def cycle_holonomy(path_fwd, path_bwd):
    """Olonomia del ciclo: path f0->f poi ritorno lungo path_bwd (f0->f)."""
    # cammina path_fwd da f0 a f, poi path_bwd all'inverso da f a f0
    M = np.eye(2)
    seq = list(path_fwd) + [(g, f) for (f, g) in reversed(path_bwd)]
    # M accumula a sinistra: v -> A_{fg} v per ogni arco (f,g)
    for (f, g) in seq:
        M = A[(f, g)] @ M
    return M

def angle_of(M):
    return float(np.degrees(np.arctan2(M[1, 0], M[0, 0])))

# ---------- 7. Verifiche ----------
rep = {}

# isometria + orientazione + inversa
max_iso = max_det = max_inv = 0.0
for (f, g), M in A.items():
    max_iso = max(max_iso, np.abs(M.T @ M - np.eye(2)).max())
    max_det = max(max_det, abs(np.linalg.det(M) - 1.0))
    max_inv = max(max_inv, np.abs(A[(g, f)] @ M - np.eye(2)).max())
rep["A_isometry_residual"] = max_iso
rep["A_det_minus_1"] = max_det
rep["A_inverse_residual"] = max_inv

# ricorrenza D_g = A_fg D_f sugli archi dell'albero
max_rec = 0.0
for g, p in [(g, paths_bfs[g]) for g in paths_bfs if g != 0]:
    f = paths_bfs[g][-1][0]
    max_rec = max(max_rec, np.abs(D_bfs[g] - A[(f, g)] @ D_bfs[f]).max())
rep["D_recurrence_residual"] = max_rec

# olonomia attorno a ogni vertice: 3 facce incidenti
vertex_faces = {v: [] for v in range(NV)}
for fi, f in enumerate(faces):
    for v in f:
        vertex_faces[v].append(fi)
assert all(len(vertex_faces[v]) == 3 for v in range(NV))

# ordine ciclico delle 3 facce attorno al vertice:
# gli spigoli del vertice v, ordinati per angolo nel piano perp a p_v
vert_holo = []
for v in range(NV):
    pv = PTS[v]
    axis = pv / np.linalg.norm(pv)
    ref = np.array([1.0, 0, 0])
    if abs(np.dot(ref, axis)) > 0.9:
        ref = np.array([0.0, 1.0, 0])
    e1 = np.cross(axis, ref); e1 /= np.linalg.norm(e1)
    e2 = np.cross(axis, e1)
    # i 3 spigoli uscenti da v: vertici adiacenti
    adj_v = set()
    for fi in vertex_faces[v]:
        f = faces[fi]
        k = f.index(v)
        adj_v.add(f[(k - 1) % len(f)])
        adj_v.add(f[(k + 1) % len(f)])
    adj_v = list(adj_v)
    assert len(adj_v) == 3
    ang = []
    for w in adj_v:
        d = PTS[w] - pv
        d = d - np.dot(d, axis) * axis
        ang.append((np.arctan2(np.dot(d, e2), np.dot(d, e1)), w))
    order_w = [w for _, w in sorted(ang)]
    # faccia "opposta" allo spigolo (w_i,w_{i+1})? ogni faccia contiene
    # due spigoli consecutivi: la faccia tra w_i e w_{i+1}
    face_seq = []
    for i in range(3):
        w1, w2 = order_w[i], order_w[(i + 1) % 3]
        for fi in vertex_faces[v]:
            f = faces[fi]
            if v in f and w1 in f and w2 in f:
                face_seq.append(fi)
                break
    assert len(face_seq) == 3
    f1, f2, f3 = face_seq
    M = A[(f3, f1)] @ A[(f2, f3)] @ A[(f1, f2)]
    vert_holo.append(angle_of(M))

vert_holo = np.array(vert_holo)
rep["vertex_holonomy_deg_min"] = float(vert_holo.min())
rep["vertex_holonomy_deg_max"] = float(vert_holo.max())
rep["vertex_holonomy_abs_deg"] = float(np.abs(vert_holo).mean())
rep["total_vertex_curvature_deg"] = float(np.abs(vert_holo).sum())
rep["n_vertices_12deg"] = int(np.sum(np.isclose(np.abs(vert_holo), 12.0, atol=1e-6)))

# gauge: albero BFS vs DFS -> olonomie dei cammini devono coincidere
max_gauge = 0.0
for f in range(NF):
    if f == 0:
        continue
    W_bfs = cycle_holonomy(paths_bfs[f], paths_bfs[f])  # cammino banale
    # W_f = D_dfs[f] D_bfs[f]^{-1}: confronto con olonomia del ciclo
    # (path_bfs + reverse(path_dfs))
    M = np.eye(2)
    seq = list(paths_bfs[f]) + [(g, ff) for (ff, g) in reversed(paths_dfs[f])]
    for (ff, gg) in seq:
        M = A[(ff, gg)] @ M
    W = D_dfs[f] @ np.linalg.inv(D_bfs[f])
    # l'olonomia del ciclo chiuso (bfs -> f, ritorno dfs) e' W^{-1}
    max_gauge = max(max_gauge, np.abs(W.T - M).max())
rep["gauge_holonomy_consistency"] = max_gauge

# ---------- 8. M_f candidato: G_f = B_f D_f, M_f = nabla g|_f - G_f ----------
# non abbiamo un campo g: usiamo nabla g|_f = B_f (riferimento piatto)
Mnorms = []
for fi in range(NF):
    D = D_bfs[fi]
    Mf = BF[fi] @ (np.eye(2) - D)
    Mnorms.append(np.linalg.norm(Mf))
rep["M_f_candidate_norm_min"] = float(min(Mnorms))
rep["M_f_candidate_norm_max"] = float(max(Mnorms))
rep["M_f_candidate_norm_mean"] = float(np.mean(Mnorms))
rep["n_faces_D_identity"] = int(sum(1 for fi in range(NF)
                                   if np.allclose(D_bfs[fi], np.eye(2))))

# ---------- 9. Output ----------
result = {
    "date": STAMP,
    "construction": "p_ij = (2u_i+u_j)/3 su icosaedro; A_fg = B_g^T T_fg B_f; "
                    "D_g = A_fg D_f su albero del grafo duale",
    "counts": {"vertices": int(NV), "edges": len(edge_list), "faces": NF,
               "pentagons": 12, "hexagons": 20,
               "radius": float(RADIUS[0])},
    "edge_length": float(np.linalg.norm(PTS[edge_list[0][1]] - PTS[edge_list[0][0]])),
    "checks": rep,
}

jpath = OUT_DIR / f"truncated_icosahedron_transports_{STAMP}.json"
jpath.write_text(json.dumps(result, indent=2, ensure_ascii=False))

np.savez_compressed(
    OUT_DIR / f"truncated_icosahedron_transports_{STAMP}.npz",
    vertices=PTS, faces=np.array([f + [-1] * (6 - len(f)) for f in faces]),
    face_normals=FN, face_bases=BF,
    D_bfs=np.array([D_bfs[i] for i in range(NF)]),
    D_dfs=np.array([D_dfs[i] for i in range(NF)]),
    vertex_holonomy_deg=vert_holo,
)

print(json.dumps(result, indent=2, ensure_ascii=False))
print("saved:", jpath)
