"""Exact matrix realization of T124 from the T121 signed-axis action.

Run from repository root: python audits/t124_mixed_tensor_character_check.py
All calculations use exact SymPy arithmetic over Q(sqrt(5)).
"""
import sympy as sp
from audits.t121_q6_a5_three_plus_three_prime import build_audit


def main():
    source = build_audit()
    actions = [sp.Matrix(g) for g in source["signed_actions"]]
    class_data = source["class_of_action"]
    names = ("identity", "order_2", "order_3", "order_5_phi",
             "order_5_phi_conjugate")
    p3 = sp.Matrix(source["projectors"]["P3"])
    p3p = sp.Matrix(source["projectors"]["P3_prime"])
    c3 = sp.Matrix.hstack(*p3.columnspace())
    c3p = sp.Matrix.hstack(*p3p.columnspace())
    assert c3.shape == (6, 3) and c3p.shape == (6, 3)
    l3 = (c3.T * c3).inv() * c3.T
    l3p = (c3p.T * c3p).inv() * c3p.T
    d3 = [(l3 * g * c3).applyfunc(sp.simplify) for g in actions]
    d3p = [(l3p * g * c3p).applyfunc(sp.simplify) for g in actions]

    for g, a, b in zip(actions, d3, d3p):
        assert g * c3 == c3 * a
        assert g * c3p == c3p * b
        assert a.det() == 1 and b.det() == 1

    action_index = {tuple(g): i for i, g in enumerate(actions)}
    for i, gi in enumerate(actions):
        for j, gj in enumerate(actions):
            k = action_index[tuple(gi * gj)]
            assert d3[i] * d3[j] == d3[k]
            assert d3p[i] * d3p[j] == d3p[k]

    tensor = [sp.kronecker_product(a, b) for a, b in zip(d3, d3p)]
    chi4 = {"identity": 4, "order_2": 0, "order_3": 1,
            "order_5_phi": -1, "order_5_phi_conjugate": -1}
    chi5 = {"identity": 5, "order_2": 1, "order_3": -1,
            "order_5_phi": 0, "order_5_phi_conjugate": 0}
    p4, p5 = sp.zeros(9), sp.zeros(9)
    for name in names:
        for i in class_data[name]:
            p4 += sp.Rational(4, 60) * chi4[name] * tensor[i]
            p5 += sp.Rational(5, 60) * chi5[name] * tensor[i]
    p4, p5 = p4.applyfunc(sp.simplify), p5.applyfunc(sp.simplify)
    eye = sp.eye(9)
    class_representatives = tuple(class_data[n][0] for n in names)
    tensor_character = tuple(sp.simplify(sp.trace(tensor[i]))
                             for i in class_representatives)
    checks = {
        "basis_dimensions_3_and_3prime": c3.shape == (6, 3) and c3p.shape == (6, 3),
        "restricted_actions_invariant": all(g*c3 == c3*a and g*c3p == c3p*b
                                             for g,a,b in zip(actions,d3,d3p)),
        "D3_representation_law": all(d3[i]*d3[j] == d3[action_index[tuple(actions[i]*actions[j])]]
                                      for i in range(60) for j in range(60)),
        "D3prime_representation_law": all(d3p[i]*d3p[j] == d3p[action_index[tuple(actions[i]*actions[j])]]
                                          for i in range(60) for j in range(60)),
        "P4_idempotent": p4*p4 == p4,
        "P5_idempotent": p5*p5 == p5,
        "P4_P5_orthogonal": p4*p5 == sp.zeros(9),
        "projectors_sum_identity": p4+p5 == eye,
        "ranks_4_and_5": p4.rank() == 4 and p5.rank() == 5,
        "centrality_all_60": all(p4*t == t*p4 and p5*t == t*p5 for t in tensor),
        "tensor_character": tensor_character == (9,1,0,-1,-1),
    }
    if not all(checks.values()):
        raise AssertionError([k for k,v in checks.items() if not v])
    print({
        "audit": "T124_EXACT_MATRIX_3_TENSOR_3PRIME_4_PLUS_5",
        "field": "Q(sqrt(5))",
        "basis_3": c3.tolist(), "basis_3prime": c3p.tolist(),
        "restricted_D3": [m.tolist() for m in d3],
        "restricted_D3prime": [m.tolist() for m in d3p],
        "P4": p4.tolist(), "P5": p5.tolist(),
        "ranks": [p4.rank(), p5.rank()],
        "checks": checks, "all_exact_checks_passed": all(checks.values()),
    })


if __name__ == "__main__":
    main()
