import importlib.util
from pathlib import Path
import numpy as np

P=Path(__file__).parents[1]/"scripts"/"audit_ja_local_identifiability.py"
S=importlib.util.spec_from_file_location("ja_ident",P)
M=importlib.util.module_from_spec(S); S.loader.exec_module(M)

def test_central_difference_recovers_linear_jacobian():
    A=np.array([[2.,-1.],[.5,3.],[-4.,2.]])
    J=M.jacobian(lambda x:A@x+np.array([1.,-2.,.25]),np.array([.3,-.7]))
    np.testing.assert_allclose(J,A,rtol=1e-8,atol=1e-8)

def test_constant_field_preserves_initial_state():
    H=np.zeros(12); p=np.array([100.,50.,.001,.2,20.])
    np.testing.assert_allclose(M.simulate(H,p,3.),np.full(12,3.))

def test_monotone_branch_is_finite_and_increasing():
    H=np.linspace(-100.,100.,101); p=np.array([100.,50.,.001,.2,20.])
    out=M.simulate(H,p,0.)
    assert np.isfinite(out).all()
    assert out[-1]>out[0]
