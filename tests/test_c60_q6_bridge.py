import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from audit_c60_q6_bridge import audit


def test_exact_homology_of_c60_kathara_and_q6_complexes():
    result=audit()
    c60=result["complexes"]["C60"]
    kathara=result["complexes"]["Kathara"]
    q6=result["complexes"]["Q6"]
    assert c60["cell_counts_C0_C1_C2"] == [60,90,32]
    assert c60["boundary_ranks_over_Q"] == {"rank_B1":59,"rank_B2":31}
    assert c60["betti_numbers"] == {"beta0":1,"beta1":0,"beta2":1}
    assert kathara["cell_counts_C0_C1_C2"] == [12,21,10]
    assert kathara["boundary_ranks_over_Q"] == {"rank_B1":11,"rank_B2":10}
    assert kathara["betti_numbers"] == {"beta0":1,"beta1":0,"beta2":0}
    assert q6["cell_counts_C0_C1_C2"] == [64,192,240]
    assert q6["boundary_ranks_over_Q"] == {"rank_B1":63,"rank_B2":129}
    assert q6["betti_numbers"] == {"beta0":1,"beta1":0,"beta2":111}
    assert all(x["boundary_squared_zero"] for x in (c60,kathara,q6))


def test_kathara_factorization_kills_c60_fundamental_class():
    result=audit()
    assert result["complexes"]["C60"]["betti_numbers"]["beta2"] == 1
    assert result["complexes"]["Kathara"]["betti_numbers"]["beta2"] == 0
    assert "kills the C60 fundamental class" in result["homological_obstruction"]
