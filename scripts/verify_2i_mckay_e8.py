#!/usr/bin/env python3
"""Exact-integer McKay E8 / Molien consistency check for the binary icosahedral group.

No third-party dependencies. The vector m_r contains the multiplicities of all
nine irreducible 2I representations in Sym^r(C^2)|_{2I}. The script checks the
McKay recurrence against the Molien coefficient formula through degree 120.
This finite check is not a proof of McKay's correspondence or Molien's theorem.
"""

from __future__ import annotations

MAX_DEGREE = 120
TABLE_MAX_DEGREE = 60

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
        for p in range(remainder // 12 + 1):
            if (remainder - 12 * p) % 20 == 0:
                count += 1
    return count


def mckay_multiplicity_vectors(max_degree: int) -> list[list[int]]:
    """Return m_r, with (m_r)_i = mult(rho_i, Sym^r(C^2)|_{2I})."""
    # m_0=e_0 (trivial); m_1=e_1 (the defining two-dimensional irrep).
    previous = [1] + [0] * 8
    current = [0, 1] + [0] * 7
    vectors = [previous, current]
    matrix = adjacency_matrix()

    for _r in range(1, max_degree):
        product = mat_vec(matrix, current)
        following = [product[i] - previous[i] for i in range(9)]
        if any(value < 0 for value in following):
            raise AssertionError("Negative irreducible multiplicity in recurrence")
        vectors.append(following)
        previous, current = current, following

    return vectors[: max_degree + 1]


def main() -> None:
    matrix = adjacency_matrix()

    # The affine E8 dimension vector is the positive null vector of 2I - A.
    adjacency_dimensions = mat_vec(matrix, list(DIMENSIONS))
    assert adjacency_dimensions == [2 * value for value in DIMENSIONS]

    # Sum of squared irreducible dimensions equals the group order.
    assert sum(value * value for value in DIMENSIONS) == 120

    # Connected graph with 9 vertices and 8 edges is a tree.
    assert len(EDGES) == 8
    reached = {0}
    frontier = [0]
    while frontier:
        vertex = frontier.pop()
        for i, j in EDGES:
            neighbour = j if i == vertex else i if j == vertex else None
            if neighbour is not None and neighbour not in reached:
                reached.add(neighbour)
                frontier.append(neighbour)
    assert len(reached) == 9

    vectors = mckay_multiplicity_vectors(MAX_DEGREE)
    mckay = [vector[0] for vector in vectors]
    molien = [molien_coefficient(r) for r in range(MAX_DEGREE + 1)]

    even_mismatches = [
        (r, mckay[r], molien[r])
        for r in range(0, MAX_DEGREE + 1, 2)
        if mckay[r] != molien[r]
    ]
    odd_nonzero = [
        (r, mckay[r], molien[r])
        for r in range(1, MAX_DEGREE + 1, 2)
        if mckay[r] != 0 or molien[r] != 0
    ]
    assert not even_mismatches, even_mismatches
    assert not odd_nonzero, odd_nonzero

    first_positive = next(r for r in range(1, MAX_DEGREE + 1) if mckay[r])
    assert first_positive == 12
    assert mckay[60] == 2
    assert mckay[120] == 3
    assert (first_positive * (first_positive + 2),
            (first_positive + 1) * mckay[first_positive]) == (168, 13)

    print("PASS: affine E8 dimension-vector and graph checks")
    print("PASS: sum(dim rho_i^2) = 120 = |2I|")
    print(f"PASS: even-degree McKay/Molien comparisons: "
          f"{MAX_DEGREE // 2 + 1}/{MAX_DEGREE // 2 + 1}")
    print(f"PASS: odd-degree central-parity checks: "
          f"{MAX_DEGREE // 2}/{MAX_DEGREE // 2}")
    print(f"PASS: total degree checks 0..{MAX_DEGREE}: {MAX_DEGREE + 1}")
    print()
    print("k  spin  a_k  lambda_k  d_k")
    for k in range(0, TABLE_MAX_DEGREE + 1, 2):
        a_k = mckay[k]
        print(f"{k:2d} {k // 2:5d} {a_k:4d} "
              f"{k * (k + 2):9d} {(k + 1) * a_k:4d}")
    print()
    print(f"At k=60: a_60={mckay[60]}, d_60={61 * mckay[60]}")
    print(f"At k=120: a_120={mckay[120]}, d_120={121 * mckay[120]}")


if __name__ == "__main__":
    main()
