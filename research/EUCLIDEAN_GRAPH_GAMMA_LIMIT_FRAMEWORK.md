# Euclidean graph energies: a first discrete-to-continuum theorem

**Status:** conditional theorem framework; the graph-to-compactness and graph-to-integral-representation steps are not yet proved under the geometric hypotheses alone.

**Scope:** scalar-valued, uniformly elliptic, quadratic nearest-edge energies on embedded graphs in a fixed Euclidean domain. This is deliberately a baseline problem, not yet an RGS, curved-metric, Hodge, or de Rham convergence theorem.

## 1. Objective and claim boundary

Let \(\Omega\subset\mathbb R^d\) be bounded and Lipschitz. For \(\varepsilon\downarrow0\), let
\[
G_\varepsilon=(V_\varepsilon,E_\varepsilon)
\]
be a finite undirected graph embedded in \(\overline\Omega\). The first objective is to understand limits of quadratic energies built only from its edges.

The intended continuum functional is
\[
F(u)=
\begin{cases}
\displaystyle\int_\Omega \nabla u(x)^{T}A(x)\nabla u(x)\,dx,
&u\in H^1(\Omega),\\[1mm]
+\infty,&u\notin H^1(\Omega),
\end{cases}
\]
where \(A(x)\) is measurable, symmetric, and uniformly elliptic:
\[
0<\lambda I\le A(x)\le \Lambda I
\quad\text{for a.e. }x\in\Omega.
\]

The central distinction is:

- compactness plus integral representation may identify every subsequential limit;
- they do **not** by themselves imply that the entire sequence has one limit;
- uniqueness of the cell limit, or another mechanism identifying all subsequential densities, is an additional obligation.

No convergence theorem for arbitrary graphs follows merely from vertex separation, relative density, short edges, and approximate-geodesic paths. In particular, those geometric assumptions do not by themselves exclude bottlenecks, poor directional sampling, or oscillating effective coefficients.

## 2. Euclidean graph hypotheses

Fix constants \(c_{\rm sep},C_{\rm fill},C_{\rm edge},C_{\rm path}>0\), independent of \(\varepsilon\).

**(G1) Common ambient space.** Every \(G_\varepsilon\) is embedded in \(\overline\Omega\subset\mathbb R^d\), with the Euclidean norm and Lebesgue measure. No varying metric is used at this stage.

**(G2) Uniform separation.** For distinct vertices,
\[
|x-y|\ge c_{\rm sep}\varepsilon,
\qquad x,y\in V_\varepsilon.
\]

**(G3) Relative density / fill distance.** Away from the boundary layer, every point is within \(C_{\rm fill}\varepsilon\) of a vertex:
\[
\sup_{z\in\Omega_{C\varepsilon}}
\operatorname{dist}(z,V_\varepsilon)
\le C_{\rm fill}\varepsilon,
\]
where \(\Omega_{C\varepsilon}=\{z\in\Omega:
\operatorname{dist}(z,\partial\Omega)>C\varepsilon\}\). A boundary-compatible version can instead be imposed on \(\overline\Omega\).

**(G4) Edge scale.** Every edge \(e=\{x,y\}\in E_\varepsilon\) satisfies
\[
c_{\rm edge}\varepsilon\le |y-x|
\le C_{\rm edge}\varepsilon.
\]
The lower bound follows from (G2) for distinct endpoints, but is recorded to make the energy scale explicit.

**(G5) Approximate-geodesic connectivity.** For every pair \(x,y\in V_\varepsilon\), there is an edge path \(P_\varepsilon(x,y)\) joining them whose vertices lie in the \(C_{\rm path}\varepsilon\)-neighbourhood of the Euclidean segment \([x,y]\). Every edge on the path satisfies (G4).

The path is a connectivity/geometric-accessibility condition. It is **not** a substitute for a uniform Poincaré inequality: it gives no uniform bound on path length, overlap, congestion, or the energy cost of transporting values through a bottleneck.

**(G6) Edge weights.** Each edge has a scalar conductance \(a_e^\varepsilon\) with
\[
0<a_-\le a_e^\varepsilon\le a_+<\infty.
\]

By separation and the upper edge-length bound, the degree is uniformly bounded by a packing argument. This controls local edge counts, but does not by itself give coercivity in every direction.

## 3. Discrete energy and identification with \(L^2(\Omega)\)

For \(v:V_\varepsilon\to\mathbb R\), define
\[
\mathcal E_\varepsilon(v)
=\frac12\sum_{\{x,y\}\in E_\varepsilon}
\varepsilon^{d-2}a_{\{x,y\}}^\varepsilon
\big(v(y)-v(x)\big)^2.
\tag{3.1}
\]
The factor \(1/2\) is a convention and can be absorbed into the conductances. The scaling \(\varepsilon^{d-2}\) is the one compatible with a first-order continuum gradient in dimension \(d\).

