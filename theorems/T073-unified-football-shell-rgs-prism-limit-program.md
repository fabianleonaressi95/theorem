# T073 — Unified football-shell / RGS–PRISM–Q6 limit programme

**Status: OPEN — conditional theorem target, not a proved convergence theorem.**  
**Role:** formal statement of the common limit problem underlying the 10 November 2026 work. The local ingredients T068–T072 and S.1–S.11 remain governed by their own proof statuses. This record does not promote their separate conclusions into a global theorem.

## 1. Geometric and functional setting

Let (Ssubsetmathbb R^3) be a compact, oriented, piecewise-(C^2) shell with a finite panel decomposition. In the football model the panel complex has 60 vertices, 12 pentagons, 20 hexagons and 90 physical panel seams. Its fan triangulation has 180 triangular CST facets and the recorded shell discretization has 92 nodes including panel centres. Let (mathcal T_h) be a conforming, shape-regular family of triangular refinements of (S), with maximum element diameter (h	o0). Physical seams are retained as a distinguished interface set (mathcal S_h).

The discrete comparison complex is the six-cube (Q_6), with 64 vertices, 192 edges and 240 square 2-cells. A Kathara complex may also be included. The 92-node shell and the 64-vertex Q6 complex are not identified by cardinality; all comparisons must be made through explicit maps.

For a structured-deformation field, use the standard pair
[
(g,G)in SBV(S;mathbb R^m)	imes L^p(S;mathbb R^{m	imes2}),
qquad M=
abla_Sg-G,
]
with the tangent/covariant interpretation fixed by the shell geometry. (G) here is the structured-deformation field, not the shell metric.

## 2. Local cell measure and the proved quadrature input

On each triangle (Finmathcal T_h), choose parameters (a_{F,i}>0), (S_F=sum_i a_{F,i}), barycentric coordinates (lambda_i), and vertex matrix (V_F). Define
[
Z_F(a_F)=2A_Frac{prod_iGamma(a_{F,i})}{Gamma(S_F)},qquad
m_{F,i}=rac{a_{F,i}}{S_F},
]
[
C_{F,ij}=rac{a_{F,i}(S_Fdelta_{ij}-a_{F,j})}
{S_F^2(S_F+1)},qquad
c_{F,a}=V_F^{mathsf T}m_F,qquad
Sigma_{F,a}=V_F^{mathsf T}C_FV_F.
]
For (g_Fin C^3) on a neighbourhood of (F), T068/T070 prove
[
int_Fg_F,dmu_{F,a}
=g_F(c_{F,a})+rac12D^2g_F(c_{F,a}):Sigma_{F,a}+R_F,
quad
|R_F|lerac{h_F^3}{6}sup_F|D^3g_F|_{m op}.
]
For the unnormalized integral multiply by (Z_F(a_F)). In particular, if the parameters are uniformly controlled and the derivatives are uniformly bounded, then
[
sum_{Finmathcal T_h}Z_F(a_F)|R_F|
le rac{h^3}{6}sup_F|D^3g_F|_{m op}
sum_{Finmathcal T_h}Z_F(a_F),
]
where (h=max_F h_F). This is the local-to-global quadrature estimate to be used in the shell argument; its uniform hypotheses must be verified for the actual family.

## 3. Candidate discrete energy

For shell fields (u_h,	heta_h) and a structured-deformation pair ((g_h,G_h)), consider a functional of the form
[
mathcal E_h=
sum_{Finmathcal T_h}int_F
W_F(X,
abla_Su_h,G_h,	heta_h,
abla_S	heta_h),dA
+sum_{einmathcal S_h}int_e
arphi_e([g_h],
u_e,	heta_h),dmathcal H^1
+mathcal E_h^{(4)}.
]
The seam density (arphi_e) and the fourth-moment contribution (mathcal E_h^{(4)}) must be specified independently. The schematic expression does not prescribe a constitutive law. A physical panel seam is not automatically a jump set of (g_h), and a quadratic seam penalty is not automatically covered by a one-homogeneous interfacial density.

The Gamma/Beta/Dirichlet parameters generate local barycentric moments. The digamma/trigamma derivatives generate parameter cumulants. Zeta/Bernoulli values enter through special-function identities and asymptotic expansions. These identities do not, without an actual mesh summation rule, supply the Euler–Maclaurin coefficients of (mathcal T_h).

## 4. Required hypotheses for the global theorem

A proof must establish, rather than assume implicitly, hypotheses of the following types.

- **H1 — Surface geometry and refinement.** (S) has the regularity required by the chosen surface finite-element setting; (mathcal T_h) is conforming and uniformly shape regular; panel seams and their incidence are tracked under refinement.
- **H2 — Dirichlet weights and local moments.** (a_{F,i}) stay in a declared admissible range; (Z_F), barycentres, covariances and phase moments have uniform bounds; the sum of the local Taylor remainders tends to zero.
- **H3 — Field compactness and density regularity.** The interpolated fields have the Sobolev/BV bounds needed for compactness; the composed bulk density has the required regularity for quadrature wherever T068/T070 are invoked.
- **H4 — Bulk and interface energy.** (W_F) and (arphi_e) satisfy the precise coercivity, growth, lower-semicontinuity and compatibility assumptions required by the selected structured-deformation relaxation theorem. The interface measure and seam/jump-set convention are explicit.
- **H5 — Moment consistency.** The refinement stencil has the required first/third-moment cancellation, second-moment metric consistency, uniform fourth-moment bounds and higher regularity for the S.5 Taylor estimate. S.4 (fixed-cloud fourth moment) and S.5 (jump fourth moment) are not interchangeable.
- **H6 — Discrete transfer.** There are explicitly defined maps between the relevant Q6/Kathara and shell chain/field spaces. They commute with the boundary operators where required, are uniformly bounded, and satisfy independently stated geometry, metric, measure and orientation consistency. The finite Gate D identities alone do not imply these analytic properties.
- **H7 — Operator convergence.** If a Mosco or spectral conclusion is sought, the varying Hilbert spaces, comparison maps, quadratic forms, compactness and resolvent hypotheses are all specified. A chain map is not by itself a Mosco-convergence theorem.

