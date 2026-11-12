# T123 — Central-character obstruction and the minimal 2I twist of the Q6 exterior module

**Classification:** exact representation-theoretic theorem. The vanishing statement follows from the central element of \(2I\). The twisted embedding is explicit. Finite matrix audits are supporting implementation checks, not the proof.

## 1. Representations

Let \(2I\subset SU(2)\) be the binary icosahedral group, with central subgroup \(\{\pm1\}\), and let
\[
\pi:2I\to A_5\cong 2I/\{\pm1\}
\]
be the quotient map.

Let \(V_6\cong\mathbb C^6\) be the signed-axis representation obtained by pulling back the proper icosahedral \(A_5\)-action on the six unoriented icosahedral axes. Let
\[
W=\Lambda^*V_6,\qquad \dim_{\mathbb C}W=2^6=64
\]
be its induced exterior representation. Since this representation factors through \(A_5\),
\[
\rho_W(-1)=I_W.
\]

Let \(S=\mathbb C^2\) be the defining fundamental representation of \(2I\subset SU(2)\). Its central character is
\[
\rho_S(-1)=-I_S.
\]

## 2. Vanishing of the untwisted intertwiner space

Suppose \(T:S\to W\) is \(2I\)-equivariant. Equivariance at the central element \(-1\) gives
\[
T\rho_S(-1)=\rho_W(-1)T.
\]
Substituting the two central actions,
\[
-T=T.
\]
Over \(\mathbb C\), this implies \(T=0\). Therefore
\[
\boxed{\operatorname{Hom}_{2I}(S,W)=0.}
\]

This is exact and independent of numerical precision, basis choices, or the other group elements. In particular, the Q6 exterior module of T121 does not contain the fundamental \(2I\) doublet as a subrepresentation under the specified pulled-back \(A_5\)-action.

## 3. Minimal tensor twist and explicit embedding

Define the twisted representation on \(S\otimes W\) by
\[
\rho_{\mathrm{tw}}(g)=\rho_S(g)\otimes\rho_W(g).
\]
The degree-zero exterior vacuum \(1\in\Lambda^0V_6\subset W\) is fixed by every induced exterior action:
\[
\rho_W(g)1=1.
\]
Consequently
\[
J:S\to S\otimes W,\qquad J(s)=s\otimes1
\]
is nonzero and satisfies
\[
\begin{aligned}
\rho_{\mathrm{tw}}(g)J(s)
&=(\rho_S(g)s)\otimes(\rho_W(g)1)\\
&=\rho_S(g)s\otimes1\\
&=J(\rho_S(g)s).
\end{aligned}
\]
Thus
\[
\boxed{\operatorname{Hom}_{2I}(S,S\otimes W)\ne0,}
\]
with an explicit injective intertwiner \(J\). The twisted module has dimension \(2\cdot64=128\).

This construction repairs the central-character mismatch algebraically. It does not prove that the added fundamental factor is forced by geometry or physics.

## 4. Finite implementation audit

Companion source implementation:
- \`src/q6_2i_intertwiners.py\`
- \`src/representations_2i.py\`
- \`src/rgs_icosahedral_q6_intertwiner.py\`

Tests:
- \`tests/test_q6_2i_intertwiners.py\`

The audit induces the signed-permutation action on all 64 exterior basis states, pulls it back to all 120 quaternion elements, verifies the opposite central characters, and checks the explicit twisted embedding against all group elements.

Reproduction command in the source repository:
\`\`\`bash
PYTHONPATH=. python -m pytest tests/test_q6_2i_intertwiners.py tests/test_representations_2i.py tests/test_rgs_icosahedral_q6_intertwiner.py -q
\`\`\`

The algebraic proof above is exact. Floating-point group matrices provide a finite computational consistency check.

## 5. Boundary with Pin+(4)

T122 constructs a Pin+(4) lift of the specified Möbius orientation-transition system on its six-face dual graph. T123 concerns the pullback of the proper icosahedral \(A_5\)-action to \(2I\). These are not yet identified as representations of a common structure group: no homomorphism, common bundle atlas, or Pin-to-\(2I\) coupling is asserted here.

Nor does T123 imply torsion, a continuum Dirac operator, or a physical QLG interaction. Those require additional geometric and dynamical input.
