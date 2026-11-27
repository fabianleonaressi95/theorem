import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from audit_c60_mmff94s_relaxed_coulomb import c60_ideal
from audit_c60_stone_wales import graph_from_bonds,oriented_faces,topology,enumerate_switches,make_chain_map,incidence

def test_c60_sw_topology_and_chain_map():
    xyz,bonds=c60_ideal(); g=graph_from_bonds(len(xyz),bonds); f=oriented_faces(g)
    t=topology(g,f)
    assert (t["V"],t["E"],t["F"],t["pentagons"],t["hexagons"],t["euler"])==(60,90,32,12,20,2)
    assert set(t["degrees"])=={3}
    cs=enumerate_switches(g,f); assert len(cs)==30
    assert cs
    # Pyracylene SW_5|6 patch: central bond is 6|6, flanked by two 5-rings.
    ef=incidence(f); dual=__import__('networkx').Graph(); dual.add_nodes_from(range(len(f)))
    for fs in ef.values(): dual.add_edge(*fs)
    d1,d2=cs[0]["dual_edge"]; p1,p2=cs[0]["opposite_pentagon_faces"]
    assert sorted([dual.degree[d1],dual.degree[d2],dual.degree[p1],dual.degree[p2]])==[5,5,6,6]
    assert dual.degree[d1]==dual.degree[d2]==6 and dual.degree[p1]==dual.degree[p2]==5
    flipped=dual.copy(); flipped.remove_edge(d1,d2); flipped.add_edge(p1,p2)
    assert flipped.degree[d1]==flipped.degree[d2]==5 and flipped.degree[p1]==flipped.degree[p2]==6
    h,hf=cs[0]["graph"],cs[0]["faces"]; z=topology(h,hf)
    assert (z["V"],z["E"],z["F"],z["pentagons"],z["hexagons"],z["euler"])==(60,90,32,12,20,2)
    assert set(z["degrees"])=={3}
    q=make_chain_map(g,f,h,hf)
    assert q["B1S1_equals_B1"] and q["B2S2_equals_S1B2"]