## 5. The target conclusions (separate statements)

Under suitable verified versions of H1–H7, the programme seeks the following results. They must be proved separately.

**(A) Global barycentric quadrature.** The sum of the T068/T070 cell expansions converges to the surface bulk integral, with an explicit global error bound. The Bernoulli/Euler–Maclaurin correction terms, if present, are derived from the actual refinement summation rule.

**(B) Structured-deformation Gamma limit.** The functionals (mathcal E_h) Gamma-converge (in a declared topology) to a surface bulk/interface functional (mathcal E). The proof requires compactness, a liminf inequality and a recovery sequence. The Euclidean periodic theorem of Amar–Matias–Morandotti–Zappale (2022) is not, without an extension proof, a theorem on the closed curved shell.

**(C) Mosco/operator limit.** Separately, the discrete quadratic forms associated with the selected shell/Q6 operators Mosco-converge on the declared varying Hilbert spaces. The comparison maps must preserve the relevant energy and (L^2) structures in the limit.

**(D) Spectral convergence.** Only after (C), together with the required compactness/compact-resolvent and multiplicity-control hypotheses, may convergence of eigenvalues or spectral projectors be concluded. The (Q_6) Walsh spectrum, the (S^3/T^*) spectrum and the (S^3/2I) spectrum are separate exact finite/spherical benchmarks; none is automatically the limit spectrum of the football shell.

## 6. Exact finite inputs already available

- **T068/T070:** proved local uniform/weighted triangle barycentre, covariance and Taylor quadrature laws; T070 also gives the affine-phase moment bound.
- **T069:** exact pair mean/difference covariance identity for a fixed-point-free involution; the recovered RGS seed covariance and XOR 7/XOR 63 distinction are finite numerical records.
- **T071:** exact Q6 cubical chain identities (B_1B_2=0), Anti-Twin chain-map identities and the stated truncated-2-skeleton ranks/Betti numbers; synchronization/hysteresis is exploratory.
- **T072:** exact Möbius phase-translation action, pure-gauge vertex-phase connection, Q6 Walsh Laplacian spectrum and antipodal (32+32) decomposition; the canonical equal-time connection is trivial.
- **Gate D / PR #195:** the recorded finite Kathara–Q6 chain-map identities and rank checks; no (O_h)-equivariance, canonical metric, shell embedding or spin transport is claimed.
- **Gate E.1 / T068:** local quadrature law and companion implementation; not a global limit theorem.
- **S.4–S.8:** fourth-moment tensor, local current, Maxwell obstruction and algebraic coframe variation with the exact/numerical distinctions in their records.
- **S.9/S.10:** Weber–Dedekind eta, supergolden class invariant, Dirichlet eta/(L)-function/quadratic zeta and Bernoulli/polygamma identities.
- **S011:** source-verified binary-tetrahedral (S^3/T^*) spectrum and independent Molien check. The binary-icosahedral (S^3/2I) spectrum remains a separate module.

## 7. What would falsify or invalidate the proposed unification

The proposed global theorem fails in its stated form if any of the following cannot be supplied: a shape-regular shell refinement; uniform local moment bounds; a compatible surface bulk/interface density; a seam/jump-set convention satisfying the energy assumptions; a transfer map with the required metric/measure compatibility; or compactness and recovery constructions. A numerical fit between spectra, a shared algebraic polynomial, a common phase parameter, or a visual correspondence of cells cannot replace these hypotheses.

## 8. Status and repository links

**Status: OPEN.** This is the formal research target organising the results, not a proof that the global limit exists.

- [Canonical unitary theory](../docs/UNIFIED_THEORY_FOOTBALL_GAMMA_BETA_ZETA_MORANDOTTI_RGS_PRISM_Q6_2026-11-10.md).
- [Integrated moments/barycentres/Gamma–Beta–zeta/Morandotti synthesis](../docs/SYNTHESIS_MOMENTS_BARYCENTRES_GAMMA_BETA_ZETA_MORANDOTTI_2026-11-10.md).
- [Independent numerical replay report](../reports/2026-11-10_integrated_synthesis_numerical_replay.md).
- [Special-functions and Morandotti bibliography](../bibliography/special-functions-beta-zeta-bernoulli-veneziano/README.md).

## References

1. N. Yui and D. Zagier, “On the Singular Values of Weber Modular Functions,” *Mathematics of Computation* 66 (1997), 1645–1662.
2. A. Ikeda, “On the Spectrum of Homogeneous Spherical Space Forms,” *Kodai Mathematical Journal* 18 (1995), 57–67.
3. Amar–Matias–Morandotti–Zappale (2022), “Periodic Homogenization in the Context of Structured Deformations,” *ZAMP* 73, article 173, DOI 10.1007/s00033-022-01817-6.
4. NIST Digital Library of Mathematical Functions, Chapters 5, 23, 24 and 25.
