# Critical audit — *FORMULAZIONE.pdf* (RGS–EMS / teleparallel, LQG and quantum-gravity claims)

## Editorial verdict

**The 70-page Library document is a mixed exploratory compilation, not a submission-ready scientific paper.** It contains some standard geometric ingredients and useful diagnostic warnings, but it also contains incompatible model generations, placeholder computations, unsupported identifications with loop quantum gravity (LQG), unjustified wormhole/bounce interpretations, gauge-invariance problems in the proposed electromagnetic coupling, and observational predictions with no derivation. It must not be cited as a proof of an RGS–EMS solution, a quantum-gravity result, proton tunnelling, gravitational-wave echoes, or a unified theory.

The original PDF should be preserved as historical source material. A clean paper must be reconstructed from a single fully specified action and a consistent set of field equations, not obtained by cosmetically editing the compiled dialogue.

## 1. Material that can be retained after convention checks

- The static, spherically symmetric proper-radial metric
  \[
  ds^2=-N(u)^2dt^2+du^2+R(u)^2d\Omega^2
  \]
  is a legitimate ansatz. The associated Levi-Civita curvature can be calculated exactly once the Riemann-sign convention is fixed.
- The teleparallel identity relating the Levi-Civita Ricci scalar, the torsion scalar and the divergence of the torsion vector is a standard geometric identity **only after** the torsion, superpotential, torsion-vector and sign conventions are fixed consistently.
- The scalar-tensor action can be studied as a candidate model. Its field equations must be derived from the displayed action, not assembled from schematic terms.
- The distinction between a metric and a teleparallel tetrad-plus-inertial-spin-connection pair is essential and should be retained.

These points do not establish that any quoted wormhole profile solves the field equations.

## 2. A concrete variational error in the scalar equation

