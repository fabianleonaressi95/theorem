# S.7 — Fourth-moment Maxwell obstruction and common \(A_4\) intertwiner

**Status: PROVED algebraic no-go and finite-group representation statements under the stated representation hypotheses; Maxwell constitutive response is a candidate.** The tensor-index obstruction is exact. The common-subgroup equivalence does not provide a canonical intertwiner or a connection-preserving map.

## 1. No direct rank-four correction from two antisymmetric field strengths

Let \(R_{ijkl}\) be fully symmetric and \(F_{ij}=-F_{ji}\). Then
\[
\boxed{R_{ijkl}F_{ij}F_{kl}=0.}
\]
Interchanging \(i\) and \(j\) leaves \(R\) unchanged and reverses the sign of \(F_{ij}\), so the contraction equals its negative. The fourth-moment residual cannot be inserted directly as a nonzero \(RFF\) Maxwell term, nor identified with a Riemann-type constitutive tensor or teleparallel torsion.

## 2. Correct intermediate: an independent STF order parameter

For \(Q\in\operatorname{Sym}_0(3)\), define
\[
A(Q)_{ij}=R_{ijkl}Q_{kl}.
\]
The pair-trace-free property of \(R\) implies \(A(Q)\in\operatorname{Sym}_0(3)\). A possible electric/magnetic constitutive ansatz is
\[
Z_E(Q)=z_EI+g_EA(Q),\qquad Z_B(Q)=z_BI+g_BA(Q),
\]
where \(z_E,z_B>0\). A sufficient condition for positive definiteness is
\[
|g_E|\,\|A(Q)\|_2<z_E,\qquad
|g_B|\,\|A(Q)\|_2<z_B.
\]
The density
\[
\mathcal L_{EM}(Q)=\frac12E^TZ_E(Q)E-\frac12B^TZ_B(Q)B
\]
is a well-defined candidate material constitutive law. It is not derived from the Wilson measure and does not predict the fine-structure constant.

If \(Q\) is integrated with a centered \(Q\mapsto-Q\) symmetric measure, then \(\langle A(Q)\rangle=0\); the first-order anisotropic correction to the vacuum quadratic Maxwell term vanishes. A Gaussian \(Q\) coupled linearly to \(F^2\) produces an \(F^4\) term at leading nontrivial order. A nonzero background, non-centred measure or Wilson-induced field dependence must be derived before a quadratic anisotropic response can appear.

## 3. Full-group obstruction and common tetrahedral subgroup

There is no injective homomorphism \(A_5\to O_h\): since \(A_5\) is simple, the kernel of any homomorphism is either all of \(A_5\) or trivial; injectivity is impossible because \(60\nmid48\). Thus a full-group identification \(A_5\simeq O_h\) is impossible.

Both groups contain a tetrahedral subgroup \(A_4\):
- \(A_4\subset A_5\), as the stabilizer of one letter in the natural five-letter action;
- \(A_4\subset O_h\), as the proper tetrahedral rotation subgroup.

For the five-dimensional irreducible representation of \(A_5\), its restriction to \(A_4\), with classes ordered as identity, double transpositions, and the two 3-cycle classes, has character
\[
\chi_{5\downarrow A_4}=(5,1,-1,-1).
\]
The \(A_4\) character table therefore gives
\[
\boxed{5\downarrow A_4=1'\oplus1''\oplus3.}
\]
On the RGS side,
\[
\operatorname{Sym}_0(3)=E_g\oplus T_{2g},
\]
and restriction to the same tetrahedral subgroup gives
\[
E_g\downarrow A_4=1'\oplus1'',\qquad
T_{2g}\downarrow A_4=3.
\]
Thus the two five-dimensional real representations have the same \(A_4\) representation type, and an \(A_4\)-equivariant real isomorphism exists after restriction, provided the specified subgroup embeddings and representation actions are used.

It is not canonical. One must choose common generators and bases, solve
\[
T\rho_1(h)=\rho_2(h)T
\]
for generators \(h\) of \(A_4\), and fix independent normalization/sign freedoms on the 2- and 3-dimensional blocks. Equality of dimensions alone is not an intertwiner.

## 4. Real representation type and bundle compatibility

The real two-dimensional representation underlying \(1'\oplus1''\) is of complex type, while the three-dimensional block is of real type. The real commutant is
\[
\operatorname{End}_{A_4}(V_5)\simeq\mathbb C\oplus\mathbb R.
\]
After invariant inner products and bases are fixed, this leaves a phase/rotation freedom on the real two-plane and a scalar freedom on the real three-dimensional block. It does not establish a quaternionic structure. Such a structure requires an antiunitary \(J\) commuting with the action and satisfying \(J^2=-I\); no such \(J\) follows from this representation argument.

For a principal \(G\)-bundle \(P\to M\), representation \(\rho\), and associated bundle \(E=P\times_\rho V\), a principal connection induces \(\nabla=d+\rho_*(\omega)\). An \(A_4\)-intertwiner induces a bundle map only when the reductions and transition functions use the same \(A_4\) action. It is connection-preserving only if
\[
\nabla_2\circ\Phi=\Phi\circ\nabla_1.
\]
Representation equivalence alone does not imply this equation.

## 5. Evidence and open obligations

- **PROVED:** \(R_{ijkl}F_{ij}F_{kl}=0\) for fully symmetric \(R\) and antisymmetric \(F\); \(R:Q\in\operatorname{Sym}_0(3)\); common \(A_4\) restriction type \(2\oplus3\); existence (not canonicity) of an \(A_4\)-intertwiner under the stated representation hypotheses; real commutant type.
- **IMPLEMENTED, NOT EXECUTION-CERTIFIED HERE:** the companion source/tests construct positive electric/magnetic response matrices for declared test inputs and check tensor covariance.
- **CANDIDATE:** Q-dependent Maxwell constitutive response.
- **OPEN:** actual Q6-to-STF intertwiner matrices; derivation of \(Q\) from PSU/Anti-Twin/coframe geometry; derivation of the \(Q\)-measure from the complete nonlinear Wilson fibre; connection compatibility; scalar Maxwell normalization and any fine-structure-constant prediction.

The five-dimensional \(A_5\) representation and the RGS \(\operatorname{Sym}_0(3)\) representation are compared only after restriction to a common \(A_4\). No full \(A_5\cong O_h\) identification is asserted.

## 6. Implementation provenance

Companion source and tests are imported into this repository as src/rgs_fourth_moment_maxwell_bridge.py and tests/test_rgs_fourth_moment_maxwell_bridge.py. The actual Q6 \(A_4\)-intertwiner matrix remains open.
