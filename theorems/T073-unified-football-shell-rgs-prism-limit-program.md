# T073 — Unified football-shell / RGS–PRISM–Q6 limit programme

**Status: OPEN — conditional research programme; no global Γ-convergence theorem is claimed.**  
**Scope:** organise the local barycentric results, the football-shell discretisation, structured deformations, discrete transfer maps and possible operator limits. The local results T068–T072 and S.1–S.11 retain their own proof classifications. None is promoted here into a global limit theorem.

## 1. Geometry, meshes and distinct complexes

Let \(S\subset\mathbb R^3\) be a compact, orientable, embedded, piecewise-\(C^2\) surface representing the football shell. Its panel complex has 60 vertices, 12 pentagons, 20 hexagons and 90 physical panel seams. The fan triangulation has 180 triangular CST facets; the recorded shell discretisation has 92 nodes when panel centres are included.

Let \(\mathcal T_h\) be a conforming triangular refinement of the shell, with maximum element diameter \(h\to0\). Shape regularity alone is not enough for the conclusions below: the geometric approximation, element maps, metric tensors, normals and seam incidence must also be controlled uniformly.

The comparison cubical complex \(Q_6\) has 64 vertices, 192 edges and 240 square 2-cells. The 92-node shell and \(Q_6\) are different complexes. No bijection or canonical identification is inferred from their node counts. Any comparison must use explicitly defined chain or field maps, with stated domains, codomains and norms.

The orientability of the closed embedded shell supplies a global choice of unit normal away from the panel singularities. If the piecewise-\(C^2\) structure has creases, the two one-sided normals and the convention for traces at each crease must be specified; a global orientation does not make the normal continuous across a crease.

## 2. Intrinsic structured-deformation variables

For an \(\mathbb R^m\)-valued deformation \(g\), the intrinsic tangential derivative is a section
\[
\nabla_S g\in L^p(S;T^*S\otimes\mathbb R^m).
\]
The structured-deformation field \(G\) must belong to the same bundle. Only then is
\[
M=\nabla_Sg-G
\]
a well-defined section of \(T^*S\otimes\mathbb R^m\). In a local chart this is represented by an \(m\times2\) matrix; under a change of chart the two factors transform covariantly, so the bundle-valued difference is chart-independent.

A candidate state space is
\[
(g,G)\in SBV(S;\mathbb R^m)\times
L^p(S;T^*S\otimes\mathbb R^m).
\]
Here \(SBV\) on \(S\) must be defined intrinsically, for example through a finite atlas and compatible trace/jump definitions, or through an equivalent ambient formulation. The atlas, transition maps and uniformity required for a family of approximating surfaces \(S_h\) must be stated. This is an obligation, not a result supplied by the Euclidean structured-deformation theorem.

The shell metric is denoted by \(g_S\) (or another unambiguous symbol); it must not be confused with the deformation \(g\) or the structured field \(G\).

## 3. Local Dirichlet–Gamma/Beta moments and what T068/T070 prove

For a triangle \(F\) of area \(A_F\), let \(a_{F,i}>0\), \(S_F=\sum_{i=1}^3a_{F,i}\), \(\lambda_i\) be barycentric coordinates and \(V_F\) the vertex matrix. Define
\[
B_3(a_F)=\frac{\prod_i\Gamma(a_{F,i})}{\Gamma(S_F)},
\qquad Z_F=2A_FB_3(a_F),
\qquad p_{F,i}=\frac{a_{F,i}}{S_F}.
\]
For the Dirichlet probability measure,
\[
C_{F,ij}
=\operatorname{Cov}(\lambda_i,\lambda_j)
=\frac{p_{F,i}\delta_{ij}-p_{F,i}p_{F,j}}{S_F+1}
=\frac{a_{F,i}(S_F\delta_{ij}-a_{F,j})}
{S_F^2(S_F+1)}.
\]
The barycentre and physical covariance are
\[
c_F=V_F^{\mathsf T}p_F,\qquad
\Sigma_F=V_F^{\mathsf T}C_FV_F.
\]
For a scalar- or vector-valued \(u\in C^3\) on a neighbourhood of \(F\), the local Taylor estimate is
\[
\mathbb E_F[u(X)]
=u(c_F)+\frac12D^2u(c_F):\Sigma_F+R_F,
\qquad
|R_F|\le \frac{h_F^3}{6}
\sup_F\|D^3u\|_{\mathrm{op}},
\]
with the unnormalised integral obtained by multiplying by \(Z_F\).

