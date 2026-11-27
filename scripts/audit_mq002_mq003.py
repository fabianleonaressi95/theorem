#!/usr/bin/env python3
"""Reproducible finite-dimensional audit for MQ-002 and MQ-003.

Requires NumPy. Uses the standard computational basis and spin-1/2 generators.
The exact theorem statements are in the corresponding theorem Markdown files.
"""
from __future__ import annotations

import json
import numpy as np

I2 = np.eye(2, dtype=complex)
JX = np.array([[0, 1], [1, 0]], dtype=complex) / 2
JY = np.array([[0, -1j], [1j, 0]], dtype=complex) / 2
JZ = np.diag([1, -1]).astype(complex) / 2
GENERATORS = (JX, JY, JZ)


def kron_all(items):
    out = items[0]
    for item in items[1:]:
        out = np.kron(out, item)
    return out


def intertwiner_basis():
    singlet = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)
    triplet_plus = np.array([1, 0, 0, 0], dtype=complex)
    triplet_zero = np.array([0, 1, 1, 0], dtype=complex) / np.sqrt(2)
    triplet_minus = np.array([0, 0, 0, 1], dtype=complex)
    basis_0 = np.kron(singlet, singlet)
    basis_1 = (
        np.kron(triplet_plus, triplet_minus)
        - np.kron(triplet_zero, triplet_zero)
        + np.kron(triplet_minus, triplet_plus)
    ) / np.sqrt(3)
    return np.column_stack((basis_0, basis_1))


def total_generator(generator, nlegs):
    return sum(
        (kron_all([generator if k == leg else I2 for k in range(nlegs)])
         for leg in range(nlegs)),
        start=np.zeros((2**nlegs, 2**nlegs), dtype=complex),
    )


def pair_flux_matrix(basis, i, j):
    operator = np.zeros((16, 16), dtype=complex)
    for generator in GENERATORS:
        factors = [I2] * 4
        factors[i] = generator
        factors[j] = generator
        operator += kron_all(factors)
    return basis.conj().T @ operator @ basis


def glue_one_fundamental_leg(state_a, state_b):
    """Glue leg 4 of A to leg 1 of B using the normalized SU(2) singlet."""
    epsilon = np.array([[0, 1], [-1, 0]], dtype=complex) / np.sqrt(2)
    tensor_a = state_a.reshape((2, 2, 2, 2))
    tensor_b = state_b.reshape((2, 2, 2, 2))
    # Output order: A legs 1,2,3 followed by B legs 2,3,4.
    return np.einsum("abcx,xy,ydef->abcdef",
                     tensor_a, epsilon, tensor_b, optimize=True).reshape(-1)


def run_audit():
    basis = intertwiner_basis()
    orthogonality_residual = float(np.linalg.norm(basis.conj().T @ basis - np.eye(2)))
    invariance_residuals = [
        float(np.linalg.norm(total_generator(g, 4) @ basis))
        for g in GENERATORS
    ]

    expected = {
        (0, 1): np.diag([-0.75, 0.25]),
        (2, 3): np.diag([-0.75, 0.25]),
        (0, 2): np.array([[0, -np.sqrt(3)/4], [-np.sqrt(3)/4, -0.5]]),
        (1, 3): np.array([[0, -np.sqrt(3)/4], [-np.sqrt(3)/4, -0.5]]),
        (0, 3): np.array([[0, np.sqrt(3)/4], [np.sqrt(3)/4, -0.5]]),
        (1, 2): np.array([[0, np.sqrt(3)/4], [np.sqrt(3)/4, -0.5]]),
    }
    pair_residuals = {}
    matrices = {}
    for pair, target in expected.items():
        matrix = pair_flux_matrix(basis, *pair)
        key = f"{pair[0]+1}{pair[1]+1}"
        matrices[key] = np.real_if_close(matrix).tolist()
        pair_residuals[key] = float(np.linalg.norm(matrix - target))

    closure_residuals = []
    for leg in range(4):
        total = sum(
            (pair_flux_matrix(basis, min(leg, other), max(leg, other))
             for other in range(4) if other != leg),
            start=np.zeros((2, 2), dtype=complex),
        )
        closure_residuals.append(float(np.linalg.norm(total + 0.75*np.eye(2))))

    gluing_norms = []
    gluing_invariance_residuals = []
    for a in range(2):
        for b in range(2):
            glued = glue_one_fundamental_leg(basis[:, a], basis[:, b])
            gluing_norms.append(float(np.linalg.norm(glued)))
            gluing_invariance_residuals.extend(
                float(np.linalg.norm(total_generator(g, 6) @ glued))
                for g in GENERATORS
            )

    max_residual = max(
        [orthogonality_residual, *invariance_residuals, *pair_residuals.values(),
         *closure_residuals, *gluing_invariance_residuals]
    )
    result = {
        "module": "MQ-002/MQ-003",
        "status": {
            "MQ-T002": "proved_analytically",
            "MQ-T003": "proved_analytically_under_dual_representation_pairing",
            "numerical_checks": "passed",
        },
        "intertwiner_dimension": 2,
        "basis_orthogonality_residual": orthogonality_residual,
        "total_spin_invariance_residuals": invariance_residuals,
        "pair_flux_matrices": matrices,
        "pair_flux_matrix_residuals": pair_residuals,
        "pairwise_closure_residuals": closure_residuals,
        "two_node_gluing": {
            "input_basis_pairs": 4,
            "unnormalized_output_norms": gluing_norms,
            "normalized_output_factor": 2.0,
            "global_su2_invariance_residuals": gluing_invariance_residuals,
            "shared_spin": "j=1/2 on both ends",
            "area_matching": True,
            "shape_matching_imposed": False,
        },
        "max_numerical_residual": max_residual,
        "tolerance": 1e-12,
        "interpretation": (
            "Finite-dimensional checks support the exact representation-theoretic "
            "statements. They do not establish shape matching, a Regge continuum "
            "limit, or an RGS/Q6 identification."
        ),
    }
    assert max_residual < 1e-12
    assert all(abs(n - 0.5) < 1e-12 for n in gluing_norms)
    return result


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
