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


def test_exact_cell_masses_reproduce_continuum_volume():
    errors = [audit(n, 1)["relative_volume_error"] for n in (8, 16, 32, 64)]
    assert all(math.isfinite(e) for e in errors)
    assert max(errors) < 1e-12


def test_spherical_dual_areas_sum_to_four_pi():
    result = EllisGraph(radial_cells=4, sphere_subdivisions=2).build()
    assert abs(float(result["sphere_cell_area"].sum()) - 4 * math.pi) < 1e-10


def test_separated_spherical_l1_mode_is_a_finite_consistency_diagnostic():
    coarse = audit(6, 0)
    refined = audit(6, 1)
    for result in (coarse, refined):
        value = result["spherical_l1_rayleigh"]
        assert math.isfinite(value)
        assert value > 0
        assert result["spherical_l1_continuum_eigenvalue"] == 2.0
