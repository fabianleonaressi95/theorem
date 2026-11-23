"""Exact incidence audit for the standard cubical 6-cube through degree 3.

No numerical linear algebra is used. Cells are oriented by increasing free
coordinate directions; boundary matrices have integer entries.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from math import comb


def cells(n: int, k: int) -> list[tuple[int, ...]]:
    """Encode a cell by a length-n tuple: -1 means free, 0/1 fixed."""
    out = []
    for free in combinations(range(n), k):
        free_set = set(free)
        fixed_axes = [i for i in range(n) if i not in free_set]
        for bits in product((0, 1), repeat=n-k):
            cell = [0] * n
            for i in free:
                cell[i] = -1
            for i, bit in zip(fixed_axes, bits):
                cell[i] = bit
            out.append(tuple(cell))
    return out


def boundary_columns(n: int, k: int):
    """Return k-cells, (k-1)-cells, and sparse columns of partial_k."""
    source = cells(n, k)
    target = cells(n, k - 1)
    target_index = {cell: i for i, cell in enumerate(target)}
    columns: list[dict[int, int]] = []
    for cell in source:
        free_axes = [i for i, value in enumerate(cell) if value == -1]
        col: dict[int, int] = {}
        for r, axis in enumerate(free_axes):
            sign = 1 if r % 2 == 0 else -1
            for side, coefficient in ((0, -sign), (1, sign)):
                face = list(cell)
                face[axis] = side
                idx = target_index[tuple(face)]
                col[idx] = col.get(idx, 0) + coefficient
        columns.append({i: v for i, v in col.items() if v})
    return source, target, columns


def exact_rank(columns: list[dict[int, int]]) -> int:
    """Exact column rank by sparse Fraction Gaussian elimination."""
    basis: dict[int, dict[int, Fraction]] = {}
    for raw in columns:
        v = {i: Fraction(x) for i, x in raw.items() if x}
        while v:
            pivot = min(v)
            if pivot not in basis:
                scale = v[pivot]
                basis[pivot] = {i: x / scale for i, x in v.items()}
                break
            factor = v[pivot]
            for i, x in basis[pivot].items():
                new = v.get(i, Fraction(0)) - factor * x
                if new:
                    v[i] = new
                else:
                    v.pop(i, None)
    return len(basis)


def composition_is_zero(left_columns, right_columns) -> bool:
    """Check (partial_{k-1} partial_k)=0 column by column."""
    for col in right_columns:
        result: dict[int, int] = {}
        for mid, coefficient in col.items():
            for row, value in left_columns[mid].items():
                result[row] = result.get(row, 0) + coefficient * value
        if any(result.values()):
            return False
    return True


def build_report() -> dict:
    data = {k: boundary_columns(6, k) for k in (1, 2, 3)}
    counts = {k: len(data[k][0]) for k in (1, 2, 3)}
    ranks = {k: exact_rank(data[k][2]) for k in (1, 2, 3)}
    identities = {
        "B1_B2_zero": composition_is_zero(data[1][2], data[2][2]),
        "B2_B3_zero": composition_is_zero(data[2][2], data[3][2]),
    }
    closed_2_cochain_dimension = counts[2] - ranks[3]
    # Derive the exact spectrum from tensor-product multiplicities:
    # m_p(2(p+j)) = C(6,p) C(6-p,j). For each positive eigenvalue,
    # exact degree-2 multiplicity = m_1(lambda) - m_0(lambda).
    closed_spectrum = {}
    for level in range(1, 7):
        eigenvalue = 2 * level
        m0 = comb(6, level)
        m1 = 6 * comb(5, level - 1)
        multiplicity = m1 - m0
        if multiplicity:
            closed_spectrum[eigenvalue] = multiplicity
    if sum(closed_spectrum.values()) != closed_2_cochain_dimension:
        raise ArithmeticError("tensor-product spectrum does not fill ker(B3^T)")
    green_kubo_trace = sum(
        (Fraction(multiplicity, eigenvalue)
         for eigenvalue, multiplicity in closed_spectrum.items()),
        Fraction(0, 1),
    )
    isotropic_green_kubo_coefficient = green_kubo_trace / closed_2_cochain_dimension
    return {
        "n": 6,
        "cell_counts_C1_C2_C3": counts,
        "boundary_ranks_B1_B2_B3": ranks,
        "boundary_identities": identities,
        "closed_2_cochain_dimension": closed_2_cochain_dimension,
        "harmonic_2_cochain_dimension": counts[2] - ranks[2] - ranks[3],
        "closed_2_hodge_spectrum": closed_spectrum,
        "green_kubo_trace_sum_m_over_lambda": str(green_kubo_trace),
        "isotropic_green_kubo_coefficient": str(isotropic_green_kubo_coefficient),
        "projector": "P_cl = I_240 - B3 (B3^T B3)^+ B3^T",
        "inner_product": "standard Euclidean inner product in the oriented cell bases",
        "arithmetic": "exact integers and rational Gaussian elimination",
    }


def main() -> None:
    import json
    report = build_report()
    print(json.dumps(report, indent=2))
    if not all(report["boundary_identities"].values()):
        raise SystemExit("boundary identity failed")
    if report["boundary_ranks_B1_B2_B3"] != {1: 63, 2: 129, 3: 111}:
        raise SystemExit("unexpected exact boundary ranks")
    if report["closed_2_cochain_dimension"] != 129:
        raise SystemExit("unexpected closed 2-cochain dimension")
    if report["harmonic_2_cochain_dimension"] != 0:
        raise SystemExit("unexpected H^2 dimension")


if __name__ == "__main__":
    main()
