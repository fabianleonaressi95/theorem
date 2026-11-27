"""Exact character-level check for T124: 3 tensor 3' = 4 + 5.

This is deliberately not the 9x9 matrix-projector audit. It checks the
character identity over Q(sqrt(5)); see the T124 theorem record for the
remaining explicit matrix-realization obligations.
Run: python audits/t124_mixed_tensor_character_check.py
"""
import sympy as sp


def main():
    s5 = sp.sqrt(5)
    phi = (1 + s5) / 2
    phi_prime = (1 - s5) / 2
    sizes = (1, 15, 20, 12, 12)

    chi3 = (3, -1, 0, phi, phi_prime)
    chi3p = (3, -1, 0, phi_prime, phi)
    chi4 = (4, 0, 1, -1, -1)
    chi5 = (5, 1, -1, 0, 0)

    tensor = tuple(sp.simplify(a * b) for a, b in zip(chi3, chi3p))
    rhs = tuple(a + b for a, b in zip(chi4, chi5))
    assert sum(sizes) == 60
    assert sp.simplify(phi * phi_prime + 1) == 0
    assert tensor == rhs == (9, 1, 0, -1, -1)

    # Inner products against the irreducible characters give multiplicities.
    inner4 = sp.simplify(sum(n * a * b for n, a, b in zip(sizes, tensor, chi4)) / 60)
    inner5 = sp.simplify(sum(n * a * b for n, a, b in zip(sizes, tensor, chi5)) / 60)
    assert inner4 == 1
    assert inner5 == 1
    assert sp.simplify(sum(n * a * a for n, a in zip(sizes, tensor)) / 60) == 2

    print({
        "tensor_character": tuple(map(str, tensor)),
        "decomposition": "4 + 5",
        "multiplicities": {"4": int(inner4), "5": int(inner5)},
        "exact_Q_sqrt5": True,
        "matrix_projectors_checked": False,
    })


if __name__ == "__main__":
    main()
