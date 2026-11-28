# T160 — Covariant-gradient Galerkin energy on the refined dodecahedron

**Classification:** numerical construction / candidate conforming Galerkin method.  
**Status:** the energy and mass are assembled from the same transported nodal basis, including the derivative of the parallel-transport factor. This repairs the specific omission identified in T159. It does not by itself prove spectral convergence.

## 1. Bundle and basis

Let (n:T\to S^2) be the fixed piecewise-smooth normal map inherited from T157/T158. On a refined triangle with vertices (v_0,v_1,v_2), let (lambda_i) be its barycentric coordinates. Choose an oriented orthonormal frame ((e_{1,i},e_{2,i})) in (T_{n(v_i)}S^2), and set (w_i=e_{1,i}+i e_{2,i}).

For (x\in T), let (R_{v_i x}\in SO(3)) be the minimal rotation taking (n(v_i)) to (n(x)). Define the transported nodal section
\[
\Phi_i(x)=\lambda_i(x)R_{v_i x}w_i\in T_{n(x)}S^2\otimes\mathbb C.
\]
The finite-element space is the span of these sections. This is a local bundle-valued P1 space; chart transitions are represented by the frame changes at vertices.

## 2. Covariant derivative and forms

The Levi-Civita connection on the unit sphere is the tangential projection of the ambient derivative. Thus
\[
\nabla^A_X\Phi_i=P_{n(x)}D_X\Phi_i,\qquad
P_n=I-nn^T.
\]
In particular,
\[
D_X\Phi_i=(X\lambda_i)R_{v_i x}w_i
+\lambda_i(D_XR_{v_i x})w_i.
\]
The second term is retained. It is the path-transport derivative omitted by the old T159 edge-Whitney surrogate.

Assemble
\[
M_{ij}=\int_T\langle\Phi_i,\Phi_j\rangle\,dA,\qquad
K_{ij}=\int_T\langle\nabla^A\Phi_i,\nabla^A\Phi_j\rangle\,dA,
\]
summing over all triangles. The discrete scalar spectrum is the generalized Hermitian problem
\[
K u=\lambda M u.
\]
This is a Bochner-energy Galerkin operator. It does not assert a flat covariant de Rham complex; in particular, nonzero curvature and (D_1^AD_0^A\ne0) remain allowed.

## 3. Numerical differentiation

The implementation represents each section in ambient \(\mathbb C^3\), differentiates the complete map \(\lambda_iR_{v_i x}w_i\) by centered differences in the two affine reference coordinates, then projects each derivative with (P_{n(x)}). This explicitly differentiates the minimal-rotation factor, rather than treating it as constant.

The quadrature uses a Duffy transform and tensor Gauss–Legendre nodes. The finite-difference step is recorded in the JSON report. A separate step-halving test is required before interpreting eigenvalue digits as converged with respect to differentiation.

## 4. What this establishes

The construction now uses a single trial basis for both mass and stiffness, and its stiffness is the Gram matrix of the covariant derivatives of that basis (up to the reported finite-difference and quadrature errors). Positivity of (M), nonnegativity of (K), Hermiticity, normal-map regularity, and mesh-refinement behavior are audited.

**It does not yet establish** a uniform interpolation estimate, density of the spaces in the form domain, a mesh-independent coercivity bound, a finite-difference consistency bound uniform in refinement, or convergence of the eigenvalues. Those are the hypotheses needed to invoke the conditional min–max theorem recorded in the convergence discussion. Nor does this construction derive the Q6 values (0,4,6) or the polynomial (f).

## 5. Reproduction

```bash
python scripts/audit_t160_covariant_gradient_energy.py
python -m unittest tests.test_t160_covariant_gradient_energy
```

The machine-readable report is written to `results/json/t160_covariant_gradient_energy.json`.
