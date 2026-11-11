"""Exact metric-graph masses and Bernoulli moments for the Q6 D4 orbit.

Six-bit labels are embedded in [0,1]^6. Edge lengths are 1 or sqrt(2).
The script assembles the consistent P1 vertex mass W0 and constant
Whitney-1 edge mass W1 over Q(sqrt(2)). It deliberately does not assign
areas or W2 masses to combinatorial orbit squares.
"""
from __future__ import annotations
import json
from collections import Counter
from fractions import Fraction
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
        raise AssertionError("expected D4 order 8")
    return tuple(sorted(G))

def _add(a,b):
    return (a[0]+b[0],a[1]+b[1])

def _scale(a,q):
    return (a[0]*q,a[1]*q)

def run_audit():
    K=build_q6_complex(); G=_group(K)
    edges=set()
    for g in G:
        for u,v in K.edges:
            edges.add(tuple(sorted((g[u],g[v]))))
    edges=tuple(sorted(edges))
    if len(edges)!=256:
        raise AssertionError(f"expected 256 edges, got {len(edges)}")

    # Q(sqrt(2)): pair (a,b) represents a+b*sqrt(2).
    W0=[[(Fraction(0),Fraction(0)) for _ in range(64)] for _ in range(64)]
    W1=[]; lengths=Counter()
    for u,v in edges:
        x,y=K.vertices[u],K.vertices[v]
        d2=sum((a^b)**2 for a,b in zip(x,y))
        if d2 not in (1,2):
            raise AssertionError(f"unexpected squared length {d2}")
        L=(Fraction(1),Fraction(0)) if d2==1 else (Fraction(0),Fraction(1))
        invL=(Fraction(1),Fraction(0)) if d2==1 else (Fraction(0),Fraction(1,2))
        lengths[d2]+=1
        for a,b,q in ((u,u,Fraction(1,3)),(v,v,Fraction(1,3)),
                      (u,v,Fraction(1,6)),(v,u,Fraction(1,6))):
            W0[a][b]=_add(W0[a][b],_scale(L,q))
        W1.append(invL)

    symmetric=all(W0[i][j]==W0[j][i] for i in range(64) for j in range(64))
    positive_diagonal=all(W0[i][i][0]>0 or W0[i][i][1]>0 for i in range(64))
    segment_moments={str(2*r):str(Fraction(1,(2**(2*r))*(2*r+1))) for r in range(1,5)}
    return {
      "audit":"Q6_D4_ORBIT_GRAPH_GEOMETRIC_MASS_BERNOULLI_V1",
      "embedding":"six-bit labels as vertices of [0,1]^6",
      "field":"Q(sqrt(2)); pairs (a,b) represent a+b*sqrt(2)",
      "counts":{"vertices":64,"orbit_edges":len(edges),
                "edge_squared_lengths":{str(k):v for k,v in sorted(lengths.items())}},
      "W0":{"definition":"consistent P1 edge mass; local L/6 [[2,1],[1,2]]",
            "shape":[64,64],"symmetric_exact":symmetric,
            "positive_diagonal_exact":positive_diagonal,
            "positive_definite_argument":"sum of positive-definite local edge masses; graph has no isolated vertices"},
      "W1":{"definition":"constant Whitney 1-form edge mass; integral |a/L|^2 ds = a^2/L",
            "shape":[256,256],"positive_diagonal_exact":all(a>0 or b>0 for a,b in W1),
            "inverse_lengths":{"unit":"1","sqrt2":"sqrt(2)/2"}},
      "segment_moments":segment_moments,
      "segment_cumulants":{"kappa2":"1/12","kappa4":"-1/120","kappa6":"1/252","kappa8":"-1/240"},
      "bernoulli_identity":"log(sinh(z/2)/(z/2)) = sum B_(2r) z^(2r)/(2r(2r)!)",
      "boundary":"No W2: orbit square cycles are not assumed planar regular cells in this embedding.",
      "status":{"exact":["orbit edge lengths","W0 and W1 entries over Q(sqrt(2))","segment moments and cumulants"],
                "open":["geometric filling and W2 for orbit squares","full weighted 2D Hodge spectrum","Mosco/FEEC convergence","Bernoulli-corrected Liouville-Bergman density"]}
    }

if __name__=="__main__":
    print(json.dumps(run_audit(),indent=2,sort_keys=True))
