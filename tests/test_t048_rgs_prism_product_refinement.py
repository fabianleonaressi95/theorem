import math
from itertools import islice

import pytest

from scripts.rgs_prism_product_refinement import (
    BASE_LENGTHS,
    PrismProductRefinement,
    audit_refinements,
)


def test_level_one_is_the_existing_prism_product_graph():
    graph = PrismProductRefinement(1)
    assert graph.lengths == BASE_LENGTHS
    assert graph.vertex_count == 64 * 6**3 * 5 == 69120
    assert graph.degree == 10


def test_refinement_scales_each_factor_and_mesh_to_zero():
    graphs = [PrismProductRefinement(m) for m in (1, 2, 4, 8)]
    assert [g.vertex_count for g in graphs] == [69120 * m**5 for m in (1, 2, 4, 8)]
    assert all(graphs[i + 1].lengths[j] == 2 * graphs[i].lengths[j]
               for i in range(3) for j in range(5))
    assert all(max(graphs[i + 1].spacings) < max(graphs[i].spacings)
               for i in range(3))


def test_vertex_measure_and_conductances_are_positive_and_normalized():
    for level in (1, 2, 4, 8):
        graph = PrismProductRefinement(level)
        assert graph.vertex_count * graph.cell_volume == pytest.approx(1.0)
        assert graph.cell_volume > 0
        assert all(weight > 0 for weight in graph.conductances)


def test_indexing_is_bijective_on_representative_vertices():
    graph = PrismProductRefinement(2)
    samples = (
        (0, 0, 0, 0, 0),
        tuple(n - 1 for n in graph.lengths),
        tuple(n // 2 for n in graph.lengths),
        (1, 2, 3, 4, 5),
    )
    for vertex in samples:
        assert graph.decode(graph.encode(vertex)) == vertex
    assert graph.encode((0, 0, 0, 0, 0)) == 0
    assert graph.decode(graph.vertex_count - 1) == tuple(n - 1 for n in graph.lengths)


def test_periodic_neighbours_and_lazy_positive_edge_iterator():
    graph = PrismProductRefinement(1)
    origin = (0, 0, 0, 0, 0)
    assert graph.neighbor(origin, 0, -1) == (63, 0, 0, 0, 0)
    assert graph.neighbor(origin, 1, 1) == (0, 1, 0, 0, 0)
    first_edges = list(islice(graph.positive_direction_edges(), 12))
    assert len(first_edges) == 12
    assert all(head == graph.neighbor(tail, axis, 1)
               for tail, head, axis in first_edges)
    assert graph.vertex_count * graph.degree // 2 == 5 * graph.vertex_count


def test_intrinsic_metric_condition_holds_exactly():
    for level in (1, 2, 4, 8):
        graph = PrismProductRefinement(level)
        assert graph.intrinsic_metric_residual() < 1e-14


def test_fourier_eigenvalues_converge_for_fixed_modes():
    mode = (1, 1, 0, 0, 0)
    target = 4.0 * math.pi**2 * sum(k * k for k in mode)
    errors = [abs(PrismProductRefinement(m).discrete_eigenvalue(mode) - target)
              for m in (1, 2, 4, 8, 16)]
    assert all(errors[i + 1] < errors[i] for i in range(len(errors) - 1))
    assert errors[-1] < 0.02


def test_sampled_smooth_mode_energy_has_second_order_convergence():
    mode = (1, 0, 0, 0, 0)
    records = [PrismProductRefinement(m).mode_energy(mode)
               for m in (1, 2, 4, 8, 16)]
    errors = [row["relative_energy_error"] for row in records]
    assert all(errors[i + 1] < errors[i] for i in range(len(errors) - 1))
    # Doubling each cyclic resolution reduces the leading O(h^2) error by ~4.
    assert errors[-1] < 2e-4
    assert all(row["mass_norm_squared"] == pytest.approx(0.5) for row in records)


def test_uniform_fourier_lower_bound():
    graph = PrismProductRefinement(4)
    mode = (2, -1, 1, 0, 0)
    lam = graph.discrete_eigenvalue(mode)
    assert lam >= 16.0 * sum(k * k for k in mode)


@pytest.mark.parametrize("level", [0, -1, 1.5, True])
def test_invalid_level_rejected(level):
    with pytest.raises(ValueError):
        PrismProductRefinement(level)


@pytest.mark.parametrize("mode", [
    (1, 2), (1, 0, 0, 0, 1.5), (True, 0, 0, 0, 0),
    (0, 0, 0, 0, 100),
])
def test_invalid_modes_rejected(mode):
    with pytest.raises(ValueError):
        PrismProductRefinement(1).discrete_eigenvalue(mode)


def test_invalid_indices_and_neighbour_arguments_rejected():
    graph = PrismProductRefinement(1)
    with pytest.raises(ValueError):
        graph.decode(-1)
    with pytest.raises(ValueError):
        graph.encode((0, 0, 0, 0, 64))
    with pytest.raises(ValueError):
        graph.neighbor((0, 0, 0, 0, 0), 5, 1)
    with pytest.raises(ValueError):
        graph.neighbor((0, 0, 0, 0, 0), 0, 0)
    with pytest.raises(ValueError):
        graph.neighbor((0, 0, 0, 0, 0), 0, True)


def test_aliasing_constant_sign_cosine_is_rejected_for_energy():
    with pytest.raises(ValueError):
        PrismProductRefinement(1).mode_energy((0, 0, 0, 0, 0))


def test_audit_labels_scope_and_reports_milestones():
    result = audit_refinements([1, 2, 4], modes=[(1, 0, 0, 0, 0)])
    assert result["status"] == "flat_reference_refinement_not_curved_RGS_Mosco_theorem"
    assert [row["vertices"] for row in result["rows"]] == [69120, 69120 * 32, 69120 * 1024]
    assert [row["undirected_edges"] for row in result["rows"]] == [5 * row["vertices"] for row in result["rows"]]
    assert all(result["milestone_checks"].values())
    assert all(all(row["checks"].values()) for row in result["rows"])


def test_empty_refinement_list_rejected():
    with pytest.raises(ValueError):
        audit_refinements([])
