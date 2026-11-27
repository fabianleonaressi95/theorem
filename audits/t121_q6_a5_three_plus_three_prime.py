"""Exact reconstruction of the signed-axis A5 action on the six icosahedral axes.

All group and projector checks are exact over Q(sqrt(5)); SymPy is required.
Run: python audits/t121_q6_a5_three_plus_three_prime.py
"""
from __future__ import annotations

import itertools
import json
import sympy as sp


def build_audit() -> dict:
    sqrt5 = sp.sqrt(5)
    phi = (1 + sqrt5) / 2
    phi_conj = (1 - sqrt5) / 2

    # Twelve vertices of a regular icosahedron, in three cyclic families.
    vertices = []
    for s1, s2 in itertools.product((1, -1), repeat=2):
        vertices.extend(
            ((0, s1, s2 * phi), (s1, s2 * phi, 0), (s2 * phi, 0, s1))
        )
    vertices = tuple(dict.fromkeys(tuple(map(sp.simplify, v)) for v in vertices))
    vertex_set = set(vertices)
    if len(vertices) != 12:
        raise ArithmeticError("icosahedron must have exactly 12 vertices")

    # Six chosen representatives of the six antipodal axes. This ordering
    # fixes the signed-permutation basis used by the Q6 coordinates.
    axes = tuple(
        sp.Matrix(v)
        for v in (
            (0, 1, phi),
            (1, phi, 0),
            (phi, 0, 1),
            (0, 1, -phi),
            (1, -phi, 0),
            (phi, 0, -1),
        )
    )
    if len({frozenset((tuple(a), tuple(-a))) for a in axes}) != 6:
        raise ArithmeticError("axis representatives are not six distinct antipodal pairs")
    if any(tuple(a) not in vertex_set for a in axes):
        raise ArithmeticError("an axis representative is not an icosahedron vertex")

    # An orientation-preserving orthogonal map is determined by the images
    # of a linearly independent ordered vertex triple. Enumerate exactly the
    # triples with the same Gram matrix and retain those preserving all 12
    # vertices. This constructs SO(3) symmetry matrices over Q(sqrt(5)).
    source = sp.Matrix.hstack(*(sp.Matrix(v) for v in vertices[:3]))
    if sp.simplify(source.det()) == 0:
        raise ArithmeticError("chosen source triple is dependent")
    dot = [
        [sp.simplify(sp.Matrix(a).dot(sp.Matrix(b))) for b in vertices]
        for a in vertices
    ]
    rotations = {}
    pairs = ((0, 1), (0, 2), (1, 2))
    for image_indices in itertools.permutations(range(12), 3):
        if any(
            dot[i][j] != dot[image_indices[i]][image_indices[j]]
            for i, j in pairs
        ):
            continue
        target = sp.Matrix.hstack(*(sp.Matrix(vertices[i]) for i in image_indices))
        rotation = (target * source.inv()).applyfunc(sp.simplify)
        if sp.simplify(rotation.det() - 1) != 0:
            continue
        if any(
            tuple(sp.simplify(x) for x in rotation * sp.Matrix(v)) not in vertex_set
            for v in vertices
        ):
            continue
        rotations[image_indices] = rotation

    if len(rotations) != 60:
        raise ArithmeticError(f"expected 60 proper rotations, got {len(rotations)}")

    # Induce each rotation on the six oriented representatives, recording
    # the sign needed when the image is the negative representative.
    signed_actions = {}
    for rotation in rotations.values():
        action = sp.zeros(6)
        for column, axis in enumerate(axes):
            image = (rotation * axis).applyfunc(sp.simplify)
            matches = [
                (row, sign)
                for row, representative in enumerate(axes)
                for sign in (1, -1)
                if image == sign * representative
            ]
            if len(matches) != 1:
                raise ArithmeticError("rotation failed to permute the six signed axes")
            row, sign = matches[0]
            action[row, column] = sign
        signed_actions[tuple(action)] = action

    actions = tuple(signed_actions.values())
    action_keys = set(signed_actions)
    if len(actions) != 60:
        raise ArithmeticError("signed-axis action is not faithful/order 60")
    identity = sp.eye(6)
    for action in actions:
        if action.T * action != identity:
            raise ArithmeticError("signed action is not orthogonal")
    for left in actions:
        for right in actions:
            if tuple(left * right) not in action_keys:
                raise ArithmeticError("signed actions are not closed under multiplication")

    # Retain the unique SO(3) rotation corresponding to each signed action.
    rotation_by_action = {}
    for rotation in rotations.values():
        action = sp.zeros(6)
        for column, axis in enumerate(axes):
            image = (rotation * axis).applyfunc(sp.simplify)
            for row, representative in enumerate(axes):
                if image == representative:
                    action[row, column] = 1
                    break
                if image == -representative:
                    action[row, column] = -1
                    break
        rotation_by_action[tuple(action)] = rotation

    # Conjugacy classes are identified by SO(3) trace. The order-5 classes
    # split according to the two golden-ratio trace values.
    class_data = {
        "identity": [],
        "order_2": [],
        "order_3": [],
        "order_5_phi": [],
        "order_5_phi_conjugate": [],
    }
    for action in actions:
        rotation = rotation_by_action[tuple(action)]
        tr = sp.simplify(sp.trace(rotation))
        if action == identity:
            class_data["identity"].append(action)
        elif tr == -1:
            class_data["order_2"].append(action)
        elif tr == 0:
            class_data["order_3"].append(action)
        elif tr == phi:
            class_data["order_5_phi"].append(action)
        elif tr == phi_conj:
            class_data["order_5_phi_conjugate"].append(action)
        else:
            raise ArithmeticError(f"unexpected icosahedral rotation trace {tr}")

    expected_sizes = (1, 15, 20, 12, 12)
    if tuple(len(class_data[k]) for k in class_data) != expected_sizes:
        raise ArithmeticError("A5 conjugacy class sizes do not match (1,15,20,12,12)")

    # Central character projectors. A5 characters are real, so chi(g^-1)=chi(g).
    chi3 = {
        "identity": 3,
        "order_2": -1,
        "order_3": 0,
        "order_5_phi": phi,
        "order_5_phi_conjugate": phi_conj,
    }
    chi3p = {
        "identity": 3,
        "order_2": -1,
        "order_3": 0,
        "order_5_phi": phi_conj,
        "order_5_phi_conjugate": phi,
    }
    p3 = sp.zeros(6)
    p3p = sp.zeros(6)
    for name, elements in class_data.items():
        for action in elements:
            p3 += sp.Rational(3, 60) * chi3[name] * action
            p3p += sp.Rational(3, 60) * chi3p[name] * action
    p3 = p3.applyfunc(sp.simplify)
    p3p = p3p.applyfunc(sp.simplify)

    # Independently check the compact closed forms recorded in the theorem.
    b = sp.simplify((10 / sqrt5) * (p3 - sp.Rational(1, 2) * identity))
    b_expected = sp.Matrix(
        [
            [0, 1, 1, -1, -1, -1],
            [1, 0, 1, 1, -1, 1],
            [1, 1, 0, -1, 1, 1],
            [-1, 1, -1, 0, -1, 1],
            [-1, -1, 1, -1, 0, 1],
            [-1, 1, 1, 1, 1, 0],
        ]
    )
    checks = {
        "P3_idempotent": p3 * p3 == p3,
        "P3prime_idempotent": p3p * p3p == p3p,
        "mutually_orthogonal": p3 * p3p == sp.zeros(6),
        "sum_identity": p3 + p3p == identity,
        "ranks_3_and_3": p3.rank() == 3 and p3p.rank() == 3,
        "commute_with_all_60_actions": all(
            p3 * g == g * p3 and p3p * g == g * p3p for g in actions
        ),
        "B_squared_5I": b * b == 5 * identity,
        "B_matches_explicit_matrix": b == b_expected,
        "P3_closed_form": p3 == sp.Rational(1, 2) * identity + sqrt5 / 10 * b_expected,
        "P3prime_closed_form": p3p == sp.Rational(1, 2) * identity - sqrt5 / 10 * b_expected,
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise ArithmeticError(f"projector checks failed: {failed}")

    restricted_characters = {}
    for name, elements in class_data.items():
        g = elements[0]
        restricted_characters[name] = {
            "3": sp.simplify(sp.trace(p3 * g)),
            "3_prime": sp.simplify(sp.trace(p3p * g)),
        }

    expected_characters = {
        "identity": {"3": 3, "3_prime": 3},
        "order_2": {"3": -1, "3_prime": -1},
        "order_3": {"3": 0, "3_prime": 0},
        "order_5_phi": {"3": phi, "3_prime": phi_conj},
        "order_5_phi_conjugate": {"3": phi_conj, "3_prime": phi},
    }
    checks["restricted_characters"] = restricted_characters == expected_characters
    if not checks["restricted_characters"]:
        raise ArithmeticError("restricted characters do not match 3 and 3'")

    return {
        "audit": "T121_Q6_A5_GEOMETRIC_3_PLUS_3_PRIME_EXACT",
        "arithmetic": "exact SymPy arithmetic over Q(sqrt(5)); no floating point",
        "icosahedron": {"vertices": len(vertices), "antipodal_axes": len(axes)},
        "group": {
            "proper_rotations": len(rotations),
            "distinct_signed_actions": len(actions),
            "class_sizes": {k: len(v) for k, v in class_data.items()},
            "six_dimensional_character": [6, -2, 0, 1, 1],
        },
        "projectors": {
            "P3": p3.tolist(),
            "P3_prime": p3p.tolist(),
            "B": b_expected.tolist(),
            "ranks": [p3.rank(), p3p.rank()],
            "restricted_characters": restricted_characters,
        },
        "checks": checks,
        "all_exact_checks_passed": all(checks.values()),
        # Stable exact data interface for downstream representation audits.
        "signed_actions": [g.tolist() for g in actions],
        "class_of_action": {
            name: [actions.index(g) for g in elements]
            for name, elements in class_data.items()
        },
    }


if __name__ == "__main__":
    print(json.dumps(build_audit(), indent=2, default=str, sort_keys=True))
