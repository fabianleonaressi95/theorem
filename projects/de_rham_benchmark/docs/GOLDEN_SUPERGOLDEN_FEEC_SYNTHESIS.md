# Golden and supergolden scaling in curvilinear de Rham–FEEC convergence

**Status:** exact algebraic scaling identities and a conditional refinement framework. This note does not claim that the repository's current meshes satisfy a golden/supergolden Mosco theorem.

## 1. Purpose and logical boundary

The golden ratio and the supergolden constant are used here as exact algebraic refinement parameters, not as decorative constants and not as substitutes for FEEC stability or compactness.

Set
\[
\varphi=(1+\sqrt5)/2,\qquad \varphi^2=\varphi+1,
\]
and let \(\psi>1\) be the real root of
\[
\psi^3-\psi^2-1=0,\qquad \psi^3=\psi^2+1.
\]
Numerically, \(\psi\simeq1.465571231876768\). The first identity is quadratic over \(\mathbb Q\); the second is cubic. They belong to different number fields and must not be conflated.

The useful simplification is to encode a self-similar refinement schedule by one fixed algebraic unit \(\lambda>1\). The analytic proof is then stated once for general \(\lambda\), and specialized to \(\varphi\) or \(\psi\). The constants in geometric and FEEC estimates remain explicit proof obligations.

## 2. Exact algebraic refinement laws

### 2.1 Golden recurrence

Define \(F_0=0,F_1=1\) and
\[
F_{n+2}=F_{n+1}+F_n.
\]
Then
\[
F_n=\frac{\varphi^n-(-\varphi^{-1})^n}{\sqrt5},
\qquad F_{n+1}/F_n\to\varphi.
\]
This is an exact integer recurrence; its approximation error is controlled by the conjugate \(-\varphi^{-1}\).

### 2.2 Supergolden recurrence

Define \(S_0=0,S_1=0,S_2=1\) and
\[
S_{n+3}=S_{n+2}+S_n.
\]
Its characteristic polynomial is \(x^3-x^2-1\). If \(\psi\) is its dominant real root and \(\psi_2,\psi_3\) are the other roots, then
\[
S_n=c_\psi\psi^n+O(\rho^n),\qquad
\rho=\max(|\psi_2|,|\psi_3|)<\psi,
\]
with nonzero dominant coefficient \(c_\psi\). In particular, \(S_{n+1}/S_n\to\psi\). This follows from the spectral decomposition of the companion matrix.

These are algebraic facts. They do not by themselves imply a mesh approximation theorem.

## 3. General lambda-refinement lemma

Let \(\lambda>1\) be fixed and set \(h_n=h_0\lambda^{-n}\). Then
\[
h_{n+1}=\lambda^{-1}h_n,\qquad h_n^{-2}=h_0^{-2}\lambda^{2n}.
\]
For first-order differential energies, the natural scale is \(h_n^{-2}\). For degree-\(k\) FEEC Gram matrices on shape-regular cells in dimension \(d\), the pullback scale is \(h_n^{d-2k}\).

**Lemma 3.1 (scale bookkeeping).** Suppose the cell family is uniformly shape regular and its geometry maps satisfy uniform scaled derivative bounds. If the cell diameter is comparable to \(h_n\), then
\[
c h_n^{d-2k}\|\widehat v\|^2
\leq (\!M_{K,n}^k\widehat v,\widehat v\!)
\leq C h_n^{d-2k}\|\widehat v\|^2,
\]
with constants independent of cell \(K\) and level \(n\), provided the ambient metric is uniformly elliptic.

**Proof.** Write \(DF_{K,n}=h_n A_{K,n}\) after reference-cell scaling. Uniform shape regularity gives uniform upper and lower singular-value bounds for \(A_{K,n}\). The \(k\)-form Gram density contains \(\sqrt{\det g}\,\Lambda^k(g^{-1})\); its eigenvalues scale as \(h_n^{d-2k}\), while its dimensionless part is bounded above and below by the singular-value and metric bounds. Integration over the fixed reference cell gives the estimate. \(\square\)

The lemma is independent of whether \(\lambda=\varphi\), \(\lambda=\psi\), or another fixed value. The algebraic constant selects the refinement schedule; shape regularity supplies the analytic estimate.

