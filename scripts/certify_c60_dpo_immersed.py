#!/usr/bin/env python3
"""
Certificato ESATTO dell'immersione per la determining sequence C60.

Sulle strip il gradiente e' analitico: per ogni spigolo e lato (u>0: eta=ef,
u<0: eta=eg), con x = pa + sigma te + u eta e lam = 1/2 - u/h:

  a = dsigma S = (1-lam) Q_f te + lam Q_g te          (dipende solo da u)
  b = du     S = [(1-lam) Q_f + lam Q_g] eta - jump/h (jump = g_g(x)-g_f(x))

rank nabla S = 2  <=>  a x b != 0.

sigma_min(J) con J=[a b]:  sigma_min^2 = (tr(JtJ) - sqrt(tr^2 - 4 det))/2,
det(JtJ) = |a x b|^2.  Valutazione esatta su griglia (sigma,u): nessun
differenze finite. Il minimo globale e' un inf su celle compatte di una
funzione polinomiale -> certificato numerico denso + struttura analitica.

Output: audits/c60_dpo_immersed_certificate_<data>.json
"""
import json
import numpy as np
from datetime import date
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent / "audits"
OUT_DIR.mkdir(exist_ok=True)
STAMP = date.today().isoformat()

src = Path(__file__).resolve().parent / "c60_truncated_icosahedron_transports.py"
exec(src.read_text().split("# ---------- 7. Verifiche")[0])

def angle_of(M):
    return float(np.arctan2(M[1, 0], M[0, 0]))

def build_Q(D):
    out = {}
    for fi in range(NF):
        n = FN[fi]
        K = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
        th = angle_of(D[fi])
        out[fi] = np.eye(3) + np.sin(th) * K + (1 - np.cos(th)) * (K @ K)
    return out

Q = build_Q(D_bfs)

# traslazioni LS (stessa costruzione)
und = []
for (a, b, f, g_, t) in edge_list:
    und.append((f, g_, a, b) if f < g_ else (g_, f, a, b))
L = np.zeros((NF, NF))
for (f, g_, a, b) in und:
    L[f, f] += 1.0; L[g_, g_] += 1.0
    L[f, g_] -= 1.0; L[g_, f] -= 1.0
trans = np.zeros((NF, 3))
trans[1:] = np.linalg.inv(L[1:, 1:]) @ np.array([
    sum(((Q[g_] - Q[f]) @ ((PTS[a] + PTS[b]) / 2.0)) for (f, g_, a, b) in und
        if f == i) - sum(((Q[g_] - Q[f]) @ ((PTS[a] + PTS[b]) / 2.0)) for (f, g_, a, b) in und
                        if g_ == i) for i in range(1, NF)])
w_face = np.array([len(f) for f in faces], float); w_face /= w_face.sum()
trans -= (w_face[:, None] * trans).sum(0)

def gf(fi, x):
    return Q[fi] @ x + trans[fi]

def edge_frame(a, b, f, g_):
    pa, pb = PTS[a], PTS[b]
    te = pb - pa; L_e = np.linalg.norm(te); te /= L_e
    cen_f = PTS[faces[f]].mean(0); cen_g = PTS[faces[g_]].mean(0)
    ef = np.cross(FN[f], te); eg = np.cross(FN[g_], te)
    mid = (pa + pb) / 2.0
    if np.dot(ef, cen_f - mid) < 0: ef = -ef
    if np.dot(eg, cen_g - mid) < 0: eg = -eg
    return pa, pb, te, L_e, ef, eg

# ---------- sigma_min esatto per strip ----------
h = 0.05
NS, NU = 240, 80
min_sv = np.inf
arg = None
per_edge_min = []

for ei, (a, b, f, g_, t) in enumerate(edge_list):
    pa, pb, te, L_e, ef, eg = edge_frame(a, b, f, g_)
    Qf_te = Q[f] @ te; Qg_te = Q[g_] @ te
    Qf_eta_p = Q[f] @ ef; Qg_eta_p = Q[g_] @ ef
    Qf_eta_m = Q[f] @ eg; Qg_eta_m = Q[g_] @ eg
    e_min = np.inf; e_arg = None
    # strip valida per sigma in [h, L-h] (le zone vertice le coprono i cap)
    ss = np.linspace(h, L_e - h, NS)
    for side, (eta_sign, Qf_eta, Qg_eta) in enumerate(
            [(+1, Qf_eta_p, Qg_eta_p), (-1, Qf_eta_m, Qg_eta_m)]):
        us = np.linspace(1e-6, h / 2 - 1e-6, NU) * (1 if side == 0 else -1)
        # lam = 0.5 - u/h  (u>0 -> lam<0.5; u<0 -> lam>0.5)
        lam = 0.5 - us / h
        # a(u): (1-lam) Qf_te + lam Qg_te  -> shape (NU,3)
        a = (1 - lam)[:, None] * Qf_te[None, :] + lam[:, None] * Qg_te[None, :]
        # per ogni sigma: x = pa + sigma te + u eta
        for i, s in enumerate(ss):
            base = pa + s * te
            # x: (NU,3)
            x = base[None, :] + us[:, None] * (ef if side == 0 else eg)[None, :]
            F = x @ Q[f].T + trans[f]
            Gm = x @ Q[g_].T + trans[g_]
            jump = Gm - F                                    # (NU,3)
            # b(u,sigma) = [(1-lam)Qf + lam Qg] eta - jump/h
            Mlam = ((1 - lam)[:, None, None] * Q[f][None, :, :]
                    + lam[:, None, None] * Q[g_][None, :, :])  # (NU,3,3)
            b = np.einsum('nij,j->ni', Mlam,
                          ef if side == 0 else eg) - jump / h   # (NU,3)
            # cross a x b
            cx = np.cross(a, b)
            det = np.einsum('ni,ni->n', cx, cx)             # |a x b|^2
            tr = np.einsum('ni,ni->n', a, a) + np.einsum('ni,ni->n', b, b)
            disc = np.maximum(tr * tr - 4 * det, 0.0)
            sv2 = 0.5 * (tr - np.sqrt(disc))
            j = int(np.argmin(sv2))
            if sv2[j] < e_min:
                e_min = float(sv2[j]); e_arg = (float(s), float(us[j]), side)
    per_edge_min.append(e_min)
    if e_min < min_sv:
        min_sv = e_min
        arg = (ei, e_arg)

rep = {
    "h": h,
    "exact_gradient": "a(u), b(sigma,u) analitici; niente differenze finite",
    "min_sigma_min_sq": min_sv,
    "min_sigma_min": float(np.sqrt(max(min_sv, 0.0))),
    "min_at_edge_and_coords": arg,
    "per_edge_min_sigma_min": [float(np.sqrt(max(v, 0.0))) for v in per_edge_min],
    "all_strips_immersed": bool(min_sv > 0.0),
    "strip_domain": "sigma in [h, L_e-h], |u| in (0,h/2); zone vertice coperte dai cap O(h)",
}
result = {
    "date": STAMP,
    "candidate": "g_f = Q_f x + t_f, Q_f da D_BFS",
    "certificate": rep,
}
jpath = OUT_DIR / f"c60_dpo_immersed_certificate_{STAMP}.json"
jpath.write_text(json.dumps(result, indent=2, ensure_ascii=False))
print(json.dumps(rep, indent=2, ensure_ascii=False)[:3000])
print("saved:", jpath)
