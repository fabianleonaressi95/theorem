# Theorematic foundations: cubical de Rham, Herasymov parity maps, and FEEC

**Status.** This document separates proved statements, finite exact audits, conditional theorems, and open analytical problems. A passing program is not, by itself, a proof of a universal mathematical statement.

## 1. Conventions and basic objects

Let d be 2 or 3, let K_N=[0,N]^d be the unit cubical cell complex, and orient every k-cell by the increasing order of its varying coordinate axes. Write C_k(K_N;Z) for its cellular chain group and ∂_k:C_k→C_{k-1} for its cellular boundary. The dual cochain differential is D^k=∂_{k+1}^T in the chosen oriented cell bases.

For a cell map F_K from a reference cell to a physical cell, the pullback metric is
\[
g_K=DF_K^{T}G(F_K)DF_K,
\]
where G is the ambient Riemannian metric. Cell maps are assumed to be sufficiently regular diffeomorphisms on cell interiors, with compatible traces on common faces.

The lowest-order tensor-product cubical de Rham space on the reference cube is
\[
\widehat V^k
=\bigoplus_{|I|=k}
\left(\bigotimes_{j\notin I}Q_1(\widehat x_j)\right)
\otimes
\left(\bigotimes_{i\in I}Q_0(\widehat x_i)\right)
\,d\widehat x^I.
\]
Here I=(i_1<...<i_k), Q_0 means constant dependence in active axes, and Q_1 means degree at most one in each fixed axis. The canonical degrees of freedom are oriented face integrals (point evaluation for k=0).

## 2. Exact algebraic theorems

### Theorem 2.1 — Boundary-of-boundary identity

For every oriented cubical cell complex,
\[
\partial_{k-1}\partial_k=0,\qquad D^{k+1}D^k=0.
\]

**Proof.** Every codimension-two face of an oriented k-cube is obtained by fixing two distinct coordinate axes. It occurs twice in the iterated boundary, once for each order of deleting those axes. The two signs differ by one transposition and cancel. No other codimension-two face occurs. Dualizing gives the cochain identity. \(\square\)

A zero numerical residual is an implementation check of this identity, not its proof.

### Theorem 2.2 — Exact cubical subdivision chain map

Let S_k:C_k(K_N;Z)→C_k(K_{2N};Z) send an oriented coarse cell
\[
c=(v;i_1,\ldots,i_k),\qquad i_1<\cdots<i_k,
\]
to the sum of its 2^k fine k-subcells:
\[
S_k(c)=
\sum_{\epsilon\in\{0,1\}^k}
\left(2v+\sum_{r=1}^k\epsilon_r e_{i_r};
i_1,\ldots,i_k\right).
\]
Coordinates not in the active axes are doubled without an offset. Every subcell inherits the orientation of c. Then
\[
\boxed{\partial_{2N}S_k=S_{k-1}\partial_N.}
\]

**Proof.** Apply the boundary formula to every fine subcell. A face internal to the coarse cell is shared by exactly two fine subcells, with opposite induced orientations, and cancels. The remaining faces lie on the boundary of the coarse cell. For each coarse boundary face, its fine subdivision is exactly the corresponding term of S_{k-1}(∂_N c), with the same induced orientation. Thus the chains agree term by term. Extend by linearity. \(\square\)

### Theorem 2.3 — Naturality under cubical signed permutations

Let T(x)=Px+b be a symmetry of the cubical grid, where P is a signed permutation matrix and b is the corresponding cube offset. Let T_N,T_{2N} be its induced chain maps. Then
\[
\boxed{T_{2N}S_k=S_kT_N.}
\]

**Proof.** A signed permutation sends each coarse cube to a coarse cube and permutes its active coordinate axes. It sends the 2^k fine subcells of a coarse cell bijectively to the 2^k fine subcells of its image. The orientation sign induced by the permutation is the same on the coarse cell and on each fine subcell. Hence both sides have identical cells and coefficients. \(\square\)

This concerns the standard cubical subdivision operator. It does not identify a mixed parity-selected voxel recursion with that operator.

## 3. Herasymov parity-selected affine maps

### Definition 3.1 — Parity-cell affine assignment

Let Δ={0,1}^3. For every δ in Δ, assign an affine map
\[
\Phi_\delta(x)=A_\delta x+b_\delta
\]
on [0,N]^3, where A_δ is a signed permutation matrix and b_δ is the corresponding cube-isometry offset. The parity class δ labels an interleaved sublattice, not a contiguous octant.

The affine extension uses the continuous reflection offset N, not the voxel-index offset N-1. The latter acts on unit-cell indices; the former acts on cell vertices.

