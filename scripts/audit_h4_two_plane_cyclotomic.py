#!/usr/bin/env python3
"""Exact representative checks and numerical exhaustive H4 angle census.

Exact arithmetic in Q(sqrt(5)) certifies the two displayed words, their
orders, and characteristic polynomials. The full 14,400-element enumeration
uses rounded floating-point matrices and is explicitly only a numerical census.
"""
from collections import Counter, deque
from fractions import Fraction as F
import math
import numpy as np

# ---------------- Exact arithmetic in Q(sqrt(5)) ----------------
# Represent a + b*sqrt(5) by (Fraction(a), Fraction(b)).
ZERO = (F(0), F(0))
ONE = (F(1), F(0))

def qadd(x, y):
    return (x[0] + y[0], x[1] + y[1])

def qneg(x):
    return (-x[0], -x[1])

def qsub(x, y):
    return qadd(x, qneg(y))

def qmul(x, y):
    return (x[0]*y[0] + 5*x[1]*y[1],
            x[0]*y[1] + x[1]*y[0])

def qscale(x, r):
    return (x[0]*r, x[1]*r)

def qdiv_int(x, n):
    return (x[0]/n, x[1]/n)

def qsum(items):
    out = ZERO
    for item in items:
        out = qadd(out, item)
    return out

I_exact = [[ONE if i == j else ZERO for j in range(4)] for i in range(4)]
G_exact = [[ONE if i == j else ZERO for j in range(4)] for i in range(4)]
c5 = (F(1, 4), F(1, 4))  # cos(pi/5) = (1 + sqrt(5))/4
G_exact[0][1] = G_exact[1][0] = qneg(c5)
G_exact[1][2] = G_exact[2][1] = (F(-1, 2), F(0))
G_exact[2][3] = G_exact[3][2] = (F(-1, 2), F(0))

def matmul_exact(A, B):
    return [[qsum([qmul(A[i][k], B[k][j]) for k in range(4)])
             for j in range(4)] for i in range(4)]

def matpow_exact(A, n):
    out = [row[:] for row in I_exact]
    for _ in range(n):
        out = matmul_exact(out, A)
    return out

def transpose_exact(A):
    return [[A[j][i] for j in range(4)] for i in range(4)]

def trace_exact(A):
    return qsum([A[i][i] for i in range(4)])


def matrix_add_exact(A, B):
    return [[qadd(A[i][j], B[i][j]) for j in range(4)] for i in range(4)]

def matrix_scale_exact(A, scalar):
    return [[qmul(scalar, A[i][j]) for j in range(4)] for i in range(4)]

def matrix_equal_exact(A, B):
    return A == B


def format_qsqrt5(value):
    a, b = value
    if b == 0:
        return str(a)
    if a == 0:
        return f"({b})*sqrt(5)"
    return f"({a}) + ({b})*sqrt(5)"

def print_exact_matrix(name, A):
    print(name + " (simple-root coordinates; entries in Q(sqrt(5))):")
    for row in A:
        print("  [" + ", ".join(format_qsqrt5(x) for x in row) + "]")

def charpoly_exact(A):
    # Newton identities; result [1,c1,c2,c3,c4] for
    # x^4 + c1*x^3 + c2*x^2 + c3*x + c4.
    power_traces = [None] + [trace_exact(matpow_exact(A, k))
                             for k in range(1, 5)]
    coeffs = [ONE]
    for k in range(1, 5):
        total = qsum([qmul(coeffs[k-i], power_traces[i])
                      for i in range(1, k+1)])
        coeffs.append(qdiv_int(qneg(total), k))
    return coeffs

S_exact = []
for i in range(4):
    R = [row[:] for row in I_exact]
    for j in range(4):
        R[i][j] = qsub(R[i][j], qscale(G_exact[i][j], F(2)))
    S_exact.append(R)

for reflection in S_exact:
    assert matmul_exact(matmul_exact(transpose_exact(reflection), G_exact),
                        reflection) == G_exact

WORD_ORDER3 = (1, 2, 1, 2, 1, 3, 2, 1, 2, 1, 3, 2, 1, 2, 4, 3,
               2, 1, 2, 1, 3, 2, 1, 2, 4, 3, 2, 1, 2, 1, 3, 2,
               1, 4, 3, 2, 1, 2, 3, 4)
WORD_ORDER5 = (1, 2, 1, 2, 1, 3, 2, 1, 2, 1, 3, 2, 1, 4, 3, 2,
               1, 2, 1, 3, 2, 1, 2, 3, 4, 3)

def exact_word(word):
    out = [row[:] for row in I_exact]
    for i in word:
        out = matmul_exact(out, S_exact[i-1])
    return out

U3_exact = exact_word(WORD_ORDER3)
U5_exact = exact_word(WORD_ORDER5)
assert matpow_exact(U3_exact, 3) == I_exact
assert matpow_exact(U5_exact, 5) == I_exact
assert charpoly_exact(U3_exact) == [
    ONE, (F(2),F(0)), (F(3),F(0)), (F(2),F(0)), ONE
]
assert charpoly_exact(U5_exact) == [
    ONE, ONE, ONE, ONE, ONE
]


