# Bernoulli–RGS geometric quadrature and weighted Hodge theory

**Status:** foundational identities proved; Q6/RGS cell realization and convergence theorem remain open.  
**Scope:** this record consolidates the Bernoulli, barycentric-moment, anisotropy, and weighted-Hodge framework developed alongside PR #139. It does not claim that the proposed Bernoulli mass matrices have already been constructed for the Q6 orbit complex or the 188-dimensional RGS tangent space.

## 1. Mathematical architecture

The proposed chain is

\[
\text{cell geometry}
\longrightarrow \text{moments and cumulants}
\longrightarrow \text{Bernoulli corrections}
\longrightarrow \text{weighted cochain inner products}
\longrightarrow \text{Hodge spectra}.
\]

The incidence operators encode topology. Positive-definite mass matrices encode metric and measure. Keeping these roles separate is essential: changing a mass matrix may change eigenvalues and harmonic representatives, but it does not change the cochain identity \(D_{k+1}D_k=0\).

## 2. Midpoint Euler–Maclaurin formula

Let \(h=1/n\), and let \(f\) be sufficiently smooth on \([0,1]\). The composite midpoint rule satisfies

\[
h\sum_{j=0}^{n-1}f((j+\tfrac12)h)
=
\int_0^1 f(x)\,dx
+
\sum_{r=1}^{p}
\frac{B_{2r}(1/2)}{(2r)!}h^{2r}
\left[f^{(2r-1)}(1)-f^{(2r-1)}(0)\right]
+R_p.
\]

Here the Bernoulli polynomials are defined by

\[
\frac{te^{xt}}{e^t-1}
=
\sum_{m\geq0}B_m(x)\frac{t^m}{m!},
\qquad
B_{2r}(1/2)=(2^{1-2r}-1)B_{2r}.
\]

In particular, \(B_2(1/2)=-1/12\) and \(B_4(1/2)=7/240\). The first correction is therefore
\(-h^2[f'(1)-f'(0)]/24\). For \(f(x)=x^2\), this gives the exact midpoint error \(-h^2/12\).

In six dimensions, the tensor-product midpoint rule is the product of the six one-dimensional rules. Its expansion contains single-coordinate boundary terms and mixed products of boundary operators. This is a product-domain statement; it is not automatically a formula for an arbitrary Q6 cell complex.

## 3. Exact moment-generating function for a parallelepiped

Let a centred parallelepiped be parametrized by

\[
x=c+A\xi,\qquad \xi\in[-\tfrac12,\tfrac12]^d,
\]

where the columns of \(A\) are its edge vectors. For normalized uniform measure on the cell, define

\[
M_F(t)=\mathbb E[e^{t\cdot(x-c)}].
\]

A change of variables and factorization of the cube give the exact identity

\[
M_F(t)=
\prod_{i=1}^{d}
\frac{\sinh((A^Tt)_i/2)}{(A^Tt)_i/2}.
\]

Using the Bernoulli generating function,

\[
\log\!\left(\frac{\sinh(z/2)}{z/2}\right)
=
\sum_{r\geq1}
\frac{B_{2r}}{2r(2r)!}z^{2r},
\]

we obtain

\[
\boxed{
\log M_F(t)=
\sum_{r\geq1}
\frac{B_{2r}}{2r(2r)!}
\sum_{i=1}^{d}((A^Tt)_i)^{2r}.
}
\]

Thus the Bernoulli numbers are the cumulant coefficients of the uniform measure on a centred parallelepiped. This is an exact analytic identity, not merely a formal analogy.

The covariance is

\[
\Sigma_F=\frac1{12}AA^T.
\]

For a smooth function, write \(D_i=a_i\cdot\nabla\), where \(a_i\) is the \(i\)-th column of \(A\). The cell average has the differential-operator expansion

\[
\mathbb E[f(c+A\xi)]
=
\left[
1+\frac1{24}\sum_iD_i^2
-\frac1{2880}\sum_iD_i^4
+\frac1{1152}\left(\sum_iD_i^2\right)^2
+O(\nabla^6)
\right]f(c).
\]

