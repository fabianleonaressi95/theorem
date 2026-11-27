import numpy as np
from dec_se3.se3 import random_rotation
from dec_se3.connection import SE3Connection
from dec_se3.holonomy import face_holonomy, rotational_defect, translational_defect

def square_connection(seed=31):
    rng=np.random.default_rng(seed)
    edges={("v0","v1"):(random_rotation(rng),rng.normal(size=3)),
           ("v1","v2"):(random_rotation(rng),rng.normal(size=3)),
           ("v2","v3"):(random_rotation(rng),rng.normal(size=3)),
           ("v3","v0"):(random_rotation(rng),rng.normal(size=3))}
    return SE3Connection(edges),edges

def test_face_holonomy_shape():
    conn,edges=square_connection()
    face=[("v0","v1"),("v1","v2"),("v2","v3"),("v3","v0")]
    R,b=face_holonomy(conn,face)
    assert R.shape==(3,3) and b.shape==(3,)

def test_face_holonomy_matches_loop():
    conn,edges=square_connection()
    face=[("v0","v1"),("v1","v2"),("v2","v3"),("v3","v0")]
    R,b=face_holonomy(conn,face)
    H=conn.loop_transport(["v0","v1","v2","v3","v0"])
    assert np.allclose(R,H[0],atol=1e-13)
    assert np.allclose(b,H[1],atol=1e-13)

def test_rotation_flat_does_not_imply_translation_flat():
    t=np.array([0.2,0.4,-0.6])
    conn=SE3Connection({
        ("a","b"):(np.eye(3),t),
        ("b","c"):(np.eye(3),t),
        ("c","d"):(np.eye(3),t),
        ("d","a"):(np.eye(3),-3*t+np.array([0.5,0.1,-0.3])),
    })
    R,b=face_holonomy(conn,[("a","b"),("b","c"),("c","d"),("d","a")])
    assert np.allclose(R,np.eye(3),atol=1e-14)
    assert not np.allclose(b,np.zeros(3),atol=1e-14)
