import sys
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from models.football_quaternion_bridge import principal_angle_audit, quaternionic_intertwiner_audit, quaternion_action_matrix, compare_rgs_shell_triplets


def rot(axis, angle):
    axis=np.asarray(axis,float); axis/=np.linalg.norm(axis)
    x,y,z=axis; c=np.cos(angle); s=np.sin(angle); C=1-c
    return np.array([[c+x*x*C,x*y*C-z*s,x*z*C+y*s],
                     [y*x*C+z*s,c+y*y*C,y*z*C-x*s],
                     [z*x*C-y*s,z*y*C+x*s,c+z*z*C]])


def test_principal_angles_identical_and_orthogonal():
    A=np.eye(6)[:,:3]
    assert principal_angle_audit(A,A)["max_angle_degrees"]<1e-6
    B=np.eye(6)[:,3:]
    assert np.allclose(principal_angle_audit(A,B)["principal_angles_degrees"],[90,90,90])


def test_quaternion_intertwiner_same_representation():
    R=[rot([1,0,0],.7),rot([0,1,0],.4)]
    S=[rot([1,0,0],.7),rot([0,1,0],.4)]
    out=quaternionic_intertwiner_audit(R,S)
    assert out["normalized_residual"]<1e-12
    assert np.allclose(quaternion_action_matrix([1,0,0,0]),np.eye(3))


def test_triplet_bridge_requires_explicit_transfer():
    A=np.zeros((192,3)); A[:3,:]=np.eye(3)
    W=np.zeros((276,192)); W[:3,:3]=np.eye(3)
    B=np.zeros((276,3)); B[:3,:]=np.eye(3)
    out=compare_rgs_shell_triplets(A,B,W)
    assert out["principal_angles"]["max_angle_degrees"]<1e-6
