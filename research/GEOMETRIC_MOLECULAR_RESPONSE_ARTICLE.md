# Geometric molecular response: a unified research article and evidence ledger

**Author:** Fabian Leo Naressi  
**Status:** integrated research manuscript — mixed evidence levels; not a theorem or established physical law.  
**Scope:** assemble the De Aquino prolate geometry, the H₂⁺ numerical benchmark, the neutral-H₂ and LiH tests, the Naressi–Harrabi phenomenological phase response, and a testable anisotropic-vesica geometry. Related Q6 transport and zeta–electromagnetism results are recorded as separate mathematical connections, not silently identified with molecular response.

## Abstract

We formulate a fixed geometric observable for diatomic electronic states using prolate spheroidal coordinates and the threshold \(\xi_\star=\sqrt5/2\). The threshold determines a confocal ellipsoidal region and an associated angular reference measure. For H₂⁺, a prolate-coordinate Rayleigh–Ritz calculation gives a molecular-distance sweep of the regional probability and its static electric-field curvature; comparison with published fixed-nuclei dipole polarizabilities yields a strong but provisional power-law correlation over nine points. This is a single-system empirical fit and does not establish a universal law. We specify the correlated two-electron H₂ test, retain LiH as the planned heteronuclear test, and state the numerical convergence criteria required before promotion of the relation. We also recover the phenomenological Naressi–Harrabi phase ansatz and introduce a precise, falsifiable extension in which the molecular overlap lens is characterized by a density-weighted anisotropy tensor. The affine geometry is a model to test, not an established physical deformation. Q6 gradient/baricenter, hypercube, Green–Kubo, and zeta–electromagnetism results remain separate mathematical connections.

## 1. Research question and evidence discipline

The central question is whether a geometric regional electronic observable, defined with one fixed threshold and no system-dependent refitting, tracks a measurable molecular response such as dipole-polarizability anisotropy.

The programme is organized into five distinct layers:

1. **Geometry:** exact coordinate identities, the chosen threshold, and its induced measure.
2. **Molecular computation:** wavefunctions, regional probabilities, field derivatives, and published polarizability benchmarks.
3. **Anisotropic overlap geometry:** a density-defined shape tensor and its comparison with an area-preserving affine deformation.
4. **Phenomenology:** empirical fits and candidate scaling relations.
5. **Cross-domain connections:** phase-response ansätze, spectral/zeta constructions, and discrete transport identities.

The labels used below are:
- **Analytic identity:** follows exactly from definitions or standard mathematics.
- **Published benchmark:** value or method reported in a cited source.
- **Numerical result:** obtained in the stated calculation, subject to its convergence record.
- **Empirical candidate:** fitted relation supported by a finite dataset only.
- **Open hypothesis:** not yet tested or not yet derived.

No empirical fit is called a law. No molecular result is inferred from a gravitational-wave phase ansatz. No connection between zeta values and electromagnetic response is promoted to a derivation unless an operator identity and its domain are supplied.

## 2. Prolate geometry and the fixed De Aquino threshold

For two nuclei at \(z=\pm R/2\), define prolate spheroidal coordinates by
\[
\xi=\frac{r_A+r_B}{R},\qquad
\eta=\frac{r_A-r_B}{R},\qquad \phi\in[0,2\pi).
\]
The coordinate ranges are \(1\leq\xi<\infty\), \(-1\leq\eta\leq1\). In cylindrical coordinates,
\[
z=\frac R2\xi\eta,\qquad
s=\frac R2\sqrt{(\xi^2-1)(1-\eta^2)},
\]
and the volume element is
\[
dV=\frac{R^3}{8}(\xi^2-\eta^2)\,d\xi\,d\eta\,d\phi.
\]
These are analytic coordinate identities.

We adopt the fixed threshold
\[
\boxed{\xi_\star=\frac{\sqrt5}{2}}.
\]
At this shell the ellipsoid has semimajor axis \(a=\sqrt5R/4\), semiminor axis \(b=R/4\), focal half-distance \(c=R/2\), aspect ratio \(a/b=\sqrt5\), and eccentricity \(e=2/\sqrt5\). This geometric choice is a postulate of the research programme; its physical significance is what the molecular tests are intended to assess.

