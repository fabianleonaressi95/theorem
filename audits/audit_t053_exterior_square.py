#!/usr/bin/env python3
"""Exact audit of the exterior-square matrix construction used in yess.pdf.

The source uses normalized standard icosahedron coordinates and a floating-point
nearest-edge threshold. Here the same vertex set is represented with exact
sqrt(5), and adjacency is selected by the exact minimum nonzero squared
distance before the common normalization. All subsequent matrix calculations
are exact SymPy rational/algebraic calculations.

This checks one specific source construction. It does not prove 2I* equivariance,
representation irreducibility, or any physical interpretation.
"""

from itertools import combinations
import sympy as sp


def main() -> None:
    phi = (1 + sp.sqrt(5)) / 2

    # Standard 12 vertices in the same generation order as the source code.
    vertices = []
    for a in (-1, 1):
        for b in (-phi, phi):
            vertices.extend(((0, a, b), (a, b, 0), (b, 0, a)))

    # Exact squared distances; normalization by one common positive factor
    # does not change which pairs are nearest neighbors.
    d2 = {}
    for i in range(12):
        for j in range(i + 1, 12):
            value = sp.simplify(
                sum((vertices[i][k] - vertices[j][k]) ** 2 for k in range(3))
            )
            d2[(i, j)] = value

    min_d2 = min(d2.values(), key=lambda value: float(value.evalf()))
    assert min_d2 == 4

    A = sp.zeros(12, 12)
    for (i, j), value in d2.items():
        if value == min_d2:
            A[i, j] = A[j, i] = 1

    assert A == A.T
    assert [sum(A[i, j] for j in range(12)) for i in range(12)] == [5] * 12

    # Reproduce the source's antipodal-axis dictionary ordering/sign choice.
    axes = {}
    for v in vertices:
        max_index = max(range(3), key=lambda idx: abs(v[idx]))
        canonical = tuple(v if v[max_index] > 0 else tuple(-z for z in v))
        axes.setdefault(canonical, v)
    assert len(axes) == 6
    reps = list(axes.values())

    B = sp.zeros(12, 6)
    for j, rep in enumerate(reps):
        ip = vertices.index(tuple(rep))
        im = vertices.index(tuple(-z for z in rep))
        B[ip, j] = 1
        B[im, j] = -1

    assert B.T * B == 2 * sp.eye(6)

    C6 = B.T * A * B / 2
    assert all(entry.is_Integer for entry in C6)
    assert C6 == C6.T

    pairs = list(combinations(range(6), 2))
    C15 = sp.zeros(15, 15)
    C15_direct = sp.zeros(15, 15)

    # Formula for the matrix induced on Lambda^2 V:
    # row [ij], column [kl] = C_ik C_jl - C_il C_jk.
    for row, (i, j) in enumerate(pairs):
        for col, (k, l) in enumerate(pairs):
            C15[row, col] = C6[i, k] * C6[j, l] - C6[i, l] * C6[j, k]

            # Independently apply C6 to e_k and e_l and take their wedge.
            col_k = C6[:, k]
            col_l = C6[:, l]
            C15_direct[row, col] = col_k[i] * col_l[j] - col_k[j] * col_l[i]

    assert C15 == C15_direct
    assert C15 == C15.T
    assert C15 * C15 == 25 * sp.eye(15)

    P_plus = (sp.eye(15) + C15 / 5) / 2
    P_minus = (sp.eye(15) - C15 / 5) / 2

    assert P_plus * P_plus == P_plus
    assert P_minus * P_minus == P_minus
    assert P_plus * P_minus == sp.zeros(15, 15)
    assert P_plus + P_minus == sp.eye(15)
    assert P_plus == P_plus.T and P_minus == P_minus.T
    assert P_plus.rank() == 6
    assert P_minus.rank() == 9

    lam = sp.symbols("lambda")
    characteristic_polynomial = sp.factor(C15.charpoly(lam).as_expr())
    assert characteristic_polynomial == (lam - 5) ** 6 * (lam + 5) ** 9

    print("PASS: exact icosahedral adjacency, degree 5")
    print("PASS: C6 symmetric and integer-valued")
    print("PASS: Lambda^2 C6 minor formula agrees with direct wedge action")
    print("PASS: C15 symmetric and C15^2 = 25 I_15 exactly")
    print("PASS: P+ / P- orthogonal complementary projectors")
    print("PASS: exact ranks rank(P+) = 6, rank(P-) = 9")
    print(f"charpoly(C15) = {characteristic_polynomial}")
    print("LIMIT: no 2I* representation matrices, commutators, or irreducibility tested")


if __name__ == "__main__":
    main()
