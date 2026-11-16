"""Exact quaternion model of the binary icosahedral group 2I over Q(sqrt(5)).

The implementation uses pairs (rational, rational) to represent a + b*phi,
where phi=(1+sqrt(5))/2 and phi**2=phi+1. No floating-point arithmetic is
used in group construction or the defining SU(2) representation.
"""
from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from fractions import Fraction
from typing import TypeAlias

import sympy as sp

Quadratic: TypeAlias = tuple[Fraction, Fraction]
Quaternion: TypeAlias = tuple[Quadratic, Quadratic, Quadratic, Quadratic]

ZERO: Quadratic = (Fraction(0), Fraction(0))
ONE: Quadratic = (Fraction(1), Fraction(0))
HALF: Quadratic = (Fraction(1, 2), Fraction(0))
PHI_HALF: Quadratic = (Fraction(0), Fraction(1, 2))
NEG_HALF_PLUS_PHI_HALF: Quadratic = (Fraction(-1, 2), Fraction(1, 2))

CLASS_SCALARS: tuple[Quadratic, ...] = (
    ONE,
    (-Fraction(1), Fraction(0)),
    (-HALF[0], Fraction(0)),
    ZERO,
    NEG_HALF_PLUS_PHI_HALF,
    (Fraction(0), Fraction(-1, 2)),
    HALF,
    PHI_HALF,
    (Fraction(1, 2), Fraction(-1, 2)),
)
CLASS_SIZES = (1, 1, 20, 30, 12, 12, 20, 12, 12)
CLASS_ORDERS = (1, 2, 3, 4, 5, 5, 6, 10, 10)


def quadratic_add(left: Quadratic, right: Quadratic) -> Quadratic:
    """Add a+b*phi and c+d*phi in Q(phi)."""
    return (left[0] + right[0], left[1] + right[1])


def quadratic_neg(value: Quadratic) -> Quadratic:
    """Return the additive inverse in Q(phi)."""
    return (-value[0], -value[1])


def quadratic_sub(left: Quadratic, right: Quadratic) -> Quadratic:
    """Subtract two elements of Q(phi)."""
    return quadratic_add(left, quadratic_neg(right))


def quadratic_mul(left: Quadratic, right: Quadratic) -> Quadratic:
    """Multiply in Q(phi), reducing phi**2 to phi+1."""
    rational_a, phi_a = left
    rational_b, phi_b = right
    return (
        rational_a * rational_b + phi_a * phi_b,
        rational_a * phi_b + phi_a * rational_b + phi_a * phi_b,
    )


def quaternion_mul(left: Quaternion, right: Quaternion) -> Quaternion:
    """Hamilton product, using scalar-first coordinates (a,b,c,d)."""
    a, b, c, d = left
    e, f, g, h = right
    return (
        quadratic_sub(
            quadratic_sub(
                quadratic_sub(quadratic_mul(a, e), quadratic_mul(b, f)),
                quadratic_mul(c, g),
            ),
            quadratic_mul(d, h),
        ),
        quadratic_sub(
            quadratic_add(
                quadratic_add(quadratic_mul(a, f), quadratic_mul(b, e)),
                quadratic_mul(c, h),
            ),
            quadratic_mul(d, g),
        ),
        quadratic_add(
            quadratic_sub(
                quadratic_add(quadratic_mul(a, g), quadratic_mul(c, e)),
                quadratic_mul(b, h),
            ),
            quadratic_mul(d, f),
        ),
        quadratic_add(
            quadratic_sub(
                quadratic_add(quadratic_mul(a, h), quadratic_mul(b, g)),
                quadratic_mul(c, f),
            ),
            quadratic_mul(d, e),
        ),
    )


def quaternion_conjugate(quaternion: Quaternion) -> Quaternion:
    """Quaternionic conjugate in scalar-first coordinates."""
    return (
        quaternion[0],
        quadratic_neg(quaternion[1]),
        quadratic_neg(quaternion[2]),
        quadratic_neg(quaternion[3]),
    )


