#!/usr/bin/env python3
"""Exact-integer McKay E8 / Molien consistency check for the binary icosahedral group.

No third-party dependencies. This verifies the stated affine E8 graph data and
compares the SU(2) restriction recurrence with the Molien coefficient formula
through degree 120. It is a finite computational check, not a proof of McKay's
correspondence or Molien's theorem.
"""

from __future__ import annotations

MAX_DEGREE = 120

# Vertex order: trivial, defining 2D, then along the long arm, then the
# length-two arm, then the length-one arm.
DIMENSIONS = (1, 2, 3, 4, 5, 6, 4, 2, 3)
EDGES = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (5, 8),
)


def adjacency_matrix() -> list[list[int]]:
    n = len(DIMENSIONS)
    matrix = [[0] * n for _ in range(n)]
    for i, j in EDGES:
        matrix[i][j] = 1
        matrix[j][i] = 1
    return matrix


def mat_vec(matrix: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def molien_coefficient(degree: int) -> int:
    """Coefficient of t^degree in (1+t^30)/((1-t^12)(1-t^20))."""
    count = 0
    for epsilon in (0, 1):
        remainder = degree - 30 * epsilon
        if remainder < 0:
            continue
        for r in range(remainder // 12 + 1):
            if (remainder - 12 * r) % 20 == 0:
                count += 1
    return count


def mckay_invariant_coefficients(max_degree: int) -> list[int]:
    """Return a_n = multiplicity of the trivial irrep in Sym^n(C^2)."""
    # m_0 = e_0, m_1 = e_1 (the defining two-dimensional representation).
    previous = [1] + [0] * 8
    current = [0, 1] + [0] * 7
    coefficients = [previous[0], current[0]]

    matrix = adjacency_matrix()
    for _n in range(1, max_degree):
        product = mat_vec(matrix, current)
        following = [product[i] - previous[i] for i in range(9)]
        if any(value < 0 for value in following):
            raise AssertionError("Negative irreducible multiplicity in recurrence")
        coefficients.append(following[0])
        previous, current = current, following

    return coefficients[: max_degree + 1]


def main() -> None:
    matrix = adjacency_matrix()

    # Dimension vector is the positive null vector of 2I - A.
    twice_dimensions = [2 * value for value in DIMENSIONS]
    adjacency_dimensions = mat_vec(matrix, list(DIMENSIONS))
    assert adjacency_dimensions == twice_dimensions

    # Sum of squared irreducible dimensions equals the group order.
    assert sum(value * value for value in DIMENSIONS) == 120

    # The graph is connected and has 9 vertices / 8 edges: affine E8 is a tree.
    assert len(EDGES) == 8
    reached = {0}
    while True:
        expanded = reached | {
            j for i, j in EDGES if i in reached
        } | {
            i for i, j in EDGES if j in reached
        }
        if expanded == reached:
            break
        reached = expanded
    assert len(reached) == 9

    mckay = mckay_invariant_coefficients(MAX_DEGREE)
    molien = [molien_coefficient(n) for n in range(MAX_DEGREE + 1)]
    mismatches = [
        (n, mckay[n], molien[n])
        for n in range(MAX_DEGREE + 1)
        if mckay[n] != molien[n]
    ]
    assert not mismatches, mismatches

    # Central element -1 acts by (-1)^n on Sym^n(C^2).
    assert all(mckay[n] == 0 for n in range(1, MAX_DEGREE + 1, 2))

    first_positive = next(n for n in range(1, MAX_DEGREE + 1) if mckay[n])
    assert first_positive == 12
    eigenvalue = first_positive * (first_positive + 2)
    multiplicity = (first_positive + 1) * mckay[first_positive]
    assert (eigenvalue, multiplicity) == (168, 13)

    print(f"PASS: affine E8 dimension-vector checks")
    print(f"PASS: sum(dim rho_i^2) = {sum(x*x for x in DIMENSIONS)} = |2I|")
    print(f"PASS: McKay recurrence agrees with Molien coefficients: "
          f"{MAX_DEGREE + 1}/{MAX_DEGREE + 1}")
    print(f"First positive invariant degree: n={first_positive}")
    print(f"First positive scalar eigenvalue: {eigenvalue}")
    print(f"Quotient multiplicity at that eigenvalue: {multiplicity}")


if __name__ == "__main__":
    main()
