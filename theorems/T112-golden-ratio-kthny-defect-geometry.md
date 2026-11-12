# T112 — Golden-ratio geometry as a controlled KTHNY defect-lattice comparison

**Classification:** exact algebraic properties of the proposed unimodular map; research protocol and falsifiable candidate; no KTHNY transition, golden scaling law, or physical relevance established.

**Dependencies:** T110 (2D torus vortices and KTHNY distinctions), T111 (GP zeros, with \(\Psi_{\rm GP}\) notation), the three-defect-gas dossier, and the canonical notation policy.

## 1. Question and scope

Does a two-dimensional crystal's defect geometry or elastic renormalization acquire a distinguished golden-ratio structure when its Burgers lattice is acted on by a golden-ratio hyperbolic automorphism?

This is a testable question, not a consequence of KTHNY. Standard KTHNY theory applies to two-dimensional crystals with translational and orientational order and distinguishes vector dislocations from disclinations. A triangular crystal is the control system. A Penrose-type quasiperiodic tiling is a separate comparison system: it has phason degrees of freedom and does not possess the ordinary rank-two translational lattice assumed by the elementary KTHNY Burgers-gas construction. Do not call its phason defects ordinary KTHNY dislocations without deriving the appropriate generalized elasticity.

The golden ratio is
\[
\varphi=\frac{1+\sqrt5}{2},\qquad
\varphi^2=\varphi+1.
\]
The supergolden constant remains distinct:
\[
\psi_{\rm SA}^3-\psi_{\rm SA}^2-1=0.
\]
T112 does not assume a relation between \(\varphi\) and \(\psi_{\rm SA}\).

## 2. Exact integer-lattice candidate

Consider the integer matrix
\[
A_\varphi=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
\]
Its characteristic polynomial is
\[
\det(\lambda I-A_\varphi)=\lambda^2-\lambda-1,
\]
so its eigenvalues are exactly
\[
\lambda_+=\varphi,\qquad
\lambda_-=-\varphi^{-1}.
\]
Moreover, \(\det A_\varphi=-1\), hence
\[
A_\varphi\in GL(2,\mathbb Z).
\]
It maps integer Burgers-coordinate vectors to integer Burgers-coordinate vectors and is invertible over the integer lattice. Its powers generate Fibonacci entries:
\[
A_\varphi^n=
\begin{pmatrix}
F_{n+1}&F_n\\F_n&F_{n-1}
\end{pmatrix},\qquad n\geq1,
\]
with \(F_0=0,F_1=1\).

**Important limitation:** \(A_\varphi\) is not an isometry of the Euclidean triangular-lattice metric. It is a hyperbolic lattice automorphism (a candidate imposed geometric deformation), not a symmetry of the ordinary isotropic triangular crystal. A golden eigenvalue in this matrix is therefore an input to the comparison, not evidence that an unmodified KTHNY system dynamically generates golden scaling.

## 3. Two-model design

### Model C — triangular-crystal KTHNY control

Use a periodic triangular lattice with primitive vectors
\[
a_1=a(1,0),\qquad a_2=a(1/2,\sqrt3/2).
\]
Represent dislocations by integer Burgers coordinates
\[
b=m a_1+n a_2,\qquad (m,n)\in\mathbb Z^2.
\]
Measure separately:
- Burgers charge and neutrality;
- disclination/Frank charge and orientational winding;
- elastic tensor and renormalized Young modulus;
- defect core energies and fugacities;
- pair correlations and finite-size scaling.

The KTHNY dislocation-unbinding diagnostic is
\[
K_R=\frac{Y_Ra^2}{k_BT}=16\pi,
\]
with renormalized Young modulus. This remains the reference criterion; do not substitute bare elastic constants.

### Model G — golden-deformed Burgers-coordinate comparison

Apply \(A_\varphi\) to Burgers coordinates, or equivalently compare the elastic theory under a declared pullback/pushforward of its metric and defect-charge basis. State explicitly which convention is used. For a coordinate pushforward,
\[
b' = A_\varphi b,\qquad
G' = A_\varphi^{-T}G A_\varphi^{-1}
\]
keeps the scalar quadratic form \(b^TGb\) invariant if both charge coordinates and metric are transformed consistently. This is a change of coordinates, not a new physical effect.

To test a physical anisotropic deformation instead, hold the laboratory metric fixed while changing the embedding or interaction kernel. Then the elastic tensor, allowed defect energies and RG flow must be recomputed; no invariance is presumed.

### Model Q — quasiperiodic comparison (optional, distinct theory)

