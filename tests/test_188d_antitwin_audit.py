from pathlib import Path
import sys
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from audit_188d_antitwin import audit

def test_188d_audit_pipeline(tmp_path):
    p=tmp_path/"matrices.npz"; n=188
    q=np.linalg.qr(np.random.default_rng(2).normal(size=(n,64)))[0]
    P=q@q.T; K=np.eye(n)-P; pi=np.diag([1.0]*32+[-1.0]*32)
    A=np.linalg.qr(np.random.default_rng(3).normal(size=(n,64)))[0]
    R=np.eye(n); Rk=q@pi@q.T+(np.eye(n)-P)
    np.savez(p,Pi_AT=pi,Q_tangent=np.eye(n),V_vertex_modes=np.zeros((192,64)),A_raw=A,A_geometry_orthonormal=A,P_G=P,K0=K,R_geo_tangent=R,principal_angle_cosines=np.ones(64),singular_values_A_raw=np.ones(64),singular_values_PG_A=np.ones(64),U_geom_projected=q,R_AT_kernel_extension=Rk)
    r=audit(p)
    assert r["ranks"]["P_G_rank"]==64
    assert r["ranks"]["K0_near_zero_abs_lt_1e-8"]==64
    assert r["residuals"]["P_G_idempotency_fro"]<1e-10
