import numpy as np

def se3(R, t):
    R = np.asarray(R, dtype=float)
    t = np.asarray(t, dtype=float).reshape(3)
    assert R.shape == (3, 3)
    return (R, t)

def identity():
    return (np.eye(3), np.zeros(3))

def compose(a, b):
    R2, t2 = a
    R1, t1 = b
    return (R2 @ R1, t2 + R2 @ t1)

def inverse(a):
    R, t = a
    return (R.T, -R.T @ t)

def apply(a, x):
    R, t = a
    return R @ np.asarray(x, dtype=float).reshape(3) + t

def rotation_from_axis_angle(axis, angle):
    axis = np.asarray(axis, dtype=float)
    axis = axis / np.linalg.norm(axis)
    K = np.array([[0, -axis[2], axis[1]],
                  [axis[2], 0, -axis[0]],
                  [-axis[1], axis[0], 0]])
    return np.eye(3) + np.sin(angle) * K + (1 - np.cos(angle)) * (K @ K)

def random_rotation(rng):
    q = rng.normal(size=4)
    q /= np.linalg.norm(q)
    w, x, y, z = q
    return np.array([
        [1-2*(y*y+z*z), 2*(x*y-z*w), 2*(x*z+y*w)],
        [2*(x*y+z*w), 1-2*(x*x+z*z), 2*(y*z-x*w)],
        [2*(x*z-y*w), 2*(y*z+x*w), 1-2*(x*x+y*y)],
    ])
