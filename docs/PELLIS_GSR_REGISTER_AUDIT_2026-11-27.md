# Independent mathematical audit — Pellis / GSR register (PEL-01–PEL-11)

**Date:** 27 November 2026  
**Repository:** `fabianleonaressi95/theorem`  
**Scope:** direct review of the PEL register against the GSR preprint and repository records T138, T150, T151, S013, T119, T032, T034, T144, the H4 audit, and the Fibonacci/Q6 bridge.  
**Classification:** audit report, not a new physical theorem.  
**Overall result:** the register is structurally sound. Two technical wording defects are corrected in this branch. No PEL item is promoted to solved.

## 1. Executive findings

1. The dependency logic is correct: the physical state must be selected independently before an expectation can count as a prediction; the operator/domain must be fixed before its spectral measure is physically meaningful; the continuum claim is a separate theorem.
2. T151 overstated the countable-spectrum result. For a countably infinite spectrum, attainable expectations are probability barycentres; their closure is the closed convex hull. The set need not be closed. Example: \(\lambda_n=1/n\) gives strictly positive expectations, although zero is in the closed convex hull.
3. T150 §9 mislabeled the ambient group. The displayed reflection \(\operatorname{diag}(1,1,-1)\) has determinant \(-1\); the rotation-reflection group is a copy of \(D_3\) in \(O(3)\), not a subgroup of \(SO(3)\). Its proper rotation subgroup \(C_3\) lies in \(SO(3)\).
4. PEL-08 is correctly labelled “partly established / bridge open”: S013 supplies exact Reynolds/Peter–Weyl multiplicity formulas, including the left-\(2I\) scalar spectrum, while T119/T144 record exact group and invariant data. None derives the Pellis exponents or resonance weights.
5. The H4 audit is adjacent evidence, not a solution of a PEL item. Its \(\sqrt3\) and \(\varphi\) examples occur in different actual elements; the no-mixed-element census remains numerical pending exact class certification.

## 2. PEL-by-PEL audit

| ID | Verdict | Mathematical basis and boundary |
|---|---|---|
| PEL-01 | **OPEN — correct** | The preprint explicitly constructs expectation values by choosing modal weights proportional to desired coefficients and normalizing. This is representability/inverse design, not an independent derivation. |
| PEL-02 | **OPEN — correct; refine subclaims** | For \(R_n=R_0\varphi^{-n}\), surface area and volume scale exactly as \(\varphi^{-2n}\) and \(\varphi^{-3n}\). That dimensional scaling is valid. The identification with contributions to \(\alpha^{-1}\), and especially the \((3\varphi)^{-5n}\) wave correction, is not derived from a completed field equation or mode calculation in the inspected source. |
| PEL-03 | **OPEN — correct** | The coefficient 360 appears in the target expression, but the inspected derivation does not establish a unique geometric, group-theoretic, or measure-theoretic count that forces it. |
| PEL-04 | **OPEN — correct** | The paper introduces a formal mode-space operator and ansatz, but does not close the Hilbert-space measure, dense domain, self-adjoint realization, boundary conditions, and complete spectral data as one specified operator. |
| PEL-05 | **OPEN — highest priority justified** | Modal weights may be chosen to reproduce Pellis coefficients. The later variational section leaves shell energies and couplings as model choices and discusses target-weight penalties/inverse design. No target-independent, geometry-derived functional with a proved unique ground state is supplied. |
| PEL-06 | **OPEN — correct** | The scale \(s=2\ln\varphi\) is a proposed choice; the inspected source gives no independent extremality or uniqueness condition selecting it. |
| PEL-07 | **OPEN — correct** | The series \((1+t^{30})/((1-t^{12})(1-t^{20}))\) and degrees 12, 20, 30 are exact for the defining \(2I\)-action on \(\mathbb C^2\) (T144). No equivariant map or selection theorem deriving exponents 2, 3, 5 follows from those degrees alone. |
| PEL-08 | **PARTLY ESTABLISHED / BRIDGE OPEN — correct** | S013 proves the Reynolds formula for finite \(SO(4)\)-actions and the Peter–Weyl formula. For the left binary-icosahedral action it records \(d_\ell=(\ell+1)c_\ell\), with \(c_\ell\) from the exact invariant series. T119/T144 supply additional group/Molien data. No resonance selection rule or map to Pellis coefficients is established. |
| PEL-09 | **FINITE ALGEBRA AVAILABLE; PHYSICAL OPERATOR OPEN — correct** | T138 proves a specific symmetric 6×6 matrix splitting into 3+3 eigenspaces. T150 proves a six-state \(D_6\)-set correspondence and a two-sheet/three-mode representation factorization. The Fibonacci/Q6 note gives a neck factorization only under its stated matching convention. These are distinct finite constructions, not a common physical Hilbert space or self-adjoint continuum operator. |
| PEL-10 | **OPEN — correct; terminology corrected** | T150 proves a finite dihedral action and a three-mode permutation representation. Its \(D_3\) realization in §9 lies in \(O(3)\), since one generator is an improper reflection. It is not full \(SO(3)\) symmetry. Equality of operator blocks would require an actual irreducible \(SO(3)\) vector action and strong commutation/domain/boundary invariance. |
| PEL-11 | **OPEN — correct** | The finite graph, orbit, and representation identities do not supply a refinement family, Hilbert-space identifications, Mosco/strong-resolvent convergence, gauge-covariant continuum degrees of freedom, or uniform estimates. |