### Theorem 3.2 — Necessary and sufficient criterion for affine shared-face conformity

Assume N≥2. Require the affine traces selected by neighboring parity classes to agree pointwise on every internal shared face, for every parent-cell index and every tangential parity patch. Then the assignment is face-conforming if and only if
\[
\Phi_\delta=\Phi_{\delta+e_i}
\quad\text{for every }\delta_i=0,\ i\in\{1,2,3\}.
\]
Equivalently,
\[
\boxed{A_\delta=A,\quad b_\delta=b
\quad\text{for all }\delta\in\Delta.}
\]

**Proof.** Fix a parity edge (δ,δ+e_i), and put Ψ(x)=Φ_δ(x)-Φ_{δ+e_i}(x)=Dx+c. The shared faces normal to axis i contain relatively open two-dimensional patches in at least two distinct parallel planes, because N≥2 and the condition is imposed for every parent index. If the traces agree pointwise, Ψ vanishes on each such patch. Vanishing on a relatively open patch forces the two tangential columns of D to vanish and fixes the affine offset on that plane. Vanishing on a second parallel plane forces the remaining normal column to vanish and then c=0. Thus D=0 and c=0. Conversely, equal affine maps have equal restrictions on every common face. The parity graph is the connected three-dimensional cube graph, so equality on every parity edge implies that all eight maps coincide. \(\square\)

**Scope.** This theorem is necessary and sufficient for the declared cellwise affine geometric interpretation. It does not prove that a voxel-value recursion, without an explicit geometric cell map, defines such a mesh. Geometric trace conformity alone does not imply scalar continuity, conservation, a chain map, or FEEC stability.

### Proposition 3.3 — Geometry/scalar separation for the complement bit

Suppose two source modes induce the same coordinate map but differ only by Boolean complementation of the scalar value. Their geometric face traces agree, while their scalar actions need not agree.

**Proof.** The coordinate map is identical by hypothesis, so its restrictions to every face are identical. Complementation acts on the value variable and not on the coordinate map. Any scalar matching condition is an additional constraint. \(\square\)

### Corollary 3.4 — Uniform coordinate-map class is necessary

Under Theorem 3.2, all eight selected rules must belong to one coordinate-map equivalence class. Modes differing only by a scalar complement may remain distinct if that bit leaves the coordinate map unchanged.

The exhaustive source-mode enumeration is a finite verification of the mode classification and its multiplicities. The general conformity conclusion follows from Theorem 3.2, not from enumeration alone.

## 4. Pullback FEEC and mass matrices

### Lemma 4.1 — Commutation of exterior derivative and pullback

For a sufficiently regular diffeomorphism F and a sufficiently smooth differential form ω,
\[
d(F^*\omega)=F^*(d\omega).
\]

**Proof.** In local coordinates, pullback is composition with F combined with the appropriate minors of DF. Differentiating and using equality of mixed partial derivatives yields the identity. \(\square\)

This explains why the differential is represented by incidence matrices independently of the metric. It does not by itself prove stability or approximation of a projection.

### Corollary 4.1 — Exact commutation of face-integral interpolation

Let \(\pi_h^k\omega\) assign to every oriented k-face \(\sigma\) the integral \(\int_\sigma\omega\), with point evaluation in degree zero. For every smooth k-form \(\omega\), every oriented (k+1)-cell \(\tau\), and the incidence differential built with the standard induced-boundary signs,
\[
(D^k\pi_h^k\omega)(\tau)
=\sum_{\sigma\subset\partial\tau}[\tau:\sigma]\int_\sigma\omega
=\int_{\partial\tau}\omega
=\int_\tau d\omega
=(\pi_h^{k+1}d\omega)(\tau).
\]
Hence \(D^k\pi_h^k=\pi_h^{k+1}d\) exactly whenever the face integrals are exact and the cell complex has compatible oriented traces.

**Proof.** The first equality is the definition of the cellular incidence action; the second is the oriented cubical boundary formula; the third is Stokes' theorem; the final equality is the definition of the next-degree face-integral interpolator. For k=0 this is the fundamental theorem of calculus on each edge. \(\square\)

The repository evaluates these integrals by finite-order Gauss quadrature. Thus the theorem applies to the exact mathematical interpolator; the numerical commutator tests verify its quadrature approximation on the tested forms and meshes.

### Proposition 4.2 — Positive definiteness of the exact local FEEC mass

Assume F_K is a diffeomorphism and G is uniformly positive definite on the physical cell. Let {φ_a} be a linearly independent local basis of V^k(K). Then the exact Gram matrix
\[
(M_K^k)_{ab}=\int_{\widehat K}
\langle\phi_a,\phi_b\rangle_{\Lambda^k(g_K^{-1})}
\sqrt{\det g_K}\,d\xi
\]
is symmetric positive definite.

