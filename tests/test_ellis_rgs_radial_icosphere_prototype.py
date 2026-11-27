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


def test_affine_radial_mode_has_exact_ellis_interior_radial_energy():
    r0 = 0.8292
    result = EllisGraph(r0=r0, radial_cells=17, sphere_subdivisions=1).build()
    nv = len(result["sphere_vertices"])
    nr = len(result["u"])
    radial_count = result["radial_edges"]
    radial_edges = result["edges"][:radial_count]
    values = np.repeat(result["u"], nv)
    discrete_energy = float(np.sum(
        radial_edges[:, 2] * (values[radial_edges[:, 0].astype(int)]
                              - values[radial_edges[:, 1].astype(int)]) ** 2
    ))
    u_left, u_right = result["u"][0], result["u"][-1]
    primitive = lambda u: u ** 3 / 3.0 + r0 ** 2 * u
    continuum_energy = 4 * math.pi * (primitive(u_right) - primitive(u_left))
    assert nr == 17
    assert abs(discrete_energy - continuum_energy) < 1e-10


def test_circumcentric_dual_crosses_every_primal_edge_at_refinement_levels():
    # EllisGraph.build now rejects same-side circumcentres instead of
    # accepting their unsigned distance as a positive conductance.
    for level in (0, 1, 2, 3):
        result = EllisGraph(radial_cells=3, sphere_subdivisions=level).build()
        assert result["angular_edges_per_layer"] == 30 * (4 ** level)
        assert np.all(np.isfinite(result["edges"][:, 2]))
        assert np.all(result["edges"][:, 2] > 0)
