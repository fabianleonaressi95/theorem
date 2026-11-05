#!/usr/bin/env python3
"""Exact matrix-unit audit for finite-group representations.

Callers provide an exact group multiplication table, exact unitary matrices
U(g), and exact irreducible matrices rho(g). The routine checks the chosen
left-representation convention; it does not reconstruct character data.
Requires SymPy.
"""
from __future__ import annotations

from typing import Dict, Hashable, Mapping, Sequence, Tuple

import sympy as sp


def adjoint(matrix: sp.Matrix) -> sp.Matrix:
    """Return the Hermitian adjoint of a matrix."""
    return matrix.conjugate().T


def matrix_units(
    elements: Sequence[Hashable],
    representation: Mapping[Hashable, sp.Matrix],
    irrep: Mapping[Hashable, sp.Matrix],
) -> Dict[Tuple[int, int], sp.Matrix]:
    """Return E_ij = d/|G| sum_g conjugate(rho(g)_ij) U(g).

    Raises:
        ValueError: if the group list or either representation is empty,
            if matrix dimensions are inconsistent, or if group labels differ.
    """
    if not elements:
        raise ValueError(
            "Cannot construct matrix units: the group element sequence is empty."
        )
    if not representation:
        raise ValueError(
            "Cannot construct matrix units: the ambient representation is empty."
        )
    if not irrep:
        raise ValueError(
            "Cannot construct matrix units: the irreducible representation is empty."
        )

    first_irrep_matrix = next(iter(irrep.values()))
    irrep_dimension = first_irrep_matrix.rows
    if first_irrep_matrix.cols != irrep_dimension or irrep_dimension == 0:
        raise ValueError(
            "Invalid irreducible representation matrix: expected a non-empty "
            f"square matrix, received shape {first_irrep_matrix.shape}."
        )
    for element, matrix in irrep.items():
        if matrix.shape != (irrep_dimension, irrep_dimension):
            raise ValueError(
                "Inconsistent irreducible representation dimension at group "
                f"element {element!r}: expected {(irrep_dimension, irrep_dimension)}, "
                f"received {matrix.shape}."
            )

    first_ambient_matrix = next(iter(representation.values()))
    ambient_dimension = first_ambient_matrix.rows
    if (
        first_ambient_matrix.cols != ambient_dimension
        or ambient_dimension == 0
    ):
        raise ValueError(
            "Invalid ambient representation matrix: expected a non-empty "
            f"square matrix, received shape {first_ambient_matrix.shape}."
        )
    for element, matrix in representation.items():
        if matrix.shape != (ambient_dimension, ambient_dimension):
            raise ValueError(
                "Inconsistent ambient representation dimension at group "
                f"element {element!r}: expected {(ambient_dimension, ambient_dimension)}, "
                f"received {matrix.shape}."
            )

    group_labels = set(elements)
    if len(group_labels) != len(elements):
        raise ValueError(
            "The group element sequence contains duplicate labels; each group "
            "element must occur exactly once."
        )
    ambient_labels = set(representation)
    irrep_labels = set(irrep)
    if group_labels != ambient_labels or group_labels != irrep_labels:
        missing_ambient = group_labels - ambient_labels
        extra_ambient = ambient_labels - group_labels
        missing_irrep = group_labels - irrep_labels
        extra_irrep = irrep_labels - group_labels
        raise ValueError(
            "Group labels do not match representation keys: "
            f"missing ambient={sorted(map(repr, missing_ambient))}, "
            f"extra ambient={sorted(map(repr, extra_ambient))}, "
            f"missing irrep={sorted(map(repr, missing_irrep))}, "
            f"extra irrep={sorted(map(repr, extra_irrep))}."
        )

    matrix_units_by_indices: Dict[Tuple[int, int], sp.Matrix] = {}
    for row_index in range(irrep_dimension):
        for column_index in range(irrep_dimension):
            unit_matrix = sp.zeros(ambient_dimension, ambient_dimension)
            for element in elements:
                unit_matrix += (
                    sp.conjugate(irrep[element][row_index, column_index])
                    * representation[element]
                )
            matrix_units_by_indices[(row_index, column_index)] = sp.simplify(
                sp.Rational(irrep_dimension, len(elements)) * unit_matrix
            )
    return matrix_units_by_indices


