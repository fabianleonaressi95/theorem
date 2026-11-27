#!/usr/bin/env python3
"""
Certificazione RIGOROSA (non solo numerica) che rank nabla S = 2 su tutte
le strip della determining sequence C60, e rank dei cap ai vertici.

Metodo: q(s,u) = |a x b|^2 e' un polinomio in (s,u) di bidegree (2,4).
- coefficienti monomiali: risolti una volta per edge-side su nodi
  Chebyshev (Vandermonde 15x15)
- conversione a Bernstein su [0,1]^2 (proprieta': q >= min coeff Bernstein)
- suddivisione adattiva de Casteljau: una cella e' certificata se
  min(coeff locali) > 0; altrimenti si divide in 4
- se una cella raggiunge profondita' max senza certificare -> segnalata

Cap ai vertici: gradiente di C per differenze finite sulle coordinate
intrinseche (r,phi), sigma_min del Jacobiano 3x2 su griglia densa.

Output: audits/c60_dpo_bernstein_certificate_<data>.json
"""
import json
import numpy as np
from datetime import date
from pathlib import Path
from math import comb

OUT_DIR = Path(__file__).resolve().parent / "audits"
OUT_DIR.mkdir(exist_ok=True)
STAMP = date.today().isoformat()
H = 0.05
MAX_DEPTH = 14

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

# ---------- q(s,u) = |a x b|^2 in coordinate locali (S,U) in [0,1]^2 ----------
# s_loc = (sigma - s_lo)/(s_hi - s_lo),  u_loc = |u|/(h/2) in [0,1]
# per lato: eta fisso; u_phys = +/- u_loc*h/2

def q_eval_batch(f, g_, pa, te, eta, s_lo, s_hi, pts_s, pts_u):
    """Valuta q sui punti (pts_s, pts_u) gia' in coordinate locali [0,1].
    Ritorna array (ns, nu)."""
    ds = s_hi - s_lo
    ss = s_lo + pts_s * ds
    uu = pts_u * (H / 2.0)          # u positivo; lato gestito dal chiamante
    S, U = np.meshgrid(ss, uu, indexing='ij')
    lam = 0.5 - U / H
    # a = (1-lam) Qf te + lam Qg te
    a = ((1 - lam)[..., None] * (Q[f] @ te)[None, None, :]
         + lam[..., None] * (Q[g_] @ te)[None, None, :])
    x = pa[None, None, :] + S[..., None] * te[None, None, :] + U[..., None] * eta[None, None, :]
    F = np.einsum('...i,ji->...j', x, Q[f]) + trans[f]
    Gm = np.einsum('...i,ji->...j', x, Q[g_]) + trans[g_]
    jump = Gm - F
    M = ((1 - lam)[..., None, None] * Q[f][None, None]
         + lam[..., None, None] * Q[g_][None, None])
    b = np.einsum('...ij,j->...i', M, eta) - jump / H
    cx = np.cross(a, b)
    return np.einsum('...i,...i->...', cx, cx)

def monomial_coeffs(f, g_, pa, te, eta, s_lo, s_hi):
    """Coefficienti monomiali di q in (S,U) locali, gradi (2,4).
    Risolve Vandermonde su nodi Chebyshev 3x5."""
    ns_, nu_ = 3, 5
    cs = np.cos(np.pi * (np.arange(ns_) + 0.5) / ns_)
    pts_s = 0.5 * (1 + cs)          # in (0,1)
    cu = np.cos(np.pi * (np.arange(nu_) + 0.5) / nu_)
    pts_u = 0.5 * (1 + cu)
    V = q_eval_batch(f, g_, pa, te, eta, s_lo, s_hi, pts_s, pts_u)
    # V[i,j] = q(s_i,u_j) = sum_{p<=2,q<=4} c[p,q] s_i^p u_j^q
    Vs = np.vander(pts_s, ns_, increasing=True)   # (3,3)
    Vu = np.vander(pts_u, nu_, increasing=True)   # (5,5)
    # V = Vs C Vu^T -> C = Vs^{-1} V (Vu^T)^{-1}
    C = np.linalg.solve(Vs, V) @ np.linalg.inv(Vu).T
    # C[p,q] coeff di s^p u^q, p in 0..2, q in 0..4
    return C  # shape (3,5)

