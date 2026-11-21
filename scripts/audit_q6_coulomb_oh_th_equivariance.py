#!/usr/bin/env python3
"""Coulomb Hessian, O_h/T_h equivariance and isotypic audit for the 64-point RGS configuration.

Input: RGS_PSU_all_matrices.npz containing X_Oh_reconstructed, Q_tangent,
       Q6_adjacency.
The generated K_C is a constrained Coulomb Hessian, NOT the archived K0.
"""
from __future__ import annotations
import argparse, itertools, json
from pathlib import Path
import numpy as np
from scipy.spatial.distance import cdist

TOL = 1e-8

def signed_permutations():
    for perm in itertools.permutations(range(3)):
        P = np.eye(3)[list(perm)]
        for signs in itertools.product((-1, 1), repeat=3):
            yield np.diag(signs) @ P

def action_data(X, Q, adjacency):
    n = len(X)
    all_actions = []
    for G in signed_permutations():
        Y = X @ G.T
        D = cdist(Y, X)
        p = D.argmin(axis=1)
        err = float(D[np.arange(n), p].max())
        if err > TOL or len(set(p.tolist())) != n:
            continue
        preserves = bool(np.array_equal(adjacency[np.ix_(p, p)], adjacency))
        S = np.zeros((3*n, 3*n))
        for i, j in enumerate(p):
            S[3*j:3*j+3, 3*i:3*i+3] = G
        U = Q.T @ S @ Q
        subspace_res = float(np.linalg.norm(S@Q-Q@U, 'fro') / np.linalg.norm(Q, 'fro'))
        orth_res = float(np.linalg.norm(U.T@U-np.eye(Q.shape[1]), 'fro'))
        comm_data = {'G':G, 'p':p, 'adj':preserves, 'S':S, 'U':U,
                     'subspace_res':subspace_res, 'orth_res':orth_res,
                     'point_error':err}
        all_actions.append(comm_data)
    return all_actions

def coulomb(X):
    n = len(X)
    grad = np.zeros((n,3))
    H = np.zeros((3*n,3*n))
    E = 0.0
    for i in range(n):
        for j in range(i+1,n):
            d = X[i]-X[j]
            r = np.linalg.norm(d)
            E += 1.0/r
            grad[i] += -d/r**3
            grad[j] += d/r**3
            B = 3*np.outer(d,d)/r**5 - np.eye(3)/r**3
            si, sj = slice(3*i,3*i+3), slice(3*j,3*j+3)
            H[si,si] += B; H[sj,sj] += B
            H[si,sj] -= B; H[sj,si] -= B
    return E, grad, H

def oh_class(R):
    tr = round(float(np.trace(R)))
    if np.allclose(R, np.eye(3)): return 'E'
    if tr == 0: return '8C3'
    if tr == 1: return '6C4'
    if tr == -1:
        offdiag = np.count_nonzero(np.abs(R-np.diag(np.diag(R))) > 1e-8)
        return '3C2' if offdiag == 0 else '6C2p'
    raise ValueError(f'Unclassified proper octahedral element: {R}')

def tetra_class(R):
    tr = round(float(np.trace(R)))
    if np.allclose(R, np.eye(3)): return 'E'
    if tr == 0:
        # The two A4 classes of 3-cycles are distinguished by the underlying
        # coordinate 3-cycle (not by an arbitrary fixed-axis dot product).
        perm = tuple(np.argmax(np.abs(R), axis=1).tolist())
        return 'C3a' if perm == (1, 2, 0) else 'C3b'
    if tr == -1: return 'C2'
    raise ValueError(f'Unclassified tetrahedral element: {R}')

