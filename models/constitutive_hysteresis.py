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


def _langevin(x):
    """Stable Langevin function coth(x) - 1/x."""
    x=np.asarray(x,float)
    out=np.empty_like(x)
    small=np.abs(x)<1e-4
    xs=x[small]
    out[small]=xs/3.0-xs**3/45.0+2.0*xs**5/945.0
    xl=x[~small]
    out[~small]=1.0/np.tanh(xl)-1.0/xl
    return out


def _langevin_derivative(x):
    """Derivative of the Langevin function, with a stable small-x series."""
    x=np.asarray(x,float)
    out=np.empty_like(x)
    small=np.abs(x)<1e-4
    xs=x[small]
    out[small]=1.0/3.0-xs**2/15.0+2.0*xs**4/189.0
    xl=x[~small]
    out[~small]=1.0/(xl**2)-1.0/(np.sinh(xl)**2)
    return out


def simulate_jiles_atherton(H, Ms, a, k, alpha, c, Mirr0=0.0):
    """Simulate the classical scalar Jiles--Atherton magnetization model.

    Parameters use one consistent field/magnetization unit system:
    Ms saturation magnetization, a anhysteretic field scale, k pinning
    parameter, alpha mean-field coupling, and c reversible fraction (0..1).
    The irreversible state is advanced with a predictor-corrector step in H.
    This is a reference quasi-static model, not a dynamic eddy-current model.
    """
    H=np.asarray(H,float)
    if H.ndim!=1 or H.size<2 or not np.all(np.isfinite(H)):
        raise ValueError("H must be a finite 1-D vector with at least two samples")
    if not (Ms>0 and a>0 and k>0 and alpha>=0 and 0<=c<=1):
        raise ValueError("require Ms,a,k > 0, alpha >= 0 and 0 <= c <= 1")
    if not np.isfinite(Mirr0):
        raise ValueError("Mirr0 must be finite")

    Mirr=np.empty_like(H)
    M=np.empty_like(H)
    Mirr[0]=float(Mirr0)

    def anhysteretic(he):
        z=he/a
        return Ms*_langevin(np.asarray(z))

    def irreversible_rate(he, mirr, direction):
        man=float(anhysteretic(np.asarray(he)))
        delta=man-mirr
        denom=direction*k-alpha*delta
        if abs(denom)<1e-12*max(1.0,k,abs(alpha*delta)):
            raise FloatingPointError("Jiles-Atherton irreversible denominator is singular")
        return delta/denom

    he0=H[0]+alpha*Mirr[0]
    man0=float(anhysteretic(np.asarray(he0)))
    M[0]=c*man0+(1.0-c)*Mirr[0]

    for i in range(1,H.size):
        dH=float(H[i]-H[i-1])
        if dH==0.0:
            Mirr[i]=Mirr[i-1]
            M[i]=M[i-1]
            continue
        direction=float(np.sign(dH))
        h0=float(H[i-1]+alpha*M[i-1])
        r0=irreversible_rate(h0,Mirr[i-1],direction)
        pred_mirr=Mirr[i-1]+dH*r0
        pred_man=float(anhysteretic(np.asarray(H[i]+alpha*(c*float(anhysteretic(
            np.asarray(H[i]+alpha*M[i-1])))+(1.0-c)*pred_mirr))))
        r1=irreversible_rate(float(H[i]+alpha*(c*pred_man+(1.0-c)*pred_mirr)),
                             pred_mirr,direction)
        Mirr[i]=Mirr[i-1]+0.5*dH*(r0+r1)
        he=H[i]+alpha*M[i-1]
        man=float(anhysteretic(np.asarray(he)))
        M[i]=c*man+(1.0-c)*Mirr[i]
    return M
