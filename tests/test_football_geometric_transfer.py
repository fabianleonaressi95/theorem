import sys
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from models.football_shell import build_football_shell
from models.football_quaternion_bridge import build_geometry_transfer, project_shell_tangent

def test_geometry_transfer_reproduces_constant_and_direction_fields():
    data=np.genfromtxt(ROOT/"data/rgs_188d/X_Oh_reconstructed.csv",delimiter=",",names=True)
    X=np.column_stack([data[k] for k in ("x","y","z")])
    mesh=build_football_shell()
    W,diag=build_geometry_transfer(X,mesh["nodes"],neighbors=16)
    assert W.shape==(276,192)
    assert diag["weights_row_sum_residual"]<1e-9
    assert diag["affine_direction_reproduction_frobenius"]<1e-7
    V=np.tile(np.array([[1.,0,0],[0,1.,0],[0,0,1.]]),(64,1))
    target=np.tile(np.eye(3),(92,1))
    assert np.linalg.norm(W@V-target)<1e-8

def test_shell_tangent_projection_is_tangent():
    mesh=build_football_shell()
    V=np.random.default_rng(4).normal(size=(276,3))
    T=project_shell_tangent(mesh,V)
    assert T.shape==(276,3)
    # Each node's projected vector is orthogonal to its averaged normal.
    X=mesh["nodes"]; normals=np.zeros_like(X)
    for tri in mesh["triangles"]:
        p=X[tri]; a=np.cross(p[1]-p[0],p[2]-p[0])
        for i in tri: normals[i]+=a
    normals/=np.linalg.norm(normals,axis=1)[:,None]
    tangent_modes=T.reshape(len(X),3,-1)
    assert np.max(np.abs(np.einsum("ni,nik->nk",normals,tangent_modes)))<1e-10