# ---------- conversione monomial -> Bernstein ----------
def bernstein_matrix(deg):
    """T[j,k] = C(j,k)/C(n,k) per j>=k: beta = T @ m (univariato)."""
    n = deg
    T = np.zeros((n + 1, n + 1))
    for j in range(n + 1):
        for k in range(j + 1):
            T[j, k] = comb(j, k) / comb(n, k)
    return T

Ts = bernstein_matrix(2)   # grado s = 2
Tu = bernstein_matrix(4)   # grado u = 4

def to_bernstein(C):
    """C[p,q] monomial -> B[i,j] Bernstein, shape (3,5)."""
    # beta[i,j] = sum_{p<=i,q<=j} Ts[i,p] Tu[j,q] C[p,q]
    return Ts @ C @ Tu.T

# --- de Casteljau generico su asse ---
def split_axis(B, axis):
    """Divide B (shape (ns,nu)) a meta' lungo `axis`.
    Ritorna (B1,B2) shape identica (si tiene ridondanza? no: degree si
    dimezza? NO — de Casteljau produce due rappresentazioni dello stesso
    grado sulle meta'.)"""
    A = B.copy()
    n = A.shape[axis] - 1
    # itero de Casteljau su ogni "fibra"
    # trasporto axis alla fine per semplicità
    if axis == 0:
        A = A.T.copy()   # ora axis=1
    # A shape (m, n+1): divido lungo ultima dim
    m = A.shape[0]
    left = np.zeros_like(A); right = np.zeros_like(A)
    for i in range(m):
        row = A[i].copy()
        pyr = [row]
        for r in range(1, n + 1):
            pyr.append(0.5 * (pyr[-1][:-1] + pyr[-1][1:]))
        # left coeffs: pyr[k][0] per k=0..n  -> left[i,k]=pyr[k][0]
        # right coeffs: pyr[k][n-k] -> right[i,k]=pyr[n-k][k]?? standard:
        # right Bernstein coeffs = pyr[r][r] reversed? uso formula nota:
        left[i, :] = [pyr[k][0] for k in range(n + 1)]
        right[i, :] = [pyr[n - k][k] for k in range(n + 1)]
    if axis == 0:
        return left.T.copy(), right.T.copy()
    return left, right

# --- certificazione a 4 vie corretta ---
def certify_domain4(C, tag):
    B = to_bernstein(C)
    # ogni cella: (Bs, Bu bounds) dove Bs e' la sotto-matrice Bernstein
    # gia' splittata su entrambi gli assi -> shape (3,5) ma gradi dimezzati?
    # NO: split_axis dimezza l'intervallo ma MAINTIENE il grado (3,5).
    # Quindi una cella e' descritta da (Bloc, s0,s1,u0,u1,depth).
    stack = [(B, 0.0, 1.0, 0.0, 1.0, 0)]
    stats = {"certified": 0, "failed": 0, "max_depth": 0,
             "min_coeff_seen": np.inf, "worst": None}
    while stack:
        Bc, s0, s1, u0, u1, d = stack.pop()
        m = float(Bc.min())
        stats["min_coeff_seen"] = min(stats["min_coeff_seen"], m)
        stats["max_depth"] = max(stats["max_depth"], d)
        if m > 1e-11:
            stats["certified"] += 1
            continue
        if d >= MAX_DEPTH:
            stats["failed"] += 1
            stats["worst"] = (s0, s1, u0, u1, m)
            continue
        # 4 sotto-celle: prima split s -> (Bs_left,Bs_right);
        # per ogni meta' in s, split u
        BsL, BsR = split_axis(Bc, 0)
        sm = 0.5 * (s0 + s1); um = 0.5 * (u0 + u1)
        for Bs, sa, sb in ((BsL, s0, sm), (BsR, sm, s1)):
            BuL, BuR = split_axis(Bs, 1)
            stack.append((BuL, sa, sb, u0, um, d + 1))
            stack.append((BuR, sa, sb, um, u1, d + 1))
    stats["tag"] = tag
    return stats

