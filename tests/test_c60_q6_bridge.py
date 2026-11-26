import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from audit_c60_q6_bridge import audit


def test_c60_cellular_homology_is_sphere_not_its_graph_cycle_space():
    result = audit()
    assert result["cell_counts_C0_C1_C2"] == [60, 90, 32]
    assert result["boundary_ranks_over_Q"] == {"rank_B1": 59, "rank_B2": 31}
    assert result["betti_numbers"] == {"beta0": 1, "beta1": 0, "beta2": 1}
    assert result["euler_characteristic"] == 2
    assert result["boundary_squared_zero"]
