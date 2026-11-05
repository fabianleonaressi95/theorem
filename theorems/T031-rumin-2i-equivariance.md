# T031 — Equivariance of the 3D Rumin complex under the binary icosahedral action

**Status:** the geometric descent and operator-equivariance statements below are proved from naturality, under the explicitly fixed left/right action and contact data. The quaternionic bridge and its finite audit are maintained in this repository, so acceptance does not depend on the slower CI cycle of the separate quaternion-bridge repository. A full nine-irrep matrix realization and a new spectral calculation are **not** claimed here.

## 1. Fixed model and conventions

Identify the unit 3-sphere with the unit quaternions:
\[
S^3=SU(2)=\{q\in\mathbb H:|q|=1\}.
\]
Use scalar-first coordinates \(q=(w,x,y,z)\), Hamilton multiplication, and the subgroup \(2I\subset SU(2)\) of order 120. The deck action is **left multiplication**
\[
L_g(q)=gq,\qquad g\in2I.
\]
It is free: \(gq=q\) implies \(g=1\). Thus \(S^3\to S^3/2I\) is a regular covering with deck group \(2I\).

Fix a unit imaginary quaternion \(i\). The Hopf/Reeb circle acts on the right:
\[
R_{e^{it i}}(q)=q e^{it i}.
\]
Left and right multiplication commute:
\[
L_gR_h(q)=g(qh)=(gq)h=R_hL_g(q).
\]
The standard left-invariant contact/CR structure is chosen so that the Reeb flow is this right circle action. In the quaternionic Maurer–Cartan description, the contact form is the \(i\)-component of \(\bar q\,dq\); its horizontal plane and compatible complex structure are preserved by the left \(SU(2)\) action and by the right Hopf circle. Consequently the contact structure descends to the quotient and the descended Reeb action is locally free.

**Important correction of a common wording error:** \(2I\) is not a subgroup of the Hopf circle. It acts freely by left multiplication and commutes with the right Hopf circle; that is the reason the CR-Seifert structure descends.

## 2. Naturality of the Rumin complex

Let \(\theta\) be the fixed contact form, \(H=\ker\theta\), and let \(D_R\) be the middle Rumin differential. For any contactomorphism \(F\) preserving the chosen contact data, pullback commutes with the Rumin differentials:
\[
F^*d_R^k=d_R^kF^*\quad(k=0,2),\qquad
F^*D_R=D_RF^*.
\]
For the middle operator this follows directly from its normalization definition: if \(\beta_\alpha\equiv\alpha\pmod\theta\) is the unique corrected representative with \(\theta\wedge d\beta_\alpha=0\), then \(F^*\beta_\alpha\) is the unique corrected representative for \(F^*\alpha\), and
\[
D_R(F^*\alpha)=d(F^*\beta_\alpha)=F^*(d\beta_\alpha)=F^*D_R\alpha.
\]
Uniqueness of the correction is essential; no coordinate-specific formula is being assumed invariant by inspection.

Since every \(L_g\) preserves the contact data, the Rumin complex on \(S^3\) is a complex of \(2I\)-modules. Its invariant subcomplex is the untwisted Rumin complex on \(S^3/2I\).

## 3. Flat unitary twists and equivariant forms

Let \(\rho:2I\to U(V_\rho)\) be a unitary representation. In the convention used here, sections of the associated flat bundle are represented on the cover by functions/forms \(u\) satisfying
\[
u(gq)=\rho(g)u(q).
\]
The same equivariance condition is imposed coefficientwise on Rumin forms. Because the geometric Rumin differentials commute with deck pullback and the coefficient action is constant in the lifted flat trivialization, the differentials preserve this equivariant subspace. They therefore descend to the Rumin complex with coefficients in the flat bundle \(E_\rho\to S^3/2I\).

The sign/inverse convention for the associated-bundle quotient must be kept consistent with the displayed equivariance rule. Replacing \(\rho\) by \(\rho^{-1}\) without changing the quotient convention changes the local system.

## 4. Isotypic projectors

For a finite-dimensional unitary representation \(U\) of \(2I\) on a Hilbert space \(\mathcal H\), the projector onto the \(\rho\)-isotypic component is
\[
P_\rho=\frac{d_\rho}{120}\sum_{g\in2I}
\overline{\chi_\rho(g)}\,U(g),
\]
where \(d_\rho=\dim V_\rho\). It satisfies
\[
P_\rho^2=P_\rho=P_\rho^*,\qquad
P_\rho P_\sigma=0\quad(\rho\not\simeq\sigma),
\]
and commutes with every operator that commutes with the group action. In particular, for a group-equivariant Rumin Laplacian, the isotypic subspaces are invariant.

