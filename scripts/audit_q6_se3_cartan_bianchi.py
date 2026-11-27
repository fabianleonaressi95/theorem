#!/usr/bin/env python3
"""Affine SE(3) Cartan-link and exact cubical Bianchi audit on Q6.

The rotational link U_(g->h) and source-frame coframe increment theta_(g->h)
are packaged as the SE(3) element (U, U theta). The semidirect product is
(U,b)(V,c)=(UV,b+Uc). Reverse links are exact group inverses.

The cube Bianchi identity is evaluated as the six adjacent-swap loops in the
permutohedron of the three coordinate directions. Each face loop is parallel
transported to the cube's lower base vertex before ordered multiplication.
"""
from __future__ import annotations

import json
from itertools import combinations
import numpy as np

from scripts.audit_q6_discrete_cartan import (
    I3, reconstruct_seed, spatial_coframes, build_discrete_cartan,
    q6_squares, random_so3
)

ZERO = np.zeros(3)
IDENTITY = (I3.copy(), ZERO.copy())


def se3_mul(left, right):
    """Standard SE(3) product (U,b)(V,c)=(UV,b+Uc)."""
    U, b = left
    V, c = right
    return U @ V, b + U @ c


def se3_inv(g):
    U, b = g
    Ui = U.T
    return Ui, -Ui @ b


def se3_distance(g, h):
    U, b = g
    V, c = h
    return float(np.linalg.norm(U - V)), float(np.linalg.norm(b - c))


def se3_edge_from_coframe(U, theta):
    """Store affine translation b=U theta, so reverse edge is exact inverse."""
    return U, U @ theta


def q6_cubes():
    """All 160 elementary 3-cubes, represented by (lower_vertex, axes)."""
    out = []
    for axes in combinations(range(6), 3):
        free = set(axes)
        fixed = [i for i in range(6) if i not in free]
        for bits in range(1 << len(fixed)):
            base = 0
            for j, axis in enumerate(fixed):
                if (bits >> j) & 1:
                    base |= 1 << axis
            out.append((base, tuple(axes)))
    if len(out) != 160:
        raise AssertionError("Q6 must have 160 elementary 3-cubes")
    return out


def build_se3_links(X=None, edges=None, E=None, gauge=None):
    if X is None or edges is None:
        X0, e0 = reconstruct_seed()
        X = X0 if X is None else X
        edges = e0 if edges is None else edges
    if E is None:
        E = spatial_coframes(X)
    curved = build_discrete_cartan(X, edges, E)
    directed = {}
    for i, (g, h, _) in enumerate(edges):
        g, h = int(g), int(h)
        link = se3_edge_from_coframe(curved["links"][i],
                                     curved["coframe_edges"][i])
        directed[(g, h)] = link
        directed[(h, g)] = se3_inv(link)

    if gauge is not None:
        transformed = {}
        for (g, h), link in directed.items():
            transformed[(g, h)] = se3_mul(
                se3_mul(gauge[h], link), se3_inv(gauge[g])
            )
        directed = transformed

    return {"links": directed, "X": X, "edges": edges, "E": E,
            "squares": q6_squares(), "cubes": q6_cubes(),
            "curved_reference": curved}


def path_transport(links, start, axes):
    """SE(3) transporter along the positive coordinate path in axes order."""
    current = int(start)
    total = IDENTITY
    for axis in axes:
        nxt = current | (1 << axis)
        total = se3_mul(links[(current, nxt)], total)
        current = nxt
    return total


def face_holonomy(links, base, i, j):
    """Based face loop: path i,j followed by inverse path j,i."""
    yi = base | (1 << i)
    yj = base | (1 << j)
    yij = yi | (1 << j)
    path_ij = se3_mul(links[(yi, yij)], links[(base, yi)])
    path_ji = se3_mul(links[(yj, yij)], links[(base, yj)])
    return se3_mul(se3_inv(path_ji), path_ij)


def face_holonomies(links):
    out = []
    for base, j, k, ell in q6_squares():
        # Positive square: base -> j -> k -> ell -> base.
        axes = [a for a in range(6) if (j ^ base) & (1 << a)]
        axis_i = axes[0]
        axis_j = next(a for a in range(6) if (ell ^ base) & (1 << a))
        out.append(face_holonomy(links, base, axis_i, axis_j))
    return out


def cube_bianchi(links, base, axes):
    """Six-face Bianchi identity from adjacent swaps of three coordinate steps."""
    a, b, c = axes
    perms = [
        (a, b, c), (b, a, c), (b, c, a),
        (c, b, a), (c, a, b), (a, c, b), (a, b, c)
    ]
    total = IDENTITY
    for p, q in zip(perms[:-1], perms[1:]):
        swap = next(k for k in range(2) if p[k] != q[k])
        prefix = p[:swap]
        i, j = p[swap], p[swap + 1]
        face_base = int(base)
        for axis in prefix:
            face_base |= 1 << axis
        H_face = face_holonomy(links, face_base, i, j)
        P = path_transport(links, base, prefix)
        H_at_cube_base = se3_mul(
            se3_mul(se3_inv(P), H_face), P
        )
        total = se3_mul(H_at_cube_base, total)
    return total


def random_se3_gauge(seed=20261129):
    rng = np.random.default_rng(seed)
    return [
        (random_so3(rng), rng.normal(scale=0.25, size=3))
        for _ in range(64)
    ]