Consequently,
\[
\sum_{F\in\mathcal T_h}Z_F|R_F|
\le \frac{h^3}{6}
\left(\sup_F\|D^3u\|_{\mathrm{op}}\right)
\sum_{F\in\mathcal T_h}Z_F,
\qquad h=\max_Fh_F,
\]
provided the displayed supremum is uniform. This is a conditional summation of the local estimate, not by itself a global convergence theorem. To conclude that the right-hand side tends to zero one must establish a uniform bound on the total weights \(\sum_F Z_F\), as well as the stated uniform derivative bound and admissible control of the Dirichlet parameters.

T068/T070 establish local moment, covariance and Taylor/quadrature statements under their stated hypotheses. They do not establish uniformity for every football refinement, a global surface quadrature theorem, or a Γ-limit.

The derivatives of \(\log B_3\) are expressed through digamma and trigamma functions and encode cumulants of logarithmic barycentric coordinates. Zeta, Bernoulli and Euler–Maclaurin identities may enter asymptotic expansions, but they do not determine mesh-summation correction terms without an explicit refinement and summation rule.

## 4. Candidate discrete energy — constitutive choices remain open

A schematic family may have the form
\[
\begin{aligned}
\mathcal E_h(u_h,g_h,G_h,\theta_h)
={}&\sum_{F\in\mathcal T_h}\int_F
W_F(X,\nabla_Su_h,G_h,\theta_h,\nabla_S\theta_h)\,dA\\
&+\sum_{e\in\mathcal S_h}\int_e
\psi_e([g_h],\nu_e,\theta_h)\,d\mathcal H^1
+\mathcal E_h^{(4)}.
\end{aligned}
\]
This is only a template. The bulk density \(W_F\), seam density \(\psi_e\), fourth-moment term \(\mathcal E_h^{(4)}\), admissible variables and boundary conditions must be specified before a Γ-convergence statement is even a complete mathematical proposition.

In particular, a physical panel seam \(\Gamma_{\rm phys}\) is prescribed geometric data, whereas the jump set \(S_{g_h}\) is part of the variational state. They must not be identified without an explicit modelling choice. A seam term quadratic in the jump is not automatically covered by a theory requiring a one-homogeneous interfacial density.

## 5. Required hypotheses — obligations, not established assumptions

A proof must verify the following items for the actual mesh family and energy.

- **H1 — Surface approximation and geometry.** Specify \(S_h\), element-to-surface maps and comparison maps to \(S\). Require appropriate uniform bi-Lipschitz bounds, convergence of metrics and surface measures, and convergence/control of one-sided normals. Shape regularity alone does not imply all of these.
- **H2 — Mesh and local moments.** Require uniform shape regularity, admissible Dirichlet parameters, bounds on \(Z_F\), barycentres and covariance tensors, and a uniform Taylor remainder estimate. In particular establish \(\sup_h\sum_F Z_F<\infty\) if using the global estimate in §3.
- **H3 — Field compactness.** State the topology and prove uniform bounds sufficient for compactness of \(g_h\) in \(L^1\), weak compactness of \(G_h\) in \(L^p\), and control of the jump measures. A typical sufficient coercivity assumption is
  \[
  W(X,A,B)\ge c_1(|A|^p+|B|^p)-c_2,\qquad p>1,
  \]
  but it is not necessary in this exact form. Control of \(B\) may instead follow from a bound on \(A-B\) together with control of \(A\). A bound on \(A\) alone does not control \(B\).
