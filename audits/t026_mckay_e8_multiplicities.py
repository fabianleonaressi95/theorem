#!/usr/bin/env python3
"""Exact McKay-E8 multiplicity audit for Sym^m(C^2)|_{2I}.

No third-party dependencies.  The recurrence is integer arithmetic only.
Node order:
  0: 1, 1: 2_s, 2: 3, 3: 4_s, 4: 5,
  5: 6_s, 6: 4, 7: 2'_s, 8: 3'.
"""
import argparse
import json


DIMS = (1, 2, 3, 4, 5, 6, 4, 2, 3)
NAMES = ("1", "2_s", "3", "4_s", "5", "6_s", "4", "2'_s", "3'")
EDGES = ((0, 1), (1, 2), (2, 3), (3, 4),
         (4, 5), (5, 6), (6, 7), (5, 8))
SPINORIAL = {1, 3, 5, 7}


def adjacency():
    a = [[0] * 9 for _ in range(9)]
    for i, j in EDGES:
        a[i][j] += 1
        a[j][i] += 1
    return a


def matvec(a, v):
    return [sum(a[i][j] * v[j] for j in range(9)) for i in range(9)]


def recurrence(max_degree):
    a = adjacency()
    v0 = [1] + [0] * 8
    if max_degree == 0:
        return [v0]
    v1 = [0, 1] + [0] * 7
    out = [v0, v1]
    for m in range(1, max_degree):
        av = matvec(a, out[-1])
        nxt = [av[i] - out[-2][i] for i in range(9)]
        out.append(nxt)
    return out


def invariant_hilbert_coefficients(max_degree):
    """Coefficients of (1+t^30)/((1-t^12)(1-t^20))."""
    coeff = [0] * (max_degree + 1)
    for a in range(max_degree // 12 + 1):
        for b in range(max_degree // 20 + 1):
            k = 12 * a + 20 * b
            if k <= max_degree:
                coeff[k] += 1
            if k + 30 <= max_degree:
                coeff[k + 30] += 1
    return coeff


def audit(max_degree):
    a = adjacency()
    assert sum(d * d for d in DIMS) == 120
    assert sum(DIMS) == 30
    assert matvec(a, list(DIMS)) == [2 * d for d in DIMS]

    vectors = recurrence(max_degree)
    hilbert = invariant_hilbert_coefficients(max_degree)
    rows = []
    for m, v in enumerate(vectors):
        assert all(isinstance(x, int) and x >= 0 for x in v), (m, v)
        assert sum(DIMS[i] * v[i] for i in range(9)) == m + 1, (m, v)
        if m % 2 == 0:
            assert all(v[i] == 0 for i in SPINORIAL), (m, v)
        else:
            assert all(v[i] == 0 for i in set(range(9)) - SPINORIAL), (m, v)
        assert v[0] == hilbert[m], (m, v[0], hilbert[m])
        rows.append({
            "degree": m,
            "multiplicities": {NAMES[i]: v[i] for i in range(9) if v[i]},
            "dimension_check": sum(DIMS[i] * v[i] for i in range(9)),
            "trivial_multiplicity": v[0],
            "exact": True,
        })

    expected = {
        0: {"1": 1},
        1: {"2_s": 1},
        2: {"3": 1},
        3: {"4_s": 1},
        4: {"5": 1},
        5: {"6_s": 1},
        6: {"4": 1, "3'": 1},
        7: {"6_s": 1, "2'_s": 1},
        8: {"5": 1, "4": 1},
        9: {"4_s": 1, "6_s": 1},
        10: {"3": 1, "5": 1, "3'": 1},
        11: {"2_s": 1, "4_s": 1, "6_s": 1},
        12: {"1": 1, "3": 1, "5": 1, "4": 1},
    }
    for m, want in expected.items():
        got = {NAMES[i]: vectors[m][i] for i in range(9) if vectors[m][i]}
        assert got == want, (m, got, want)

    return {
        "audit": "T026 exact affine-E8 McKay multiplicity recurrence",
        "max_degree": max_degree,
        "irreps": [{"name": NAMES[i], "dimension": DIMS[i]} for i in range(9)],
        "edges": [list(e) for e in EDGES],
        "dimension_vector_identity": "A*d = 2*d",
        "recurrence": "n(0)=e_1; n(1)=e_2s; n(m+1)=A*n(m)-n(m-1)",
        "degrees_checked": len(rows),
        "hilbert_series": "(1+t^30)/((1-t^12)(1-t^20))",
        "all_assertions_passed": True,
        "rows": rows,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-degree", type=int, default=120)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.max_degree < 0:
        parser.error("--max-degree must be >= 0")
    report = audit(args.max_degree)
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(report["audit"])
        print(f"degrees checked: {report['degrees_checked']}")
        print("Ad=2d: PASS")
        print("weighted dimension = m+1: PASS")
        print("central parity support: PASS")
        print("trivial Hilbert-series cross-check: PASS")
        print("selected decompositions m=0..12: PASS")
        print("all assertions passed")


if __name__ == "__main__":
    main()
