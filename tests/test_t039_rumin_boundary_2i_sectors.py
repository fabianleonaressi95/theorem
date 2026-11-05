"""Exact scalar tests for T039 boundary sectors."""
import sympy as sp
import pytest
from src.t039_rumin_boundary_2i_sectors import audit_boundary_sector, boundary_eigenvalue


@pytest.mark.parametrize(("kind", "index", "expected"), [
    ("q=-1", 1, sp.Rational(1)),
    ("q=-1", 2, sp.Rational(9, 4)),
    ("q=-1", 7, sp.Rational(16)),
    ("p=-1", 1, sp.Rational(1)),
    ("p=-1", 3, sp.Rational(4)),
    ("p=-1", 8, sp.Rational(81, 4)),
])
def test_boundary_eigenvalues_are_exact(kind, index, expected):
    assert boundary_eigenvalue(kind, index) == expected


def test_orientations_remain_distinct_labels():
    assert boundary_eigenvalue("q=-1", 4) == sp.Rational(25, 4)
    assert boundary_eigenvalue("p=-1", 4) == sp.Rational(25, 4)


@pytest.mark.parametrize(("kind", "index"), [
    ("generic", 2), ("q=-1", 0), ("p=-1", -1),
])
def test_invalid_boundary_input_rejected(kind, index):
    with pytest.raises(ValueError):
        boundary_eigenvalue(kind, index)


def test_representation_degree_is_never_inferred():
    report = audit_boundary_sector("q=-1", 3)
    assert report["D_adjoint_D_eigenvalue"] == "4"
    assert "not supplied" in report["representation_identification"]
    assert "representation_degree" not in report