def gauge_transform_audit(data, seed=20261129):
    gauge = random_se3_gauge(seed)
    changed = build_se3_links(data["X"], data["edges"], data["E"], gauge)
    base_faces = face_holonomies(data["links"])
    changed_faces = face_holonomies(changed["links"])
    rot_res, trans_res = [], []
    for square, H, Hp in zip(data["squares"], base_faces, changed_faces):
        base = square[0]
        expected = se3_mul(se3_mul(gauge[base], H), se3_inv(gauge[base]))
        dr, dt = se3_distance(Hp, expected)
        rot_res.append(dr)
        trans_res.append(dt)

    bianchi_rot, bianchi_trans = [], []
    for base, axes in changed["cubes"]:
        H = cube_bianchi(changed["links"], base, axes)
        dr, dt = se3_distance(H, IDENTITY)
        bianchi_rot.append(dr)
        bianchi_trans.append(dt)
    return {
        "seed": seed,
        "face_holonomy_conjugation_rotation_max": max(rot_res),
        "face_holonomy_conjugation_translation_max": max(trans_res),
        "cube_bianchi_rotation_max": max(bianchi_rot),
        "cube_bianchi_translation_max": max(bianchi_trans),
    }


def build_report():
    X, edges = reconstruct_seed()
    E = spatial_coframes(X)
    data = build_se3_links(X, edges, E)
    faces = face_holonomies(data["links"])
    bianchi = [cube_bianchi(data["links"], base, axes)
               for base, axes in data["cubes"]]
    br = [float(np.linalg.norm(H[0] - I3)) for H in bianchi]
    bt = [float(np.linalg.norm(H[1])) for H in bianchi]

    rot_compare, trans_compare = [], []
    torsion_norms, curvature_angles = [], []
    for H_aff, H_ref, tau_ref, angle in zip(
        faces, data["curved_reference"]["holonomies"],
        data["curved_reference"]["torsions"],
        data["curved_reference"]["curvature_angles"]
    ):
        R, t = H_aff
        tau = R.T @ t
        rot_compare.append(float(np.linalg.norm(R - H_ref)))
        trans_compare.append(float(np.linalg.norm(tau - tau_ref)))
        torsion_norms.append(float(np.linalg.norm(tau)))
        curvature_angles.append(angle)

    gauge = gauge_transform_audit(data)
    return {
        "status": "FINITE_Q6_SE3_AFFINE_CARTAN_AND_CUBICAL_BIANCHI_AUDIT",
        "carrier": {
            "vertices": 64, "edges": 192, "square_faces": len(faces),
            "elementary_3_cubes": len(bianchi),
            "cube_axes": "20 coordinate triples, 8 fixed-bit choices each"
        },
        "affine_link": {
            "group": "SE(3)=SO(3) semidirect R^3",
            "encoding": "(U_gh, b_gh) with b_gh=U_gh theta_gh",
            "product": "(U,b)(V,c)=(UV,b+U c)",
            "reverse": "G_hg=G_gh^(-1)=(U_gh^T,-theta_gh)",
            "face_holonomy": "(H_p,t_p); base-frame closure tau_p=H_p^T t_p",
            "max_rotation_difference_from_previous_face_holonomy": max(rot_compare),
            "max_closure_difference_from_previous_developed_torsion": max(trans_compare),
            "mean_face_closure_norm": float(np.mean(torsion_norms)),
            "max_face_closure_norm": float(np.max(torsion_norms)),
            "mean_curvature_angle_rad": float(np.mean(curvature_angles)),
        },
        "cubical_bianchi": {
            "construction": "six adjacent-swap plaquette loops in the permutohedron of three coordinate directions, parallel-transported to the cube base",
            "max_rotation_residual": max(br),
            "max_translation_residual": max(bt),
            "cubes_with_rotation_residual_over_1e-10": int(np.count_nonzero(np.asarray(br) > 1e-10)),
            "cubes_with_translation_residual_over_1e-10": int(np.count_nonzero(np.asarray(bt) > 1e-10)),
        },
        "full_SE3_gauge_covariance": gauge,
        "epistemic_limits": [
            "The affine face translation is a discrete dislocation/closure observable; identifying it with a continuum Cartan torsion 2-form requires a refinement and consistency theorem.",
            "The exact cube identity is a lattice groupoid/Bianchi consistency identity for links, not a continuum field equation.",
            "The SO(3) connection and coframe remain the current finite spatial RGS prescriptions; no action selects them.",
            "No Lorentzian Spin(1,3) lift, physical time leg, TEGR equivalence, or polariton/Q-ball identification is established."
        ]
    }


def main():
    report = build_report()
    print(json.dumps(report, indent=2))
    b = report["cubical_bianchi"]
    g = report["full_SE3_gauge_covariance"]
    if max(b["max_rotation_residual"], b["max_translation_residual"]) > 1e-10:
        raise SystemExit("SE(3) cubical Bianchi identity failed")
    if max(v for k, v in g.items() if k != "seed") > 1e-10:
        raise SystemExit("full SE(3) gauge covariance failed")
    a = report["affine_link"]
    if max(a["max_rotation_difference_from_previous_face_holonomy"],
           a["max_closure_difference_from_previous_developed_torsion"]) > 1e-10:
        raise SystemExit("affine face holonomy disagrees with prior discrete Cartan observables")


if __name__ == "__main__":
    main()
