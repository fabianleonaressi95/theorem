#!/usr/bin/env python3
"""T029 exact Gram-matrix audit for generic Rumin middle blocks on S^3/2I.

The matrix computed here is D^*D in the normalized two-copy multiplicity
basis of T025, NOT the geometric differential matrix D itself.  The latter
requires a fixed target harmonic basis and phase/connection coefficients not
determined by singular values alone.

Requires SymPy and the existing T027 McKay recurrence audit.
"""
import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
T027_PATH = ROOT / "audits/t027_mckay_molien_bridge.py"
NAMES = ("1", "2_s", "3", "4_s", "5", "6_s", "4", "2'_s", "3'")
DIMS = (1, 2, 3, 4, 5, 6, 4, 2, 3)
LABEL_MAP = {
    "1": "1", "2_s": "2", "3": "3", "4_s": "4'",
    "5": "5", "6_s": "6", "4": "4", "2'_s": "2'", "3'": "3'"
}


def load_t027():
    spec = importlib.util.spec_from_file_location("t027_mckay_audit", T027_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {T027_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def generic_gram_block(p, q, sp):
    """Return exact D^*D matrix in the normalized (1,0)/(0,1) basis."""
    if p < 1 or q < 1:
        raise ValueError("generic block requires p,q >= 1")
    a2 = sp.Rational(p * (q + 1), 2)
    b2 = sp.Rational(q * (p + 1), 2)
    L = 2 * p * q + p + q
    S = a2 + b2
    lam = sp.Rational(L * L, 4)
    cross = sp.sqrt(a2 * b2)

    # Exact line is span(sqrt(a2), sqrt(b2)); D annihilates it.
    # Positive line is its orthogonal complement.
    gram = sp.simplify((lam / S) * sp.Matrix([
        [b2, -cross],
        [-cross, a2],
    ]))
    kernel_vector = sp.Matrix([sp.sqrt(a2), sp.sqrt(b2)])
    positive_vector = sp.Matrix([sp.sqrt(b2), -sp.sqrt(a2)])

    assert sp.simplify(a2 + b2 - sp.Rational(L, 2)) == 0
    assert sp.simplify(gram * kernel_vector) == sp.zeros(2, 1)
    assert sp.simplify(gram * positive_vector - lam * positive_vector) == sp.zeros(2, 1)
    assert sp.simplify(gram * gram - lam * gram) == sp.zeros(2)
    assert sp.simplify(sp.trace(gram) - lam) == 0
    assert sp.simplify(gram.det()) == 0
    assert sp.simplify(gram - gram.T) == sp.zeros(2)

    return {
        "p": p, "q": q, "m": p + q, "L": L,
        "A_squared": str(a2), "B_squared": str(b2),
        "DdaggerD_matrix": [[str(sp.simplify(gram[i, j])) for j in range(2)] for i in range(2)],
        "eigenvalues": ["0", str(lam)],
        "kernel_vector": [str(x) for x in kernel_vector],
        "positive_vector": [str(x) for x in positive_vector],
        "trace": str(sp.trace(gram)),
        "determinant": str(gram.det()),
        "exact_matrix_identities": True,
    }


def audit(max_index=20):
    import sympy as sp
    if max_index < 1:
        raise ValueError("max_index must be >= 1")
    t027 = load_t027()
    max_m = 2 * max_index
    recurrence = t027.recurrence(max_m)
    checked = 0
    sector_counts = {LABEL_MAP[name]: {"kernel_dimension": 0, "positive_dimension": 0,
                                       "harmonic_blocks": 0} for name in NAMES}
    sample_blocks = []

    for p in range(1, max_index + 1):
        for q in range(1, max_index + 1):
            block = generic_gram_block(p, q, sp)
            m = p + q
            row = recurrence[m]
            assert sum(DIMS[i] * row[i] for i in range(9)) == m + 1
            for i, node in enumerate(NAMES):
                label = LABEL_MAP[node]
                copies = row[i]
                dim = DIMS[i] * copies
                sector_counts[label]["kernel_dimension"] += dim
                sector_counts[label]["positive_dimension"] += dim
                sector_counts[label]["harmonic_blocks"] += copies
            checked += 1
            if (p, q) in ((1, 1), (1, 2), (2, 1), (2, 2), (max_index, max_index)):
                block["2I_multiplicity_by_irrep"] = {
                    LABEL_MAP[NAMES[i]]: {
                        "copies": int(row[i]),
                        "dimension_per_line": int(DIMS[i] * row[i]),
                    } for i in range(9)
                }
                sample_blocks.append(block)

    assert sum(DIMS[i] * recurrence[2][i] for i in range(9)) == 3
    assert sum(v["kernel_dimension"] for v in sector_counts.values()) == checked * 0 + sum(
        p + q + 1 for p in range(1, max_index + 1) for q in range(1, max_index + 1)
    )
    assert all(v["kernel_dimension"] == v["positive_dimension"] for v in sector_counts.values())

    return {
        "audit": "T029 exact Rumin Gram matrices and 2I multiplicities",
        "max_index": max_index,
        "generic_harmonic_blocks_checked": checked,
        "McKay_recurrence_max_degree": max_m,
        "sector_dimensions": sector_counts,
        "sample_blocks": sample_blocks,
        "all_exact_matrix_assertions_passed": True,
        "all_McKay_dimension_identities_passed": True,
        "scope": [
            "The displayed 2x2 matrices are D^*D Gram matrices in the normalized two-copy multiplicity basis.",
            "They are not coefficient matrices of the geometric differential D.",
            "The left-unitary/target-basis freedom in D is not fixed by D^*D or by singular values.",
            "Kitaoka boundary families (q=-1 and p=-1) remain separate and are not inserted into the generic p,q>=1 matrix.",
            "Each irreducible 2I sector has d_rho*n_rho(m) dimensions on both the exact kernel line and the positive line."
        ]
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-index", type=int, default=20)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    report = audit(args.max_index)
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(report["audit"])
        print("generic harmonic blocks:", report["generic_harmonic_blocks_checked"])
        print("exact 2x2 Gram identities: PASS")
        print("McKay dimension identities: PASS")
        print("geometric D matrix: NOT CLAIMED")
        print("all assertions passed")


if __name__ == "__main__":
    main()
