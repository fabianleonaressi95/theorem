import unittest
from src.t037_rumin_harmonic_multiplicities import run

class TestT037Multiplicity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = run(2)

    def test_degrees_and_success(self):
        self.assertTrue(self.report['passed'])
        self.assertEqual(self.report['degrees_checked'], [0, 1, 2])

    def test_hom_dimensions_match_molien(self):
        for labels in self.report['decompositions'].values():
            for entry in labels.values():
                self.assertEqual(entry['Hom_dimension'], entry['Molien_multiplicity'])
                self.assertEqual(entry['central_projector_rank'], entry['isotypic_dimension'])

    def test_total_dimension(self):
        for degree, labels in self.report['decompositions'].items():
            total = sum(item['isotypic_dimension'] for item in labels.values())
            self.assertEqual(total, int(degree) + 1)

if __name__ == '__main__':
    unittest.main()
