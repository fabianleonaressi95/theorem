"""Exact boundary-to-SU(2)-to-2I checks for T039."""
import pytest
from src.t039_rumin_boundary_2i_sectors import audit_boundary_sector, boundary_data


@pytest.mark.parametrize(("kind", "index", "degree", "eigenvalue"), [
    ("q=-1", 1, 0, "1"),
    ("q=-1", 2, 1, "9/4"),
    ("q=-1", 13, 12, "49"),
    ("p=-1", 1, 0, "1"),
    ("p=-1", 3, 2, "4"),
    ("p=-1", 13, 12, "49"),
])
def test_boundary_highest_weight_and_exact_eigenvalue(kind, index, degree, eigenvalue):
    data = boundary_data(kind, index)
    assert data["SU2_symmetric_power_degree"] == degree
    assert data["SU2_module_dimension"] == degree + 1
    assert data["D_adjoint_D_eigenvalue"] == eigenvalue


@pytest.mark.parametrize(("kind", "index"), [
    ("q=-1", 0), ("p=-1", -1), ("generic", 4),
])
def test_invalid_boundary_input(kind, index):
    with pytest.raises(ValueError):
        boundary_data(kind, index)


@pytest.mark.parametrize(("kind", "index"), [("q=-1", 13), ("p=-1", 13)])
def test_first_nontrivial_invariant_boundary_level(kind, index):
    report = audit_boundary_sector(kind, index)
    assert report["SU2_symmetric_power_degree"] == 12
    assert report["trivial_2I_multiplicity"] == 1
    assert report["2I_dimension_sum"] == 13


@pytest.mark.parametrize(("kind", "index"), [("q=-1", 1), ("p=-1", 1)])
def test_constant_boundary_representation(kind, index):
    report = audit_boundary_sector(kind, index)
    assert report["2I_irrep_multiplicities"]["1"] == 1
    assert report["2I_dimension_sum"] == 1
