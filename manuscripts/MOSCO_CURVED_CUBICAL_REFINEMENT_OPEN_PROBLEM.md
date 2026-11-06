# Mosco Convergence for Refinement-Dependent Curved Cubical Complexes

**Open problem and proof strategy — companion to T048**

**Status.** This document formulates a concrete refinement programme and a set of sufficient-condition targets. It does not claim that Mosco convergence has been proved for the RGS–PRISM sequence. The product-grid construction below is a baseline model; the passage to genuinely curved, non-affinely mapped RGS cells remains a separate theorem to establish.

- Main record: [T048 — Mosco convergence and spectral compactness for RGS–PRISM refinements](../theorems/T048-rgs-prism-mosco-changing-spaces.md)
- Calibration code: [periodic-cycle model](../scripts/rgs_prism_mosco_calibration.py)
- Calibration tests: [T048 tests](../tests/test_t048_rgs_prism_mosco_calibration.py)

## 1. The precise question

Let \(M\) be a compact, connected, smooth \(d\)-dimensional Riemannian manifold, possibly with a regular boundary and a fixed boundary condition. Let \(\mathcal T_h\) be a family of cubical cell decompositions whose maximum cell diameter tends to zero. The cells are allowed to be curved and to be represented by non-affine maps from a reference cube.

For each resolution \(h\), let \(V_h\) be the set of cell centres (or another explicitly specified set of degrees of freedom), \(m_h(x)>0\) a vertex measure, and \(b_h(x,y)=b_h(y,x)\geq0\) edge conductances. Define
\[
H_h=\ell^2(V_h,m_h),\qquad
\mathcal E_h(u)=\frac12\sum_{x,y\in V_h}b_h(x,y)|u(x)-u(y)|^2.
\]
The target is
\[
H=L^2(M,d\mathrm{vol}_g),\qquad
\mathcal E(u)=\int_M|\nabla_g u|_g^2\,d\mathrm{vol}_g,
\qquad D(\mathcal E)=H^1(M),
\]
with the appropriate boundary-condition domain when \(\partial M\ne\varnothing\).

**Question.** Which geometric and analytic assumptions on the non-affine cell maps, metric tensors, measures, and conductances guarantee generalized Mosco convergence of \((H_h,\mathcal E_h)\) to \((H,\mathcal E)\), and which additional assumptions give compactness of resolvents and convergence of isolated eigenvalue clusters with multiplicity?

The question has two logically distinct parts:

1. prove generalized Mosco convergence (weak liminf and strong recovery);
2. prove uniform compactness sufficient for spectral convergence.

Neither part follows from convergence of a finite list of eigenvalues.

## 2. A concrete refinement sequence already suggested by PRISM

The finite graph
\[
G_1=C_{64}\square C_6\square C_6\square C_6\square C_5
\]
is a five-dimensional product of cycles, with \(69120\) vertices and degree \(10\). It is a finite combinatorial object; by itself it does not specify a Riemannian metric or a continuum limit.

A natural *baseline refinement* is
\[
G_r=C_{64r}\square C_{6r}^{\,\square 3}\square C_{5r},
\qquad r\in\mathbb N,\quad r\to\infty.
\]
Here \(C_{6r}^{\,\square 3}\) means three Cartesian factors, not a graph power. Then
\[
|V_r|=69120\,r^5,\qquad \deg(G_r)=10.
\]
This preserves the five-factor product pattern while subdividing every cyclic direction.

For a flat unit five-torus, set
\[
n(r)=(64r,6r,6r,6r,5r),\qquad
h_j(r)=1/n_j(r),\qquad
m_r(x)=\prod_{j=1}^5h_j(r).
\]
For an edge in coordinate direction \(j\), use
\[
b_{r,j}=\frac{m_r(x)}{h_j(r)^2}.
\]
The resulting form is
\[
\mathcal E_r(u)=
\sum_{x\in V_r}\sum_{j=1}^5
\frac{m_r(x)}{h_j(r)^2}
|u(x+e_j)-u(x)|^2,
\]
where each unoriented edge is counted once. This is the standard anisotropic finite-difference energy on a rectangular periodic grid. It supplies a precise flat benchmark with the same five cycle factors and a fixed degree.

