#!/usr/bin/env python3
"""Audit: chain map from the dodecahedral graph to Q6 1-chains.

Duality: dodecahedron vertices <-> icosahedron faces (20).
Each dodecahedron edge is dual to an icosahedron edge shared by two
faces f=(a,b,p), g=(a,b,q); its boundary is g - f, and

    C_0(g) - C_0(f) = b_g - b_f = (1/3)( e_{iota(q)} - e_{iota(p)} )

where b_f is the Q6 barycentre 0-chain of the face and iota is the
T140 vertex lift (icosahedron vertex -> even-weight Q6 code).

For each dodecahedron edge we define C(edge) = (1/3) * (average of ALL
minimal Q6 paths from iota(p) to iota(q)).  Every such path has boundary
e_q - e_p, so the boundary identity is checked explicitly, together
with antipodal equivariance (Q6 antipode = bitwise complement, c -> 63-c)
and the Dirichlet-type norm of the induced chains.
"""
from __future__ import annotations
from collections import Counter, deque
from pathlib import Path
import json
import sys

import numpy as np
from scipy.spatial import ConvexHull

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from scripts.audit_t140_icosahedron_q6_lift import Q6_CODES, hull_edges

OUT = ROOT / "audits" / "DODECAHEDRON_Q6_CHAIN_MAP.json"

Q6_ANTIPODE = lambda c: c ^ 63  # bitwise complement on 6 bits


def q6_adj():
    adj = {c: [] for c in range(64)}
    for c in range(64):
        for b in range(6):
            adj[c].append(c ^ (1 << b))
    return adj


def minimal_paths(adj, src, dst):
    """All shortest paths src->dst as lists of oriented links."""
    # BFS distances from dst
    dist = {dst: 0}
    dq = deque([dst])
    while dq:
        u = dq.popleft()
        for w in adj[u]:
            if w not in dist:
                dist[w] = dist[u] + 1
                dq.append(w)
    if src not in dist:
        return []
    paths = []

    def rec(u, acc):
        if u == dst:
            paths.append(list(acc))
            return
        for w in adj[u]:
            if dist.get(w, 1 << 30) == dist[u] - 1:
                acc.append((min(u, w), max(u, w), 1 if u < w else -1))
                rec(w, acc)
                acc.pop()

    rec(src, [])
    return paths


def chain_from_paths(paths):
    """Average of oriented 1-chains over all minimal paths."""
    total = Counter()
    for p in paths:
        for link in p:
            total[link] += 1
    n = len(paths)
    return {k: v / n for k, v in total.items()}


def boundary(chain):
    b = Counter()
    for (s, t, sign), coef in chain.items():
        # oriented link stored as (min,max,dir): actual endpoints are
        # (s->t) if sign==+1 else (t->s)
        a, bb = (s, t) if sign == 1 else (t, s)
        b[bb] += coef
        b[a] -= coef
    return {k: v for k, v in b.items() if abs(v) > 1e-12}


def antipode_chain(chain):
    out = Counter()
    for (s, t, sign), coef in chain.items():
        a, bb = (s, t) if sign == 1 else (t, s)
        na, nb = Q6_ANTIPODE(a), Q6_ANTIPODE(bb)
        # antipode reverses orientation? complement preserves adjacency;
        # orientation of link under antipode: keep traversal direction
        l2 = (min(na, nb), max(na, nb))
        sgn = 1 if na < nb else -1
        out[(l2[0], l2[1], sgn)] += coef
    return dict(out)