This formula is the character projector; it does not by itself construct matrix units, a basis of each multiplicity space, or all nine irreducible representation matrices. Those require the full character table and explicit unitary models.

## 5. Relation to the existing torsion results

- T021 computes the character-twisted spectral/Molien data for all nine irreducible representations of \(2I\).
- T024 identifies the dimension-three Kitaoka and Rumin–Seshadri operators and reconciles their torsion conventions under the stated common metric and flat-unitary hypotheses.
- T030 records the explicit local central differential and its formal adjoint in the chosen Darboux model.

T031 supplies the geometric equivariance/descent layer connecting these ingredients. It does **not** redo T021/T024, nor does it claim a new evaluation of any zeta function or analytic torsion.

## 6. In-repository quaternionic bridge and acceptance boundary

The companion implementation is deliberately consolidated in `theroem`. It does not require importing code or CI results from `rgs-qlg-quaternion-bridge`.

The standalone audit `verification/test_t031_quaternion_bridge.py` constructs the 120 unit quaternions of the binary icosahedral group from the standard coordinate families:
- 8 coordinate units \(\pm1,\pm i,\pm j,\pm k\);
- 16 half-coordinate quaternions \((\pm1\pm i\pm j\pm k)/2\);
- 96 even-permutation/sign variants of \((0,1,\varphi,\varphi^{-1})/2\).

It checks cardinality, unit norm, closure under Hamilton multiplication, and the left/right action identity
\[
g(qh)=(gq)h
\]
for every generated group element and a fixed deterministic collection of unit quaternions and Hopf angles. The test uses only the Python standard library and reports a floating-point tolerance; it is a finite implementation audit, not a proof of associativity or of the contact-geometric theorem.

The representation-level scope remains separate: the trivial, defining 2D spin, and 3D vector representations are selected examples, not the complete nine-irrep catalogue used in T021. In particular, the central element \(-1\) acts by \(-I_2\) in the defining spin representation and by \(+I_3\) in the vector representation. No numerical test in this section proves analytic hypoellipticity, zeta continuation, or torsion identities; those belong to T021–T024.

## 7. Explicit proof obligations left open

1. Export the complete nine irreducible unitary models and character table into a single convention-controlled machine-readable artifact.
2. Verify the character-projector identities and the sum-of-squares identity \(\sum_\rho d_\rho^2=120\) in exact algebraic arithmetic, not floating-point rounding.
3. Construct matrix units and explicit bases for the multiplicity spaces occurring in the relevant \(\operatorname{Sym}^m(\mathbb C^2)\) sectors.
4. If a discrete Q6/PRISM operator is to be compared with the continuum Rumin operator, define a specific map and prove an operator-intertwining or convergence theorem. No such implication follows from group equivariance alone.

## References

1. M. Rumin and N. Seshadri, *Analytic torsions on contact manifolds*, Ann. Inst. Fourier 62 (2012), 727–782, DOI: 10.5802/aif.2693.
2. A. Kitaoka, *Analytic Torsions Associated with the Rumin Complex on Contact Spheres*, Int. J. Math. 31 (2020), 2050112, arXiv:1911.03092.
3. Repository theorem T021, *Character-twisted Rumin analytic torsion on the Poincaré sphere*.
4. Repository theorem T024, *Operator and torsion-convention matching for the Rumin complex on 3D CR-Seifert quotients*.
5. In-repository finite audit: `verification/test_t031_quaternion_bridge.py`.

## Classification

- **PROVED:** free left deck action; commutation of left 2I and right Hopf actions; naturality/descent of the Rumin complex under the fixed contact action; preservation of equivariant coefficient subspaces for flat unitary twists; character-projector formula.
- **NUMERICALLY VERIFIED IN THIS REPOSITORY (when the standalone test passes):** finite 2I cardinality, unit norms, closure and left/right action identities, subject to the stated floating-point tolerance.
- **OPEN:** full nine-irrep explicit matrix models, exact projector/matrix-unit export, and any continuum limit linking Q6/PRISM to the Rumin complex.
