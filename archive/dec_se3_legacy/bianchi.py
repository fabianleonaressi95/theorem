import numpy as np
from .se3 import compose, inverse, identity
from .mesh import tet_faces, face_edges

def position_matching_transport(x_v, x_w, R):
    return (R, x_w - R @ x_v)

def build_connection_from_field(vertices, edges, rotation_field):
    transports={}
    for v,w in edges:
        midpoint=0.5*(vertices[v]+vertices[w])
        R=rotation_field(midpoint)
        transports[(v,w)]=position_matching_transport(vertices[v],vertices[w],R)
    return transports

def face_holonomy_element(connection, face):
    H=identity()
    for v,w in face_edges(face):
        H=compose(connection.transport(v,w),H)
    return H

def face_curvature_and_torsion(connection, vertices, face):
    R_f=np.eye(3); T_f=np.zeros(3)
    for v,w in face_edges(face):
        R_e,_=connection.transport(v,w)
        delta=vertices[w]-vertices[v]
        R_f=R_e@R_f
        T_f=T_f+R_e@delta
    return R_f,T_f

def tet_boundary_holonomy(connection, tet):
    """Product of the four face holonomies, all expressed at a common basepoint.

    The three faces incident to v0 are already based at v0. The fourth face
    is based at v1 and is conjugated back to v0 with the transport from v0
    to v1. Each boundary edge then appears once forward and once backward,
    so the product must be the identity in SE(3).
    """
    v0,v1,v2,v3=tet
    faces=[
        (v0,v1,v2),
        (v0,v2,v3),
        (v0,v3,v1),
        (v1,v3,v2),
    ]
    H=identity()
    for face in faces[:3]:
        H=compose(face_holonomy_element(connection,face),H)
    P=connection.transport(v0,v1)
    H4=face_holonomy_element(connection,faces[3])
    H4_at_v0=compose(compose(inverse(P),H4),P)
    H=compose(H4_at_v0,H)
    return H

def tet_torsion_balance(connection, vertices, tet):
    total=np.zeros(3)
    for face in tet_faces(tet):
        _,T_f=face_curvature_and_torsion(connection,vertices,face)
        total=total+T_f
    return total

def curvature_coupling(connection, vertices, tet):
    total=np.zeros(3)
    for face in tet_faces(tet):
        R_f,_=face_curvature_and_torsion(connection,vertices,face)
        edges=face_edges(face)
        representative=vertices[edges[0][1]]-vertices[edges[0][0]]
        total=total+(R_f-np.eye(3))@representative
    return total
