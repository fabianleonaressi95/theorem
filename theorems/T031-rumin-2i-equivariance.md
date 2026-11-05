# T031 — Equivariance of the 3D Rumin complex under the binary icosahedral action

**Status:** the geometric descent and operator-equivariance statements below are proved from naturality, under the explicitly fixed left/right action and contact data. The repository's finite quaternion and selected-representation routines provide computational checks of the group conventions. A full nine-irrep matrix realization and a new spectral calculation are **not** claimed here.

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

## 6. Computational bridge and acceptance boundary

The quaternion-bridge repository already contains:
- the deterministic 120-element scalar-first quaternion table;
- exhaustive finite closure/inverse/unit-norm checks;
- selected trivial, fundamental and vector representations;
- numerical intertwiner-space checks for those selected representations.

These are finite computational audits. The fundamental and vector representations distinguish the central element \(-1\): it acts by \(-I_2\) in the defining spin representation and by \(+I_3\) in the vector representation. This is a useful convention check for spinorial versus rotational data.

The three implemented representations are **not** the full nine-irrep catalogue used in T021. The finite checks also do not prove analytic hypoellipticity, zeta continuation, or torsion identities; those are covered by the separate analytic arguments in T021–T024.

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
5. Quaternion bridge: `docs/binary-icosahedral-2i.md`, `src/binary_icosahedral.py`, `src/representations_2i.py`.

## Classification

- **PROVED:** free left deck action; commutation of left 2I and right Hopf actions; naturality/descent of the Rumin complex under the fixed contact action; preservation of equivariant coefficient subspaces for flat unitary twists; character-projector formula.
- **NUMERICALLY VERIFIED IN THE BRIDGE REPOSITORY:** finite 2I closure and the selected representation/intertwiner audits, subject to their floating-point tolerances.
- **OPEN:** full nine-irrep explicit matrix models, exact projector/matrix-unit export, and any continuum limit linking Q6/PRISM to the Rumin complex.