### 2.1 Reference angular measure on the shell

Using the prolate volume-Jacobian factor evaluated at \(\xi_\star\), the normalized conditional angular density for a uniform reference amplitude on the shell is
\[
p_0(\eta)=\frac3{22}(5-4\eta^2),\qquad -1\leq\eta\leq1.
\]
For \(u=(1+\eta)/2\),
\[
p_0(u)=\frac3{11}+\frac{48}{11}u(1-u)
=\frac3{11}\,\mathrm{Beta}(1,1)+\frac8{11}\,\mathrm{Beta}(2,2).
\]
Its moments are
\[
\mathbb E_0[\eta]=0,\qquad
\mathbb E_0[\eta^2]=\frac{13}{55},\qquad
\mathbb E_0[\eta^4]=\frac9{77}.
\]
The fourth moment is \(9/77\), not \(17/231\). These are exact integrals for this reference measure. The measure is induced by the prolate volume Jacobian; it is **not** the Euclidean surface-area measure of the ellipsoid.

For a molecular wavefunction, the actual shell-weighted moments are state-dependent:
\[
M_{2k}(R)=
\frac{\int_{-1}^{1}\eta^{2k}(\xi_\star^2-\eta^2)
|\Psi(\xi_\star,\eta;R)|^2\,d\eta}
{\int_{-1}^{1}(\xi_\star^2-\eta^2)
|\Psi(\xi_\star,\eta;R)|^2\,d\eta}.
\]
The reference value \(13/55\) is therefore a geometric baseline, not a universal prediction for a molecular state.

## 3. Molecular observable and electric-field response

For a normalized electronic state in an applied static field \(F\), define the regional probability
\[
P_{\rm DA}(F,R)=
\frac{\int_{\xi\leq\xi_\star}|\Psi_F(\mathbf r;R)|^2d^3r}
{\int |\Psi_F(\mathbf r;R)|^2d^3r},
\]
for a one-electron problem. The regional curvature is
\[
\boxed{\chi_{\rm DA}(R)=
\left.\frac{\partial^2P_{\rm DA}(F,R)}{\partial F^2}\right|_{F=0}.}
\]
In atomic units, its numerical dimensions follow from the chosen field convention. It is a curvature of a regional probability, not the conventional dipole polarizability.

For an inversion-symmetric nondegenerate ground state, \(P(F,R)=P(-F,R)\), so the first derivative at zero field vanishes. A central finite-difference estimate is
\[
\chi_{\rm DA}(R;F)=
\frac{P(F,R)+P(-F,R)-2P(0,R)}{F^2}.
\]
It must be checked over decreasing \(F\), with basis and quadrature convergence. The sign and magnitude are outputs, not assumptions.

For H₂, the normalized two-electron wavefunction gives the spin-summed one-electron density
\[
\rho_F(\mathbf r;R)=2\int|\Psi_F(\mathbf r,\mathbf r_2;R)|^2d^3r_2,
\qquad \int\rho_Fd^3r=2,
\]
and the electron fraction is
\[
P_{\rm DA}^{H_2}(F,R)=\frac12
\int_{\xi\leq\xi_\star}\rho_F(\mathbf r;R)d^3r.
\]
The factor \(1/2\) ensures a fraction between zero and one. The full two-electron Coulomb interaction must be retained.

## 4. Anisotropic vesica, deformed flower-of-life, and multioverlap regions

### 4.1 Geometric definition: start from the planar lens

A vesica piscis is defined here in a specified plane as the intersection of two equal disks whose centres are separated by a distance \(R\) and whose radii are \(R\):
\[
D_A=\{x\in\mathbb R^2:|x-a_A|\leq R\},\qquad
D_B=\{x\in\mathbb R^2:|x-a_B|\leq R\},\qquad
|a_A-a_B|=R,
\]
\[
\Omega_2=D_A\cap D_B.
\]
The symbol \(\Omega_2\) denotes a two-centre overlap lens (the biveca in the terminology of this programme). For three disks, define
\[
\Omega_3=D_1\cap D_2\cap D_3,
\]
and for \(N\) disks, \(\Omega_N=\bigcap_{j=1}^N D_j\), whenever the intersection has nonzero area. “Biveca”, “triveca”, and “poliveca” are programme-specific labels, not standard names in molecular quantum chemistry. The definitions above, rather than the labels, carry the mathematical content.

