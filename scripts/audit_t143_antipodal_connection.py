#!/usr/bin/env python3
"""Antipodal SO(3)/Spin(3) audit for the RGS Q6 connection.

Input: RGS_PSU_all_matrices.npz (X_Oh_reconstructed, Q6_adjacency).
The connection is reconstructed as in build_connection.py: minimal SO(3)
rotations between normalized embedded vertex vectors. Spin(3) objects are
canonical quaternion lifts, not a replay of the archived U_SU2 array.
"""
import argparse, json
from pathlib import Path
import numpy as np

MASK, N, D = 7, 64, 6
I3 = np.eye(3)

def skew(v):
    x,y,z=v
    return np.array([[0.,-z,y],[z,0.,-x],[-y,x,0.]])

def minimal_rotation(a,b):
    c=float(np.clip(a@b,-1.,1.)); v=np.cross(a,b); s=float(np.linalg.norm(v))
    if s<1e-14:
        if c>0: return I3.copy()
        ref=np.array([1.,0.,0.]) if abs(a[0])<.8 else np.array([0.,1.,0.])
        u=np.cross(a,ref); u/=np.linalg.norm(u)
        return 2.*np.outer(u,u)-I3
    V=skew(v/s)
    return I3+V*s+(V@V)*(1.-c)

def quat_from_rotation(R):
    w=.5*np.sqrt(max(0.,1.+np.trace(R)))
    if w<1e-12:
        vals,vecs=np.linalg.eigh((R+I3)/2.)
        axis=vecs[:,int(np.argmax(vals))]; axis/=np.linalg.norm(axis)
        q=np.r_[0.,axis]
    else:
        q=np.array([w,(R[2,1]-R[1,2])/(4*w),
                    (R[0,2]-R[2,0])/(4*w),(R[1,0]-R[0,1])/(4*w)])
    q/=np.linalg.norm(q)
    return q if q[0]>=0 else -q

def qmul(a,b):
    aw,ax,ay,az=a; bw,bx,by,bz=b
    return np.array([aw*bw-ax*bx-ay*by-az*bz,
      aw*bx+ax*bw+ay*bz-az*by, aw*by-ax*bz+ay*bw+az*bx,
      aw*bz+ax*by-ay*bx+az*bw])

def qinv(q): return q*np.array([1.,-1.,-1.,-1.])

def qcomm(a,b):
    c=qmul(qmul(qmul(a,b),qinv(a)),qinv(b))
    return min(np.linalg.norm(c-np.array([1.,0.,0.,0.])),
               np.linalg.norm(c+np.array([1.,0.,0.,0.])))

