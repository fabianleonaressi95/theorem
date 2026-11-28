"""Exact lattice connection-difference identity for the two Q6 branches.

For edge g->h, links map source-frame vectors to target-frame vectors.
The relative link V_gh = Uc_gh (Uw_gh)^(-1) is an SO(3) element at h,
and transforms by conjugation at h. Its principal logarithm is a discrete
connection-difference/contorsion candidate. No continuum 1-form is claimed.
"""
import json
import numpy as np
from scripts.audit_q6_discrete_cartan import (
    I3, reconstruct_seed, spatial_coframes, build_discrete_cartan, q6_squares
)
from scripts.audit_q6_teleparallel_branch import build_teleparallel_branch

def so3_log(R):
    c = float(np.clip((np.trace(R)-1.0)/2.0, -1.0, 1.0))
    angle = float(np.arccos(c))
    if angle < 1e-10:
        return 0.5 * (R - R.T)
    if np.pi-angle < 1e-7:
        vals, vecs = np.linalg.eigh((R+I3)/2.0)
        axis = vecs[:, np.argmax(vals)]
        axis /= np.linalg.norm(axis)
    else:
        axis = np.array([R[2,1]-R[1,2], R[0,2]-R[2,0], R[1,0]-R[0,1]])
        axis /= 2.0*np.sin(angle)
    x,y,z = axis*angle
    return np.array([[0.,-z,y],[z,0.,-x],[-y,x,0.]])

def so3_exp(A):
    v=np.array([A[2,1],A[0,2],A[1,0]])
    a=float(np.linalg.norm(v))
    if a < 1e-12:
        return I3+A+0.5*(A@A)
    K=A/a
    return I3+np.sin(a)*K+(1.-np.cos(a))*(K@K)

def build_connection_difference():
    X,edges=reconstruct_seed()
    E=spatial_coframes(X)
    curved=build_discrete_cartan(X,edges,E)
    flat=build_teleparallel_branch(X,edges,E)
    V=np.asarray([Uc@Uw.T for Uc,Uw in zip(curved["links"],flat["links"])])
    A=np.asarray([so3_log(v) for v in V])
    reconstruction=max(float(np.linalg.norm(so3_exp(a)-v)) for a,v in zip(A,V))
    edge_index={(int(g),int(h)):i for i,(g,h,_) in enumerate(edges)}
    def oriented(a,b):
        if a<b:
            i=edge_index[(a,b)]
            return curved["links"][i],flat["links"][i],V[i]
        i=edge_index[(b,a)]
        return curved["links"][i].T,flat["links"][i].T,V[i].T
    face_res=[]
    for p in q6_squares():
        Hc,Hw=I3.copy(),I3.copy()
        for a,b in zip(p,p[1:]+p[:1]):
            uc,uw,_=oriented(a,b)
            Hc=uc@Hc
            Hw=uw@Hw
        # Exact identity: Hc = (V3)(Uw3 V2 Uw3^-1)...
        # The direct factorization is checked using the sequential recurrence.
        Q=I3.copy()
        for a,b in zip(p,p[1:]+p[:1]):
            uc,uw,v=oriented(a,b)
            Q=(v@uw)@Q
        face_res.append(float(np.linalg.norm(Hc-Q)))
    return {
        "status":"EXACT_FINITE_LATTICE_CONNECTION_DIFFERENCE_IDENTITY",
        "carrier":{"vertices":64,"edges":192,"faces":240},
        "relative_link_definition":"V_gh = U_curved,gh (U_flat,gh)^(-1), based at target vertex h",
        "transformation_law":"V'_gh = G_h V_gh G_h^(-1)",
        "discrete_contorsion_candidate":"A_gh = Log(V_gh) in so(3), principal branch",
        "factorization":"U_curved,gh = Exp(A_gh) U_flat,gh",
        "max_link_reconstruction_residual":reconstruction,
        "max_face_factorization_residual":max(face_res),
        "relative_rotation_angle_mean_rad":float(np.mean([np.linalg.norm([a[2,1],a[0,2],a[1,0]]) for a in A])),
        "scope":["This is an exact finite link-group identity, not the continuum Cartan contorsion 1-form.",
                 "The logarithm is branch-dependent near rotation angle pi.",
                 "A continuum limit requires refinement, compatible coframes, and a discrete covariant derivative.",
                 "No Lorentzian lift, physical time leg, action, or field equations are established."]
    }

if __name__=="__main__":
    r=build_connection_difference()
    print(json.dumps(r,indent=2))
    if r["max_link_reconstruction_residual"]>1e-10 or r["max_face_factorization_residual"]>1e-12:
        raise SystemExit("connection-difference identity failed")
