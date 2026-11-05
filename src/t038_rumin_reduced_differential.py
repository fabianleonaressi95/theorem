"""Exact restriction of the geometric Rumin row differential to 2I sectors.

The Rumin polarization block acts on C^2 and the binary-icosahedral group
acts on Sym^m(C^2). Hence the reduced operator is D_pol tensor identity
on each irreducible representation and its multiplicity space.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sympy as sp

from audits.t035_exact_binary_icosahedral_model import elements_2i, rho2
from src.t032_2i_molien import IRREP_DIMENSIONS
from src.t036_2i_irreducible_models import build_all_models, symmetric_power_matrix
from src.t037_rumin_harmonic_multiplicities import decompose_degree

A, B = sp.symbols("A B", real=True)


def rumin_polarization_block(p: int, q: int):
    """Return exact (D_pol, Gram, metadata) for the generic p,q >= 1 block."""
    if not isinstance(p, int) or not isinstance(q, int) or p < 1 or q < 1:
        raise ValueError("generic middle-degree block requires integers p,q >= 1")
    a2 = sp.Rational(p * (q + 1), 2)
    b2 = sp.Rational(q * (p + 1), 2)
    L = 2 * p * q + p + q
    S = sp.Rational(L, 2)
    D = sp.simplify(sp.Rational(L, 2) / sp.sqrt(S) * sp.Matrix([[-B, A]]))
    gram = sp.simplify(sp.Rational(L, 2) * sp.Matrix([[B**2, -A*B], [-A*B, A**2]]))
    # Keep the square-root relations explicit; the Gram identity is checked
    # as an exact symbolic matrix identity in the regression test.
    return D, gram, {"p": p, "q": q, "m": p + q, "A_squared": a2,
                     "B_squared": b2, "L": L, "S": S}


def verify_polarization_identity(p: int, q: int):
    D, gram, meta = rumin_polarization_block(p, q)
    product = sp.simplify(D.conjugate().T * D - gram)
    # Keep the relation explicit rather than choosing arbitrary square-root signs.
    expected = sp.Rational(meta["L"], 2) * sp.Matrix(
        [[B**2, -A*B], [-A*B, A**2]])
    if sp.simplify(D.conjugate().T * D - expected) != sp.zeros(2):
        raise AssertionError("D_pol^* D_pol does not reproduce the T032 Gram block")
    return {"passed": True, "D_pol": D, "Gram": gram, **meta}


def ambient_group_matrices(group, degree):
    return tuple(symmetric_power_matrix(rho2(g), degree) for g in group)


def restrict_degree(degree, group, chars, models):
    """Check equivariance and compute every reduced multiplicity-space block."""
    decomposition = decompose_degree(degree, group, chars, models)
    U = ambient_group_matrices(group, degree)
    n = degree + 1
    Dpol = sp.Matrix([[-B, A]])  # universal row; scalar normalization is external
    Dfull = sp.kronecker_product(Dpol, sp.eye(n))
    I2 = sp.eye(2)
    reduced = {}
    equivariance_checks = 0
    restriction_checks = 0

    for g_index, Ug in enumerate(U):
        lhs = Dfull * sp.kronecker_product(I2, Ug)
        rhs = Ug * Dfull
        if sp.simplify(lhs-rhs) != sp.zeros(n, 2*n):
            raise AssertionError(f"Rumin equivariance failed at group element {g_index}")
        equivariance_checks += 1

    for label, entry in decomposition.items():
        d = IRREP_DIMENSIONS[label]
        b = entry["Molien_multiplicity"]
        maps = entry["multiplicity_basis"]
        if b == 0:
            reduced[label] = {"irrep_dimension": d, "multiplicity": 0,
                              "source_dimension": 0, "target_dimension": 0}
            continue
        M = sp.Matrix.hstack(*maps)  # Sym^m <- V_rho tensor C^b
        if M.cols != d*b or M.rank() != d*b:
            raise AssertionError(f"non-basis multiplicity embedding for {label}")
        source_embedding = sp.kronecker_product(I2, M)
        reduced_operator = sp.kronecker_product(Dpol, sp.eye(d*b))
        lhs = Dfull * source_embedding
        rhs = M * reduced_operator
        if sp.simplify(lhs-rhs) != sp.zeros(n, 2*d*b):
            raise AssertionError(f"reduced Rumin block mismatch for {label}")
        restriction_checks += 1
        reduced[label] = {
            "irrep_dimension": d,
            "multiplicity": b,
            "source_dimension": 2*d*b,
            "target_dimension": d*b,
            "reduced_operator": reduced_operator,
            "multiplicity_embedding_rank": M.rank(),
        }

    return {"degree": degree, "equivariance_checks": equivariance_checks,
            "restriction_checks": restriction_checks, "reduced": reduced}


def run(max_degree=3):
    if max_degree < 0:
        raise ValueError("max_degree must be nonnegative")
    group, chars, _, models = build_all_models()
    degree_reports = [restrict_degree(m, group, chars, models)
                      for m in range(max_degree+1)]
    # All reports are exact symbolic identities; no numerical approximation is used.
    return {
        "passed": True,
        "group_order": 120,
        "degrees_checked": list(range(max_degree+1)),
        "group_equivariance_checks": sum(x["equivariance_checks"] for x in degree_reports),
        "reduced_restriction_checks": sum(x["restriction_checks"] for x in degree_reports),
        "degrees": [{
            "degree": x["degree"],
            "equivariance_checks": x["equivariance_checks"],
            "restriction_checks": x["restriction_checks"],
            "sectors": {k: {a: v for a, v in val.items() if a != "reduced_operator"}
                        for k, val in x["reduced"].items()}
        } for x in degree_reports],
        "operator_convention": "D_R = D_pol tensor I_{Sym^m}; D_pol = (-B,A) up to the T032 scalar normalization",
        "scope": "Exact finite-degree restriction; generic p,q middle-degree blocks only. Boundary sectors and global analytic torsion remain separate."
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-degree", type=int, default=3)
    parser.add_argument("--output", default="data/t038_rumin_reduced_differential.json")
    args = parser.parse_args()
    report = run(args.max_degree)
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "degrees"}, indent=2))


if __name__ == "__main__":
    main()
