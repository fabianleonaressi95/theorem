#!/usr/bin/env python3
"""Investigation: induced map (S2)* : H2(C) -> H2(D) for the C60 Stone-Wales
chain map, with integer coefficients.

Motivation: tests/test_c60_stone_wales.py::test_chain_map_preserves_
spherical_fundamental_class (PR fix/c60-sw-homology-evidence) reports
multiplier ~ 3e-16, i.e. S2 z_fund ~ 0. Three hypotheses were distinguished:

  H1 construction error  - make_chain_map is not actually a chain map;
  H2 gauge error         - per-column representatives mod H2(D) are chosen
                           incoherently, so the induced map is gauge-dependent;
  H3 topological         - the map is canonical and genuinely null on H2.

Method (all exact integer arithmetic, no floats in the homology step):
  1. rebuild boundary matrices B1, B2 for both cellulations;
  2. verify B1' S1 = B1 and B2' S2 = S1 B2 exactly (chain-map identity);
  3. compute primitive integer generators of ker B2, ker B2' via exact
     rational nullspace (sympy), verify 1-dimensionality and primitivity;
  4. c = S2 z ; check B2' c = 0 ; k = (c . z') / (z' . z') must be integral;
  5. gauge sweep: rebuild S2 columns adding arbitrary multiples of z'
     (the exact ambiguity of each column's preimage) and recompute k.

Outputs audits/c60_sw_h2_induced_map_<date>.json and prints a verdict.
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from audit_c60_mmff94s_relaxed_coulomb import c60_ideal  # noqa: E402
from audit_c60_stone_wales import (  # noqa: E402
    boundary, enumerate_switches, graph_from_bonds, incidence,
    make_chain_map, oriented_faces,
)
import networkx as nx  # noqa: E402


def int_nullspace_1d(B: np.ndarray):
    """Exact 1-D integer kernel of integer matrix B (columns = chains)."""
    M = sp.Matrix(B.tolist())
    ns = M.nullspace()
    if len(ns) != 1:
        return None, len(ns)
    v = ns[0]
    entries = [sp.Rational(x) for x in v]
    # scale to primitive integer vector
    from math import gcd
    from functools import reduce
    den = 1
    for x in entries:
        den = den * x.q // gcd(den, x.q)
    ints = [int(x * den) for x in entries]
    g = reduce(gcd, [abs(i) for i in ints if i])
    ints = [i // g for i in ints]
    return np.array(ints, dtype=np.int64), 1


def rebuild_s2_with_gauge(g, fg, h, fh, s1, ob2, nb2, zprime, gauge_vec):
    """Same construction as make_chain_map's S2 step, but column j gets
    x_j + gauge_vec[j] * zprime (the exact per-column ambiguity)."""
    n_old_f = len(fg)
    s2 = np.zeros((len(fh), n_old_f), dtype=np.int64)
    nb2f = nb2.astype(float)
    for j in range(n_old_f):
        target = (s1 @ ob2)[:, j].astype(float)
        x = np.linalg.lstsq(nb2f, target, rcond=None)[0]
        x = np.rint(x - x[0]).astype(np.int64)
        assert np.array_equal(nb2 @ x, target.astype(np.int64)), \
            f"column {j} does not fill boundary"
        s2[:, j] = x + int(gauge_vec[j]) * zprime
    return s2


def main() -> int:
    stamp = date.today().isoformat()
    xyz, bonds = c60_ideal()
    g = graph_from_bonds(len(xyz), bonds)
    f = oriented_faces(g)
    cand = enumerate_switches(g, f)[0]
    h, fh = cand["graph"], cand["faces"]

    oe, ob1, ob2 = boundary(g, f)
    ne, nb1, nb2 = boundary(h, fh)
    ni = {e: i for i, e in enumerate(ne)}

    # --- S1 (same construction as make_chain_map) ---
    s1 = np.zeros((len(ne), len(oe)), dtype=np.int64)
    for j, (u, v) in enumerate(oe):
        path = [u, v] if h.has_edge(u, v) else nx.shortest_path(h, u, v)
        for a, b in zip(path, path[1:]):
            s1[ni[tuple(sorted((a, b)))], j] += 1 if a < b else -1

    # --- canonical S2 via library function (for identity check) ---
    q = make_chain_map(g, f, h, fh)
    s2_lib = np.array(q["S2"], dtype=np.int64)

    report = {"date": stamp, "checks": {}}

    # 1. chain-map identities, exact integers
    report["checks"]["B1p_S1_eq_B1"] = bool(np.array_equal(nb1 @ s1, ob1))
    report["checks"]["B2p_S2_eq_S1B2_lib"] = bool(
        np.array_equal(nb2 @ s2_lib, s1 @ ob2))

    # 2. H2 generators (exact integer nullspaces)
    z, dim_z = int_nullspace_1d(ob2)
    zp, dim_zp = int_nullspace_1d(nb2)
    report["checks"]["dim_ker_B2"] = dim_z
    report["checks"]["dim_ker_B2p"] = dim_zp
    report["checks"]["z_primitive_gcd"] = int(
        np.gcd.reduce(np.abs(z))) if z is not None else None
    report["checks"]["zp_primitive_gcd"] = int(
        np.gcd.reduce(np.abs(zp))) if zp is not None else None
    report["checks"]["z_entries_set"] = sorted(set(z.tolist()))
    report["checks"]["zp_entries_set"] = sorted(set(zp.tolist()))

    # 3. induced map with library S2
    c = s2_lib @ z
    report["checks"]["S2z_is_cycle"] = bool(
        np.array_equal(nb2 @ c, np.zeros(nb2.shape[0], dtype=np.int64)))
    denom = int(zp @ zp)
    num = int(c @ zp)
    report["induced"] = {
        "S2z_max_abs": int(np.abs(c).max()),
        "numerator_c_dot_zp": num,
        "denominator_zp_sq": denom,
        "k_rational": f"{num}/{denom}",
        "k_integer": (num % denom == 0),
        "k": num // denom if num % denom == 0 else None,
    }

    # 4. gauge sweep: add multiples of zp to each S2 column
    rng = np.random.default_rng(20261127)
    ks = []
    for trial in range(200):
        gv = rng.integers(-3, 4, size=len(f))
        s2g = rebuild_s2_with_gauge(g, f, h, fh, s1, ob2, nb2, zp, gv)
        # chain-map identity must still hold exactly
        assert np.array_equal(nb2 @ s2g, s1 @ ob2)
        cg = s2g @ z
        assert np.array_equal(nb2 @ cg, np.zeros(len(nb2)))
        numg = int(cg @ zp)
        kg = numg // denom if numg % denom == 0 else numg / denom
        ks.append(kg)
    ks = np.array(ks, dtype=float)
    report["gauge_sweep"] = {
        "trials": len(ks),
        "k_min": float(ks.min()),
        "k_max": float(ks.max()),
        "k_values": sorted(set(ks.tolist())),
        "gauge_invariant": bool(ks.min() == ks.max()),
    }

    # verdict
    if not (report["checks"]["B1p_S1_eq_B1"] and
            report["checks"]["B2p_S2_eq_S1B2_lib"]):
        verdict = "H1_CONSTRUCTION_ERROR"
    elif report["gauge_sweep"]["gauge_invariant"]:
        verdict = "H3_TOPOLOGICAL_NULL_MAP" if report["induced"]["k"] == 0 \
            else f"H3_INDUCED_MAP_k={report['induced']['k']}"
    else:
        verdict = "H2_GAUGE_DEPENDENT"
    report["verdict"] = verdict

    out = ROOT / "audits" / f"c60_sw_h2_induced_map_{stamp}.json"
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    print("verdict:", verdict)
    return 0


if __name__ == "__main__":
    sys.exit(main())
