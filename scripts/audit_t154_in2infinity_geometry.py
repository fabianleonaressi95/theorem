#!/usr/bin/env python3
"""Coordinate and sphere audit for the five In2Infinity Extended-Jitterbug solids.
Unit-edge coordinates; standard-library only. Face-plane distances are reported
by face orbit, so non-tangential solids are not assigned a fictitious unique IN sphere.
"""
from itertools import combinations, permutations, product
from math import sqrt

def norm(v): return sqrt(sum(x*x for x in v))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def unique_permutations(items): return sorted(set(permutations(items)))

def vertices_octahedron():
    out=set()
    for i in range(3):
        for s in (-1,1):
            v=[0,0,0]; v[i]=s; out.add(tuple(v))
    return sorted(out)

def vertices_icosahedron():
    phi=(1+sqrt(5))/2; out=set()
    for a,b in product((-1,1),repeat=2):
        out.update(((0,a,b*phi),(a,b*phi,0),(b*phi,0,a)))
    return sorted(out)

def vertices_cuboctahedron():
    out=set()
    for a,b in product((-1,1),repeat=2):
        out.update(((a,b,0),(a,0,b),(0,a,b)))
    return sorted(out)

def tribonacci_constant():
    lo,hi=1.0,2.0
    for _ in range(100):
        m=(lo+hi)/2
        if m**3-m**2-m-1<0: lo=m
        else: hi=m
    return (lo+hi)/2

def vertices_snub_cube():
    t=tribonacci_constant(); base=(1.0,t,1.0/t); out=set()
    for perm in permutations(range(3)):
        inv=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        parity=(-1)**inv
        p=tuple(base[perm[i]] for i in range(3))
        for signs in product((-1,1),repeat=3):
            if signs[0]*signs[1]*signs[2]==parity:
                out.add(tuple(signs[i]*p[i] for i in range(3)))
    return sorted(out)

def vertices_rhombic_cuboctahedron():
    q=1+sqrt(2); out=set()
    for p in unique_permutations((1.0,1.0,q)):
        for signs in product((-1,1),repeat=3):
            out.add(tuple(signs[i]*p[i] for i in range(3)))
    return sorted(out)

def hull_faces(vertices,tol=1e-8):
    faces={}
    for i,j,k in combinations(range(len(vertices)),3):
        a,b,c=vertices[i],vertices[j],vertices[k]
        n=cross(sub(b,a),sub(c,a)); nn=norm(n)
        if nn<tol: continue
        n=tuple(x/nn for x in n); d=dot(n,a)
        signed=[dot(n,p)-d for p in vertices]
        if max(signed)>tol and min(signed)<-tol: continue
        if min(signed)>=-tol and max(signed)>tol: n,d=tuple(-x for x in n),-d
        if d<0: n,d=tuple(-x for x in n),-d
        face=tuple(m for m,p in enumerate(vertices) if abs(dot(n,p)-d)<1e-7)
        if len(face)>=3: faces[face]=d
    return faces

def audit(name,raw):
    edge=min(norm(sub(a,b)) for a,b in combinations(raw,2))
    v=[tuple(x/edge for x in p) for p in raw]
    edges=[(a,b) for a,b in combinations(v,2) if abs(norm(sub(a,b))-1)<1e-6]
    faces=hull_faces(v)
    mids={round(norm(tuple((a[i]+b[i])/2 for i in range(3))),9) for a,b in edges}
    face_radii=sorted({round(d,9) for d in faces.values()})
    return {"name":name,"V":len(v),"E":len(edges),"F":len(faces),
            "face_sizes":sorted({len(f) for f in faces}),"edge":1.0,
            "face_plane_radii":face_radii,"mid_radii":sorted(mids),
            "out_radius":round(max(norm(p) for p in v),9)}

def all_audits():
    models=(("octahedron",vertices_octahedron()),("icosahedron",vertices_icosahedron()),
            ("cuboctahedron",vertices_cuboctahedron()),("snub_cube",vertices_snub_cube()),
            ("rhombic_cuboctahedron",vertices_rhombic_cuboctahedron()))
    return [audit(n,v) for n,v in models]

def main():
    expected={"octahedron":(6,12,8),"icosahedron":(12,30,20),
              "cuboctahedron":(12,24,14),"snub_cube":(24,60,38),
              "rhombic_cuboctahedron":(24,48,26)}
    for r in all_audits():
        assert (r["V"],r["E"],r["F"])==expected[r["name"]]
        assert abs(r["V"]-r["E"]+r["F"]-2)<1e-12
        print(r)
    print("T154 five-solid coordinate/sphere audit: PASS")

if __name__=="__main__": main()
