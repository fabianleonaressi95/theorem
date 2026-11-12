# T122 — Pin+(4) lift and Clifford-compatible transport of the Möbius orientation cocycle

**Classification:** exact algebraic theorem for the declared finite six-face dual-graph transition system. It establishes a Pin+ lift on that graph and a compatible automorphism of the represented Clifford algebra. It does not, by itself, establish a Pin structure on an unspecified tangent bundle over the full 2-complex.

## 1. Base transition system

Let the dual graph have six face-vertices and the cycle
\[
0\to1\to2\to5\to4\to3\to0.
\]
The orientation signs \(t_{ij}\in\{\pm1\}\) are those induced by the six oriented square boundaries in T117. In this cycle order they have five \(+1\) entries and one \(-1\) entry, hence
\[
\prod_{\rm cycle}t_{ij}=-1.
\]
At each dual vertex choose a local frame change \(h_i\in\{\pm1\}\). The edge transitions change by
\[
t'_{ij}=h_jt_{ij}h_i^{-1}=h_jt_{ij}h_i.
\]

## 2. Pin+(4) lift

Work in the Euclidean Clifford algebra \(\mathrm{Cl}(4,0)\), with Hermitian generators
\[
\gamma_a\gamma_b+\gamma_b\gamma_a=2\delta_{ab}I_4.
\]
Fix a reflected axis \(a\in\{0,1,2,3\}\), and define
\[
\widehat{t}=
\begin{cases}
I_4,&t=+1,\\
\gamma_a,&t=-1.
\end{cases}
\]
Since \(\gamma_a^2=I_4\), this is a group homomorphism
\[
\widehat{\phantom t}:\mathbb Z_2\longrightarrow\mathrm{Pin}^+(4).
\]
The standard twisted-adjoint projection of an odd Pin element is
\[
\widetilde{\mathrm{Ad}}(\gamma_a)(v)
=-\gamma_a v\gamma_a^{-1}.
\]
For \(v=\sum_bv_b\gamma_b\), anticommutation gives
\[
-\gamma_a v\gamma_a^{-1}
=-v_a\gamma_a+\sum_{b\ne a}v_b\gamma_b.
\]
This is exactly the orthogonal reflection \(R_a\) on the selected axis. Thus the Pin+ lift projects to the O(4) transition used for the base orientation reversal.

## 3. Lifted transition cocycle

Define lifted edge transitions \(\widehat t_{ij}=\widehat{t_{ij}}\). Because the lift is a homomorphism and the local frame group is abelian,
\[
\widehat{t'_{ij}}
=\widehat h_j\,\widehat t_{ij}\,\widehat h_i^{-1}.
\]
Hence the lifted transitions obey the correct local-frame covariance law. Along the dual cycle,
\[
\prod_{\rm cycle}\widehat t_{ij}
=\widehat{\prod_{\rm cycle}t_{ij}}
=\widehat{-1}
=\gamma_a.
\]
The lifted holonomy is therefore nontrivial and is precisely the lift of the base orientation holonomy.

## 4. Clifford-compatible transport

Let \(\Gamma=\gamma_0\gamma_1\gamma_2\gamma_3\). In even dimension four, \(\Gamma^2=I_4\), and \(\alpha(X)=\Gamma X\Gamma^{-1}\) implements the grade automorphism; in particular \(\alpha(v)=-v\) on Clifford vectors.

Set \(\Phi_+(X)=X\), and for a negative transition define
\[
\Phi_-(X)=\gamma_a\alpha(X)\gamma_a^{-1}.
\]
This is an algebra automorphism. On vectors,
\[
\Phi_-(v)=-\gamma_a v\gamma_a^{-1}=R_av,
\]
so it transports Clifford generators by the same O(4) reflection as the base transition. Also \(\Phi_-^2=\mathrm{id}\), because \(\alpha(\gamma_a)=-\gamma_a\) and conjugation by a scalar is trivial. Thus \(\Phi_t\) is a representation of \(\mathbb Z_2\) and preserves Clifford products.

## 5. Finite audit

Implementation: \`src/pin_mobius_lift.py\`, \`src/mobius_representations.py\`, \`src/discrete_spin_geometry.py\`. Tests: \`tests/test_pin_mobius_lift.py\`, \`tests/test_mobius_representations.py\`, \`tests/test_discrete_spin_geometry.py\`.

The audit checks the Pin+ square, twisted-adjoint projection, grade automorphism, Clifford-vector covariance, lifted local-frame law, dual-cycle holonomy and induced Clifford transition group law. Floating-point residuals are implementation checks; the proof above is algebraic.

Reproduce in the source repository:
\`\`\`bash
PYTHONPATH=. python -m pytest tests/test_pin_mobius_lift.py tests/test_mobius_representations.py tests/test_discrete_spin_geometry.py -q
\`\`\`

## 6. Exact scope boundary

**Established:** a Pin+(4) lift of the specified \(\mathbb Z_2\) orientation-transition representation on the six-face dual graph, and Clifford-algebra transport compatible with its O(4) reflection.

**Not established:** a full Pin+ structure on a tangent bundle over every cell of the 2-complex; extension over all primal/dual cell overlaps; identification with the independent SU(2) lattice gauge field or the central element of \(2I\); a continuum Dirac operator; torsion; or a physical QLG coupling. Non-orientability alone is not a torsion equation.
