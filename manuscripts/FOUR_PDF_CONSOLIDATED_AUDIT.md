# Consolidated critical audit of four exploratory PDFs

**Audit date:** 2026-11-06  
**Sources:** \`dirac.pdf\`, \`siiiiii.pdf\`, \`soluzione.pdf\`, \`yess.pdf\` (ChatGPT Library uploads; original uploads are unchanged).  
**Editorial outcome:** retain a small number of mathematical definitions and explicit diagnostics; do not treat any of the four PDFs as a validated paper or as evidence for new physical effects.

This is a source audit, not an independent reproduction of the numerical experiments. The PDFs contain narrative, equations and selected output tables, but the displayed material does not consistently provide complete executable source, input data, conventions, error controls and independent checks. Reported numerical values are therefore classified as *reported*, not independently verified.

## Executive disposition

| Source | Defensible material | Claims not established | Decision |
|---|---|---|---|
| \`dirac.pdf\` | A fixed Hermitian finite-dimensional Hamiltonian can be propagated by Crank–Nicolson with norm preservation; the document itself reports substantial drift in its proposed total energy | A physical breather, a self-consistent conservative Dirac–geometry system, particle–hole symmetry, Majorana/BdG structure, supersolidity | Keep only as a negative numerical audit / future model specification |
| \`siiiiii.pdf\` | Static spherical ansatz; standard scalar potential derivatives; a possible scalar–torsion action can be studied once conventions are fixed | A closed RGS–EMS action, its complete field equations, a validated wormhole BVP, a derived Hessian or QNM potential | Do not promote profiles or stability claims; use the separately cleaned scalar–torsion identity only for its explicitly stated action |
| \`soluzione.pdf\` | Standard formal definitions of tortoise coordinate and one-dimensional wave equation are recognizable in isolation; finite-matrix heat traces can be computed once a matrix is specified | Claimed QNM frequencies/stability, bounce, ghost freedom, UV regularization, Seeley–DeWitt coefficients, SUSY cancellation, cosmological constant, wormhole stabilization, Mosco convergence | Quarantine as a mixed exploratory compilation; no active paper |
| \`yess.pdf\` | The exterior-square construction \`Λ²(C₆)\` is a well-defined finite-dimensional algebraic operation; if the stated matrix identity and ranks are independently checked, the corresponding projector identities follow | Equivariance under \`2I*\`, irreducibility/decomposition claims, a covariant curvature tensor on a manifold, Yang–Mills dynamics, a bridge to \`Q₆\` | Extract only the conditional linear-algebra lemma; group and geometric claims remain open |

## 1. \`dirac.pdf\`: Dirac operator and proposed breather

### What survives

- For a **fixed** Hermitian matrix \(H\), the Crank–Nicolson update
  \[
  (I+\tfrac{i\Delta t}{2}H)\psi_{n+1}
  =(I-\tfrac{i\Delta t}{2}H)\psi_n
  \]
  is unitary in exact arithmetic, hence preserves \(\|\psi_n\|_2\). This is a standard numerical fact, not evidence of a new physical mechanism.
- The PDF explicitly records that the reported total energy is not conserved: one table changes from \(0.026004\) to values near \(0.9\); a later coupled-splitting table reports a relative drift of about \(+29\%\). These outputs contradict the accompanying language of exact Noether conservation.
- The text itself correctly retracts the inference from an oscillating SCF iteration to a physical breather, and correctly notes that a symmetric spectrum \(\pm E\) alone does not establish a particle–hole antiunitary symmetry.

### What fails or remains unproved

1. The proposed feedback potential \(U[\rho(t)]\) makes the Hamiltonian state-dependent. Norm preservation of a frozen-Hamiltonian Crank–Nicolson step does not establish conservation of the energy of the coupled field–spinor system.
2. The proposed total action is schematic: the field variables, boundary terms, dimensions, gauge structure, and full variations are not specified sufficiently to derive the displayed coupled equations uniquely.
3. The document reports a large residual in an attempted antiunitary symmetry test and then proposes that a suitable matrix \(U\) may exist. Until an explicit \(C=UK\) is constructed and the identity \(U H_D^* U^\dagger=-H_D\) is checked for the actual matrix, particle–hole symmetry is **not established**.
4. The reported sub-gap localization and time-dependent core fraction are numerical observations without a complete reproducible specification of the discretized operator, grid, parameters, convergence study and independent solver.
5. A reduced core probability that decreases and later rises is not, by itself, a periodic localized solution or a breather.

**Classification:** norm preservation for a fixed Hermitian finite matrix is established mathematics; the PDF's energy-drift tables are reported diagnostics; the proposed breather and physical interpretations are unsupported. No Majorana, BdG, supersolid or new-particle claim should be made from this source.

## 2. \`siiiiii.pdf\`: RGS–EMS action, static background and perturbations

### What survives

The line element
\[
ds^2=-N(u)^2dt^2+du^2+R(u)^2d\Omega^2
\]
is a legitimate static, spherically symmetric ansatz on a region where \(N>0\) and \(R>0\). The derivatives of
\[
V(\phi)=V_0+\frac{\lambda}{4}(\phi^2-\phi_v^2)^2
\]
are correctly
\[
V'(\phi)=\lambda\phi(\phi^2-\phi_v^2),\qquad
V''(\phi)=\lambda(3\phi^2-\phi_v^2).
\]
For a minimally coupled static scalar in this metric, the radial Klein–Gordon equation can be written
\[
\frac{1}{NR^2}\frac{d}{du}\left(NR^2\phi'\right)-V'(\phi)=0.
\]
These are standard ansatz-level statements and do not establish a wormhole solution.

### Defects in the proposed unified model

1. The function \(F_{\rm RGS}(T,\mathcal K_i)\) is left unspecified. The nonlinear electromagnetic function \(\mathcal F(X,Z)\), the nonlocal kernel and its causal prescription, and the interaction terms are also not defined. Consequently, the displayed expression is not a closed action from which a unique ODE system or Hessian can be derived.
2. A teleparallel variational problem must specify the tetrad, inertial spin connection, local-Lorentz convention, torsion/sign conventions and independent variables. A metric ansatz alone does not determine the teleparallel field equations.
3. The text alternates between \(\sqrt{-g}\) and the tetrad determinant and does not provide a complete, consistent tetrad/spin-connection variation for the proposed modified theory.
4. The displayed second-order action contains a term \((\partial_u\Psi)^5\). As written this is not the usual quadratic principal part of a linear perturbation action and is inconsistent with the stated claim that it is a Hessian. It must be treated as an error, not silently corrected.
5. The PDF asserts a converged BVP and an \(L^2\) residual of exactly zero, but does not supply enough of the actual equations, boundary conditions, solver source, tolerances and independent constraint checks to reproduce that result. A printed zero is not a validated residual.
6. A local minimum \(R'(0)=0,\ R''(0)>0\) is only a geometric throat candidate. It does not establish the energy conditions, traversability, global regularity, or dynamical stability.

**Classification:** the ansatz and elementary scalar-potential identities are established; the unified RGS–EMS model, its BVP profiles, Hessian, QNM potential and wormhole stability are not established by this PDF.

## 3. \`soluzione.pdf\`: cosmology, QNMs, spectral coefficients and wormhole claims

This 63-page file is a compilation of several distinct threads, not one coherent derivation.

### Specific mathematical and methodological problems

1. **QNM calculation:** the Schrödinger-type master equation and outgoing-wave boundary conditions are standard once a valid master variable and potential have been derived. Here the PDF does not provide a reproducible derivation of \(V_{\rm eff}\) from a specified second variation. The quoted WKB values therefore cannot be treated as QNM predictions of the RGS–EMS model.
2. **Stability inference:** a negative imaginary part in a selected approximate frequency does not establish stability of the full coupled background, especially when the perturbation operator and boundary-value problem have not been validated.
3. **Bounce:** the displayed background audit gives \(H_+(t_b)=-6.73358\times10^{-2}\), not \(H(t_b)=0\). Under the usual definition of a smooth cosmological bounce, this does not demonstrate a bounce. A near-match of a parameter \(\xi\) to a chosen threshold is not a substitute for the background equations and their constraints.
4. **Ghost freedom:** a generic interaction written using symmetric polynomials of a mixed deformation matrix does not, by assertion alone, establish the constraint structure that removes the Boulware–Deser degree of freedom. The full action and Hamiltonian constraint analysis are missing.
5. **Seeley–DeWitt coefficients:** for a finite matrix \(H\), \(\operatorname{Tr}(e^{-tH})\) and the moments \(\operatorname{Tr}(H^k)\) are computable. They are not automatically the continuum Seeley–DeWitt coefficients of a specified Laplace-type operator. In particular, setting \(a_4=\tfrac12\operatorname{Tr}(H^2)\) is a convention-dependent finite-matrix moment, not a general heat-kernel theorem.
6. **SUSY cancellation:** a claimed supertrace or residual index requires an explicitly defined graded Hilbert space, grading operator and supercharge/intertwining relation. Counting 60 cancellations in a table is not by itself a supersymmetric index theorem.
7. **UV regularization and cosmological constant:** neither UV finiteness nor a finite physical vacuum energy follows from a finite graph spectrum or a truncated heat-trace expansion without a continuum limit, renormalization prescription, dimensions and a specified physical operator.
8. **Wormhole potential:** the terms proportional to \(1/\rho\), \(1/\rho^4\) and \(\rho^2\) are introduced phenomenologically. The algebraic stationary-point calculation is valid conditional on that ansatz, but it does not derive the potential from the RGS action or prove a stable throat.
9. **Mosco convergence:** a single fixed finite graph \(Q_6\) cannot establish a continuum Mosco limit. A refining family of spaces/forms, comparison maps, lower-bound and recovery-sequence arguments are required.

**Classification:** retain only standard equations as background exposition when independently sourced. All model-specific numerical outputs and physical conclusions remain unverified or unsupported.

## 4. \`yess.pdf\`: exterior-square operator and the proposed \(6+9\) split

Let \(C_6\) be a specified \(6\times6\) matrix. The induced operator on \(\Lambda^2\mathbb R^6\), of dimension 15, is well-defined by
\[
(\Lambda^2 C_6)_{[ij],[kl]}=(C_6)_{ik}(C_6)_{jl}-(C_6)_{il}(C_6)_{jk}.
\]
If an independently checked construction gives a symmetric matrix \(C_{15}=\Lambda^2C_6\) satisfying \(C_{15}^2=25I_{15}\) and with eigenspace dimensions 6 and 9, then
\[
P_\pm=\frac12(I_{15}\pm C_{15}/5)
\]
are orthogonal complementary projectors of ranks 6 and 9. This implication is a valid elementary linear-algebra lemma.

### What the PDF does not prove

1. The code shown constructs \(C_6\) and \(C_{15}\), but does not construct the claimed matrices \(R_6(g)\) and \(R_{15}(g)\) for the generators of \(2I^*\). The printed zero commutator is therefore not independently reproducible from the displayed code.
2. The proof assumes the key intertwining identity \(C_6R_6=R_6C_6\); it does not derive it from an explicit group action on the six-dimensional space.
3. Commutation of a projector with a group representation proves invariance of its image, not irreducibility. The claimed irreducible decomposition requires characters or explicit invariant-subspace calculations for the restricted representation.
4. A constant matrix acting on a trivial rank-15 bundle over \(\mathbb R^6\) is a legitimate bundle endomorphism, but it is not automatically a curvature tensor, a covariant geometric field, or a dynamical Yang–Mills background.
5. The claimed bridge from this \(6+9\) split to the 64 vertices and 240 square faces of \(Q_6\) is not defined in this PDF. It needs an explicit map, chain-level action and compatibility proof.

**Classification:** conditional finite-dimensional algebra only. Group equivariance, representation decomposition, continuum geometry and physical interpretation remain open.

## Consolidated action items

- Keep the already cleaned [scalar–torsion variational identity](SCALAR_TORSION_VARIATIONAL_IDENTITY.md) as a narrow conditional derivation; do not import the incomplete BVP or Hessian claims from \`siiiiii.pdf\`.
- Keep the already cleaned [inhomogeneous spin-chain note](INHOMOGENEOUS_SPIN_CHAIN.md) separate from the Dirac feedback/breather narrative.
- The conditional exterior-square projector implication has now been extracted as [T053](../theorems/T053-exterior-square-projector-lemma.md). The source-specific hypotheses (exact matrix, symmetry and quadratic identity) still require independent verification; no equivariance or irreducibility claim is imported.
- For \`dirac.pdf\`, any continuation must begin with an explicit finite-dimensional action/Hamiltonian and a coupled integrator tested against norm, energy, timestep refinement and spatial refinement. Do not use the existing output tables as physical evidence.
- Do not use \`soluzione.pdf\` as a source for QNM, bounce, ghost-free, UV, SUSY, vacuum-energy or wormhole-stability claims.
- Preserve all four original Library PDFs as source material. Their rejection as evidence does not require deleting the originals.

## Theorem extraction register\n\nThe defensible statements have been separated into theorem records: [T050](../theorems/T050-geometric-spin-chain-bounds.md) (geometric spin-chain summability and norm bound), [T051](../theorems/T051-crank-nicolson-unitarity.md) (fixed-Hamiltonian norm preservation), [T052](../theorems/T052-scalar-torsion-variation.md) (conditional scalar variation), [T053](../theorems/T053-exterior-square-projector-lemma.md) (conditional exterior-square projectors), and [T054](../theorems/T054-static-radial-klein-gordon.md) (static radial Klein–Gordon reduction). The theorem records contain their own hypotheses, proofs and non-conclusions.\n\n## Final status

No theorem about new particles, a physical breather, a traversable/stable wormhole, a cosmological bounce, ghost freedom, UV completion, Yang–Mills dynamics or a continuum limit is established by these four PDFs. The defensible residue is limited to standard ansätze, elementary scalar-potential derivatives, conditional finite-dimensional linear algebra, and diagnostic evidence that several earlier numerical interpretations were overstated.
