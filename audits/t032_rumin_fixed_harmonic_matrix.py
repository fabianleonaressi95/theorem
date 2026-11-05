#!/usr/bin/env python3
"""T032 exact audit of the fixed 1x2 generic Rumin middle block.

Requires SymPy. This script is supplied for reproducibility; no execution
claim is made unless a separate run record is added.
"""
import argparse
import json
import sympy as sp


def audit_block(p: int, q: int):
    if p < 1 or q < 1:
        raise ValueError("generic Case V requires p,q >= 1")

    A2 = sp.Rational(p * (q + 1), 2)
    B2 = sp.Rational(q * (p + 1), 2)
    A, B = sp.sqrt(A2), sp.sqrt(B2)
    L = 2 * p * q + p + q
    S = sp.simplify(A2 + B2)
    C = sp.Rational(p - q, 2)
    Aprime = sp.simplify(C - 2 * A2)
    Bprime = sp.simplify(C + 2 * B2)

    assert S == sp.Rational(L, 2)
    assert Aprime == -sp.Rational(L, 2)
    assert Bprime == sp.Rational(L, 2)

    # Fixed source basis (e1,e2), fixed real target unit vector f.
    D = sp.Matrix([[Aprime * B / sp.sqrt(S),
                    Bprime * A / sp.sqrt(S)]])
    G = sp.simplify(D.H * D)
    G_expected = sp.Rational(L, 2) * sp.Matrix([
        [B2, -A * B],
        [-A * B, A2],
    ])
    assert sp.simplify(G - G_expected) == sp.zeros(2)

    # Exact rank, trace, determinant and nonzero singular value.
    assert sp.simplify(G.det()) == 0
    assert sp.simplify(sp.trace(G) - sp.Rational(L * L, 4)) == 0
    assert sp.simplify(G * G - sp.Rational(L * L, 4) * G) == sp.zeros(2)
    assert sp.simplify(D * sp.Matrix([A, B])) == sp.zeros(1, 1)

    # Target phase is a U(1) basis change and leaves D*D invariant.
    theta = sp.symbols("theta", real=True)
    Dtheta = sp.exp(sp.I * theta) * D
    assert sp.simplify(Dtheta.H * Dtheta - G) == sp.zeros(2)

    return {
        "p": p, "q": q, "L": L,
        "A2": str(A2), "B2": str(B2), "S": str(S),
        "Aprime": str(Aprime), "Bprime": str(Bprime),
        "D_row": [[str(sp.simplify(D[0, 0])),
                   str(sp.simplify(D[0, 1]))]],
        "gram": [[str(sp.simplify(G[i, j])) for j in range(2)]
                 for i in range(2)],
        "rank": 1,
        "singular_values": ["0", str(sp.Rational(L, 2))],
        "all_exact_checks_passed": True,
    }


def run(max_p: int, max_q: int):
    rows = [audit_block(p, q)
            for p in range(1, max_p + 1)
            for q in range(1, max_q + 1)]
    return {
        "audit": "T032 fixed harmonic-basis Rumin matrix",
        "range": {"p": [1, max_p], "q": [1, max_q]},
        "blocks_checked": len(rows),
        "all_exact_checks_passed": all(
            row["all_exact_checks_passed"] for row in rows
        ),
        "results": rows,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=20)
    parser.add_argument("--max-q", type=int, default=20)
    parser.add_argument("--output", default="t032_audit.json")
    args = parser.parse_args()
    result = run(args.max_p, args.max_q)
    with open(args.output, "w", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2)
    print(json.dumps({k: v for k, v in result.items() if k != "results"},
                     indent=2))


if __name__ == "__main__":
    main()