**Important limitation.** \(G_r\) is a proposed refinement family, not an already established geometric refinement of the current RGS–PRISM data. A repository-level construction must still define the coordinate assignment, physical side lengths, cell measures, and the maps from the coarse RGS data to each refined level. The flat five-torus is a calibration target, not an assertion that the physical RGS limit is a torus.

## 3. Curved cells and non-affine maps

Let \(\widehat Q=[0,1]^d\) be the reference cube. For every cell \(Q\in\mathcal T_h\), prescribe a map
\[
F_{h,Q}:\widehat Q\longrightarrow \overline Q\subset M.
\]
The maps need not be affine. A usable regularity class is \(C^1\) with weak second derivatives, or \(C^2\) when the estimates require pointwise curvature control.

The first geometric hypotheses to test are:

**(G1) Valid cell maps.** Each \(F_{h,Q}\) is one-to-one on the cell interior, has nonsingular differential almost everywhere, and maps faces consistently to shared cell faces. Cell interiors are disjoint and cover \(M\) up to measure-zero interfaces.

**(G2) Uniform shape regularity.** There are constants \(0<c<C<\infty\), independent of \(h,Q\), such that
\[
c h^d\leq \mathrm{vol}_g(Q)\leq C h^d,
\qquad
c h\leq \mathrm{diam}_g(Q)\leq C h,
\]
and the singular values of \(DF_{h,Q}\), after the reference scaling by \(h\), are uniformly bounded above and away from zero.

**(G3) Controlled non-affinity.** The scaled derivatives and metric pullbacks are uniformly regular. A typical sufficient target is
\[
\|D F_{h,Q}\| \leq C h,\quad
\|(D F_{h,Q})^{-1}\|\leq C h^{-1},\quad
\|D^2F_{h,Q}\|\leq C h
\]
in local coordinates, with the precise powers adjusted to the chosen reference-cell scaling. Equivalently, after rescaling each cell to unit size, the maps have uniformly bounded \(C^{1,1}\) norms and uniformly nondegenerate Jacobians. The rescaled metric coefficients
\[
g_{h,Q}=(DF_{h,Q})^\top g(F_{h,Q})DF_{h,Q}
\]
must be uniformly elliptic and have a uniform modulus of continuity.

**(G4) Metric consistency.** The discrete edge geometry and conductances must approximate the target metric tensor, not just the combinatorial adjacency. In local coordinates, a useful moment-consistency target is
\[
\frac{1}{2m_h(x)}
\sum_y b_h(x,y)\,
\xi_{xy}\otimes\xi_{xy}
\longrightarrow A(x),
\]
uniformly (or in a controlled \(L^p\) sense), where \(\xi_{xy}\in T_xM\) is the consistently transported edge displacement and \(A\) is the coefficient tensor of the target energy relative to the chosen measure. For \(d\mathrm{vol}_g\) and the scalar Laplace–Beltrami energy, \(A=g^{-1}\). This second-moment condition is a consistency condition, not by itself a Mosco theorem: it must be paired with shape regularity, coercivity, and a discrete compactness argument.

**(G5) Positive, stable conductances.** \(b_h(x,y)\geq0\), with uniform ellipticity after scaling. If the mapped grid is not asymptotically orthogonal, nearest-neighbour two-point flux weights may fail to reproduce cross terms of the metric tensor. In that case one must either impose asymptotic orthogonality, enlarge the stencil with a proved positive moment representation, or use a different discrete form. One must not silently assume that arbitrary non-affine maps preserve a positive nearest-neighbour graph representation.

These hypotheses are intentionally stated as a proof target. Their compatibility for a particular RGS–PRISM cell geometry must be checked, not presumed.

## 4. Identification maps on changing Hilbert spaces

