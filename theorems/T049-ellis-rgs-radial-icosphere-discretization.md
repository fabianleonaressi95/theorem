# Ellis–RGS radial–icosphere discretization prototype

**Status: explicit positive-conductance benchmark; not a Mosco-convergence theorem and not yet an RGS-derived refinement.**

## Decision

The existing 64-point O_h coordinate seed and Q6 edge/coframe data are not a tetrahedral mesh. The repository manifest explicitly rules out identifying the Q6 2-skeleton with a tetrahedral mesh or relabelling its link coframe as a tetrahedral coframe. Therefore the first implementable continuum calibration is a geometry-first product discretization of the already specified Ellis benchmark. The RGS coordinate seed is retained as a later candidate for a structure-preserving refinement, after a valid cell complex and geometric maps have been constructed.

This choice deliberately separates (i) testing the continuum metric and energy from (ii) proving that the RGS combinatorics generate that metric.

## Continuum target

Let
\[
\Omega_L=[-L,L]\times S^2,\qquad L=3r_0,\qquad r_0=0.8292,
\]
with
\[
g=du^2+a(u)^2g_{S^2},\qquad a(u)^2=u^2+r_0^2.
\]
Then
\[
d\mu_g=a(u)^2\,du\,d\Omega,\qquad
\Delta_g=a^{-2}\partial_u(a^2\partial_u)+a^{-2}\Delta_{S^2}.
\]
The Dirichlet energy is
\[
\mathcal E(f)=\int_{-L}^{L}\int_{S^2}
\left(a(u)^2|\partial_u f|^2+|\nabla_{S^2}f|^2\right)d\Omega\,du.
\]
The radial boundary convention in the prototype is natural (Neumann): no edges are added beyond the first and last radial layers.

The exact continuum volume is
\[
\mu_g(\Omega_L)=4\pi\int_{-3r_0}^{3r_0}(u^2+r_0^2)\,du=96\pi r_0^3.
\]

## Discrete spaces

For a radial partition with N_r cells, let u_i be cell centres and delta_i the associated one-dimensional dual widths. On S^2, use a recursively subdivided icosahedron, its spherical Voronoi dual cells C_j, and their areas A_j. The product graph has vertices (i,j) and
\[m_{ij}=\delta_i(u_i^2+r_0^2)A_j.\]
Thus H_h=ell^2(V_h,m_h).

For radial neighbours:
\[
b^{(r)}_{(i,j),(i+1,j)}=
\frac{(u_{i+1/2}^2+r_0^2)A_j}{u_{i+1}-u_i}.
\]
For angular neighbours j~k, use the circumcentric spherical dual:
\[
b^{(omega)}_{(i,j),(i,k)}=\delta_i\frac{\ell^*_{jk}}{\ell_{jk}},
\]
where ell_jk is the spherical primal-edge length and ell*_jk is the oriented dual-arc length between the circumcentres of its two adjacent spherical triangles. The implementation measures signed angles from the normalized primal-edge midpoint and accepts the dual only when the two circumcentres lie on opposite sides of that midpoint; see T070. It rejects a same-side pair instead of treating its unsigned geodesic separation as a valid dual. The graph energy convention is
\[
\mathcal E_h(v)=\frac12\sum_{x,y}b_h(x,y)|v(x)-v(y)|^2.
\]

These formulas define a concrete finite-volume graph family. The oriented circumcentric crossing condition is checked edge-by-edge in the constructor. Its execution across refinement levels remains a test obligation; failure of crossing or positivity is a hard error, not repaired by clipping weights. This geometric check is necessary but does not by itself prove angular DEC energy consistency.

## Identification maps

For product cells K_ij, define I_h v to be piecewise constant with value v_ij. The script uses the exact radial cell integral and spherical Voronoi cell area, so the piecewise-constant reconstruction I_h:H_h to L^2(Omega_L,dmu_g) is exactly isometric for this product partition.

For f in L^2, define J_h f by cell averages with respect to dmu_g. Then I_h J_h f tends to f in L^2 as the product partition mesh tends to zero, provided the maximal cell diameter tends to zero and the partitions are shape-regular.

## What this prototype does and does not establish

The script scripts/ellis_rgs_radial_icosphere_prototype.py constructs the graph, reports node/edge counts, positivity, and the discrete-vs-continuum volume discrepancy. The tests check graph counts, positivity, spherical area normalization, and radial volume convergence.

It does NOT establish:
- Mosco liminf (M1);
- a recovery sequence for the graph energy (M2);
- a uniform discrete Rellich estimate;
- spectral convergence;
- that the original O_h/Q6 RGS seed generates this product mesh or its conductances.

## Next mathematical obligations

