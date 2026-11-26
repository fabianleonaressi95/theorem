#!/usr/bin/env python3
"""Finite algebraic audit of T143 using the geometric AntiTwin p(g)=g xor 7.

This checks the finite construction under the archive-documented label rule.
It does not independently reload the RGS binary matrices or infer phases from
SO(3)/SU(2) transport and plaquette holonomies.
"""
from __future__ import annotations
import cmath
import math

N = 64
TOL = 1e-10
MASK = 7
CODES = (3, 5, 9, 4, 2, 14)
REPRESENTATIVES = tuple(r for r in range(N) if r < (r ^ MASK))
EXPECTED_REPRESENTATIVES = (
    0, 1, 2, 3, 8, 9, 10, 11, 16, 17, 18, 19, 24, 25, 26, 27,
    32, 33, 34, 35, 40, 41, 42, 43, 48, 49, 50, 51, 56, 57, 58, 59,
)
FIXED = {
    2: (0.5, -math.sqrt(3.0) / 2.0),  # label 2 = -omega
    3: (1.0, 0.0),
    9: (-0.5, -math.sqrt(3.0) / 2.0),
}
FREE_REPRESENTATIVES = tuple(r for r in REPRESENTATIVES if r not in FIXED)

def zeros(m, n):
    return [[0.0] * n for _ in range(m)]

def eye(n):
    a = zeros(n, n)
    for i in range(n):
        a[i][i] = 1.0
    return a

def transpose(a):
    return [list(row) for row in zip(*a)]

def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def scale(c, a):
    return [[c * v for v in row] for row in a]

def max_abs(a):
    return max(abs(v) for row in a for v in row)

def error(a, b):
    return max_abs(sub(a, b))

def rank(a, tol=TOL):
    m = [list(map(float, row)) for row in a]
    rows, cols, r = len(m), len(m[0]), 0
    for col in range(cols):
        if r == rows:
            break
        pivot = max(range(r, rows), key=lambda i: abs(m[i][col]))
        if abs(m[pivot][col]) <= tol:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        p = m[r][col]
        m[r] = [v / p for v in m[r]]
        for i in range(rows):
            if i != r:
                q = m[i][col]
                m[i] = [m[i][j] - q * m[r][j] for j in range(cols)]
        r += 1
    return r

def permutation_matrix():
    j = zeros(N, N)
    for g in range(N):
        j[g ^ MASK][g] = 1.0
    return j

def build():
    omega = cmath.exp(2j * math.pi / 3)
    points = (1+0j, omega, omega**2, -1+0j, -omega, -(omega**2))
    x, y = zeros(6, 6), zeros(6, 6)
    for k, z in enumerate(points):
        x[k][k], y[k][k] = z.real, z.imag
    iota = zeros(N, 6)
    for col, code in enumerate(CODES):
        iota[code][col] = 1.0
    j = permutation_matrix()
    j6 = zeros(6, 6)
    for k in range(3):
        j6[k+3][k] = j6[k][k+3] = 1.0
    it = transpose(iota)
    pi = matmul(iota, it)
    x0, y0 = matmul(matmul(iota, x), it), matmul(matmul(iota, y), it)
    return x, y, iota, it, j, j6, pi, x0, y0

def build_full_diagonal_extension(angles):
    if len(angles) != 29:
        raise ValueError("exactly 29 complementary-pair angles are required")
    angle_by_rep = dict(zip(FREE_REPRESENTATIVES, angles))
    a, b = [0.0]*N, [0.0]*N
    for r in REPRESENTATIVES:
        ca, sb = FIXED[r] if r in FIXED else (
            math.cos(angle_by_rep[r]), math.sin(angle_by_rep[r]))
        partner = r ^ MASK
        a[r], b[r] = ca, sb
        a[partner], b[partner] = -ca, -sb
    xq = [[a[i] if i == j else 0.0 for j in range(N)] for i in range(N)]
    yq = [[b[i] if i == j else 0.0 for j in range(N)] for i in range(N)]
    return xq, yq, a, b