For a Penrose/Ammann-type tiling, identify phonon and phason displacement fields, their coupled elastic constants, and the correct topological charge group before attempting an RG analysis. Fivefold local order and golden tile ratios alone do not supply a rank-two Burgers lattice or prove KTHNY universality. Report this as a generalized-quasicrystal elasticity problem, not as the triangular-crystal control.

## 4. Falsifiable numerical protocol

For each model and size:

1. Generate defect-free reference configurations and validate the primitive-cell geometry and periodic boundary conditions.
2. Insert isolated dislocation–antidislocation pairs with known integer Burgers coordinates; recover each charge from a closed Burgers circuit.
3. Insert isolated disclination pairs and recover Frank angle independently. Verify that Burgers and Frank estimators do not alias.
4. Compute the elastic Green kernel and pair interaction from the specified elastic tensor; compare measured pair free energies with the predicted vector Coulomb interaction.
5. Run the defect-gas sampling/RG analysis with declared core energies, fugacity normalization, update rules, independent seeds and finite-size sequence.
6. Compare Model C with (a) a pure coordinate transform by \(A_\varphi\), which must leave scalar predictions invariant when the metric is transformed consistently, and (b) a genuine fixed-laboratory-metric deformation, which may change anisotropic observables.
7. Test whether any golden ratio appears in an observable not inserted by construction: e.g. a converged ratio of independently measured correlation lengths, elastic eigenvalues, defect-pair scales, or RG crossover scales. Compare against rational/Fibonacci approximants and include uncertainty and null controls.

### Acceptance and rejection criteria

- **Exact algebra accepted:** characteristic polynomial, determinant, integer-lattice invertibility, and Fibonacci power identity.
- **Coordinate-covariance control accepted:** transformed quadratic energies agree to numerical tolerance when both coordinates and metric are transformed.
- **Golden physical scaling accepted only if:** a ratio converges toward \(\varphi\) under increasing sizes and independent seeds, survives changes of microscopic discretization, is not fixed by the imposed matrix, and beats non-golden/null models under a preregistered comparison.
- **Rejected:** a ratio found only in the entries/eigenvalues of the imposed \(A_\varphi\); a ratio that drifts with size; a ratio explained by a coordinate convention; or a Penrose tile-length ratio relabelled as a KTHNY critical exponent.

## 5. Connection to RGS–PRISM and the supergolden constant

Keep three objects separate:
1. \(\varphi\), the quadratic golden ratio;
2. \(\psi_{\rm SA}\), the supergolden constant defined by \(s^3-s^2-1=0\);
3. the spectrum of the RGS–PRISM operator(s), including any operator satisfying \(K^3=K^2+I\).

A spectral value \(\lambda\) satisfying the cubic is a supergolden eigenvalue only if the operator identity and the relevant invariant subspace are established. The cubic relation for an operator does not imply that the KTHNY elastic flow has the same eigenvalue. A cross-map must specify a chain map or an intertwiner and prove compatibility with the defect charge lattice and elastic energy.

Candidate bridge to test:
\[
\text{Burgers lattice}
\xrightarrow{\;A_\varphi\;}
\text{integer defect coordinates}
\xrightarrow{\;\text{elastic Green operator}\;}
\text{vector Coulomb gas}
\xrightarrow{\;\text{RG}\;}
(Y_R,\,y_R,\,\ldots).
\]
Only after this chain is derived may one compare its spectral/scaling data with PRISM operators and \(\psi_{\rm SA}\).

## 6. Deliverables and status

- exact symbolic audit of \(A_\varphi\), determinant, eigenvalues and Fibonacci powers;
- triangular-crystal defect-charge benchmark;
- coordinate-covariance null test;
- separately specified physical anisotropy experiment;
- optional quasicrystal phonon–phason extension;
- finite-size RG results only after the model and sampling implementation are available.

**Current status:** exact matrix identities are proved by direct algebra. The physical golden-ratio/KTHNY connection is a candidate research question. No new Monte Carlo simulation, transition estimate, universal golden exponent, or RGS–PRISM-to-KTHNY theorem is claimed.

## References

1. D. R. Nelson, B. I. Halperin, “Dislocation-mediated melting in two dimensions,” *Physical Review B* 19 (1979), 2457–2484.
2. A. P. Young, “Melting and the vector Coulomb gas in two dimensions,” *Physical Review B* 19 (1979), 1855–1866.
3. B. I. Halperin, D. R. Nelson, “Theory of two-dimensional melting,” *Physical Review Letters* 41 (1978), 121–124.
4. M. Baake, U. Grimm, *Aperiodic Order*, Vol. 1, Cambridge University Press (2013), for the distinct phonon–phason framework of quasiperiodic order.