def decompositions(actions):
    oh_chars = {
        'A1':[1,1,1,1,1], 'A2':[1,1,1,-1,-1],
        'E':[2,-1,2,0,0], 'T1':[3,0,-1,1,-1], 'T2':[3,0,-1,-1,1]
    }
    oh_order = ['E','8C3','3C2','6C4','6C2p']
    omega = np.exp(2j*np.pi/3)
    th_chars = {
        '1':[1,1,1,1], '1p':[1,omega,omega**2,1],
        '1pp':[1,omega**2,omega,1], '3':[3,0,0,-1]
    }
    th_order = ['E','C3a','C3b','C2']
    out = {'O_h':{}, 'T_h':{}}
    # O_h = O x {1,inversion}; every G is c*R with R proper and c=det(G).
    for parity in ('g','u'):
        for ir, chars in oh_chars.items():
            total = 0.0
            for a in actions:
                G = a['G']; c = int(round(np.linalg.det(G))); R = c*G
                ch = chars[oh_order.index(oh_class(R))]
                if parity == 'u' and c == -1: ch = -ch
                total += float(np.trace(a['U'])) * ch
            out['O_h'][ir+parity] = int(round(total/48))
    # T_h subgroup: proper tetrahedral rotations preserving xyz>0 tetrahedron,
    # together with their products by central inversion. In signed-permutation
    # coordinates this is product(nonzero entries)=det(G).
    th = []
    for a in actions:
        G = a['G']; det = int(round(np.linalg.det(G)))
        sign_product = int(round(np.prod(G[np.abs(G)>0.5])))
        if sign_product == det: th.append(a)
    if len(th) != 24:
        raise RuntimeError(f'Expected |T_h|=24, got {len(th)}')
    for parity in ('g','u'):
        for ir, chars in th_chars.items():
            total = 0j
            for a in th:
                G=a['G']; c=int(round(np.linalg.det(G))); R=c*G
                ch=chars[th_order.index(tetra_class(R))]
                if parity == 'u' and c == -1: ch=-ch
                total += np.trace(a['U']) * np.conjugate(ch)
            m=total/24
            if abs(m.imag)>1e-7: raise RuntimeError(f'Non-real multiplicity {ir}{parity}: {m}')
            out['T_h'][ir+parity] = int(round(m.real))
    return out, len(th)


