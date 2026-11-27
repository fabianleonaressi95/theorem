import numpy as np
from dec_se3.se3 import random_rotation
from dec_se3.connection import SE3Connection
from dec_se3.holonomy import face_holonomy

def icosahedron_faces():
    """A minimal closed oriented surface fixture for regression testing.

    This is not a geometric C60 mesh; it is a deterministic 20-face
    icosahedral connectivity fixture used to ensure that the C60-facing
    surface API remains stable.
    """
    phi = (1 + 5 ** 0.5) / 2
    verts = np.array([
        [-1, phi, 0], [1, phi, 0], [-1, -phi, 0], [1, -phi, 0],
        [0, -1, phi], [0, 1, phi], [0, -1, -phi], [0, 1, -phi],
        [phi, 0, -1], [phi, 0, 1], [-phi, 0, -1], [-phi, 0, 1],
    ])
    faces = [
        (0, 11, 5), (0, 5, 1), (0, 1, 7), (0, 7, 10), (0, 10, 11),
        (1, 5, 9), (5, 11, 4), (11, 10, 2), (10, 7, 6), (7, 1, 8),
        (3, 9, 4), (3, 4, 2), (3, 2, 6), (3, 6, 8), (3, 8, 9),
        (4, 9, 5), (2, 4, 11), (6, 2, 10), (8, 6, 7), (9, 8, 1),
    ]
    return verts, faces

def test_surface_has_20_faces_and_12_vertices():
    verts, faces = icosahedron_faces()
    assert len(verts) == 12
    assert len(faces) == 20

def test_face_holonomy_is_computable_on_surface():
    verts, faces = icosahedron_faces()
    rng = np.random.default_rng(41)
    edges = {}
    for f in faces:
        for a, b in zip(f, f[1:] + f[:1]):
            if (a, b) not in edges and (b, a) not in edges:
                edges[(a, b)] = (random_rotation(rng), rng.normal(size=3))
    conn = SE3Connection(edges)
    for f in faces:
        loop = [(f[i], f[(i + 1) % len(f)]) for i in range(len(f))]
        R, b = face_holonomy(conn, loop)
        assert R.shape == (3, 3)
        assert b.shape == (3,)

def test_no_volumetric_bianchi_claim_on_surface():
    verts, faces = icosahedron_faces()
    assert all(len(f) == 3 for f in faces)
    assert not any(len(f) == 4 for f in faces)
