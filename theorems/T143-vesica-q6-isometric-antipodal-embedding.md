# T143 — Isometric antipodal embedding of the Vesica six-state model into Q6

**Record type:** exact finite-dimensional embedding and zero-extension theorem.  
**Status:** exact construction proved. The numerical script is a reproducibility check; its execution status is reported separately. A nonzero extension on the orthogonal complement and any physical PSU–Anti-Twin interpretation remain open.

## 1. Six Q6 states selected from the existing T141 assignment

Write \(Q_6=\mathbb F_2^6\), identify a bit string with its integer in \(\{0,\ldots,63\}\), and let
\[
J_{Q6}e_c=e_{c\oplus63}.
\]
Use the three antipodal pairs already present in the T141 icosahedral assignment:
\[
(3,60),\qquad(5,58),\qquad(9,54),
\]
where
\[
60=3\oplus63,\quad58=5\oplus63,\quad54=9\oplus63.
\]
All six labels have even Hamming weight. They are distinct.

In T142, order the six Vesica points as
\[
( z_0,z_1,z_2,-z_0,-z_1,-z_2)
=(1,\omega,\omega^2,-1,-\omega,-\omega^2),
\quad\omega=e^{2\pi i/3}.
\]
Define \(\iota:\ell^2(\mathcal H)\to\mathbb C^{64}\) on the point basis by
\[
\boxed{
\begin{aligned}
\iota\delta_{1}&=e_3,&
\iota\delta_{\omega}&=e_5,&
\iota\delta_{\omega^2}&=e_9,\\
\iota\delta_{-1}&=e_{60},&
\iota\delta_{-\omega}&=e_{58},&
\iota\delta_{-\omega^2}&=e_{54}.
\end{aligned}}
\]
Equivalently, the \(64\times6\) matrix of \(\iota\) has one unit entry in each column, in rows \((3,5,9,60,58,54)\), and zero elsewhere.

## 2. Isometry and antipodal intertwining

The six image basis vectors are distinct standard basis vectors, hence orthonormal. Therefore
\[
\boxed{\iota^\dagger\iota=I_6.}
\]
By the pair assignments,
\[
J_{Q6}\iota\delta_{z_k}
=e_{c_k\oplus63}
=\iota\delta_{-z_k}
=\iota J\delta_{z_k}
\]
for \(c=(3,5,9)\). The same identity holds on the antipodal basis vectors, so
\[
\boxed{J_{Q6}\iota=\iota J.}
\]
Thus \(\iota\mathscr H\) is a six-dimensional \(J_{Q6}\)-invariant subspace. Its even and odd parts each have dimension three.

## 3. Exact zero extensions of the coordinate operators

Let \(X,Y\) be the T142 coordinate multiplication operators. Define
\[
\widetilde X_0=\iota X\iota^\dagger,\qquad
\widetilde Y_0=\iota Y\iota^\dagger,\qquad
\Pi=\iota\iota^\dagger.
\]
These are Hermitian operators on \(\mathbb C^{64}\), supported on the six selected states, and vanish on \((\iota\mathscr H)^\perp\). Since \(\iota^\dagger\iota=I_6\),
\[
\widetilde X_0^2+\widetilde Y_0^2
=\iota(X^2+Y^2)\iota^\dagger
=\boxed{\Pi},
\]
not \(I_{64}\). This is the exact identity for the zero extension.

The intertwining relation gives
\[
\boxed{
J_{Q6}\widetilde X_0J_{Q6}=-\widetilde X_0,\qquad
J_{Q6}\widetilde Y_0J_{Q6}=-\widetilde Y_0.
}
\]
Consequently both zero-extended operators exchange the global even and odd Q6 sectors. Their nonzero action is confined to the embedded six-dimensional subspace.

## 4. Embedded block ranks and full-space ranks

The restriction of the embedded operators to \(\iota\mathscr H\) is unitarily equivalent (via the isometry \(\iota\)) to T142. Therefore the embedded even-to-odd blocks have
\[
\boxed{\operatorname{rank}(P_{Q6,-}\widetilde X_0P_{Q6,+})=3,\qquad
\operatorname{rank}(P_{Q6,-}\widetilde Y_0P_{Q6,+})=2.}
\]
As operators on the full 64-dimensional space, their ranks are respectively
\[
\operatorname{rank}\widetilde X_0=6,\qquad
\operatorname{rank}\widetilde Y_0=4.
\]
The orthogonal complement has dimension 58, with 29 even and 29 odd dimensions, and both zero extensions vanish there.

## 5. Why this does not yet define a full Q6 coordinate pair

