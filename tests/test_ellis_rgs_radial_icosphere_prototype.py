import math

import numpy as np

from scripts.ellis_rgs_radial_icosphere_prototype import EllisGraph, audit


def test_icosphere_product_graph_has_positive_weights_and_correct_counts():
    result = EllisGraph(radial_cells=8, sphere_subdivisions=1).build()
    nv = 42
    ne_sphere = 120
    assert result["nodes"] == 8 * nv
    assert result["radial_edges"] == 7 * nv
    assert result["angular_edges_per_layer"] == ne_sphere
    assert np.all(result["masses"] > 0)
    assert np.all(result["edges"][:, 2] > 0)


def test_discrete_volume_converges_under_radial_refinement():
    errors = [audit(n, 1)["relative_volume_error"] for n in (8, 16, 32, 64)]
    assert all(math.isfinite(e) for e in errors)
    assert errors[1] < errors[0]
    assert errors[2] < errors[1]
    assert errors[3] < errors[2]


def test_spherical_dual_areas_sum_to_four_pi():
    result = EllisGraph(radial_cells=4, sphere_subdivisions=2).build()
    assert abs(float(result["sphere_cell_area"].sum()) - 4 * math.pi) < 1e-10