This construction must not be confused with the prolate ellipsoid \(\xi=\xi_\star\): the latter is a three-dimensional two-focus coordinate surface, while the vesica above is a planar intersection of disks. A link between them requires an explicit projection or section map.

### 4.2 Density-weighted shape tensor

For a molecular state, choose a plane \(\Pi\) containing the internuclear axis and one fixed transverse direction. Let \(\rho_\Pi(u,v;R)\) be the electronic density projected onto this plane by integrating the three-dimensional density along the normal direction. Restrict it to a declared overlap region \(\Omega_2(R)\), and define
\[
N_\Omega=\int_{\Omega_2}\rho_\Pi(q;R)\,d^2q,\qquad
\bar q=\frac1{N_\Omega}\int_{\Omega_2}q\rho_\Pi(q;R)\,d^2q,
\]
\[
Q(R)=\frac1{N_\Omega}\int_{\Omega_2}
(q-\bar q)(q-\bar q)^T\rho_\Pi(q;R)\,d^2q.
\]
Here \(Q\) is a symmetric positive-semidefinite 2×2 covariance tensor, provided \(N_\Omega>0\). Its eigenvalues \(\lambda_+\geq\lambda_->0\) and eigenvectors give the principal density-spread directions inside the chosen lens. If \(\lambda_-=0\), the logarithmic anisotropy below is undefined and the data must be reported as degenerate rather than regularized silently.

Define the dimensionless shape anisotropy
\[
\mathcal A_Q=\frac{\lambda_+-\lambda_-}{\lambda_++\lambda_-},
\qquad
\epsilon_Q=\frac14\log\frac{\lambda_+}{\lambda_-}.
\]
The factor \(1/4\) is deliberate. Under a planar area-preserving affine map
\[
A(\epsilon,\theta)=
R(\theta)
\begin{pmatrix}e^\epsilon&0\\0&e^{-\epsilon}\end{pmatrix}
R(\theta)^T,\qquad\det A=1,
\]
an initially isotropic covariance \(Q_0=\sigma^2I\) transforms as \(Q=AQ_0A^T\), so its eigenvalue ratio is \(e^{4|\epsilon|}\). Thus \(\epsilon_Q\) recovers the magnitude of the affine strain in this idealized isotropic-reference case. It is not generally a unique physical strain when the undeformed density is already anisotropic.

The principal angle \(\theta_Q\) is the orientation of the eigenvector for \(\lambda_+\), defined modulo \(\pi\). A sign/orientation convention must be fixed consistently across internuclear distances. For a heteronuclear molecule, the centroid \(\bar q\) need not coincide with the midpoint; this displacement is a separate observable and must not be folded into \(Q\).

### 4.3 Deformed flower-of-life as an affine construction

A global affine map sends every circle in a planar flower-of-life arrangement to an ellipse. If the same matrix \(A\) is applied to all centres and all points, incidence and intersection are preserved under the invertible map, although angles and Euclidean lengths are not. This gives a mathematically exact model of a globally deformed pattern.

A spatially varying field \(A(q)\) is a different construction: it is not automatically the image of one global affine map, and it may fail to define a globally integrable coordinate transformation. To interpret it as a physical deformation, one must specify a displacement field, compatibility conditions, and the induced metric. A collection of locally chosen ellipses alone is not a deformation theorem.

The molecular proposal is therefore precise but limited: compare the density-derived \(Q(R)\) with the affine reference family, and test whether the principal strain, orientation, and centroid shift track the independently computed electronic response. Do not assume that chemical coupling literally deforms a classical flower-of-life lattice.

### 4.4 Candidate molecular relation and falsification