def quaternion_norm_squared(quaternion: Quaternion) -> Quadratic:
    """Return the exact squared norm q*conjugate(q)."""
    norm_squared = ZERO
    for component in quaternion:
        norm_squared = quadratic_add(
            norm_squared, quadratic_mul(component, component)
        )
    return norm_squared


def _is_even_permutation(permutation: tuple[int, ...]) -> bool:
    """Return whether a permutation has even parity."""
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(4)
        for j in range(i + 1, 4)
    )
    return inversions % 2 == 0


def binary_icosahedral_elements() -> tuple[Quaternion, ...]:
    """Construct the 120 unit quaternions given by the 600-cell vertices."""
    coordinate_values = (ZERO, HALF, PHI_HALF, NEG_HALF_PLUS_PHI_HALF)
    elements: set[Quaternion] = set()

    # Even permutations of (0, ±1/2, ±phi/2, ±(phi-1)/2).
    for permutation in itertools.permutations(range(4)):
        if not _is_even_permutation(permutation):
            continue
        coordinates = [coordinate_values[index] for index in permutation]
        nonzero_positions = [
            index for index, value in enumerate(coordinates) if value != ZERO
        ]
        for signs in itertools.product((-1, 1), repeat=3):
            signed_coordinates = list(coordinates)
            for position, sign in zip(nonzero_positions, signs):
                if sign < 0:
                    signed_coordinates[position] = quadratic_neg(
                        signed_coordinates[position]
                    )
            elements.add(tuple(signed_coordinates))  # type: ignore[arg-type]

    # The eight signed coordinate units.
    for axis in range(4):
        for sign in (-1, 1):
            coordinates = [ZERO] * 4
            coordinates[axis] = ONE if sign > 0 else quadratic_neg(ONE)
            elements.add(tuple(coordinates))  # type: ignore[arg-type]

    # The sixteen half-coordinate vertices.
    for signs in itertools.product((-1, 1), repeat=4):
        elements.add(
            tuple(HALF if sign > 0 else quadratic_neg(HALF) for sign in signs)  # type: ignore[arg-type]
        )

    if len(elements) != 120:
        raise AssertionError(
            f"600-cell construction produced {len(elements)} elements; expected 120"
        )
    return tuple(sorted(elements))


def _sympy_quadratic(value: Quadratic) -> sp.Expr:
    """Convert an exact Q(phi) pair to a SymPy expression."""
    phi = (1 + sp.sqrt(5)) / 2
    return (
        sp.Rational(value[0].numerator, value[0].denominator)
        + sp.Rational(value[1].numerator, value[1].denominator) * phi
    )


def fundamental_su2_matrix(quaternion: Quaternion) -> sp.Matrix:
    """Map a scalar-first unit quaternion to its defining SU(2) matrix."""
    scalar, i_component, j_component, k_component = map(
        _sympy_quadratic, quaternion
    )
    imaginary_unit = sp.I
    return sp.Matrix(
        [
            [scalar + imaginary_unit * i_component,
             j_component + imaginary_unit * k_component],
            [-j_component + imaginary_unit * k_component,
             scalar - imaginary_unit * i_component],
        ]
    )


def multiplication_table(
    elements: tuple[Quaternion, ...],
) -> tuple[tuple[tuple[int, ...], ...], int, tuple[int, ...]]:
    """Build the exact Cayley table, identity index, and inverse indices."""
    element_indices = {element: index for index, element in enumerate(elements)}
    table: list[tuple[int, ...]] = []
    for left in elements:
        row = []
        for right in elements:
            product = quaternion_mul(left, right)
            if product not in element_indices:
                raise AssertionError(
                    "2I closure failed: a Hamilton product is absent "
                    "from the 600-cell vertex set"
                )
            row.append(element_indices[product])
        table.append(tuple(row))

    identity_index = element_indices[(ONE, ZERO, ZERO, ZERO)]
    inverse_indices = tuple(
        element_indices[quaternion_conjugate(element)] for element in elements
    )
    return tuple(table), identity_index, inverse_indices


