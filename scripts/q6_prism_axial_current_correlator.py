#!/usr/bin/env python3
"""Lorentz-covariant axial-current correlator on Q6/PRISM.

NPZ: scale_factors (T,), axial_currents (T,N,4) or (T,R,N,4), optional
volumes (T,). Currents are real contravariant J5^a in eta=(-,+,+,+).
Each node value is an integrated microscopic contribution to the coarse cell.
"""
from __future__ import annotations
import argparse,itertools,json,math
import numpy as np
Q6=(2,2,2,2,2,2); PRISM=(64,6,6,6,5); ETA=np.diag([-1.,1.,1.,1.])

def offsets(dims,R):
    if R<0: raise ValueError('max_distance must be nonnegative')
    for d in itertools.product(*(range(L) for L in dims)):
        r=sum(min(x,L-x) for x,L in zip(d,dims))
        if r<=R: yield d,r

def lorentz_scalar(M): return float(np.sum(ETA*np.asarray(M)))

def local_moments(currents):
    x=np.asarray(currents,float).reshape(-1,4)
    if not np.isfinite(x).all(): raise ValueError('axial currents must be finite')
    mu=x.mean(axis=0); M=x.T@x/len(x); C=M-np.outer(mu,mu)
    return {'sample_count':len(x),'mean_axial_current':mu.tolist(),
      'second_moment':M.tolist(),'covariance':C.tolist(),
      'mean_current_lorentz_norm':lorentz_scalar(np.outer(mu,mu)),
      'fluctuation_lorentz_trace':lorentz_scalar(C),
      'mean_of_lorentz_norm_squared':lorentz_scalar(M),
      'moment_decomposition_residual':lorentz_scalar(M)-lorentz_scalar(C)-lorentz_scalar(np.outer(mu,mu)),
      'spatial_isotropy_residual':float(np.linalg.norm(M[1:,1:]-np.trace(M[1:,1:])*np.eye(3)/3)/max(np.linalg.norm(M[1:,1:]),1.0)),
      'time_space_second_moment_norm':float(np.linalg.norm(M[0,1:])),
      'mean_spatial_polarization_norm':float(np.linalg.norm(mu[1:]))}

def shell_correlator(currents,dims,max_distance):
    N=math.prod(dims); f=np.asarray(currents,float).reshape(*dims,4)
    mu=f.mean(axis=tuple(range(len(dims))),keepdims=True); c=f-mu
    tensor=np.zeros((max_distance+1,4,4)); counts=np.zeros(max_distance+1,dtype=np.int64)
    axes=tuple(range(len(dims)))
    for d,r in offsets(dims,max_distance):
        shifted=np.roll(c,tuple(-v for v in d),axis=axes)
        tensor[r]+=np.tensordot(c.reshape(-1,4).T,shifted.reshape(-1,4),axes=(1,0))
        counts[r]+=N
    rows=[]
    for r in range(max_distance+1):
        if counts[r]:
            M=tensor[r]/counts[r]
            rows.append({'distance':r,'directed_pair_count':int(counts[r]),
              'connected_tensor':M.tolist(),'lorentz_trace':lorentz_scalar(M)})
    return rows

def coarse_cell_moments(currents,volume):
    x=np.asarray(currents,float); V=float(volume)
    if not math.isfinite(V) or V<=0: raise ValueError('volume must be finite and positive')
    total=x.sum(axis=1)/V
    M=total.T@total/len(total); mu=total.mean(axis=0)
    self_M=np.mean([np.einsum('na,nb->ab',z,z)/V**2 for z in x],axis=0)
    pair_M=M-self_M
    return {'coarse_current_mean':mu.tolist(),'coarse_second_moment':M.tolist(),
      'coarse_axial_invariant':lorentz_scalar(M),
      'coarse_self_contribution':lorentz_scalar(self_M),
      'coarse_pair_contribution':lorentz_scalar(pair_M),
      'coarse_decomposition_residual':lorentz_scalar(M)-lorentz_scalar(self_M)-lorentz_scalar(pair_M)}