**Proof.** Symmetry follows from symmetry of the induced inner product on the exterior power. For any nonzero coefficient vector z, u_z=Σ_a z_a φ_a is not identically zero by linear independence. Positive definiteness of g_K induces a positive-definite inner product on every exterior power, so |u_z|² times the positive volume density is positive on a set of positive measure. Hence z^T M_K^k z>0. \(\square\)

For numerical quadrature, positive definiteness additionally requires the quadrature rule to be sufficiently positive and non-degenerate on the finite-element space.

### Proposition 4.3 — Discrete codifferential is the mass adjoint

Let D^k:V_h^k→V_h^{k+1} have coefficient matrix D^k and let M_k,M_{k+1} be symmetric positive-definite mass matrices. Then
\[
\boxed{\delta_h^{k+1}=M_k^{-1}(D^k)^TM_{k+1},}
\]
and
\[
\langle D^k u,v\rangle_{M_{k+1}}
=\langle u,\delta_h^{k+1}v\rangle_{M_k}
\]
for all coefficient vectors u,v.

**Proof.** The right side equals u^T M_k M_k^{-1}(D^k)^T M_{k+1}v=u^T(D^k)^TM_{k+1}v, which is the left side. Positive definiteness makes the adjoint unique. \(\square\)

### Proposition 4.4 — Correct top-degree primal DEC weight

For a top-degree cochain whose degree of freedom is the integral of a d-form over a primal d-cell K, the diagonal primal DEC Hodge weight is
\[
M_d(K)=\frac{\operatorname{vol}_g(K^*)}{\operatorname{vol}_g(K)}
=\frac{1}{\operatorname{vol}_g(K)}
\]
when the dual of a top cell is a point with unit zero-volume.

**Proof.** The diagonal primal/dual Hodge star is defined by the dual-to-primal volume ratio. A point has zero-dimensional volume one, leaving the reciprocal primal volume. \(\square\)

The historical assignment M_d(K)=vol_g(K) is a reproducibility variant, not this standard top-degree primal DEC weight. These conventions must remain distinct in spectral comparisons.

## 5. Conditional analytic theorem: sufficient conditions for convergence

The following is a theorem template, not a claim that the benchmark has verified its hypotheses.

### Theorem 5.1 — Abstract Mosco convergence of discrete Hodge energies (conditional)

Let H be a Hilbert space. After reconstruction into H, regard each discrete energy as an extended-valued form q_n:H→[0,∞] (with q_n(u)=+∞ outside the reconstructed discrete domain), and let q:H→[0,∞] be a densely defined, closed, nonnegative form. Suppose:

1. **Weak liminf inequality:** whenever u_n converges weakly to u in H, q(u)≤liminf_n q_n(u_n).
2. **Strong recovery sequence:** for every u in the domain of q, there exist u_n converging strongly to u in H with limsup_n q_n(u_n)≤q(u).
3. **Closedness:** every q_n is also a densely defined, closed, nonnegative form on H.

Then q_n Mosco-converges to q, and the associated nonnegative self-adjoint operators converge in the strong-resolvent sense.

If, in addition, the family is **equicoercive** (bounded energy and bounded H norm imply relative compactness in H), one obtains the compactness input needed for stronger spectral consequences, subject to the relevant spectral-isolation hypotheses.

**Proof.** Conditions 1 and 2 are exactly the weak lower-bound and strong recovery conditions defining Mosco convergence of closed forms. The closed-form representation theorem associates nonnegative self-adjoint operators to q_n and q, and Mosco convergence of closed nonnegative forms implies strong-resolvent convergence. Equicoercivity is an additional compactness property; it is not part of the definition of Mosco convergence itself. \(\square\)
Strong-resolvent convergence alone does not imply norm-resolvent convergence, convergence of individual eigenvalues without compactness, or convergence of harmonic representatives. Those require additional uniform compactness, spectral isolation, and control of kernels.

### Required estimates still absent

For the curvilinear cubical family, a proof would need at least:
- uniform upper and lower bounds on singular values of DF_{K,h}, and compatible face traces;
- reconstruction into a fixed Hilbert complex, uniformly bounded in the relevant graph norms;
- a bounded commuting projection or an equivalent approximation mechanism;
- discrete compactness on discrete co-closed subspaces;
- liminf and recovery-sequence constructions for the actual discrete Hodge energy;
- separate treatment of boundary conditions and harmonic kernels.

Finite refinement tables, positive Jacobian samples, and small commutator residuals are evidence, not substitutes for these estimates.

## 6. Theorem-status ledger

