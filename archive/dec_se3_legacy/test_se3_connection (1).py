import numpy as np
from dec_se3.se3 import identity, compose, inverse, random_rotation
from dec_se3.connection import SE3Connection

def test_identity_composition():
    A=identity()
    assert np.allclose(compose(A,A)[0],np.eye(3))
    assert np.allclose(compose(A,A)[1],np.zeros(3))

def test_inverse_law():
    rng=np.random.default_rng(7)
    A=(random_rotation(rng),rng.normal(size=3))
    C=compose(inverse(A),A)
    assert np.allclose(C[0],np.eye(3),atol=1e-13)
    assert np.allclose(C[1],np.zeros(3),atol=1e-13)

def test_edge_inverse_transport():
    rng=np.random.default_rng(11)
    A=(random_rotation(rng),rng.normal(size=3))
    conn=SE3Connection({("v","w"):A})
    assert np.allclose(conn.transport("w","v")[0],A[0].T,atol=1e-13)
    assert np.allclose(conn.transport("w","v")[1],-A[0].T@A[1],atol=1e-13)

def test_path_composition():
    rng=np.random.default_rng(13)
    edges={("a","b"):(random_rotation(rng),rng.normal(size=3)),
           ("b","c"):(random_rotation(rng),rng.normal(size=3))}
    conn=SE3Connection(edges)
    direct=conn.path_transport(["a","b","c"])
    expected=compose(edges[("b","c")],edges[("a","b")])
    assert np.allclose(direct[0],expected[0],atol=1e-13)
    assert np.allclose(direct[1],expected[1],atol=1e-13)

def test_loop_transport_returns_to_start():
    rng=np.random.default_rng(17)
    edges={("a","b"):(random_rotation(rng),rng.normal(size=3)),
           ("b","c"):(random_rotation(rng),rng.normal(size=3)),
           ("c","a"):(random_rotation(rng),rng.normal(size=3))}
    conn=SE3Connection(edges)
    H=conn.loop_transport(["a","b","c","a"])
    assert H[0].shape==(3,3) and H[1].shape==(3,)
