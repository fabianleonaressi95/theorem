#!/usr/bin/env python3
"""T090: Whitney P1 gauge-fluid energy and discrete first-variation audit."""
from __future__ import annotations
import json
from pathlib import Path
import sys
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from models.football_shell import build_football_shell, _panel_frame

SEED = 20261111
Q_CHARGE = 1.3
KAPPA = 0.04
GAUGE_G = 1.7
ALPHA = 0.2
W_COEFF = 0.7
V_EXT = 0.1


def geometry(mesh):
    X = np.asarray(mesh["nodes"], float)
    tri = np.asarray(mesh["triangles"], int)
    edges = sorted(mesh["edge_triangles"])
    eidx = {e:i for i,e in enumerate(edges)}
    B1 = np.zeros((len(X),len(edges)))
    B2 = np.zeros((len(edges),len(tri)))
    for e,(i,j) in enumerate(edges):
        B1[i,e], B1[j,e] = -1., 1.
    for f,t in enumerate(tri):
        for u,v in zip(t,np.roll(t,-1)):
            B2[eidx[tuple(sorted((int(u),int(v))))],f] += 1. if u<v else -1.
    return X,tri,edges,eidx,B1,B2


def triangle_data(X, tri, panel, panels, alpha):
    pts=X[list(tri)]
    e1=pts[1]-pts[0]
    l1=np.linalg.norm(e1); t1=e1/l1
    normal=np.cross(e1,pts[2]-pts[0]); normal/=np.linalg.norm(normal)
    t2=np.cross(normal,t1)
    J=np.array([[l1, np.dot(pts[2]-pts[0],t1)],
                [0., np.dot(pts[2]-pts[0],t2)]])
    area=abs(np.linalg.det(J))/2
    # Gradients of barycentric coordinates in the local orthonormal plane.
    grad_ref=np.array([[-1.,-1.],[1.,0.],[0.,1.]])
    grad=grad_ref @ np.linalg.inv(J)
    # Existing panel material frame and H4 direction.
    Q1,Q2,_=_panel_frame(X,panels[int(panel)],0.)
    Q=np.column_stack((Q1,Q2))
    centre=np.mean(X[list(panels[int(panel)])],axis=0)
    n=centre/np.linalg.norm(centre)
    h40=np.sum(n**4)
    g3=4*(n**3-h40*n)
    gp=Q.T@g3
    ng=np.linalg.norm(gp)
    if ng>1e-12:
        gh=gp/ng
        A2=np.eye(2)+alpha*np.outer(gh,gh)
    else:
        A2=np.eye(2)
    # Map triangle tangent coordinates into panel tangent coordinates.
    T=Q.T@np.column_stack((t1,t2))
    At=T.T@A2@T
    return area,grad,At


def quadrature3():
    # Weights sum to one; exact for polynomials through total degree 3.
    return [
        (np.array([1/3,1/3,1/3]), -27/48),
        (np.array([0.6,0.2,0.2]), 25/48),
        (np.array([0.2,0.6,0.2]), 25/48),
        (np.array([0.2,0.2,0.6]), 25/48),
    ]


def assemble(mesh):
    X,tri,edges,eidx,B1,B2=geometry(mesh)
    data=[]
    for f,t in enumerate(tri):
        data.append(triangle_data(X,t,mesh["triangle_panels"][f],mesh["panels"],ALPHA))
    return X,tri,edges,eidx,B1,B2,data


def energy_and_grad(meshdata, rho, theta, a, need_grad=True):
    X,tri,edges,eidx,B1,B2,data=meshdata
    v=B1.T@theta-Q_CHARGE*a
    face_flux=B2.T@a
    E=0.
    grad_theta=np.zeros_like(theta)
    grad_a=np.zeros_like(a)
    grad_rho=np.zeros_like(rho)
    mass=np.zeros((len(edges),len(edges)))
    for f,t in enumerate(tri):
        area,grads,A=data[f]
        local_edges=[(int(t[0]),int(t[1])),(int(t[1]),int(t[2])),(int(t[2]),int(t[0])))]
        le=[]; signs=[]
        for u,w in local_edges:
            key=tuple(sorted((u,w)))
            le.append(eidx[key]); signs.append(1. if u<w else -1.)
        # Whitney 1-form basis in local triangle coordinates.
        bary_samples=[x for x,_ in quadrature3()]
        wvals=[]
        for lam in bary_samples:
            vals=[]
            for (i,j) in ((0,1),(1,2),(2,0)):
                vals.append(lam[i]*grads[j]-lam[j]*grads[i])
            wvals.append(np.asarray(vals).T @ np.diag(signs))
        locv=v[le]*np.asarray(signs)
        # The local basis is oriented as (t0,t1),(t1,t2),(t2,t0).
        for (lam,wgt),Wmat in zip(quadrature3(),wvals):
            rh=float(lam@rho[t])
            vh=Wmat@locv
            av=float(vh@A@vh)
            E += 0.5*area*wgt*rh*av
            if need_grad:
                for k,node in enumerate(t):
                    grad_rho[node] += 0.5*area*wgt*lam[k]*av
                local_mass=area*wgt*rh*(Wmat.T@A@Wmat)
                for i in range(3):
                    for j in range(3):
                        mass[le[i],le[j]] += signs[i]*signs[j]*local_mass[i,j]
        # density-gradient term with P1 interpolation of nodal square roots
        s=np.sqrt(rho[t])
        gs=s@grads
        E += 0.5*KAPPA*area*(gs@A@gs)
        if need_grad:
            for k,node in enumerate(t):
                grad_rho[node] += KAPPA*area*(grads[k]@A@gs)/(2*s[k])
        # Internal energy W=0.5*c*rho^2 and constant external V*rho.
        for lam,wgt in quadrature3():
            rh=float(lam@rho[t])
            E += area*wgt*(0.5*W_COEFF*rh**2+V_EXT*rh)
            if need_grad:
                for k,node in enumerate(t):
                    grad_rho[node] += area*wgt*lam[k]*(W_COEFF*rh+V_EXT)
        # Gauge curvature energy: F_h is face flux / area.
        E += 0.5/(GAUGE_G**2)*face_flux[f]**2/area
    if need_grad:
        grad_theta=B1@(mass@v)
        grad_a=-Q_CHARGE*(mass@v)+B2@(face_flux/(GAUGE_G**2*np.array([d[0] for d in data])))
    return E,grad_theta,grad_a,grad_rho,mass


