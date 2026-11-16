"""Independent exact character-average audit for the scalar spectrum of S^3/2I.

The class data are imported from the exact 600-cell quaternion audit.  The
character average is evaluated by the SU(2) symmetric-power recurrence and
compared degree-by-degree with the coefficient count in the binary Molien
series.  All arithmetic is exact in Q(sqrt(5)).
"""
from __future__ import annotations
import json
from pathlib import Path
import argparse
import sympy as sp
from audits.t035_exact_binary_icosahedral_model import (
    CLASS_SCALARS, CLASS_SIZES, expr,
)

PHI = (1 + sp.sqrt(5)) / 2
CHI_FUND = tuple(sp.simplify(2 * expr(x)) for x in CLASS_SCALARS)


def binary_molien_coefficient(k: int) -> int:
    """[t^k](1+t^30)/((1-t^12)(1-t^20)), by exact integer counting."""
    if k < 0:
        raise ValueError("degree must be nonnegative")
    total = 0
    for epsilon in (0, 1):
        residual = k - 30 * epsilon
        if residual < 0:
            continue
        for b in range(residual // 20 + 1):
            rem = residual - 20 * b
            if rem % 12 == 0:
                total += 1
    return total


def symmetric_power_character_rows(max_degree: int):
    if max_degree < 0:
        raise ValueError("max_degree must be nonnegative")
    rows = [[sp.Integer(1)] * 9]
    if max_degree == 0:
        return rows
    rows.append(list(CHI_FUND))
    for k in range(2, max_degree + 1):
        rows.append([
            sp.simplify(CHI_FUND[j] * rows[k - 1][j] - rows[k - 2][j])
            for j in range(9)
        ])
    return rows


def audit(max_degree: int = 120) -> dict:
    rows = symmetric_power_character_rows(max_degree)
    checked = []
    for k, row in enumerate(rows):
        character_average = sp.simplify(
            sum(CLASS_SIZES[j] * row[j] for j in range(9)) / 120
        )
        molien = binary_molien_coefficient(k)
        if character_average != molien:
            raise AssertionError(
                f"degree {k}: character average {character_average} != Molien {molien}"
            )
        if character_average.is_Integer is not True:
            raise AssertionError(f"degree {k}: nonintegral invariant multiplicity")
        n_k = int(character_average)
        spectral_multiplicity = (k + 1) * n_k
        if k % 2 and (n_k or spectral_multiplicity):
            raise AssertionError(f"odd degree {k} must vanish by the central element")
        checked.append({
            "degree": k,
            "invariant_dimension": n_k,
            "laplace_eigenvalue": k * (k + 2),
            "spectral_multiplicity": spectral_multiplicity,
        })
    positive = [x for x in checked if x["degree"] > 0 and x["spectral_multiplicity"]]
    first = positive[0] if positive else None
    return {
        "passed": True,
        "group": "binary icosahedral group 2I",
        "group_order": 120,
        "field": "Q(sqrt(5))",
        "class_sizes": list(CLASS_SIZES),
        "degrees_checked": max_degree + 1,
        "character_average_vs_binary_molien": "exact equality at every degree",
        "odd_degree_vanishing": True,
        "first_positive_eigenpair": first,
        "degree_120": checked[120] if max_degree >= 120 else None,
        "nonzero_spectrum": positive,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-degree", type=int, default=120)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()
    report = audit(args.max_degree)
    payload = json.dumps(report, indent=2)
    if args.output:
        path = Path(args.output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(payload + "\n", encoding="utf-8")
    print(payload)


if __name__ == "__main__":
    main()
