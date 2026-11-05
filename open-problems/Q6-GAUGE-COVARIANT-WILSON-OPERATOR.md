# Q6 gauge-covariant Wilson operator — construction audit

**Status:** exact algebraic identities proved for the explicitly defined periodic cubical lattice and unitary link variables. The accompanying finite tests are numerical verification only. This is not yet a continuum-limit theorem, a 3+1-dimensional model, or a QCD result.

## 1. Domain and conventions

Fix an integer \(n\geq2\), lattice side length \(L=2n\), spacing \(h=1/n\), and
\[
\Lambda_n=(\mathbb Z/L\mathbb Z)^6,\qquad
\mathcal H_n=\ell^2(\Lambda_n)\otimes\mathbb C^8\otimes\mathbb C^3.
\]
The eight-dimensional spin factor carries Hermitian Euclidean generators
\[
\Gamma_i^\dagger=\Gamma_i,\qquad
\{\Gamma_i,\Gamma_j\}=2\delta_{ij}I_8,\quad i,j=1,\ldots,6.
\]
Color is the fundamental representation of \(SU(3)_C\). For every positive oriented link \((x,x+e_i)\), choose \(U_i(x)\in SU(3)\). The reverse link is, by definition, \(U_i(x-e_i)^\dagger\).

Use the counting inner product on lattice sites and the standard Hermitian inner products on spin and color. No continuum measure factor is needed for the finite-dimensional adjoint identities.

## 2. Covariant shifts

Define the forward and backward parallel-transport shifts by
\[
(S_i^U\psi)(x)=U_i(x)\psi(x+e_i),
\qquad
((S_i^U)^\dagger\psi)(x)=U_i(x-e_i)^\dagger\psi(x-e_i).
\]
The second identity follows by changing the summation variable in the lattice inner product and using unitarity of every link. In particular, \(S_i^U\) is unitary and \((S_i^U)^\dagger\) is exactly the reverse-edge shift.

For a sitewise gauge transformation \(g:\Lambda_n\to SU(3)\), let
\[
\psi^g(x)=g(x)\psi(x),\qquad
U_i^g(x)=g(x)U_i(x)g(x+e_i)^\dagger.
\]
Then
\[
S_i^{U^g}\psi^g(x)=g(x)S_i^U\psi(x),
\quad\text{or}\quad
S_i^{U^g}G=G S_i^U,
\]
where \(G\) is multiplication by \(g(x)\). The same intertwining identity holds for the adjoint shifts.

## 3. Dirac–Wilson operator

Define
\[
D_{\mathrm{naive}}^U
=\frac1{2h}\sum_{i=1}^6\Gamma_i
\big(S_i^U-(S_i^U)^\dagger\big),
\]
\[
W^U=\frac r{2h}\sum_{i=1}^6
\big(2I-S_i^U-(S_i^U)^\dagger\big),\qquad r>0,
\]
and
\[
D_W^U=m_0I+D_{\mathrm{naive}}^U+W^U.
\]
All shifts act trivially on spin; the \(\Gamma_i\) act trivially on color. This convention fixes the sign, orientation, and normalization that were left schematic in T014.

At \(U_i(x)=I_3\), the Fourier symbols are
\[
D_{\mathrm{naive}}(p)=\frac{i}{h}\sum_i\Gamma_i\sin p_i,
\qquad
W(p)=\frac r h\sum_i(1-\cos p_i).
\]
They agree with the free symbol convention in T017. At the corner \(p_i=\pi\epsilon_i\), the Wilson contribution is \(2r|\epsilon|/h\).

## 4. Exact identities

### Theorem A — gauge covariance

For every sitewise \(g\), every link field \(U\), and every spinor \(\psi\),
\[
D_W^{U^g}(G\psi)=G(D_W^U\psi).
\]

**Proof.** The forward-shift intertwining identity above and its adjoint imply covariance of each summand in \(D_{\mathrm{naive}}^U\) and \(W^U\). The mass term commutes with \(G\). Summing proves the claim. \(\square\)

