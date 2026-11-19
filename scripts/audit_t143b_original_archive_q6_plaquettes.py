#!/usr/bin/env python3
"""Audit the original PSU fibre archive against the Q6 Anti-Twin p(g)=g xor 7.

This script checks the archived normal/link formulae, all 192 archived
links, all 240 coordinate-square holonomies generated from Q6 bit labels,
the 32-vertex quotient graph, and (when present) K_fibre commutation with
P tensor I_2. It does not infer generator provenance from numerical fit.
"""
import argparse
import json
from pathlib import Path

import numpy as np

N = 64
P = np.arange(N, dtype=int) ^ 7
I2 = np.eye(2, dtype=complex)
I3 = np.eye(3, dtype=float)
SIGMA = (
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[1, 0], [0, -1]], dtype=complex),
)


def fro(a):
    return float(np.linalg.norm(a, ord="fro"))


def skew(v):
    x, y, z = v
    return np.array([[0, -z, y], [z, 0, -x], [-y, x, 0]], dtype=float)


def canonical_links(normals, edges):
    r_links, u_links = [], []
    min_denominator = float("inf")
    for g, h, _direction in edges:
        ng, nh = normals[int(g)], normals[int(h)]
        c = float(np.dot(ng, nh))
        if c <= -1.0:
            raise ValueError(f"antipodal edge normals at {(int(g), int(h))}")
        v = np.cross(ng, nh)
        w = skew(v)
        r_links.append(I3 + w + (w @ w) / (1.0 + c))
        v_sigma = sum(v[j] * SIGMA[j] for j in range(3))
        u_links.append(
            np.sqrt((1.0 + c) / 2.0) * I2
            - 1j / np.sqrt(2.0 * (1.0 + c)) * v_sigma
        )
        min_denominator = min(min_denominator, 1.0 + c)
    return np.asarray(r_links), np.asarray(u_links), min_denominator


def build_edge_lookup(edges):
    lookup = {}
    for k, (g, h, _d) in enumerate(edges):
        key = (int(g), int(h))
        if key in lookup or (key[1], key[0]) in lookup:
            raise ValueError(f"duplicate undirected edge {key}")
        lookup[key] = k
    return lookup


def directed_link(a, b, links, lookup, spin=False):
    if (a, b) in lookup:
        return links[lookup[(a, b)]]
    if (b, a) in lookup:
        m = links[lookup[(b, a)]]
        return m.conj().T if spin else m.T
    raise ValueError(f"missing Q6 edge {(a, b)}")


def q6_coordinate_squares(edges):
    """Generate each of the C(6,2)*2^4=240 coordinate faces once."""
    lookup = build_edge_lookup(edges)
    squares = []
    for i in range(6):
        for j in range(i + 1, 6):
            for g in range(N):
                if ((g >> i) & 1) or ((g >> j) & 1):
                    continue
                gi = g ^ (1 << i)
                gij = gi ^ (1 << j)
                gj = g ^ (1 << j)
                cyc = (g, gi, gij, gj)
                for a, b in zip(cyc, cyc[1:] + cyc[:1]):
                    if (a, b) not in lookup and (b, a) not in lookup:
                        raise ValueError(f"Q6 coordinate square has missing edge {(a, b)}")
                squares.append(cyc)
    if len(squares) != 240 or len(set(tuple(sorted(s)) for s in squares)) != 240:
        raise ValueError("Q6 square enumeration did not produce 240 distinct faces")
    return np.asarray(squares, dtype=int), lookup


def ordered_holonomy(cycle, links, lookup, spin=False):
    mats = [
        directed_link(int(a), int(b), links, lookup, spin=spin)
        for a, b in zip(cycle, np.roll(cycle, -1))
    ]
    # Column-vector convention: the last edge acts last on the state.
    out = mats[-1]
    for m in reversed(mats[:-1]):
        out = out @ m
    return out


