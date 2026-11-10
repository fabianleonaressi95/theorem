import sys
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:sys.path.insert(0,str(ROOT))
from scipy.linalg import null_space
from models.football_shell import build_football_shell
from models.football_quaternion_bridge import build_geometry_transfer,project_shell_tangent
def test_rgs_rotation_triplet_lies_in_exact_tangent_space():
 d=np.genfromtxt(ROOT/"data/rgs_188d/X_Oh_reconstructed.csv",delimiter=",",names=True)
 X=np.column_stack([d[k] for k in ("x","y","z")]); C=np.zeros((4,192))
 C[0,0::3]=1;C[1,1::3]=1;C[2,2::3]=1;C[3]=X.reshape(-1)
 Q=null_space(C); G=np.column_stack([np.cross(np.broadcast_to(e,(64,3)),X).reshape(-1) for e in np.eye(3)])
 assert Q.shape==(192,188)
 assert np.linalg.norm(C@G)<1e-10
 assert np.linalg.matrix_rank(Q.T@G)==3
def test_transferred_rotation_triplet_has_rank_three():
 d=np.genfromtxt(ROOT/"data/rgs_188d/X_Oh_reconstructed.csv",delimiter=",",names=True)
 X=np.column_stack([d[k] for k in ("x","y","z")]);mesh=build_football_shell()
 W,_=build_geometry_transfer(X,mesh["nodes"],neighbors=16)
 G=np.column_stack([np.cross(np.broadcast_to(e,(64,3)),X).reshape(-1) for e in np.eye(3)])
 C=np.zeros((4,192));C[0,0::3]=1;C[1,1::3]=1;C[2,2::3]=1;C[3]=X.reshape(-1)
 Q=null_space(C);U,_,_=np.linalg.svd(Q.T@G,full_matrices=False);A=Q@U[:,:3]
 V=project_shell_tangent(mesh,W@A)
 assert np.linalg.matrix_rank(V,tol=1e-9)==3


def test_direction_grouped_transfer_has_stable_full_rank_triplet():
    from models.football_quaternion_bridge import principal_angle_audit
    from models.football_quaternion_tangent import quaternion_from_matrix,qrotate
    d=np.genfromtxt(ROOT/"data/rgs_188d/X_Oh_reconstructed.csv",delimiter=",",names=True)
    X=np.column_stack([d[k] for k in ("x","y","z")])
    mesh=build_football_shell()
    C=np.zeros((4,192)); C[0,0::3]=1; C[1,1::3]=1; C[2,2::3]=1; C[3]=X.reshape(-1)
    Q=null_space(C)
    G=np.column_stack([np.cross(np.broadcast_to(e,(64,3)),X).reshape(-1) for e in np.eye(3)])
    U,s,_=np.linalg.svd(Q@(Q.T@G),full_matrices=False); A=U[:,:3]
    for k in (8,12,16,24,32):
        W,diag=build_geometry_transfer(X,mesh["nodes"],neighbors=k)
        assert diag["distinct_source_direction_count"]==56
        assert diag["duplicate_direction_group_count"]==8
        assert diag["duplicate_direction_group_sizes"]==[2]*8
        assert diag["source_direction_min_separation_unique"]>0
        assert diag["affine_direction_reproduction_frobenius"]<1e-8
        mapped=project_shell_tangent(mesh,W@A)
        assert np.linalg.matrix_rank(mapped,tol=1e-9)==3

def test_quaternion_double_cover_and_rotation_action():
    from models.football_quaternion_tangent import quaternion_from_matrix,qrotate
    angle=.41
    R=np.array([[np.cos(angle),-np.sin(angle),0],
                [np.sin(angle),np.cos(angle),0],[0,0,1.]])
    q=quaternion_from_matrix(R); v=np.array([.2,-.5,.7])
    assert np.linalg.norm(qrotate(q,v)-R@v)<1e-12
    assert np.linalg.norm(qrotate(q,v)-qrotate(-q,v))<1e-12
