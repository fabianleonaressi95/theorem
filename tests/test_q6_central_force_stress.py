"""Finite-difference checks for the Q6 central-force strain-energy identities."""
import numpy as np


def symmetric_basis(i, j, d):
    s = np.zeros((d, d))
    if i == j:
        s[i, i] = 1.0
    else:
        s[i, j] = s[j, i] = 0.5
    return s


def energy_and_stress(y, edges, u, kappa, eps):
    d = y.shape[1]
    total = 0.0
    stress = np.zeros((d, d))
    F = np.eye(d) + eps
    for e, (v, w) in enumerate(edges):
        r = y[w] - y[v]
        ell = np.linalg.norm(r)
        s = F @ r + u[w] - u[v]
        length = np.linalg.norm(s)
        delta = length - ell
        total += 0.5 * kappa[e] * delta**2
        nhat = s / length
        for i in range(d):
            for j in range(i, d):
                S = symmetric_basis(i, j, d)
                val = -kappa[e] * delta * (nhat @ S @ r)
                stress[i, j] += val
                stress[j, i] = stress[i, j]
    return total, stress


def rigidity_hessian(y, edges, kappa):
    n, d = y.shape
    R = np.zeros((len(edges), n * d))
    for e, (v, w) in enumerate(edges):
        r = y[w] - y[v]
        nhat = r / np.linalg.norm(r)
        R[e, v*d:(v+1)*d] = -nhat
        R[e, w*d:(w+1)*d] = nhat
    return R.T @ np.diag(kappa) @ R


def linear_stress_coefficients(y, edges, kappa):
    n, d = y.shape
    c = np.zeros((d, d, n*d))
    for e, (v, w) in enumerate(edges):
        r = y[w] - y[v]
        ell = np.linalg.norm(r)
        nhat = r / ell
        for i in range(d):
            for j in range(d):
                c[i, j, v*d:(v+1)*d] += kappa[e] * ell * nhat[i] * nhat[j] * nhat
                c[i, j, w*d:(w+1)*d] -= kappa[e] * ell * nhat[i] * nhat[j] * nhat
    return c


def test_energy_strain_derivative_matches_exact_stress():
    rng = np.random.default_rng(731)
    y = np.array([[0., 0., 0.], [1.1, .1, 0.], [.2, 1.0, .1], [.1, .2, 1.2]])
    edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    u = rng.normal(scale=2e-3, size=y.shape)
    kappa = np.linspace(1.0, 2.0, len(edges))
    eps = np.zeros((3, 3))
    _, stress = energy_and_stress(y, edges, u, kappa, eps)
    h = 1e-6
    for i in range(3):
        for j in range(i, 3):
            S = symmetric_basis(i, j, 3)
            hp, _ = energy_and_stress(y, edges, u, kappa, h*S)
            hm, _ = energy_and_stress(y, edges, u, kappa, -h*S)
            deriv = (hp - hm) / (2*h)
            assert np.isclose(deriv, -stress[i, j], rtol=2e-6, atol=2e-9)


def test_rigidity_hessian_is_symmetric_positive_semidefinite():
    y = np.array([[0., 0., 0.], [1.1, .1, 0.], [.2, 1.0, .1], [.1, .2, 1.2]])
    edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    K = rigidity_hessian(y, edges, np.ones(len(edges)))
    assert np.allclose(K, K.T, atol=1e-13)
    assert np.linalg.eigvalsh(K).min() > -1e-12


def test_linear_stress_is_first_derivative_of_exact_stress():
    rng = np.random.default_rng(732)
    y = np.array([[0., 0., 0.], [1.1, .1, 0.], [.2, 1.0, .1], [.1, .2, 1.2]])
    edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    kappa = np.linspace(1.0, 2.0, len(edges))
    u = rng.normal(scale=1e-7, size=y.shape)
    _, sigma = energy_and_stress(y, edges, u, kappa, np.zeros((3, 3)))
    c = linear_stress_coefficients(y, edges, kappa)
    pred = np.einsum("ijk,k->ij", c, u.reshape(-1))
    assert np.allclose(sigma, pred, rtol=2e-5, atol=2e-10)


def hessian_at_strain(y, edges, kappa, eps):
    n, d = y.shape
    K = np.zeros((n*d, n*d))
    F = np.eye(d) + eps
    for e, (v, w) in enumerate(edges):
        r = y[w] - y[v]
        ell = np.linalg.norm(r)
        rr = F @ r
        ell_eps = np.linalg.norm(rr)
        nhat = rr / ell_eps
        prestress = (ell_eps - ell) / ell_eps
        block = kappa[e] * (np.outer(nhat, nhat) +
                            prestress * (np.eye(d) - np.outer(nhat, nhat)))
        ids = np.r_[np.arange(v*d, (v+1)*d), np.arange(w*d, (w+1)*d)]
        incidence = np.concatenate((-np.eye(d), np.eye(d)), axis=1)
        K[np.ix_(ids, ids)] += incidence.T @ block @ incidence
    return K


def analytic_hessian_strain_derivative(y, edges, kappa, i, j):
    n, d = y.shape
    A = np.zeros((n*d, n*d))
    S = symmetric_basis(i, j, d)
    for e, (v, w) in enumerate(edges):
        r = y[w] - y[v]
        ell = np.linalg.norm(r)
        nhat = r / ell
        q = nhat @ S @ nhat
        m = (np.eye(d) - np.outer(nhat, nhat)) @ S @ nhat
        block = kappa[e] * (np.outer(m, nhat) + np.outer(nhat, m) +
                            q * (np.eye(d) - np.outer(nhat, nhat)))
        ids = np.r_[np.arange(v*d, (v+1)*d), np.arange(w*d, (w+1)*d)]
        incidence = np.r_[-np.eye(d), np.eye(d)]
        A[np.ix_(ids, ids)] += incidence.T @ block @ incidence
    return A


def test_strain_derivative_of_full_hessian_matches_formula():
    y = np.array([[0., 0., 0.], [1.1, .1, 0.], [.2, 1.0, .1], [.1, .2, 1.2]])
    edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    kappa = np.linspace(1.0, 2.0, len(edges))
    h = 1e-6
    for i in range(3):
        for j in range(i, 3):
            S = symmetric_basis(i, j, 3)
            fd = (hessian_at_strain(y, edges, kappa, h*S) -
                  hessian_at_strain(y, edges, kappa, -h*S)) / (2*h)
            exact = analytic_hessian_strain_derivative(y, edges, kappa, i, j)
            assert np.allclose(fd, exact, rtol=2e-6, atol=2e-9)
