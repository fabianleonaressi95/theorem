from scripts.audit_t103_cycle_cocycle import (
    audit_cycle_cocycle,
    cut_cocycle_basis,
    fundamental_cycle_basis,
    square_boundary_vectors,
    dot_f2,
)


def test_q6_fundamental_cycle_basis_has_dimension_129():
    basis = fundamental_cycle_basis()
    assert len(basis) == 129


def test_q6_cut_cocycle_basis_has_dimension_63():
    basis = cut_cocycle_basis()
    assert len(basis) == 63


def test_cycle_cocycle_pairing_is_zero_mod_two():
    cycles = fundamental_cycle_basis()
    cocycles = cut_cocycle_basis()
    assert all(dot_f2(c, z) == 0 for c in cycles for z in cocycles)


def test_square_boundaries_generate_all_graph_cycles():
    result = audit_cycle_cocycle()
    assert result["conclusions"]["cycle_space_equals_square_boundary_span"]


def test_first_homology_and_cohomology_vanish():
    result = audit_cycle_cocycle()
    assert result["H1_dimension"] == 0
    assert result["H1_cohomology_dimension"] == 0