**Coefficient correction:** the fourth-order expression is the combination
\(-\frac1{2880}\sum_iD_i^4+\frac1{1152}(\sum_iD_i^2)^2\). Writing instead a positive \(\frac1{1920}\sum_iD_i^4\) *in addition to* the square term double-counts the pure fourth-order contribution. The formula above follows by exponentiating the cumulant series.

For a cube of side \(h\), \(A=hI\), so \(\Sigma_F=h^2I/12\) and the second-order cell-average correction is \(h^2\Delta f(c)/24\).

The one-dimensional centred moments are

\[
\mathbb E[\xi^{2k}]=\frac{1}{(2k+1)2^{2k}},
\qquad
\mathbb E[\xi^{2k+1}]=0,
\]

with recurrence

\[
\mu_{2k}=\frac{2k-1}{4(2k+1)}\mu_{2k-2},
\qquad \mu_0=1.
\]

For a general polytope the factorization above is unavailable; its moments must be computed from the actual cell geometry.

## 4. Anisotropic tangent correction

Let \(T\subset\mathbb R^d\) be a tangent subspace and \(P_T\) its orthogonal projector. The projected covariance is

\[
\Sigma_T=P_T\Sigma_FP_T\big|_T.
\]

It is positive semidefinite; it is positive definite on \(T\) only if the cell has nonzero variance in every tangent direction. If \(u_j\) is an orthonormal eigenbasis of \(\Sigma_T\), with eigenvalues \(\sigma_j^2\), then

\[
\mathcal C_Tf
=
\frac12\Sigma_T:D_T^2f
=
\frac12\sum_j\sigma_j^2D_T^2f(u_j,u_j).
\]

This gives a geometric anisotropy tensor without inserting arbitrary directional weights. It is a local cell-average correction. Its identification with a particular RGS 188D tangent operator requires the actual cell-to-tangent maps and has not yet been established.

## 5. Weighted finite cochain complexes

Consider a finite cochain complex

\[
C^0\xrightarrow{D_0}C^1\xrightarrow{D_1}C^2\longrightarrow\cdots,
\qquad D_{k+1}D_k=0.
\]

Choose symmetric positive-definite mass matrices \(W_k\) on \(C^k\), defining
\(\langle u,v\rangle_{W_k}=u^TW_kv\). The metric adjoint of \(D_{k-1}\) is

\[
\delta_k=W_{k-1}^{-1}D_{k-1}^TW_k.
\]

The degree-\(k\) Hodge Laplacian is

\[
\Delta_k=D_{k-1}\delta_k+\delta_{k+1}D_k.
\]

For every \(v\in C^k\),

\[
\langle v,\Delta_kv\rangle_{W_k}
=
\|D_{k-1}^Tv\|_{W_{k-1}^{-1}}^2
+
\|D_kv\|_{W_{k+1}}^2
\geq0.
\]

Consequently,

\[
\ker\Delta_k=\ker D_k\cap\ker D_{k-1}^T,
\]

and the finite-dimensional Hodge theorem identifies \(\ker\Delta_k\) with the cohomology of the underlying complex. Its dimension is the Betti number \(\beta_k\).

**Theorem B3 (weighted Hodge compatibility).** For any finite cochain complex and any symmetric positive-definite family \(W_k\), the weighted adjoints and Laplacians above are well-defined and positive semidefinite; the harmonic-space dimension equals the cohomological Betti number. Replacing \(W_k\) by another positive-definite family leaves \(D_{k+1}D_k=0\) and the Betti numbers unchanged, although it may change the spectrum and harmonic representatives.

This theorem is abstract and exact. It does not by itself construct Bernoulli-corrected matrices \(W_k(h)\) for a particular cell complex.

## 6. Bernoulli-corrected mass matrices: construction still required

A candidate expansion is

\[
W_k(h)=W_k^{(0)}+\sum_{r=1}^{p}h^{2r}C_{k,2r},
\]

