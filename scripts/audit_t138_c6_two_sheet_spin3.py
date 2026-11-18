#!/usr/bin/env python3
"""Exact integer audit for T138: the six-dimensional two-sheet matrix."""
C = (
    (0, 1, 1, -1, -1, 1),
    (1, 0, 1, 1, -1, -1),
    (1, 1, 0, -1, 1, -1),
    (-1, 1, -1, 0, -1, -1),
    (-1, -1, 1, -1, 0, -1),
    (1, -1, -1, -1, -1, 0),
)
U = ((0, 1, 1), (1, 0, 1), (1, 1, 0))
S = ((-1, -1, 1), (1, -1, -1), (-1, 1, -1))

def tr(a):
    return tuple(zip(*a))

def mm(a, b):
    bt = tr(b)
    return tuple(tuple(sum(x*y for x, y in zip(row, col)) for col in bt) for row in a)

def eye(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))

def scale(k, a):
    return tuple(tuple(k*x for x in row) for row in a)

def run():
    assert mm(C, C) == scale(5, eye(6))
    st = tr(S)
    target = tuple(tuple(4*int(i == j)-1 for j in range(3)) for i in range(3))
    assert mm(U, U) == tuple(tuple(1+int(i == j) for j in range(3)) for i in range(3))
    assert mm(S, st) == target == mm(st, S)
    assert mm(U, S) == mm(S, U)
    # All four blocks of the square are checked independently.
    assert tuple(tuple(x+y for x, y in zip(a, b)) for a, b in zip(mm(U,U), mm(S,st))) == scale(5, eye(3))
    assert mm(U,S) == mm(S,U)
    assert mm(st,U) == mm(U,st)
    print("T138 exact integer audit: PASS (36 entries and block identities).")

if __name__ == "__main__":
    run()
