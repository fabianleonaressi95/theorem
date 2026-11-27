# T158 — Interior pullback Levi-Civita connection and path-transported Whitney masses

**Date:** 27 November 2026  
**Classification:** explicit piecewise-smooth normal map; pullback Levi-Civita connection; numerical path-transported Whitney mass/Hodge audit.  
**Status:** T157's endpoint-link model is upgraded by specifying the connection inside every triangle. The interior mass matrices are integrated along the connection's path transports; order-8/order-12 quadrature agrees to approximately (10^{-14}). The construction remains a finite-mesh model, not a mesh-refinement convergence theorem.

## 1. Interior normal map

T157 supplies a unit normal (n_v\in S^2) at each of the 32 nodes. On an oriented triangle (T=(i,j,k)), with barycentric coordinates ((\lambda_i,\lambda_j,\lambda_k)), define
\[
\boxed{
n_T(\lambda)=
\frac{\lambda_i n_i+\lambda_j n_j+\lambda_k n_k}
{\|\lambda_i n_i+\lambda_j n_j+\lambda_k n_k\|}.
}
\]
This is a piecewise-smooth map from the centroid-fan surface to the unit sphere whenever the denominator is nonzero. The audit checks that it stays uniformly away from zero over all quadrature points. The minimum sampled denominator is 0.91215925 for the supergolden geometry and 0.92336297 for the regular control.

The connection inside (T) is the pullback
\[
\nabla^T=n_T^*\nabla^{S^2}
\]
of the unit-sphere Levi-Civita connection. Along a mesh edge, the normal interpolation is the normalized linear interpolation of its endpoint normals, which traces the minor great-circle arc. Consequently, its endpoint parallel transport is exactly the T157 link (U_{ij}), not a newly fitted phase.

## 2. Interior path transport and local gauges

Choose the first vertex (i) of each oriented triangle as its base fibre. Let (R(a,b)\in SO(3)) denote the minimal rotation taking unit vector (a) to (b). For a quadrature point (x\in T), write (n_x=n_T(\lambda(x))). The path from a vertex (v\in\{i,j,k\}) to (x), then from (x) to the base vertex (i), gives
\[
\boxed{
Q_{v,T}(x)=
F_i^T R(n_x,n_i)R(n_v,n_x)F_v\in SO(2).
}
\]
This is a path-dependent local trivialization. The dependence on (x) is essential: in nonzero curvature, transport from (v) to (i) through (x) is not generally the same as the direct endpoint link (U_{vi}).

The transported scalar basis is
\[
\widetilde\lambda_{v,T}(x)=Q_{v,T}(x)\lambda_v(x),
\]
and for an oriented edge (e=(a,b)), whose cochain value is stored in the fibre at (b), the transported Whitney 1-form basis is
\[
\widetilde w_{e,T}(x)=Q_{b,T}(x)
\bigl(\lambda_a\,d\lambda_b-\lambda_b\,d\lambda_a\bigr).
\]
The matrices are assembled by integrating their pointwise Hermitian products:
\[
(M_0^A|_T)_{ab}
=\int_T\overline{Q_{a,T}(x)}Q_{b,T}(x)
\lambda_a(x)\lambda_b(x)\,dA,
\]
\[
(M_1^A|_T)_{ef}
=\int_T\overline{Q_{b(e),T}(x)}Q_{b(f),T}(x)
\langle w_{e,T}(x),w_{f,T}(x)\rangle\,dA.
\]
The normalized Whitney 2-form has unit integral and constant squared norm (1/|T|^2), so
\[
(M_2^A)_{TT}=1/|T|.
\]

The integrals use a Duffy transformation of the reference triangle and tensor Gauss–Legendre quadrature. This is a genuine interior path-transported mass construction for the specified normal map, rather than the endpoint-only transport approximation used in T157.

## 3. Curvature-aware differential

The edge and face differences remain those of T157:
\[
(D_0^A u)_{ij}=u_j-U_{ij}u_i,
\qquad
(D_1^A c)_{ijk}=U_{ji}c_{ij}+U_{ki}c_{jk}+c_{ki}.
\]
Their composition is the exact curvature identity
\[
(D_1^A D_0^A u)_{ijk}
=(1-H_{ijk})U_{ji}u_j,
\qquad H_{ijk}=U_{ij}U_{jk}U_{ki}.
\]
It is nonzero in both geometries. This is a curved covariant sequence, not a cochain complex; the construction never imposes (D_1^AD_0^A=0).

The mass adjoints define the degree-0, degree-1 and degree-2 Hodge operators exactly as in T157, with the T158 interior masses substituted for the endpoint-transport masses.

## 4. Numerical certificates

The full 32–90–60 audit runs at (t=\psi_{\rm sg}=1.465571231876768) and at the regular (t=\varphi) control.