A candidate extension is
\[
\Delta\alpha(R)=C\,|\chi_{\rm DA}(R)|^p
G\!\left(\epsilon_Q(R),\theta_Q(R),\frac{|\bar q-q_{\rm mid}|}{R}\right),
\]
where \(G\) is a dimensionless function to be selected and tested, not prescribed to force agreement. The simpler isotropic candidate corresponds to \(G=1\). Fit parameters must be learned on one set of molecules and evaluated on held-out molecular systems; a fit across many internuclear distances of one molecule is not independent cross-system validation.

The first concrete calculation is to evaluate \(Q(R)\), \(\mathcal A_Q(R)\), \(\epsilon_Q(R)\), and \(\theta_Q(R)\) from the existing H₂⁺ wavefunctions at the same nine separations as the regional-probability scan. Then compare them with \(M_2(R)\), \(P_{DA}(R)\), \(\chi_{DA}(R)\), and the published \(\Delta\alpha(R)\). This calculation is **not yet performed** in the archived record. No numerical anisotropy values are asserted here.

A meaningful test must also vary the overlap-region definition (disk radii and plane choice) as a sensitivity analysis, while keeping the primary definition fixed before inspecting the polarizability fit. Otherwise the geometry could be tuned post hoc. H₂ and LiH then provide the independent-system tests. If \(Q\) adds no out-of-sample predictive value beyond \(R\) or \(\chi_{DA}\), the anisotropic-geometry extension should be rejected or narrowed.

## 5. H₂⁺: one-electron benchmark

### 5.1 Hamiltonian and numerical representation

At fixed nuclear separation, the Born–Oppenheimer electronic Hamiltonian in a uniform axial field is
\[
H(F;R)=-\frac12\nabla^2-\frac1{r_A}-\frac1{r_B}+Fz,
\]
with nuclear repulsion \(1/R\) added to report the total BO energy. A prolate-coordinate Ritz representation used in the working calculation is
\[
\Psi(\xi,\eta)=e^{-\kappa\xi}
\sum_{n=0}^{N_\xi-1}\sum_{\ell=0}^{N_\eta-1}
c_{n\ell}L_n(2\kappa(\xi-1))P_\ell(\eta).
\]
The zero-field ground state is even in \(\eta\); the field response requires odd angular components as well.

The total BO energy at \(R=2a_0\) was computed as
\[
E_{\rm BO}=-0.6026342144948114\ E_h,
\]
in agreement to approximately \(10^{-13}E_h\) with the Tsogbayar value obtained from the reported electronic energy \(-1.10263421449494646150\) Ry plus \(1/R\). At \(R_e=1.997193a_0\), the working result is
\[
E_{\rm BO}=-0.602634619106\ E_h,
\]
consistent with the high-accuracy reference \(-0.602634619105\ E_h\). These are numerical working-session results and should be archived with the executable code, basis details, and convergence tables before being treated as independently reproducible repository results.

### 5.2 Regional probability and field curvature

The one-electron regional probability is
\[
P_{\rm DA}(F,R)=
\frac{\int_1^{\xi_\star}\int_{-1}^{1}
|\Psi_{F,R}|^2(\xi^2-\eta^2)\,d\eta\,d\xi}
{\int_1^{\infty}\int_{-1}^{1}
|\Psi_{F,R}|^2(\xi^2-\eta^2)\,d\eta\,d\xi},
\]
where the common azimuthal and dimensional constants cancel. The working nine-point scan is:

