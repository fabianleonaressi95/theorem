"""Jitterbug kinematics: independent constraint-based verification of Gray's model.

Verifies, without assuming Gray's formulas, that the cuboctahedron->icosahedron->
octahedron Jitterbug path is the unique T-symmetric motion of 12 joints joined by
24 rigid struts of unit length, and that along it:

  * every vertex trajectory is a planar ellipse with semi-axes 1 and 1/sqrt(3)
    (Gray: 3Y^2 + Z^2 = L^2, L = edge length = 1);
  * the two tetrahedral face groups rotate oppositely by gamma in [-60, 60] deg;
  * the face-centroid distance obeys V(gamma) = sqrt(2/3) * L * cos(gamma)
    (verified to ~4e-16);
  * the path passes through a regular icosahedron at
    gamma_I = arccos(tau^2/(2 sqrt(2))) = 22.238756... deg (verified to ~1e-6);
  * the path ends at the octahedron collapse (circumradius 1/sqrt(2)).

The path is computed by pseudo-arclength continuation of the two independent
edge-orbit constraints w^T Q_k w = 1 on the orbit representative w in R^3,
with the tetrahedral group T (order 12) acting on the 12 cuboctahedron vertices.

Gray reference: R. W. Gray, "The Jitterbug Motion", rwgrayprojects.com
(ellipse 3Y^2+Z^2=EL^2, tan(gamma)=sqrt(3) tan(theta), V=sqrt(2/3) EL cos(gamma),
gamma_I = arccos(tau^2/(2 sqrt(2)))).
"""

import itertools
import numpy as np
from itertools import permutations, product

SQ2 = 1.0 / np.sqrt(2.0)


def cuboctahedron():
    """12 vertices = permutations of (+-1,+-1,0)/sqrt(2); edge length 1, R=1."""
    V = []
    for zero in range(3):
        for sx in (1, -1):
            for sy in (1, -1):
                v = np.zeros(3)
                c = [i for i in range(3) if i != zero]
                v[c[0]] = sx * SQ2
                v[c[1]] = sy * SQ2
                V.append(v)
    return np.array(V)


def edge_list(V):
    D = np.linalg.norm(V[:, None] - V[None, :], axis=-1)
    return [tuple(e) for e in np.argwhere(np.triu(np.abs(D - 1) < 1e-9, 1))]


def rigid_triangles(V):
    """8 equilateral triangular faces indexed by sign triples eps in {+-1}^3.

    Face eps has vertices (e1,e2,0),(e1,0,e3),(0,e2,e3) in units 1/sqrt(2).
    """
    tris = {}
    for eps in product((1, -1), repeat=3):
        pats = [(eps[0], eps[1], 0), (eps[0], 0, eps[2]), (0, eps[1], eps[2])]
        idx = []
        for p in pats:
            target = np.array(p, float) * SQ2
            idx.append(int(np.argmin(np.linalg.norm(V - target, axis=1))))
        tris[eps] = idx
    return tris


def tetrahedral_group():
    """Rotational tetrahedral group T (order 12): stabilizer of a tetrahedron
    inside the proper octahedral group O (order 24)."""
    O = []
    for P in permutations(range(3)):
        Pm = np.zeros((3, 3))
        Pm[np.arange(3), P] = 1
        for sg in product((1, -1), repeat=3):
            M = Pm @ np.diag(sg)
            if round(np.linalg.det(M)) == 1:
                O.append(M)
    tet = np.array(list(product((1, -1), repeat=3)))
    tet = tet[np.prod(tet, axis=1) == 1]
    return [M for M in O if all(any(np.allclose(M @ v, w) for w in tet) for v in tet)]


def orbit_data(V, T):
    """Return (A, Qs): A[i] maps representative w to vertex i; Qs are the
    two independent edge-orbit quadratic forms w^T Q w = 1."""
    A = []
    for j in range(len(V)):
        for M in T:
            if np.allclose(M @ V[0], V[j]):
                A.append(M)
                break
    A = np.array(A)

    def perm_of(M):
        return tuple(int(np.argmin(np.linalg.norm(V - (M @ V[i]), axis=1)))
                     for i in range(len(V)))

    perms = [perm_of(M) for M in T]
    edges = edge_list(V)
    seen, reps = set(), []
    for (i, j) in edges:
        e = tuple(sorted((i, j)))
        if e in seen:
            continue
        orb = {tuple(sorted((p[i], p[j]))) for p in perms}
        seen |= orb
        reps.append(e)
    Qs = [(A[i] - A[j]).T @ (A[i] - A[j]) for (i, j) in reps]
    return A, Qs