def audit(fibre_path, embedding_path):
    with np.load(fibre_path) as fz, np.load(embedding_path) as ez:
        edges = np.asarray(fz["edges"], dtype=int)
        normals = np.asarray(fz["normals"], dtype=float)
        r_stored = np.asarray(fz["R_SO3"], dtype=float)
        u_stored = np.asarray(fz["U_SU2"], dtype=complex)
        x = np.asarray(ez["X_Oh_reconstructed"], dtype=float)
        states = np.asarray(ez["Q6_states"], dtype=int)
        k_fibre = np.asarray(fz["K_fibre"], dtype=complex) if "K_fibre" in fz.files else None
        d_fibre = np.asarray(fz["D_fibre"], dtype=complex) if "D_fibre" in fz.files else None

    if edges.shape != (192, 3) or normals.shape != (64, 3):
        raise ValueError("unexpected Q6 archive shapes")
    if r_stored.shape != (192, 3, 3) or u_stored.shape != (192, 2, 2):
        raise ValueError("unexpected archived link matrix shapes")
    if x.shape != (64, 3) or states.shape != (64, 6):
        raise ValueError("unexpected embedding/Q6 state shapes")

    # Confirm that the integer vertex labels really are the Q6 bit labels.
    expected_states = np.array([[(g >> (5-j)) & 1 for j in range(6)] for g in range(64)])
    if not np.array_equal(states, expected_states):
        raise ValueError("Q6_states do not match the binary vertex-label convention")
    for g, h, d in edges:
        if int(h) != (int(g) ^ (1 << int(d))):
            raise ValueError(f"edge direction metadata inconsistent at {(int(g), int(h), int(d))}")

    x_norm = x / np.linalg.norm(x, axis=1)[:, None]
    x_normal_res = np.linalg.norm(normals - x_norm, axis=1)
    anti_res = np.linalg.norm(normals[P] + normals, axis=1)

    r_formula, u_formula, min_denominator = canonical_links(normals, edges)
    r_formula_res = np.linalg.norm(r_stored - r_formula, axis=(1, 2))
    u_formula_res = np.linalg.norm(u_stored - u_formula, axis=(1, 2))

    lookup = build_edge_lookup(edges)
    link_r, link_udirect, link_uproj, signs, reversed_count = [], [], [], [], 0
    for k, (g0, h0, _d) in enumerate(edges):
        g, h = int(g0), int(h0)
        pg, ph = int(P[g]), int(P[h])
        if (pg, ph) in lookup:
            kp, rev = lookup[(pg, ph)], False
        elif (ph, pg) in lookup:
            kp, rev = lookup[(ph, pg)], True
        else:
            raise ValueError(f"antipodal edge image missing for {(g, h)}")
        reversed_count += int(rev)
        rp = r_stored[kp].T if rev else r_stored[kp]
        up = u_stored[kp].conj().T if rev else u_stored[kp]
        link_r.append(fro(rp-r_stored[k]))
        direct = fro(up-u_stored[k])
        opposite = fro(up+u_stored[k])
        link_udirect.append(direct)
        link_uproj.append(min(direct, opposite))
        signs.append(1 if direct <= opposite else -1)

    squares, lookup = q6_coordinate_squares(edges)
    square_r, square_udirect, square_uproj = [], [], []
    for cyc in squares:
        image = cyc ^ 7
        hr = ordered_holonomy(cyc, r_stored, lookup, spin=False)
        hpr = ordered_holonomy(image, r_stored, lookup, spin=False)
        hu = ordered_holonomy(cyc, u_stored, lookup, spin=True)
        hpu = ordered_holonomy(image, u_stored, lookup, spin=True)
        square_r.append(fro(hpr-hr))
        du, dm = fro(hpu-hu), fro(hpu+hu)
        square_udirect.append(du)
        square_uproj.append(min(du, dm))

    # Quotient graph: one vertex per p-orbit and one edge per edge orbit.
    representatives = np.minimum(np.arange(64), P)
    quotient_edges = set()
    quotient_degree = {int(r): 0 for r in np.unique(representatives)}
    for g, h, _d in edges:
        a, b = int(representatives[g]), int(representatives[h])
        if a == b:
            raise ValueError("quotient graph unexpectedly has a loop")
        quotient_edges.add(tuple(sorted((a, b))))
    for a, b in quotient_edges:
        quotient_degree[a] += 1
        quotient_degree[b] += 1

    report = {
        "status": "ORIGINAL_ARCHIVE_FORMULA_AND_Q6_PLAQUETTE_AUDIT",
        "source": {
            "fibre_archive": str(fibre_path),
            "embedding_archive": str(embedding_path),
            "edges_shape": list(edges.shape),
            "normals_shape": list(normals.shape),
            "R_SO3_shape": list(r_stored.shape),
            "U_SU2_shape": list(u_stored.shape),
        },
        "anti_twin": {
            "map": "p(g)=g xor 7",
            "normal_antipodal_max_residual": float(anti_res.max()),
            "normal_X_normalization_max_residual": float(x_normal_res.max()),
        },
        "canonical_link_formula_fit": {
            "SO3_direct_max_frobenius_residual": float(r_formula_res.max()),
            "SO3_direct_rms_frobenius_residual": float(np.sqrt(np.mean(r_formula_res**2))),
            "SU2_direct_max_frobenius_residual": float(u_formula_res.max()),
            "SU2_direct_rms_frobenius_residual": float(np.sqrt(np.mean(u_formula_res**2))),
            "minimum_1_plus_dot": float(min_denominator),
        },
        "archived_link_antipodal_replay": {
            "count": len(link_r),
            "orientation_reversed_count": reversed_count,
            "SO3_max_frobenius_residual": float(max(link_r)),
            "SU2_direct_max_frobenius_residual": float(max(link_udirect)),
            "SU2_projective_max_frobenius_residual": float(max(link_uproj)),
            "SU2_direct_plus_sign_count": int(np.sum(np.asarray(signs) == 1)),
            "SU2_direct_minus_sign_count": int(np.sum(np.asarray(signs) == -1)),
        },
        "Q6_plaquettes": {
            "construction": "all coordinate squares; choose 2 of 6 bit directions and fix the other 4 bits",
            "ordered_cycle_count": int(len(squares)),
            "SO3_holonomy_max_residual": float(max(square_r)),
            "SU2_holonomy_direct_max_residual": float(max(square_udirect)),
            "SU2_holonomy_projective_max_residual": float(max(square_uproj)),
            "product_convention": "column vectors; H=U_last ... U_first",
        },
        "anti_twin_quotient_graph": {
            "vertex_orbits": int(len(np.unique(representatives))),
            "edge_orbits": int(len(quotient_edges)),
            "degree_min": int(min(quotient_degree.values())),
            "degree_max": int(max(quotient_degree.values())),
        },
    }

    if k_fibre is not None:
        if k_fibre.shape != (128, 128):
            raise ValueError("K_fibre does not have expected 128x128 shape")
        p_fibre = np.zeros((128, 128), dtype=complex)
        for g in range(64):
            for s in range(2):
                p_fibre[2*(g ^ 7)+s, 2*g+s] = 1.0
        comm = k_fibre @ p_fibre - p_fibre @ k_fibre
        kdata = {
            "action": "P_fibre e_(g,s)=e_(g xor 7,s), interleaved vertex-spin indexing",
            "commutator_frobenius": fro(comm),
            "commutator_relative_frobenius": fro(comm) / max(fro(k_fibre), 1e-300),
            "hermiticity_residual": fro(k_fibre-k_fibre.conj().T),
        }
        if d_fibre is not None:
            kdata["DdagD_vs_K_fibre_residual"] = fro(d_fibre.conj().T @ d_fibre-k_fibre)
        # Orthonormal bases for the +/- eigenspaces of the deck involution.
        plus, minus = [], []
        for g in range(64):
            h = int(P[g])
            if g < h:
                for s in range(2):
                    vp = np.zeros(128); vm = np.zeros(128)
                    vp[2*g+s] = vp[2*h+s] = 1/np.sqrt(2)
                    vm[2*g+s] = 1/np.sqrt(2); vm[2*h+s] = -1/np.sqrt(2)
                    plus.append(vp); minus.append(vm)
        bp, bm = np.asarray(plus).T, np.asarray(minus).T
        kp, km = bp.conj().T @ k_fibre @ bp, bm.conj().T @ k_fibre @ bm
        ep, em = np.linalg.eigvalsh(kp), np.linalg.eigvalsh(km)
        kdata.update({
            "parity_sector_dimensions": {"plus": int(bp.shape[1]), "minus": int(bm.shape[1])},
            "off_diagonal_sector_block_frobenius": fro(bp.conj().T @ k_fibre @ bm),
            "plus_minus_sorted_spectrum_max_difference": float(np.max(np.abs(np.sort(ep)-np.sort(em)))),
            "plus_sector_eigenvalue_range": [float(ep.min()), float(ep.max())],
            "minus_sector_eigenvalue_range": [float(em.min()), float(em.max())],
        })
        report["K_fibre_operator_level_check"] = kdata

    # All checks use tolerances because archive entries are floating point.
    tol = 1e-10
    checks = {
        "normal_antipodal": report["anti_twin"]["normal_antipodal_max_residual"] < tol,
        "normal_matches_embedding": report["anti_twin"]["normal_X_normalization_max_residual"] < tol,
        "SO3_formula_fit": report["canonical_link_formula_fit"]["SO3_direct_max_frobenius_residual"] < tol,
        "SU2_formula_fit": report["canonical_link_formula_fit"]["SU2_direct_max_frobenius_residual"] < tol,
        "SO3_link_antipodal": report["archived_link_antipodal_replay"]["SO3_max_frobenius_residual"] < tol,
        "SU2_link_antipodal_direct": report["archived_link_antipodal_replay"]["SU2_direct_max_frobenius_residual"] < tol,
        "SO3_all_240_plaquettes": report["Q6_plaquettes"]["SO3_holonomy_max_residual"] < tol,
        "SU2_all_240_plaquettes_direct": report["Q6_plaquettes"]["SU2_holonomy_direct_max_residual"] < tol,
        "quotient_graph_32_vertices_96_edges_6_regular": (
            report["anti_twin_quotient_graph"]["vertex_orbits"] == 32
            and report["anti_twin_quotient_graph"]["edge_orbits"] == 96
            and report["anti_twin_quotient_graph"]["degree_min"] == 6
            and report["anti_twin_quotient_graph"]["degree_max"] == 6
        ),
    }
    if "K_fibre_operator_level_check" in report:
        checks["K_fibre_commutes_with_P_tensor_I2"] = (
            report["K_fibre_operator_level_check"]["commutator_relative_frobenius"] < tol
        )
        checks["K_fibre_parity_blocks_decouple"] = (
            report["K_fibre_operator_level_check"]["off_diagonal_sector_block_frobenius"] < tol
        )
    report["checks"] = checks
    report["checks_pass"] = bool(all(checks.values()))
    report["tolerance"] = tol
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fibre", required=True)
    ap.add_argument("--embedding", required=True)
    ap.add_argument("--out", default="T143B_original_archive_q6_plaquette_audit.json")
    args = ap.parse_args()
    report = audit(args.fibre, args.embedding)
    Path(args.out).write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["checks_pass"] else 1)


if __name__ == "__main__":
    main()
