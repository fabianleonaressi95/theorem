"""Comparison bridge between 188-DOF RGS triplets and football-shell modes.

No canonical map between the RGS 192-coordinate ambient space and the
football shell's 276-coordinate ambient space is assumed. The caller must
supply a geometric transfer operator. Subspace comparison uses principal
angles; quaternionic symmetry comparison uses SO(3) actions lifted to unit
quaternions and a least-squares intertwiner.
"""
from __future__ import annotations
import numpy as np
from .football_quaternion_tangent import quaternion_from_matrix, qrotate


def orthonormal_columns(A, tol=1e-11):
    A=np.asarray(A,float)
    if A.ndim!=2: raise ValueError("basis must be a matrix")
    U,s,_=np.linalg.svd(A,full_matrices=False)
    if len(s)==0 or s[0]==0: raise ValueError("basis has zero rank")
    rank=int(np.sum(s>tol*s[0]))
    return U[:,:rank]


def principal_angle_audit(A,B):
    """Principal angles in degrees between two column spaces in one ambient space."""
    QA=orthonormal_columns(A); QB=orthonormal_columns(B)
    if QA.shape[0]!=QB.shape[0]: raise ValueError("spaces must share an ambient coordinate system")
    if QA.shape[1]!=QB.shape[1]: raise ValueError("subspaces must have equal dimension")
    s=np.linalg.svd(QA.T@QB,compute_uv=False)
    s=np.clip(s,-1.,1.)
    angles=np.degrees(np.arccos(s))
    return {"principal_angles_degrees":angles.tolist(),
            "max_angle_degrees":float(np.max(angles)),
            "rms_angle_degrees":float(np.sqrt(np.mean(angles**2))),
            "singular_values":s.tolist()}


def quaternion_action_matrix(q):
    """SO(3) matrix induced by q p q^-1 on pure-imaginary quaternions."""
    return np.column_stack([qrotate(q,np.eye(3)[:,i]) for i in range(3)])


def quaternionic_intertwiner_audit(rgs_rotations, shell_rotations):
    """Find X satisfying S_g X = X R_g for paired rotation generators.

    Inputs are sequences of 3x3 proper rotations in corresponding generator
    order. Returns the best nonzero least-squares intertwiner and normalized
    residual. A small residual alone is not proof of symmetry: generators
    and their physical correspondence must be independently justified.
    """
    if len(rgs_rotations)!=len(shell_rotations) or not rgs_rotations:
        raise ValueError("paired nonempty generator lists required")
    blocks=[]
    for R,S in zip(rgs_rotations,shell_rotations):
        R=np.asarray(R,float); S=np.asarray(S,float)
        if R.shape!=(3,3) or S.shape!=(3,3): raise ValueError("generators must be 3x3")
        # vec(S X - X R) = (I kron S - R.T kron I) vec(X)
        blocks.append(np.kron(np.eye(3),S)-np.kron(R.T,np.eye(3)))
    L=np.vstack(blocks)
    _,sv,Vh=np.linalg.svd(L,full_matrices=False)
    x=Vh[-1]
    X=x.reshape(3,3,order="F")
    denom=np.linalg.norm(L,ord="fro")*np.linalg.norm(X)
    residual=float(np.linalg.norm(L@x)/(denom+1e-30))
    U,_,Vt=np.linalg.svd(X)
    Xorth=U@Vt
    return {"intertwiner":X.tolist(),"orthogonal_intertwiner":Xorth.tolist(),
            "normalized_residual":residual,"singular_values":sv.tolist(),
            "quaternion_lift_rgs":[quaternion_from_matrix(np.asarray(R)).tolist() for R in rgs_rotations],
            "quaternion_lift_shell":[quaternion_from_matrix(np.asarray(S)).tolist() for S in shell_rotations],
            "interpretation":"candidate intertwiner; verify generator relations, group action, commutators and stability"}


def compare_rgs_shell_triplets(rgs_triplet_192, shell_triplet_276,
                               transfer_276x192, rgs_generators=None,
                               shell_generators=None):
    """Transfer an RGS ambient triplet to shell coordinates, then compare."""
    A=np.asarray(rgs_triplet_192,float); B=np.asarray(shell_triplet_276,float)
    W=np.asarray(transfer_276x192,float)
    if A.shape!=(192,3) or B.shape!=(276,3) or W.shape!=(276,192):
        raise ValueError("expected RGS (192,3), shell (276,3), transfer (276,192)")
    mapped=W@A
    QA=orthonormal_columns(mapped); QB=orthonormal_columns(B)
    if QA.shape[1]!=3 or QB.shape[1]!=3:
        raise ValueError("both transferred and shell triplets must have rank three")
    result={"mapped_rgs_rank":3,"shell_triplet_rank":3,
            "principal_angles":principal_angle_audit(QA,QB),
            "transfer_operator_shape":[276,192],
            "warning":"result depends on the supplied geometric transfer; do not infer it from dimensions"}
    if (rgs_generators is None)!=(shell_generators is None):
        raise ValueError("supply both generator lists or neither")
    if rgs_generators is not None:
        result["quaternionic_intertwiner"]=quaternionic_intertwiner_audit(rgs_generators,shell_generators)
    return result
