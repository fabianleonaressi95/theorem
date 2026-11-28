"""Deterministic algebraic audit for the Q6 square 2-skeleton (T168)."""
from collections import deque
from fractions import Fraction
from itertools import combinations

N_BITS = 6
N_VERTICES = 1 << N_BITS


def edges():
    return tuple((v, v ^ (1 << k)) for v in range(64)
                 for k in range(6) if not (v & (1 << k)))


def spanning_tree():
    parent = {0: None}
    queue = deque([0])
    tree = set()
    while queue:
        v = queue.popleft()
        for w in sorted(v ^ (1 << k) for k in range(6)):
            if w not in parent:
                parent[w] = v
                tree.add(tuple(sorted((v, w))))
                queue.append(w)
    assert len(parent) == 64 and len(tree) == 63
    return parent, frozenset(tree)


def square_faces():
    out = []
    for i, j in combinations(range(6), 2):
        for base in range(64):
            if base & (1 << i) or base & (1 << j):
                continue
            vi, vij, vj = base | (1 << i), base | (1 << i) | (1 << j), base | (1 << j)
            out.append((base, vi, vij, vj))
    assert len(out) == 240
    return tuple(out)


def attaching_words():
    _, tree = spanning_tree()
    all_edges = tuple(sorted(tuple(sorted(e)) for e in edges()))
    chords = tuple(e for e in all_edges if e not in tree)
    gen = {e: k for k, e in enumerate(chords)}
    words = []
    for face in square_faces():
        word = []
        cyc = face + (face[0],)
        for a, b in zip(cyc, cyc[1:]):
            e = tuple(sorted((a, b)))
            if e not in tree:
                word.append((gen[e], 1 if a < b else -1))
        words.append(tuple(word))
    assert len(chords) == 129 and all(words)
    return chords, tuple(words)


def _sparse_rational_column_rank(columns):
    basis = {}
    for raw in columns:
        v = {r: Fraction(c) for r, c in raw.items() if c}
        while v:
            pivot = min(v)
            coeff = v[pivot]
            if pivot not in basis:
                basis[pivot] = {r: x / coeff for r, x in v.items()}
                break
            for r, x in basis[pivot].items():
                y = v.get(r, Fraction(0)) - coeff * x
                if y:
                    v[r] = y
                else:
                    v.pop(r, None)
    return len(basis)


def boundary_matrix_rank():
    edge_list = tuple(sorted(tuple(sorted(e)) for e in edges()))
    row = {e: k for k, e in enumerate(edge_list)}
    columns = []
    for face in square_faces():
        col = {}
        cyc = face + (face[0],)
        for a, b in zip(cyc, cyc[1:]):
            e = tuple(sorted((a, b)))
            col[row[e]] = col.get(row[e], 0) + (1 if a < b else -1)
        columns.append({r: c for r, c in col.items() if c})
    return _sparse_rational_column_rank(columns)


def audit():
    _, tree = spanning_tree()
    chords, words = attaching_words()
    rank = boundary_matrix_rank()
    return {
        "vertices": 64, "edges": 192, "tree_edges": len(tree),
        "free_generators": len(chords), "square_faces": len(square_faces()),
        "nonempty_square_words": sum(bool(w) for w in words),
        "boundary_rank_Q": rank, "H2_rank": 240 - rank,
        "Euler_characteristic": 64 - 192 + 240,
        "all_square_words_nonempty": all(words),
    }


if __name__ == "__main__":
    print(audit())
