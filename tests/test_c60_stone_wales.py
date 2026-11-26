import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from audit_c60_mmff94s_relaxed_coulomb import c60_ideal
from audit_c60_stone_wales import graph_from_bonds,oriented_faces,topology,enumerate_switches,make_chain_map

def test_c60_sw_topology_and_chain_map():
    xyz,bonds=c60_ideal(); g=graph_from_bonds(len(xyz),bonds); f=oriented_faces(g)
    t=topology(g,f)
    assert (t["V"],t["E"],t["F"],t["pentagons"],t["hexagons"],t["euler"])==(60,90,32,12,20,2)
    assert set(t["degrees"])=={3}
    cs=enumerate_switches(g,f); assert len(cs)==30
    cs=enumerate_switches(g,f); assert cs
    h,hf=cs[0]["graph"],cs[0]["faces"]; z=topology(h,hf)
    assert (z["V"],z["E"],z["F"],z["pentagons"],z["hexagons"],z["euler"])==(60,90,32,12,20,2)
    assert set(z["degrees"])=={3}
    q=make_chain_map(g,f,h,hf)
    assert q["B1S1_equals_B1"] and q["B2S2_equals_S1B2"]