def run_audit():
    x, y, iota, it, j, j6, pi, x0, y0 = build()
    I6, I64 = eye(6), eye(64)
    p = [g ^ MASK for g in range(N)]
    angles = [0.137*(k+1) for k in range(29)]
    xq, yq, a, b = build_full_diagonal_extension(angles)
    errors = {
        "isometry": error(matmul(it, iota), I6),
        "embedding_intertwining": error(matmul(j, iota), matmul(iota, j6)),
        "zero_extension_X_hermitian": error(transpose(x0), x0),
        "zero_extension_Y_hermitian": error(transpose(y0), y0),
        "zero_extension_X_odd": error(matmul(matmul(j, x0), j), scale(-1, x0)),
        "zero_extension_Y_odd": error(matmul(matmul(j, y0), j), scale(-1, y0)),
        "zero_extension_sum_projection": error(
            add(matmul(x0, x0), matmul(y0, y0)), pi),
        "projection_idempotence": error(matmul(pi, pi), pi),
        "six_state_unit_circle": error(add(matmul(x, x), matmul(y, y)), I6),
        "full_X_odd": error(matmul(matmul(j, xq), j), scale(-1, xq)),
        "full_Y_odd": error(matmul(matmul(j, yq), j), scale(-1, yq)),
        "full_unit_circle": error(add(matmul(xq, xq), matmul(yq, yq)), I64),
        "full_X_hermitian": error(transpose(xq), xq),
        "full_Y_hermitian": error(transpose(yq), yq),
    }
    pair_partition = (
        REPRESENTATIVES == EXPECTED_REPRESENTATIVES
        and len(REPRESENTATIVES) == 32
        and len({min(g, p[g]) for g in range(N)}) == 32
        and all(p[p[g]] == g for g in range(N))
    )
    expected_fixed = {
        2: (0.5, -math.sqrt(3)/2), 5: (-0.5, math.sqrt(3)/2),
        3: (1.0, 0.0), 4: (-1.0, 0.0),
        9: (-0.5, -math.sqrt(3)/2), 14: (0.5, math.sqrt(3)/2),
    }
    fixed_values = all(
        abs(a[g]-v[0]) < TOL and abs(b[g]-v[1]) < TOL
        for g, v in expected_fixed.items()
    )
    ranks = {
        "embedded_X_even_to_odd": rank([[x[i][i] if i == k else 0.0
                                        for k in range(3)] for i in range(3)]),
        "embedded_Y_even_to_odd": rank([[y[i][i] if i == k else 0.0
                                        for k in range(3)] for i in range(3)]),
        "zero_extension_X": rank(x0),
        "zero_extension_Y": rank(y0),
        "orthogonal_complement_dimension": N-rank(pi),
    }
    expected_ranks = {
        "embedded_X_even_to_odd": 3, "embedded_Y_even_to_odd": 2,
        "zero_extension_X": 6, "zero_extension_Y": 4,
        "orthogonal_complement_dimension": 58,
    }
    status = (max(errors.values()) < TOL and pair_partition and fixed_values
              and len(FREE_REPRESENTATIVES) == 29 and ranks == expected_ranks)
    return {
        "status": "PASS" if status else "FAIL",
        "antipodal_rule": "g xor 7",
        "representatives": REPRESENTATIVES,
        "free_representatives": FREE_REPRESENTATIVES,
        "pair_partition": pair_partition,
        "fixed_values": fixed_values,
        "errors": errors,
        "ranks": ranks,
        "free_angle_count": len(angles),
        "transport_holonomy_audit": "NOT_RUN: archived SO(3)/SU(2) arrays not replayed",
    }

if __name__ == "__main__":
    result = run_audit()
    for key, value in result.items():
        print(f"{key}: {value}")
    raise SystemExit(0 if result["status"] == "PASS" else 1)