- **H4 — Bulk/interface relaxation.** State the precise growth, coercivity, measurability, lower-semicontinuity, quasiconvexity and interfacial subadditivity assumptions needed by the chosen relaxation theorem. The Euclidean periodic theorem of Amar–Matias–Morandotti–Zappale (2022) applies under its own hypotheses; it is not automatically a theorem for a compact curved shell.
- **H5 — Seams and jumps.** Fix one seam model (see §7), define whether physical seams are admissible jump locations, and prevent double counting between a seam energy and the jump part of the bulk/interface functional.
- **H6 — Moment and fourth-order consistency.** Prove the required first-, second-, third- and fourth-moment bounds/cancellations for the actual refinement. S.4 (fixed-cloud fourth moment), S.5 (jump fourth moment/Taylor expansion), S.6 (derivative), S.7 (Maxwell obstruction) and S.8 (coframe variation) are distinct results and must not be conflated.
- **H7 — Discrete transfer.** Define each map between \(Q_6\), Kathara and shell chain/field spaces, including domain, codomain, norms and orientation conventions. Prove the relevant chain identities, uniform boundedness and geometric/metric/measure consistency. The finite Gate D chain identities alone do not imply these analytic properties.
- **H8 — Operator and spectral convergence.** If sought, separately specify varying Hilbert spaces, comparison maps, quadratic forms, Mosco convergence, compactness of resolvents and multiplicity control. A chain map or Γ-limit of a non-quadratic energy is not by itself an operator- or spectral-convergence theorem.

## 6. L1–L6: proof obligations and current status

The following are the logical work packages. Their surface versions remain open unless a separate proof is added.

| Lemma | Required statement and missing proof | Status |
|---|---|---|
| **L1 — Compactness** | Prove compactness of \(g_h\) in the declared \(L^1\) topology and weak compactness of \(G_h\) in \(L^p\). This requires coercive bounds, control of the jump measure (typically a uniform \(\mathcal H^1(S_{g_h})\) bound or the precise substitute supplied by the energy), an \(L^1/L^\infty\) bound or normalization, and uniform surface charts/transfer maps. The Euclidean SBV compactness theorem does not automatically supply the uniform statement on varying \(S_h\). | **OPEN on the shell.** Euclidean compactness is established in the relevant classical theory under its hypotheses. |
| **L2 — Localisation and Radon measure** | Show that the limiting set function on open subsets of \(S\) is finite, increasing and suitably subadditive, and verify the De Giorgi–Letta/Fonseca–Malý hypotheses in the intrinsic surface topology. The local compact-space measure argument is potentially transferable, but the required nested subadditivity and seam conventions must actually be checked. | **OPEN for this functional on \(S\).** General measure-representation machinery is available; its hypotheses have not been verified here. |
| **L3 — Relaxation and cell density** | Define the local blow-up/cell problem, prove existence of the limiting density, and establish independence from charts and local frames. The periodic cell formula in Euclidean space cannot simply be copied to a general compact surface, which has no global translation group. The effective density may depend on position, tangent plane and curvature. | **OPEN.** No intrinsic cell formula or chart-independence proof is supplied. |
| **L4 — Liminf inequality** | For the declared convergence, prove \(\mathcal E(g,G)\le\liminf_h\mathcal E_h(g_h,G_h)\). This requires the appropriate intrinsic lower-semicontinuity/quasiconvexity and control of the limiting interface measure, including discrete seams and one-sided geometry. | **OPEN.** |
| **L5 — Recovery sequence** | For each admissible \((g,G)\), construct a sequence \((g_h,G_h)\) with \(\limsup_h\mathcal E_h(g_h,G_h)\le\mathcal E(g,G)\). The approximation of a general jump set by mesh edges, and the associated seam/jump cost, must be controlled. A jump not aligned with edges cannot be assumed to have a cost-free or uniformly bounded mesh approximation. | **OPEN.** |
| **L6 — Discrete/continuous transfer** | Define explicit maps \(T_h\), prove consistency and stability, and verify the chain/field and metric properties needed by the intended limit. Without a specified \(T_h\), this is not yet a fully testable theorem statement. | **OPEN; not yet an instantiated lemma.** |