For the action displayed in the document,
\[
S=\int d^4x\,e\left[-\frac12F(\phi)T
-T^\mu\partial_\mu F(\phi)
-\frac12\partial_\mu\phi\partial^\mu\phi
-V(\phi)\right],
\]
with the geometric variables held fixed in the scalar variation, integration by parts gives
\[
\Box\phi-V'(\phi)-\frac12F'(\phi)T
+F'(\phi)\nabla_\mu T^\mu=0.
\]
The PDF instead writes
\[
\Box\phi-V'-\frac12F'T+\nabla_\mu(F'T^\mu)=0.
\]
The last term is not the result of varying the displayed action: it contains an extra term \(F''(\phi)\partial_\mu\phi\,T^\mu\). For \(F=1+\xi\phi^2\), the correct term from this action is \(2\xi\phi\nabla_\mu T^\mu\), not \(\nabla_\mu(2\xi\phi T^\mu)\).

This correction assumes the stated action and the stated convention for the torsion-vector divergence. If the intended action is different, it must be written explicitly and varied afresh.

## 3. Tetrad and inertial spin connection

The diagonal spherical co-tetrad together with an imposed zero spin connection is not, by itself, a covariant teleparallel specification. In spherical coordinates, the diagonal frame carries inertial contributions. A covariant formulation must give the tetrad and the corresponding inertial spin connection (or clearly state a pure-tetrad formulation and its frame dependence), then compute all torsion quantities from that same pair.

The PDF alternates between:
- zero spin connection in spherical coordinates;
- a torsion vector containing angular coordinate terms;
- a teleparallel identity used as a numerical pass criterion;
- later non-diagonal tetrads and additional “twist” terms.

These are not one fixed geometric model. The tetrad, inverse tetrad, spin connection, torsion convention, superpotential and curvature-sign convention must be frozen before any invariant or field equation is reported. A metric alone does not determine the teleparallel torsion scalar.

A continuum identity may hold exactly, but a second-order finite-difference residual should converge with grid refinement; it is not generally expected to be at machine precision on a finite grid. A residual of order \(10^{-4}\) is not evidence of exactness. Report a convergence study and independently evaluate the analytic identity where possible.

## 4. Background and BVP claims

The document reports several incompatible outcomes, including:
- a BVP returning a trivial scalar profile and a throat radius near 29.3;
- a later “4D converged” profile with \(R(0)\simeq0.8292\), \(\phi(0)\simeq0.3450\), \(N(0)\simeq1.4529\);
- other calculations using a throat near 2.31 and a different negative-mode spectrum.

A solver reporting numerical convergence only means that its implemented boundary-value problem converged. It does not show that the equations are the Euler–Lagrange equations of the declared action. The PDF itself contains schematic placeholders for the gravitational equations and describes arbitrary test profiles. No single complete action, complete coupled ODE system, parameter registry, asymptotic boundary conditions, residual dossier and reproducible solver package are supplied consistently for all the quoted backgrounds.

The later independent archive diagnostics explicitly classify the \((0.8292,1.4529,0.3450)\) profile as a reconstructed diagnostic ansatz, not a full RGS–EMS BVP solution; the asymptotic lapse and scalar boundary conditions are not satisfied by that ansatz. It must not be called a converged physical wormhole.

**Editorial action:** remove “converged solution”, “stable traversable wormhole”, “scalar hair solution” and all derived physical conclusions until the coupled field equations are derived and a BVP is solved with the correct asymptotic conditions and independent residual checks.

## 5. Negative modes, instantons and proton tunnelling

A negative eigenvalue of a chosen discretized operator is not, by itself, proof of an instanton or bounce. One must first derive the second variation of the action about an actual stationary background, specify gauge and constraint reduction, boundary conditions, inner product and self-adjoint domain, then establish convergence of the spectrum. The document reports more than one negative eigenvalue in some runs, while invoking the “one negative mode” bounce criterion without reconciling that discrepancy.

The quoted Euclidean action estimate is not derived from a normalized fluctuation solution and has no demonstrated dimensions or determinant prefactor. The semiclassical factor is \(e^{-S_E/\hbar}\) only when the Euclidean action and \(\hbar\) use consistent units. A value \(S_E/\hbar\ll1\) is outside the regime in which a dilute semiclassical instanton approximation is controlled; it does not establish an unsuppressed physical transition.

The proton WKB expression contains an undefined effective potential and no derived proton–torsion coupling, barrier, boundary state or scattering problem. Therefore the quoted \(P=1.0000\) is not a proton-tunnelling prediction and must be removed.

## 6. LQG polymerization and the two-sheet “factor of two”

The area-gap expression quoted in the document is recognizable as a standard LQG area-gap convention. The subsequent steps are not established:

- The replacement \(K\mapsto\sin(\mu_0K)/\mu_0\) belongs to specified effective Hamiltonian constructions in canonical loop approaches. It does not imply the generic substitution \(T\mapsto T(1-T/T_{\rm crit})\) in a covariant teleparallel action.
- No canonical variables, Poisson brackets, Hamiltonian constraint, holonomy representation or derivation of the proposed polynomial torsion correction is given.
- The proposed throat-radius formula contains an unspecified ZPE density and a potential value whose normalization and units are not fixed. It is therefore not an exact prediction.
- The reported value 1.6354 does not agree with 0.8292. Dividing by two because the manifold has two asymptotic sheets is not a valid geometric correction. A two-sheeted covering does not halve the local areal radius; the covering map is locally a diffeomorphism (and in the usual covering metric, a local isometry). The residual 1.39% after this ad hoc division is not evidence of equivalence.

Remove the claimed LQG derivation, “exact” matching and covering-factor explanation. A genuine LQG comparison would require a derived effective Hamiltonian constraint and a clear map between its variables and the RGS–EMS variables.

## 7. Horizon entropy, gravitational-wave echoes and ER=EPR

- The Bekenstein–Hawking area law is not automatically an entropy formula for an arbitrary wormhole throat. A logarithmic correction coefficient is model- and ensemble-dependent; the document gives no microstate counting or derivation for its chosen coefficient.
- The proposed phase correction \(\delta\Psi_{\rm NZ}(f)\) has no derivation from a perturbation equation, scattering problem or waveform model. The dimensions of \(\beta_{\rm NZ}\), the frequency normalization and the exponent are not fixed. A quoted Planck-scale delay does not establish a detectable accumulated phase.
- A traversable geometric throat does not establish quantum entanglement between its mouths. ER=EPR is not a consequence of classical wormhole geometry, and the document specifies no quantum state or entanglement calculation.
- A finite-frequency echo calculation requires a well-posed wave equation, effective potential, boundary conditions, reflection/transmission coefficients and detector-band analysis. These are absent.

Remove the observational and ER=EPR claims from the results and conclusions. They may be listed as future questions only after a quantitative model is supplied.

## 8. Quaternionic electromagnetism and gauge invariance

The proposed term \(\xi T^\mu A_\mu\) in a Maxwell-type Lagrangian is not generally invariant under the U(1) transformation \(A_\mu\mapsto A_\mu+\partial_\mu\chi\). Its change is a boundary term only if the torsion-vector current obeys the required conservation condition \(\nabla_\mu T^\mu=0\), which is not established and is not generally true. The corresponding sourced Maxwell equation must satisfy the current-conservation identity implied by the antisymmetry of \(F^{\mu\nu}\). This coupling cannot be presented as a consistent gauge interaction without resolving that issue.

Writing \(F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu\) is the ordinary Abelian field strength; calling it quaternionic does not make it a new quaternionic gauge theory. A genuine quaternionic formulation must define the algebra, representation, connection, gauge group, transformation law, curvature and matter coupling. The direct-sum notation \(\mathfrak{so}(3,1)\oplus\mathfrak{u}(1)\) alone does not derive Maxwell dynamics from torsion.

The claim that local Lorentz symmetry is merely a spurious redundancy and can be discarded is also not an acceptable description of covariant teleparallel gravity. The tetrad and inertial spin connection transform together under local Lorentz transformations. A zero-spin-connection gauge may be chosen, but it does not justify ignoring the covariant pair or frame dependence in modified teleparallel theories.

**Editorial action:** remove the claim that the electromagnetic sector has been derived or unified. Retain ordinary Maxwell theory as a separately defined U(1) sector until a gauge-invariant action and its complete variations are provided.

## 9. Heat kernel, spectral projection and ultraviolet finiteness

The leading heat-kernel factor \((4\pi s)^{-d/2}\) depends on the dimension \(d\) of the operator's underlying manifold. The document uses a four-dimensional leading factor while referring to the three-dimensional spherical space form \(S^3/2I^*\), without specifying a four-dimensional product/spacetime operator.

The coefficients in a heat-kernel expansion are local geometric invariants of the specified operator and geometry. They are not “regulated by the golden topology \(N=5\)” merely because a finite group or a fivefold label appears. A finite-rank spectral projection can truncate a spectrum, but it changes the operator/problem and does not prove that the unprojected continuum theory is UV finite or renormalized.

No operator domain, bundle, Laplace-type operator, projection kernel, trace-class estimate, coefficient calculation or regulator-removal argument is supplied. Therefore remove the claims that the projection proves absolute convergence, eliminates all UV divergences, or yields a finite partition function.

A valid spectral paper may study explicit spectra on \(S^3/2I^*\), invariant subspaces and heat traces, with the dimension and operator stated precisely. That mathematical problem is separate from claims about quantum gravity or physical UV completion.

## 10. Nonlocal memory and quantum Fisher information

The proposed \(\Pi_{\mu\nu}\) uses a Green function said to live on \(S^3/2I^*\), while integrating over a four-dimensional spacetime variable \(x'\). The domain, measure, tensor bundle, operator, boundary conditions and conservation properties are not specified. The claimed explanation of dark-matter phenomenology and lensing therefore does not follow.

The pure-state QFI formula is standard, but the manuscript does not define a Hilbert space, normalized state family, generator, parameter dependence or unitary dynamics for the proposed gravitational state. A finite maximum at the bounce and information-preserving reheating cannot be inferred from the definition alone.

Remove the lensing, dark-matter, QFI-maximum and unitary-information-transfer claims unless these structures are explicitly constructed and calculated.

## 11. Required editorial reconstruction

The 70-page source contains dialogue prompts, repeated formulations, incompatible numerical generations, unfinished code descriptions and speculative conclusions. These must not be retained in a formal paper.

A defensible successor manuscript should be split into independent documents:

1. **Teleparallel geometry audit:** conventions, tetrad, inertial spin connection, torsion tensor/vector/scalar, Levi-Civita invariants and exact identity checks.
2. **Scalar–tensor RGS–EMS model:** one complete action, dimensions, all Euler–Lagrange equations, constraints and boundary conditions.
3. **Background BVP:** equations derived from that action, asymptotic flatness/vacuum conditions, convergence and independent residuals.
4. **Perturbation/stability problem:** second variation derived from the action, physical constraint reduction, self-adjoint operator and converged spectrum.
5. **Optional QLG/Maxwell extension:** a separate gauge-invariant action and explicit algebraic/representation data. No LQG, ER=EPR, proton or observational claim should be included until independently derived.

## Epistemic status

- **Standard mathematics, subject to convention audit:** spherical metric geometry; the teleparallel curvature–torsion identity; variational calculus.
- **Candidate model:** the displayed scalar–torsion action, once conventions and full field variations are fixed.
- **Diagnostic only:** reconstructed profiles and finite-domain spectral/Maxwell calculations that do not solve the complete field equations.
- **Not established:** a physical RGS–EMS wormhole, a stable throat, an instanton, proton tunnelling, LQG equivalence, a biverso radius correction, gravitational-wave echoes, ER=EPR, quaternionic Maxwell emergence, UV finiteness, dark-matter explanation or quantum-information conservation.

The source PDF is retained for provenance. None of the rejected claims is silently promoted into the central theorem registry.
