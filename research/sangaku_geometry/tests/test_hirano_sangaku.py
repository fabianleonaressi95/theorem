import sympy as sp

from research.sangaku_geometry.hirano_sangaku import verify


def test_hirano_sangaku_exact_construction():
    result = verify()
    assert sp.simplify(result["CT"] - (sp.sqrt(5) - 1) / 2) == 0
    assert sp.simplify(result["EF_squared"] - (5 - sp.sqrt(5)) / 2) == 0
    assert sp.simplify(result["central_cosine"] - (sp.sqrt(5) - 1) / 4) == 0