### Theorem B — adjoint and \(\Gamma_*\)-Hermiticity

Let
\[
\Gamma_*=i^3\Gamma_1\Gamma_2\cdots\Gamma_6,
\]
with the phase convention giving \(\Gamma_*^\dagger=\Gamma_*\), \(\Gamma_*^2=I\), and \(\{\Gamma_*,\Gamma_i\}=0\). Then
\[
(D_{\mathrm{naive}}^U)^\dagger=-D_{\mathrm{naive}}^U,
\qquad (W^U)^\dagger=W^U,
\]
and
\[
(D_W^U)^\dagger
=m_0I-D_{\mathrm{naive}}^U+W^U
=\Gamma_*D_W^U\Gamma_*
\]
for real \(m_0,r\).

**Proof.** Each \(S_i^U\) is unitary, so its antisymmetric difference is anti-Hermitian and its symmetric Laplacian combination is Hermitian. The Clifford generators commute with color shifts and anticommute with \(\Gamma_*\); the Wilson scalar commutes with \(\Gamma_*\). These facts give the identities. \(\square\)

The exact chiral anticommutator is instead
\[
\{\Gamma_*,D_W^U\}=2\Gamma_*(m_0I+W^U).
\]
Thus the Wilson operator is not chirally anticommuting at finite spacing in general. At \(m_0=0\), the breaking is precisely the Wilson term. This is the standard Wilson trade-off, not an evasion of Nielsen–Ninomiya.

### Theorem C — positivity of the Wilson Laplacian

For every \(\psi\),
\[
\langle\psi,W^U\psi\rangle
=\frac r{2h}\sum_{i=1}^6
\|(I-S_i^U)\psi\|^2\geq0.
\]
Equality holds exactly when \(S_i^U\psi=\psi\) for every direction \(i\). The kernel can depend on gauge holonomy and need not consist only of constant fields.

**Proof.** Expand \(\|(I-S)\psi\|^2\) and use \(S^\dagger S=I\). \(\square\)

## 5. What is and is not established

**PROVED:** finite-dimensional gauge covariance; anti-Hermiticity of the naive kinetic term; Hermiticity/positivity of the Wilson term; \(\Gamma_*\)-Hermiticity for real mass; exact free Fourier symbol and corner Wilson masses.

**VERIFIED_NUMERICALLY:** only the tests that pass when the companion script is executed. The script checks Clifford relations, link unitarity, covariance under random local gauge transformations, adjoint identities, \(\Gamma_*\)-Hermiticity, and Wilson positivity on small periodic lattices.

**OPEN:** uniform low-energy resolvent/spectral convergence; interacting continuum limit; reflection positivity and determinant properties; a justified \(3+1\)-dimensional reduction; relation to the user's separate RGS/PSU/PRISM construction. Gauge covariance alone does not establish confinement, a physical quark spectrum, baryon masses, or QCD phenomenology.

## 6. Relation to T012–T017

- T012 supplies \(SU(3)_F\) flavor representation theory; it is not the color gauge group.
- T013 supplies color-singlet contractions; this operator supplies a candidate covariant kinetic term.
- T014's conditional graph covariance is made explicit here with oriented links and a fixed Hilbert-space adjoint.
- T015/T016 concern the finite base \(Q_6=\mathbb Z_2^6\) and its forward operator; they are not silently identified with this refinement.
- T017 supplies \(Q_{6,n}=(C_{2n})^{\square6}\) and the free centered/Wilson symbols. This note adds link coupling on that same family.
- No baryon correlator or mass prediction is claimed. Such a calculation still needs a gauge action/measure, fermion determinant prescription, flavor/spin projectors, and controlled scaling.

## 7. Reproducibility

Run:
\`\`\`bash
python -m pip install numpy
python scripts/verify_q6_gauge_covariant_wilson.py
\`\`\`
The script prints a JSON report and exits nonzero if any asserted finite-dimensional identity fails.