def spinors_to_axial_currents(spinors, reality_tolerance=1e-10):
    """Compute J5^a=i*bar(psi)*gamma5*gamma^a*psi in the source convention."""
    psi=np.asarray(spinors,dtype=complex)
    if psi.shape[-1:]!=(4,) or not np.isfinite(psi).all():
        raise ValueError('spinors must be finite complex arrays with trailing dimension 4')
    I2=np.eye(2,dtype=complex); Z2=np.zeros((2,2),complex)
    pauli=(np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.array([[1,0],[0,-1]],complex))
    gamma0=1j*np.block([[I2,Z2],[Z2,-I2]])
    gammas=(gamma0,)+tuple(1j*np.block([[Z2,s],[-s,Z2]]) for s in pauli)
    gamma5=1j*gammas[0]@gammas[1]@gammas[2]@gammas[3]
    bar=1j*np.einsum('...i,ij->...j',psi.conj(),gamma0)
    values=np.stack([1j*np.einsum('...i,ij,...j->...',bar,gamma5@g,psi) for g in gammas],axis=-1)
    if np.max(np.abs(values.imag),initial=0.0)>reality_tolerance:
        raise ArithmeticError('Dirac axial current is not real within tolerance')
    return values.real


def project_axial_current_to_fluid_rest_space(currents, fluid_velocity, tolerance=1e-9):
    """Project J5 orthogonally to a unit timelike fluid 4-velocity.

    h^a_b = delta^a_b + u^a u_b for eta=(-,+,+,+). This is a candidate
    spatial spin-vector invariant; the Noether spin-tensor normalization
    must still be derived before identifying it with Weyssenhoff s^2.
    """
    j=np.asarray(currents,float); u=np.asarray(fluid_velocity,float)
    if j.shape[-1:]!=(4,) or u.shape!=(4,) or not np.isfinite(j).all() or not np.isfinite(u).all():
        raise ValueError('currents (...,4) and finite fluid_velocity (4,) required')
    if abs(float(u@ETA@u)+1.0)>tolerance:
        raise ValueError('fluid_velocity must be unit timelike: eta(u,u)=-1')
    uj=np.einsum('a,...a->...',ETA@u,j)
    projected=j+uj[...,None]*u
    norm=np.einsum('...a,ab,...b->...',projected,ETA,projected)
    if np.min(norm,initial=0.0)<-tolerance:
        raise ArithmeticError('rest-space projection produced a negative norm')
    return projected,np.maximum(norm,0.0)