Let \(\{V_\varepsilon(x)\}_{x\in V_\varepsilon}\) be the Euclidean Voronoi partition, clipped to \(\Omega\), with a fixed measurable tie-breaking convention. Define the piecewise-constant identification
\[
(P_\varepsilon v)(z)=v(x)
\quad\text{for }z\in V_\varepsilon(x).
\]
The functional on the fixed space \(L^2(\Omega)\) is
\[
F_\varepsilon(w)=
\begin{cases}
\mathcal E_\varepsilon(v),&w=P_\varepsilon v,\\
+\infty,&w\notin P_\varepsilon\mathbb R^{V_\varepsilon}.
\end{cases}
\tag{3.2}
\]
This makes the varying discrete spaces explicit. The cell volumes are of order \(\varepsilon^d\) in the interior under (G2)–(G3); boundary cells require the corresponding boundary convention.

The continuum comparison is strong \(L^2(\Omega)\). Other identifications (finite elements, partitions, or averaging maps) are possible, but must be specified and proved consistent rather than silently interchanged.

## 4. The missing analytic hypothesis: uniform compactness

The geometric assumptions (G1)–(G6) are not currently claimed to imply compactness. Add one of the following analytic conditions and then investigate whether it can be derived from stronger graph-geometric assumptions.

**(C1) Extension formulation.** There are linear or suitably stable extension/interpolation maps
\[
I_\varepsilon:\mathbb R^{V_\varepsilon}\to H^1(\Omega)
\]
and a constant \(C\) independent of \(\varepsilon\) such that
\[
\|\nabla I_\varepsilon v\|_{L^2(\Omega)}^2
\le C\mathcal E_\varepsilon(v),
\qquad
\|I_\varepsilon v-P_\varepsilon v\|_{L^2(\Omega)}^2
\le C\varepsilon^2\mathcal E_\varepsilon(v).
\tag{4.1}
\]
A harmless \(L^2\)-normalization (or a fixed mean value) is also imposed when controlling constants.

Then bounded energy and bounded \(L^2\)-norm give boundedness of \(I_\varepsilon v\) in \(H^1(\Omega)\). Rellich compactness gives a strongly \(L^2\)-convergent subsequence, and (4.1) transfers that convergence to \(P_\varepsilon v\).

**(C2) Fréchet–Kolmogorov formulation.** Alternatively, require a uniform translation estimate for the zero-mean or normalized interpolants:
\[
\|P_\varepsilon v(\,\cdot+h)-P_\varepsilon v\|_
 {L^2(\Omega_{|h|})}^2
\le C(|h|+\varepsilon)^2\mathcal E_\varepsilon(v),
\tag{4.2}
\]
together with uniform \(L^2\) boundedness and a boundary-extension/equi-tightness condition. For sequences \(\varepsilon_n\to0\), (4.2) yields the translation control needed by the Fréchet–Kolmogorov criterion.

**Important:** (C1) or (C2) is an additional analytic input, not a consequence asserted here from (G1)–(G6). A proof deriving it from the path condition would need quantitative control of path lengths and congestion, or a suitable uniform discrete Poincaré/isoperimetric inequality.

## 5. Locality, growth, and the integral-representation target

For an open set \(U\subset\Omega\), define the localized energy
\[
\mathcal E_\varepsilon(v;U)
=\frac12\sum_{\substack{\{x,y\}\in E_\varepsilon\\
[x,y]\cap U\ne\varnothing}}
\varepsilon^{d-2}a_{\{x,y\}}^\varepsilon
(v(y)-v(x))^2,
\tag{5.1}
\]
with a fixed convention for edges crossing \(\partial U\). Any rigorous proof must use one boundary convention consistently and show that boundary-layer choices do not affect the limit.

The integral-representation argument requires, in addition to compactness:

- **(L1) locality:** interactions are nearest-edge and have range \(O(\varepsilon)\);
- **(L2) uniform upper growth:** a suitable interpolant or recovery construction gives an upper bound by the continuum \(H^1\) energy;
- **(L3) coercive lower growth:** discrete energy controls the relevant \(H^1\)-type difference quotients;
- **(L4) fundamental estimate / gluing:** functions can be joined across an annulus with a controlled energy error;
- **(L5) measure property:** localized energies have the required subadditivity and inner-regularity properties in the limit;
- **(L6) quadratic stability:** the limit of the quadratic forms remains a quadratic form (for example, through an appropriate Mosco convergence theorem for closed forms on the fixed \(L^2\) space).