def audit() -> dict:
    """Run exact group-law and defining-representation checks for 2I."""
    elements = binary_icosahedral_elements()
    table, identity_index, inverse_indices = multiplication_table(elements)

    for element_index in range(len(elements)):
        if (
            table[identity_index][element_index] != element_index
            or table[element_index][identity_index] != element_index
        ):
            raise AssertionError(f"Identity law failed at element index {element_index}")
        inverse_index = inverse_indices[element_index]
        if (
            table[element_index][inverse_index] != identity_index
            or table[inverse_index][element_index] != identity_index
        ):
            raise AssertionError(f"Inverse law failed at element index {element_index}")
        if quaternion_norm_squared(elements[element_index]) != ONE:
            raise AssertionError(
                f"Unit-norm check failed at element index {element_index}"
            )

    scalar_multiplicities = Counter(element[0] for element in elements)
    observed_class_sizes = tuple(
        scalar_multiplicities.get(scalar, 0) for scalar in CLASS_SCALARS
    )
    if observed_class_sizes != CLASS_SIZES:
        raise AssertionError(
            f"Conjugacy-class scalar counts {observed_class_sizes} "
            f"do not match expected counts {CLASS_SIZES}"
        )

    phi = (1 + sp.sqrt(5)) / 2
    expected_fundamental_character = (
        2, -2, -1, 0, phi - 1, -phi, 1, phi, 1 - phi
    )
    for class_index, scalar in enumerate(CLASS_SCALARS):
        observed_character = 2 * _sympy_quadratic(scalar)
        if sp.simplify(
            observed_character - expected_fundamental_character[class_index]
        ) != 0:
            raise AssertionError(
                f"Defining character mismatch in conjugacy class {class_index}"
            )

    for element_index, element in enumerate(elements):
        matrix = fundamental_su2_matrix(element)
        if sp.simplify(matrix.det() - 1) != 0:
            raise AssertionError(
                f"SU(2) determinant check failed at element index {element_index}"
            )
        if sp.simplify(matrix.conjugate().T * matrix - sp.eye(2)) != sp.zeros(2):
            raise AssertionError(
                f"SU(2) unitarity check failed at element index {element_index}"
            )

    probe_indices = (identity_index, 0, len(elements) - 1)
    for left_index in probe_indices:
        for right_index in probe_indices:
            product = quaternion_mul(
                elements[left_index], elements[right_index]
            )
            if sp.simplify(
                fundamental_su2_matrix(product)
                - fundamental_su2_matrix(elements[left_index])
                * fundamental_su2_matrix(elements[right_index])
            ) != sp.zeros(2):
                raise AssertionError(
                    "Defining SU(2) map failed multiplicativity on probe pair "
                    f"({left_index}, {right_index})"
                )

    return {
        "passed": True,
        "group": "2I",
        "order": len(elements),
        "field": "Q(sqrt(5))",
        "construction": "600-cell unit quaternions",
        "closure_products_checked": len(elements) ** 2,
        "unit_norms_checked": len(elements),
        "identity_inverse_checks": 2 * len(elements),
        "fundamental_su2_determinants_checked": len(elements),
        "fundamental_su2_unitarity_checked": len(elements),
        "class_sizes": observed_class_sizes,
        "class_orders": CLASS_ORDERS,
        "fundamental_character": [
            str(sp.simplify(2 * _sympy_quadratic(scalar)))
            for scalar in CLASS_SCALARS
        ],
        "scope": (
            "Exact group construction and defining 2D representation only; "
            "the remaining eight irreducible matrix models are not established here."
        ),
    }


def main() -> None:
    """Command-line entry point for the exact 2I audit."""
    parser = argparse.ArgumentParser(
        description="Audit the binary icosahedral group 2I exactly over Q(sqrt(5))."
    )
    parser.add_argument("--output", default=None, help="Optional JSON report path.")
    arguments = parser.parse_args()
    report = audit()
    serialized_report = json.dumps(report, indent=2)
    if arguments.output:
        from pathlib import Path

        output_path = Path(arguments.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(serialized_report + "\n", encoding="utf-8")
    print(serialized_report)


if __name__ == "__main__":
    main()
