"""Regression tests for the exact boundary Barnes-zeta reduction."""
import pytest

from src.t040_boundary_barnes_zeta import (
    audit, barnes_zeta_decomposition, boundary_level,
    invariant_multiplicity, partial_spectral_zeta,
)


@pytest.mark.parametrize("kind", ["q=-1", "p=-1"])
def test_boundary_level_exact_data(kind):
    assert boundary_level(kind, 1) == {
        "kind": kind, "boundary_index": 1, "SU2_degree": 0,
        "eigenvalue": "1", "untwisted_2I_multiplicity": 1,
    }
    assert boundary_level(kind, 2)["eigenvalue"] == "9/4"
    assert boundary_level(kind, 3)["eigenvalue"] == "4"
    assert boundary_level(kind, 4)["eigenvalue"] == "25/4"
    assert boundary_level(kind, 13)["eigenvalue"] == "49"
    assert boundary_level(kind, 13)["untwisted_2I_multiplicity"] == 1


def test_molien_multiplicity_matches_two_barnes_lattices():
    # Coefficients of 1/((1-t^12)(1-t^20)) and its t^30 shift.
    for m in range(121):
        expected = sum(
            1 for a in range(m // 12 + 1)
            for b in range(m // 20 + 1)
            if 12 * a + 20 * b == m or 30 + 12 * a + 20 * b == m
        )
        assert invariant_multiplicity(m) == expected


def test_first_nonconstant_invariant_degree():
    assert [m for m in range(1, 31) if invariant_multiplicity(m)] == [12, 20, 24, 30]


@pytest.mark.parametrize("kind", ["q=-1", "p=-1"])
def test_barnes_parameters_and_domain(kind):
    data = barnes_zeta_decomposition(kind)
    assert data["barnes_starts"] == [2, 32]
    assert data["barnes_periods"] == [12, 20]
    assert data["initial_convergence"] == "Re(s) > 1"


def test_two_orientations_are_equal_but_not_implicitly_collapsed():
    q = [boundary_level("q=-1", n) for n in range(1, 41)]
    p = [boundary_level("p=-1", n) for n in range(1, 41)]
    assert q == [{**x, "kind": "q=-1"} for x in p]


def test_partial_zeta_matches_direct_first_terms():
    direct = sum(
        invariant_multiplicity(n - 1) * (((n + 1) ** 2) / 4.0) ** (-2.0)
        for n in range(1, 41)
    )
    assert partial_spectral_zeta("q=-1", 2.0, 40) == pytest.approx(direct)


@pytest.mark.parametrize("kind,index", [("bad", 1), ("q=-1", 0), ("p=-1", -2)])
def test_invalid_boundary_level(kind, index):
    with pytest.raises(ValueError):
        boundary_level(kind, index)


def test_audit_keeps_boundary_orientations_separate():
    report = audit(13)
    assert report["levels_per_orientation"] == 13
    assert report["combined_if_both_orientations_are_counted"].startswith("2 *")
    assert len(report["boundary_levels"]) == 26