| \(R/a_0\) | \(E_{BO}/E_h\) | \(M_2\) | \(M_2-13/55\) | \(P_{DA}(0,R)\) | \(|\chi_{DA}(R)|\) |
|---:|---:|---:|---:|---:|---:|
| 1.0 | -0.451786313356 | 0.2518410323 | 0.0154773959 | 0.0478889100 | 0.1250353637 |
| 1.3 | -0.552740621876 | 0.2607765712 | 0.0244129348 | 0.0699109594 | 0.3172860575 |
| 1.5 | -0.582323205453 | 0.2676214819 | 0.0312578455 | 0.0844823613 | 0.5455267998 |
| 1.8 | -0.600253634102 | 0.2791954030 | 0.0428317666 | 0.1057850486 | 1.1344604771 |
| 2.0 | -0.602634214495 | 0.2877834257 | 0.0514197894 | 0.1195136777 | 1.7747967065 |
| 2.3 | -0.598930886158 | 0.3019864601 | 0.0656228237 | 0.1393258040 | 3.3174740799 |
| 2.5 | -0.593823510991 | 0.3123432619 | 0.0759796255 | 0.1520057617 | 4.9126876830 |
| 2.8 | -0.584356003468 | 0.3292127896 | 0.0928491532 | 0.1702515275 | 8.6001931185 |
| 3.0 | -0.577562864049 | 0.3413385954 | 0.1049749590 | 0.1819203464 | 12.2937250859 |

The scan used basis refinements (including 5×7, 7×9 and 8×11 tests) and a central finite-field response. A complete archival release still needs the raw basis-by-basis convergence table, field-step sequence, quadrature settings, and code. The listed \(M_2\) is the shell moment weighted by the prolate Jacobian and wavefunction density, not a Euclidean ellipsoid surface moment.

### 5.3 Published H₂⁺ polarizability benchmark

Tsogbayar reports fixed-nuclei static dipole polarizabilities for the \(1s\sigma\) state. Values below are in \(a_0^3\); \(\Delta\alpha=\alpha_\parallel-\alpha_\perp\).

| \(R/a_0\) | \(\alpha_\parallel\) | \(\alpha_\perp\) | \(\Delta\alpha\) |
|---:|---:|---:|---:|
| 1.0 | 1.1195940 | 0.7762294 | 0.343365 |
| 1.3 | 1.7981683 | 1.0322175 | 0.765951 |
| 1.5 | 2.44196012 | 1.22321099 | 1.218749 |
| 1.8 | 3.8089455 | 1.5354815 | 2.273464 |
| 2.0 | 5.0776490 | 1.7576486 | 3.320001 |
| 2.3 | 7.7249621 | 2.1056348 | 5.619327 |
| 2.5 | 10.149485 | 2.3434247 | 7.806061 |
| 2.8 | 15.154185 | 2.7014497 | 12.452735 |
| 3.0 | 19.699506 | 2.9366088 | 16.762897 |

These are literature values, not outputs of the present Ritz scan. The comparison is fixed-nuclei electronic response; it must not be described as a rovibrational polarizability.

### 5.4 Empirical relation: provisional, not universal

A nine-point log-space fit from the working session gives
\[
\boxed{\Delta\alpha_{H_2^+}(R)\simeq
2.02465\,|\chi_{\rm DA}^{H_2^+}(R)|^{0.846833}.}
\]
Reported diagnostics: \(R^2_{\log}=0.9999593\), maximum leave-one-out relative error about \(2.53\%\). A separate fit against \(M_2-13/55\) gave exponent about \(2.03997\), \(R^2_{\log}\approx0.997166\), with maximum leave-one-out error about \(20\%\).

This is an **empirical candidate on one molecule and one smooth distance sweep**. The points are not independent molecular systems; smooth covariation with \(R\) can produce an impressive fit. No universal exponent, coefficient, or causal mechanism has been established. The data and fitting script must be archived before publication as a reproducible numerical claim.

## 6. Neutral H₂ and heteronuclear LiH: decisive tests

### 6.1 Neutral H₂

At fixed \(R\), the two-electron BO Hamiltonian in atomic units is
\[
H(F;R)=-\frac12(\nabla_1^2+\nabla_2^2)
-\sum_{i=1}^{2}\left(\frac1{r_{iA}}+\frac1{r_{iB}}\right)
+\frac1{r_{12}}+\frac1R+F(z_1+z_2).
\]
The target is the correlated \(X\,{}^1\Sigma_g^+\) state. The regional probability and response are defined in Section 3 using the spin-summed one-electron density. Inversion symmetry requires an even regional probability in \(F\).

Zammit et al. (2017), Table II, reports fixed-nuclei H₂ polarizabilities and comparison values attributed to Kolos–Wolniewicz. The following are the **Kolos–Wolniewicz comparison columns**, not the authors' separate “Present” model values:

| \(R/a_0\) | \(\alpha_\parallel\) | \(\alpha_\perp\) | \(\Delta\alpha\) |
|---:|---:|---:|---:|
| 0.8 | 3.204 | 2.783 | 0.421 |
| 1.0 | 4.088 | 3.341 | 0.747 |
| 1.2 | 5.147 | 3.944 | 1.203 |
| 1.4 | 6.380 | 4.578 | 1.802 |
| 1.6 | 7.781 | 5.228 | 2.553 |
| 1.8 | 9.320 | 5.878 | 3.442 |
| 2.0 | 10.964 | 6.511 | 4.453 |
| 2.2 | 12.638 | 7.110 | 5.528 |

The correlated H₂ density response \(\chi_{\rm DA}^{H_2}(R)\) has **not yet been computed**. Required methods include explicitly correlated Gaussians, Hylleraas functions, or a converged prolate-coordinate CI with explicit electron–electron Coulomb integrals. Energy convergence alone is insufficient: the regional density response must itself converge with basis, quadrature, and field step. Do not fill this missing column by scaling the H₂⁺ answer.

### 6.2 LiH

LiH is the planned heteronuclear extension. The same dimensionless prolate coordinate and fixed threshold should be retained, with the internuclear axis and origin explicitly defined. Unlike H₂ and H₂⁺, inversion symmetry about the bond midpoint is absent; a linear-in-field term in the regional probability may therefore occur. Report both
\[
\left.\partial_F P_{DA}\right|_{0}
\quad\text{and}\quad
\left.\partial_F^2P_{DA}\right|_{0}.
\]
The LiH test must use a correlated electronic treatment and independent fixed-nuclei polarizability benchmarks. It must not be replaced by HeH⁺ merely for computational convenience: LiH is the originally selected heteronuclear target.

## 7. Naressi–Harrabi phenomenological phase response

The formula recovered from the 23 October 2026 working record is
\[
\boxed{
\Delta\Psi_{\rm NH}(f)=
\beta_{\rm NH}x^{-4/3}
\operatorname{Re}\!\left[
\frac{1}{1-(x/\omega_0)^2+i\gamma x/\omega_0^2}
\right],
\qquad
x=\frac{2\pi GM_{\rm det}f}{c^3}.
}
\]
The recorded parameter values were
\[
\omega_0=1.506372,\qquad \gamma=0.05,
\]
with \(\beta_{\rm NH}\) a dimensionless phenomenological amplitude under this dimensionless-frequency convention. A prior used in that analysis was uniform on \([-\beta_{\max},+\beta_{\max}]\). The factor \(x^{-4/3}\) is the stated 0.5PN-like frequency scaling in the model.

Important interpretation limits:
- \(\beta_{\rm NH}\) is a free phenomenological amplitude, not a derived coupling constant.
- \(\omega_0\) is a nominal response scale. With nonzero \(\gamma\), the real part of the response factor vanishes at \(x=\omega_0\); it is not automatically the phase-peak frequency.
- \(\gamma\) regularizes/broadens the denominator. It is not automatically a quasinormal-mode damping rate or quality-factor parameter.
- The historical discussion explored frequency-to-Hz interpretations (including roughly 110.8 Hz and 700 Hz for a 30-solar-mass example), but the physical anchoring of \(\omega_0\) was unresolved. Those conversions must not be presented as validated predictions.
- Earlier shorthand forms such as \(f^{-4/3}/(1-f^2/\omega_0^2)\) omit the dimensionless-frequency convention and regularization and are not the preferred definition.

This phase ansatz is a **candidate phenomenological model**, not a consequence of the molecular De Aquino construction. The molecular and gravitational-wave sectors may be compared only after a common response-theoretic derivation is supplied. No verified Green–Kubo or Dedekind-eta identity for this phase law was present in the recovered record.

## 8. Related mathematical programme: links, not conflations

The following results belong to the user's wider mathematical programme and are relevant as possible structural analogies or future derivation routes. They are not evidence that the molecular fit or the Naressi–Harrabi phase law is already derived.