# Exact invariant-plane projectors for the order-five element.
# cos(72°)=(sqrt(5)-1)/4; cos(144°)=-(sqrt(5)+1)/4.
cos72 = (F(-1, 4), F(1, 4))
cos144 = (F(-1, 4), F(-1, 4))

def spectral_pair_projector(U, cosine_weights):
    out = [[ZERO for _ in range(4)] for _ in range(4)]
    power = [row[:] for row in I_exact]
    scale = (F(2, 5), F(0))
    for weight in cosine_weights:
        out = matrix_add_exact(out, matrix_scale_exact(
            power, qmul(scale, weight)
        ))
        power = matmul_exact(power, U)
    return out

P72_exact = spectral_pair_projector(
    U5_exact, [ONE, cos72, cos144, cos144, cos72]
)
P144_exact = spectral_pair_projector(
    U5_exact, [ONE, cos144, cos72, cos72, cos144]
)
assert matmul_exact(P72_exact, P72_exact) == P72_exact
assert matmul_exact(P144_exact, P144_exact) == P144_exact
assert matmul_exact(P72_exact, P144_exact) == [[ZERO for _ in range(4)] for _ in range(4)]
assert matrix_add_exact(P72_exact, P144_exact) == I_exact
assert matmul_exact(U5_exact, P72_exact) == matmul_exact(P72_exact, U5_exact)
assert matmul_exact(U5_exact, P144_exact) == matmul_exact(P144_exact, U5_exact)
assert matmul_exact(transpose_exact(P72_exact), G_exact) == matmul_exact(G_exact, P72_exact)
assert matmul_exact(transpose_exact(P144_exact), G_exact) == matmul_exact(G_exact, P144_exact)
assert trace_exact(P72_exact) == (F(2), F(0))
assert trace_exact(P144_exact) == (F(2), F(0))

# The order-three element is isoclinic. K is sqrt(3) times a G-orthogonal
# complex structure; choosing any v gives one invariant plane span(v,Kv),
# but no such pair is canonical.
K3_exact = matrix_add_exact(
    matrix_scale_exact(U3_exact, (F(2), F(0))), I_exact
)
minus3I_exact = matrix_scale_exact(I_exact, (F(-3), F(0)))
assert matmul_exact(K3_exact, K3_exact) == minus3I_exact
assert matrix_add_exact(
    matmul_exact(transpose_exact(K3_exact), G_exact),
    matmul_exact(G_exact, K3_exact)
) == [[ZERO for _ in range(4)] for _ in range(4)]

# ---------------- Floating-point full-group enumeration ----------------
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
for reflection in S:
    assert np.linalg.norm(reflection.T @ reflection - I4) < 2e-8
    assert abs(np.linalg.det(reflection) + 1.0) < 2e-8

def word_matrix(word):
    out = I4.copy()
    for i in word:
        out = out @ S[i-1]
    return out

def angle_pair(A):
    vals = np.linalg.eigvals(A)
    # Each real rotation-plane angle occurs twice, including 0 and pi.
    angles = sorted(abs(float(np.angle(z))) for z in vals)
    return (angles[0], angles[2])

def check_word(word, expected):
    U = word_matrix(word)
    assert np.linalg.norm(U.T @ U - I4) < 2e-8
    assert abs(np.linalg.det(U) - 1.0) < 2e-8
    angles = angle_pair(U)
    assert max(abs(angles[i] - expected[i]) for i in range(2)) < 2e-7
    return angles

a3 = check_word(WORD_ORDER3, (2*math.pi/3, 2*math.pi/3))
a5 = check_word(WORD_ORDER5, (2*math.pi/5, 4*math.pi/5))
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
assert proper_pairs[p120] == 40
assert proper_pairs[p72_144] == 288

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

print("H4 audit: PASS")
print("Exact Q(sqrt(5)) checks: U3^3=I, charpoly(U3)=(x^2+x+1)^2")
print("Exact Q(sqrt(5)) checks: U5^5=I, charpoly(U5)=Phi_5(x)")
print("Exact invariant-plane projectors P72 and P144: idempotent, orthogonal,")
print("  complementary, G-self-adjoint, U5-invariant, each rank 2.")
print("Exact order-three complex structure K=2U3+I: K^2=-3I and K^T G+GK=0.")
print(f"Numerical census: |H4|={len(seen)}, proper rotations=7200")
print("Order-three angles (deg):", tuple(round(math.degrees(x), 8) for x in a3))
print("Order-three chord singular values:", (s3, s3), "sqrt(3) =", math.sqrt(3))
print("Order-five angles (deg):", tuple(round(math.degrees(x), 8) for x in a5))
print("Order-five chord singular values:", tuple(s5), "ratio =", s5[1]/s5[0], "phi =", PHI)
print("Counts (120,120) and (72,144):", proper_pairs[p120], proper_pairs[p72_144])
print("Mixed 120/golden angle pairs:", mixed)
print_exact_matrix("P72", P72_exact)
print_exact_matrix("P144", P144_exact)
print_exact_matrix("K3=2U3+I", K3_exact)
print("NOTE: full group census uses rounded floating-point keys; representative checks are exact.")
