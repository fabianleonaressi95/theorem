# Technical audit: T047–T049D

**Scope:** theorem records, companion scripts/tests, and the declared EC–Dirac source convention. This is a source-level mathematical audit with independent calculations; it is not a claim that the repository's full pytest suite or CI workflow was executed.

## Findings and corrections

### T047 — Weyssenhoff scaling

- The continuity equation gives the **physical/proper** number density \(n\propto a^{-3}\), not a comoving number density. The wording was corrected.
- The displayed Friedmann background omitted spatial curvature. The theorem's hypotheses now explicitly state spatially flat FLRW, matching the displayed background equation.
- Given conserved spin per particle and the stated local isotropic closure \(S_{\mu\nu}=n\sigma_{\mu\nu}\) with fixed quadratic average of \(\sigma\), \(s^2\propto n^2\propto a^{-6}\) follows.
- For \(\rho_s=p_s=-A s^2\), the separately conserved component has \(w=1\); the negative sign does not change the ratio. The code's continuity residual is algebraically zero.
- **Boundary:** this is the stated Weyssenhoff closure, not a microscopic derivation for RGS–PSU and not a generic statement for every EC matter model.

### T048 — Mosco calibration

- The form convention \(\mathcal E_n(u)=n\sum_i|u_{i+1}-u_i|^2\), mass \(1/n\), and eigenvalue \(4n^2\sin^2(\pi k/n)\) are mutually consistent.
- Independent Fourier-mode calculations for \(k=2\), \(n=32,64,128,256,512\), show the discrete energy error decreasing from approximately \(1.00948\) to \(0.003964\); the eigenvalue error decreases from \(2.01895\) to \(0.007927\).
- Found and fixed an input-validation defect: non-integer cycle sizes and Fourier modes could pass the initial comparisons. The cycle, sample-mode, eigenvalue, and continuum-energy functions now reject non-integer and boolean values. Regression tests were added.
- **Boundary:** this remains a periodic-cycle calibration. There is no RGS–PRISM refinement sequence, comparison-map construction, uniform Rellich/tightness proof, or Mosco convergence theorem in the repository yet.

### T049 — Microscopic spin invariant

- The self/pair identity is the exact expansion of \(V^{-2}|\sum_x\mathbf s_x|^2\). The pair term is signed and may be negative.
- The coarse-graining expression has dimensions set by the units of the supplied spin contributions and physical volume; those units must be fixed by the dataset.
- **Boundary:** the classical self term is not automatically the renormalized quantum EC contact operator. The Noether normalization and contact prescription remain open.

### T049A — Q6/PRISM spin correlator

- Reviewed the shell metric, directed-pair counting, self/pair decomposition, replica averaging, and log-fit filtering. The Q6 shell multiplicities \(1,6,15,20,15,6,1\) and PRISM first-shell degree 10 are consistent with the product graphs.
- Repaired malformed display-math delimiters and a corrupted control character in the invariant formulas.
- **Boundary:** no physical spin-vector NPZ dataset with declared normalization is present. Fits on synthetic or supplied finite configurations are diagnostics only, not cosmological exponents.

### T049B — Lorentzian axial-current correlator

- Cross-checked the declared signature \((-+++)\), real current \(J_5^a=i\bar\psi\gamma^5\gamma^a\psi\), Dirac adjoint, Cartan source, torsion quadratic invariant, and four-fermion coefficient against the companion source modules rgs_ec_algebraic_torsion.py and rgs_ec_dirac_four_fermion.py.
- The implementation distinguishes the indefinite Lorentz contraction from the positive rest-space projected candidate. The latter is not identified with the Weyssenhoff spin invariant without the Noether normalization.
- **Boundary:** no validated Q6/PRISM spinor/current dataset, gauge-covariant transport, or operator contact renormalization is available. The source convention is traceable, but the physical RGS–PSU state is not constructed.

### T049C — Spatial intertwiner classification

- Schur's lemma gives \(\mathrm{Hom}_{SU(2)}(\mathbb C^2,\mathbb C^2\oplus\mathbb C^2)\cong\mathbb C^2\), with \(K_{\alpha,\beta}=(\alpha I_2,\beta I_2)^T\). Isometry requires \(|\alpha|^2+|\beta|^2=1\).
- Independent random-sample matrix calculation returned nullity 2; sample equivariance residuals were zero to displayed precision and isometry residuals were at most \(3.2\times10^{-16}\).
- **Boundary:** this is Spin(3)/SU(2) equivariance only; it does not determine boost action or a physical embedding.

### T049D — Lorentzian chirality

- Found a demonstrable convention error in the boost generator: the original script/theorem omitted the factor \(i\) in the Hermitian-commutator convention. This gave the wrong sign in the boost-boost commutator.
- Corrected the four-component generator to \(\mathcal K_i=\tfrac{i}{2}\gamma^0\gamma^i\), the induced Weyl generator to \(K_i^{(s)}=-\tfrac{i s}{2}\sigma_i\), and the explicit block matrix accordingly.
- Added regression tests for
  \[
  [J_i,J_j]=i\epsilon_{ijk}J_k,\quad
  [J_i,K_j]=i\epsilon_{ijk}K_k,\quad
  [K_i,K_j]=-i\epsilon_{ijk}J_k.
  \]
- Independent matrix calculations with the repository gamma matrices gave zero residual (to machine precision) for the Clifford anticommutators, both Weyl intertwiners, boost/rotation invariance, parity exchange, and the Lorentz commutators. The chirality-projector residual was approximately \(3.1\times10^{-16}\).
- The boost matrices are non-Hermitian in this finite-dimensional spinor basis; the factor \(i\) above fixes the stated commutator convention and must not be described as a unitarity statement.
- **Boundary:** the QLG source supplies only the spatial SU(2) action. Assigning either Weyl boost action is an extension, not a consequence of the QLG fibre alone; neither chirality is dynamically selected.

## Execution and reproducibility limits

- Source files and test files were read from the default branch after edits.
- Independent symbolic/algebraic reasoning and Python matrix calculations were performed for the identities described above.
- The repository's full pytest suite and GitHub Actions were **not executed** in this environment: a direct repository clone was unavailable because the execution environment could not resolve GitHub. The added/modified regression tests therefore still require execution in the repository CI or a local checkout.
- No physical NPZ data were available for T049A/T049B; no finite-data fit is reported as a physical result.

## Change ledger

- T047 wording and flat-FLRW hypothesis clarified.
- T048 calibration input validation hardened; regression tests extended.
- T049A mathematical display notation repaired.
- T049D boost-generator convention corrected in theorem, script, tests, and root README; Lie-algebra regression tests added.
- No change to the claimed physical scope of any record.
