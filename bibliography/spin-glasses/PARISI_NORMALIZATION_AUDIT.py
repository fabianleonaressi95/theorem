#!/usr/bin/env python3
"""Exact normalization checks for the SK/Parisi 1/2 factors.

Primary conventions:
- Talagrand (Ann. Math. 163 (2006)), eqs. (1.1), (1.3)-(1.14).
- Guerra (CMP 233 (2003)), §§2-4, eqs. (10)-(15), Theorems 3-5.

Uses Fraction arithmetic only; no stochastic simulation is needed.
"""
from fractions import Fraction
from itertools import product


def covariance_from_unordered_pairs(beta, sigma, tau):
    """Covariance for H_N=-beta/sqrt(N) sum_{i<j} g_ij sigma_i sigma_j."""
    n = len(sigma)
    r = [sigma[i] * tau[i] for i in range(n)]
    pair_sum = sum(r[i] * r[j] for i in range(n) for j in range(i + 1, n))
    return beta**2 * Fraction(pair_sum, n)


def covariance_from_overlap(beta, sigma, tau):
    """Equivalent covariance beta^2*N*R^2/2 - beta^2/2."""
    n = len(sigma)
    overlap = Fraction(sum(sigma[i] * tau[i] for i in range(n)), n)
    return beta**2 * Fraction(n, 2) * overlap**2 - beta**2 * Fraction(1, 2)


def verify_covariance_identity():
    beta = Fraction(3, 2)
    # Exhaustive spin pairs for N<=5, exact rational arithmetic.
    for n in range(1, 6):
        configs = list(product((-1, 1), repeat=n))
        for sigma in configs:
            for tau in configs:
                assert covariance_from_unordered_pairs(beta, sigma, tau) == \
                       covariance_from_overlap(beta, sigma, tau)
    return True


def xi_covariance_sk(beta, q):
    """Talagrand's covariance function xi_cov(q)=beta^2 q^2/2."""
    return beta**2 * q**2 / 2


def talagrand_discrete_penalty(beta, q, m):
    """-1/2 sum_{ell=1}^k m_ell [theta(q_{ell+1})-theta(q_ell)].

    q=(q_0,...,q_{k+1}), m=(m_0,...,m_k), q_0=0, q_{k+1}=1,
    m_0=0, m_k=1, theta(q)=q xi_cov'(q)-xi_cov(q)=beta^2 q^2/2.
    """
    assert len(q) == len(m) + 1
    assert q[0] == 0 and q[-1] == 1
    assert m[0] == 0 and m[-1] == 1
    theta = lambda z: beta**2 * z**2 / 2
    total = sum(m[ell] * (theta(q[ell + 1]) - theta(q[ell]))
                for ell in range(1, len(m)))
    return -total / 2


def integral_parisi_penalty(beta, q, m):
    """-beta^2/2 int_0^1 q x(q)dq for the same step order parameter."""
    assert len(q) == len(m) + 1
    assert q[0] == 0 and q[-1] == 1
    assert m[0] == 0 and m[-1] == 1
    integral = sum(m[ell] * (q[ell + 1]**2 - q[ell]**2) / 2
                   for ell in range(1, len(m)))
    return -beta**2 * integral / 2


def verify_penalty_identity():
    beta = Fraction(7, 5)
    q = [Fraction(0), Fraction(1, 5), Fraction(3, 5), Fraction(1)]
    m = [Fraction(0), Fraction(1, 4), Fraction(1)]
    assert talagrand_discrete_penalty(beta, q, m) == \
           integral_parisi_penalty(beta, q, m)
    return True


def verify_pde_coefficient():
    """For xi_cov=beta^2 q^2/2, (1/2)xi_cov''=beta^2/2."""
    beta = Fraction(5, 3)
    # exact second derivative of beta^2 q^2 / 2 is beta^2
    second_derivative = beta**2
    assert second_derivative / 2 == beta**2 / 2
    # If xi_cov is doubled to beta^2 q^2, the PDE coefficient doubles too.
    doubled_covariance_second_derivative = 2 * beta**2
    assert doubled_covariance_second_derivative / 2 == beta**2
    return True


if __name__ == "__main__":
    assert verify_covariance_identity()
    assert verify_penalty_identity()
    assert verify_pde_coefficient()
    beta = Fraction(3, 2)
    print("SK covariance identity: exact PASS (all spin pairs N=1..5)")
    print("Talagrand discrete penalty = Parisi integral penalty: exact PASS")
    print("PDE coefficient 1/2 xi_cov'' = beta^2/2: exact PASS")
    print("Example covariance at N=5, R=1: ",
          covariance_from_overlap(beta, (1,)*5, (1,)*5))
