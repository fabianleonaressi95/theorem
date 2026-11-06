import math

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
    assert all(graphs[i + 1].spacings[0] < graphs[i].spacings[0]
               for i in range(3))


def test_vertex_measure_is_probability_volume_normalized():
    for level in (1, 2, 4, 8):
        graph = PrismProductRefinement(level)
        assert graph.vertex_count * graph.cell_volume == pytest.approx(1.0)


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


def test_audit_labels_scope_and_records():
    result = audit_refinements([1, 2, 4], modes=[(1, 0, 0, 0, 0)])
    assert result["status"] == "flat_reference_refinement_not_curved_RGS_Mosco_theorem"
    assert [row["vertices"] for row in result["rows"]] == [69120, 69120 * 32, 69120 * 1024]
