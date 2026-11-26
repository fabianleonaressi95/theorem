import sympy as sp

from research.sangaku_geometry.symbolic_checks import vesica, pentagon, tangent_model


def test_vesica_exact_chord():
    _, chord2 = vesica()
    r, s = sp.symbols("r s", positive=True, real=True)
    assert sp.simplify(chord2 - (4*r**2 - s**2)) == 0


def test_pentagon_golden_ratio():
    phi, _, _ = pentagon()
    assert sp.simplify(phi**2 - phi - 1) == 0


def test_tangent_model_equal_radii():
    r1, r3, r4 = tangent_model()
    r, x = sp.symbols("r x", positive=True, real=True)
    assert sp.simplify(r3 - x**2/r) == 0
    assert sp.simplify(r3 - r4) == 0
    assert sp.simplify(r1.subs(x, r/3)/r - sp.Rational(4, 9)) == 0
    assert sp.simplify(r3.subs(x, r/3)/r - sp.Rational(1, 9)) == 0