## 3. Corrections applied in this branch

### 3.1 T151 — countable-spectrum expectation range

For finite \(I\), attainable expectations are exactly \(\operatorname{conv}\{\lambda_i\}\). For countably infinite \(I\), they are
\[
\mathcal E_G=\left\{\sum_iw_i\lambda_i:w_i\ge0,\sum_iw_i=1\right\},
\qquad
\overline{\mathcal E_G}=\overline{\operatorname{conv}\{\lambda_i\}}.
\]
For \(\lambda_n=1/n\), zero is a limit point but is not attained. T151 has been amended; its finite-dimensional non-uniqueness argument and the source-level inverse-design conclusion remain valid.

### 3.2 T150 §9 — ambient group

The displayed matrices satisfy
\[
\det(W_3C_3W_3^T)=+1,\qquad
\det(W_3F_3W_3^T)=-1.
\]
The generated action is orthogonal but not orientation-preserving. T150 now identifies it as the natural \(\ell=1\) representation of \(O(3)\) restricted to a planar-triangle \(D_3\) subgroup. The exact two-sheet/three-mode factorization is unchanged.

## 4. Source audit of the GSR preprint

The inspected Pellis preprint supports these conclusions:

- It explicitly says modal weights can be chosen proportional to desired Pellis coefficients and normalized to encode the target series as an expectation.
- It says surface/volume coefficients still need physical or experimental justification or selection rules.
- It introduces a variational Hamiltonian with shell energies and couplings, but presents these as suggested choices/ansätze rather than deriving them uniquely from a fixed geometric action.
- It discusses a penalty term favoring target block weights as an inverse-design device.
- It assigns surface, volume, and wave-correction interpretations to the scaling terms, but the fifth-power correction is not obtained from a completed boundary-value/eigenmode derivation in the inspected text.
- The operator discussion does not provide a complete self-adjoint specification sufficient to derive a unique physical spectral measure.

Thus the register's central distinction—an expectation can represent a target without the operator predicting it—is supported. This does not rule out a future independently derived variational model.

## 5. Cross-document consistency

- **T138:** exact algebraic 3+3 splitting for its displayed \(C_6\) matrix; no specified \(2I^*\) action or Pellis operator equivalence.
- **T150:** exact six-state \(D_6\)-equivariant orbit map; not an identification of all 64 Q6 states or of the full Q6 graph Laplacian with a physical transfer operator.
- **T151:** countable expectation statement corrected; inverse-design critique remains supported.
- **S013:** distinguishes the two-dimensional \(2I\)-invariant Hilbert series, four-dimensional real Molien series, and harmonic spherical multiplicities. These must not be conflated.
- **T119/T032/T034/T144:** establish group/invariant/character data at their stated scopes. T034 itself conditions its character-table certification on execution of its accompanying tests; do not silently upgrade that test status.
- **H4 audit:** its two representative elements are exact examples, but the no-mixed-element census is an exhaustive floating-point enumeration, not yet an exact conjugacy-class proof.
- **Fibonacci/Q6 bridge:** the trace-map and neck statements retain their hypotheses; a trace orbit alone does not recover individual transfer entries or establish a Pellis intertwiner.

## 6. Final status and next dependency

No PEL item is closed by this audit. The order PEL-05 → PEL-04 → PEL-01–03 → PEL-06 → PEL-07/08 → PEL-09/10 → PEL-11 remains logically sensible. The immediate task is PEL-05: specify a target-independent geometric action and a well-posed self-adjoint selection problem, then prove existence, uniqueness or controlled degeneracy, and derive its state weights without using target coefficients as input.

## 7. Sources and repository records

- Stergios Pellis, *Fine-Structure Constant via the Golden Spheres Resonance*, DOI [10.13140/RG.2.2.35410.00968](https://doi.org/10.13140/RG.2.2.35410.00968), 11 September 2025; SSRN [5473588](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5473588), posted 2 October 2025.
- Repository records audited: T138, T150, T151, S013, T119, T032, T034, T144, `docs/H4_600_CELL_TWO_PLANE_CYCLOTOMIC_AUDIT_2026-11-26.md`, and `docs/PELLIS_FIBONACCI_Q6_TWO_SHEET_BRIDGE.md`.
