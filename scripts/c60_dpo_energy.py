#!/usr/bin/env python3
"""
Livello energetico per la structured deformation (g,G) sul C60.

Funzionale candidato (anisotropia solo tramite il salto):
  E(u) = ∫_Σ w(|∇u|^2) dA + Σ_e ∫_e ψ(|[u]|) dσ
con w(t) = t (Dirichlet) e ψ(s) = s (lunghezza del salto) — scelte
canoniche; la struttura e' quella di Choksi-Fonseca: bulk + interfaccia.

Calcolo:
  - bulk sulla g esatta: |G_f|^2 = 2 -> 2*Area
  - interfaccia: massa dei salti (gia' nota = 38.93 per psi=|jump|)
  - E(g_h) per strip di larghezza h: misuro ∫strip |∇g_h|^2 dA (evolve
    con h: picco ~1/h^2 * area ~h -> contributo ~1/h * jump^2 -> DIVERGE
    per w=|.|^2? no: |∇S|^2 ha termine jump^2/h^2, area strip ~h ->
    ~jump^2/h -> diverge. Quindi w=|.|^2 NON e' la scelta coerente:
    l'energia di interfaccia deve essere separata (come in CF dove
    l'energia ha termine bulk W(∇u) + superficie ψ([u])).

  Verifica corretta: E(u) = ∫ W(∇u) dA + ∫_{S_u} ψ([u],ν) dH^1.
  Per g_h continua: S_{g_h}=vuoto, il "salto" e' regolarizzato negli
  strip -> il termine di superficie di g_h diventa bulk-extra.
  Attenzione: g_h e' la regolarizzazione continua e il test strip misura
  il suo costo, non quello della determining sequence CF.

  Per la coppia C60 nel documento formale, ∇_Σg = G_f = B_f D_f su ogni
  faccia. Quindi M=∇_Σg-G=0 e la successione costante u_n=g e' gia'
  determinante: u_n->g in L1 e ∇_Σu_n dA=G dA esattamente. I micro-salti
  non sono necessari nel bulk per questa coppia.

  Conseguenza: la divergenza quadratica degli strip continui NON esclude
  W(F)=|F|^2 nel problema CF. Lungo u_n=g il bulk quadratico vale 2*Area;
  il bulk lineare vale sqrt(2)*Area. Entrambi hanno costo finito. Il termine
  interfaciale qui calcolato usa tutti i 90 spigoli (200 campioni per spigolo).
  I costi sono upper bound per I(g,G), non l'infimo.

Output: audits/c60_dpo_energy_<data>.json
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

edge_data = []
for (a, b, f, g_, t) in edge_list:
    pa, pb, te, L_e, ef, eg = edge_frame(a, b, f, g_)
    edge_data.append(dict(f=f, g=g_, pa=pa, te=te, L=L_e, ef=ef, eg=eg))

# aree
face_area = []
for fi, f in enumerate(faces):
    c = PTS[f].mean(0); area = 0.0; m = len(f)
    for k in range(m):
        area += 0.5 * np.linalg.norm(np.cross(PTS[f[k]] - c, PTS[f[(k + 1) % m]] - c))
    face_area.append(area)
tot_area = float(np.array(face_area).sum())

# ---------- 1. bulk energy candidate: W(F) = |F|^2_F ----------
# |G_f|^2 = 2 (isometria 3x2) -> bulk = 2*Area
bulk_W2 = 2.0 * tot_area
# W(F) = |F| (TV-like): |G_f|_F = sqrt(2) -> sqrt(2)*Area
bulk_W1 = np.sqrt(2.0) * tot_area

# ---------- 2. interfaccia: Σ_e ∫ ψ(|jump|) dσ ----------
# ψ(s) = s (isotropo) -> gia' calcolato: tot_jump_mass = 38.93
# ψ(s) = s^2 -> calcolo
jump_mass_psi1 = 0.0; jump_mass_psi2 = 0.0
for e in edge_data:
    pa, te, L_e = e["pa"], e["te"], e["L"]
    ns = 200
    sig = np.linspace(0, L_e, ns)
    jm = np.array([np.linalg.norm(gf(e["g"], pa + s * te) - gf(e["f"], pa + s * te))
                   for s in sig])
    jump_mass_psi1 += float(np.trapezoid(jm, sig))
    jump_mass_psi2 += float(np.trapezoid(jm ** 2, sig))

# ---------- 3. E(g_h): energia bulk W2 sulle strip vs h ----------
# ∫strip |∇S|^2 dA ~ C/h (diverge) — verifico l'ordine
def strip_L2(e, h, ns=120, nu=40):
    pa, te, L_e, ef, eg = e["pa"], e["te"], e["L"], e["ef"], e["eg"]
    f, g_ = e["f"], e["g"]
    us = np.linspace(-h / 2, h / 2, nu)
    ss = np.linspace(0, L_e, ns)
    S = np.zeros((ns, nu, 3))
    for i, s in enumerate(ss):
        ex = pa + s * te
        for j, u in enumerate(us):
            eta = ef if u >= 0 else eg
            x = ex + u * eta
            F = gf(f, x); Gm = gf(g_, x)
            lam = 0.5 - u / h
            S[i, j] = (1 - lam) * F + lam * Gm
    ds = ss[1] - ss[0]; du = us[1] - us[0]
    tot = 0.0
    for i in range(1, ns - 1):
        for j in range(1, nu - 1):
            dSds = (S[i + 1, j] - S[i - 1, j]) / (2 * ds)
            dSdu = (S[i, j + 1] - S[i, j - 1]) / (2 * du)
            tot += float(dSds @ dSds + dSdu @ dSdu) * ds * du
    return tot

hs_test = [0.2, 0.1, 0.05]
strip_L2_by_h = {h: 0.0 for h in hs_test}
# solo 20 spigoli per velocita', scala per 90
for e in edge_data[:20]:
    for h in hs_test:
        strip_L2_by_h[h] += strip_L2(e, h)
for h in hs_test:
    strip_L2_by_h[h] *= 90.0 / 20.0
rep = {
    "bulk_W2_Dirichlet": bulk_W2,
    "bulk_W1_TV": bulk_W1,
    "surface_psi_s": jump_mass_psi1,
    "surface_psi_s2": jump_mass_psi2,
    "strip_integral_L2_by_h_scaled": {str(h): strip_L2_by_h[h] for h in hs_test},
}
# verifica divergenza ~1/h: rapporto
for h1, h2 in [(0.2, 0.1), (0.1, 0.05)]:
    rep[f"L2_ratio_{h1}_vs_{h2}"] = strip_L2_by_h[h1] / strip_L2_by_h[h2]
rep["CF_constant_sequence_energy_W1_plus_psi1"] = bulk_W1 + jump_mass_psi1
rep["CF_constant_sequence_energy_W2_plus_psi1"] = bulk_W2 + jump_mass_psi1
rep["CF_constant_sequence_status"] = (
    "u_n=g e' una determining sequence per la coppia C60 corrente poiche' "
    "∇_Σg=G faccia per faccia (M=0). Le energie W1/W2 sono upper bound "
    "numerici per I(g,G), non il valore dell'infimo."
)
rep["interpretation"] = (
    "I valori strip L2 sono un audit della regolarizzazione continua e "
    "campionano 20/90 spigoli con scaling. Non escludono W quadratica per "
    "CF: la successione costante u_n=g e' determinante per la coppia "
    "corrente (M=0), ha energia finita W1 e W2. L'interfaccia psi=s e' "
    "integrata su tutti i 90 spigoli con quadratura trapezoidale."
)
rep["regularization_TV_candidate"] = {
    "bulk": bulk_W1,
    "surface": jump_mass_psi1,
    "total_TV": bulk_W1 + jump_mass_psi1,
}
jpath = OUT_DIR / f"c60_dpo_energy_{STAMP}.json"
jpath.write_text(json.dumps(rep, indent=2, ensure_ascii=False))
print(json.dumps(rep, indent=2, ensure_ascii=False))
print("saved:", jpath)