def isotypic_blocks(actions, Kc):
    """Return ranks and compressed spectra of all O_h and T_h isotypic projectors."""
    result = {'O_h': {}, 'T_h': {}}
    oh_chars = {
        'A1':[1,1,1,1,1], 'A2':[1,1,1,-1,-1],
        'E':[2,-1,2,0,0], 'T1':[3,0,-1,1,-1], 'T2':[3,0,-1,-1,1]
    }
    oh_order = ['E','8C3','3C2','6C4','6C2p']
    for parity in ('g','u'):
        for ir, chars in oh_chars.items():
            P = np.zeros_like(Kc)
            for a in actions:
                G=a['G']; c=int(round(np.linalg.det(G))); R=c*G
                ch=chars[oh_order.index(oh_class(R))]
                if parity=='u' and c==-1: ch=-ch
                P += ch*a['U']
            P *= chars[0]/48
            P=(P+P.T)/2
            ew,ev=np.linalg.eigh(P); keep=ew>0.5
            B=ev[:,keep]; rank=int(np.sum(keep))
            block=np.linalg.eigvalsh(B.T@Kc@B)
            result['O_h'][ir+parity]={
                'rank':rank,
                'projector_idempotence_fro':float(np.linalg.norm(P@P-P,'fro')),
                'projector_commutator_fro':float(np.linalg.norm(P@Kc-Kc@P,'fro')),
                'eigenvalue_min':float(block.min()),
                'eigenvalue_max':float(block.max()),
                'negative':int(np.sum(block < -1e-8)),
                'near_zero':int(np.sum(np.abs(block)<=1e-8)),
                'positive':int(np.sum(block > 1e-8))
            }
    omega=np.exp(2j*np.pi/3)
    th_chars={'1':[1,1,1,1], '1p':[1,omega,omega**2,1],
              '1pp':[1,omega**2,omega,1], '3':[3,0,0,-1]}
    th_order=['E','C3a','C3b','C2']
    th=[]
    for a in actions:
        G=a['G']; det=int(round(np.linalg.det(G)))
        sign_product=int(round(np.prod(G[np.abs(G)>0.5])))
        if sign_product==det: th.append(a)
    for parity in ('g','u'):
        for ir, chars in th_chars.items():
            P=np.zeros_like(Kc,dtype=complex)
            for a in th:
                G=a['G']; c=int(round(np.linalg.det(G))); R=c*G
                ch=chars[th_order.index(tetra_class(R))]
                if parity=='u' and c==-1: ch=-ch
                P += np.conjugate(ch)*a['U']
            P *= chars[0]/24
            P=(P+P.conj().T)/2
            ew,ev=np.linalg.eigh(P); keep=ew>0.5
            B=ev[:,keep]; rank=int(np.sum(keep))
            block=np.linalg.eigvalsh(B.conj().T@Kc@B)
            result['T_h'][ir+parity]={
                'rank':rank,
                'projector_idempotence_fro':float(np.linalg.norm(P@P-P,'fro')),
                'projector_commutator_fro':float(np.linalg.norm(P@Kc-Kc@P,'fro')),
                'eigenvalue_min':float(block.min()),
                'eigenvalue_max':float(block.max()),
                'negative':int(np.sum(block < -1e-8)),
                'near_zero':int(np.sum(np.abs(block)<=1e-8)),
                'positive':int(np.sum(block > 1e-8))
            }
    return result

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--npz', required=True)
    ap.add_argument('--out-dir', default='coulomb_q6_audit')
    args=ap.parse_args()
    out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
    z=np.load(args.npz)
    X=z['X_Oh_reconstructed']; Q=z['Q_tangent']; A=z['Q6_adjacency']
    actions=action_data(X,Q,A)
    if len(actions)!=48: raise RuntimeError(f'Expected 48 O_h actions, got {len(actions)}')
    E,grad,H=coulomb(X)
    x=X.reshape(-1); g=grad.reshape(-1)
    lam=-float(g@x)/(float(x@x))
    stationarity=g+lam*x
    Kc=Q.T@(H+lam*np.eye(3*len(X)))@Q
    Kc=(Kc+Kc.T)/2
    w,V=np.linalg.eigh(Kc)
    zero_idx=np.where(np.abs(w)<1e-8)[0]
    rotations=[]
    rot_tangent_res=[]
    for axis in np.eye(3):
        d=np.cross(np.tile(axis,(len(X),1)),X).reshape(-1)
        q=Q.T@d; rotations.append(q)
        rot_tangent_res.append(float(np.linalg.norm(d-Q@q)))
    Rrot=np.stack(rotations,axis=1)
    sv=np.linalg.svd(V[:,zero_idx].T@Rrot,compute_uv=False)
    dec, th_order=decompositions(actions)
    group_results={}
    for label, subset in [('O_h',actions),('Q6_graph_automorphisms',[a for a in actions if a['adj']])]:
        comm=[]
        for a in subset:
            comm.append(float(np.linalg.norm(Kc@a['U']-a['U']@Kc,'fro')/np.linalg.norm(Kc,'fro')))
        group_results[label]={
            'order':len(subset),
            'max_adjacency_residual':0.0 if all(a['adj'] for a in subset) else None,
            'max_tangent_subspace_residual':max(a['subspace_res'] for a in subset),
            'max_representation_orthogonality_residual':max(a['orth_res'] for a in subset),
            'max_relative_commutator':max(comm),
        }
    report={
      'input':str(Path(args.npz).name),
      'n_points':len(X),'ambient_dimension':3*len(X),'tangent_dimension':Q.shape[1],
      'tangent_codimension':3*len(X)-Q.shape[1],
      'Q_orthogonality_fro':float(np.linalg.norm(Q.T@Q-np.eye(Q.shape[1]),'fro')),
      'centroid':X.mean(axis=0).tolist(),
      'Q_translation_annihilation_norms':[float(np.linalg.norm(Q.T@np.tile(a,len(X)))) for a in np.eye(3)],
      'Q_scale_annihilation_norm':float(np.linalg.norm(Q.T@x)),
      'O_h_point_action_order':len(actions),
      'Q6_adjacency_automorphism_order':sum(a['adj'] for a in actions),
      'groups':group_results,
      'coulomb':{
        'energy':E,'gradient_norm':float(np.linalg.norm(g)),
        'gradient_per_coordinate_rms':float(np.linalg.norm(g)/np.sqrt(len(g))),
        'radial_multiplier_lambda':lam,
        'stationarity_residual_norm_grad_plus_lambda_X':float(np.linalg.norm(stationarity)),
        'radial_alignment_cosine':float(abs(g@x)/(np.linalg.norm(g)*np.linalg.norm(x))),
        'K_C_spectrum':{'min':float(w.min()),'max':float(w.max()),
          'negative':int(np.sum(w < -1e-8)),'near_zero':int(np.sum(np.abs(w)<=1e-8)),
          'positive':int(np.sum(w>1e-8))},
        'zero_modes_match_rigid_rotations':{
          'number_zero_modes':int(len(zero_idx)),
          'rotation_rank':int(np.linalg.matrix_rank(Rrot,tol=1e-8)),
          'rotation_tangent_residuals':rot_tangent_res,
          'principal_overlap_singular_values':sv.tolist()
        }
      },
      'irreducible_multiplicities':dec,\n      'isotypic_block_spectra':isotypic_blocks(actions,Kc),
      'T_h_subgroup_order':th_order,
      'classification':{
        'K_C':'constrained Coulomb Hessian, distinct from archived K0',
        'O_h_action_on_64_labels':'valid as a point-set permutation for all 48 elements',
        'Q6_adjacency':'preserved by only 16 of the 48 O_h elements',
        'lambda':'chosen by the global spherical constraint grad(E)+lambda*X=0',
        'T_h':'subgroup selected by the xyz>0 tetrahedron convention'
      }
    }
    np.savez_compressed(out/'K_C_coulomb_constrained_188d.npz',
        K_C=Kc,H_coulomb=H,gradient=grad,lambda_radial=np.array(lam),
        eigenvalues=w,eigenvectors=V)
    (out/'report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__': main()
