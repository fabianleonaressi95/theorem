#!/usr/bin/env python3
"""
Problema variazionale per la candidata g globale sul C60 (icosaedro troncato).

Il campo D_f (albero duale) fissa la connessione: il gradiente elastico
candidato e' G_f = B_f D_f. Ma una g con ∇g|_f = B_f D_f esatta ha salti
sugli spigoli (olonomia 12 gradi), mentre g = identita' ha salti nulli ma
M_f = B_f(I - D_f) grande. Il problema ben posto e' il compromesso:

  per ogni faccia f scegliamo liberamente l'angolo phi_f del gradiente
  E_f = rot(phi_f) in SO(2), cosi' che  ∇g|_f = B_f E_f.
  g_f(x) = Q_f(phi_f) x + t_f  con Q_f rotazione di phi_f attorno a n_f.
  Le traslazioni t_f sono fissate per LS (minimo salto) dato phi.

  F(phi; mu) = J(phi) + mu * sum_f ||B_f(E_f - D_f)||_F^2
             = J(phi) + 2 mu sum_f (1 - cos(phi_f - theta_f))

  J(phi) = somma sugli spigoli dei residui di salto minimi (dopo LS).

  mu -> 0 : g -> identita' (J=0, M grande)
  mu -> +inf : phi -> theta_D (J massima, M=0)

  Il fronte di Pareto E_min(J) e' la risposta: quanto disarrangiamento
  (salti) costa la fedelta' alla connessione.

Output: audits/c60_g_variational_tradeoff_<data>.json
"""
import json
import numpy as np
from datetime import date
from pathlib import Path
from scipy.optimize import minimize

OUT_DIR = Path(__file__).resolve().parent / "audits"
OUT_DIR.mkdir(exist_ok=True)
STAMP = date.today().isoformat()

src = Path(__file__).resolve().parent / "build_truncated_icosahedron_transports.py"
exec(src.read_text().split("# ---------- 7. Verifiche")[0])
# PTS, faces, FN, BF, A, D_bfs, D_dfs, edge_list, NF, NV

def angle_of(M):
    return float(np.arctan2(M[1, 0], M[0, 0]))

# theta_f dai campi D (BFS e DFS)
theta_bfs = np.array([angle_of(D_bfs[f]) for f in range(NF)])
theta_dfs = np.array([angle_of(D_dfs[f]) for f in range(NF)])

# archi non orientati e incidenza per il LS delle traslazioni
und = []
for (a, b, f, g_, t) in edge_list:
    und.append((f, g_, a, b) if f < g_ else (g_, f, a, b))
NU = len(und)

# sistema LS per t: Laplaciano del grafo duale (31 x 31, radice 0 pinnata)
L = np.zeros((NF, NF))
for (f, g_, a, b) in und:
    L[f, f] += 1.0; L[g_, g_] += 1.0
    L[f, g_] -= 1.0; L[g_, f] -= 1.0
Lr = L[1:, 1:]
Lr_inv = np.linalg.inv(Lr)
w_face = np.array([len(f) for f in faces], float); w_face /= w_face.sum()

def rodrigues(n, th):
    K = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
    return np.eye(3) + np.sin(th) * K + (1 - np.cos(th)) * (K @ K)

def solve_translations(Q):
    """t_f che minimizzano la somma dei salti quadratici. Ritorna (t, J)."""
    rhs = np.zeros((NF, 3))
    for (f, g_, a, b) in und:
        pa, pb = PTS[a], PTS[b]
        mid = (pa + pb) / 2.0
        d_e = (Q[g_] - Q[f]) @ mid
        rhs[f] += d_e; rhs[g_] -= d_e
    tr = np.zeros((NF, 3))
    tr[1:] = Lr_inv @ rhs[1:]
    tr -= (w_face[:, None] * tr).sum(0)   # gauge globale
    # energia dei salti: per ogni spigolo, 2 endpoint
    J = 0.0
    for (f, g_, a, b) in und:
        pa, pb = PTS[a], PTS[b]
        d = (Q[f] - Q[g_])
        df = tr[f] - tr[g_]
        ra = d @ pa + df
        rb = d @ pb + df
        J += float(ra @ ra + rb @ rb)
    return tr, J

