import numpy as np
from scripts.run_q6_hysteresis_sweep_study import compare_branches, run_study


def test_branch_metrics_zero_for_identical_branches():
    sigmas=np.linspace(0,1,5)
    rows=[{"R0":float(x),"R1_down":float(x*x),"R1_up":float(1-x)}
          for x in sigmas]
    backward=[{"R0":float(x),"R1_down":float(x*x),"R1_up":float(1-x)}
              for x in sigmas[::-1]]
    m=compare_branches(sigmas,rows,backward)
    assert all(v["mean_abs_branch_gap"] < 1e-14 for v in m.values())
    assert all(v["loop_area_sigma_order"] < 1e-14 for v in m.values())


def test_branch_metrics_detect_separation():
    sigmas=np.linspace(0,1,5)
    f=[{"R0":float(x),"R1_down":float(x),"R1_up":float(x)} for x in sigmas]
    b=[{"R0":float(x+.2),"R1_down":float(x+.1),"R1_up":float(x+.3)}
       for x in sigmas[::-1]]
    m=compare_branches(sigmas,f,b)
    assert m["R0"]["mean_abs_branch_gap"] > .19
    assert m["R1_down"]["mean_abs_branch_gap"] > .09
    assert m["R1_up"]["mean_abs_branch_gap"] > .29


def test_small_multiseed_multirate_study_shape():
    r=run_study([2,5],[1,2],.2,3,.01)
    assert len(r["runs"])==2*2*2
    assert set(r["summary"])=={
        "NL_dwell_1","NL_dwell_2","NLT_dwell_1","NLT_dwell_2"}
    assert r["protocol"]["seeds"]==[2,5]
    assert r["protocol"]["effective_sweep_rate"]["1"] > r["protocol"]["effective_sweep_rate"]["2"]