## 4. Why the two constants define alternative isotropic schedules

Use the two schedules as separate families:
\[
h_n^{(\varphi)}=h_0\varphi^{-n},\qquad
h_n^{(\psi)}=h_0\psi^{-n}.
\]
Each has a constant scale ratio and can satisfy the same shape-regularity assumptions.

Do not assign \(h_{1,n}=\varphi^{-n}\) and \(h_{2,n}=\psi^{-n}\) to different coordinate directions while claiming uniform shape regularity: the aspect ratio contains \((\varphi/\psi)^n\), which diverges because \(\varphi\ne\psi\). That construction is anisotropic and requires a different theorem with directional regularity and anisotropic compactness estimates.

The clean comparison is two parallel refinement families, not an unqualified mixed golden/supergolden mesh.

## 5. FEEC structure is unchanged by the algebraic scale

For each \(\lambda\in\{\varphi,\psi\}\), let \(\mathcal T_n^{(\lambda)}\) be a conforming cubical mesh with cell diameter comparable to \(h_n^{(\lambda)}\). Define \(V_n^k\) as the mapped lowest-order tensor-product cubical \(Q_1^-\Lambda^k\) space. The covariant pullback obeys
\[
F_{K,n}^*(d\omega)=d(F_{K,n}^*\omega).
\]
The incidence matrices must be the oriented cellular coboundary matrices and agree exactly with the exterior derivative of the local basis. The sign mismatch recorded in the independent audit must be resolved before a commuting diagram is asserted.

The consistent mass is
\[
(M_{K,n}^k)_{ab}=\int_{\widehat K}
\langle F_{K,n}^*\phi_a,F_{K,n}^*\phi_b\rangle_{g_n}\,dV_{g_n}.
\]
Uniform ellipticity, geometry regularity, and quadrature consistency are required uniformly in \(n\). Neither \(\varphi\) nor \(\psi\) repairs a wrong orientation, a nonconforming trace, or an unstable projection.

## 6. Conditional golden/supergolden Mosco theorem

**Theorem 6.1 (two algebraic self-similar FEEC families).** Fix \(\lambda\in\{\varphi,\psi\}\) and let \(h_n=h_0\lambda^{-n}\). Assume:

1. **Geometric realization:** \(\mathcal T_n\) is a conforming cubical refinement of a fixed compact Lipschitz manifold/domain, with maximum cell diameter comparable to \(h_n\).
2. **Uniform shape regularity:** scaled cell maps and inverses have uniform \(W^{r,\infty}\) bounds at the regularity required by FEEC approximation estimates; neighboring face maps and orientations agree.
3. **Metric convergence:** ambient metrics are uniformly elliptic and converge in \(L^\infty\), or in a stronger topology sufficient for mass-pairing convergence.
4. **Conforming subcomplex:** mapped tensor-product spaces form a subcomplex with fixed boundary conditions, and incidence matrices represent the actual exterior derivative in the declared oriented DoF bases.
5. **Uniform mass consistency:** exact or quadrature Gram matrices are uniformly coercive and bounded, and quadrature error tends to zero uniformly in the mesh.
6. **Commuting projections:** genuine projections \(\pi_n^k\) satisfy \(d\pi_n^k=\pi_n^{k+1}d\), are uniformly bounded in graph norms, and converge on a dense core.
7. **Adjoint graph convergence:** identified discrete codifferentials satisfy the weak graph lower-bound property and admit a simultaneous strong recovery sequence with the primal differentials.
8. **Discrete compactness:** bounded identified Hodge-energy sets are relatively compact in the common \(L^2\) space; a uniform discrete Gaffney/Rellich estimate is one sufficient route.
9. **Harmonic topology and gap:** discrete cohomology dimensions agree with continuous Betti numbers and a uniform positive gap holds on the orthogonal complement of discrete harmonic forms.

Then, degree by degree, discrete Hodge quadratic forms Mosco-converge to the continuum Hodge form and the associated resolvents converge strongly. Under assumption 8, identified resolvents converge in norm and isolated finite-multiplicity spectral clusters and spectral projectors converge. Under assumptions 8–9, harmonic subspaces converge and have the correct dimensions for all sufficiently large \(n\).

