"""Tests for the finite Q6/Walsh filtration audit.

Run from the repository root:
    python -m pytest tests/test_quantum_fractal_q6.py -v
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]
                     / "experiments" / "quantum_fractal_q6"))

from walsh_filtration import (  # noqa: E402
    N_SITES, audit_operator, conditional_expectation, coordinate_swap_matrix,
    decode_state_permutation, describe_induced_map, load_canonical_q6,
    operator_inventory, permutation_matrix_from_map, run_audit,
    suffix_mask, walsh_matrix,
)

SYNTHETIC_CONTROLS = {"synthetic_GOE_control",
                      "reviewer_swap_cols_2_4_control"}


def _fixtures():
    arrays = load_canonical_q6()
    states = arrays["Q6_states"]
    W = walsh_matrix(states)
    projections = {j: conditional_expectation(j) for j in range(7)}
    return arrays, states, W, projections


def test_q6_states_product_order_and_laplacian_is_hypercube():
    arrays, _, _, _ = _fixtures()
    states = arrays["Q6_states"]
    assert states.shape == (64, 6)
    assert np.array_equal(
        states,
        np.array(list(__import__("itertools").product((0, 1), repeat=6))))
    L = arrays["Q6_laplacian"].astype(float)
    A = arrays["Q6_adjacency"].astype(float)
    # stored Laplacian is exactly 6I - adjacency (unweighted hypercube)
    assert np.allclose(L, 6.0 * np.eye(64) - A)
    assert np.allclose(L.sum(axis=1), 0.0)


def test_projection_identities():
    _, _, _, projections = _fixtures()
    for j, E in projections.items():
        assert np.linalg.norm(E @ E - E, "fro") < 1e-12
        assert np.linalg.norm(E - E.T, "fro") < 1e-12
        assert int(round(np.linalg.matrix_rank(E, tol=1e-9))) == (1 << j)
    # nested filtration: E_j E_k = E_min(j,k)
    for j in range(7):
        for k in range(7):
            m = min(j, k)
            assert np.linalg.norm(
                projections[j] @ projections[k] - projections[m], "fro"
            ) < 1e-12


def test_walsh_matrix_unitary_and_diagonalizes_laplacian():
    _, states, W, _ = _fixtures()
    assert np.allclose(W @ W.T, np.eye(N_SITES), atol=1e-12)
    L = load_canonical_q6()["Q6_laplacian"].astype(float)
    LW = W.T @ L @ W
    # Walsh basis diagonalizes the hypercube Laplacian with eigenvalues 2|S|
    offdiag = LW - np.diag(np.diag(LW))
    assert np.abs(offdiag).max() < 1e-10
    evals = np.diag(LW)
    expected = np.array(
        [2 * bin(s).count("1") for s in range(N_SITES)], dtype=float)
    assert np.allclose(np.sort(evals), np.sort(expected), atol=1e-10)


def test_stored_operators_have_zero_filtration_commutators():
    arrays = load_canonical_q6()
    states = arrays["Q6_states"]
    W = walsh_matrix(states)
    projections = {j: conditional_expectation(j) for j in range(7)}
    ops = operator_inventory(arrays)
    for name, spec in ops.items():
        if name in SYNTHETIC_CONTROLS:
            continue
        result = audit_operator(spec["matrix"], projections, W)
        for j in range(7):
            assert result["commutators"][str(j)]["frobenius"] < 1e-10, (
                f"{name} unexpectedly fails to commute at level {j}")


def test_synthetic_control_is_detected():
    """The commutator machinery must return nonzero values for an
    operator with no reason to respect the filtration."""
    arrays = load_canonical_q6()
    states = arrays["Q6_states"]
    W = walsh_matrix(states)
    projections = {j: conditional_expectation(j) for j in range(7)}
    ops = operator_inventory(arrays)
    goe = ops["synthetic_GOE_control"]["matrix"]
    result = audit_operator(goe, projections, W)
    # j=6 is trivial (E_6 = I); intermediate levels must be nonzero
    assert result["commutators"]["3"]["frobenius"] > 1.0
    assert result["walsh_blocks"]["3"]["frobenius"] > 1.0


def test_suffix_mask_counts():
    for j in range(7):
        assert int(suffix_mask(j).sum()) == (1 << j)


def test_pi_at_decodes_to_bit_flip_not_coordinate_swap():
    """Regression for the PR #431 review: the stored Pi_AT must be the
    bitwise complement of columns 3,4,5 (0-based), NOT a coordinate
    transposition.  The independently rebuilt permutation matrix must
    coincide with the stored array."""
    arrays = load_canonical_q6()
    states = arrays["Q6_states"]
    P = arrays["Pi_AT"].astype(float)
    idx = decode_state_permutation(P, states)
    desc = describe_induced_map(idx, states)
    assert desc["kind"] == "bit_flip"
    assert desc["detail"]["flipped_columns_0based"] == [3, 4, 5]
    # independent reconstruction matches the stored matrix exactly
    rebuilt = permutation_matrix_from_map(idx)
    assert np.abs(rebuilt - P).max() == 0.0
    # and it is genuinely not the conjectured 3<->5 swap
    swap = coordinate_swap_matrix(2, 4)
    assert np.abs(swap - P).max() > 0.0


def test_antipodal_decodes_to_full_bit_flip():
    arrays = load_canonical_q6()
    states = arrays["Q6_states"]
    idx = decode_state_permutation(arrays["Q6_antipodal"].astype(float),
                                   states)
    desc = describe_induced_map(idx, states)
    assert desc["kind"] == "bit_flip"
    assert desc["detail"]["flipped_columns_0based"] == [0, 1, 2, 3, 4, 5]


def test_reviewer_swap_hypothesis_reproduces_expected_commutators():
    """The transposition (0-based cols 2<->4 = 1-based cols 3<->5),
    conjectured to be Pi_AT, must give the independently reported
    nonzero commutators: ||[.,E_3]||_F = 2*sqrt(2), ||[.,E_4]||_F = 4,
    spectral norm 1, zero at the other levels.  This validates both the
    filtration machinery and the reviewer's arithmetic while confirming
    the stored Pi_AT is a different map."""
    arrays = load_canonical_q6()
    states = arrays["Q6_states"]
    W = walsh_matrix(states)
    projections = {j: conditional_expectation(j) for j in range(7)}
    swap = coordinate_swap_matrix(2, 4)
    result = audit_operator(swap, projections, W)
    assert abs(result["commutators"]["3"]["frobenius"]
               - 2.0 * np.sqrt(2.0)) < 1e-9
    assert abs(result["commutators"]["4"]["frobenius"] - 4.0) < 1e-9
    assert abs(result["commutators"]["3"]["spectral"] - 1.0) < 1e-9
    assert abs(result["commutators"]["4"]["spectral"] - 1.0) < 1e-9
    for j in (0, 1, 2, 5, 6):
        assert result["commutators"][str(j)]["frobenius"] < 1e-12


def test_run_audit_report_shape():
    report = run_audit()
    assert report["experiment"].startswith("Q6/Walsh")
    assert set(report["operators"]) >= {
        "Q6_laplacian", "Q6_adjacency", "Q6_antipodal", "Pi_AT",
        "synthetic_GOE_control"}
    assert "missing_operators" in report
    # Laplacian spectrum must match the Walsh formula 2|S| exactly
    assert report["laplacian_spectrum_check"]["max_abs_difference"] < 1e-8