1. Retain exact radial cell masses m_ij=A_j integral over the radial cell of (u^2+r0^2) du, and add tests for exact total mass.
2. Audit circumcentric dual geometry and conductance positivity at several angular levels.
3. Prove consistency on smooth separated test functions f(u,omega)=p(u)Y_lm(omega).
4. Prove M1 using a uniform discrete gradient bound and weak lower semicontinuity.
5. Prove M2 by cell-average recovery and consistency.
6. Prove a uniform discrete Rellich estimate before claiming compact resolvent or eigenvalue convergence.
7. Only then construct a separate RGS-preserving refinement and compare its metric, measures, and energies with this benchmark.

The finite PRISM graph C64 square C6^3 square C5 remains a finite combinatorial model; it is not silently treated as a member of this radial–icosphere refinement family.

## First separated-mode diagnostic

The script now reports the discrete Rayleigh quotient of the coordinate function
\[
Y_{1}(\omega)=\omega_3,
\]
whose continuum spherical eigenvalue is 2:
\[
-\Delta_{S^2}Y_1=2Y_1.
\]
The discrete quotient is
\[
\lambda_{1,h}=\frac{\sum_{\{j,k\}}(\ell^*_{jk}/\ell_{jk})(Y_1(\omega_j)-Y_1(\omega_k))^2}
{\sum_j A_jY_1(\omega_j)^2}.
\]
This is a **consistency diagnostic only**. The test checks finiteness and positivity at two refinement levels; it deliberately does not assert monotone convergence or treat a finite quotient as proof of the angular Mosco liminf/recovery statements.


## Separated-variable energy factorization

For nodal data v_ij=p(u_i)Y(omega_j), the product graph energy splits exactly:
\[
\mathcal E_h(v)=
\left[\sum_i\frac{a(u_{i+1/2})^2}{u_{i+1}-u_i}
(p(u_{i+1})-p(u_i))^2\right]
\left[\sum_j A_jY(\omega_j)^2\right]
+
\left[\sum_i\delta_i p(u_i)^2\right]
\left[\sum_{\{j,k\}}\frac{\ell^*_{jk}}{\ell_{jk}}
(Y(\omega_j)-Y(\omega_k))^2\right].
\]
This identity is useful because it isolates the radial and spherical consistency problems. The corresponding continuum expression is
\[
\mathcal E(pY)=
\left[\int_{-L}^L a(u)^2|p'(u)|^2du\right]
\left[\int_{S^2}Y^2d\Omega\right]
+
\left[\int_{-L}^L p(u)^2du\right]
\left[\int_{S^2}|\nabla_{S^2}Y|^2d\Omega\right].
\]

A new invariant test uses p(u)=u and Y=1. Since a(u)^2=u^2+r0^2 is quadratic, the radial midpoint quadrature is exact on each interval between adjacent radial cell centres; the angular areas sum to 4 pi. At finite resolution the graph has no exterior radial edges, so its energy equals 4 pi integral from u_0 to u_{N_r-1} of a(u)^2 du, where u_0 and u_{N_r-1} are the first and last cell centres. It does not equal the full-domain integral at finite h: the two omitted boundary half-cells contribute an O(h_r) term. Those boundary contributions vanish as h_r tends to zero. This exact interior calibration checks the radial conductance normalization, not the boundary truncation, general p, or the angular factor.


## Conditional consistency proposition for separated smooth modes

**Proposition (separated-mode consistency, conditional on angular DEC consistency).**
Let the radial partitions be quasi-uniform with mesh size h_r tending to zero, and let the spherical triangulations be shape-regular with maximal edge length h_s tending to zero. Assume positive circumcentric dual weights and, for every smooth Y on S^2, the two angular consistency limits
\[
\sum_j A_jY(\omega_j)^2\longrightarrow\int_{S^2}Y^2d\Omega,
\qquad
\sum_{\{j,k\}}\frac{\ell^*_{jk}}{\ell_{jk}}
(Y(\omega_j)-Y(\omega_k))^2
\longrightarrow\int_{S^2}|\nabla_{S^2}Y|^2d\Omega.
\]
Then for every smooth p on [-L,L] and smooth Y on S^2, the nodal product samples v_ij=p(u_i)Y(omega_j) satisfy
\[
\mathcal E_h(v_h)\longrightarrow\mathcal E(pY).
\]

**Proof.** Use the exact separated-variable factorization above. The radial difference quotient converges uniformly to p' on compact intervals, while the midpoint samples of a(u)^2 converge by Riemann-sum consistency. Hence the first radial bracket tends to integral a^2|p'|^2. The radial dual-width sum tends to integral p^2. The two angular brackets converge by the stated angular hypotheses. Multiplying the convergent factors and adding proves the energy limit. The same cell-quadrature argument, using the exact radial masses, gives convergence of the discrete L2 norms for these smooth separated samples. QED.

**Logical scope.** This proposition is a consistency result on a tensor-product core, conditional on the angular DEC consistency statement. It is not the Mosco liminf inequality for arbitrary weakly convergent sequences, nor does it provide a recovery sequence for every function in the limiting form domain. To obtain M2 one must extend from a dense smooth core with a controlled diagonal argument; M1 still requires a uniform lower-bound/compactness mechanism. In particular, this proposition does not establish compact resolvent or spectral convergence.
