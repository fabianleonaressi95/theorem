"""Exact finite-field audit of the Q6 square 2-skeleton counts and ranks.

The theorem's integral homology argument is given in T167. This script is an
independent combinatorial regression audit over F_2, not a substitute for the
integral proof.
"""
from __future__ import annotations


def gf2_rank(columns: list[int]) -> int:
    pivots: dict[int, int] = {}
    for value in columns:
        x = value
        while x:
            p = x.bit_length() - 1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                break
    return len(pivots)


def q6_square_complex_audit() -> dict[str, int]:
    n = 6
    vertices = list(range(1 << n))
    edges = [(v, i) for v in vertices for i in range(n) if not (v >> i) & 1]
    edge_index = {e: k for k, e in enumerate(edges)}

    squares = []
    for i in range(n):
        for j in range(i + 1, n):
            for v in vertices:
                if ((v >> i) & 1) == 0 and ((v >> j) & 1) == 0:
                    squares.append((v, i, j))

    # Boundary columns over F_2; signs disappear.
    d1_cols = []
    for v, i in edges:
        w = v ^ (1 << i)
        # Each edge has two endpoint incidences.
        d1_cols.append((1 << v) | (1 << w))

    d2_cols = []
    for v, i, j in squares:
        e_i_at_v = edge_index[(v, i)]
        e_i_at_vj = edge_index[(v ^ (1 << j), i)]
        e_j_at_v = edge_index[(v, j)]
        e_j_at_vi = edge_index[(v ^ (1 << i), j)]
        d2_cols.append(
            (1 << e_i_at_v)
            | (1 << e_i_at_vj)
            | (1 << e_j_at_v)
            | (1 << e_j_at_vi)
        )

    return {
        "vertices": len(vertices),
        "edges": len(edges),
        "squares": len(squares),
        "rank_d1_mod2": gf2_rank(d1_cols),
        "rank_d2_mod2": gf2_rank(d2_cols),
        "euler_characteristic": len(vertices) - len(edges) + len(squares),
        "b2_from_integral_exactness": len(squares) - (len(edges) - 63),
    }


if __name__ == "__main__":
    result = q6_square_complex_audit()
    expected = {
        "vertices": 64,
        "edges": 192,
        "squares": 240,
        "rank_d1_mod2": 63,
        "rank_d2_mod2": 129,
        "euler_characteristic": 112,
        "b2_from_integral_exactness": 111,
    }
    assert result == expected, (result, expected)
    print(result)
