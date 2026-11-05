"""Exact reconstruction of the 2I character table from T021 Molien data.

All arithmetic is performed in Q(sqrt(5)) using SymPy. This constructs
characters, not explicit irreducible representation matrices.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sympy as sp

from src.t032_2i_molien import IRREP_DIMENSIONS, IRREP_NUMERATORS, molien_coefficients

PHI = (1 + sp.sqrt(5)) / 2
CLASS_SIZES = (1, 1, 20, 30, 12, 12, 20, 12, 12)
CLASS_ORDERS = (1, 2, 3, 4, 5, 5, 6, 10, 10)
FUNDAMENTAL = (
    sp.Integer(2), sp.Integer(-2), sp.Integer(-1), sp.Integer(0),
    PHI - 1, -PHI, sp.Integer(1), PHI, 1 - PHI,
)


def symmetric_power_characters(max_degree: int) -> list[list[sp.Expr]]:
    if max_degree < 0:
        raise ValueError("max_degree must be nonnegative")
    rows = [[sp.Integer(1)] * 9]
    if max_degree == 0:
        return rows
    rows.append(list(FUNDAMENTAL))
    for m in range(2, max_degree + 1):
        rows.append([
            sp.simplify(FUNDAMENTAL[j] * rows[m - 1][j] - rows[m - 2][j])
            for j in range(9)
        ])
    return rows


def independent_degree_rows(max_degree: int = 40) -> tuple[int, ...]:
    chars = symmetric_power_characters(max_degree)
    selected: list[int] = []
    matrix = sp.zeros(0, 9)
    rank = 0
    for m, chi in enumerate(chars):
        candidate = matrix.col_join(sp.Matrix([CLASS_SIZES[j] * chi[j] for j in range(9)]).T)
        new_rank = candidate.rank()
        if new_rank > rank:
            selected.append(m)
            matrix = candidate
            rank = new_rank
            if rank == 9:
                return tuple(selected)
    raise ArithmeticError("Symmetric-power character rows did not span class functions.")


def reconstruct_character_table() -> tuple[dict[str, tuple[sp.Expr, ...]], tuple[int, ...]]:
    degrees = independent_degree_rows()
    chars = symmetric_power_characters(max(degrees))
    A = sp.Matrix([
        [CLASS_SIZES[j] * chars[m][j] for j in range(9)]
        for m in degrees
    ])
    if A.det() == 0:
        raise ArithmeticError("Selected interpolation matrix is singular.")
    Ainv = A.inv()
    table: dict[str, tuple[sp.Expr, ...]] = {}
    for label in IRREP_NUMERATORS:
        rhs = sp.Matrix([
            120 * molien_coefficients(label, m)[m] for m in degrees
        ])
        values = [sp.simplify(x) for x in Ainv * rhs]
        table[label] = tuple(values)
    return table, degrees


def verify_character_table(table: dict[str, tuple[sp.Expr, ...]], max_degree: int = 240) -> dict:
    labels = tuple(IRREP_DIMENSIONS)
    if set(table) != set(labels):
        raise AssertionError("Character table labels do not match T021.")
    for label in labels:
        row = table[label]
        if len(row) != 9:
            raise AssertionError(f"Wrong number of classes in row {label}.")
        if sp.simplify(row[0] - IRREP_DIMENSIONS[label]) != 0:
            raise AssertionError(f"Identity value does not equal dimension for {label}.")
        central_ratio = sp.simplify(row[1] / IRREP_DIMENSIONS[label])
        if central_ratio not in (sp.Integer(1), sp.Integer(-1)):
            raise AssertionError(f"Central element does not act as +/- identity for {label}.")
    for a in labels:
        for b in labels:
            inner = sp.simplify(sum(
                CLASS_SIZES[j] * sp.conjugate(table[a][j]) * table[b][j]
                for j in range(9)
            ) / 120)
            expected = sp.Integer(1 if a == b else 0)
            if sp.simplify(inner - expected) != 0:
                raise AssertionError(f"Character orthogonality failed for {a}, {b}.")
    if tuple(table["2"]) != tuple(FUNDAMENTAL):
        raise AssertionError("The label '2' does not match the defining SU(2) character.")
    chars = symmetric_power_characters(max_degree)
    checked = 0
    for label in labels:
        for m in range(max_degree + 1):
            average = sp.simplify(sum(
                CLASS_SIZES[j] * sp.conjugate(table[label][j]) * chars[m][j]
                for j in range(9)
            ) / 120)
            expected = sp.Integer(molien_coefficients(label, m)[m])
            if sp.simplify(average - expected) != 0:
                raise AssertionError(f"Molien reconstruction failed: {label}, degree {m}.")
            checked += 1
    squares = sum(IRREP_DIMENSIONS[label] ** 2 for label in labels)
    if squares != 120 or sum(CLASS_SIZES) != 120:
        raise AssertionError("Group order / sum-of-squares identity failed.")
    return {
        "passed": True,
        "class_sizes": CLASS_SIZES,
        "class_orders": CLASS_ORDERS,
        "selected_degrees": None,
        "character_orthogonality_pairs": len(labels) ** 2,
        "molien_character_averages_checked": checked,
        "sum_irrep_dimension_squares": squares,
        "arithmetic_field": "Q(sqrt(5))",
    }


def exact_json(table: dict[str, tuple[sp.Expr, ...]], degrees: tuple[int, ...]) -> dict:
    return {
        "group": "binary_icosahedral_group_2I",
        "order": 120,
        "field": "Q(sqrt(5))",
        "class_sizes": list(CLASS_SIZES),
        "class_orders": list(CLASS_ORDERS),
        "selected_interpolation_degrees": list(degrees),
        "irreps": {
            label: {
                "dimension": IRREP_DIMENSIONS[label],
                "character_values": [sp.sstr(v) for v in table[label]],
            }
            for label in IRREP_DIMENSIONS
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="data/2i_character_table_exact.json")
    args = parser.parse_args()
    table, degrees = reconstruct_character_table()
    report = verify_character_table(table)
    report["selected_degrees"] = degrees
    payload = exact_json(table, degrees)
    payload["verification"] = report
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