Logical dependencies: L1 supports L2, L4 and L5; L2 supplies a measure framework for L3; L3 supplies candidate densities for L4 and L5; L4 and L5 together establish Γ-convergence once compactness/equicoercivity is also available. L6 is a separate prerequisite for conclusions that compare the shell discretisation with \(Q_6\)/Kathara or identify discrete operators with continuum ones.

## 7. Physical seam models — choose one before proving a limit

Let \(\Gamma_{\rm phys}\subset S\) be the prescribed panel-seam network.

- **Model A — kinematic constraint.** Impose a trace constraint such as \([g]=0\), or a prescribed jump, on \(\Gamma_{\rm phys}\). The seam is a constraint, not an additional free jump energy. The admissible class and trace convention must be specified.
- **Model B — cohesive interface.** Assign a separate density \(\psi_\Gamma([g],\nu,\theta)\) to the fixed interface. State its growth, continuity and lower-semicontinuity assumptions and ensure that the same interface is not counted again in a generic jump term.
- **Model C — geometric seam without an energetic jump penalty.** The seam records a change of panel geometry, metric or normal but contributes no independent jump cost. This is mathematically possible only after specifying the admissible traces and the bulk density across the seam; zero penalty can otherwise permit energetically uncontrolled jumps.

These are different models, not interchangeable notational conventions. The energy must say whether \(S_g\) may intersect \(\Gamma_{\rm phys}\), whether it may contain it, and how the seam contribution is counted. In particular, double-counting a seam once as a prescribed interface and again as a free jump is a modelling error unless the two terms represent distinct physical mechanisms.

A useful falsification test is to compare meshes with seams aligned to edges against meshes where the same fixed seam cuts element interiors. Compute the seam and jump contributions separately. A non-vanishing discrepancy under refinement signals that the discrete interface convention is not consistent; it is not, by itself, a proof of a general counterexample.

## 8. Four convergence claims that must remain separate

1. **Γ-convergence** concerns convergence of functionals in a declared topology. It does not by itself imply convergence of minimisers without equicoercivity, nor convergence of operators.
2. **Mosco convergence** is a weak-liminf/strong-recovery convergence for convex functionals (in particular closed quadratic forms) on a fixed Hilbert space, or on varying spaces with explicitly controlled comparison maps. It is not merely another name for Γ-convergence.
3. **Operator/resolvent convergence** requires the relevant closed forms, domains and Hilbert-space identifications, plus the hypotheses of the chosen form-convergence theorem.
4. **Spectral convergence** additionally requires suitable compactness of resolvents (or another precise spectral compactness condition) and control of multiplicities. Compactness of \(S\) alone is not enough if the limiting form domain or coercivity does not give compact embedding.

The \(Q_6\) Walsh spectrum, the \(S^3/T^*\) spectrum and the \(S^3/2I\) spectrum are separate exact benchmarks. None is automatically the limit spectrum of the football shell.

## 9. Separate target statements

The programme has four targets, each requiring its own hypotheses and proof.

**(A) Global barycentric quadrature.** Sum the local T068/T070 expansions and prove an explicit global error bound, including uniform control of the total weights and derivative norms. Derive any Bernoulli/Euler–Maclaurin corrections from the actual mesh summation rule.

**(B) Structured-deformation Γ-limit.** Define the surface functional, topology and seam model; prove compactness/equicoercivity, liminf and recovery. Any use of Amar–Matias–Morandotti–Zappale (2022) must identify the exact Euclidean hypotheses used and prove the additional surface/mesh extension.

**(C) Mosco/operator limit.** Define the discrete and continuum quadratic forms and comparison maps; prove weak-liminf and strong-recovery properties on the declared Hilbert spaces.

