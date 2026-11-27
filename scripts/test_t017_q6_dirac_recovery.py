#!/usr/bin/env python3
"""Exact finite audit of the Q6=H(6,2) graph Laplacian.

This tests the vertex graph Laplacian and Walsh basis only. It does NOT
construct or certify the historical T017 Dirac operator.
Uses Python integers and the standard library only.
"""
from itertools import product, combinations
from math import comb

N = 6
vertices = list(product((0, 1), repeat=N))
index = {v: i for i, v in enumerate(vertices)}
assert len(vertices) == 64

# Integer graph Laplacian L = 6 I - adjacency.
L = [[0] * 64 for _ in range(64)]
for i, v in enumerate(vertices):
    L[i][i] = N
    for bit in range(N):
        w = list(v)
        w[bit] ^= 1
        L[i][index[tuple(w)]] -= 1

# Every Walsh character is an exact integer eigenvector.
multiplicity = [0] * (N + 1)
for r in range(N + 1):
    for S in combinations(range(N), r):
        S = set(S)
        chi = [(-1) ** sum(v[j] for j in S) for v in vertices]
        eigenvalue = 2 * r
        for i in range(64):
            lhs = sum(L[i][j] * chi[j] for j in range(64))
            assert lhs == eigenvalue * chi[i], (r, i, lhs)
        multiplicity[r] += 1

# Orthogonality: distinct Walsh characters have zero inner product.
characters = []
for r in range(N + 1):
    for S_tuple in combinations(range(N), r):
        S = set(S_tuple)
        characters.append([(-1) ** sum(v[j] for j in S) for v in vertices])
assert len(characters) == 64
for a in range(64):
    for b in range(a, 64):
        dot = sum(x * y for x, y in zip(characters[a], characters[b]))
        assert dot == (64 if a == b else 0)

expected = [comb(N, r) for r in range(N + 1)]
assert multiplicity == expected == [1, 6, 15, 20, 15, 6, 1]
assert sum(multiplicity) == 64

# Full cubical 6-cube cell counts: choose varying axes and fix remaining bits.
cell_counts = [comb(N, k) * (2 ** (N - k)) for k in range(N + 1)]
assert cell_counts == [64, 192, 240, 160, 60, 12, 1]
assert sum(cell_counts) == 3 ** N == 729

print("PASS: Q6 graph Laplacian Walsh eigenpairs (exact integer arithmetic)")
print("eigenvalues:", [2 * r for r in range(N + 1)])
print("multiplicities:", multiplicity)
print("cubical cell counts:", cell_counts, "total:", sum(cell_counts))
print("LIMIT: no T017 Dirac matrix, Clifford action, or full Dirac spectrum tested")
