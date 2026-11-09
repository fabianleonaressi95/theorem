from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from audit_prism_69120 import audit

def test_prism_product_invariants():
    B1,B2,r=audit()
    assert r["vertices"]==69120
    assert r["edges"]==345600
    assert r["square_faces"]==691200
    assert r["B1B2_exact_zero"] is True
    assert r["betti_product_torus"]==[1,5,10,10,5,1]
    assert abs(r["vertex_laplacian_gap"]-0.009630546655606143)<1e-14
