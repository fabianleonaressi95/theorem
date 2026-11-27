import numpy as np
from .se3 import compose

def face_holonomy(connection, face_edges):
    H = (np.eye(3), np.zeros(3))
    for u, v in face_edges:
        H = compose(connection.transport(u, v), H)
    R, b = H
    return R, b

def rotational_defect(R):
    return R - np.eye(3)

def translational_defect(b):
    return np.asarray(b, dtype=float)
