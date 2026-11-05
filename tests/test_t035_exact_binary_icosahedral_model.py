import unittest
from audits.t035_exact_binary_icosahedral_model import CLASS_ORDERS, CLASS_SIZES, audit, elements_2i, group_table
class TestExactBinaryIcosahedralModel(unittest.TestCase):
 @classmethod
 def setUpClass(cls): cls.report=audit()
 def test_order(self): self.assertEqual(len(elements_2i()),120)
 def test_group_laws(self):
  G=elements_2i(); table,e,inv=group_table(G)
  for g in range(120):
   self.assertEqual(table[e][g],g); self.assertEqual(table[g][e],g); self.assertEqual(table[g][inv[g]],e)
 def test_class_convention(self):
  self.assertEqual(CLASS_SIZES,(1,1,20,30,12,12,20,12,12))
  self.assertEqual(CLASS_ORDERS,(1,2,3,4,5,5,6,10,10))
  self.assertEqual(self.report["class_sizes"],CLASS_SIZES)
 def test_fundamental_model(self):
  self.assertTrue(self.report["passed"])
  self.assertEqual(self.report["fundamental_SU2_unitarity_checked"],120)
  self.assertEqual(self.report["fundamental_SU2_determinants_checked"],120)
if __name__=="__main__": unittest.main()
