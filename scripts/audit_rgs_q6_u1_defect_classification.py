#!/usr/bin/env python3
"""A18b: classify compact-U(1) branch defects on the finite Q6 cubical 6-cube.

Input is the A13 psu_fibre_connection_matrices.npz archive. This is a finite
combinatorial audit; it makes no continuum or physical-monopole claim.
"""
import argparse, itertools, json
from collections import Counter, defaultdict, deque
from pathlib import Path
import numpy as np


def wrap(x):
    return float((x + np.pi) % (2*np.pi) - np.pi)


def audit(path):
    z = np.load(path)
    X, edges, R = z["X"], z["edges"], z["R_SO3"]
    assert X.shape == (64, 3) and edges.shape == (192, 3) and R.shape == (192, 3, 3)
    n = X / np.linalg.norm(X, axis=1)[:, None]
    frames = []
    for nn in n:
        e = np.eye(3)[np.argmin(np.abs(nn))]
        u = e - np.dot(e, nn)*nn
        u /= np.linalg.norm(u)
        frames.append(np.column_stack((u, np.cross(nn, u), nn)))
    frames = np.asarray(frames)
    link = {}
    for (g, h, a), rot in zip(edges, R):
        B = frames[h].T @ rot @ frames[g]
        link[(int(g), int(a))] = float(np.arctan2(B[1, 0], B[0, 0]))

    def edge(g, a, sign):
        return link[(g, a)] if sign > 0 else -link[(g ^ (1 << a), a)]

    theta = {}
    for g in range(64):
        for a, b in itertools.combinations(range(6), 2):
            if (g >> a) & 1 or (g >> b) & 1:
                continue
            raw = (edge(g, a, 1) + edge(g ^ (1 << a), b, 1)
                   + edge(g ^ (1 << a) ^ (1 << b), a, -1)
                   + edge(g ^ (1 << b), b, -1))
            theta[(g, a, b)] = wrap(raw)

    cells = []
    for g in range(64):
        for a, b, c in itertools.combinations(range(6), 3):
            if any((g >> k) & 1 for k in (a, b, c)):
                continue
            S = (theta[(g ^ (1 << a), b, c)] - theta[(g, b, c)]
                 - theta[(g ^ (1 << b), a, c)] + theta[(g, a, c)]
                 + theta[(g ^ (1 << c), a, b)] - theta[(g, a, b)])
            m = int(round(S/(2*np.pi)))
            faces = [(g,b,c),(g^(1<<a),b,c),(g,a,c),
                     (g^(1<<b),a,c),(g,a,b),(g^(1<<c),a,b)]
            cells.append({"base":g,"axes":(a,b,c),"charge":m,"faces":faces})
    m = {(q["base"], q["axes"]):q["charge"] for q in cells}

    # Integer closure on all 4-cells.
    d_m = []
    for g in range(64):
        for a,b,c,d in itertools.combinations(range(6),4):
            if any((g >> k) & 1 for k in (a,b,c,d)):
                continue
            val = (m[(g^(1<<a),(b,c,d))]-m[(g,(b,c,d))]
                   -m[(g^(1<<b),(a,c,d))]+m[(g,(a,c,d))]
                   +m[(g^(1<<c),(a,b,d))]-m[(g,(a,b,d))]
                   -m[(g^(1<<d),(a,b,c))]+m[(g,(a,b,c))])
            d_m.append(val)

    # Support components: two charged 3-cells are adjacent iff they share a 2-face.
    support = [i for i,q in enumerate(cells) if q["charge"]]
    face_map = defaultdict(list)
    for i in support:
        for f in cells[i]["faces"]:
            face_map[f].append(i)
    adj = {i:set() for i in support}
    for ids in face_map.values():
        for i in ids:
            adj[i].update(j for j in ids if j != i)
    unseen, components = set(support), []
    while unseen:
        root = min(unseen); unseen.remove(root)
        todo, comp = deque([root]), []
        while todo:
            i = todo.popleft(); comp.append(i)
            for j in adj[i] & unseen:
                unseen.remove(j); todo.append(j)
        comp.sort()
        vals = [cells[i]["charge"] for i in comp]
        components.append({
            "size":len(comp), "charge_sum":sum(vals),
            "histogram":{str(k):v for k,v in sorted(Counter(vals).items())},
            "cells":[{"base_vertex":cells[i]["base"],"axes":list(cells[i]["axes"]),
                      "charge":cells[i]["charge"]} for i in comp]})
    vals = [q["charge"] for q in cells]
    return {
      "classification":"NUMERICAL_VERIFICATION",
      "complex":{"type":"full_nonperiodic_6_cube","vertices":64,"edges":192,
                 "plaquettes":len(theta),"three_cells":len(cells),"four_cells":len(d_m)},
      "charge_histogram":{str(k):v for k,v in sorted(Counter(vals).items())},
      "nonzero_cells":len(support),"total_integer_charge":sum(vals),
      "components_by_shared_square_face":components,
      "closure":{"max_abs_integer_d_m":max(map(abs,d_m),default=0),
                 "nonzero_four_cell_boundaries":sum(x!=0 for x in d_m),
                 "status":"PASS" if all(x==0 for x in d_m) else "FAIL"},
      "cohomology":{"H3_Z_of_I6":0,
        "reason":"The full 6-cube I^6 is contractible.",
        "consequence":"A closed integral 3-cochain is exact: m=d(beta) for some integral 2-cochain.",
        "caveat":"This is absolute cohomology of the nonperiodic cube; it implies no physical monopole or continuum magnetic charge."},
      "limits":["Finite cubical complex, not a periodic 6-torus.",
                "Principal-branch defects are not established physical monopoles.",
                "No continuum limit or physical source interpretation is established."]
    }


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--npz", required=True, type=Path)
    p.add_argument("--out", required=True, type=Path)
    a = p.parse_args()
    result = audit(a.npz)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k:result[k] for k in ("complex","charge_histogram","nonzero_cells",
                                             "total_integer_charge","components_by_shared_square_face",
                                             "closure","cohomology")}, indent=2))
    if result["closure"]["status"] != "PASS":
        raise SystemExit(1)
