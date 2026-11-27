import numpy as np

def cube_tetrahedralization(n=1, origin=(0.0,0.0,0.0), size=(1.0,1.0,1.0)):
    ox, oy, oz = origin
    sx, sy, sz = size
    xs = np.linspace(ox, ox+sx, n+1)
    ys = np.linspace(oy, oy+sy, n+1)
    zs = np.linspace(oz, oz+sz, n+1)
    vertices=[]; index={}
    for k,z in enumerate(zs):
        for j,y in enumerate(ys):
            for i,x in enumerate(xs):
                index[(i,j,k)]=len(vertices)
                vertices.append([x,y,z])
    vertices=np.asarray(vertices,dtype=float)
    tets=[]
    for k in range(n):
        for j in range(n):
            for i in range(n):
                v000=index[(i,j,k)]; v100=index[(i+1,j,k)]
                v010=index[(i,j+1,k)]; v110=index[(i+1,j+1,k)]
                v001=index[(i,j,k+1)]; v101=index[(i+1,j,k+1)]
                v011=index[(i,j+1,k+1)]; v111=index[(i+1,j+1,k+1)]
                tets += [
                    (v000,v100,v110,v111),
                    (v000,v100,v111,v101),
                    (v000,v111,v011,v001),
                    (v000,v110,v010,v011),
                    (v000,v111,v001,v101),
                    (v000,v110,v111,v011),
                ]
    return vertices, tets

def tet_faces(tet):
    a,b,c,d = tet
    return [(a,b,c),(a,c,d),(a,d,b),(b,d,c)]

def face_edges(face):
    a,b,c = face
    return [(a,b),(b,c),(c,a)]

def boundary_faces(tets):
    count={}
    for tet in tets:
        for face in tet_faces(tet):
            key=tuple(sorted(face))
            count[key]=count.get(key,0)+1
    return [face for face,n in count.items() if n==1]

def icosahedron_volumetric_complex():
    phi=(1+5**0.5)/2
    surface=np.array([
        [-1,phi,0],[1,phi,0],[-1,-phi,0],[1,-phi,0],
        [0,-1,phi],[0,1,phi],[0,-1,-phi],[0,1,-phi],
        [phi,0,-1],[phi,0,1],[-phi,0,-1],[-phi,0,1],
    ],dtype=float)
    faces=[
        (0,11,5),(0,5,1),(0,1,7),(0,7,10),(0,10,11),
        (1,5,9),(5,11,4),(11,10,2),(10,7,6),(7,1,8),
        (3,9,4),(3,4,2),(3,2,6),(3,6,8),(3,8,9),
        (4,9,5),(2,4,11),(6,2,10),(8,6,7),(9,8,1),
    ]
    center=len(surface)
    vertices=np.vstack([surface,[[0.0,0.0,0.0]]])
    tets=[(center,a,b,c) for a,b,c in faces]
    return vertices,tets,faces
