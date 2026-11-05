import unittest
import sympy as sp
from src.t032_2i_molien import IRREP_DIMENSIONS
from src.t036_2i_irreducible_models import (
    build_all_models, verify_models, symmetric_power_matrix
)
from audits.t035_exact_binary_icosahedral_model import elements_2i, rho2

class TestT036ExplicitIrreducibleModels(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.group,cls.chars,cls.degrees,cls.models=build_all_models()
        cls.report=verify_models(cls.group,cls.chars,cls.degrees,cls.models)

    def test_nine_models_and_dimensions(self):
        self.assertEqual(set(self.models),set(IRREP_DIMENSIONS))
        for label,d in IRREP_DIMENSIONS.items():
            self.assertEqual(self.models[label]["projector_rank"],d)
            self.assertEqual(len(self.models[label]["matrices"]),120)

    def test_character_table_recovered(self):
        self.assertTrue(self.report["passed"])
        for label,d in IRREP_DIMENSIONS.items():
            for j in range(9):
                indices=[i for i,q in enumerate(self.group)
                         if __import__("audits.t035_exact_binary_icosahedral_model",
                           fromlist=["CLASS_SCALARS"]).CLASS_SCALARS.index(q[0])==j]
                self.assertEqual(sp.simplify(sp.trace(self.models[label]["matrices"][indices[0]])-
                                             self.chars[label][j]),0)

    def test_invariant_hermitian_metrics(self):
        for label,m in self.models.items():
            G=m["gram"]
            self.assertNotEqual(G.det(),0)
            for R in m["matrices"]:
                self.assertEqual(sp.simplify(R.conjugate().T*G*R-G),sp.zeros(G.rows))

if __name__=="__main__": unittest.main()