**Proof.** Assumptions 1–5 provide uniform geometric and Hilbert-norm equivalence. Assumption 6 supplies primal cochain approximation but is not a substitute for adjoint convergence. Assumption 7 gives the separate graph lower bound and simultaneous recovery sequence for \(d\) and \(\delta\), hence both Mosco conditions. The representation theorem for closed nonnegative forms yields strong resolvent convergence. Assumption 8 supplies collective compactness, upgrading strong resolvent convergence to norm-resolvent convergence under the stated identifications and giving convergence of isolated spectral clusters. Assumption 9 prevents a change in zero-eigenspace dimension and, with the gap, isolates the harmonic cluster. Spectral-projector convergence then gives convergence of harmonic subspaces. \(\square\)

**Status:** conditional theorem. The nine analytic/topological assumptions are not proved for the repository's current benchmark.

## 7. What the algebraic constants genuinely simplify

1. **One scale parameter:** prove analytic estimates for a general fixed \(\lambda>1\), then instantiate \(\lambda=\varphi\) and \(\lambda=\psi\).
2. **Exact refinement bookkeeping:** use integer recurrences rather than rounded floating-point scale ratios.
3. **Independent robustness tests:** compare two refinement schedules with different algebraic rates while holding geometry, FEEC spaces, quadrature policy, and continuum target fixed.
4. **Symbolic coefficient fields:** golden identities can be checked in \(\mathbb Q(\sqrt5)\); supergolden identities in \(\mathbb Q(\psi)\), when those coefficients actually occur.

They do not reduce the number of functional-analytic hypotheses. Neither recurrence proves uniform boundedness of commuting projections, convergence of adjoints, Mosco liminf, recovery, compactness, norm-resolvent convergence, or stability of harmonic kernels.

## 8. A falsifiable refinement law

> **Algebraic self-similar refinement law.** Fix one algebraic unit \(\lambda>1\). At level \(n\), use cell scale \(h_n=h_0\lambda^{-n}\), and normalize first-order energies by \(h_n^{-2}\). A claimed continuum limit should be invariant under replacing the golden schedule by the supergolden schedule, provided the geometric and FEEC hypotheses are held fixed.

This is a falsifiable universality test, not a theorem without the hypotheses above. If the two schedules produce different continuum limits after consistent normalization, the cause must be traced to geometry, quadrature, anisotropy, topology, or a failed uniform estimate—not attributed to the algebraic names of the constants.

## 9. Proof obligations

1. Resolve incidence orientation and test each \(D_k\) against the derivative of every local basis form.
2. Define actual golden and supergolden mesh families on the same compact target; publish cell maps, mesh sizes, and face identifications.
3. Prove uniform scaled-Jacobian bounds and uniform mass equivalence for both families.
4. Construct uniformly bounded commuting FEEC projections on the curvilinear families.
5. Prove separate adjoint graph closure and simultaneous recovery.
6. Prove a uniform discrete Gaffney/Rellich estimate.
7. Establish cohomology matching and a uniform positive gap.
8. Only then state Mosco, norm-resolvent, spectral, and harmonic-kernel conclusions.

## 10. Status ledger

| Statement | Status |
|---|---|
| \(\varphi^2=\varphi+1\), Fibonacci recurrence | **Proved algebraically** |
| \(\psi^3=\psi^2+1\), supergolden recurrence | **Proved algebraically** |
| Scale bookkeeping for \(h_n=h_0\lambda^{-n}\) | **Proved** |
| FEEC mass scaling under uniform shape regularity | **Conditional lemma proved above** |
| Two actual curvilinear mesh families in this repository | **Not yet constructed** |
| Uniform commuting projections on those families | **Open** |
| Adjoint graph convergence / Mosco | **Open** |
| Discrete compactness / norm-resolvent | **Open** |
| Harmonic-kernel stability | **Open** |

## 11. Relation to the independent audit and T048

This note supplements, and does not supersede, the independent de Rham audit. Its findings remain in force: incidence orientation must be reconciled with the FEEC basis; the consistent mass and codifferential formulas are sound under their stated conventions; and convergence machinery is not yet present. The RGS–PRISM changing-space framework in theorem T048 is a separate programme and must not be conflated with this cubical FEEC theorem.