def verify_matrix_units(
    units: Mapping[Tuple[int, int], sp.Matrix],
    dimension: int,
) -> dict:
    """Verify E_ij E_kl = delta_jk E_il and E_ij*=E_ji exactly."""
    if dimension < 1:
        raise ValueError(
            f"Matrix-unit dimension must be positive; received {dimension}."
        )
    if not units:
        raise ValueError("Cannot verify matrix units: no units were supplied.")

    expected_indices = {
        (row_index, column_index)
        for row_index in range(dimension)
        for column_index in range(dimension)
    }
    supplied_indices = set(units)
    if supplied_indices != expected_indices:
        missing = sorted(expected_indices - supplied_indices)
        extra = sorted(supplied_indices - expected_indices)
        raise ValueError(
            "Matrix-unit index set is incomplete or contains unexpected entries: "
            f"missing={missing}, extra={extra}."
        )

    sample_matrix = units[(0, 0)]
    if sample_matrix.rows != sample_matrix.cols:
        raise ValueError(
            "Matrix units must be square; "
            f"the (0, 0) unit has shape {sample_matrix.shape}."
        )
    ambient_shape = sample_matrix.shape
    for index, matrix in units.items():
        if matrix.shape != ambient_shape:
            raise ValueError(
                f"Matrix unit {index} has shape {matrix.shape}; "
                f"expected {ambient_shape}."
            )

    failures = []
    for row_index in range(dimension):
        for column_index in range(dimension):
            if adjoint(units[(row_index, column_index)]) != units[
                (column_index, row_index)
            ]:
                failures.append(("adjoint", row_index, column_index))
            for next_row in range(dimension):
                for next_column in range(dimension):
                    target = (
                        units[(row_index, next_column)]
                        if column_index == next_row
                        else sp.zeros(*ambient_shape)
                    )
                    product_residual = (
                        units[(row_index, column_index)]
                        * units[(next_row, next_column)]
                        - target
                    )
                    if sp.simplify(product_residual) != sp.zeros(*ambient_shape):
                        failures.append(
                            (
                                "product",
                                row_index,
                                column_index,
                                next_row,
                                next_column,
                            )
                        )
    return {
        "dimension": dimension,
        "identities_checked": dimension**2 + dimension**4,
        "failures": failures,
        "passed": not failures,
    }


def central_projector(
    units: Mapping[Tuple[int, int], sp.Matrix],
    dimension: int,
) -> sp.Matrix:
    """Return the isotypic projector as the sum of diagonal matrix units."""
    if dimension < 1:
        raise ValueError(
            f"Projector dimension must be positive; received {dimension}."
        )
    if not units:
        raise ValueError(
            "Cannot form the central projector: no matrix units were supplied."
        )
    expected_diagonal = {(index, index) for index in range(dimension)}
    missing_diagonal = expected_diagonal - set(units)
    if missing_diagonal:
        raise ValueError(
            "Cannot form the central projector: missing diagonal matrix units "
            f"{sorted(missing_diagonal)}."
        )

    sample_matrix = units[(0, 0)]
    projector = sp.zeros(*sample_matrix.shape)
    for index in range(dimension):
        projector += units[(index, index)]
    return sp.simplify(projector)


if __name__ == "__main__":
    # A minimal exact regression fixture: G=C2, with its one-dimensional
    # sign representation and the regular representation.
    identity, reflection = "e", "s"
    group_elements = [identity, reflection]
    ambient_representation = {
        identity: sp.eye(2),
        reflection: sp.Matrix([[0, 1], [1, 0]]),
    }
    sign_representation = {
        identity: sp.Matrix([[1]]),
        reflection: sp.Matrix([[-1]]),
    }
    units = matrix_units(
        group_elements, ambient_representation, sign_representation
    )
    report = verify_matrix_units(units, 1)
    assert report["passed"], report
    projector = central_projector(units, 1)
    expected_projector = sp.Matrix(
        [
            [sp.Rational(1, 2), -sp.Rational(1, 2)],
            [-sp.Rational(1, 2), sp.Rational(1, 2)],
        ]
    )
    assert projector == expected_projector
    print({"fixture": "C2 sign representation", **report})
    print("NOTE: no 2I representation data were supplied; 2I audit not run.")
