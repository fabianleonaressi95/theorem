"""Flat Weitzenboeck branch on the finite Q6 carrier."""
import json
import numpy as np
from scripts.audit_q6_discrete_cartan import I3, reconstruct_seed, spatial_coframes, q6_squares, random_so3

def build_teleparallel_branch(X=None, edges=None, E=None, gauge=None):
    if X is None or edges is None:
        X0, e0 = reconstruct_seed()
        X = X0 if X is None else X
        edges = e0 if edges is None else edges
    if E is None:
        E = spatial_coframes(X)
    index = {(int(g), int(h)): i for i, (g, h, _) in enumerate(edges)}
    links = np.repeat(I3[None, :, :], len(edges), axis=0)
    theta = np.asarray([E[g] @ (X[h] - X[g]) for g, h, _ in edges])
    if gauge is not None:
        links = np.asarray([gauge[h] @ U @ gauge[g].T for U, (g, h, _) in zip(links, edges)])
        theta = np.asarray([gauge[g] @ t for t, (g, h, _) in zip(theta, edges)])
    def edge(a, b):
        if a < b:
            i = index[(a, b)]
            return links[i], theta[i]
        i = index[(b, a)]
        return links[i].T, -links[i] @ theta[i]
    torsions, holonomies = [], []
    for square in q6_squares():
        P, tau = I3.copy(), np.zeros(3)
        for a, b in zip(square, square[1:] + square[:1]):
            U, t = edge(a, b)
            tau += P.T @ t
            P = U @ P
        torsions.append(tau)
        holonomies.append(P)
    torsions, holonomies = np.asarray(torsions), np.asarray(holonomies)
    return {"links": links, "coframe_edges": theta, "torsions": torsions,
            "holonomies": holonomies, "squares": q6_squares(),
            "flat_holonomy_residual_max": max(float(np.linalg.norm(H-I3)) for H in holonomies)}

def gauge_audit(X, edges, E, base):
    rng = np.random.default_rng(20261128)
    G = np.asarray([random_so3(rng) for _ in range(64)])
    changed = build_teleparallel_branch(X, edges, E, G)
    tr, hr = [], []
    for i, p in enumerate(base["squares"]):
        g = G[p[0]]
        tr.append(float(np.linalg.norm(changed["torsions"][i] - g @ base["torsions"][i])))
        hr.append(float(np.linalg.norm(changed["holonomies"][i] - g @ base["holonomies"][i] @ g.T)))
    return {"torsion_covariance_max": max(tr), "holonomy_conjugation_max": max(hr)}

def build_report():
    X, edges = reconstruct_seed()
    E = spatial_coframes(X)
    d = build_teleparallel_branch(X, edges, E)
    g = gauge_audit(X, edges, E, d)
    n = np.linalg.norm(d["torsions"], axis=1)
    return {"status": "FINITE_SPATIAL_FLAT_CONNECTION_BRANCH_GAUGE_COVARIANCE_AUDITED",
            "carrier": {"vertices": 64, "edges": 192, "square_faces": 240},
            "flat_branch": {"definition": "U_W,gh=I in the chosen global trivialization",
                "face_holonomy_residual_max": d["flat_holonomy_residual_max"],
                "nonzero_face_torsion_count": int(np.count_nonzero(n > 1e-10)),
                "mean_face_torsion_norm": float(np.mean(n)),
                "max_face_torsion_norm": float(np.max(n))},
            "gauge_covariance": g,
            "limits": ["The flat connection is a pure-gauge representative, not selected by field equations.",
                "The closure defect is a finite discrete torsion observable; continuum Cartan limit is open.",
                "No Lorentzian lift, physical time leg, TEGR action, or equivalence theorem is established."]}

if __name__ == "__main__":
    report = build_report()
    print(json.dumps(report, indent=2))
    if report["flat_branch"]["face_holonomy_residual_max"] > 1e-12:
        raise SystemExit("flat plaquette holonomy check failed")
    if max(report["gauge_covariance"].values()) > 1e-10:
        raise SystemExit("gauge covariance failed")