The identity \(\widetilde X_0^2+\widetilde Y_0^2=\Pi\) is a projection identity. It is not the global coordinate identity \(I_{64}\). A full-space extension would require additional operators \(X_\perp,Y_\perp\) on \((\iota\mathscr H)^\perp\), with a separately justified construction. To preserve the antipodal grading they must be Hermitian and odd under the restricted antipodal involution; if one also wants the unit-circle relation, they must satisfy
\[
X_\perp^2+Y_\perp^2=I_{(\iota\mathscr H)^\perp}.
\]
There is no canonical choice supplied by the six-state Vesica data. Choosing one arbitrarily would add structure not derived from the geometry.


## 6. A parameterized class of full diagonal extensions

Although the six-state data do not select a canonical action on the orthogonal complement, they do determine the form of a simple **family** of full-space extensions under the additional ansatz that \(X_{Q6},Y_{Q6}\) are real diagonal multiplication operators in the Q6 vertex basis.

Choose one representative \(r\) from each of the 32 antipodal pairs \(\{r,r\oplus63\}\). For the three selected representatives \(r=3,5,9\), fix
\[
(a_r,b_r)=
(1,0),\quad
\left(-\frac12,\frac{\sqrt3}{2}\right),\quad
\left(-\frac12,-\frac{\sqrt3}{2}\right),
\]
respectively. For each of the other 29 pairs choose an arbitrary angle
\(\theta_r\in\mathbb R/(2\pi\mathbb Z)\), and set
\[
(a_r,b_r)=(\cos\theta_r,\sin\theta_r).
\]
Define the multipliers on the partner by
\[
a_{r\oplus63}=-a_r,\qquad b_{r\oplus63}=-b_r.
\]
Then
\[
(X_{Q6}f)(c)=a_cf(c),\qquad
(Y_{Q6}f)(c)=b_cf(c)
\]
are Hermitian, satisfy
\[
J_{Q6}X_{Q6}J_{Q6}=-X_{Q6},\qquad
J_{Q6}Y_{Q6}J_{Q6}=-Y_{Q6},
\]
and obey the global identity
\[
\boxed{X_{Q6}^2+Y_{Q6}^2=I_{64}.}
\]
On the six selected states they agree exactly with the embedded Vesica coordinate operators. The 29 angles are free parameters: this is a 29-parameter family within the diagonal-multiplier ansatz, not a canonical extension and not a classification of all possible (possibly nondiagonal) extensions. A geometric or dynamical principle is still needed to determine these angles.

## 7. Relation to T141 and evidence status

The six code labels are reused from three of the six antipodal pairs in T141. This reuses the Q6 labels, not the icosahedron-to-Q6 edge-path construction. T143 does not claim that the six-state Vesica is the icosahedron, nor that the T141 path lift induces these coordinate operators.

**Proved exactly:** isometry; antipodal intertwining; invariance of the image; zero-extension Hermiticity and oddness; \(\widetilde X_0^2+\widetilde Y_0^2=\Pi\); embedded block ranks 3 and 2; full zero-extension ranks 6 and 4; 29+29 dimensions of the orthogonal complement; and the 29-parameter diagonal full-extension family described above.

**Numerically audited by the accompanying script:** the finite matrix identities and ranks for the isometric embedding and one representative member of the full diagonal-extension family, up to the declared floating-point tolerance.

**Open:** a geometric or dynamical principle selecting the 29 complementary angles, or a justified nondiagonal extension; physical identification of the two parity sectors; a PSU-to-Anti-Twin current or Hamiltonian derived from this construction.


The six code labels are reused from three of the six antipodal pairs in T141. This reuses the Q6 labels, not the icosahedron-to-Q6 edge-path construction. T143 does not claim that the six-state Vesica is the icosahedron, nor that the T141 path lift induces these coordinate operators.

**Proved exactly:** isometry; antipodal intertwining; invariance of the image; zero-extension Hermiticity and oddness; \(\widetilde X_0^2+\widetilde Y_0^2=\Pi\); embedded block ranks 3 and 2; full-space ranks 6 and 4; 29+29 dimensions of the orthogonal complement.

**Numerically audited by the accompanying script:** the same finite matrix identities and ranks, up to the declared floating-point tolerance.

**Open:** a geometrically or dynamically justified nonzero extension on the 58-dimensional complement; physical identification of the two parity sectors; a PSU-to-Anti-Twin current or Hamiltonian derived from this construction.

## 7. Reproduction

\`\`\`bash
python scripts/audit_t143_vesica_q6_embedding.py
python -m unittest tests.test_t143_vesica_q6_embedding
\`\`\`
