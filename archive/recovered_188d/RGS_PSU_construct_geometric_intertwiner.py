#!/usr/bin/env python3
"""Construct a geometry-driven 64->188 map for the RGS-PSU Anti-Twin audit.

Inputs expected in the same directory (or via CLI):
  X_Oh_reconstructed.npy : (64,3) original geometry
  K0.npy, P_G.npy        : (188,188) kernel and projector

This source was recovered from the user's Library. It explicitly distinguishes
an original geometry run from a proxy smoke test and warns that the direct
[K0,R_geo] commutator is meaningful only when the tangent bases are aligned.
"""
import argparse, json, os, glob, zipfile
import numpy as np
from scipy.linalg import null_space, eigh, svd

def locate(name, roots):
    for root in roots:
        p=os.path.join(root,name)
        if os.path.isfile(p): return p
    return None

def polar_frame(B, tol=1e-10):
    U,s,Vh=svd(B,full_matrices=False,check_finite=True)
    rank=int(np.sum(s>tol*max(1.0,s[0] if len(s) else 1.0)))
    if rank<B.shape[1]: return None,s,rank
    return U@Vh,s,rank

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--x',default='X_Oh_reconstructed.npy')
    ap.add_argument('--k0',default='K0.npy')
    ap.add_argument('--pg',default='P_G.npy')
    ap.add_argument('--proxy',action='store_true',help='use bridge_arrays.npz Y only as a proxy smoke test')
    ap.add_argument('--out',default='RGS_PSU_geometric_intertwiner_report.json')
    args=ap.parse_args()
    base=os.path.dirname(os.path.abspath(__file__))
    roots=[os.getcwd(),base,'/mnt/data','/mnt/data/rgs_recovery','/mnt/data/RGS_PSU_AntiTwin_next_audit']
    if args.proxy:
        zp=locate('bridge_arrays.npz',roots)
        if not zp: raise FileNotFoundError('bridge_arrays.npz not found for proxy run')
        with np.load(zp) as z: X=z['Y']
        xsource=zp+'::Y (PROXY, not original X_Oh)'
    else:
        xp=args.x if os.path.isabs(args.x) else locate(args.x,roots)
        if not xp: raise FileNotFoundError('Original X_Oh_reconstructed.npy not found; do not substitute proxy geometry.')
        X=np.load(xp); xsource=xp
    if X.shape!=(64,3): raise ValueError(f'Expected X shape (64,3), got {X.shape}')
    def loadmat(name,arg):
        p=arg if os.path.isabs(arg) else locate(arg,roots)
        if p: return np.load(p),p
        for zp in glob.glob('/mnt/data/**/188D_FINAL_BUNDLE.zip',recursive=True):
            with zipfile.ZipFile(zp) as z:
                hits=[n for n in z.namelist() if n==name or n.endswith('/'+name)]
                if hits:
                    import io
                    return np.load(io.BytesIO(z.read(hits[0]))),zp+'::'+hits[0]
        raise FileNotFoundError(f'{name} not found')
    K0,kpath=loadmat('K0.npy',args.k0); PG,pgpath=loadmat('P_G.npy',args.pg)
    if K0.shape!=(188,188) or PG.shape!=(188,188): raise ValueError('K0 and P_G must be 188x188')
    I64=np.eye(64); I188=np.eye(188)
    dist=np.linalg.norm(X[:,None,:]+X[None,:,:],axis=2)
    perm=np.argmin(dist,axis=1); err=dist[np.arange(64),perm]
    Pi=np.zeros((64,64)); Pi[np.arange(64),perm]=1.0
    if not (err.max()<1e-7 and np.array_equal(np.sort(perm),np.arange(64))):
        raise ValueError(f'Antipodal pairing failed: max residual={err.max():.3e}')
    C=np.zeros((4,192)); C[0,0::3]=1; C[1,1::3]=1; C[2,2::3]=1; C[3,:]=X.reshape(-1)
    Q=null_space(C)
    if Q.shape!=(192,188): raise ValueError(f'Unexpected tangent frame shape {Q.shape}')
    axis=np.array([1.0,np.sqrt(2.0),np.sqrt(3.0)]); axis/=np.linalg.norm(axis)
    V=np.zeros((192,64))
    for i,x in enumerate(X):
        n=np.cross(x,axis); nn=np.linalg.norm(n)
        if nn<1e-10: raise ValueError(f'Generic axis degenerate at vertex {i}')
        V[3*i:3*i+3,i]=n/nn
    Araw=Q.T@V; A,sA,rankA=polar_frame(Araw)
    if A is None: raise RuntimeError(f'Geometric map rank {rankA}/64')
    Damb=-np.kron(Pi,np.eye(3)); Rgeo=Q.T@Damb@Q
    tangent_invariance=np.linalg.norm(Damb@Q-Q@Rgeo,'fro')
    geometric_equivariance=np.linalg.norm(Rgeo@A-A@Pi,'fro')
    PGs=(PG+PG.T)/2; wp,Vp=eigh(PGs); Ug=Vp[:,wp>.5]
    B=PGs@A; Ugeom,sB,rankB=polar_frame(B)
    containment=np.linalg.norm(PGs@A-A,'fro')
    overlap=svd(Ug.T@A,compute_uv=False)
    Rkernel=None; kres=None
    if Ugeom is not None:
        Rkernel=Ugeom@Pi@Ugeom.T+(I188-PGs)
        kres={'Ugeom_orthogonality':float(np.linalg.norm(Ugeom.T@Ugeom-I64,'fro')),
          'P_G_Ugeom_minus_Ugeom':float(np.linalg.norm(PGs@Ugeom-Ugeom,'fro')),
          'K0_Ugeom':float(np.linalg.norm(K0@Ugeom,'fro')),
          'Rkernel_involution':float(np.linalg.norm(Rkernel@Rkernel-I188,'fro')),
          'Rkernel_orthogonality':float(np.linalg.norm(Rkernel.T@Rkernel-I188,'fro')),
          'relative_commutator_K0_Rkernel':float(np.linalg.norm(K0@Rkernel-Rkernel@K0,'fro')/max(1.,np.linalg.norm(K0,'fro'))),
          'warning':'Commutation follows from construction on Ker(K0); it is not independent proof of geometric identification.'}
    direct={'Rgeo_symmetry':float(np.linalg.norm(Rgeo-Rgeo.T,'fro')),
      'Rgeo_involution':float(np.linalg.norm(Rgeo@Rgeo-I188,'fro')),
      'tangent_invariance_DQ_minus_QRgeo':float(tangent_invariance),
      'relative_commutator_K0_Rgeo_if_same_188D_basis':float(np.linalg.norm(K0@Rgeo-Rgeo@K0,'fro')/max(1.,np.linalg.norm(K0,'fro'))),
      'basis_warning':'Direct commutator is interpretable only if K0 and Q use the same 188D tangent coordinates.'}
    report={'title':'RGS-PSU geometry-driven Anti-Twin intertwiner construction',
      'status':'COMPUTED' if not args.proxy else 'PIPELINE_SMOKE_TEST_ONLY_PROXY_GEOMETRY',
      'sources':{'X':xsource,'K0':kpath,'P_G':pgpath},
      'construction':{'ambient_feature':'V_i=normalized cross(X_i,generic_axis)','A_raw':'Q.T @ V','A':'polar factor of A_raw','projected_intertwiner':'polar factor of P_G @ A'},
      'dimensions':{'X':list(X.shape),'Q':list(Q.shape),'V':list(V.shape),'A_raw':list(Araw.shape),'P_G_rank':int(Ug.shape[1]),'projected_rank':int(rankB)},
      'antipodal':{'max_pair_residual':float(err.max()),'Pi_symmetry':float(np.linalg.norm(Pi-Pi.T,'fro')),'Pi_involution':float(np.linalg.norm(Pi@Pi-I64,'fro')),'Pi_trace':float(np.trace(Pi)),'ambient_equivariance_DV_minus_VPi':float(np.linalg.norm(Damb@V-V@Pi))},
      'singular_values_A_raw':sA.tolist(),'singular_values_PG_A':sB.tolist(),
      'geometry_kernel_alignment':{'Frobenius_distance_PG_A_minus_A':float(containment),'principal_angle_cosines':overlap.tolist(),'minimum_cosine':float(overlap.min()),'maximum_cosine':float(overlap.max())},
      'projected_polar_extension':kres,'direct_tangent_action':direct,
      'geometric_map_equivariance_Rgeo_A_minus_A_Pi':float(geometric_equivariance),
      'K0_intrinsic':{'symmetry':float(np.linalg.norm(K0-K0.T,'fro')),'P_G_idempotency':float(np.linalg.norm(PG@PG-PG,'fro')),'K0P_G':float(np.linalg.norm(K0@PG,'fro')),'P_GK0':float(np.linalg.norm(PG@K0,'fro'))},
      'limitations':['Feature map is antipodally equivariant but is not thereby identified with the original kernel.','Projected-polar extension commutes with K0 by construction.','Direct [K0,Rgeo] requires verified basis alignment.']}
    out=args.out if os.path.isabs(args.out) else os.path.join(base,args.out)
    with open(out,'w') as f: json.dump(report,f,indent=2)
    payload={'Pi_AT':Pi,'Q_tangent':Q,'V_vertex_modes':V,'A_raw':Araw,'A_geometry_orthonormal':A,'P_G':PG,'K0':K0,'R_geo_tangent':Rgeo,'principal_angle_cosines':overlap,'singular_values_A_raw':sA,'singular_values_PG_A':sB}
    if Ugeom is not None: payload.update({'U_geom_projected':Ugeom,'R_AT_kernel_extension':Rkernel})
    np.savez_compressed(os.path.splitext(out)[0]+'_matrices.npz',**payload)
    print(json.dumps(report,indent=2))

if __name__=='__main__': main()
