#!/usr/bin/env python3
"""Numerical exhaustive audit of two-plane rotations in the H4 Coxeter group.

The group is generated in simple-root coordinates by the [5,3,3] Coxeter
reflections. Enumeration uses rounded floating-point matrices, so this is a
reproducible numerical census, not an exact algebraic-number certificate.
"""
from collections import Counter, deque
import math
import numpy as np

PHI = (1.0 + math.sqrt(5.0)) / 2.0
G = np.array([
    [1.0, -math.cos(math.pi / 5.0), 0.0, 0.0],
    [-math.cos(math.pi / 5.0), 1.0, -0.5, 0.0],
    [0.0, -0.5, 1.0, -0.5],
    [0.0, 0.0, -0.5, 1.0],
])
I4 = np.eye(4)

S_root = []
for i in range(4):
    e = np.eye(4)[:, i]
    S_root.append(I4 - 2.0 * np.outer(e, G[i, :]))

L = np.linalg.cholesky(G).T
Linv = np.linalg.inv(L)
S = [L @ R @ Linv for R in S_root]

WORD_ORDER3 = (1, 2, 1, 2, 3, 2, 1, 2, 3, 4)
WORD_ORDER5 = (1, 2, 1, 2, 1, 3, 2, 1, 2, 1, 3, 2, 1,
               4, 3, 2, 1, 2, 1, 3, 2, 1, 2, 3, 4, 3)

def word_matrix(word):
    out = I4.copy()
    for i in word:
        out = out @ S[i - 1]
    return out

def angle_pair(A):
    vals = np.linalg.eigvals(A)
    # Each real rotation-plane angle occurs twice in the four eigenvalues;
    # this also handles 0 and pi planes (real eigenvalues +/-1).
    angles = sorted(abs(float(np.angle(z))) for z in vals)
    return (angles[0], angles[2])

def check_word(word, expected):
    U = word_matrix(word)
    assert np.linalg.norm(U.T @ U - I4) < 2e-8
    assert abs(np.linalg.det(U) - 1.0) < 2e-8
    angles = angle_pair(U)
    assert max(abs(angles[i] - expected[i]) for i in range(2)) < 2e-7
    return U, angles

U3, a3 = check_word(WORD_ORDER3, (2*math.pi/3, 2*math.pi/3))
U5, a5 = check_word(WORD_ORDER5, (2*math.pi/5, 4*math.pi/5))

s3 = 2.0 * math.sin(a3[0] / 2.0)
s5 = sorted(2.0 * math.sin(a / 2.0) for a in a5)
assert abs(s3 - math.sqrt(3.0)) < 2e-7
assert abs(s5[1] / s5[0] - PHI) < 2e-7

def key(A):
    return tuple(np.round(A, 8).ravel())

seen = {key(I4): I4}
queue = deque([I4])
while queue:
    A = queue.popleft()
    for R in S:
        B = A @ R
        k = key(B)
        if k not in seen:
            seen[k] = B
            queue.append(B)

assert len(seen) == 14400, f"Expected |H4|=14400, got {len(seen)}"

proper_pairs = Counter()
for A in seen.values():
    if np.linalg.det(A) > 0.5:
        proper_pairs[tuple(round(x, 6) for x in angle_pair(A))] += 1

assert sum(proper_pairs.values()) == 7200
p120 = (round(2*math.pi/3, 6), round(2*math.pi/3, 6))
p72_144 = (round(2*math.pi/5, 6), round(4*math.pi/5, 6))
assert proper_pairs[p120] > 0 and proper_pairs[p72_144] > 0

mixed = []
for pair, count in proper_pairs.items():
    has_120 = any(abs(x - 2*math.pi/3) < 2e-5 for x in pair)
    has_golden = any(
        min(abs(x - 2*math.pi/5), abs(x - 4*math.pi/5)) < 2e-5
        for x in pair
    )
    if has_120 and has_golden:
        mixed.append((pair, count))
assert not mixed, f"Unexpected mixed-angle H4 element(s): {mixed}"

print("H4 numerical audit: PASS")
print(f"|H4| = {len(seen)}; proper rotations = {sum(proper_pairs.values())}")
print("order-3 representative angles (deg):", tuple(round(math.degrees(x), 8) for x in a3))
print("order-3 chord singular values:", (s3, s3), "target sqrt(3) =", math.sqrt(3))
print("order-5 representative angles (deg):", tuple(round(math.degrees(x), 8) for x in a5))
print("order-5 chord singular values:", tuple(s5), "ratio =", s5[1]/s5[0], "phi =", PHI)
print("count (120,120) degrees:", proper_pairs[p120])
print("count (72,144) degrees:", proper_pairs[p72_144])
print("mixed 120/golden angle pairs:", mixed)
print("NOTE: rounded-matrix enumeration is a numerical census, not an exact class certificate.")
