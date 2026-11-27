import importlib.util
from pathlib import Path
import numpy as np
P=Path(__file__).parents[1]/"scripts"/"audit_hysteresis_antipodal_symmetry.py"
S=importlib.util.spec_from_file_location("anti",P)
M=importlib.util.module_from_spec(S); S.loader.exec_module(M)

def test_centrally_symmetric_loop_has_small_defect():
    t=np.linspace(0,2*np.pi,1001)
    r=M.antipodal_defect(np.cos(t),np.sin(t))
    assert r["status"]=="COMPUTED"
    assert r["antipodal_defect_nrmse_percent"]<0.2

def test_invalid_input_is_rejected():
    assert M.antipodal_defect([0,1,np.nan],[0,1,2])["status"]=="INVALID_INPUT"
