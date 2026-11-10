#!/usr/bin/env python3
"""Exact algebraic and finite-combinatorial audit of the Q6 -> supergolden bridge.

This deliberately separates:
  (1) the exact 3-state supergolden transfer law;
  (2) the exact Q6 midpoint subdivision law;
  (3) the still-missing geometric map intertwining the two.

Requires Python 3 and NumPy. No repository data files are needed.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import numpy as np

A_PSI = np.array([[1, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=np.int64)
P = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=np.int64)
M_TRIGRAM = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 1]], dtype=np.int64)


def supergolden_sequence(n_terms: int = 32) -> list[int]:
    """S_0=0, S_1=0, S_2=1; S_(n+3)=S_(n+2)+S_n."""
    if n_terms < 0:
        raise ValueError("n_terms must be nonnegative")
    s = [0, 0, 1]
    if n_terms <= 3:
        return s[:n_terms]
    for n in range(n_terms - 3):
        s.append(s[n + 2] + s[n])
    return s


def q6_antipodal_audit() -> dict:
    """Audit complement involution and distinguish it from bipartition."""
    n = 6
    states = range(1 << n)
    antipode = lambda x: x ^ ((1 << n) - 1)
    fixed_points = [x for x in states if antipode(x) == x]
    involution_failures = [x for x in states if antipode(antipode(x)) != x]
    parity_changes = [
        x for x in states
        if (x.bit_count() % 2) != (antipode(x).bit_count() % 2)
    ]
    even = [x for x in states if x.bit_count() % 2 == 0]
    odd = [x for x in states if x.bit_count() % 2 == 1]
    return {
        "vertices": 64,
        "antipodal_pairs": 32,
        "fixed_points": len(fixed_points),
        "involution_failures": len(involution_failures),
        "bipartition_even_odd": [len(even), len(odd)],
        "antipode_changes_bipartition": len(parity_changes),
        "interpretation": (
            "Complement gives 32 antipodal pairs; for even n=6 it preserves "
            "Hamming parity, so antipodality is not the 32/32 bipartition."
        ),
    }


def audit() -> dict:
    # Exact matrix conjugacy from T056.
    conjugacy_ok = np.array_equal(P @ A_PSI @ P.T, M_TRIGRAM)
    permutation_ok = np.array_equal(P.T @ P, np.eye(3, dtype=np.int64))

    # Characteristic polynomial is exactly lambda^3-lambda^2-1.
    # The determinant expansion is recorded symbolically as integer coefficients.
    charpoly_coefficients_descending = [1, -1, 0, -1]
    roots = np.roots(np.array(charpoly_coefficients_descending, dtype=float))
    psi = float(max(roots.real[np.abs(roots.imag) < 1e-10]))
    other_roots = [complex(z) for z in roots if abs(z.real - psi) > 1e-8]

    seq = supergolden_sequence(40)
    ratios = [seq[k + 1] / seq[k] for k in range(3, len(seq) - 1) if seq[k] != 0]

    # T055: Q6 midpoint subdivision is axis-preserving and has D=2 I_6.
    direction_transfer = 2 * np.eye(6, dtype=np.int64)
    q6_counts = {
        "coarse_cells": [64, 192, 240],
        "midpoint_refined_cells": [496, 1344, 960],
        "subdivision_children_per_parent": [1, 2, 4],
        "direction_transfer": direction_transfer.tolist(),
    }
    # A full-rank similarity cannot turn 2 I_3 into A_PSI:
    # their characteristic polynomials are (x-2)^3 and x^3-x^2-1.
    scalar_three_channel = 2 * np.eye(3, dtype=np.int64)
    spectra_obstruction = not np.array_equal(
        np.sort(np.linalg.eigvals(scalar_three_channel).real),
        np.sort(np.linalg.eigvals(A_PSI).real),
    )

    return {
        "audit": "Q6_SUPERGOLDEN_BRIDGE",
        "classification": {
            "supergolden_recurrence": "EXACT_ALGEBRAIC_IDENTITY",
            "phase21_trigram_conjugacy": "EXACT_FINITE_MATRIX_IDENTITY",
            "q6_midpoint_chain_refinement": "EXACT_FINITE_COMBINATORIAL_RESULT_FROM_T055",
            "q6_midpoint_to_supergolden_intertwiner": "NOT_ESTABLISHED",
            "kristall_11725_classes_and_K_identity": "NOT_CERTIFIED_BY_RECOVERED_ARCHIVE",
        },
        "supergolden": {
            "matrix_A": A_PSI.tolist(),
            "matrix_trigram": M_TRIGRAM.tolist(),
            "permutation_P": P.tolist(),
            "permutation_conjugacy_exact": bool(conjugacy_ok),
            "permutation_orthogonal_exact": bool(permutation_ok),
            "characteristic_polynomial_coefficients_descending": charpoly_coefficients_descending,
            "roots": [[float(z.real), float(z.imag)] for z in roots],
            "dominant_real_root_psi": psi,
            "sequence_first_16": seq[:16],
            "last_8_ratios": ratios[-8:],
        },
        "q6": {
            **q6_counts,
            "antipodal": q6_antipodal_audit(),
            "axis_transfer_is_2I6_not_supergolden": True,
            "three_channel_spectral_obstruction_to_2I3_similarity": bool(spectra_obstruction),
        },
        "missing_bridge": [
            "Define a three-channel state space as an explicit quotient/subrepresentation of Q6 cochains.",
            "Construct a geometric parent-to-child map R on that space, from Q6 incidences or a declared RGS/Krist-All cell complex.",
            "Prove the intertwining relation J R_Q6 = A_psi J (or the declared conjugate convention).",
            "Verify that J is well-defined, has stated rank/kernel, and respects antipodal and quaternionic actions.",
            "Recover the map from source data; do not infer it from the shared polynomial or numerical proximity.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="reports/q6_supergolden_bridge_audit_2026-11-10.json")
    args = parser.parse_args()
    result = audit()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
