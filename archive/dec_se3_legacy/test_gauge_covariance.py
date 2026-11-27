import numpy as np
from dec_se3.se3 import identity, compose, inverse, random_rotation
from dec_se3.connection import SE3Connection
from dec_se3.covariant_derivative import covariant_difference, vector_representation

def transformed_connection(conn, frames):
    new = {}
    for (u, v), A in conn._g.items():
        if (v, u) in new:
            continue
        h_v, h_w = frames[u], frames[v]
        new[(u, v)] = compose(compose(h_w, A), inverse(h_v))
    return SE3Connection(new)

def test_covariant_difference_gauge_covariance():
    rng = np.random.default_rng(23)
    A = (random_rotation(rng), rng.normal(size=3))
    conn = SE3Connection({("v", "w"): A})
    u_v = rng.normal(size=3)
    u_w = rng.normal(size=3)

    h_v = (random_rotation(rng), rng.normal(size=3))
    h_w = (random_rotation(rng), rng.normal(size=3))
    conn2 = transformed_connection(conn, {"v": h_v, "w": h_w})

    rho = vector_representation
    # The cochain itself must transform with the local frames.
    u_v_prime = h_v[0] @ u_v
    u_w_prime = h_w[0] @ u_w

    d1 = covariant_difference(rho, conn.transport("v", "w"), u_v, u_w)
    d2 = covariant_difference(
        rho, conn2.transport("v", "w"), u_v_prime, u_w_prime
    )

    expected = h_w[0] @ d1
    assert np.allclose(d2, expected, atol=1e-12)

def test_flat_connection_has_zero_curvature():
    conn = SE3Connection({
        ("a", "b"): identity(),
        ("b", "c"): identity(),
        ("c", "a"): identity(),
    })
    H = conn.loop_transport(["a", "b", "c", "a"])
    assert np.allclose(H[0], np.eye(3), atol=1e-14)
    assert np.allclose(H[1], np.zeros(3), atol=1e-14)

def test_pure_translation_defect_has_no_rotation():
    t = np.array([0.3, -0.7, 1.1])
    conn = SE3Connection({
        ("a", "b"): (np.eye(3), t),
        ("b", "c"): (np.eye(3), t),
        ("c", "a"): (np.eye(3), -2*t + np.array([0.4, -0.2, 0.9])),
    })
    H = conn.loop_transport(["a", "b", "c", "a"])
    R, b = H
    assert np.allclose(R, np.eye(3), atol=1e-14)
    assert not np.allclose(b, np.zeros(3), atol=1e-14)