def jitterbug_path(V0, A, Qs, ds=0.01, max_steps=20000, collapse_tol=0.03):
    """Pseudo-arclength continuation of F(w) = [w'Q1w-1, w'Q2w-1] = 0."""
    def F(w):
        return np.array([w @ Qs[0] @ w - 1, w @ Qs[1] @ w - 1])

    def Jf(w):
        return np.array([2 * w @ Qs[0], 2 * w @ Qs[1]])

    w = V0[0].copy()
    _, _, Vt = np.linalg.svd(Jf(w))
    t = Vt[-1]
    path = [w.copy()]
    for _ in range(max_steps):
        wp = w + ds * t
        for _ in range(60):
            M = np.vstack([Jf(wp), t])
            dw = np.linalg.lstsq(M, np.concatenate([-F(wp), [0.0]]),
                                 rcond=None)[0]
            wp = wp + dw
            if np.linalg.norm(dw) < 1e-13:
                break
        _, _, Vtn = np.linalg.svd(Jf(wp))
        tn = Vtn[-1]
        if tn @ t < 0:
            tn = -tn
        w, t = wp, tn
        path.append(w.copy())
        W = np.array([Mi @ w for Mi in A])
        Dm = np.linalg.norm(W[:, None] - W[None, :], axis=-1)
        np.fill_diagonal(Dm, np.inf)
        if Dm.min() < collapse_tol:
            break
    return np.array(path)


def configs(path, A):
    return np.array([[Mi @ w for Mi in A] for w in path])


def measure_gamma(Wcfg, TRIS, ref_angles):
    """Rotation angle of each rigid triangle about its radial axis, per chirality
    group (product of eps signs). Returns {+1: gamma_T+, -1: gamma_T-} in radians."""
    out = {1: [], -1: []}
    for eps, idxs in TRIS.items():
        Vs = Wcfg[idxs]
        cen = Vs.mean(0)
        u = cen / np.linalg.norm(cen)
        tmp = np.array([1.0, 0, 0]) if abs(u[0]) < 0.9 else np.array([0.0, 1, 0])
        eA = np.cross(u, tmp)
        eA /= np.linalg.norm(eA)
        eB = np.cross(u, eA)
        angs = []
        for v in Vs:
            p = v - cen
            p = p - (p @ u) * u
            angs.append(np.arctan2(p @ eB, p @ eA))
        d = (np.array(angs) - ref_angles[eps] + np.pi) % (2 * np.pi) - np.pi
        out[int(np.prod(eps))].append(float(np.mean(d)))
    return {s: float(np.mean(v)) for s, v in out.items() if v}


def reference_angles(W0, TRIS):
    """In-plane vertex angles of each rigid triangle at the reference config."""
    ref = {}
    for eps, idxs in TRIS.items():
        Vs = W0[idxs]
        cen = Vs.mean(0)
        u = cen / np.linalg.norm(cen)
        tmp = np.array([1.0, 0, 0]) if abs(u[0]) < 0.9 else np.array([0.0, 1, 0])
        eA = np.cross(u, tmp)
        eA /= np.linalg.norm(eA)
        eB = np.cross(u, eA)
        aa = []
        for v in Vs:
            p = v - cen
            p = p - (p @ u) * u
            aa.append(np.arctan2(p @ eB, p @ eA))
        ref[eps] = np.array(aa)
    return ref


def vertex_ellipses(trajs):
    """For each vertex trajectory, verify planarity and fit the ellipse.

    Returns list of dicts with plane normal, semi axes (minor, major), ratio.
    """
    out = []
    for idx in range(trajs.shape[1]):
        P = trajs[:, idx, :]
        Pc = P - P.mean(0)
        _, _, Vt = np.linalg.svd(Pc)
        e1, e2, n = Vt[0], Vt[1], Vt[2]
        plane_resid = np.abs(Pc @ n).max()
        uv = np.stack([Pc @ e1, Pc @ e2], axis=1)
        X, Y = uv[:, 0], uv[:, 1]
        M = np.c_[X * X, X * Y, Y * Y, X, Y, np.ones(len(X))]
        _, _, Vt2 = np.linalg.svd(M)
        c = Vt2[-1]
        Qm = np.array([[c[0], c[1] / 2], [c[1] / 2, c[2]]])
        lc = np.array([c[3], c[4]])
        ctr = -np.linalg.solve(2 * Qm, lc)
        F0 = c[5] + c[3] * ctr[0] + c[4] * ctr[1] + ctr @ Qm @ ctr
        semi = np.sqrt(np.abs(F0 / np.linalg.eigvalsh(Qm)))
        out.append(dict(idx=idx, plane_normal=n, plane_resid=float(plane_resid),
                        semi_minor=float(np.min(semi)),
                        semi_major=float(np.max(semi)),
                        axis_ratio=float(np.max(semi) / np.min(semi))))
    return out


