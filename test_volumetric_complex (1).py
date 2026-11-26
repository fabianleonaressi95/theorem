import numpy as np
from dec_se3.mesh import (cube_tetrahedralization, tet_faces, face_edges,
    boundary_faces, icosahedron_volumetric_complex)
from dec_se3.se3 import random_rotation, identity, compose, inverse
from dec_se3.connection import SE3Connection
from dec_se3.bianchi import (build_connection_from_field,
    face_curvature_and_torsion, tet_boundary_holonomy,
    tet_torsion_balance, curvature_coupling)

def rotation_field(axis, strength):
    axis=np.asarray(axis,dtype=float); axis=axis/np.linalg.norm(axis)
    def field(x):
        angle=strength*float(np.dot(x,axis))
        K=np.array([[0,-axis[2],axis[1]],[axis[2],0,-axis[0]],[-axis[1],axis[0],0]])
        return np.eye(3)+np.sin(angle)*K+(1-np.cos(angle))*(K@K)
    return field

def build_cube_connection(n=1, strength=0.15):
    vertices,tets=cube_tetrahedralization(n=n)
    edges=set()
    for tet in tets:
        for face in tet_faces(tet):
            for a,b in face_edges(face):
                edges.add((min(a,b),max(a,b)))
    edges=sorted(edges)
    field=rotation_field([0.2,0.7,0.6],strength)
    transports=build_connection_from_field(vertices,edges,field)
    return vertices,tets,edges,SE3Connection(transports),transports

def test_cube_mesh_has_six_tets_per_cube():
    vertices,tets=cube_tetrahedralization(n=2)
    assert len(tets)==6*8
    assert all(len(t)==4 for t in tets)

def test_cube_boundary_is_closed():
    vertices,tets=cube_tetrahedralization(n=2)
    boundary=boundary_faces(tets)
    assert len(boundary)>0
    assert all(len(f)==3 for f in boundary)

def test_icosahedron_complex_has_c60_boundary_topology():
    vertices,tets,faces=icosahedron_volumetric_complex()
    assert len(vertices)==13 and len(tets)==20 and len(faces)==20
    assert len(boundary_faces(tets))==20

def test_every_tet_boundary_holonomy_is_identity():
    vertices,tets,edges,conn,transports=build_cube_connection(n=1)
    for tet in tets:
        H=tet_boundary_holonomy(conn,tet)
        assert np.allclose(H[0],np.eye(3),atol=1e-12)
        assert np.allclose(H[1],np.zeros(3),atol=1e-12)

def test_face_curvature_is_nonzero_for_twisted_field():
    vertices,tets,edges,conn,transports=build_cube_connection(n=1,strength=0.4)
    curvatures=[]
    for tet in tets:
        for face in tet_faces(tet):
            R,T=face_curvature_and_torsion(conn,vertices,face)
            curvatures.append(np.linalg.norm(R-np.eye(3)))
    assert max(curvatures)>1e-6

def test_position_matching_holonomy_fixes_basepoint():
    vertices,tets,edges,conn,transports=build_cube_connection(n=1)
    for tet in tets:
        for face in tet_faces(tet):
            H=conn.loop_transport(list(face)+[face[0]])
            x0=vertices[face[0]]
            assert np.allclose(H[0]@x0+H[1],x0,atol=1e-12)

def test_pure_translation_defect_is_detectable():
    t=np.array([0.3,-0.2,0.5])
    conn=SE3Connection({
        ("a","b"):(np.eye(3),t),
        ("b","c"):(np.eye(3),t),
        ("c","a"):(np.eye(3),-2*t+np.array([0.4,0.1,-0.2])),
    })
    H=conn.loop_transport(["a","b","c","a"])
    R,b=H
    assert np.allclose(R,np.eye(3),atol=1e-14)
    assert not np.allclose(b,np.zeros(3),atol=1e-14)

def test_torsion_balance_and_coupling_are_finite():
    vertices,tets,edges,conn,transports=build_cube_connection(n=1,strength=0.3)
    for tet in tets:
        balance=tet_torsion_balance(conn,vertices,tet)
        coupling=curvature_coupling(conn,vertices,tet)
        assert np.all(np.isfinite(balance))
        assert np.all(np.isfinite(coupling))
        assert balance.shape==(3,) and coupling.shape==(3,)

def test_icosahedron_boundary_holonomy_identity():
    vertices,tets,faces=icosahedron_volumetric_complex()
    edges=set()
    for tet in tets:
        for face in tet_faces(tet):
            for a,b in face_edges(face):
                edges.add((min(a,b),max(a,b)))
    edges=sorted(edges)
    field=rotation_field([0.1,0.8,0.5],0.25)
    transports=build_connection_from_field(vertices,edges,field)
    conn=SE3Connection(transports)
    for tet in tets:
        H=tet_boundary_holonomy(conn,tet)
        assert np.allclose(H[0],np.eye(3),atol=1e-12)
        assert np.allclose(H[1],np.zeros(3),atol=1e-12)
