"""Exact D4-equivariant edge Hodge audit on the full M3 orbit graph.

The 2-cells are the distinct unoriented cyclic square boundaries in the
D4-orbit of the original Q6 square faces. Cycles with the same vertex set
but different cyclic order are retained as distinct labelled 2-cells.
All ranks, nullspaces and eigenvalue multiplicities are computed over QQ.
"""
from __future__ import annotations

import json
import sympy as sp
from models.q6_topological_synchronization import build_q6_complex


def _r(v):
    b1,b2,b3,s1,s2,s3=v
    return (b1,b2,b3^b1^b2,s2,1^s1,s3)


def _s(v):
    b1,b2,b3,s1,s2,s3=v
    return (b1,b2,b3,1^s1,s2,s3)


def _compose(g,h):
    return tuple(g[h[i]] for i in range(64))


def _group(K):
    R=tuple(K.vertex_index[_r(v)] for v in K.vertices)
    S=tuple(K.vertex_index[_s(v)] for v in K.vertices)
    I=tuple(range(64)); G={I}; todo=[I]
    while todo:
        g=todo.pop()
        for x in (R,S):
            for y in (_compose(x,g),_compose(g,x)):
                if y not in G:
                    G.add(y); todo.append(y)
    if len(G)!=8:
        raise ArithmeticError(f"D4 order is {len(G)}, not 8")
    return R,S,tuple(sorted(G))


def _canon(c):
    c=tuple(c); forms=[]
    for x in (c,tuple(reversed(c))):
        forms.extend(x[i:]+x[:i] for i in range(4))
    return min(forms)


def _sign(c,canon):
    c=tuple(c); canon=tuple(canon)
    for i in range(4):
        if c[i:]+c[:i]==canon: return 1
    rev=tuple(reversed(canon))
    for i in range(4):
        if c[i:]+c[:i]==rev: return -1
    raise ArithmeticError("not the same unoriented cyclic cell")


def run_audit():
    K=build_q6_complex()
    R,S,G=_group(K)
    edge_set=set()
    for g in G:
        for a,b in K.edges:
            edge_set.add(tuple(sorted((g[a],g[b]))))
    edges=tuple(sorted(edge_set)); ei={e:i for i,e in enumerate(edges)}
    if len(edges)!=256: raise ArithmeticError(f"orbit graph has {len(edges)} edges")

    face_set=set()
    for g in G:
        for face in K.faces:
            face_set.add(_canon(tuple(g[v] for v in face)))
    faces=tuple(sorted(face_set)); fi={f:i for i,f in enumerate(faces)}

    B1=sp.zeros(64,len(edges))
    for j,(u,v) in enumerate(edges):
        B1[u,j]=-1; B1[v,j]=1
    B2=sp.zeros(len(edges),len(faces))
    for j,f in enumerate(faces):
        for u,v in zip(f,f[1:]+f[:1]):
            key=(min(u,v),max(u,v))
            if key not in ei: raise ArithmeticError("missing orbit edge")
            B2[ei[key],j]+=1 if u<v else -1
    if B1*B2 != sp.zeros(64,len(faces)):
        raise ArithmeticError("B1 B2 is not zero")

    def edge_action(g):
        J=sp.zeros(len(edges),len(edges))
        for j,(u,v) in enumerate(edges):
            gu,gv=g[u],g[v]
            J[ei[(min(gu,gv),max(gu,gv))],j]=1 if gu<gv else -1
        return J

    def face_action(g):
        J=sp.zeros(len(faces),len(faces))
        for j,f in enumerate(faces):
            image=tuple(g[v] for v in f)
            target=_canon(image)
            J[fi[target],j]=_sign(image,target)
        return J

    maps=[]
    for g in G:
        J0=sp.zeros(64)
        for i in range(64): J0[g[i],i]=1
        J1=edge_action(g); J2=face_action(g)
        if J0*B1 != B1*J1 or J1*B2 != B2*J2:
            raise ArithmeticError("D4 action fails to be a chain map")
        maps.append((J0,J1,J2))

    # Edge Hodge Laplacian: d_0 d_0^* + d_1^* d_1.
    H1=B1.T*B1+B2*B2.T
    Hco=B2*B2.T
    rank_B1=B1.rank(); rank_B2=B2.rank()
    beta1=len(edges)-rank_B1-rank_B2
    spectrum=H1.eigenvals()
    co_spectrum=Hco.eigenvals()

    def _eigenspace_report(operator, spectral_data):
        details={}
        for eig,mult in spectral_data.items():
            V=sp.Matrix.hstack(*((operator-eig*sp.eye(operator.rows)).nullspace()))
            traces=[]
            invariant=True
            for _J0,J1,_J2 in maps:
                image=J1*V
                coeff=(V.T*V).inv()*V.T*image
                if V*coeff != image: invariant=False
                traces.append(int(sp.trace(coeff)))
            details[str(eig)]={
                "multiplicity":int(mult),
                "D4_invariant":invariant,
                "character_traces_in_group_order":traces,
            }
        return details

    eig_details=_eigenspace_report(H1,spectrum)
    co_details=_eigenspace_report(Hco,co_spectrum)
    positive=[{"eigenvalue":str(eig),"multiplicity":int(mult)}
              for eig,mult in co_spectrum.items() if eig != 0]
    return {
        "audit":"M3_D4_ORBIT_EDGE_HODGE_EXACT",
        "arithmetic":"SymPy exact rational/integer",
        "counts":{"vertices":64,"edges":len(edges),"square_2_cells":len(faces)},
        "boundary":{"B1_shape":list(B1.shape),"B2_shape":list(B2.shape),
                    "rank_B1":rank_B1,"rank_B2":rank_B2,
                    "B1B2_zero":True,"beta1":beta1},
        "edge_hodge":{"definition":"B1.T*B1 + B2*B2.T",
                      "spectrum":positive,"zero_multiplicity":int(spectrum.get(0,0)),
                      "eigenspaces":eig_details},
        "coexact_hodge":{"definition":"B2*B2.T",
                         "positive_spectrum":positive,
                         "zero_multiplicity":int(co_spectrum.get(0,0)),
                         "eigenspaces":co_details},
        "D4":{"order":len(G),"all_eight_signed_chain_maps_exact":True},
        "five_dimensional_positive_eigenspaces":[
            {"eigenvalue":k,"multiplicity":v["multiplicity"],
             "character_traces":v["character_traces_in_group_order"]}
            for k,v in co_details.items() if k != "0" and v["multiplicity"]==5
        ],
    }


if __name__=="__main__":
    print(json.dumps(run_audit(),indent=2,sort_keys=True))
