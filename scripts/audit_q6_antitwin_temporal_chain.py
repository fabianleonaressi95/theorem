"""Exact finite audit of the Q6 Anti-Twin Hodge time generator.

Uses oriented cubical incidence matrices and sparse rational arithmetic.
It verifies the chain-map identity for the Hodge generator and for the
two-sheet coupling. Exponentiation then preserves the chain map by its
power series; no numerical matrix exponential is needed.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product


Sparse = list[dict[int, Fraction]]  # matrix stored by columns


def cells(n: int, k: int) -> list[tuple[int, ...]]:
    out = []
    for free in combinations(range(n), k):
        free_set = set(free)
        fixed_axes = [i for i in range(n) if i not in free_set]
        for bits in product((0, 1), repeat=n - k):
            cell = [0] * n
            for i in free:
                cell[i] = -1
            for i, bit in zip(fixed_axes, bits):
                cell[i] = bit
            out.append(tuple(cell))
    return out


def boundary(n: int, k: int) -> tuple[list[tuple[int, ...]], list[tuple[int, ...]], Sparse]:
    source, target = cells(n, k), cells(n, k - 1)
    target_index = {cell: i for i, cell in enumerate(target)}
    columns: Sparse = []
    for cell in source:
        free_axes = [i for i, value in enumerate(cell) if value == -1]
        col: dict[int, Fraction] = {}
        for r, axis in enumerate(free_axes):
            sign = 1 if r % 2 == 0 else -1
            for side, coeff in ((0, -sign), (1, sign)):
                face = list(cell)
                face[axis] = side
                idx = target_index[tuple(face)]
                col[idx] = col.get(idx, Fraction(0)) + coeff
        columns.append({i: x for i, x in col.items() if x})
    return source, target, columns


def transpose(A: Sparse, nrows: int) -> Sparse:
    out: Sparse = [{} for _ in range(nrows)]
    for j, col in enumerate(A):
        for i, value in col.items():
            out[i][j] = value
    return out


def matmul(A: Sparse, B: Sparse) -> Sparse:
    """Compose A after B; both matrices are stored by columns."""
    out: Sparse = []
    for col_b in B:
        col: dict[int, Fraction] = {}
        for mid, b in col_b.items():
            for row, a in A[mid].items():
                col[row] = col.get(row, Fraction(0)) + a * b
        out.append({i: x for i, x in col.items() if x})
    return out


def add(A: Sparse, B: Sparse) -> Sparse:
    out: Sparse = []
    for a, b in zip(A, B):
        col = dict(a)
        for i, x in b.items():
            col[i] = col.get(i, Fraction(0)) + x
        out.append({i: x for i, x in col.items() if x})
    return out


def scale(A: Sparse, c: Fraction) -> Sparse:
    return [{i: c * x for i, x in col.items() if c * x} for col in A]


def identity(n: int) -> Sparse:
    return [{i: Fraction(1)} for i in range(n)]


def kron(A: Sparse, B: Sparse) -> Sparse:
    """Kronecker product, with the B index varying fastest."""
    nrows_b = len(B[0]) if False else None
    # Infer B row count from its column indices; caller supplies full-rank
    # identities or square matrices, so this is the maximum row index + 1.
    nrows_b = 1 + max((i for col in B for i in col), default=-1)
    out: Sparse = []
    for col_a in A:
        for col_b in B:
            col: dict[int, Fraction] = {}
            for ia, va in col_a.items():
                for ib, vb in col_b.items():
                    row = ia * nrows_b + ib
                    col[row] = va * vb
            out.append(col)
    return out


def equal(A: Sparse, B: Sparse) -> bool:
    return A == B


def hodge_laplacian(Bk: Sparse, Bkp1: Sparse, nk: int) -> Sparse:
    # Bk: C_k -> C_(k-1); Bkp1: C_(k+1) -> C_k.
    term_down = matmul(transpose(Bk, nk), Bk)
    term_up = matmul(Bkp1, transpose(Bkp1, len(Bkp1)))
    return add(term_down, term_up)


def build_report() -> dict:
    _, _, B1 = boundary(6, 1)
    _, _, B2 = boundary(6, 2)
    _, _, B3 = boundary(6, 3)

    n0, n1, n2 = 64, 192, 240
    L0 = matmul(B1, transpose(B1, n0))
    L1 = hodge_laplacian(B1, B2, n1)
    L2 = hodge_laplacian(B2, B3, n2)

    # The exact chain-Hodge identity is B_k L_k = L_(k-1) B_k.
    chain_hodge_1 = equal(matmul(B1, L1), matmul(L0, B1))
    chain_hodge_2 = equal(matmul(B2, L2), matmul(L1, B2))

    I2 = identity(2)
    S = [{1: Fraction(1)}, {0: Fraction(1)}]
    Q = add(identity(2), scale(S, Fraction(-1)))  # I-S
    B1_at = kron(B1, I2)
    B2_at = kron(B2, I2)
    L0_at = kron(L0, I2)
    L1_at = kron(L1, I2)
    L2_at = kron(L2, I2)

    # Sheet coupling is degree-independent: I_(C_k) tensor (I-S).
    Q0 = kron(identity(n0), Q)
    Q1 = kron(identity(n1), Q)
    Q2 = kron(identity(n2), Q)
    mu = Fraction(1, 3)  # rational regression value; identity holds for all mu.

    H0 = add(L0_at, scale(Q0, mu))
    H1 = add(L1_at, scale(Q1, mu))
    H2 = add(L2_at, scale(Q2, mu))

    doubled_chain_1 = equal(matmul(B1_at, H1), matmul(H0, B1_at))
    doubled_chain_2 = equal(matmul(B2_at, H2), matmul(H1, B2_at))

    S0 = kron(identity(n0), S)
    S1 = kron(identity(n1), S)
    S2 = kron(identity(n2), S)
    sheet_commutators_zero = (
        equal(matmul(H0, S0), matmul(S0, H0))
        and equal(matmul(H1, S1), matmul(S1, H1))
        and equal(matmul(H2, S2), matmul(S2, H2))
    )

    return {
        "cell_counts": {"C0": n0, "C1": n1, "C2": n2, "C3": 160},
        "oriented_incidence": {
            "B1B2_zero": all(not x for x in matmul(B1, B2)),
            "B2B3_zero": all(not x for x in matmul(B2, B3)),
        },
        "hodge_chain_intertwining": {
            "B1_L1_equals_L0_B1": chain_hodge_1,
            "B2_L2_equals_L1_B2": chain_hodge_2,
        },
        "antitwin_generator": {
            "mu_regression_value": str(mu),
            "doubled_B1_H1_equals_H0_B1": doubled_chain_1,
            "doubled_B2_H2_equals_H1_B2": doubled_chain_2,
            "commutes_with_sheet_swap": sheet_commutators_zero,
            "real_time_evolution": "U_k(t)=exp(-i t H_k), unitary for real mu",
            "heat_semigroup": "exp(-t H_k), contractive for mu >= 0",
            "analytic_consequence": "B_k H_k=H_(k-1) B_k implies B_k exp(-i t H_k)=exp(-i t H_(k-1)) B_k",
        },
        "arithmetic": "exact sparse Fraction arithmetic; no floating-point tolerance",
    }


def main() -> None:
    import json
    report = build_report()
    print(json.dumps(report, indent=2))
    if not all(report["oriented_incidence"].values()):
        raise SystemExit("cubical boundary identity failed")
    if not all(report["hodge_chain_intertwining"].values()):
        raise SystemExit("Hodge generator does not intertwine the boundary")
    if not all(report["antitwin_generator"][key] for key in (
        "doubled_B1_H1_equals_H0_B1",
        "doubled_B2_H2_equals_H1_B2",
        "commutes_with_sheet_swap",
    )):
        raise SystemExit("Anti-Twin temporal generator audit failed")


if __name__ == "__main__":
    main()