where each \(C_{k,2r}\) must be derived from cell moments, basis functions, and any boundary quadrature terms appropriate to degree \(k\). The coefficients cannot be assigned by multiplying a mass matrix by a Bernoulli number alone.

Required checks are:

1. symmetry of every assembled \(W_k(h)\);
2. uniform positive definiteness (or a quantified range of \(h\));
3. consistency with the chosen finite-element or cochain basis;
4. compatibility with pullbacks and the discrete differential;
5. invariance under the desired group action, when claimed.

If \(J_k(g)\) is the cochain representation of \(g\), metric invariance is

\[
J_k(g)^TW_k(h)J_k(g)=W_k(h).
\]

When this holds and the differentials are equivariant, the weighted Hodge Laplacian commutes with the group action and its eigenspaces can be decomposed into irreducible representations.

## 7. Relation to Q6, M3, RGS and Liouville–Bergman

- **Q6/M3:** the incidence matrices and signed group actions supply the finite cochain data. The existing orbit-edge calculation in PR #139 remains separate from the proposed quadrature correction.
- **D4:** symmetry constrains admissible moment and mass matrices. A representation decomposition of the orbit-edge Hodge eigenspaces is still a separate pending computation.
- **RGS tangent sector:** the projected covariance supplies a candidate geometric anisotropy tensor. A numerical or exact identification with the stored 188D tangent matrices has not been made here.
- **Liouville–Bergman:** orthogonal transformations of the five-dimensional phase-space coordinates preserve the already-established invariant expressions under the stated action. A new Bernoulli-corrected density does not automatically inherit this property; its Jacobian and transformation law must be derived.
- **Bernoulli/zeta:** the classical identity \(\zeta(1-2n)=-B_{2n}/(2n)\) links Bernoulli numbers to zeta values. A connection to the spectral zeta function of a corrected Q6/RGS Laplacian requires its spectrum and analytic continuation and is not asserted here.

## 8. Open theorem B4: convergence to a continuum operator

The desired result is a convergence theorem for the discrete energy forms, for example Mosco convergence of appropriately embedded forms. A proof needs, at minimum:

- a specified sequence of meshes/cell complexes and continuum domain;
- discrete-to-continuum maps and a consistent identification of cochain spaces;
- uniform coercivity and boundedness of the corrected mass matrices;
- a liminf inequality for weakly convergent sequences;
- a recovery sequence for each continuum form-domain element;
- compactness assumptions if convergence of individual eigenvalues is claimed.

For FEEC applications, commuting projections and discrete compactness must also be verified. None of these hypotheses follows solely from the midpoint Euler–Maclaurin formula.

## 9. Status ledger

| Result | Status |
|---|---|
| Midpoint Euler–Maclaurin coefficients | Classical exact identity |
| Parallelepiped moment-generating function | Exact |
| Bernoulli cumulant expansion | Exact |
| Affine covariance and tangent projection | Exact; strict positivity requires a rank condition |
| Weighted finite Hodge compatibility (B3) | Proved under SPD mass matrices |
| Bernoulli mass matrices for Q6/M3 cells | Not constructed |
| D4-equivariant corrected Hodge spectrum | Open |
| Identification with RGS 188D tangent operators | Open |
| Mosco/FEEC convergence (B4) | Open |
| Bernoulli-corrected Liouville–Bergman density | Open |

## 10. Reproducibility and repository relation

This is a theorem and research-program record, not a numerical audit. It introduces no computed eigenvalues and does not change the verification status of the existing M3/Q6 results. It should be reviewed alongside:

- docs/M3_D4_ORBIT_EDGE_HODGE_VERIFICATION.md
- docs/Q6_D5_D4_LIOUVILLE_BRIDGE.md
- theorems/M3-minkowski-q6-d4-cell-orbit-closure.md

The next computational deliverable should construct cell moment tensors from explicit Q6/M3 cell coordinates, assemble the corresponding mass matrices, and test symmetry and positivity before attempting spectral perturbation.