def make_Q(phi):
    return [rodrigues(FN[f], phi[f]) for f in range(NF)]

def energy(phi, mu, theta_ref):
    Q = make_Q(phi)
    _, J = solve_translations(Q)
    Mterm = 2.0 * mu * float(np.sum(1.0 - np.cos(phi - theta_ref)))
    return J + Mterm

def jump_only(phi):
    Q = make_Q(phi)
    _, J = solve_translations(Q)
    return J

def m_term(phi, theta_ref, mu=1.0):
    return 2.0 * mu * float(np.sum(1.0 - np.cos(phi - theta_ref)))

# ----- punti di partenza -----
starts = {
    "phi=0 (identita')": np.zeros(NF),
    "phi=theta_BFS": theta_bfs.copy(),
    "phi=theta_DFS": theta_dfs.copy(),
}
rng = np.random.default_rng(20261121)
for k in range(3):
    starts[f"random{k}"] = rng.uniform(-np.pi, np.pi, NF)

# ----- curve mu -----
mus = [0.0, 1e-4, 1e-3, 1e-2, 3e-2, 0.1, 0.3, 1.0, 3.0, 10.0, 100.0]

results = []
for mu in mus:
    if mu == 0.0:
        phi_opt = np.zeros(NF)
        Q = make_Q(phi_opt); _, J = solve_translations(Q)
        Mv = m_term(phi_opt, theta_bfs)
        results.append({
            "mu": mu, "J_min": J, "M_term": Mv, "F": J,
            "mean_jump": float(np.sqrt(J / (2 * NU))),
            "rms_phi_minus_theta": float(np.sqrt(np.mean(
                (phi_opt - theta_bfs + np.pi) % (2 * np.pi) - np.pi) ** 2)),
        })
        print(f"mu={mu:g}  J={J:.4f}  Mterm={Mv:.4f}")
        continue
    best = None
    for name, phi0 in starts.items():
        res = minimize(energy, phi0, args=(mu, theta_bfs),
                       method="L-BFGS-B",
                       options={"maxiter": 300, "ftol": 1e-12, "gtol": 1e-8})
        phi_opt = res.x
        Q = make_Q(phi_opt); _, J = solve_translations(Q)
        Mv = m_term(phi_opt, theta_bfs)
        if best is None or res.fun < best[0]:
            best = (res.fun, phi_opt, J, Mv)
    _, phi_opt, J, Mv = best
    results.append({
        "mu": mu, "J_min": J, "M_term": Mv,
        "F": J + mu * Mv,
        "mean_jump": float(np.sqrt(J / (2 * NU))),
        "rms_phi_minus_theta": float(np.sqrt(np.mean(
            (phi_opt - theta_bfs + np.pi) % (2 * np.pi) - np.pi) ** 2)),
    })
    print(f"mu={mu:g}  J={J:.4f}  Mterm={Mv:.4f}  "
          f"rms_jump={np.sqrt(J/(2*NU)):.4f}")

# ----- riferimenti: identita' e D_BFS esatto -----
Q0 = make_Q(np.zeros(NF)); _, J0 = solve_translations(Q0)
QB = make_Q(theta_bfs); _, JB = solve_translations(QB)
QD = make_Q(theta_dfs); _, JD = solve_translations(QD)

summary = {
    "date": STAMP,
    "construction": "phi_f free SO(2) per face; Q_f=rot(n_f,phi_f); "
                    "g_f=Q_f x+t_f, t_f LS; F=J+mu*||M||^2",
    "counts": {"faces": NF, "dual_edges": NU},
    "references": {
        "identity_J": J0,
        "D_BFS_J": JB,
        "D_DFS_J": JD,
        "D_BFS_mean_rms_jump": float(np.sqrt(JB / (2 * NU))),
        "D_DFS_mean_rms_jump": float(np.sqrt(JD / (2 * NU))),
    },
    "pareto": results,
    "interpretation": "F(J,M) tradeoff: mu->0 identity, mu->inf connection-"
                      "following g with jumps; min J>0 for M=0 is the "
                      "holonomy obstruction",
}
jpath = OUT_DIR / f"c60_g_variational_tradeoff_{STAMP}.json"
jpath.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
print(json.dumps(summary["references"], indent=2))
print("saved:", jpath)