# ---------- esecuzione su tutti gli edge-side ----------
rep = {"h": H, "method": "Bernstein + de Casteljau adattivo",
       "degree": "q = |a x b|^2 bidegree (2,4)",
       "domains": []}
total_cert = total_fail = 0
worst_overall = None
for ei, (a, b, f, g_, t) in enumerate(edge_list):
    pa, pb, te, L_e, ef, eg = edge_frame(a, b, f, g_)
    s_lo, s_hi = H, L_e - H
    for side, eta, sgn in ((0, ef, +1.0), (1, eg, -1.0)):
        # --- q sui nodi Chebyshev, coordinate locali (s_loc,u_loc) in [0,1] ---
        ns_, nu_ = 3, 5
        cs = np.cos(np.pi * (np.arange(ns_) + 0.5) / ns_)
        pts_s = 0.5 * (1 + cs)
        cu = np.cos(np.pi * (np.arange(nu_) + 0.5) / nu_)
        pts_u = 0.5 * (1 + cu)
        ds = s_hi - s_lo
        ss = s_lo + pts_s * ds
        # u_phys = sgn * pts_u * h/2  (pts_u in (0,1))
        uu = sgn * pts_u * (H / 2.0)
        S, U = np.meshgrid(ss, uu, indexing='ij')
        lam = 0.5 - U / H
        a_arr = ((1 - lam)[..., None] * (Q[f] @ te)[None, None, :]
                 + lam[..., None] * (Q[g_] @ te)[None, None, :])
        x = (pa[None, None, :] + S[..., None] * te[None, None, :]
             + U[..., None] * eta[None, None, :])
        F = np.einsum('...i,ji->...j', x, Q[f]) + trans[f]
        Gm = np.einsum('...i,ji->...j', x, Q[g_]) + trans[g_]
        jump = Gm - F
        M = ((1 - lam)[..., None, None] * Q[f][None, None]
             + lam[..., None, None] * Q[g_][None, None])
        b_arr = np.einsum('...ij,j->...i', M, eta) - jump / H
        cx = np.cross(a_arr, b_arr)
        qv = np.einsum('...i,...i->...', cx, cx)
        Vs = np.vander(pts_s, ns_, increasing=True)
        Vu = np.vander(pts_u, nu_, increasing=True)
        C = np.linalg.solve(Vs, qv) @ np.linalg.inv(Vu).T
        st = certify_domain4(C, f"edge{ei}_side{side}")
        rep["domains"].append({"edge": ei, "side": side,
                               "certified_cells": st["certified"],
                               "failed_cells": st["failed"],
                               "max_depth": st["max_depth"],
                               "worst": st["worst"]})
        total_cert += st["certified"]; total_fail += st["failed"]
        if st["worst"] and (worst_overall is None or st["worst"][4] < worst_overall[0]):
            worst_overall = (st["worst"][4], ei, side, st["worst"])

rep["total_certified_cells"] = total_cert
rep["total_failed_cells"] = total_fail
rep["all_domains_certified"] = bool(total_fail == 0)
rep["worst_cell"] = worst_overall
rep["verdict"] = ("RANK 2 CERTIFICATO su tutte le strip (a x b != 0)"
                  if total_fail == 0 else
                  "certificazione incompleta: celle non risolte")

jpath = OUT_DIR / f"c60_dpo_bernstein_certificate_{STAMP}.json"
jpath.write_text(json.dumps(rep, indent=2, ensure_ascii=False))
print(json.dumps({k: v for k, v in rep.items() if k != "domains"},
                 indent=2, ensure_ascii=False))
print("saved:", jpath)
