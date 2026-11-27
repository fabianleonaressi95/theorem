#!/usr/bin/env python3
"""
Rank check sui cap ai vertici della determining sequence C60.

Cap_v: disco intrinseco di raggio R attorno al vertice v, con
C(r,phi) = sum_i w_i(r,phi) g_{f_i}(x(r,phi)) — partition of unity sulle
3 wedge incidenti. Jacobiano 3x2 nelle coordinate intrinseche (r,phi):
colonne dC/dr e (1/r) dC/dphi. rank 2 <=> sigma_min > 0.

Verifica su griglia densa per tutti i 60 vertici, R = 0.05.
Output: audits/c60_dpo_cap_rank_<data>.json
"""
import itertools
import json
import numpy as np
from datetime import date
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent / "audits"
OUT_DIR.mkdir(exist_ok=True)
STAMP = date.today().isoformat()
R = 0.05

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

vfaces = {v: [] for v in range(NV)}
for fi, f in enumerate(faces):
    for v in f:
        vfaces[v].append(fi)

def cap_setup(v):
    """Ritorna (wedges, bounds, wedge_dirs): wedge = (face, angolo)."""
    fs = vfaces[v]
    pv = PTS[v]
    best = None
    for perm in itertools.permutations(fs):
        ok = True
        for i in range(3):
            shared = set(faces[perm[i]]) & set(faces[perm[(i + 1) % 3]]) - {v}
            if len(shared) != 1:
                ok = False; break
        if ok:
            best = perm; break
    wedges = []
    for fi in best:
        f = faces[fi]
        k = f.index(v)
        a = PTS[f[(k - 1) % len(f)]] - pv
        b = PTS[f[(k + 1) % len(f)]] - pv
        cosang = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
        wedges.append((fi, float(np.arccos(np.clip(cosang, -1, 1)))))
    bounds = [0.0]
    for _, ang in wedges:
        bounds.append(bounds[-1] + ang)
    total = bounds[-1]
    dirs = []
    for fi, _ in wedges:
        f = faces[fi]
        k = f.index(v)
        dirs.append((f[(k - 1) % len(f)], f[(k + 1) % len(f)]))
    return pv, wedges, bounds, total, dirs

def point_on_wedge(vdata, i, r, phi_loc):
    pv, wedges, bounds, total, dirs = vdata
    fi, ang_w = wedges[i]
    vp, vn = dirs[i]
    f = faces[fi]
    k = f.index(v_global)
    up = PTS[vp] - pv; un = PTS[vn] - pv
    n = FN[fi]
    e1 = up / np.linalg.norm(up)
    e2 = np.cross(n, e1)
    beta = float(np.arctan2(np.dot(un, e2), np.dot(un, e1)))
    if beta < 0:
        beta += 2 * np.pi
    ang = beta * (phi_loc / ang_w)
    d = np.cos(ang) * e1 + np.sin(ang) * e2
    return pv + r * d

def make_C(v):
    vdata = cap_setup(v)
    pv, wedges, bounds, total, dirs = vdata
    def wedge_of(phi):
        acc = 0.0
        for i, (_, ang) in enumerate(wedges):
            if phi < acc + ang:
                return i, phi - acc
            acc += ang
        return 2, wedges[2][1]
    def Cval(r, phi):
        i, pl = wedge_of(phi)
        x = point_on_wedge(vdata, i, r, pl)
        vals = []
        for j, (fi_j, ang_j) in enumerate(wedges):
            cen = 0.5 * (bounds[j] + bounds[j + 1])
            dp = abs(phi - cen)
            vals.append(max(0.0, 1.0 - dp / (0.5 * ang_j + 1e-9)))
        s = sum(vals)
        if s <= 0:
            vals = [1.0 if j == i else 0.0 for j in range(3)]
            s = 1.0
        rad = max(0.0, 1.0 - r / R) ** 2
        out = np.zeros(3)
        for j, (fi_j, ang_j) in enumerate(wedges):
            w = vals[j] / s * rad
            if w > 1e-12:
                out += w * gf(fi_j, x)
        return out
    return Cval, total

# punto_on_wedge usa v_global: lo imposto
results = []
gmin = np.inf; garg = None
NR, NT = 18, 72
for v_global in range(NV):
    Cval, total = make_C(v_global)
    vmin = np.inf; varg = None
    rs = np.linspace(R * 0.08, R * 0.92, NR)
    phis = np.linspace(0, total, NT, endpoint=False)
    dr = rs[1] - rs[0]; dphi = phis[1] - phis[0]
    # griglia C
    Cg = np.zeros((NR, NT, 3))
    for i, r in enumerate(rs):
        for j, phi in enumerate(phis):
            Cg[i, j] = Cval(r, phi)
    for i in range(NR):
        for j in range(NT):
            jp = (j + 1) % NT; jm = (j - 1) % NT
            r = rs[i]
            if r < 1e-9:
                continue
            dCdr = (Cg[min(i+1,NR-1), j] - Cg[max(i-1,0), j]) / ((min(i+1,NR-1)-max(i-1,0)) * dr)
            dCdphi = (Cg[i, jp] - Cg[i, jm]) / (2 * dphi)
            J = np.column_stack([dCdr, dCdphi / r])
            sv = np.linalg.svd(J, compute_uv=False)
            if sv[1] < vmin:
                vmin = float(sv[1]); varg = (float(r), float(phis[j]))
    results.append({"vertex": v_global, "min_sigma_min": vmin,
                    "at": varg})
    if vmin < gmin:
        gmin = vmin; garg = (v_global, varg)

results.sort(key=lambda d: d["min_sigma_min"])
rep = {
    "R": R,
    "grid": f"{NR}x{NT} per cap, FD su (r,phi)",
    "global_min_sigma_min": gmin,
    "global_argmin": garg,
    "worst_caps": results[:10],
    "all_caps_immersed": bool(gmin > 1e-9),
    "n_caps": NV,
}
jpath = OUT_DIR / f"c60_dpo_cap_rank_{STAMP}.json"
jpath.write_text(json.dumps(rep, indent=2, ensure_ascii=False))
print(json.dumps(rep, indent=2, ensure_ascii=False)[:2500])
print("saved:", jpath)
