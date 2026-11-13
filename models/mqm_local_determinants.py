"""Local determinant coupling for the finite MQM-1 scalar field.

The collective A13 parameter q is promoted to phi_g at each Q6 vertex:
D_F[phi]=D_kin+diag(m_F+g_F phi_g tau_g),
K_B[phi]=K_B0+lambda_B diag(phi_g tau_g, phi_g tau_g).

The formulas are exact finite-matrix derivatives on the domain where D_F is
invertible and K_B is positive definite. Matrices/parameters are supplied by
the caller; this module does not fabricate the archived A13 operators.
"""
from __future__ import annotations
import numpy as np

def _real_vector(x, name):
    a=np.asarray(x,dtype=float)
    if a.ndim!=1 or not np.all(np.isfinite(a)):
        raise ValueError(f"{name} must be a finite real vector")
    return a

class LocalDeterminantCoupling:
    def __init__(self, D_kin, K_B0, tau, spin_dof, mF=0.5, gF=0.35,
                 lambdaB=0.4):
        self.Dkin=np.asarray(D_kin,dtype=complex)
        self.KB0=np.asarray(K_B0,dtype=float)
        self.tau=_real_vector(tau,"tau")
        self.n=len(self.tau)
        self.spin_dof=int(spin_dof)
        self.mF=float(mF); self.gF=float(gF); self.lambdaB=float(lambdaB)
        if self.spin_dof<1 or self.Dkin.shape!=(self.n*self.spin_dof,)*2:
            raise ValueError("D_kin shape must be (n*spin_dof,n*spin_dof)")
        if self.KB0.shape!=(2*self.n,2*self.n):
            raise ValueError("K_B0 shape must be (2*n,2*n)")
        if not np.allclose(self.Dkin.conj().T,-self.Dkin,atol=1e-10):
            raise ValueError("D_kin must be anti-Hermitian")
        if not np.allclose(self.KB0,self.KB0.T,atol=1e-10):
            raise ValueError("K_B0 must be symmetric")
        if not all(np.isfinite(v) for v in (self.mF,self.gF,self.lambdaB)):
            raise ValueError("couplings must be finite")
        self._VF=[]
        for g in range(self.n):
            diag=np.zeros(self.n*self.spin_dof)
            diag[g*self.spin_dof:(g+1)*self.spin_dof]=self.gF*self.tau[g]
            self._VF.append(np.diag(diag).astype(complex))
        self._WB=[]
        for g in range(self.n):
            diag=np.zeros(2*self.n)
            diag[g]=self.lambdaB*self.tau[g]
            diag[self.n+g]=self.lambdaB*self.tau[g]
            self._WB.append(np.diag(diag))

    def fermion_matrix(self, phi):
        phi=_real_vector(phi,"phi")
        if phi.shape!=(self.n,): raise ValueError("phi shape mismatch")
        mass=np.repeat(self.mF+self.gF*phi*self.tau,self.spin_dof)
        return self.Dkin+np.diag(mass)

    def boson_matrix(self, phi):
        phi=_real_vector(phi,"phi")
        if phi.shape!=(self.n,): raise ValueError("phi shape mismatch")
        profile=self.lambdaB*phi*self.tau
        return self.KB0+np.diag(np.r_[profile,profile])

    def effective_action(self, phi):
        D=self.fermion_matrix(phi); K=self.boson_matrix(phi)
        signD,logD=np.linalg.slogdet(D)
        if signD==0 or not np.isfinite(logD):
            raise ValueError("fermion matrix is singular")
        ev=np.linalg.eigvalsh(K)
        if ev[0]<=0:
            raise ValueError("bosonic Hessian is not positive definite")
        return -float(logD)+0.5*float(np.sum(np.log(ev)))

    def determinant_gradient_hessian(self, phi):
        """Return Gamma_F+Gamma_B, its gradient, and its full n-by-n Hessian."""
        D=self.fermion_matrix(phi); K=self.boson_matrix(phi)
        signD,logD=np.linalg.slogdet(D)
        if signD==0 or not np.isfinite(logD):
            raise ValueError("fermion matrix is singular")
        ev=np.linalg.eigvalsh(K)
        if ev[0]<=0: raise ValueError("bosonic Hessian is not positive definite")
        Di=np.linalg.inv(D); Ki=np.linalg.inv(K)
        grad=np.zeros(self.n); hess=np.zeros((self.n,self.n))
        for i in range(self.n):
            Vi=self._VF[i]; Wi=self._WB[i]
            grad[i]=-float(np.real(np.trace(Di@Vi)))+0.5*float(np.trace(Ki@Wi))
            for j in range(self.n):
                Vj=self._VF[j]; Wj=self._WB[j]
                hess[i,j]=(
                    float(np.real(np.trace(Di@Vj@Di@Vi)))
                    -0.5*float(np.trace(Ki@Wj@Ki@Wi))
                )
        return -float(logD)+0.5*float(np.sum(np.log(ev))),grad,hess

    def local_scalar_effective_action(self, phi, B, weights, lam=1.0,
                                      phi_v=1.0, V0=0.0):
        from models.mqm_local_scalar import scalar_action
        return scalar_action(phi,B,weights,lam,phi_v,V0)+self.effective_action(phi)

    def local_scalar_gradient_hessian(self, phi, B, weights, lam=1.0,
                                      phi_v=1.0):
        from models.mqm_local_scalar import scalar_gradient,scalar_hessian
        _,gd,Hd=self.determinant_gradient_hessian(phi)
        return (scalar_gradient(phi,B,weights,lam,phi_v)+gd,
                scalar_hessian(phi,B,weights,lam,phi_v)+Hd)
