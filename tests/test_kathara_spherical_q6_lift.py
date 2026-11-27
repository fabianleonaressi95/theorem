import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from audit_kathara_spherical_q6_lift import audit


def test_spherical_kathara_completion_has_nonzero_q6_h2_image():
    result=audit()
    assert result["source_completion"]["outer_face"] == [1,3,6,9,12,10,7,4]
    assert result["source_completion"]["cell_counts_C0_C1_C2"] == [12,21,11]
    assert result["source_completion"]["euler_characteristic"] == 2
    assert result["maps"]["R0_shape"] == [64,12]
    assert result["maps"]["R1_shape"] == [192,21]
    assert result["maps"]["R2_shape"] == [240,11]
    assert result["maps"]["R2_rank_mod_prime"] == 11
    assert all(result["chain_identities"].values())
    assert result["fundamental_class"]["image_is_cycle"]
    assert result["fundamental_class"]["nonzero"]
    assert result["fundamental_class"]["support_faces"] == 30
    assert result["fundamental_class"]["l1_norm"] == 30
