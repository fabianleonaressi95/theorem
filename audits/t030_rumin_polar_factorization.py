#!/usr/bin/env python3
"""T030: exact polar-factorization audit for the T025 Rumin Gram block.

This constructs the positive square root of G=D^*D and its U(1)-phase
family. These are canonical algebraic representatives, NOT claimed to be
the geometric Rumin differential in a Kitaoka target basis.
"""
import argparse
import json
import sympy as sp


def block(p, q):
    if p < 1 or q < 1:
        raise ValueError("generic Case V requires p,q >= 1")
    A2 = sp.Rational(p * (q + 1), 2)
    B2 = sp.Rational(q * (p + 1), 2)
    A, B = sp.sqrt(A2), sp.sqrt(B2)
    L = 2*p*q + p + q
    S = A2 + B2
    Pplus = sp.simplify(sp.Matrix([[B2, -A*B], [-A*B, A2]]) / S)
    G = sp.simplify(sp.Rational(L*L, 4) * Pplus)
    D0 = sp.simplify(sp.Rational(L, 2) * Pplus)
    theta = sp.symbols("theta", real=True)
    phase = sp.exp(sp.I*theta)
    Dtheta = sp.simplify(phase * D0)

    assert sp.simplify(Pplus*Pplus - Pplus) == sp.zeros(2)
    assert sp.simplify(D0.H*D0 - G) == sp.zeros(2)
    assert sp.simplify(Dtheta.H*Dtheta - G) == sp.zeros(2)
    assert sp.simplify(D0*D0 - G) == sp.zeros(2)
    assert sp.simplify(G*G - sp.Rational(L*L, 4)*G) == sp.zeros(2)

    # A target-space rotation is another admissible polar isometry:
    # U(alpha,beta)=(cos(alpha), exp(i beta) sin(alpha))^T.
    alpha, beta = sp.symbols("alpha beta", real=True)
    u = sp.Matrix([sp.cos(alpha), sp.exp(sp.I*beta)*sp.sin(alpha)])
    Dtarget = sp.simplify(sp.Rational(L, 2) * u * sp.Matrix([[B, -A]]) / sp.sqrt(S))
    assert sp.simplify(u.H*u)[0] == 1
    assert sp.simplify(Dtarget.H*Dtarget - G) == sp.zeros(2)

    return {
        "p": p, "q": q, "L": L,
        "G_DdaggerD": [[str(G[i,j]) for j in range(2)] for i in range(2)],
        "canonical_positive_sqrt_D0": [[str(D0[i,j]) for j in range(2)] for i in range(2)],
        "phase_family_Dtheta": [[str(Dtheta[i,j]) for j in range(2)] for i in range(2)],
        "general_target_isometry_example": [[str(Dtarget[i,j]) for j in range(2)] for i in range(2)],
        "identities": {
            "projector_idempotence": True,
            "D0_adjoint_D0_equals_G": True,
            "phase_family_adjoint_product_equals_G": True,
            "target_isometry_adjoint_product_equals_G": True,
            "D0_squared_equals_G": True,
        },
        "interpretation": "Polar representatives only; no geometric target basis is asserted."
    }


def audit(max_index=20):
    if max_index < 1:
        raise ValueError("max_index must be >= 1")
    samples = []
    checked = 0
    for p in range(1, max_index+1):
        for q in range(1, max_index+1):
            item = block(p,q)
            checked += 1
            if (p,q) in ((1,1),(1,2),(2,1),(2,2),(max_index,max_index)):
                samples.append(item)
    return {
        "audit": "T030 exact polar factorization and target-gauge ambiguity",
        "max_index": max_index,
        "blocks_checked": checked,
        "all_polar_factorization_identities_passed": True,
        "sample_blocks": samples,
        "scope": [
            "D0 is the positive square root of the Gram matrix in an identified target copy.",
            "Multiplication by a unit-modulus phase leaves D*D unchanged.",
            "More generally any target isometric embedding gives the same Gram matrix.",
            "No member of this family is identified as the geometric Rumin differential without evaluating the contact differential in a fixed target basis."
        ]
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--max-index",type=int,default=20)
    parser.add_argument("--json",action="store_true")
    args=parser.parse_args()
    result=audit(args.max_index)
    if args.json:
        print(json.dumps(result,indent=2))
    else:
        print(result["audit"])
        print("blocks checked:",result["blocks_checked"])
        print("positive polar factorization: PASS")
        print("U(1) phase invariance: PASS")
        print("target-isometry invariance: PASS")
        print("geometric differential coefficients: NOT CLAIMED")


if __name__=="__main__":
    main()
