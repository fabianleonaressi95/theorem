"""Local scalar-field extension of MQM-1 on the finite RGS-PSU/Q6 metric graph.

The edge kinetic term is the exact linear-edge Dirichlet action.
The quartic vertex potential is the sampled RGS-EMS scalar potential.
This module is a finite graph model, not a 4D continuum discretization.
"""
from __future__ import annotations
import numpy as np

def incidence_matrix(edges, n_vertices=64):
    B=np.zeros((n_vertices,len(edges)),dtype=float)
    for k,(u,v,*_) in enumerate(edges):
        B[int(u),k]=-1.0
        B[int(v),k]=1.0
    return B

def metric_weights(edge_lengths):
    lengths=np.asarray(edge_lengths,dtype=float)
    if lengths.ndim!=1 or len(lengths)==0 or np.any(~np.isfinite(lengths)) or np.any(lengths<=0):
        raise ValueError("edge lengths must be a nonempty finite positive vector")
    ell_rms=float(np.sqrt(np.mean(lengths**2)))
    return ell_rms/lengths

def scalar_action(phi, B, weights, lam=1.0, phi_v=1.0, V0=0.0):
    """S=1/2 phi^T K phi + mean_g[V0+lam/4(phi_g^2-phi_v^2)^2]."""
    phi=np.asarray(phi,dtype=float)
    B=np.asarray(B,dtype=float); weights=np.asarray(weights,dtype=float)
    if phi.shape!=(B.shape[0],) or weights.shape!=(B.shape[1],):
        raise ValueError("incompatible scalar, incidence, or edge-weight shape")
    if lam<0 or not np.isfinite(lam) or not np.isfinite(phi_v) or not np.isfinite(V0):
        raise ValueError("potential parameters must be finite and lambda nonnegative")
    K=B@np.diag(weights)@B.T
    potential=V0+0.25*lam*(phi**2-phi_v**2)**2
    return float(0.5*phi@K@phi+np.mean(potential))

def scalar_gradient(phi, B, weights, lam=1.0, phi_v=1.0):
    phi=np.asarray(phi,dtype=float)
    B=np.asarray(B,dtype=float); weights=np.asarray(weights,dtype=float)
    K=B@np.diag(weights)@B.T
    return K@phi+(lam/len(phi))*phi*(phi**2-phi_v**2)

def scalar_hessian(phi, B, weights, lam=1.0, phi_v=1.0):
    phi=np.asarray(phi,dtype=float)
    B=np.asarray(B,dtype=float); weights=np.asarray(weights,dtype=float)
    K=B@np.diag(weights)@B.T
    return K+np.diag((lam/len(phi))*(3*phi**2-phi_v**2))

def uniform_restriction(phi_value, B, weights, lam=1.0, phi_v=1.0, V0=0.0):
    """Return action on phi=q*1; graph kinetic term vanishes exactly."""
    n=B.shape[0]
    phi=np.full(n,float(phi_value))
    return scalar_action(phi,B,weights,lam=lam,phi_v=phi_v,V0=V0)