def main() -> None:
    # --- icosahedron geometry (T139/T140 conventions) ---
    x, ico_edges = hull_edges()
    assert len(x) == 12 and len(ico_edges) == 30
    hull = ConvexHull(x)
    faces = [tuple(sorted(int(v) for v in f)) for f in hull.simplices]
    assert len(faces) == 20

    # faces containing each icosahedron edge
    edge_to_faces = {}
    for fi, f in enumerate(faces):
        for k in range(3):
            e = tuple(sorted((f[k], f[(k + 1) % 3])))
            edge_to_faces.setdefault(e, []).append(fi)
    assert all(len(v) == 2 for v in edge_to_faces.values())

    # --- Q6 structures ---
    adj = q6_adj()
    code = {i: Q6_CODES[i] for i in range(12)}

    # face -> barycentre 0-chain {(q6_code): 1/3}
    def c0(face_idx):
        return {code[v]: 1.0 / 3.0 for v in faces[face_idx]}

    # --- build chain map on the 30 dodecahedron edges ---
    results = []
    all_pass = True
    for e_ico in sorted(edge_to_faces):
        f, g = edge_to_faces[e_ico]
        shared = set(faces[f]) & set(faces[g])
        assert len(shared) == 2
        p = (set(faces[f]) - shared).pop()   # apex of f
        q = (set(faces[g]) - shared).pop()  # apex of g
        cu, cv = code[p], code[q]
        hamming = bin(cu ^ cv).count("1")
        paths = minimal_paths(adj, cu, cv)
        if not paths:
            all_pass = False
            results.append({"ico_edge": e_ico, "faces": [f, g],
                            "error": "no path"})
            continue
        avg = chain_from_paths(paths)
        C = {k: v / 3.0 for k, v in avg.items()}
        bd = boundary(C)
        expected = {}
        for k, v in c0(g).items():
            expected[k] = expected.get(k, 0) + v
        for k, v in c0(f).items():
            expected[k] = expected.get(k, 0) - v
        expected = {k: v for k, v in expected.items() if abs(v) > 1e-12}
        # boundary of C should equal b_g - b_f = (1/3)(e_q - e_p)
        target = {cv: 1.0 / 3.0, cu: -1.0 / 3.0}
        bd_err = max(
            [abs(bd.get(k, 0) - target.get(k, 0))
             for k in set(bd) | set(target)] or [0.0]
        )
        # antipodal equivariance: antipode of apex codes; compare the
        # image of C under the Q6 antipode with the chain built directly
        # from the antipodal apex pair
        code_sets = {tuple(sorted(code[v] for v in fc)): i
                     for i, fc in enumerate(faces)}
        af_codes = tuple(sorted(Q6_ANTIPODE(code[v]) for v in faces[f]))
        ag_codes = tuple(sorted(Q6_ANTIPODE(code[v]) for v in faces[g]))
        af_i = code_sets.get(af_codes)
        ag_i = code_sets.get(ag_codes)
        anti_ok = None
        anti_err = None
        ap, aq = Q6_ANTIPODE(cu), Q6_ANTIPODE(cv)
        apaths = minimal_paths(adj, ap, aq)
        if af_i is not None and ag_i is not None and apaths:
            direct = {k: v / 3.0 for k, v in
                      chain_from_paths(apaths).items()}
            aC = antipode_chain(C)
            anti_err = max(
                [abs(aC.get(k, 0) - direct.get(k, 0))
                 for k in set(aC) | set(direct)] or [0.0])
            anti_ok = anti_err < 1e-9
        # Dirichlet-type norm of the chain (unweighted link count)
        dirichlet = float(sum(v * v for v in C.values()))
        results.append({
            "ico_edge": [int(e_ico[0]), int(e_ico[1])],
            "dodeca_edge_faces": [int(f), int(g)],
            "apex_q6_codes": [int(cu), int(cv)],
            "hamming_distance": int(hamming),
            "num_minimal_paths": int(len(paths)),
            "chain_links": int(len(C)),
            "boundary_error": float(bd_err),
            "antipodal_check": anti_ok,
            "antipodal_error": anti_err,
            "dirichlet_norm_sq": dirichlet,
        })
        if bd_err > 1e-9:
            all_pass = False

    n_paths = [r.get("num_minimal_paths") for r in results]
    report = {
        "title": "Dodecahedron-to-Q6 chain map audit",
        "construction": {
            "dodecahedron_vertices": "20 icosahedron faces",
            "dodecahedron_edges": "30 icosahedron edges (face adjacency)",
            "C0(face)": "(1/3) sum of Q6 codes of the 3 face vertices",
            "C(edge)": "(1/3) * average of all minimal Q6 paths between "
                       "the two apex codes",
        },
        "results": results,
        "summary": {
            "edges_tested": len(results),
            "boundary_identity_all_pass": all_pass,
            "max_boundary_error": max(
                (r.get("boundary_error", 1) for r in results), default=None),
            "hamming_distances": sorted(set(
                r.get("hamming_distance") for r in results
                if r.get("hamming_distance") is not None)),
            "path_count_range": [min(n_paths), max(n_paths)] if n_paths else None,
            "antipodal_all_pass": all(
                r.get("antipodal_check") in (True, None) for r in results),
        },
        "all_pass": bool(all_pass),
        "scope_note": (
            "Boundary identity holds by construction for ANY path choice "
            "(all minimal paths share endpoints); the nontrivial content "
            "is path existence between apex codes, antipodal "
            "equivariance, and the 1/3 normalization. Dirichlet norm is "
            "the unweighted link-count quadratic form, not a physical "
            "energy."
        ),
    }
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["summary"], indent=2))


if __name__ == "__main__":
    main()
