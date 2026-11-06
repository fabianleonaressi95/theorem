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

## Top-degree normalization audit

The archived geometry code assigns `M_d(K)=vol_g(K)`. For a top-degree
cochain whose degree of freedom is the integral of a d-form over K, the
standard primal DEC Hodge weight is `1/vol_g(K)`: the dual cell is a point
with unit 0-volume, and the primal d-volume appears in the denominator.
The consistent FEEC top-form basis gives the same scaling on affine cells
(and integrates `1/sqrt(det g)` on a curved reference cell).

This matters one degree lower as well: `M_d` enters the coexact energy
`D_{d-1}^T M_d D_{d-1}` in the `k=d-1` Hodge Laplacian. Therefore the
historical `M_d=vol_g(K)` convention is retained as a reproducibility
control, but it must not be labelled the standard DEC inner product for
integral top-cochains. The comparison script also constructs a corrected
diagonal DEC family with `M_d=1/vol_g(K)`, leaving lower-degree weights
unchanged. On flat affine cubical meshes, this corrected diagonal family is
exactly the row-sum lumping of the assembled tensor-product FEEC mass matrix
in every degree; CI checks this identity in 2D and 3D. The reported legacy
partition-of-unity identity between `sum(M_0)` and `sum(M_d)` is not a
Hodge-star consistency condition.

## Consistent mass

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
python mass_refinement_study.py --dim 2 --levels 4,8,16
python mass_refinement_study.py --dim 3 --levels 2,3,4,5
python mass_refinement_study.py --dim 2 --levels 4,8,16 --amplitude 0.05
python mass_refinement_study.py --dim 3 --levels 2,3,4 --amplitude 0.05
python test_consistent_mass.py
```

The output reports mass positivity/conditioning, matrix symmetry, generalized
eigenpair residuals, Betti numbers, and the smallest positive eigenvalue for
both the existing diagonal DEC weights and the consistent cubical FEEC masses.

## Interpretation rules

- First compare the historical and top-corrected DEC variants. A large
  difference in degree d-1 directly measures sensitivity to the legacy
  top-degree normalization.
- Then compare top-corrected DEC with consistent FEEC. This isolates the
  remaining effect of diagonalization/lumping and the local tensor-product
  Gram structure.
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
