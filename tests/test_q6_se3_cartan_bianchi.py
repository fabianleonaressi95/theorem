import unittest

from scripts.audit_q6_se3_cartan_bianchi import (
    IDENTITY, build_report, build_se3_links, cube_bianchi, q6_cubes,
    se3_distance, se3_mul
)
from scripts.audit_q6_discrete_cartan import reconstruct_seed, spatial_coframes


class Q6SE3CartanBianchiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        X, edges = reconstruct_seed()
        E = spatial_coframes(X)
        cls.data = build_se3_links(X, edges, E)

    def test_exact_reverse_link_inverse(self):
        for (g, h), link in self.data["links"].items():
            reverse = self.data["links"][(h, g)]
            dr, dt = se3_distance(se3_mul(reverse, link), IDENTITY)
            self.assertLess(dr, 1e-12)
            self.assertLess(dt, 1e-12)

    def test_affine_faces_reproduce_existing_cartan_observables(self):
        r = build_report()["affine_link"]
        self.assertLess(r["max_rotation_difference_from_previous_face_holonomy"], 1e-10)
        self.assertLess(r["max_closure_difference_from_previous_developed_torsion"], 1e-10)

    def test_all_160_cubical_bianchi_identities(self):
        self.assertEqual(len(q6_cubes()), 160)
        for base, axes in self.data["cubes"]:
            dr, dt = se3_distance(
                cube_bianchi(self.data["links"], base, axes), IDENTITY
            )
            self.assertLess(dr, 1e-10)
            self.assertLess(dt, 1e-10)

    def test_full_affine_gauge_covariance(self):
        r = build_report()["full_SE3_gauge_covariance"]
        self.assertLess(r["face_holonomy_conjugation_rotation_max"], 1e-10)
        self.assertLess(r["face_holonomy_conjugation_translation_max"], 1e-10)
        self.assertLess(r["cube_bianchi_rotation_max"], 1e-10)
        self.assertLess(r["cube_bianchi_translation_max"], 1e-10)


if __name__ == "__main__":
    unittest.main()
