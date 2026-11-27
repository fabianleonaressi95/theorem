"""Exact SymPy identities for the initial Sangaku geometry case studies."""
import sympy as sp

r, s, x = sp.symbols("r s x", positive=True, real=True)


def vesica():
    y2 = sp.factor(r**2 - s**2 / 4)
    chord2 = sp.factor(4 * y2)
    return y2, chord2


def pentagon():
    phi = (1 + sp.sqrt(5)) / 2
    assert sp.simplify(phi**2 - phi - 1) == 0
    side2 = (5 - sp.sqrt(5)) / 2
    diagonal2 = (5 + sp.sqrt(5)) / 2
    assert sp.simplify(diagonal2 / side2 - phi**2) == 0
    return phi, side2, diagonal2


def tangent_model():
    r1 = (r**2 - x**2) / (2 * r)
    root = (r**2 + x**2) / (2 * r)
    assert sp.simplify(root**2 - (r1**2 + x**2)) == 0
    r3 = -r1 + root
    r4 = root - r1
    assert sp.simplify(r3 - x**2 / r) == 0
    assert sp.simplify(r3 - r4) == 0
    return sp.factor(r1), sp.factor(r3), sp.factor(r4)


if __name__ == "__main__":
    print("Vesica:", vesica())
    print("Pentagon:", pentagon())
    print("Tangency model:", tangent_model())
    print("All exact symbolic identities passed.")
