"""Regression tests for the GL(6,2)-affine Q6 filtration audit.

Run from the repository root:
    python -m pytest tests/test_q6_gl2_affine.py -v
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]
                     / "experiments" / "quantum_fractal_q6"))

from gl2_affine_audit import (  # noqa: E402
    affine_vertex_map, commutator_profile, companion_matrix,
    first_nonzero, gf2_rank,
    preserves_Ej_block_criterion, random_gl6, s6_permutations,
)
from walsh_filtration import (  # noqa: E402
    conditional_expectation, load_canonical_q6, permutation_matrix_from_map,
)


def _projections():
    return {j: conditional_expectation(j) for j in range(7)}


def test_affine_vertex_map_is_a_permutation():
    P = s6_permutations()[17]
    idx = affine_vertex_map(P)
    assert sorted(idx.tolist()) == list(range(64))
    # applying twice with inverse recovers identity on indices
    Pinv = np.linalg.inv(P.astype(float))
    # binary inverse via solve over F2: brute check P invertible -> map bijective
    assert gf2_rank(P) == 6


def test_translations_preserve_every_Ej():
    rng = np.random.default_rng(7)
    projections = _projections()
    for _ in range(8):
        b = rng.integers(0, 2, 6, dtype=np.uint8)
        idx = affine_vertex_map(np.eye(6, dtype=np.uint8), b)
        fro, _ = commutator_profile(idx, projections)
        assert all(v < 1e-9 for v in fro.values())


def test_swap_2_4_control_still_breaks_filtration():
    """Consistency with PR #435: the 1-based cols 3<->5 transposition
    gives the reviewed nonzero profile."""
    P = np.zeros((6, 6), dtype=np.uint8)
    P[2, 4] = P[4, 2] = 1
    P[0, 0] = P[1, 1] = P[3, 3] = P[5, 5] = 1
    idx = affine_vertex_map(P)
    fro, _ = commutator_profile(idx, _projections())
    assert abs(fro["3"] - 2.0 * np.sqrt(2.0)) < 1e-9
    assert abs(fro["4"] - 4.0) < 1e-9
    assert fro["1"] < 1e-9 and fro["2"] < 1e-9
    assert fro["5"] < 1e-9


def test_block_criterion_matches_computations():
    """The exact criterion P[:j,j:]==0 predicts zero commutator."""
    rng = np.random.default_rng(11)
    projections = _projections()
    mats = random_gl6(rng, 40) + s6_permutations()[:40]
    for P in mats:
        fro, _ = commutator_profile(affine_vertex_map(P), projections)
        for j in range(1, 6):
            zero = fro[str(j)] < 1e-9
            assert zero == preserves_Ej_block_criterion(P, j), (
                f"criterion mismatch at j={j} for P=\n{P}")


def test_lower_triangular_preserves_full_flag():
    """A unipotent lower-triangular shear (like transvection E30)
    preserves every E_j; an upper shear does not."""
    projections = _projections()
    P_lower = np.eye(6, dtype=np.uint8)
    P_lower[3, 0] = 1  # output coord3 += input coord0 (a<c? no: 3>0 lower)
    idx = affine_vertex_map(P_lower)
    fro, _ = commutator_profile(idx, projections)
    assert all(v < 1e-9 for v in fro.values())

    P_upper = np.eye(6, dtype=np.uint8)
    P_upper[0, 3] = 1
    fro2, _ = commutator_profile(affine_vertex_map(P_upper), projections)
    assert fro2["1"] > 1e-9


def test_companion_matrix_is_invertible():
    P = companion_matrix([1, 1, 0, 0, 0, 0, 1])
    assert gf2_rank(P) == 6


def test_s6_identity_is_only_full_preserver():
    projections = _projections()
    count = 0
    for P in s6_permutations():
        fro, _ = commutator_profile(affine_vertex_map(P), projections)
        if first_nonzero(fro) is None:
            count += 1
            assert np.array_equal(P, np.eye(6, dtype=np.uint8))
    assert count == 1
