import numpy as np

from scripts.audit_t103_q6_z2_magnetic_holonomy import (
    audit,
    cells,
    gauge_fix,
    gauge_transform,
    magnetic_laplacian,
    plaquette_flux,
    q6_edges,
    spectrum_and_heat,
    three_cell_flux_constraints,
)


def test_cubical_cell_counts_and_boundary_ranks():
    result = audit()
    assert result["cell_counts"] == {"C0": 64, "C1": 192, "C2": 240, "C3": 160}
    assert result["gf2_boundary_ranks"] == {
        "rank_d1": 63, "rank_d2": 129, "rank_d3": 111
    }


def test_all_face_fluxes_obey_three_cell_constraints():
    rng = np.random.default_rng(103)
    edge_bits = rng.integers(0, 2, size=len(q6_edges()), dtype=np.uint8)
    flux = plaquette_flux(edge_bits)
    assert not np.any(three_cell_flux_constraints(flux))


def test_gauge_fix_is_canonical_for_gauge_equivalent_edges():
    rng = np.random.default_rng(104)
    edge_bits = rng.integers(0, 2, size=len(q6_edges()), dtype=np.uint8)
    vertex_gauge = rng.integers(0, 2, size=64, dtype=np.uint8)
    transformed = gauge_transform(edge_bits, vertex_gauge)
    fixed_a, _ = gauge_fix(edge_bits)
    fixed_b, _ = gauge_fix(transformed)
    assert np.array_equal(fixed_a, fixed_b)
    assert np.array_equal(plaquette_flux(edge_bits), plaquette_flux(transformed))


def test_magnetic_laplacian_is_hermitian_and_positive():
    edge_bits = np.zeros(len(q6_edges()), dtype=np.uint8)
    edge_bits[[0, 17, 89]] = 1
    laplacian = magnetic_laplacian(edge_bits)
    assert np.allclose(laplacian, laplacian.T)
    assert np.linalg.eigvalsh(laplacian).min() >= -1e-10


def test_trivial_connection_recovers_exact_q6_heat_trace():
    result = audit()
    heat = result["representatives"]["trivial"]["heat_trace"]
    times = result["heat_times"]
    expected = [(1 + np.exp(-2 * t)) ** 6 for t in times]
    assert np.allclose(heat, expected, atol=1e-10)


def test_spectrum_is_gauge_invariant():
    rng = np.random.default_rng(105)
    edge_bits = np.zeros(len(q6_edges()), dtype=np.uint8)
    edge_bits[[4, 32, 111]] = 1
    vertex_gauge = rng.integers(0, 2, size=64, dtype=np.uint8)
    transformed = gauge_transform(edge_bits, vertex_gauge)
    eigen_a, heat_a = spectrum_and_heat(edge_bits, [0.0, 0.2, 1.0])
    eigen_b, heat_b = spectrum_and_heat(transformed, [0.0, 0.2, 1.0])
    assert np.allclose(eigen_a, eigen_b, atol=1e-10)
    assert np.allclose(heat_a, heat_b, atol=1e-10)
