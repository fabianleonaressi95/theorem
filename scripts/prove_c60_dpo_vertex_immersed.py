#!/usr/bin/env python3
"""
Chiusura dei tre punti aperti del test DPO per la g candidata sul C60.

1. CONTRIBUTI VERTICI: la determining sequence lascia regioni di taglia ~h
   attorno ai 60 vertici. Costruisco il cap esplicito: partition of unity
   sulle 3 wedge incidenti, C(x) = sum_i w_i(x) g_{f_i}(x). Stimavo
   ∫_cap |∇C| dA ~ O(h) e lo verifico numericamente.

2. IMMERSA: rango di ∇S negli strip di transizione (3x2). Se sigma_min>0
   su tutta la strip, g_h e' immersione locale. Verifico il minimo.

3. INIETTIVITA' GLOBALE: sondata delle immagini delle 32 facce sotto g
   (ripiego polygonale). Se le immagini di facce non adiacenti non si
   intersecano, l'immersione e' embedded.

Output: audits/c60_dpo_vertex_immersed_<data>.json
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

# traslazioni LS
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

rep = {}

# ---------- 1. cap ai vertici ----------
# Per ogni vertice: 3 wedge (uno per faccia). Angolo di ogni wedge = angolo
# interno della faccia al vertice. Fan intrinseco: 348 deg (deficit 12).
# Cap su disco intrinseco di raggio R: C(x) = sum_i w_i(x) g_{f_i}(x).
# w_i = bump angolare liscio centrato sulla bisettrice della wedge,
#       supportato dentro la wedge, taper radiale ->0 a r=R.
# stima: |∇C| <= sum_i (|∇w_i| |g_{f_i}| + w_i sqrt(2)) ; |∇w_i| ~ 1/R
#       -> ∫|∇C| ~ O(R). Verifico l'ordine su R = 0.1, 0.05, 0.025.

def vertex_cap_integral(v, R, nr=40, nt=120):
    """∫_cap |∇C| dA stimato su griglia polare intrinseca.
    Ritorna (integrale, area)."""
    fs = vfaces[v]
    assert len(fs) == 3
    pv = PTS[v]
    # angoli interni delle wedge al vertice v
    wedges = []  # (face, angolo_inizio, angolo_fine) nel fan di 348 deg
    theta = 0.0
    # ordine delle wedge: ordino per appartenenza ciclica attorno a pv
    # uso le facce in ordine ciclico (condividono spigoli consecutivi)
    # trova ordine ciclico: due wedge adiacenti condividono uno spigolo
    # permutazioni semplici
    import itertools
    best = None
    for perm in itertools.permutations(fs):
        ok = True
        for i in range(3):
            f1, f2 = perm[i], perm[(i + 1) % 3]
            # condividono un altro vertice (spigolo uscente da v)?
            shared = set(faces[f1]) & set(faces[f2]) - {v}
            if len(shared) != 1:
                ok = False; break
        if ok:
            best = perm; break
    assert best is not None
    # angolo interno di ogni faccia nel vertice v
    for fi in best:
        f = faces[fi]
        k = f.index(v)
        a = PTS[f[(k - 1) % len(f)]] - pv
        b = PTS[f[(k + 1) % len(f)]] - pv
        cosang = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
        wedges.append((fi, float(np.arccos(np.clip(cosang, -1, 1)))))
    total_ang = sum(w[1] for w in wedges)
    # posizioni nel fan
    bounds = [0.0]
    for _, ang in wedges:
        bounds.append(bounds[-1] + ang)
    # griglia: r in (0,R), phi in [0,total_ang)
    # mappa (r,phi) -> punto 3D: wedge i, coordinate locali
    # per ogni phi determina wedge e punto: il punto sulla faccia a distanza
    # r da v lungo la direzione phi. Uso le facce reali: per wedge i, il
    # punto e' v + r*(cos a * u1 + sin a * u2) con u1,u2 base della faccia.
    # Semplificazione: approssimo il cap con punti giunti dalle facce:
    # per ogni (r,phi) ricostruisco x nel R^3 dalla wedge corretta.
    # base ortonormale della faccia fi nel piano tangente
    tot_int = 0.0
    area = 0.0
    # per velocita': grigliaayana
    rs = np.linspace(0, R, nr)
    phis = np.linspace(0, total_ang, nt, endpoint=False)
    # precomputo per ogni phi: wedge index e angolo locale
    def wedge_of(phi):
        acc = 0.0
        for i, (_, ang) in enumerate(wedges):
            if phi < acc + ang:
                return i, phi - acc
            acc += ang
        return 2, wedges[2][1]
    # per ogni wedge: i due spigoli uscenti da v (vertici adiacenti)
    wedge_dirs = []
    for fi, _ in wedges:
        f = faces[fi]
        k = f.index(v)
        v_prev = f[(k - 1) % len(f)]
        v_next = f[(k + 1) % len(f)]
        # vettori dai due lati della wedge nel piano della faccia
        wedge_dirs.append((v_prev, v_next))
    # per il gradiente di C uso differenze finite in (r,phi):
    # C(r,phi) = sum_i w_i(r,phi) g_{f_i}(x(r,phi))
    # x(r,phi): punto a distanza r da v nella wedge, direzione locale phi
    # coordinate: x = v + r*(cos(phi)*e_start + sin(phi)*e_end_normalized)
    # approssimazione: proietto la direzione del fan sul piano della faccia
    def point_on_wedge(i, r, phi_loc):
        """Punto sulla faccia i a distanza r da v, angolo phi_loc dalla
        direzione del primo spigolo (v_prev)."""
        fi = wedges[i][0]
        vp, vn = wedge_dirs[i]
        # vettori 3D dai due lati
        fv = faces[fi]
        k = fv.index(v)
        up = PTS[vp] - pv; un = PTS[vn] - pv
        # interpola la direzione nel piano: normalizzo combinazione
        # uso parametrizzazione angolare reale: u(phi) = rotate up verso un
        # proiezione del gap. Approssimazione lineare in coordinate:
        # punto = v + r * d(phi), con d(phi) = normalize(cos*s0 + sin*s1)
        # dove s0,s1 sono le due direzioni spigolo (non ortonormali).
        # per semplicità uso coordinate di fan piane: mappo (r,phi) nel
        # riferimento intrinseco e poi "svilo" verso la faccia: dato che la
        # wedge e' piatta, la mappa e' una rotazione+scala del settore.
        # Implementazione esatta: la wedge e' un settore di angolo alpha
        # delimitato dalle direzioni up,un. Angolo locale phi in [0,alpha].
        # direzione = up ruotata di phi verso un (nel piano della faccia).
        n = FN[fi]
        # base: ruota up verso un di angolo alpha
        # angolo tra up e un:
        ca = np.dot(up, un) / (np.linalg.norm(up) * np.linalg.norm(un))
        alpha = float(np.arccos(np.clip(ca, -1, 1)))
        # rotazione nel piano: decompose un
        e1 = up / np.linalg.norm(up)
        e2 = np.cross(n, e1)
        # angolo di un nel piano
        beta = float(np.arctan2(np.dot(un, e2), np.dot(un, e1)))
        if beta < 0:
            beta += 2 * np.pi
        ang = beta * (phi_loc / alpha)
        d = np.cos(ang) * e1 + np.sin(ang) * e2
        return pv + r * d

    # valutazione di C su griglia (saltando r=0)
    def Cval(r, phi):
        i, pl = wedge_of(phi)
        x = point_on_wedge(i, r, pl)
        # partition of unity: w_i = bump centrato sulla wedge media
        # w_i(phi) = max(0, 1 - |phi - center_i| / (ang_i/2 + marg))
        # normalizzato; taper radiale: (1 - r/R)^2 per r<R
        vals = []
        for j, (fi_j, ang_j) in enumerate(wedges):
            lo = bounds[j]; hi = bounds[j + 1]
            cen = 0.5 * (lo + hi)
            # distanza angolare dal centro della wedge j
            dp = abs(phi - cen)
            w = max(0.0, 1.0 - dp / (0.5 * ang_j + 1e-9))
            vals.append(w)
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

    # gradiente per differenze finite in (log r? no: r,phi)
    # uso griglia (r,phi): gradiente intrinseco = (dC/dr, (1/r) dC/dphi)
    # area element = r dr dphi
    Cgrid = np.zeros((nr, nt, 3))
    for i, r in enumerate(rs):
        for j, phi in enumerate(phis):
            if r < 1e-9:
                Cgrid[i, j] = Cval(1e-6, phi)
            else:
                Cgrid[i, j] = Cval(r, phi)
    dr = rs[1] - rs[0] if nr > 1 else R
    dphi = phis[1] - phis[0] if nt > 1 else total_ang
    for i in range(1, nr - 1):
        for j in range(nt):
            jp = (j + 1) % nt; jm = (j - 1) % nt
            r = rs[i]
            if r < 1e-9:
                continue
            dCdr = (Cgrid[i + 1, j] - Cgrid[i - 1, j]) / (2 * dr)
            dCdphi = (Cgrid[i, jp] - Cgrid[i, jm]) / (2 * dphi)
            # norma gradiente intrinseco: |dC/dr|^2 + |dC/dphi|^2 / r^2
            gn2 = float(dCdr @ dCdr) + float(dCdphi @ dCdphi) / (r * r)
            gn = np.sqrt(max(gn2, 0.0))
            tot_int += gn * r * dr * dphi
            area += r * dr * dphi
    return float(tot_int), float(area)

cap_results = []
for R in [0.15, 0.075, 0.0375]:
    ti = 0.0; ar = 0.0
    for v in range(NV):
        iv, av = vertex_cap_integral(v, R, nr=24, nt=90)
        ti += iv; ar += av
    cap_results.append({"R": R, "cap_grad_L1": ti, "cap_area": ar})
    print(f"R={R}: cap |grad|_L1 = {ti:.4f}, area={ar:.4f}")
rep["vertex_cap"] = cap_results
rep["vertex_cap_scaling"] = "atteso ~O(R): confronta R=0.15 vs 0.0375"

# ---------- 2. immersione negli strip ----------
# strip gradient rank: S(s,u) 3x2, rank 2 se sigma_min > 0
# ricampiona per un sottoinsieme di spigoli a h=0.05
def edge_frame(a, b, f, g_):
    pa, pb = PTS[a], PTS[b]
    te = pb - pa; L_e = np.linalg.norm(te); te /= L_e
    cen_f = PTS[faces[f]].mean(0); cen_g = PTS[faces[g_]].mean(0)
    ef = np.cross(FN[f], te); eg = np.cross(FN[g_], te)
    mid = (pa + pb) / 2.0
    if np.dot(ef, cen_f - mid) < 0: ef = -ef
    if np.dot(eg, cen_g - mid) < 0: eg = -eg
    return pa, pb, te, L_e, ef, eg

h = 0.05
min_sv = np.inf
argmin = None
for ei, (a, b, f, g_, t) in enumerate(edge_list):
    pa, pb, te, L_e, ef, eg = edge_frame(a, b, f, g_)
    ns, nu = 60, 24
    ss = np.linspace(0, L_e, ns)
    us = np.linspace(-h / 2 + 1e-4, h / 2 - 1e-4, nu)
    # gradiente 3x2 per differenze finite
    for i in range(1, ns - 1):
        for j in range(1, nu - 1):
            s, u = ss[i], us[j]
            eta_p = ef if u >= 0 else eg
            def Sval(ss_, uu):
                eta = ef if uu >= 0 else eg
                x = pa + ss_ * te + uu * eta
                F = gf(f, x); G = gf(g_, x)
                lam = 0.5 - uu / h
                return (1 - lam) * F + lam * G
            ds = ss[1] - ss[0]; du = us[1] - us[0]
            dSds = (Sval(s + ds, u) - Sval(s - ds, u)) / (2 * ds)
            dSdu = (Sval(s, u + du) - Sval(s, u - du)) / (2 * du)
            Jm = np.column_stack([dSds, dSdu])   # 3x2
            sv = np.linalg.svd(Jm, compute_uv=False)
            if sv[1] < min_sv:
                min_sv = float(sv[1]); argmin = (ei, i, j)
rep["strip_min_sigma_min"] = min_sv
rep["strip_min_at"] = argmin
rep["strip_is_immersed"] = bool(min_sv > 1e-6)

# ---------- 3. auto-intersezione globale ----------
# immagine di ogni faccia: poligono g_f(vertici). Controllo distanza minima
# fra spigoli di immagini di facce non adiacenti (sonda: vertici -> facce).
# costruisco adiacenza facce
fadj = {i: set() for i in range(NF)}
for (a, b, f, g_, t) in edge_list:
    fadj[f].add(g_); fadj[g_].add(f)

# immagine dei vertici per ogni faccia
img = np.zeros((NF, 6, 3))
for fi, f in enumerate(faces):
    for k, v in enumerate(f):
        img[fi, k] = gf(fi, PTS[v])

def pt_tri_dist(p, a, b, c):
    """distanza punto-triangolo (approx: proiezione su piano + clamp)."""
    n = np.cross(b - a, c - a)
    nn = np.linalg.norm(n)
    if nn < 1e-12:
        return min(np.linalg.norm(p - a), np.linalg.norm(p - b), np.linalg.norm(p - c))
    n /= nn
    # proietta nel piano e clamp nei bordi (semplice: usa vertici e piedi)
    # per la sondata basta la distanza al piano se la proiezione e' dentro
    d = p - a
    dist_plane = abs(np.dot(d, n))
    # verifica se la proiezione cade nel triangolo (coordinate baricentriche)
    v0, v1, v2 = b - a, c - a, d - np.dot(d, n) * n
    d00, d01, d11 = v0 @ v0, v0 @ v1, v1 @ v1
    d20, d21 = v2 @ v0, v2 @ v1
    den = d00 * d11 - d01 * d01
    if abs(den) < 1e-12:
        return dist_plane
    vv = (d11 * d20 - d01 * d21) / den
    ww = (d00 * d21 - d01 * d20) / den
    uu = 1 - vv - ww
    if uu >= -1e-9 and vv >= -1e-9 and ww >= -1e-9:
        return dist_plane
    # altrimenti distanza minima ai lati
    def seg_dist(p, a, b):
        ab = b - a
        t = np.clip(np.dot(p - a, ab) / max(ab @ ab, 1e-12), 0, 1)
        return np.linalg.norm(p - (a + t * ab))
    return min(seg_dist(p, a, b), seg_dist(p, b, c), seg_dist(p, c, a))

min_nonadj = np.inf
pair_arg = None
for fi in range(NF):
    m = len(faces[fi])
    # triangoli fan della faccia fi
    tris_f = [(img[fi,0], img[fi,k], img[fi,k+1]) for k in range(1, m-1)]
    for gi in range(fi + 1, NF):
        if gi in fadj[fi]:
            continue
        m2 = len(faces[gi])
        tris_g = [(img[gi,0], img[gi,k], img[gi,k+1]) for k in range(1, m2-1)]
        # vertici di gi vs triangoli di fi e viceversa
        dmin = np.inf
        for p in img[gi, :m2]:
            for tri in tris_f:
                dmin = min(dmin, pt_tri_dist(p, *tri))
        for p in img[fi, :m]:
            for tri in tris_g:
                dmin = min(dmin, pt_tri_dist(p, *tri))
        if dmin < min_nonadj:
            min_nonadj = float(dmin); pair_arg = (fi, gi)
rep["min_nonadjacent_face_image_distance"] = min_nonadj
rep["min_nonadjacent_pair"] = pair_arg
rep["globally_embedded_probe"] = bool(min_nonadj > 1e-6)

result = {
    "date": STAMP,
    "candidate": "g_f = Q_f x + t_f, Q_f da D_BFS",
    "checks": rep,
    "notes": "cap vertex: partition of unity su 3 wedge, grad ~1/R, "
             "area ~R^2 -> contributo O(R). strip: sigma_min>0 => immersione "
             "locale. embedding: sondata vertice-facci su immagini polygonali.",
}
jpath = OUT_DIR / f"c60_dpo_vertex_immersed_{STAMP}.json"
jpath.write_text(json.dumps(result, indent=2, ensure_ascii=False))
print(json.dumps(result, indent=2, ensure_ascii=False))
print("saved:", jpath)