For a cell-centred scheme, define the reconstruction
\[
I_hu_h=\sum_{Q\in\mathcal T_h}u_h(Q)\,\mathbf1_Q.
\]
Choose
\[
m_h(Q)=\mathrm{vol}_g(Q).
\]
Then \(I_h:H_h\to L^2(M)\) is an isometry:
\[
\|I_hu_h\|_{L^2(M)}^2
=\sum_Q\mathrm{vol}_g(Q)|u_h(Q)|^2
=\|u_h\|_{H_h}^2.
\]
For \(f\in C^\infty(M)\), define the sampling map by cell averages
\[
(J_hf)(Q)=\frac{1}{\mathrm{vol}_g(Q)}\int_Qf\,d\mathrm{vol}_g.
\]
Then \(I_hJ_hf\to f\) strongly in \(L^2(M)\) as the mesh size tends to zero, provided the partitions are shape regular and their maximum diameter tends to zero.

For a vertex-based RGS graph, the same construction requires a geometrically defined dual cell around each vertex. The dual cells must form a partition (up to null sets), and their volumes—not arbitrary graph weights—must define \(m_h\). If no such dual partition is specified, the claimed identification map is incomplete.

The strong and weak varying-space convergence notions should be defined through \(I_h\) (or a fully specified pair \(I_h,J_h\)). In particular, weak convergence must not be inferred solely from convergence of coordinate arrays.

## 5. Candidate analytic hypotheses for Mosco convergence

The following is a practical sufficient-condition programme, not a theorem asserted for the current RGS data.

**(A1) Uniform coercivity and boundedness.** There are constants \(0<c_0\leq C_0<\infty\) such that the discrete energy controls and is controlled by a consistent discrete gradient norm, uniformly in \(h\). The continuum coefficient tensor is uniformly elliptic:
\[
c_0|\zeta|_g^2\leq \langle A\zeta,\zeta\rangle_g
\leq C_0|\zeta|_g^2.
\]

**(A2) Smooth-core consistency.** For every \(f\in C^\infty(M)\),
\[
\|I_hJ_hf-f\|_{L^2(M)}\to0,\qquad
\mathcal E_h(J_hf)\to\mathcal E(f).
\]
The second limit must be derived from the metric pullback, cell Jacobians, and conductance construction. It is not enough to observe convergence for a finite collection of Fourier modes.

**(A3) Discrete Rellich estimate.** There is a modulus \(\omega(\delta)\to0\), independent of \(h\), such that reconstructed energy-bounded functions have uniformly small local oscillations. One possible formulation, using a suitable local averaging operator \(P_\delta\), is
\[
\|I_hu_h-P_\delta I_hu_h\|_{L^2(M)}^2
\leq \omega(\delta)^2
\big(\|u_h\|_{H_h}^2+\mathcal E_h(u_h)\big)
+o_h(1).
\]
Together with compactness of \(P_\delta\) for fixed \(\delta\), this yields relative compactness of bounded-energy sequences. A discrete translation estimate on coordinate patches is another possible route.

**(A4) Weak liminf mechanism.** Construct a discrete gradient or flux reconstruction \(G_hu_h\) bounded in \(L^2\) whenever \(\|u_h\|_{H_h}^2+\mathcal E_h(u_h)\) is bounded. Show that weak limits of these reconstructed gradients are the weak gradient of the \(L^2\) limit, and use lower semicontinuity of the uniformly elliptic continuum energy:
\[
\mathcal E(u)\leq\liminf_{h\to0}\mathcal E_h(u_h).
\]
This is the central M1 step. A second-moment Taylor expansion on smooth functions does not prove it for arbitrary weakly convergent sequences.

**(A5) Recovery sequence.** First take \(u\in C^\infty(M)\) and use \(J_hu\), proving strong convergence and energy convergence. Then extend to every \(u\in H^1(M)\) by density and a diagonal argument, with uniform energy bounds. This gives M2.

**(A6) Boundary compatibility.** If \(M\) has a boundary, specify the discrete boundary treatment and prove that the reconstruction has the intended trace behaviour. Neumann, Dirichlet, and mixed conditions lead to different form domains and cannot be interchanged.

If (A1)–(A6) are proved with the chosen varying-space identifications, they provide the route to generalized Mosco convergence. The exact theorem statement must cite the applicable varying-Hilbert-space framework and verify its hypotheses.

## 6. A separate compactness theorem is needed for spectral convergence

Mosco convergence gives the appropriate strong-resolvent/semigroup convergence under the varying-space framework. It does not alone imply convergence of isolated eigenvalues with multiplicity.

