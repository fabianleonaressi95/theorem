"""Quaternionic lift of the RGS football-shell tangent space.

A node-wise orthonormal frame is encoded by a unit quaternion. Tangent
displacements are represented as pure-imaginary quaternions and transported
to the ambient frame by q p q^{-1}. The shell tangent stiffness is the
Galerkin pullback T^T K T. No claim is made that every spectral cluster is
a physical triplet: clusters are detected from a declared tolerance.
"""
from __future__ import annotations
import numpy as np


def _unit(v):
    v = np.asarray(v, float)
    n = np.linalg.norm(v)
    if n < 1e-14:
        raise ValueError("cannot normalise a zero vector")
    return v / n


def quaternion_from_matrix(R):
    """Return scalar-first unit quaternion [w,x,y,z] for a proper rotation."""
    R = np.asarray(R, float)
    if R.shape != (3, 3) or not np.allclose(R.T @ R, np.eye(3), atol=1e-8) or np.linalg.det(R) < 0.999999:
        raise ValueError("R must be a proper orthogonal 3x3 matrix")
    tr = np.trace(R)
    if tr > 0:
        s = 2*np.sqrt(tr+1)
        q = np.array([s/4, (R[2,1]-R[1,2])/s, (R[0,2]-R[2,0])/s, (R[1,0]-R[0,1])/s])
    else:
        i = int(np.argmax(np.diag(R)))
        if i == 0:
            s=2*np.sqrt(1+R[0,0]-R[1,1]-R[2,2])
            q=np.array([(R[2,1]-R[1,2])/s,s/4,(R[0,1]+R[1,0])/s,(R[0,2]+R[2,0])/s])
        elif i == 1:
            s=2*np.sqrt(1+R[1,1]-R[0,0]-R[2,2])
            q=np.array([(R[0,2]-R[2,0])/s,(R[0,1]+R[1,0])/s,s/4,(R[1,2]+R[2,1])/s])
        else:
            s=2*np.sqrt(1+R[2,2]-R[0,0]-R[1,1])
            q=np.array([(R[1,0]-R[0,1])/s,(R[0,2]+R[2,0])/s,(R[1,2]+R[2,1])/s,s/4])
    return _unit(q)


def qmul(a, b):
    aw, ax, ay, az = np.asarray(a, float)
    bw, bx, by, bz = np.asarray(b, float)
    return np.array([aw*bw-ax*bx-ay*by-az*bz,
        aw*bx+ax*bw+ay*bz-az*by,
        aw*by-ax*bz+ay*bw+az*bx,
        aw*bz+ax*by-ay*bx+az*bw])


def qconj(q):
    q = np.asarray(q, float)
    return np.array([q[0], -q[1], -q[2], -q[3]])


def qrotate(q, v):
    """Rotate a 3-vector by q p q^{-1}; q and -q give identical results."""
    p = np.r_[0., np.asarray(v, float)]
    return qmul(qmul(q, p), qconj(q))[1:]


def _local_frame(normal):
    n = _unit(normal)
    seed = np.array([1., 0., 0.]) if abs(n[0]) < .8 else np.array([0., 1., 0.])
    e1 = _unit(seed - (seed @ n)*n)
    e2 = _unit(np.cross(n, e1))
    # Columns map local (e1,e2,n) coordinates into global coordinates.
    R = np.column_stack((e1, e2, n))
    return R, quaternion_from_matrix(R)


def build_tangent_quaternion_audit(mesh, stiffness, relative_cluster_tolerance=1e-7):
    """Build local quaternion frames and the 2-DOF/node tangent pullback.

    The returned tangent basis has shape (3N,2N); K_tan is (2N,2N).
    Consecutive eigenvalues are clustered by relative gap. Only clusters of
    exactly three are labelled candidate_triplet, not automatically physical.
    """
    X = np.asarray(mesh["nodes"], float)
    tris = np.asarray(mesh["triangles"], int)
    K = np.asarray(stiffness, float)
    nnode = len(X)
    if K.shape != (3*nnode, 3*nnode):
        raise ValueError("stiffness shape does not match 3N shell coordinates")
    normals = np.zeros((nnode, 3))
    for tri in tris:
        p = X[tri]
        area_normal = np.cross(p[1]-p[0], p[2]-p[0])
        for idx in tri:
            normals[idx] += area_normal
    normals = np.asarray([_unit(v) for v in normals])
    frames=[]; quats=[]; T=np.zeros((3*nnode, 2*nnode))
    for i, normal in enumerate(normals):
        R, q = _local_frame(normal)
        frames.append(R); quats.append(q)
        T[3*i:3*i+3, 2*i:2*i+2] = R[:, :2]
    Ktan = T.T @ K @ T
    Ktan = .5*(Ktan+Ktan.T)
    eig, vec = np.linalg.eigh(Ktan)
    clusters=[]
    start=0
    while start < len(eig):
        end=start+1
        while end < len(eig):
            scale=max(abs(eig[end]),abs(eig[end-1]),1e-14)
            if abs(eig[end]-eig[end-1])/scale > relative_cluster_tolerance:
                break
            end += 1
        size=end-start
        if size == 3:
            clusters.append({"indices":[int(start),int(start+1),int(start+2)],
                "eigenvalues":eig[start:end].tolist(),
                "relative_spread":float((eig[end-1]-eig[start])/max(abs(eig[start]),abs(eig[end-1]),1e-14)),
                "classification":"candidate_triplet"})
        start=end
    # Quaternion transport identity: local tangent coordinates (a,b,0)
    # are sent to ambient coordinates by q (a i + b j) q^{-1}.
    return {
        "coordinate_convention":"scalar-first q=[w,x,y,z]; pure imaginary p=[0,v]; q p q^{-1}",
        "quaternion_double_cover":"q and -q induce the same SO(3) rotation",
        "node_count":int(nnode), "ambient_dof":int(3*nnode),
        "tangent_dof":int(2*nnode), "tangent_basis_rank":int(np.linalg.matrix_rank(T)),
        "quaternion_frames":np.asarray(quats).tolist(),
        "local_frames":np.asarray(frames).tolist(),
        "tangent_basis":T, "tangent_stiffness":Ktan,
        "eigenvalues":eig, "eigenvectors":vec,
        "candidate_triplets":clusters,
        "spectral_cluster_rule":"adjacent relative eigenvalue gap <= relative_cluster_tolerance",
        "relative_cluster_tolerance":float(relative_cluster_tolerance),
        "interpretation":"A threefold numerical cluster is only a candidate. Physical symmetry assignment requires group-action/intertwiner tests and convergence."
    }