def build_audit(X, adjacency):
    if X.shape!=(N,3) or adjacency.shape!=(N,N):
        raise ValueError("expected X (64,3) and Q6_adjacency (64,64)")
    norms=np.linalg.norm(X,axis=1)
    if np.any(norms<1e-12): raise ValueError("zero embedding vector")
    n=X/norms[:,None]
    p_argmin=np.argmin(np.linalg.norm(X[:,None,:]+X[None,:,:],axis=2),axis=1)
    p_xor=np.arange(N)^MASK
    anti_res=np.linalg.norm(X[p_xor]+X,axis=1)
    adj_res=float(np.max(np.abs(adjacency[np.ix_(p_xor,p_xor)]-adjacency)))
    R,U={},{}
    for g in range(N):
        for h in np.flatnonzero(adjacency[g]):
            h=int(h); R[g,h]=minimal_rotation(n[g],n[h])
            U[g,h]=quat_from_rotation(R[g,h])
    so3err=[]; spinerr=[]
    for (g,h),rgh in R.items():
        pg,ph=int(p_xor[g]),int(p_xor[h])
        so3err.append(np.linalg.norm(R[pg,ph]-rgh,ord="fro"))
        spinerr.append(min(np.linalg.norm(U[pg,ph]-U[g,h]),
                           np.linalg.norm(U[pg,ph]+U[g,h])))
    faces=[]
    for a in range(D):
      for b in range(a+1,D):
       for g in range(N):
        if ((g>>a)&1) or ((g>>b)&1): continue
        i=g; j=g^(1<<a); k=g^(1<<a)^(1<<b); l=g^(1<<b)
        H=R[l,i]@R[k,l]@R[j,k]@R[i,j]
        qH=qmul(qmul(qmul(U[l,i],U[k,l]),U[j,k]),U[i,j])
        angle=float(np.arccos(np.clip((np.trace(H)-1.)/2.,-1.,1.)))
        faces.append((i,j,k,l,H,qH,angle))
    if len(faces)!=240: raise AssertionError("expected 240 square faces")
    herr=[]; qherr=[]; aerr=[]; hol=[]
    for i,j,k,l,H,qH,angle in faces:
        pi,pj,pk,pl=(v^MASK for v in (i,j,k,l))
        Hp=R[pl,pi]@R[pk,pl]@R[pj,pk]@R[pi,pj]
        qHp=qmul(qmul(qmul(U[pl,pi],U[pk,pl]),U[pj,pk]),U[pi,pj])
        herr.append(np.linalg.norm(Hp-H,ord="fro"))
        qherr.append(min(np.linalg.norm(qHp-qH),np.linalg.norm(qHp+qH)))
        ap=float(np.arccos(np.clip((np.trace(Hp)-1.)/2.,-1.,1.)))
        aerr.append(abs(ap-angle)); hol.append(qH)
    comm=[qcomm(hol[i],hol[j]) for i in range(len(hol)) for j in range(i)]
    noncomm=sum(x>1e-8 for x in comm)
    result={
      "status":"PASS_RECONSTRUCTED_GEOMETRIC_CONNECTION_ARCHIVED_SU2_NOT_REPLAYED",
      "antipodal":{"argmin_matches_xor7":bool(np.array_equal(p_argmin,p_xor)),
        "involution":bool(np.array_equal(p_xor[p_xor],np.arange(N))),
        "max_X_antipodal_residual":float(anti_res.max()),
        "Q6_adjacency_automorphism_max_residual":adj_res},
      "link_transport":{"directed_edges":len(R),
        "SO3_antipodal_max_residual":float(max(so3err)),
        "canonical_Spin3_lift_projective_max_residual":float(max(spinerr))},
      "plaquette_holonomy":{"faces":len(faces),
        "angle_mean":float(np.mean([f[6] for f in faces])),
        "angle_rms":float(np.sqrt(np.mean([f[6]**2 for f in faces]))),
        "angle_max":float(max(f[6] for f in faces)),
        "antipodal_SO3_max_residual":float(max(herr)),
        "antipodal_Spin3_projective_max_residual":float(max(qherr)),
        "antipodal_angle_max_residual":float(max(aerr))},
      "nonabelianity":{"unordered_holonomy_pairs":len(comm),
        "noncommuting_pairs_mod_centre":int(noncomm),
        "max_commutator_distance_to_centre":float(max(comm)),
        "interpretation":"The reconstructed Spin(3) plaquette holonomies have no common invariant complex line in the fundamental representation; this connection does not select one global U(1) phase line."},
      "scope":["SO(3) transports are reconstructed from X using the minimal-rotation rule in build_connection.py.",
        "Spin(3) links are canonical quaternion lifts, not the archived U_SU2 array.",
        "Direct comparison with archived U_SU2, including edge ordering and signs, remains pending.",
        "Noncommuting full holonomy family rules out a common invariant line for this fundamental representation, not every possible associated-bundle construction.",
        "No map from the 29 diagonal angles to connection holonomies is assumed."]}
    result["checks_pass"]=bool(result["antipodal"]["argmin_matches_xor7"] and
      result["antipodal"]["involution"] and adj_res<1e-12 and max(so3err)<1e-12 and
      max(spinerr)<1e-12 and max(herr)<1e-12 and max(qherr)<1e-12 and
      max(aerr)<1e-12 and noncomm>0)
    return result

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--archive",default="RGS_PSU_all_matrices.npz")
    ap.add_argument("--out",default="T143_antipodal_connection_audit.json")
    args=ap.parse_args()
    with np.load(args.archive,allow_pickle=True) as z:
        report=build_audit(np.asarray(z["X_Oh_reconstructed"],float),
                           np.asarray(z["Q6_adjacency"],float))
    Path(args.out).write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))
    raise SystemExit(0 if report["checks_pass"] else 1)
if __name__=="__main__": main()
