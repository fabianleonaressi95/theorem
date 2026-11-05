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

def audit(scale_factors,axial_currents,dims,volumes=None,kappa=None,max_distance=3):
    a=np.asarray(scale_factors,float); x=np.asarray(axial_currents,float)
    if x.ndim==3 and x.shape[-1]==4: x=x[:,None,:,:]
    if x.ndim!=4 or x.shape[-1]!=4: raise ValueError('axial_currents must be (T,N,4) or (T,R,N,4)')
    T,R,N,_=x.shape
    if N!=math.prod(dims) or a.shape!=(T,) or not np.isfinite(a).all() or np.any(a<=0): raise ValueError('geometry/scale-factor shape mismatch')
    if not np.isfinite(x).all(): raise ValueError('non-finite axial current')
    V=np.ones(T) if volumes is None else np.asarray(volumes,float)
    if V.shape!=(T,) or not np.isfinite(V).all() or np.any(V<=0): raise ValueError('volumes must be positive finite (T,)')
    if kappa is not None and (not math.isfinite(kappa) or kappa<=0): raise ValueError('kappa must be positive finite')
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
      'rows':rows,'scaling_fits':{'q_local_contact_positive_branch':fit('mean_of_lorentz_norm_squared'),
        'q_coarse_invariant_positive_branch':fit('coarse_axial_invariant')},
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
        miss={'scale_factors','axial_currents'}-set(z.files)
        if miss:p.error('missing NPZ keys: '+', '.join(sorted(miss)))
        report=audit(z['scale_factors'],z['axial_currents'],dims,z['volumes'] if 'volumes' in z.files else None,args.kappa,args.max_distance)
    out=json.dumps(report,indent=2,sort_keys=True)
    if args.output:
        with open(args.output,'w',encoding='utf-8') as f:f.write(out+'\n')
    print(out)
    if not all(report['checks'].values()):raise SystemExit(1)
if __name__=='__main__':main()
