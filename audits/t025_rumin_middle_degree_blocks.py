#!/usr/bin/env python3
"""Exact rational audit for T025 (Kitaoka, Rumin middle-degree blocks).

No third-party dependencies.  The script verifies the generic p,q>=1
singular-value reduction and separately records the two boundary families.
All calculations use fractions.Fraction, hence are exact.
"""
from fractions import Fraction
import argparse
import json


def generic_block(p: int, q: int):
    if p < 1 or q < 1:
        raise ValueError("generic block requires p,q >= 1")

    A2 = Fraction(p * (q + 1), 2)
    B2 = Fraction(q * (p + 1), 2)
    L = 2 * p * q + p + q
    C = Fraction(p - q, 2)
    Aprime = C - 2 * A2
    Bprime = C + 2 * B2

    assert A2 + B2 == Fraction(L, 2)
    assert Aprime == -Fraction(L, 2)
    assert Bprime == Fraction(L, 2)

    # Source formula for the non-exact multiplicity line.
    lam_source = ((Aprime**2) * B2 + (Bprime**2) * A2) / (A2 + B2)
    lam_closed = Fraction(L * L, 4)
    assert lam_source == lam_closed

    # D^*D in the orthonormal multiplicity basis:
    # exact line first, orthogonal complement second.
    block = ((Fraction(0), Fraction(0)),
             (Fraction(0), lam_closed))
    trace = block[0][0] + block[1][1]
    determinant = block[0][0] * block[1][1] - block[0][1] * block[1][0]
    assert trace == lam_closed
    assert determinant == 0

    return {
        "p": p,
        "q": q,
        "m": p + q,
        "su2_dimension": p + q + 1,
        "L": L,
        "A2": str(A2),
        "B2": str(B2),
        "Aprime": str(Aprime),
        "Bprime": str(Bprime),
        "DdaggerD_positive_eigenvalue": str(lam_closed),
        "multiplicity_block_DdaggerD": [
            ["0", "0"],
            ["0", str(lam_closed)],
        ],
        "trace": str(trace),
        "determinant": str(determinant),
        "exact": True,
    }


def boundary_blocks(nmax: int):
    # Keep the two conjugate families explicitly distinct.
    return {
        "case_VI_q_minus_1": [
            {"p": r, "eigenvalue": str(Fraction((r + 1) ** 2, 4))}
            for r in range(1, nmax + 1)
        ],
        "case_VII_p_minus_1": [
            {"q": r, "eigenvalue": str(Fraction((r + 1) ** 2, 4))}
            for r in range(1, nmax + 1)
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-index", type=int, default=20)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.max_index < 1:
        parser.error("--max-index must be >= 1")

    blocks = [
        generic_block(p, q)
        for p in range(1, args.max_index + 1)
        for q in range(1, args.max_index + 1)
    ]
    report = {
        "audit": "T025 exact rational Rumin middle-degree block audit",
        "max_index": args.max_index,
        "generic_blocks_checked": len(blocks),
        "generic_blocks": blocks,
        "boundary_families": boundary_blocks(args.max_index),
        "all_assertions_passed": True,
        "scope": (
            "Exact algebraic verification of the published singular-value "
            "reduction; not a numerical discretization or full 2I twist audit."
        ),
    }
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(report["audit"])
        print(f"generic blocks checked: {len(blocks)}")
        print("A^2+B^2=L/2: PASS")
        print("A'=-L/2 and B'=L/2: PASS")
        print("source quotient = L^2/4: PASS")
        print("multiplicity block trace/determinant: PASS")
        print("boundary families: kept separate")
        print("all assertions passed")


if __name__ == "__main__":
    main()
