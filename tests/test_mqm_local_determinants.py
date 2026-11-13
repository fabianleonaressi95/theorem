import unittest
import numpy as np
from models.mqm_local_determinants import LocalDeterminantCoupling
from models.mqm_local_scalar import incidence_matrix,metric_weights

class TestLocalDeterminantCoupling(unittest.TestCase):
    def setUp(self):
        self.n=4; self.spin=2
        rng=np.random.default_rng(31)
        A=rng.normal(size=(self.n*self.spin,self.n*self.spin))
        self.Dkin=0.12*(A-A.T).astype(complex)
        C=rng.normal(size=(2*self.n,2*self.n))
        self.KB0=C.T@C+2*np.eye(2*self.n)
        self.tau=np.array([0.7,1.0,0.8,1.2])
        self.model=LocalDeterminantCoupling(self.Dkin,self.KB0,self.tau,self.spin)
        self.phi=np.array([0.13,-0.08,0.21,0.04])

    def test_fermion_and_boson_domains(self):
        self.assertEqual(self.model.fermion_matrix(self.phi).shape,(8,8))
        K=self.model.boson_matrix(self.phi)
        self.assertGreater(np.linalg.eigvalsh(K)[0],0)

    def test_gradient_matches_centered_finite_difference(self):
        eps=2e-6
        _,g,_=self.model.determinant_gradient_hessian(self.phi)
        fd=np.zeros(self.n)
        for i in range(self.n):
            d=np.eye(self.n)[i]*eps
            fd[i]=(self.model.effective_action(self.phi+d)-self.model.effective_action(self.phi-d))/(2*eps)
        np.testing.assert_allclose(g,fd,atol=2e-8,rtol=2e-8)

    def test_full_hessian_matches_gradient_finite_difference(self):
        eps=2e-6
        _,_,H=self.model.determinant_gradient_hessian(self.phi)
        fd=np.column_stack([
            (self.model.determinant_gradient_hessian(self.phi+eps*np.eye(self.n)[i])[1]
             -self.model.determinant_gradient_hessian(self.phi-eps*np.eye(self.n)[i])[1])/(2*eps)
            for i in range(self.n)])
        np.testing.assert_allclose(H,fd,atol=2e-7,rtol=2e-7)

    def test_hessian_is_symmetric(self):
        _,_,H=self.model.determinant_gradient_hessian(self.phi)
        np.testing.assert_allclose(H,H.T,atol=2e-12)

    def test_local_couplings_reduce_to_collective_parameter(self):
        q=0.17
        local=self.model.effective_action(np.full(self.n,q))
        D=self.model.fermion_matrix(np.full(self.n,q))
        K=self.model.boson_matrix(np.full(self.n,q))
        sign,ld=np.linalg.slogdet(D)
        expected=-ld+0.5*np.linalg.slogdet(K)[1]
        self.assertAlmostEqual(local,float(expected),places=12)

    def test_invalid_domains_are_rejected(self):
        singular=LocalDeterminantCoupling(np.zeros((8,8)),self.KB0,self.tau,self.spin)
        with self.assertRaises(ValueError):
            singular.effective_action(np.zeros(self.n))
        bad=LocalDeterminantCoupling(self.Dkin,-10*np.eye(8),self.tau,self.spin)
        with self.assertRaises(ValueError):
            bad.effective_action(np.zeros(self.n))

    def test_combined_scalar_determinant_gradient_hessian(self):
        edges=[(i,(i+1)%self.n,0) for i in range(self.n)]
        B=incidence_matrix(edges,self.n); w=metric_weights([1.0,1.2,0.9,1.1])
        g,H=self.model.local_scalar_gradient_hessian(self.phi,B,w,lam=0.3)
        eps=2e-6
        fd=np.zeros(self.n)
        for i in range(self.n):
            d=np.eye(self.n)[i]*eps
            fd[i]=(self.model.local_scalar_effective_action(self.phi+d,B,w,lam=0.3)
                   -self.model.local_scalar_effective_action(self.phi-d,B,w,lam=0.3))/(2*eps)
        np.testing.assert_allclose(g,fd,atol=3e-8,rtol=3e-8)
        self.assertEqual(H.shape,(self.n,self.n))

if __name__=="__main__": unittest.main()