For a compact \(M\), establish:
1. compactness of \(H^1(M)\hookrightarrow L^2(M)\);
2. the uniform discrete Rellich estimate (A3);
3. collective compactness of the identified resolvents, or a suitable generalized norm-resolvent estimate.

Then apply the min–max principle and spectral projection estimates to isolated finite-multiplicity eigenvalue clusters. Record separately convergence of eigenvalues, multiplicities, and eigenspaces. For a noncompact target, replace global compactness with localization/tightness and state how essential spectrum is treated.

## 7. What changes for higher-degree discrete de Rham/Hodge complexes?

The scalar graph form is only the degree-zero problem. For a cubical cochain complex, specify
\[
C_h^0\xrightarrow{d_h^0}C_h^1
\xrightarrow{d_h^1}\cdots\xrightarrow{d_h^{d-1}}C_h^d,
\qquad d_h^{k+1}d_h^k=0,
\]
with degree-dependent inner products and adjoints. The \(k\)-form energy is
\[
\mathcal Q_h^k(\omega)
=\|d_h^k\omega\|_{H_h^{k+1}}^2
+\|(d_h^{k-1})^*\omega\|_{H_h^{k-1}}^2.
\]
A higher-degree convergence theorem needs commuting or asymptotically commuting cochain maps, uniform boundedness of the cochain projections, convergence of the exterior derivatives and adjoints (or a direct form-convergence proof), and control of harmonic subspaces. Scalar Markovianity arguments do not transfer automatically to \(k\geq1\).

For non-affine cell maps, the pullback of differential forms and the Piola-type transformations must be stated explicitly. The commuting property is a structural requirement, not a consequence of merely mapping cube vertices to curved vertices.

## 8. Falsifiable milestones for the RGS–PRISM programme

| Milestone | Required artifact | Acceptance criterion |
|---|---|---|
| M0 — combinatorial refinement | Generator for \(G_r\), incidence data, deterministic indexing | Counts, degrees, face incidences and boundary identities verified for several \(r\) |
| M1 — geometric realization | Coordinates, cell maps \(F_{h,Q}\), dual cells and metric | Nondegeneracy, face matching, coverage and Jacobian bounds checked |
| M2 — measure and weights | \(m_h\), \(b_h\), boundary convention | Positivity, uniform ellipticity and intrinsic-metric estimates verified |
| M3 — identification | \(I_h,J_h\), cochain maps if needed | Norm consistency and commuting/consistency residuals converge |
| M4 — smooth consistency | Taylor/metric expansion and tests | Energy error converges at the predicted order for a dense smooth test family |
| M5 — compactness | Discrete Rellich/translation estimate | Constants independent of refinement; no unresolved mass escape |
| M6 — Mosco proof | M1 weak liminf and M2 recovery proof | Both conditions proved for arbitrary admissible sequences/functions |
| M7 — spectral theorem | Resolvent compactness and min–max argument | Isolated eigenvalue clusters, multiplicities and projections controlled |
| M8 — Hodge extension | Cochain norms, pullbacks, commuting maps | Separate proof in each degree |

The first implementation should generate the flat product refinement \(G_r\) above and verify M0–M4. Only then should the curved maps and metric tensors be introduced. This prevents geometric distortion, combinatorial refinement, and operator scaling from being debugged simultaneously.

## 9. Questions for external mathematical review

The following are the questions to put to specialists. They are deliberately narrow and answerable.

1. **Non-affine maps:** Is uniform rescaled \(C^{1,1}\) control plus uniform Jacobian ellipticity sufficient for the chosen finite-volume consistency estimate, or is a stronger face-orthogonality condition needed?
2. **Positive graph weights:** For a prescribed pullback metric with off-diagonal terms, what local stencil conditions guarantee a nonnegative conductance representation with the correct second moment?
3. **M1:** Which discrete gradient/flux reconstruction gives the cleanest weak-liminf proof on curved cubical partitions?
4. **Compactness:** Is a patchwise translation estimate or a discrete Rellich theorem the most robust route when the cell maps vary with \(h\)?
5. **Varying spaces:** Which precise Kuwae–Shioya formulation best fits cell-average maps and the proposed vertex-dual-cell reconstruction?
6. **Hodge extension:** Which commuting projection and metric-dependent cochain inner product should be used to retain the cubical de Rham complex under non-affine refinement?