def fd_gradient(fun,x,indices,eps=2e-6):
    vals=[]
    for i in indices:
        xp=x.copy(); xm=x.copy()
        xp[i]+=eps; xm[i]-=eps
        vals.append((fun(xp)-fun(xm))/(2*eps))
    return np.asarray(vals)


def main():
    rng=np.random.default_rng(SEED)
    mesh=build_football_shell()
    md=assemble(mesh)
    X,tri,edges,eidx,B1,B2,data=md
    nV,nE,nF=len(X),len(edges),len(tri)
    rho=0.8+0.4*rng.random(nV)
    theta=rng.normal(scale=.2,size=nV)
    a=rng.normal(scale=.15,size=nE)
    E,gt,ga,gr,mass=energy_and_grad(md,rho,theta,a)
    # Gauge transformation: v and curvature, and hence full energy, are invariant.
    chi=rng.normal(size=nV)
    rho2=rho.copy()
    theta2=theta+Q_CHARGE*chi
    a2=a+B1.T@chi
    E2,*_=energy_and_grad(md,rho2,theta2,a2)
    # Finite differences on deterministic subsets of all variable blocks.
    ti=np.array([0,7,31,64])
    ai=np.array([0,19,87,143])
    ri=np.array([0,13,47,91])
    def ft(x): return energy_and_grad(md,rho,x,a,False)[0]
    def fa(x): return energy_and_grad(md,rho,theta,x,False)[0]
    def fr(x): return energy_and_grad(md,x,theta,a,False)[0]
    fdt=fd_gradient(ft,theta,ti)
    fda=fd_gradient(fa,a,ai)
    fdr=fd_gradient(fr,rho,ri)
    rel=lambda x,y: float(np.linalg.norm(x-y)/max(np.linalg.norm(x),np.linalg.norm(y),1e-14))
    # Discrete gauge Noether identity: phase gradient + (1/q) incidence contraction
    # of connection gradient vanishes for the kinetic part; curvature term annihilates B1^T.
    noether=np.linalg.norm(gt+(1/Q_CHARGE)*(B1@ga))
    result={
        "mesh":{"vertices":nV,"edges":nE,"faces":nF,
                "physical_seams":len(mesh["physical_seams"]),
                "max_abs_B1B2":int(np.max(np.abs(B1@B2)))},
        "whitney":{"space":"lowest-order Whitney 1-forms",
                   "quadrature":"4-point degree-3 exact triangle rule",
                   "anisotropy_alpha":ALPHA},
        "energy":{"value":float(E),"gauge_transformed":float(E2),
                  "absolute_gauge_energy_difference":float(abs(E-E2))},
        "first_variation_fd":{
            "phase_indices":ti.tolist(),"phase_relative_error":rel(gt[ti],fdt),
            "connection_indices":ai.tolist(),"connection_relative_error":rel(ga[ai],fda),
            "density_indices":ri.tolist(),"density_relative_error":rel(gr[ri],fdr)},
        "gauge_noether_identity_residual":float(noether),
        "classification":"fixed-mesh discrete variational audit; no refinement convergence or constitutive calibration"
    }
    print(json.dumps(result,indent=2,sort_keys=True))
    if np.max(np.abs(B1@B2))!=0: raise SystemExit("incidence identity failed")
    if abs(E-E2)>1e-10: raise SystemExit("discrete gauge invariance failed")
    if max(rel(gt[ti],fdt),rel(ga[ai],fda),rel(gr[ri],fdr))>2e-5:
        raise SystemExit("finite-difference first-variation audit failed")
    if noether>1e-9: raise SystemExit("discrete gauge Noether identity failed")


if __name__=="__main__":
    main()