These are proof obligations. The cited lattice theorems provide a model for the integral-representation and homogenization strategy, but their hypotheses are not automatically verified for the present arbitrary embedded graph class.

## 6. Conditional theorem (the first target)

**Theorem A — subsequential Euclidean graph limit (conditional).**

Let \(\Omega\subset\mathbb R^d\) be bounded and Lipschitz, and let \(G_\varepsilon\) satisfy (G1)–(G6). Suppose in addition that:

1. the identification maps \(P_\varepsilon\) are uniformly \(L^2\)-consistent and satisfy compactness condition (C1) or (C2);
2. the localized energies satisfy (L1)–(L5), with uniform coercive and upper \(H^1\)-growth bounds;
3. the quadratic-form stability condition (L6) holds.

Then every sequence \(\varepsilon_n\downarrow0\) has a subsequence (not relabelled) for which \(F_{\varepsilon_n}\) \(\Gamma\)-converges in strong \(L^2(\Omega)\) to a local quadratic functional of the form
\[
F_0(u)=
\begin{cases}
\displaystyle\int_\Omega \nabla u(x)^T A_0(x)
\nabla u(x)\,dx,&u\in H^1(\Omega),\\
+\infty,&\text{otherwise},
\end{cases}
\tag{6.1}
\]
where \(A_0\in L^\infty(\Omega;\mathbb R^{d\times d}_{\rm sym})\) and
\[
0<\lambda_0 I\le A_0(x)\le\Lambda_0 I
\quad\text{for a.e. }x\in\Omega.
\tag{6.2}
\]

The constants in (6.2) depend on the uniform growth/coercivity constants, not just on vertex separation and edge length.

**Status of Theorem A:** this is a conditional theorem target, not a completed proof for (G1)–(G6). The main open work is to derive (C1)/(C2), the fundamental estimate, and the required locality/growth bounds from verifiable graph hypotheses. The abstract integral-representation machinery can only be invoked after these hypotheses have been checked.

## 7. Cell formula and full-sequence convergence

A cell formula is the natural candidate for identifying the density. For a cube \(Q_R(x)\), an affine slope \(\xi\in\mathbb R^d\), and a boundary strip of width comparable to \(\varepsilon\), define the finite-cell minimum
\[
m_\varepsilon(\xi,Q_R(x))
=\inf\left\{
\mathcal E_\varepsilon(v;Q_R(x)):
v(z)=\xi\cdot z
\text{ on the prescribed boundary strip}
\right\}.
\tag{7.1}
\]
The exact set of constrained vertices and the treatment of crossing edges must be fixed in an implementation and in a proof.

For a local blow-up formula on the bounded macroscopic domain, the natural candidate is
\[
f(x,\xi)
=\lim_{r\downarrow0}\ \lim_{\varepsilon\downarrow0}
\frac{m_\varepsilon(\xi,Q_r(x))}{|Q_r|},
\qquad \varepsilon/r\to0,
\tag{7.2}
\]
at points where the limit exists, with the boundary strip and crossing-edge convention fixed. Here the inner limit is taken with the physical cube fixed and the mesh tending to zero; the outer limit shrinks the cube to the macroscopic point. For periodic or stationary homogenization, an equivalent cell problem is often expressed instead on the rescaled reference graph in cubes of side length \(R\to\infty\). These are different formulations and must not be conflated.

To obtain **full-sequence** convergence, it is sufficient to prove that every subsequential \(\Gamma\)-limit has the same density, equivalently that the relevant cell minima converge to one deterministic value independently of the extracted subsequence. Possible routes include:

- periodic graph geometry and periodic conductances;
- stationary ergodic graph environments with the appropriate ergodic theorem and integrability assumptions;
- deterministic quantitative homogenization or a direct Cauchy criterion for the cell energies;
- a unique blow-up/cell limit at almost every macroscopic point.

None of these structural assumptions is part of (G1)–(G6). Without one of them, oscillating graph geometries can in principle produce different subsequential effective tensors.

## 8. Which quadratic forms can the graph geometry produce?

For an affine test function \(u_\xi(z)=\xi\cdot z\), the energy per unit volume is governed by the edge-direction second moment
\[
M_\varepsilon(U)
=\frac{1}{2|U|}
\sum_{\substack{e=\{x,y\}\in E_\varepsilon\\
e\subset U}}
\varepsilon^{d-2}a_e^\varepsilon
(y-x)\otimes(y-x).
\tag{8.1}
\]
Indeed,
\[
\frac{\mathcal E_\varepsilon(u_\xi;U)}{|U|}
=\xi^T M_\varepsilon(U)\xi
\]
up to the declared boundary-edge convention. If \(M_\varepsilon(U)\to M\), then \(M\) is the affine-test energy tensor. It is an upper-bound/candidate diagnostic for the homogenized tensor, not generally the homogenized tensor itself: microscopic correctors can lower the cell energy.