A useful response should identify a missing hypothesis, counterexample, reference theorem with matching assumptions, or a proof route—not merely state that the problem is difficult.

## 10. Evidence and non-claims

| Statement | Status |
|---|---|
| \(G_r=C_{64r}\square C_{6r}^{\square3}\square C_{5r}\) has \(69120r^5\) vertices and degree 10 | Exact combinatorial consequence of the definition |
| Flat product-grid mass and conductance scaling | Explicit model definition |
| Smooth-mode consistency for the flat product grid | Standard finite-difference calculation; to be covered by a dedicated multidimensional test |
| Curved non-affine RGS–PRISM cell maps exist with the required uniform bounds | Open |
| Positive conductances reproduce a general curved metric tensor | Open; requires stencil/orthogonality analysis |
| Generalized Mosco convergence for the proposed RGS–PRISM sequence | Open |
| Uniform discrete Rellich estimate for that sequence | Open |
| Spectral convergence with multiplicities and eigenspaces | Open pending compactness/resolvent proof |
| Higher-degree de Rham/Hodge convergence | Open |

## 11. Suggested references

These references provide frameworks or nearby methods; none is cited as proving the RGS–PRISM result.

- K. Kuwae and T. Shioya, “Convergence of spectral structures: a functional analytic theory and its applications to spectral geometry,” *Communications in Analysis and Geometry* 11 (2003), 599–673. Varying-Hilbert-space convergence of spectral structures and forms.
- M. Keller, D. Lenz and R. K. Wojciechowski, *Graphs and Discrete Dirichlet Spaces*, Springer, 2021. Weighted graph forms, intrinsic metrics and operator realizations.
- M. Keller, “Intrinsic Metrics on Graphs: A Survey,” arXiv:1407.7453. Intrinsic metrics and geometric control on graphs.
- D. Arnold, R. Falk and R. Winther, “Finite element exterior calculus: from Hodge theory to numerical stability,” *Bulletin of the AMS* 47 (2010), 281–354. Commuting projections and stable discrete de Rham complexes.
- A. Buffa, G. Sangalli and R. Vázquez, “Isogeometric analysis in electromagnetics: B-splines approximation,” *Computer Methods in Applied Mechanics and Engineering* 199 (2010), 1143–1152. Geometric mappings and differential-form-compatible discretization.
- P. D. Lax and R. D. Richtmyer, “Survey of the stability of linear finite difference equations,” *Communications on Pure and Applied Mathematics* 9 (1956), 267–293. Classical consistency/stability perspective; not a substitute for the Mosco proof.

## 12. Reproducibility and contribution protocol

The one-dimensional periodic-cycle calibration remains available:
\`\`\`bash
python -m pytest tests/test_t048_rgs_prism_mosco_calibration.py -q
python -m scripts.rgs_prism_mosco_calibration --n 32 64 128 256 --mode 1
\`\`\`

The flat five-dimensional product refinement now has a lazy generator and a separate M0–M4 regression suite:
\`\`\`bash
python -m pytest tests/test_t048_rgs_prism_product_refinement.py -q
python -m scripts.rgs_prism_product_refinement --levels 1 2 4 8 16
\`\`\`
The generator defines periodic indexing, positive-direction edge iteration, cell masses and direction-dependent conductances without materializing the full graph. Its Fourier-mode energy audit checks fixed smooth modes on the flat unit five-torus. This is a finite-grid consistency calibration only: it does not prove the weak-liminf condition for arbitrary sequences, a recovery theorem, uniform discrete compactness, or convergence for curved/non-affine cells.

External reviewers are invited to comment on one numbered question in §9. If a correction is adopted, the corresponding hypothesis, proof step, script/test (where applicable), and evidence status will be updated together.

**Bottom line:** the first mathematically controlled object is the flat five-cycle-product refinement. The curved, non-affine RGS–PRISM limit is the target theorem, not a result already obtained.
