#!/usr/bin/env python3
"""Exact matrix-unit audit for finite-group representations.

Input is deliberately explicit: callers provide an exact group multiplication
table, exact unitary matrices U(g), and exact irreducible matrices rho(g).
No floating-point reconstruction of the 2I character table is attempted.
Requires SymPy. The function checks the chosen left-representation convention.
"""
from __future__ import annotations

from typing import Dict, Hashable, Mapping, Sequence, Tuple
import sympy as sp


def adjoint(A: sp.Matrix) -> sp.Matrix:
    return A.conjugate().T


def matrix_units(
    elements: Sequence[Hashable],
    representation: Mapping[Hashable, sp.Matrix],
    irrep: Mapping[Hashable, sp.Matrix],
) -> Dict[Tuple[int, int], sp.Matrix]:
    """Return E_ij = d/|G| sum_g conjugate(rho(g)_ij) U(g)."""
    if not elements:
        raise ValueError("The group element list is empty.")
    d = next(iter(irrep.values())).rows
    if any(M.shape != (d, d) for M in irrep.values()):
        raise ValueError("Irrep matrices have inconsistent dimensions.")
    n = next(iter(representation.values())).rows
    if any(M.shape != (n, n) for M in representation.values()):
        raise ValueError("Ambient representation matrices have inconsistent dimensions.")
    if set(elements) != set(representation) or set(elements) != set(irrep):
        raise ValueError("Every group element must occur in both representations.")
    out = {}
    for i in range(d):
        for j in range(d):
            E = sp.zeros(n)
            for g in elements:
                E += sp.conjugate(irrep[g][i, j]) * representation[g]
            out[i, j] = sp.simplify(sp.Rational(d, len(elements)) * E)
    return out


def verify_matrix_units(
    units: Mapping[Tuple[int, int], sp.Matrix],
    d: int,
) -> dict:
    """Verify E_ij E_kl = delta_jk E_il and E_ij*=E_ji exactly."""
    if not units:
        raise ValueError("No matrix units supplied.")
    sample = next(iter(units.values()))
    failures = []
    for i in range(d):
        for j in range(d):
            if adjoint(units[i, j]) != units[j, i]:
                failures.append(("adjoint", i, j))
            for k in range(d):
                for ell in range(d):
                    target = units[i, ell] if j == k else sp.zeros(*sample.shape)
                    if sp.simplify(units[i, j] * units[k, ell] - target) != sp.zeros(*sample.shape):
                        failures.append(("product", i, j, k, ell))
    return {
        "dimension": d,
        "identities_checked": d**2 + d**4,
        "failures": failures,
        "passed": not failures,
    }


def central_projector(units: Mapping[Tuple[int, int], sp.Matrix], d: int) -> sp.Matrix:
    sample = next(iter(units.values()))
    P = sp.zeros(*sample.shape)
    for i in range(d):
        P += units[i, i]
    return sp.simplify(P)


if __name__ == "__main__":
    # A minimal exact regression fixture: G=C2, with its one-dimensional
    # sign representation and the regular representation. This validates
    # conventions and the code path, not the 2I data.
    e, s = "e", "s"
    elements = [e, s]
    U = {e: sp.eye(2), s: sp.Matrix([[0, 1], [1, 0]])}
    rho = {e: sp.Matrix([[1]]), s: sp.Matrix([[-1]])}
    E = matrix_units(elements, U, rho)
    report = verify_matrix_units(E, 1)
    assert report["passed"], report
    P = central_projector(E, 1)
    assert P == sp.Matrix([[sp.Rational(1, 2), -sp.Rational(1, 2)],
                           [-sp.Rational(1, 2), sp.Rational(1, 2)]])
    print({"fixture": "C2 sign representation", **report})
    print("NOTE: no 2I representation data were supplied; 2I audit not run.")