| Certificate | Supergolden | Regular \(\varphi\) |
|---|---:|---:|
| Cells | (32, 90, 60) | (32, 90, 60) |
| Minimum normal-interpolation denominator | 0.91215925 | 0.92336297 |
| Minimum base-normal dot interpolant | 0.77024636 | 0.79988148 |
| Order-8 vs order-12 relative residual, (M_0) | (4.26\times10^{-15}) | (1.70\times10^{-15}) |
| Order-8 vs order-12 relative residual, (M_1) | (3.15\times10^{-14}) | (1.83\times10^{-14}) |
| T155 face-link compatibility residual | (2.22\times10^{-16}) | (2.22\times10^{-16}) |
| Antipodal link covariance residual | (4.71\times10^{-16}) | (5.55\times10^{-16}) |
| Curvature identity residual | (2.33\times10^{-15}) | (2.43\times10^{-15}) |
| Holonomy sum | 12.56637061435917 | 12.56637061435917 |
| Gauss–Bonnet residual from (4\pi) | (1.78\times10^{-15}) | 0 |

All three mass matrices are positive definite. Their minimum eigenvalues are:

| Mass | Supergolden | Regular \(\varphi\) |
|---|---:|---:|
| (M_0^A) | 0.04256375 | 0.22939939 |
| (M_1^A) | 0.32165059 | 0.32061136 |
| (M_2^A) | 10.61778063 | 2.10292445 |

The interior path transports change the mass matrices measurably relative to T157's endpoint-only construction:

| Relative Frobenius difference | Supergolden | Regular \(\varphi\) |
|---|---:|---:|
| (M_0^A), endpoint vs interior | 0.00470661 | 0.00457708 |
| (M_1^A), endpoint vs interior | 0.02107543 | 0.02044435 |

The gauge-covariance residual is (8.98\times10^{-15}) in the supergolden run and (2.78\times10^{-15}) in the regular control. The Hodge matrices are Hermitian to below (10^{-12}).

### Lowest generalized Hodge eigenvalues

| Degree | Supergolden | Regular \(\varphi\) |
|---|---|---|
| 0 | (2.28896737^{(3)},\ 13.02288603^{(3)},\ 13.31861278,\ldots) | (0.42382159^{(3)},\ 2.43554458^{(5)},\ 5.98544673^{(3)},\ldots) |
| 1 | (0,\ 4.70679548^{(3)},\ 10.16850088^{(3)},\ldots) | (0,\ 0.87335588^{(3)},\ 1.91972274^{(5)},\ldots) |
| 2 | (2.50513803^{(3)},\ 12.19240624,\ 12.21303555,\ldots) | (0.46437609^{(3)},\ 2.28405594^{(5)},\ 4.85785274^{(3)},\ldots) |

The degree-one zero eigenvalue is a kernel of the curved Hodge operator, not a cohomology class of a flat complex. No spectral rescaling or edge fitting is used to force the Q6 values (0,4,6).

## 5. Status and remaining proof obligations

**Constructed and numerically verified**
- A nondegenerate piecewise-smooth normal map on every triangle.
- The pullback sphere Levi-Civita connection inside every triangle.
- Interior path transports whose edge restriction agrees with T157 and T155.
- Path-transported Whitney (M_0^A,M_1^A,M_2^A) masses, with quadrature convergence at the reported orders.
- Gauge covariance, antipodal link covariance, spherical holonomy, curvature defect, positive masses and generalized spectra.

**Still open**
1. Prove a uniqueness/optimality principle for the area-weighted nodal normals inherited from T157.
2. Establish mesh-refinement convergence and a curved-connection FEEC error estimate.
3. Compare alternative interior paths/gauges at fixed curvature and prove the expected gauge-equivalent spectra.
4. Derive a mathematically justified map from these operators to the selected Q6/RGS sector, if one exists.
5. Derive the T144 polynomial (f(x)=\frac12+\frac{x}{120}+\frac{x^2}{240}) from the dodecahedral geometry, rather than interpolating it.

**Conclusion:** T158 removes the endpoint-only approximation in the Whitney mass assembly by specifying a continuous pullback connection inside each triangle. It closes the finite-mesh interior-transport construction, but does not yet prove refinement convergence or a continuum FEEC theorem.

## 6. Reproduction

```bash
python scripts/audit_t158_interior_covariant_whitney.py
python -m unittest tests.test_t158_interior_covariant_whitney
```

Machine-readable report: `results/json/t158_interior_covariant_whitney.json`. Workflow: `.github/workflows/t158-interior-covariant-whitney.yml`.


## 7. Refinement follow-up — T159

[T159 — curved FEEC mesh-refinement audit](T159-curved-feec-mesh-refinement.md) refines the same 32–90–60 surface by factors 1–4 while keeping the parent T158 normal map fixed through parent barycentric coordinates. The lowest covariant Hodge-0 triplet stabilizes numerically from 2.28896737 to 2.37155870; the successive first-eigenvalue increments decrease. This is finite numerical evidence only: spectral convergence, a curved-FEEC error theorem, and the Q6/RGS intertwiner remain open.
