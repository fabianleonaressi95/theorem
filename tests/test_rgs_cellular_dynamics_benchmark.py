import numpy as np
from scripts.rgs_cellular_dynamics_benchmark import q6_graph, cycle_product_graph, square_moore_graph, update

def test_q6_graph():
    g=q6_graph()
    assert (g.n,g.degree)==(64,6)
    assert len({tuple(sorted((v,int(w))) for w in g.neighbours[v]) for v in range(g.n)})==64
    assert all(int(w) in set(g.neighbours[int(w)]) for v in range(g.n) for w in g.neighbours[v])

def test_prism_graph():
    g=cycle_product_graph((64,6,6,6,5),"PRISM")
    assert (g.n,g.degree)==(69120,10)
    assert all(len(set(row.tolist()))==10 for row in g.neighbours)

def test_totalistic_constant_zero_rule():
    g=q6_graph(); state=np.ones(64,dtype=np.uint8); rule=np.zeros((2,7),dtype=np.uint8)
    assert not update(state,g,rule,"totalistic").any()

def test_ordered_constant_one_rule():
    g=q6_graph(); state=np.zeros(64,dtype=np.uint8); rule=np.ones(1<<7,dtype=np.uint8)
    assert update(state,g,rule,"ordered").all()