**(D) Spectral convergence.** After (C), prove the required compact-resolvent and spectral multiplicity hypotheses. Do not infer it from a finite chain map, a numerical spectral fit or a common algebraic parameter.

## 10. Existing finite inputs and their scope

- **T068/T070:** local triangle barycentre, covariance and Taylor/quadrature identities under their stated hypotheses; not a global shell limit.
- **T069:** exact pair mean/difference covariance identity for a fixed-point-free involution; the recovered RGS seed covariance and XOR 7/XOR 63 distinction are finite records.
- **T071:** exact \(Q_6\) cubical chain identities \(B_1B_2=0\), Anti-Twin chain-map identities and the stated truncated-2-skeleton ranks/Betti numbers; synchronisation/hysteresis remains exploratory.
- **T072:** exact Möbius phase-translation action, pure-gauge vertex-phase connection, \(Q_6\) Walsh Laplacian spectrum and antipodal \(32+32\) decomposition; the canonical equal-time connection is trivial.
- **Gate D / PR #195:** recorded finite Kathara–\(Q_6\) chain-map identities and rank checks; no \(O_h\)-equivariance, canonical metric, shell embedding or spin transport follows.
- **Gate E.1 / T068:** local quadrature law and companion implementation; no global limit theorem.
- **S.4–S.8:** fourth-moment tensor, jump expansion, derivative, Maxwell obstruction and coframe variation, each with its own exact/numerical status.
- **S.9/S.10:** Weber–Dedekind eta, supergolden class invariant, Dirichlet eta/\(L\)-function/quadratic-zeta and Bernoulli/polygamma identities; these special-function identities do not prove the shell limit.
- **S011:** binary-tetrahedral \(S^3/T^*\) spectrum with an independent Molien/Peter–Weyl reconstruction. The binary-icosahedral \(S^3/2I\) spectrum is a separate module.

## 11. Falsification and proof gates

The global programme cannot be promoted if any required item remains absent: a uniformly controlled shell refinement; intrinsic function spaces and traces; uniform local-moment and total-weight bounds; a specified bulk/interface energy; a seam convention without double counting; compactness and relaxation; liminf and recovery; explicit transfer maps with the required consistency; and, for operator/spectral claims, Mosco and compact-resolvent arguments.

A numerical fit, common polynomial, shared phase parameter, visual cell correspondence or finite chain identity cannot replace these proof obligations.

## 12. Status and references

**Status: OPEN.** T073 is a structured research programme and checklist, not a theorem asserting that the global limit exists. The sufficient coercivity and geometric assumptions listed above are candidate hypotheses to be tested against a fully specified energy; they are not claimed to be minimal or already verified.

- [Canonical unitary theory](../docs/UNIFIED_THEORY_FOOTBALL_GAMMA_BETA_ZETA_MORANDOTTI_RGS_PRISM_Q6_2026-11-10.md).
- [Integrated moments/barycentres/Gamma–Beta–zeta/Morandotti synthesis](../docs/SYNTHESIS_MOMENTS_BARYCENTRES_GAMMA_BETA_ZETA_MORANDOTTI_2026-11-10.md).
- [Independent numerical replay report](../reports/2026-11-10_integrated_synthesis_numerical_replay.md).
- [Special-functions and Morandotti bibliography](../bibliography/special-functions-beta-zeta-bernoulli-veneziano/README.md).

### References

1. N. Yui and D. Zagier, “On the Singular Values of Weber Modular Functions,” *Mathematics of Computation* 66 (1997), 1645–1662.
2. A. Ikeda, “On the Spectrum of Homogeneous Spherical Space Forms,” *Kodai Mathematical Journal* 18 (1995), 57–67.
3. Amar–Matias–Morandotti–Zappale (2022), “Periodic Homogenization in the Context of Structured Deformations,” *ZAMP* 73, article 173, DOI 10.1007/s00033-022-01817-6.
4. NIST Digital Library of Mathematical Functions, Chapters 5, 23, 24 and 25.
