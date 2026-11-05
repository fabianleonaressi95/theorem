# T024 — Operator and torsion-convention matching for the Rumin complex on 3D CR-Seifert quotients

**Status:** proved in dimension three, under the common contact metric and flat-unitary coefficient hypotheses stated below. The rescaled Rumin differential used by Kitaoka is exactly the unscaled Rumin differential used by Rumin–Seshadri when \\(n=1\\). Their fourth-order Laplacians therefore agree degree by degree. Hodge duality then identifies the full-degree Rumin–Seshadri torsion function with the negative of Kitaoka's lower-half torsion function. This closes the operator/sign-convention bridge needed for the (S^3/2I) application.

## 1. Setup and hypotheses

Let ((M,H,	heta,J)) be a compact, oriented, three-dimensional strictly pseudoconvex CR contact manifold. Let (E\to M) be a flat Hermitian vector bundle with unitary holonomy. Use the same contact form, calibrated CR structure, induced \\(L^2\\) products, and formal adjoints throughout.

The Rumin complex has the form
\[
\mathcal E^0\xrightarrow{d_R^0}\mathcal E^1
\xrightarrow{D}\mathcal E^2\xrightarrow{d_R^2}\mathcal E^3.
\]
Here \\(D=d_R^1\\) is the second-order middle differential.

Kitaoka uses the rescaling
\[
d_E^k=a_kd_R^k,\qquad
a_k=|n-k|^{-1/2}\ (k\ne n),\qquad a_n=1.
\]
For \\(n=1\\), the only first-order differentials have degrees \\(k=0,2\\), and
\[
a_0=|1-0|^{-1/2}=1,\qquad
a_2=|1-2|^{-1/2}=1,\qquad a_1=1.
\]
Consequently
\[
\boxed{d_E^k=d_R^k\quad\text{in every degree}.}
\]
This equality is specific to dimension three; it must not be extrapolated to higher-dimensional contact manifolds.

## 2. Equality of the fourth-order Laplacians

Write (d=d_R=d_E), let (\delta=d^*), and retain (D) for the middle operator. Both papers use the same degreewise fourth-order construction:
\[
\begin{aligned}
\Delta_0&=(d\delta+\delta d)^2,\\
\Delta_1&=(d\delta)^2+D^*D,\\
\Delta_2&=DD^*+(\delta d)^2,\\
\Delta_3&=(d\delta+\delta d)^2.
\end{aligned}
\]
For Rumin–Seshadri this is their contact Laplacian (2.8); for Kitaoka it is the Laplacian associated with the rescaled complex. Since the complexes, metrics, and adjoints agree, the operators agree on their common smooth domains and hence have the same self-adjoint hypoelliptic realizations:
\[
\boxed{\Delta_{RS}^k=\Delta_{K}^k,\qquad k=0,1,2,3.}
\]
In particular, the equality is operator-level, not merely an equality of eigenvalue lists on the sphere.

## 3. Hodge-star duality

The contact Hodge star gives isometric bundle maps
\[
*:\mathcal E^k\longrightarrow\mathcal E^{3-k}.
\]
The adjoint identities for the horizontal differential and the middle differential imply, by substitution in the four displayed Laplacians,
\[
\boxed{\Delta_3=*\Delta_0*^{-1},\qquad
\Delta_2=*\Delta_1*^{-1}.}
\]
The same identities hold with coefficients in (E), because the star acts on the form factor and the flat Hermitian coefficient connection is unitary.

Therefore the complete spectral zeta functions, with the common convention (0^s=1), satisfy
\[
\zeta_3(s)=\zeta_0(s),\qquad
\zeta_2(s)=\zeta_1(s).
\]
This includes the harmonic multiplicities: the star maps the kernels isometrically.

## 4. Exact comparison of torsion functions

