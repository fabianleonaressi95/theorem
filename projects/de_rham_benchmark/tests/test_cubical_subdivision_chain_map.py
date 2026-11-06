"""Exact regression tests for standard cubical subdivision and symmetry naturality."""
import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "audits" / "audit_cubical_subdivision_chain_map.py"
SPEC = importlib.util.spec_from_file_location("audit_cubical_subdivision_chain_map", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def test_subdivision_is_chain_map_on_single_cube():
    report = MODULE.audit(size=1)
    assert report["subdivision_chain_identity"]
    assert report["symmetry_naturality_identity"]
    assert report["signed_permutation_symmetries_checked"] == 48


def test_subdivision_is_chain_map_on_two_by_two_by_two_coarse_grid():
    report = MODULE.audit(size=2)
    assert report["subdivision_chain_identity"]
    assert report["symmetry_naturality_identity"]
    assert all(report["cells_checked_by_degree"][str(k)] > 0 for k in range(4))


def test_each_k_cell_has_2_to_k_fine_subcells():
    for degree in range(4):
        cell = next(MODULE.cells(2, degree))
        assert len(MODULE.subdivision(cell)) == 2 ** degree


def test_boundary_squared_vanishes_exactly():
    for degree in range(1, 4):
        for cell in MODULE.cells(2, degree):
            assert MODULE.boundary_chain(MODULE.boundary(cell)) == {}