Consequences:

- if edge directions asymptotically occupy only a proper subspace, the affine moment matrix is rank-deficient and uniform ellipticity fails;
- directional balance can produce anisotropic tensors;
- isotropy requires rotational symmetry/isotropy of the relevant weighted graph statistics, not merely Euclidean embedding;
- the full set of realizable effective tensors is a separate characterization problem involving both direction statistics and corrector relaxation.

A useful numerical first gate is therefore to compute the eigenvalues and eigenvectors of \(M_\varepsilon(U)\) on mesoscopic boxes before attempting any continuum fit.

## 9. Minimal computational benchmark

The first benchmark should be deliberately Euclidean and scalar.

1. Generate graph families with fixed \(\Omega\), decreasing \(\varepsilon_k=2^{-k}\varepsilon_0\), and recorded separation, fill-distance, edge-length, degree, and path-tube diagnostics.
2. Build the Voronoi identification \(P_{\varepsilon_k}\) and record cell-volume bounds.
3. Assemble (3.1) with \(a_e^\varepsilon\in[a_-,a_+]\).
4. Test affine fields \(u_\xi(x)=\xi\cdot x\) for a spanning set of \(\xi\); report \(M_\varepsilon\) and its spectrum.
5. Test compactness numerically using the discrete interpolation/extension map and translation moduli; numerical tests are diagnostics, not proofs of (C1)/(C2).
6. Solve finite cell problems (7.1) for several slopes and increasing cell sizes; report boundary sensitivity and the order of limits.
7. Compare the observed cell tensor with the affine moment tensor, explicitly allowing for corrector effects.
8. Test whether different subsequences or graph realizations yield the same cell density.

**Acceptance gate:** no curved metric, RGS weight, Hodge star, de Rham operator, torsion, or physical interpretation is introduced until the Euclidean graph theorem has a proof or a clearly delimited counterexample.

## 10. Relation to the later RGS/de Rham programme

Once Theorem A is proved in the Euclidean scalar setting, extensions should be introduced one at a time:

1. vector-valued displacements and elasticity-type quadratic forms;
2. simplicial complexes and compatible discrete differential forms;
3. convergence of incidence operators and weighted Hodge energies;
4. varying Hilbert spaces with explicit identification maps and Mosco convergence;
5. curved target metrics and geometric transport;
6. RGS-specific structures and physical interpretations.

The existing E(2) graph-transport convergence result concerns transport along approximating paths. It is a distinct result and does not establish compactness or \(\Gamma\)-convergence of the graph energies considered here.

## 11. Literature and precise use

1. R. Alicandro and M. Cicalese, “A General Integral Representation Result for Continuum Limits of Discrete Energies with Superlinear Growth,” *SIAM Journal on Mathematical Analysis* 36 (2004), 1–37, DOI: [10.1137/S0036141003426471](https://doi.org/10.1137/S0036141003426471). This is a general discrete-to-continuum integral-representation reference; its stated setting is a lattice, not the arbitrary embedded graph class above.
2. R. Alicandro, M. Cicalese, and A. Gloria, “Integral Representation Results for Energies Defined on Stochastic Lattices and Application to Nonlinear Elasticity,” *Archive for Rational Mechanics and Analysis* 200 (2011), 881–943, DOI: [10.1007/s00205-010-0378-7](https://doi.org/10.1007/s00205-010-0378-7). This provides a stochastic-lattice homogenization framework and cell-formula strategy; stationarity/ergodicity and the paper's lattice assumptions must not be silently replaced by (G1)–(G6).

## 12. Open obligations register

| ID | Obligation | Status |
|---|---|---|
| EG-01 | Derive a uniform discrete Poincaré/extension estimate from explicit graph hypotheses | Open |
| EG-02 | Prove Fréchet–Kolmogorov compactness for the chosen Voronoi identification | Open, conditional on EG-01 |
| EG-03 | Prove the graph fundamental estimate and boundary-layer stability | Open |
| EG-04 | Establish the local integral representation for this graph class | Open |
| EG-05 | Prove preservation of quadratic structure under the selected convergence notion | Open / theorem-specific |
| EG-06 | Define and validate the cell problem, including boundary convention and order of limits | Open |
| EG-07 | Give sufficient conditions for full-sequence cell convergence | Open |
| EG-08 | Characterize effective tensors realizable by graph geometry | Open |
| EG-09 | Extend the scalar result to de Rham/Hodge energies on varying spaces | Deferred |

**Overall classification:** RESEARCH FRAMEWORK / CONDITIONAL THEOREM TARGET. No theorem is marked proved by this document.