| Result | Status | What is established |
|---|---|---|
| ∂²=0 for cubical incidence | **Proved** | Theorem 2.1; implementation checks are regression tests |
| Standard cubical subdivision is a chain map | **Proved** | Theorem 2.2 |
| Signed-permutation naturality of subdivision | **Proved** | Theorem 2.3 |
| Herasymov affine parity face criterion | **Proved under Definition 3.1** | Theorem 3.2; the geometric interpretation must be supplied |
| Complement bit is geometrically inert | **Proved under same-coordinate-map hypothesis** | Proposition 3.3 |
| Pullback commutes with d | **Proved** | Lemma 4.1 |
| Exact consistent FEEC mass is SPD | **Proved under diffeomorphism/metric hypotheses** | Proposition 4.2 |
| Discrete codifferential formula | **Proved** | Proposition 4.3 |
| Top-degree primal DEC weight | **Proved from primal/dual volume definition** | Proposition 4.4 |
| Flat-grid row-sum lumping identity | **Finite exact audit currently present** | Needs a local tensor-product proof before promotion to theorem |
| FEEC commuting projection boundedness | **Open globally** | Commutation tests do not prove uniform boundedness |
| Discrete compactness on curvilinear refinements | **Open** | No uniform reconstruction/compactness proof yet |
| Mosco convergence | **Open** | Theorem 5.1 gives sufficient conditions, not verified hypotheses |
| Norm-resolvent and spectral convergence | **Open** | Requires stronger compactness and operator estimates |
| Mixed parity recursion is a cubical subdivision | **Not established** | Must construct cell images and prove compatibility with subdivision |

## 7. Orientation audit: convention is consistent

The source-level recheck resolves the previously reported sign discrepancy. In `ddr/mesh.py`, the implemented coefficient is
\[
(-1)^p(2s-1),
\]
where `p` is the zero-based position of the removed axis in the increasing tuple `vary`, and `s=0,1` selects the lower/upper facet. This is exactly the standard cubical boundary coefficient for the orientation \(dx_{i_1}\wedge\cdots\wedge dx_{i_k}\).

In one dimension, the degree-zero nodal basis \((1-x,x)\) has derivatives \((-dx,+dx)\), so the oriented edge incidence row is \((-1,+1)\), which is exactly what the implementation constructs. In higher dimensions, the increasing `vary` tuple used by `face_dofs` fixes the same ordered tangent orientation; the alternating facet sign in `mesh.py` is the boundary orientation induced by that ordered basis.

Consequently the earlier claim that the stored incidence matrices were the negative of the FEEC differential was a stale/source-reading error: the audit document had an extra minus sign in its transcription of the code formula. No sign flip or degree-dependent reorientation is warranted. The exact face-integral interpolator commutes with the incidence differential by Stokes' theorem, provided the geometric cell maps have matching traces and the integrals are evaluated exactly. The implemented Gauss quadrature gives a numerical approximation to those integrals, so the regression commutator remains a quadrature-level check rather than a proof of exact integration for arbitrary non-polynomial data.
## 7. Orientation audit: final disposition

The earlier subsection titled “Mandatory orientation audit before FEEC theorem claims” is superseded and removed. It repeated a preliminary sign-mismatch diagnosis that was corrected by the source-level audit above. The implementation uses the standard cubical boundary coefficient `(-1)^p(2s-1)`, consistently with the increasing active-axis orientation of the face degrees of freedom. No sign flip or degree-dependent reorientation is required. The exact Stokes commutation statement is recorded separately as [T067](../../../theorems/T067-stokes-commuting-cubical-face-integral-interpolation.md); numerical quadrature checks remain finite implementation checks.

## 8. Reproducible checks and their logical scope

The current GitHub Actions workflow exercises compilation, Herasymov symbolic/parity audits, parity shared-face conformity, cubical subdivision/naturality, chain identities, Hodge-degree checks, DEC/FEEC mass comparisons, refinement controls, projection/adjoint smoke tests, and fixed-amplitude curved-map controls.

These checks establish that the listed finite computations ran successfully for their configured inputs. They do not enlarge the quantifiers of Theorems 2.1–5.1 and do not close the open analytic obligations in Section 6.


## 9. Uniform projection stability

The local metric/mass equivalence under uniform bi-Lipschitz cell scaling, the sufficient criterion for uniformly bounded commuting projections on \(H\Lambda^k\), and the obstruction for raw face interpolation are proved and separated in [PROJECTION_STABILITY_THEOREM.md](PROJECTION_STABILITY_THEOREM.md). The theorem is conditional: the benchmark does not yet construct the required smoothed commuting projection or prove its uniform graph bound.
