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


def build_geometry_transfer(source_points, target_nodes, neighbors=12, rank_tolerance=1e-10,
                            direction_tolerance=1e-10):
    """Build a 192->276 transfer using distinct source directions.

    Coincident source directions at different radii are first grouped. The
    affine directional weights are computed on unique directions, then each
    group's weight is split equally among its original radial representatives.
    This removes KD-tree tie-breaking dependence without pretending the
    different-radius points are the same physical site.
    """
    from scipy.spatial import cKDTree
    X=np.asarray(source_points,float); Y=np.asarray(target_nodes,float)
    if X.shape!=(64,3) or Y.shape!=(92,3):
        raise ValueError("expected source_points (64,3) and target_nodes (92,3)")
    if neighbors<4: raise ValueError("neighbors must be at least four")
    nx=np.linalg.norm(X,axis=1); ny=np.linalg.norm(Y,axis=1)
    if np.any(nx<=0) or np.any(ny<=0): raise ValueError("points must be nonzero")
    Xn=X/nx[:,None]; Yn=Y/ny[:,None]

    # Deterministic tolerance-based grouping of coincident unit directions.
    groups=[]; representatives=[]
    for i,direction in enumerate(Xn):
        match=None
        for g,rep in enumerate(representatives):
            if np.linalg.norm(direction-rep)<=direction_tolerance:
                match=g; break
        if match is None:
            representatives.append(direction.copy()); groups.append([i])
        else:
            groups[match].append(i)
    U=np.asarray(representatives)
    if len(U)<4: raise ValueError("fewer than four distinct source directions")
    if neighbors>len(U):
        raise ValueError(f"neighbors={neighbors} exceeds {len(U)} distinct source directions")
    tree=cKDTree(U); k=int(neighbors)
    weights_unique=np.zeros((len(Yn),len(U))); condition_numbers=[]
    for j,y in enumerate(Yn):
        _,ids=tree.query(y,k=k); ids=np.atleast_1d(ids).astype(int)
        C=np.vstack((np.ones(k),U[ids].T)); d=np.r_[1.,y]
        gram=C@C.T
        condition_numbers.append(float(np.linalg.cond(gram)))
        w=C.T@np.linalg.pinv(gram,rcond=rank_tolerance)@d
        weights_unique[j,ids]=w
    weights=np.zeros((len(Yn),len(Xn)))
    for g,members in enumerate(groups):
        weights[:,members]=weights_unique[:,g,None]/len(members)
    W=np.kron(weights,np.eye(3))
    affine=np.column_stack((np.ones(len(U)),U))
    affine_residual=float(np.linalg.norm(
        weights_unique@affine-np.column_stack((np.ones(len(Yn)),Yn)),ord="fro"))
    pairwise=np.linalg.norm(U[:,None,:]-U[None,:,:],axis=2)
    pairwise+=np.eye(len(U))*10.
    duplicate_sizes=[len(g) for g in groups if len(g)>1]
    duplicate_radial_spreads=[float(np.ptp(nx[g])) for g in groups if len(g)>1]
    return W,{"source_point_count":int(len(Xn)),
        "distinct_source_direction_count":int(len(U)),
        "duplicate_direction_group_count":int(len(duplicate_sizes)),
        "duplicate_direction_group_sizes":duplicate_sizes,
        "duplicate_direction_radial_spreads":duplicate_radial_spreads,
        "source_direction_min_separation_unique":float(np.min(pairwise)),
        "neighbors_distinct_directions":k,
        "weights_min":float(weights.min()),"weights_max":float(weights.max()),
        "max_local_constraint_condition":float(max(condition_numbers)),
        "affine_direction_reproduction_frobenius":affine_residual,
        "weights_row_sum_residual":float(np.linalg.norm(weights.sum(axis=1)-1)),
        "transfer_shape":list(W.shape),
        "method":"local minimum-norm affine interpolation on unique directions; each directional weight is split equally across coincident radial representatives"}

def project_shell_tangent(mesh, ambient_modes):
    """Project 3N ambient vector modes into the node-wise shell tangent plane."""
    X=np.asarray(mesh["nodes"],float); tris=np.asarray(mesh["triangles"],int)
    V=np.asarray(ambient_modes,float)
    if V.ndim!=2 or V.shape[0]!=3*len(X):
        raise ValueError("ambient_modes must have 3N rows for this shell")
    normals=np.zeros_like(X)
    for tri in tris:
        p=X[tri]; av=np.cross(p[1]-p[0],p[2]-p[0])
        for node in tri: normals[node]+=av
    normals/=np.linalg.norm(normals,axis=1)[:,None]
    out=V.reshape(len(X),3,-1).copy()
    out-=normals[:,:,None]*np.einsum("ni,nik->nk",normals,out)[:,None,:]
    return out.reshape(3*len(X),-1)
