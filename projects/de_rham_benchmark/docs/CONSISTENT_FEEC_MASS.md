# Consistent cubical FEEC mass control

## Purpose

The spectral-collapse experiment used diagonal dual-volume/DEC weights. This
control replaces only the inner products. The cubical mesh, oriented face
degrees of freedom, incidence matrices, domain map, ambient metric, and
quadrature are held fixed.

## Local finite-element complex

Use the lowest-order tensor-product cubical de Rham complex. On a reference
cell in dimension d, a local k-form basis is indexed by a k-face with varying
coordinate axes I and fixed endpoint choices on the remaining axes. Its only
nonzero coordinate component is the I-component, with scalar factor

`prod_{j not in I} l_{s_j}(xi_j)`, where `l_0(t)=1-t` and `l_1(t)=t`.
The coefficient form along I is the ordered wedge of `dx_i`, i in I.
These basis forms have unit integral on their associated oriented k-face.
They are the tensor-product cubical analogues of lowest-order Whitney forms
(Nedelec/RT family in the cubical setting), not simplicial Whitney forms.

The local consistent mass is

`M_K^k[a,b] = int_K <phi_a,phi_b>_{Lambda^k(g^{-1})} sqrt(det g) dxi`,

where g is the pullback metric returned by the same geometry object as the
DEC benchmark. In coordinates,

`<dx^I,dx^J> = det((g^{-1})_{I,J})`.

Local matrices are assembled through the exact same global k-face ids used
by the incidence matrices. No diagonalization or mass lumping is applied.

## Hodge operator

For full sparse mass matrices M_k, the Euclidean-symmetric energy matrix is

`B_k = D_{k-1} M_{k-1}^{-1} D_{k-1}^T M_k
       + D_k^T M_{k+1} D_k`,

and the generalized eigenproblem is `B_k x = lambda M_k x`.
The script forms dense solves only for moderate-size diagnostic meshes.
This is deliberately an audit/reference implementation, not a large-scale
solver.

## Reproduction

From this directory:

```bash
python compare_mass_matrices.py --dim 2 --N 8
python compare_mass_matrices.py --dim 3 --N 4
python compare_mass_matrices.py --dim 2 --N 8 --amplitude 0.05 --freq 1
python test_consistent_mass.py
```

The output reports mass positivity/conditioning, matrix symmetry, generalized
eigenpair residuals, Betti numbers, and the smallest positive eigenvalue for
both the existing diagonal DEC weights and the consistent cubical FEEC masses.

## Interpretation rules

- A different eigenvalue under the consistent mass is expected: this is a
  different discrete inner product, not a change to the incidence complex.
- If the (h^{2d}) collapse persists with consistent masses and stable
  reconstruction estimates, the diagonal-weight explanation is weakened.
- If it disappears, the diagonal mass is implicated, but this alone does not
  prove discrete compactness or Mosco convergence.
- A proper compactness claim still requires uniform reconstruction into a
  common Hilbert space, bounded-energy compactness, and control of the
  discrete co-closed subspaces.
- The present control first targets flat affine meshes. Curved-map tests are
  secondary and must preserve positive Jacobians and uniform metric bounds.

Boundary convention: all boundary degrees of freedom are retained, matching
the existing algebraic full-complex benchmark (no essential trace conditions).