def audit(scale_factors,axial_currents,dims,volumes=None,kappa=None,max_distance=3,fluid_velocity=None):
    a=np.asarray(scale_factors,float); x=np.asarray(axial_currents,float)
    if x.ndim==3 and x.shape[-1]==4: x=x[:,None,:,:]
    if x.ndim!=4 or x.shape[-1]!=4: raise ValueError('axial_currents must be (T,N,4) or (T,R,N,4)')
    T,R,N,_=x.shape
    if N!=math.prod(dims) or a.shape!=(T,) or not np.isfinite(a).all() or np.any(a<=0): raise ValueError('geometry/scale-factor shape mismatch')
    if not np.isfinite(x).all(): raise ValueError('non-finite axial current')
    V=np.ones(T) if volumes is None else np.asarray(volumes,float)
    if V.shape!=(T,) or not np.isfinite(V).all() or np.any(V<=0): raise ValueError('volumes must be positive finite (T,)')
    if kappa is not None and (not math.isfinite(kappa) or kappa<=0): raise ValueError('kappa must be positive finite')
    u=None if fluid_velocity is None else np.asarray(fluid_velocity,float)
    if u is not None and (u.shape!=(T,4) or not np.isfinite(u).all()): raise ValueError('fluid_velocity must have finite shape (T,4)')
    rows=[]
    for t in range(T):
        lm=local_moments(x[t]); cm=coarse_cell_moments(x[t],V[t])
        shells=[shell_correlator(x[t,r],dims,max_distance) for r in range(R)]
        avg_shell=[]
        for j,row in enumerate(shells[0]):
            mats=np.mean([np.asarray(s[j]['connected_tensor']) for s in shells],axis=0)
            avg_shell.append({'distance':row['distance'],'directed_pair_count':row['directed_pair_count'],
                              'connected_tensor':mats.tolist(),'lorentz_trace':lorentz_scalar(mats)})
        item={'a':float(a[t]),'volume':float(V[t]),'replicas':R,**lm,**cm,'shell_correlations':avg_shell}
        if u is not None:
            projected,projected_norm=project_axial_current_to_fluid_rest_space(x[t],u[t])
            item['fluid_four_velocity']=u[t].tolist()
            item['rest_space_projected_axial_invariant_candidate']=float(np.mean(projected_norm))
            item['rest_space_projected_mean_current']=np.mean(projected.reshape(-1,4),axis=0).tolist()
            item['rest_space_projected_current_orthogonality_residual']=float(np.max(np.abs(np.einsum('a,...a->...',ETA@u[t],projected))))
            item['weyssenhoff_spin_tensor_normalization']='NOT_FIXED: derive canonical Noether spin-current map before identifying this with s^2'
        if kappa is not None:
            item['torsion_quadratic_invariant']=-1.5*kappa**2*lm['mean_of_lorentz_norm_squared']
            item['four_fermion_contact_density']=(3*kappa/16)*lm['mean_of_lorentz_norm_squared']
        rows.append(item)
    rows.sort(key=lambda z:z['a'])
    def fit(key):
        y=np.array([r[key] for r in rows]); m=(y>0)&np.isfinite(y)
        if m.sum()<2:return {'q':None,'points_used':int(m.sum())}
        xx=np.log(np.array([r['a'] for r in rows])[m])
        return {'q':float(-np.polyfit(xx,np.log(y[m]),1)[0]),'points_used':int(m.sum())}
    return {'schema':'rgs-ec-q6-prism-axial-current/v1','signature':'(-,+,+,+)',
      'geometry':{'dims':list(dims),'vertices':N,'name':'Q6' if dims==Q6 else ('PRISM' if dims==PRISM else 'custom')},
      'current_convention':'real contravariant J5^a; Cartan source Sigma_abc=-1/2 epsilon_abcd J5^d',
    fits={'q_local_contact_positive_branch':fit('mean_of_lorentz_norm_squared'),
          'q_coarse_invariant_positive_branch':fit('coarse_axial_invariant')}
    if u is not None: fits['q_rest_space_projected_axial_candidate']=fit('rest_space_projected_axial_invariant_candidate')
    return {'schema':'rgs-ec-q6-prism-axial-current/v1','signature':'(-,+,+,+)',
      'geometry':{'dims':list(dims),'vertices':N,'name':'Q6' if dims==Q6 else ('PRISM' if dims==PRISM else 'custom')},
      'current_convention':'real contravariant J5^a; Cartan source Sigma_abc=-1/2 epsilon_abcd J5^d',
      'rows':rows,'scaling_fits':fits,
      'checks':{'local_moment_decomposition':all(abs(r['moment_decomposition_residual'])<1e-10 for r in rows),
        'coarse_self_pair_decomposition':all(abs(r['coarse_decomposition_residual'])<1e-10 for r in rows)},
      'limitations':['Lorentz contractions are indefinite; the scalar can be negative or vanish by cancellation.',
        'Graph topology supplies shell distances, not a spinor state, gauge transport, or equilibrium measure.',
        'Node currents must be action-derived J5 samples with declared units and cell normalization.',
        'The local four-fermion contact needs a specified operator ordering/renormalization prescription.',
        'A graph-shell average is not automatically a Lorentz-covariant continuum correlator.']}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input',required=True);p.add_argument('--geometry',choices=('q6','prism'),required=True)
    p.add_argument('--max-distance',type=int,default=3);p.add_argument('--kappa',type=float,default=None);p.add_argument('--output',default='')
    args=p.parse_args();dims=Q6 if args.geometry=='q6' else PRISM
    with np.load(args.input,allow_pickle=False) as z:
        miss={'scale_factors'}-set(z.files)
        if miss:p.error('missing NPZ keys: '+', '.join(sorted(miss)))
        if 'axial_currents' in z.files: currents=z['axial_currents']
        elif 'spinors' in z.files: currents=spinors_to_axial_currents(z['spinors'])
        else:p.error('NPZ must contain axial_currents or spinors')
        report=audit(z['scale_factors'],currents,dims,z['volumes'] if 'volumes' in z.files else None,args.kappa,args.max_distance,z['fluid_velocity'] if 'fluid_velocity' in z.files else None)
    out=json.dumps(report,indent=2,sort_keys=True)
    if args.output:
        with open(args.output,'w',encoding='utf-8') as f:f.write(out+'\n')
    print(out)
    if not all(report['checks'].values()):raise SystemExit(1)
if __name__=='__main__':main()
