"""Exact coordinate reconstruction of Hirano's Sangaku pentagon construction."""
import sympy as sp

sqrt5 = sp.sqrt(5)
rho = (sqrt5 - 1) / 2
O = sp.Point(0, 0)
A = sp.Point(-1, 0)
B = sp.Point(1, 0)
C = sp.Point(0, 1)
D = sp.Point(0, -1)
P = sp.Point(-sp.Rational(1, 2), 0)
Q = sp.Point(sp.Rational(1, 2), 0)

T = sp.Point(sp.Rational(1, 2) - 1 / (2 * sqrt5), 1 / sqrt5)
E = sp.Point(sp.sqrt(10 - 2 * sqrt5) / 4, (1 + sqrt5) / 4)
F = sp.Point(-sp.sqrt(10 - 2 * sqrt5) / 4, (1 + sqrt5) / 4)


def verify():
    assert sp.simplify(P.distance(A) - sp.Rational(1, 2)) == 0
    assert sp.simplify(P.distance(O) - sp.Rational(1, 2)) == 0
    assert sp.simplify(Q.distance(B) - sp.Rational(1, 2)) == 0
    assert sp.simplify(Q.distance(O) - sp.Rational(1, 2)) == 0

    # T lies on line CQ and on the circle centred at Q with radius 1/2.
    assert sp.simplify(sp.det(sp.Matrix([
        [T.x - C.x, T.y - C.y],
        [Q.x - C.x, Q.y - C.y],
    ]))) == 0
    assert sp.simplify(T.distance(Q) - sp.Rational(1, 2)) == 0
    assert sp.simplify(T.distance(C) - rho) == 0

    for X in (E, F):
        assert sp.simplify(X.distance(O)**2 - 1) == 0
        assert sp.simplify(X.distance(C)**2 - rho**2) == 0

    chord2 = sp.simplify(E.distance(F)**2)
    assert sp.simplify(chord2 - (5 - sqrt5) / 2) == 0
    assert sp.simplify(E.dot(F) - (sqrt5 - 1) / 4) == 0
    return {
        "CT": sp.simplify(rho),
        "E": E,
        "F": F,
        "EF_squared": chord2,
        "central_cosine": sp.simplify(E.dot(F)),
    }


if __name__ == "__main__":
    print(verify())
    print("Hirano Sangaku exact reconstruction: all assertions passed.")
