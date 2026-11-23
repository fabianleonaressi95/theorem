import unittest

from scripts.audit_64tg_fcc_coordinates import build_model, audit


class Test64TGCoordinateReconstruction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = build_model()

    def test_published_counts_are_reproduced(self):
        result = audit(self.model)
        self.assertEqual(result["vertices"], 63)
        self.assertEqual(result["edges"], 240)
        self.assertEqual(result["tetrahedra"], 64)
        self.assertEqual(result["octahedral_cavities"], 14)
        self.assertEqual(result["square_pyramidal_cavities"], 24)

    def test_cuboctahedron_partition_counts(self):
        result = audit(self.model)
        self.assertEqual(result["tetrahedra_inside_cuboctahedron"], 56)
        self.assertEqual(result["tetrahedra_outside_cuboctahedron"], 8)
        self.assertEqual(result["boundary_facets_by_size"], {3: 32, 4: 24})

    def test_all_octahedral_faces_are_tetrahedron_faces(self):
        result = audit(self.model)
        self.assertEqual(result["cell_face_incidences"], {1: 56, 2: 200})


if __name__ == "__main__":
    unittest.main()
