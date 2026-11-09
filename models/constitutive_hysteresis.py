"""Reference constitutive hysteresis baselines for controlled synthetic/data tests.

Preisach and Prandtl-Ishlinskii are operator models; Bouc-Wen is a
differential phenomenological model. Parameter fitting here is deliberately
limited to the linear weights of fixed operator dictionaries.
"""
from __future__ import annotations
import numpy as np


def play_features(u, radii, initial_memory=None):
    u=np.asarray(u,float); radii=np.asarray(radii,float)
    if u.ndim!=1 or u.size<2 or radii.ndim!=1 or np.any(radii<0):
        raise ValueError("u must be a vector and radii nonnegative")
    out=np.empty((u.size,radii.size),float)
    for j,r in enumerate(radii):
        state=float(u[0] if initial_memory is None else initial_memory)
        state=max(u[0]-r,min(u[0]+r,state))
        out[0,j]=state
        for k in range(1,u.size):
            state=max(u[k]-r,min(u[k]+r,state))
            out[k,j]=state
    return out


def prandtl_ishlinskii_design(u, radii):
    u=np.asarray(u,float)
    return np.column_stack((u,play_features(u,radii)))


def fit_prandtl_ishlinskii(u,y,radii):
    X=prandtl_ishlinskii_design(u,radii)
    y=np.asarray(y,float)
    if y.shape!=(X.shape[0],): raise ValueError("y must match u")
    coeff,_,rank,_=np.linalg.lstsq(X,y,rcond=None)
    return {"linear_gain":float(coeff[0]),"play_weights":coeff[1:],
            "radii":np.asarray(radii,float),"rank":int(rank)}


def predict_prandtl_ishlinskii(u,model):
    X=prandtl_ishlinskii_design(u,model["radii"])
    coeff=np.r_[model["linear_gain"],model["play_weights"]]
    return X@coeff


def preisach_features(u,alpha,beta,initial_state=-1):
    u=np.asarray(u,float); alpha=np.asarray(alpha,float); beta=np.asarray(beta,float)
    if u.ndim!=1 or alpha.shape!=beta.shape or alpha.ndim!=1 or np.any(alpha<=beta):
        raise ValueError("require vector input and alpha > beta thresholds")
    states=np.full(alpha.size,float(initial_state))
    X=np.empty((u.size,alpha.size),float)
    for k,value in enumerate(u):
        states=np.where(value>=alpha,1.0,np.where(value<=beta,-1.0,states))
        X[k]=states
    return X


def fit_preisach(u,y,alpha,beta):
    X=preisach_features(u,alpha,beta)
    y=np.asarray(y,float)
    if y.shape!=(X.shape[0],): raise ValueError("y must match u")
    design=np.column_stack((np.ones(X.shape[0]),X))
    coeff,_,rank,_=np.linalg.lstsq(design,y,rcond=None)
    return {"bias":float(coeff[0]),"relay_weights":coeff[1:],
            "alpha":np.asarray(alpha,float),"beta":np.asarray(beta,float),
            "rank":int(rank)}


def predict_preisach(u,model):
    X=preisach_features(u,model["alpha"],model["beta"])
    return model["bias"]+X@model["relay_weights"]


def simulate_bouc_wen(u,dt,A=1.0,beta=0.5,gamma=0.5,n=2.0,
                      linear_gain=0.1,hysteretic_gain=1.0,z0=0.0):
    """Integrate the classical rate-dependent Bouc-Wen state equation by RK4."""
    u=np.asarray(u,float)
    if u.ndim!=1 or u.size<2 or dt<=0 or n<1:
        raise ValueError("invalid input, dt or exponent")
    du=np.gradient(u,dt)
    z=np.empty_like(u); z[0]=z0
    def f(state,velocity):
        return (A*velocity-beta*abs(velocity)*abs(state)**(n-1)*state
                -gamma*velocity*abs(state)**n)
    for k in range(u.size-1):
        h=dt; v=float(du[k])
        k1=f(z[k],v); k2=f(z[k]+.5*h*k1,v)
        k3=f(z[k]+.5*h*k2,v); k4=f(z[k]+h*k3,v)
        z[k+1]=z[k]+h*(k1+2*k2+2*k3+k4)/6
    return linear_gain*u+hysteretic_gain*z


def threshold_grid(u,levels=9):
    """Return a reproducible triangular Preisach grid over observed input range."""
    u=np.asarray(u,float)
    if levels<2 or u.ndim!=1 or u.size<2: raise ValueError("invalid grid request")
    lo,hi=float(np.min(u)),float(np.max(u))
    q=np.linspace(lo,hi,levels)
    pairs=[(a,b) for a in q for b in q if a>b]
    return np.array([p[0] for p in pairs]),np.array([p[1] for p in pairs])