Rumin–Seshadri define
\[
\kappa_C(s)=\frac12\sum_{k=0}^{3}(-1)^{k+1}w(k)\zeta_k(s),
\qquad
w(k)=
\begin{cases}
k,&k\le1,\\
k+1,&k>1.
\end{cases}
\]
Thus \\(w(0)=0,\\ w(1)=1,\\ w(2)=3,\\ w(3)=4\\), and
\[
\begin{aligned}
\kappa_C(s)
&=\frac12\bigl(\zeta_1(s)-3\zeta_2(s)+4\zeta_3(s)\bigr)\\
&=\frac12\bigl(\zeta_1(s)-3\zeta_1(s)+4\zeta_0(s)\bigr)\\
&=2\zeta_0(s)-\zeta_1(s).
\end{aligned}
\]
Kitaoka's three-dimensional definition is
\[
\kappa_E(s)=-2\zeta_0(s)+\zeta_1(s).
\]
It follows identically, as a meromorphic function wherever the zeta functions are continued, that
\[
\boxed{\kappa_C(s)=-\kappa_E(s).}
\]
With (2\log T=\kappa'(0)), this gives
\[
\boxed{T_C=T_E^{-1}.}
\]
This is precisely the inverse convention recorded by Rumin–Seshadri.

## 5. Ray–Singer convention and determinant line

Rumin–Seshadri's Theorem 4.2 states, for a three-dimensional CR-Seifert manifold and any unitary representation of its fundamental group,
\[
T_C=(T_{RS})^{-1},
\]
and identifies the contact and de Rham Ray–Singer metrics through the canonical determinant-line isomorphism induced by the contact complex resolving the constant sheaf.

Combining this theorem with Section 4 yields
\[
\boxed{T_E=T_{RS}.}
\]
The determinant-line metric statement is not an extra numerical assumption: the canonical cohomology isomorphism is the one induced by the contact-complex resolution, and Theorem 4.2 identifies the corresponding metrics. The equality is valid for unitary flat coefficients, including the bundles associated with irreducible unitary representations of (2I).

## 6. Application to the Poincaré sphere \\(S^3/2I\\)

Realize (S^3\simeq SU(2)). The binary icosahedral group (2I\subset SU(2)) acts freely by left multiplication. The scalar Hopf circle action commutes with this left action, preserves the standard CR structure and contact form, and descends to a locally free Reeb circle action on \\(S^3/2I\\). Hence the quotient is a compact three-dimensional CR-Seifert manifold.

The hypotheses of Rumin–Seshadri Theorem 4.2 therefore hold for every unitary representation of
\[
\pi_1(S^3/2I)\cong2I.
\]
For each irreducible unitary representation \(\rho\), the character-twisted spectral calculation in T021–T023 is consequently the Ray–Singer torsion in the same determinant-line convention:
\[
\boxed{T_{\mathcal E,\rho}(S^3/2I)=T_{RS,\rho}(S^3/2I).}
\]
For the trivial representation, the non-acyclic determinant line must still be normalized using the integral generators of \\(H^0\\) and \\(H^3\\); the contact metric volume factor is handled separately in T021. The present theorem does not replace that cohomological metric calculation.

## 7. What is now closed and what remains open

**Proved here**
- The degreewise rescaling in Kitaoka is the identity for \\(n=1\\).
- The Kitaoka and Rumin–Seshadri fourth-order Laplacians coincide in all four degrees under the same metric.
- Hodge-star duality gives \(\zeta_3=\zeta_0\) and \(\zeta_2=\zeta_1\).
- The torsion functions obey \(\kappa_C=-\kappa_E\), hence \(T_C=T_E^{-1}\).
- With Rumin–Seshadri Theorem 4.2, \(T_E=T_{RS}\) on the CR-Seifert quotient for unitary flat coefficients.

**Still separate**
- T021–T023's spectral/Molien input and exact evaluation of the nine irreducible twists.
- The explicit determinant-line basis and (L^2)-norm calculation for the trivial coefficient system, already treated in T021.
- Any higher-dimensional comparison: for \\(n>1\\), the rescaling factors are not all one and the above operator identity cannot be reused without a new conjugation/rescaling analysis.
- Any implication for Q6, PRISM, Yang–Mills, or physical matter; none follows from this torsion comparison.

## References

1. M. Rumin and N. Seshadri, *Analytic torsions on contact manifolds*, Ann. Inst. Fourier 62 (2012), 727–782, especially equations (2.3), (2.8), Proposition 2.2 and Theorem 4.2. DOI: 10.5802/aif.2693.
2. A. Kitaoka, *Analytic Torsions Associated with the Rumin Complex on Contact Spheres*, Int. J. Math. 31 (2020), 2050112, arXiv:1911.03092.
3. A. Kitaoka, *Ray–Singer Torsion and the Rumin Laplacian on Lens Spaces*, SIGMA 18 (2022), 091, especially §1 and the definition of \(\Delta_{\mathcal E}\). DOI: 10.3842/SIGMA.2022.091.
4. Repository audit: [T021 — Character-twisted Rumin analytic torsion on the Poincaré sphere](T021-rumin-analytic-torsion-2I.md).
