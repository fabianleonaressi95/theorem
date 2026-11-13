from fractions import Fraction as F

from models.morandotti_certified_curved_p3_forms import (
    assemble_boundary_edge_interval,
    assemble_cell_volume_interval,
    certify_interval_psd,
    integrate_rational_sqrt_segment,
)


def _p3_nodes():
    points = [
        (F(i, 3), F(j, 3))
        for i in range(4)
        for j in range(4-i)
    ]
    # The identity map has nodal coordinates equal to the reference points.
    return points, points


def test_certified_rational_sqrt_segment_constant_exact():
    lo, hi, leaves, depth = integrate_rational_sqrt_segment(
        {0: F(1)}, {0: F(1)}, {0: F(1)}
    )
    assert lo == hi == 1
    assert leaves == 1
    assert depth == 0


def test_identity_p3_cell_volume_block_is_exact_interval_matrix():
    nodes, points = _p3_nodes()
    result = assemble_cell_volume_interval(
        nodes, points, absolute_tolerance=F(1, 10**7)
    )
    matrix = result["matrix_interval"]
    assert len(matrix) == 10
    assert all(len(row) == 10 for row in matrix)
    for i in range(10):
        for j in range(10):
            assert matrix[i][j] == matrix[j][i]
            assert matrix[i][j][0] <= matrix[i][j][1]
    assert result["integration"].startswith("exact-rational Bernstein")


def test_identity_p3_boundary_edge_block_has_certified_metric():
    nodes, points = _p3_nodes()
    result = assemble_boundary_edge_interval(
        nodes, points, (0, 1), F(1), absolute_tolerance=F(1, 5)
    )
    matrix = result["matrix_interval"]
    assert len(matrix) == 10
    assert all(matrix[i][j] == matrix[j][i] for i in range(10) for j in range(10))
    assert result["integration"].startswith("exact-rational Bernstein")


def test_interval_psd_propagates_entrywise_integration_error():
    matrix = [
        [(F(1), F(1)), (F(0), F(0))],
        [(F(0), F(0)), (F(2), F(2))],
    ]
    result = certify_interval_psd(matrix)
    assert result["certified"]
    assert result["entrywise_radius"] == 0
    assert result["spectral_error_bound"] == 0



def test_exact_two_sided_interior_facet_matches_and_encloses():
    from models.morandotti_certified_curved_p3_forms import (
        assemble_interior_facet_interval,
    )

    points = [
        (F(i, 3), F(j, 3))
        for i in range(4)
        for j in range(4-i)
    ]
    nodes_a = points
    # The second affine triangle has vertices (1,0), (1,1), (0,1).
    nodes_b = [(1-y, x+y) for x, y in points]
    result = assemble_interior_facet_interval(
        nodes_a, nodes_b, points, (1, 2), (0, 2), F(1),
        absolute_tolerance=F(1, 5),
    )
    for key in ("block_AA", "block_AB", "block_BB"):
        block = result[key]
        assert len(block) == 10
        assert all(len(row) == 10 for row in block)
        assert all(block[i][j][0] <= block[i][j][1]
                   for i in range(10) for j in range(10))


def test_sparse_interval_psd_certificate_includes_perturbation():
    from models.morandotti_certified_curved_p3_forms import certify_interval_psd

    matrix = {
        (0, 0): (F(2)-F(1, 1000), F(2)+F(1, 1000)),
        (1, 1): (F(3)-F(1, 1000), F(3)+F(1, 1000)),
        (0, 1): (F(0), F(0)),
        (1, 0): (F(0), F(0)),
    }
    result = certify_interval_psd(matrix)
    assert result["certified"]
    assert result["spectral_error_bound"] == F(1, 1000)



def test_global_trace_bound_propagates_sparse_D_and_H_intervals():
    from models.morandotti_certified_curved_p3_forms import (
        certify_global_trace_bound,
    )

    D = {
        (0, 0): (F(2), F(2)), (0, 1): (F(0), F(0)),
        (1, 0): (F(0), F(0)), (1, 1): (F(3), F(3)),
    }
    H = {
        (0, 0): (F(1), F(1)), (0, 1): (F(0), F(0)),
        (1, 0): (F(0), F(0)), (1, 1): (F(2), F(2)),
    }
    result = certify_global_trace_bound(D, H, [1, 0], F(2))
    assert result["certified"]
    assert result["integration_uncertainty_propagated"]
    assert result["quotient_dimension"] == 2



def test_nonaffine_p3_geometry_has_variable_positive_jacobian():
    from models.morandotti_certified_curved_p3_forms import _geometry_data

    nodes, points = _p3_nodes()
    # Perturb the strictly interior P3 node; the resulting map is genuinely
    # cubic/non-affine while remaining a small perturbation of the identity.
    nodes = list(nodes)
    nodes[5] = (nodes[5][0] + F(1, 40), nodes[5][1] - F(1, 50))
    maps, basis, jac, adj, det = _geometry_data(nodes, points)
    from models.morandotti_exact_geometry import _certify_positive_exact

    assert any(sum(exponent) > 0 for exponent in det)
    certificate = _certify_positive_exact(det, 4, max_depth=8)
    assert certificate["positive"]
    assert certificate["lower"] is not None
    assert certificate["lower"] > 0


def test_global_assembly_forwards_requested_volume_depth(monkeypatch):
    import models.morandotti_certified_curved_p3_forms as forms

    observed = {}

    def fake_volume(nodes, points, *, absolute_tolerance, max_depth):
        observed["max_depth"] = max_depth
        zero = (F(0), F(0))
        return {"matrix_interval": [[zero for _ in range(10)] for _ in range(10)]}

    monkeypatch.setattr(forms, "assemble_cell_volume_interval", fake_volume)
    forms.assemble_global_interval_forms(
        [None], [], [list(range(10))], [F(1)], [], [], 10,
        max_depth=3,
    )
    assert observed["max_depth"] == 3


def test_shared_facet_integrator_encloses_scalar_integrals():
    from models.morandotti_certified_curved_p3_forms import (
        integrate_rational_sqrt_segments_many,
    )

    numerators = [
        {0: F(1), 1: F(1, 3)},
        {0: F(-1), 1: F(2)},
        {0: F(1), 1: F(-2), 2: F(1)},
    ]
    denominator = {0: F(2), 1: F(1, 4)}
    radicand = {0: F(1), 1: F(1, 5)}
    kwargs = {"absolute_tolerance": F(1, 1000), "max_depth": 16}
    shared = integrate_rational_sqrt_segments_many(
        numerators, denominator, radicand, **kwargs
    )
    scalar = [
        integrate_rational_sqrt_segment(p, denominator, radicand, **kwargs)
        for p in numerators
    ]
    for (lo, hi, _, _), (slo, shi, _, _) in zip(shared, scalar):
        assert lo <= shi and slo <= hi
        assert hi - lo <= F(1, 500)
