import numpy as np

def covariant_difference(rho, G_vw, u_v, u_w):
    return rho(G_vw) @ u_v - u_w

def vector_representation(A):
    R, _ = A
    return R

def affine_representation(A):
    R, t = A
    M = np.eye(4)
    M[:3, :3] = R
    M[:3, 3] = t
    return M