### 8.1 Q6 gradients and barycentres

The recorded Q6 results include the six-dimensional hypercube barycentre
\[
\bar x=(1/2,\ldots,1/2),
\]
coordinate covariance \(\operatorname{Cov}(X)=\tfrac14 I_6\), and for a coordinate gradient \(e_a\), a discrete edge-gradient supported on the 32 edges parallel to coordinate \(a\), zero on the other 160 edges, with discrete Dirichlet energy 16 under the recorded normalization. These are discrete-geometric results. Their exact definitions, boundary conventions, and normalization must accompany any reuse; they do not imply a molecular force law without a map between the discrete and continuum operators.

### 8.2 Green–Kubo transport

The standard Green–Kubo shear-viscosity expression is
\[
\eta=\frac{1}{k_BT V}\int_0^\infty
\langle\delta\Pi_{xy}(t)\delta\Pi_{xy}(0)\rangle\,dt,
\]
with a corresponding resolvent representation of the form
\[
\langle J,(-L)^{-1}J\rangle
\]
when the generator, invariant measure, domain, and normalization make that representation valid. The Q6 phonon–phason transport record (T131) is a discrete-model construction. It should be cited as such and not described as experimental validation of a molecular or gravitational response law.

### 8.3 Zeta–electromagnetism bridge

The previously explored bridge uses Fibonacci transfer matrices, a boundary response involving \(Q\cot Q\), the cotangent expansion and its zeta-value coefficients, and a radial Maxwell operator on an Ellis–Bronnikov geometry. This is a mathematical/spectral construction. It is not a Hilbert–Pólya result, and it does not by itself establish that the molecular polarizability or the Naressi–Harrabi phase amplitude is determined by zeta values.

### 8.4 Hypercube and related discrete laws

The Q6/PRISM programme contains graph-theoretic spectra, hypercube constructions, and discrete geometric identities. They can enter this article as a separate mathematical framework only when the specific graph, operator, normalization, and map to the molecular observable are stated. Numerical coincidences between constants are not derivations.

## 9. Falsifiable programme and acceptance criteria

The research sequence is:

1. Archive the H₂⁺ solver, basis definitions, quadrature, field-step scan, and all convergence tables. Reproduce the nine-point table and fit from source code.
2. Compute the density-weighted overlap tensor \(Q(R)\) on the same H₂⁺ wavefunctions, using the fixed planar lens and projection convention in Section 4. Archive the projected density and integration mesh.
3. Compute correlated H₂ \(P_{DA}(F,R)\) and \(\chi_{DA}(R)\) with the fixed \(\xi_\star\), validating energies and polarizabilities first.
4. Compare H₂⁺ and H₂ without refitting the threshold. Report whether one common exponent/coefficient is supported; do not impose the H₂⁺ fit as a prior.
5. Compute LiH as the heteronuclear test, retaining the same threshold and reporting both first- and second-order field responses.
6. Evaluate whether \(Q\) adds predictive value beyond \(R\), \(M_2\), and \(\chi_{DA}\) on held-out molecular systems. Reject the anisotropic extension if it does not improve out-of-sample prediction.
7. Only after independent systems agree should a cross-molecular scaling law be proposed. Use uncertainty propagation, ordinary and log residuals, leave-one-system-out prediction, and a clearly stated model-selection baseline.
8. Treat the Naressi–Harrabi phase ansatz as an independent phenomenological sector until a derivation connects its response kernel to a specified operator or correlation function.
9. Keep the Q6/Green–Kubo and zeta–electromagnetism work in a mathematically explicit companion section or companion paper unless a rigorous bridge is supplied.

## 10. Evidence ledger

