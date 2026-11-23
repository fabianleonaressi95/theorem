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
        self.assertEqual(result["oriented_internal_triangles_cancelled"], 200)
        self.assertEqual(result["outward_boundary_triangles"], 32)
        self.assertEqual(result["outward_boundary_squares"], 24)

    def test_circumsphere_pair_and_triple_overlaps(self):
        result = audit(self.model)
        self.assertEqual(result["tetrahedron_circumspheres"], 64)
        self.assertEqual(result["pairwise_circumsphere_lenses"], 360)
        self.assertEqual(result["common_triple_ball_intersections"], 648)

    def test_exact_cell_moment_records(self):
        moments = self.model["cell_moments"]
        self.assertEqual(len(moments["tetrahedra"]), 64)
        self.assertEqual(len(moments["octahedra"]), 14)
        self.assertEqual(len(moments["square_pyramids"]), 24)
        self.assertEqual(moments["tetrahedra"][0]["covariance_over_a2_diagonal"], ["1/160"] * 3)
        self.assertEqual(moments["octahedra"][0]["covariance_over_a2_diagonal"], ["1/80"] * 3)


if __name__ == "__main__":
    unittest.main()
