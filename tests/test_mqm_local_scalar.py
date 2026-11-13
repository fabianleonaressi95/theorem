import unittest
import numpy as np
from models.mqm_local_scalar import (
    incidence_matrix, metric_weights, scalar_action, scalar_gradient,
    scalar_hessian, uniform_restriction,
)

class TestMQMLocalScalar(unittest.TestCase):
    def setUp(self):
        self.edges=[(i,(i+1)%8,0) for i in range(8)]
        self.B=incidence_matrix(self.edges,8)
        self.w=metric_weights(np.linspace(0.8,1.4,8))
        self.phi=np.linspace(-0.4,0.7,8)

    def test_metric_weights_positive_and_rms_normalized(self):
        self.assertTrue(np.all(self.w>0))
        lengths=np.linspace(0.8,1.4,8)
        self.assertAlmostEqual(float(np.mean((self.w*lengths)**2)),float(np.mean(lengths**2)))

    def test_constant_field_has_zero_edge_kinetic_energy(self):
        q=0.37
        np.testing.assert_allclose(self.B.T@(q*np.ones(8)),0.0,atol=1e-14)

    def test_gradient_matches_centered_finite_difference(self):
        eps=1e-6
        analytic=scalar_gradient(self.phi,self.B,self.w,lam=0.7,phi_v=0.9)
        numeric=np.zeros(8)
        for i in range(8):
            d=np.zeros(8); d[i]=eps
            numeric[i]=(scalar_action(self.phi+d,self.B,self.w,lam=0.7,phi_v=0.9)
                        -scalar_action(self.phi-d,self.B,self.w,lam=0.7,phi_v=0.9))/(2*eps)
        np.testing.assert_allclose(analytic,numeric,atol=2e-8,rtol=2e-8)

    def test_hessian_matches_gradient_difference(self):
        eps=1e-6
        H=scalar_hessian(self.phi,self.B,self.w,lam=0.7,phi_v=0.9)
        numeric=np.column_stack([
            (scalar_gradient(self.phi+eps*np.eye(8)[i],self.B,self.w,lam=0.7,phi_v=0.9)
             -scalar_gradient(self.phi-eps*np.eye(8)[i],self.B,self.w,lam=0.7,phi_v=0.9))/(2*eps)
            for i in range(8)])
        np.testing.assert_allclose(H,numeric,atol=2e-8,rtol=2e-8)

    def test_hessian_is_symmetric(self):
        H=scalar_hessian(self.phi,self.B,self.w)
        np.testing.assert_allclose(H,H.T,atol=1e-14)

    def test_uniform_restriction_removes_metric_kinetic_term(self):
        q=0.42; lam=0.8; v=1.1; V0=0.2
        S=uniform_restriction(q,self.B,self.w,lam=lam,phi_v=v,V0=V0)
        self.assertAlmostEqual(S,V0+0.25*lam*(q*q-v*v)**2,places=13)

    def test_bad_edge_lengths_rejected(self):
        with self.assertRaises(ValueError):
            metric_weights([1.0,0.0])

if __name__=="__main__":
    unittest.main()
