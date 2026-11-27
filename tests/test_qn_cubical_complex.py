import numpy as np
import pytest

from models.q6_topological_synchronization import rhs, order_parameters
from scripts.run_qn_nl_nlt_t3_t4 import build_qn_2_skeleton


@pytest.mark.parametrize(
    "n, expected",
    [
        (4, (16, 32, 24)),
        (5, (32, 80, 80)),
        (6, (64, 192, 240)),
    ],
)
def test_qn_cubical_two_skeleton_counts_and_chain_identity(n, expected):
    K = build_qn_2_skeleton(n)
    assert (len(K.vertices), len(K.edges), len(K.faces)) == expected
    assert K.B1.shape == (expected[0], expected[1])
    assert K.B2.shape == (expected[1], expected[2])
    assert np.count_nonzero(K.B1 @ K.B2) == 0


@pytest.mark.parametrize("n", [4, 5, 6])
@pytest.mark.parametrize("model", ["NL", "NLT"])
def test_frozen_rhs_and_order_parameters_accept_qn_complex(n, model):
    K = build_qn_2_skeleton(n)
    rng = np.random.default_rng(20261126 + n)
    theta = rng.normal(size=len(K.vertices))
    phi = rng.normal(size=len(K.edges))
    omega = np.zeros(len(K.vertices))
    omega_link = np.zeros(len(K.edges))
    theta_dot, phi_dot = rhs(K, theta, phi, omega, omega_link, 0.7, model)
    orders = order_parameters(K, theta, phi)
    assert theta_dot.shape == theta.shape
    assert phi_dot.shape == phi.shape
    assert set(orders) == {"R0", "R1_down", "R1_up"}
    assert np.all(np.isfinite(theta_dot))
    assert np.all(np.isfinite(phi_dot))
    assert all(0.0 <= value <= 1.0 for value in orders.values())
