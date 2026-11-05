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
where ell_jk is the spherical primal-edge length and ell*_jk is the geodesic distance between the circumcentres of its two adjacent spherical triangles. The construction uses positive conductances and the graph energy convention
\[
\mathcal E_h(v)=\frac12\sum_{x,y}b_h(x,y)|v(x)-v(y)|^2.
\]

These formulas define a concrete finite-volume graph family. The angular circumcentric construction must still be audited for all refinement levels; failure of positivity is treated as a hard error, not repaired by clipping weights.

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