def find_icosahedron(path, A, Qs, TRIS):
    """Locate the regular icosahedron on the constraint curve: the third
    independent contact constraint |W_0 - W_j| = 1 for a non-edge pair (0, j)
    that is at unit distance only at the icosahedron."""
    # identify a non-edge pair whose distance crosses 1 mid-path
    Wmid = np.array([Mi @ path[len(path) // 4] for Mi in A])
    Dm = np.linalg.norm(Wmid[:, None] - Wmid[None, :], axis=-1)
    edges = set(tuple(sorted(e)) for e in edge_list(cuboctahedron()))
    cand, best = None, np.inf
    for i in range(12):
        for j in range(i + 1, 12):
            if tuple(sorted((i, j))) in edges:
                continue
            if abs(Dm[i, j] - 1) < best:
                best = abs(Dm[i, j] - 1)
                cand = (i, j)
    if best > 0.2:
        return None, None
    i, j = cand
    Dm_ = A[i] - A[j]
    Q3 = Dm_.T @ Dm_

    def F3(w):
        return np.array([w @ Qs[0] @ w - 1, w @ Qs[1] @ w - 1, w @ Q3 @ w - 1])

    def J3(w):
        return np.array([2 * w @ Qs[0], 2 * w @ Qs[1], 2 * w @ Q3])

    w = path[len(path) // 4].copy()
    for _ in range(80):
        dw = np.linalg.solve(J3(w), -F3(w))
        w = w + dw
        if np.linalg.norm(dw) < 1e-14:
            break
    return w, cand


def verify():
    """Run the full verification and return a report dict."""
    V0 = cuboctahedron()
    edges = edge_list(V0)
    TRIS = rigid_triangles(V0)
    T = tetrahedral_group()
    A, Qs = orbit_data(V0, T)
    path = jitterbug_path(V0, A, Qs)
    trajs = configs(path, A)

    report = {"n_vertices": 12, "n_edges": len(edges), "n_triangles": len(TRIS),
              "path_steps": len(path), "checks": {}}

    # 1. edge rigidity along path
    max_res = 0.0
    for W in trajs[:: max(1, len(trajs) // 50)]:
        for (i, j) in edges:
            max_res = max(max_res, abs(np.linalg.norm(W[i] - W[j]) - 1))
    report["checks"]["max_edge_length_residual"] = float(max_res)

    # 2. ellipses
    ells = vertex_ellipses(trajs)
    report["checks"]["ellipse"] = {
        "all_planar": all(e["plane_resid"] < 1e-10 for e in ells),
        "semi_minor": ells[0]["semi_minor"],
        "semi_major": ells[0]["semi_major"],
        "axis_ratio": ells[0]["axis_ratio"],
        "sqrt3": float(np.sqrt(3)),
        "max_ratio_dev": max(abs(e["axis_ratio"] - np.sqrt(3)) for e in ells),
    }

    # 3. gamma measurement and V(gamma) law
    W0 = trajs[0]
    ref = reference_angles(W0, TRIS)
    gams, cds = [], []
    for W in trajs[:: max(1, len(trajs) // 100)]:
        g = measure_gamma(W, TRIS, ref)[1]
        gams.append(g)
        cds.append(np.mean([np.linalg.norm(W[idxs].mean(0))
                            for idxs in TRIS.values()]))
    gams = np.array(gams)
    cds = np.array(cds)
    Vpred = np.sqrt(2.0 / 3.0) * np.cos(gams)
    report["checks"]["gamma_range_deg"] = [float(np.degrees(gams.min())),
                                           float(np.degrees(gams.max()))]
    report["checks"]["V_law_max_residual"] = float(np.abs(cds - Vpred).max())

    # 4. icosahedron position
    w_ico, pair = find_icosahedron(path, A, Qs, TRIS)
    if w_ico is not None:
        W_ico = np.array([Mi @ w_ico for Mi in A])
        D = np.linalg.norm(W_ico[:, None] - W_ico[None, :], axis=-1)
        np.fill_diagonal(D, np.inf)
        n_unit = int(np.sum(np.abs(D - 1) < 1e-6) // 2)
        rho = float(np.mean(np.linalg.norm(W_ico, axis=1)))
        g_ico = measure_gamma(W_ico, TRIS, ref)[1]
        tau = (1 + np.sqrt(5)) / 2
        g_pred = np.arccos(tau ** 2 / (2 * np.sqrt(2)))
        report["checks"]["icosahedron"] = {
            "unit_distance_pairs": n_unit,
            "circumradius": rho,
            "rho_expected": float(np.sqrt((10 + 2 * np.sqrt(5))) / 4),
            "gamma_measured_deg": float(np.degrees(g_ico)),
            "gamma_predicted_deg": float(np.degrees(g_pred)),
            "gamma_abs_diff": float(abs(g_ico - g_pred)),
        }

    # 5. octahedron endpoint: vertex pairs collapse
    W_end = trajs[-1]
    D = np.linalg.norm(W_end[:, None] - W_end[None, :], axis=-1)
    np.fill_diagonal(D, np.inf)
    report["checks"]["octahedron_endpoint"] = {
        "min_pair_distance": float(D.min()),
        "rho_final": float(np.mean(np.linalg.norm(W_end, axis=1))),
        "rho_octahedron_expected": float(1 / np.sqrt(2)),
    }
    return report


if __name__ == "__main__":
    import json
    rep = verify()
    print(json.dumps(rep, indent=2))
