import numpy as np
import pytest
from models.hysteresis_metrics import loop_area,rmse,branch_separation

def test_unit_rectangle_area():
    assert loop_area([0,1,1,0,0],[0,0,1,1,0])==pytest.approx(1)

def test_rmse_identical():
    y=np.array([1.,2.,-1.]); assert rmse(y,y)==0

def test_branch_separation_positive():
    assert branch_separation([0,1,2,1,0],[0,1,2,0,-1],2)>0

def test_bad_input_rejected():
    with pytest.raises(ValueError): loop_area([0,1],[0,1])
