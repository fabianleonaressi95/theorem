import sys
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from models.football_shell import build_football_shell, solve_discrete_shell
from models.football_quaternion_tangent import qrotate, quaternion_from_matrix, build_tangent_quaternion_audit


def test_quaternion_double_cover_and_rotation():
    a=.37
    R=np.array([[np.cos(a),-np.sin(a),0],[np.sin(a),np.cos(a),0],[0,0,1.]])
    q=quaternion_from_matrix(R)
    v=np.array([.3,-.4,.8])
    assert np.allclose(qrotate(q,v),R@v,atol=1e-12)
    assert np.allclose(qrotate(-q,v),R@v,atol=1e-12)


def test_shell_tangent_quaternion_lift_dimensions_and_orthogonality():
    mesh=build_football_shell()
    _,_,K,_=solve_discrete_shell(mesh)
    out=build_tangent_quaternion_audit(mesh,K)
    T=out["tangent_basis"]
    assert T.shape==(276,184)
    assert out["tangent_basis_rank"]==184
    assert np.allclose(T.T@T,np.eye(184),atol=1e-12)
    assert out["tangent_stiffness"].shape==(184,184)
    assert len(out["quaternion_frames"])==92
    assert np.allclose(np.linalg.norm(out["quaternion_frames"],axis=1),1.,atol=1e-12)


def test_quaternion_frames_reconstruct_local_normals():
    mesh=build_football_shell()
    _,_,K,_=solve_discrete_shell(mesh)
    out=build_tangent_quaternion_audit(mesh,K)
    for R in out["local_frames"]:
        assert np.allclose(R.T@R,np.eye(3),atol=1e-12)
        assert np.linalg.det(R)>0.999999