| Claim or object | Status | What is still needed |
|---|---|---|
| Prolate coordinate map and volume Jacobian | Analytic identity | None |
| \(\xi_\star=\sqrt5/2\), ellipsoid ratios | Adopted geometric hypothesis plus exact geometry | Physical justification/test |
| Reference density and moments \(13/55,9/77\) | Exact integrals for the specified measure | None; preserve measure convention |
| Planar vesica as disk intersection | Exact geometric definition | Fix plane/radii for each molecular test |
| Density covariance \(Q\) and affine strain relation | Exact tensor definition; affine-reference model | Compute from molecular density |
| Flower-of-life affine image | Exact global affine geometry | Physical displacement/metric for nonuniform case |
| Biveca/triveca/poliveca terminology | Programme-specific definitions | Do not present as standard chemistry nomenclature |
| H₂⁺ energy at \(R=2\) and near equilibrium | Numerical working result matching literature | Solver/code and full convergence archive |
| H₂⁺ nine-point \(P_{DA},\chi_{DA},M_2\) scan | Numerical working result | Raw files, basis/field convergence, executable script |
| Tsogbayar H₂⁺ polarizability table | Published benchmark | Full bibliographic citation |
| H₂⁺ power fit | Empirical candidate | Independent molecular systems |
| H₂ polarizability table | Published benchmark | Resolve original Kolos–Wolniewicz reference details |
| Correlated H₂ \(\chi_{DA}\) | Open | Perform calculation |
| LiH cross-system test | Open | Perform calculation |
| H₂⁺ density anisotropy tensor \(Q(R)\) | Open | Perform projected-density integration |
| Naressi–Harrabi phase expression | Phenomenological ansatz recovered from working record | Original PDF/page audit and independent data analysis |
| Q6 gradient/baricentre identities | Discrete mathematical result | Attach exact definitions and source artifact |
| Q6 Green–Kubo transport | Discrete-model construction | Operator/domain and numerical validation |
| Zeta–electromagnetism bridge | Mathematical/spectral construction | Full derivation and independent checks |
| Universal molecular response law | Open hypothesis | Independent H₂ and LiH validation |

## 11. References

1. B. Tsogbayar, “Static dipole polarizability for the 1sσ electronic state of the H₂⁺ molecular ion,” *Journal of Physics B: Atomic, Molecular and Optical Physics* **42** (2009), 165007. DOI: [10.1088/0953-4075/42/16/165007](https://doi.org/10.1088/0953-4075/42/16/165007).
2. M. C. Zammit et al., *Physical Review A* **95** (2017), 022707. DOI: [10.1103/PhysRevA.95.022707](https://doi.org/10.1103/PhysRevA.95.022707). Table II contains H₂ fixed-nuclei polarizability data and Kolos–Wolniewicz comparison values. Verify the article title and full author list against the publisher record before journal submission.
3. W. Kolos and L. Wolniewicz, high-accuracy H₂ calculations cited in the comparison column of Zammit et al.; original reference details must be resolved from that paper's bibliography before final publication.
4. Green, M. S. (1954), “Markoff Random Processes and the Statistical Mechanics of Time-Dependent Phenomena. II. Irreversible Processes in Fluids,” *Journal of Chemical Physics* **22**, 398–413. DOI: [10.1063/1.1740082](https://doi.org/10.1063/1.1740082).
5. Kubo, R. (1957), “Statistical-Mechanical Theory of Irreversible Processes. I. General Theory and Simple Applications to Magnetic and Conduction Problems,” *Journal of the Physical Society of Japan* **12**, 570–586. DOI: [10.1143/JPSJ.12.570].


6. For the two-centre H₂⁺ problem, confocal prolate spheroidal coordinates and their use in separating the one-electron Schrödinger equation and evaluating orbital-overlap integrals are standard; see the molecular-orbital treatment in *Quantum Mechanics*, Chapter 39, “The Molecular Orbital Method, the Hydrogen Molecular Ion, and Overlap Integrals” (online text), https://mochizuki-tus.github.io/QM_Textbook_EN/ch39_molecular_orbital_h2plus.html. This supports the coordinate framework, not the proposed density-anisotropy law.

**Publication note.** This manuscript is an integrated research record, not yet a journal-ready claim of a new physical law. Before external submission, attach the original 23 October 2026 PDF for the Naressi–Harrabi expression, archive the H₂⁺ numerical code/data, resolve the full H₂ reference list, and replace all “working-session result” labels only when the corresponding reproducibility package is committed.
