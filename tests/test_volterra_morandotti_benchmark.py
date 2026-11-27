import numpy as np
import pytest

from models.volterra_morandotti_benchmark import volterra_three_core_data


def test_dipole_and_edge_have_same_global_burgers_moment():
    data = volterra_three_core_data(0.56, 0.06, 0.01)
    assert np.allclose(data["global_moments_dipole"],
                       data["global_moments_edge"], atol=1e-14)
    assert np.allclose(data["global_moments_dipole"], [0.0, 0.0, 0.0056])


def test_finite_separation_keeps_distinct_local_cell_source_vectors():
    data = volterra_three_core_data(0.56, 0.06, 0.01)
    assert np.linalg.norm(data["local_source_vector_difference"]) > 0.0
    assert np.linalg.norm(data["burgers_vector"]) == pytest.approx(
        data["frank_magnitude"]*data["separation"])


def test_three_core_geometry_is_disjoint():
    data = volterra_three_core_data(0.56, 0.06)
    centers = data["centers"]
    distances = [np.linalg.norm(centers[i]-centers[j])
                 for i in range(3) for j in range(i+1, 3)]
    assert min(distances) > 2*data["core_radius"]


@pytest.mark.parametrize("d,a", [(0.24, 0.06), (0.48, 0.12), (0.2, 0.05)])
def test_overlapping_three_core_geometry_is_rejected(d, a):
    with pytest.raises(ValueError, match="disjoint"):
        volterra_three_core_data(d, a)
