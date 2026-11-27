import numpy as np

from scripts.rgs_airy_eigenstrain_map import (
    airy_to_eigenstrain,
    plane_strain_compliance,
    spectral_biharmonic,
    spectral_incompatibility,
)


def test_constitutive_map_reproduces_airy_stress():
    ny, nx = 48, 64
    dx, dy = 2.0 / nx, 3.0 / ny
    x = np.arange(nx) * dx
    y = np.arange(ny) * dy
    X, Y = np.meshgrid(x, y)
    phi = (np.sin(2*np.pi*X/2.0) * np.cos(4*np.pi*Y/3.0)
           + 0.17*np.cos(4*np.pi*X/2.0 + 2*np.pi*Y/3.0))
    result = airy_to_eigenstrain(phi, dx, dy, young_modulus=2.3, poisson_ratio=0.27)
    recovered = -plane_strain_compliance(result["stress"], 2.3, 0.27)
    np.testing.assert_allclose(result["eigenstrain"], recovered, rtol=0, atol=1e-14)
    np.testing.assert_allclose(result["eigenstrain"] + result["elastic_strain"], 0,
                               rtol=0, atol=1e-14)


def test_incompatibility_matches_airy_biharmonic_identity():
    ny, nx = 64, 80
    dx, dy = 2.0 / nx, 3.0 / ny
    x = np.arange(nx) * dx
    y = np.arange(ny) * dy
    X, Y = np.meshgrid(x, y)
    phi = (np.sin(2*np.pi*X/2.0) * np.cos(4*np.pi*Y/3.0)
           + 0.13*np.cos(6*np.pi*X/2.0 - 2*np.pi*Y/3.0))
    E, nu = 1.7, 0.22
    result = airy_to_eigenstrain(phi, dx, dy, E, nu)
    inc = spectral_incompatibility(result["eigenstrain"], dx, dy)
    expected = -((1.0 - nu**2) / E) * spectral_biharmonic(phi, dx, dy)
    np.testing.assert_allclose(inc, expected, rtol=2e-10, atol=2e-9)


def test_rejects_nonphysical_material_parameters():
    phi = np.zeros((8, 8))
    try:
        airy_to_eigenstrain(phi, 0.1, 0.1, 1.0, 0.5)
    except ValueError:
        pass
    else:
        raise AssertionError("nu=0.5 must be rejected for plane strain")
