# Q6–D5–D4 bridge to the Liouville–Bergman law

**Status:** exact conditional invariance lemma; the identification of the Q6-induced D4 action with the five-dimensional Q6 D5 spectral sector remains open.

## 1. Previously established Q6–D5 data

Let \(D_0\) and \(D_1\) be the Q6 incidence matrices, and let
\[
H_1=D_1^T D_1.
\]
The selected five-dimensional rational mode space is
\[
E_5=\ker_{\mathbb Q}(H_1-12I),\qquad \dim E_5=5.
\]
If \(C\in\mathbb Z^{129\times192}\) is the integral fundamental-cycle matrix and \(V\in\mathbb Q^{192\times5}\) is a basis matrix for \(E_5\), the mode map is
\[
\Pi_5(c)=cCV.
\]
The exact repository audit establishes rank five, saturated integer kernel rank 124, and the torsion-free quotient
\[
\mathbb Z^{129}/K_{\mathbb Z}\simeq\Pi_5(\mathbb Z^{129}).
\]
The pointwise Wilson weight does not descend to this quotient. The positive effective weight is the complete fibre sum
\[
W_{\rm eff}([c])=\sum_{k\in K_{\mathbb Z}}
\prod_{e=1}^{192}\frac{I_{|((c+k)C)_e|}(\beta_t)}{I_0(\beta_t)},
\]
where the intended flux index is \(|((c+k)C)_e|\). The sum is absolutely convergent, but its complete numerical value is not yet enclosed by a useful certified interval. No Wilson-to-Bergman limit is established by the integer quotient alone.

## 2. The D5 Liouville–Bergman chart

For the isotropic five-mode Hamiltonian
\[
H_5(q,\pi)=\frac{\|\pi\|^2}{2\beta_{\rm eff}}
+\frac{\beta_{\rm eff}\lambda_{\rm eff}}2\|q\|^2,
\quad
\beta_{\rm eff}=\frac{a_s^4}{g_7^2},
\quad
\lambda_{\rm eff}=\frac{12}{a_s^2},
\quad
\Omega=\sqrt{\lambda_{\rm eff}}
=\frac{\sqrt{12}}{a_s},
\]
define
\[
z_j=\frac{\sqrt{\beta_{\rm eff}\Omega}\,q_j
+i\pi_j/\sqrt{\beta_{\rm eff}\Omega}}{\sqrt{20}},
\quad j=1,\ldots,5.
\]
Then
\[
d\mu_L=\prod_{j=1}^5dq_j\,d\pi_j
=20^5\,d^{10}z,
\]
and on the type-IV domain
\[
D_5=\{z:N(z)>0,\ |z^Tz|<1\},
\qquad
N(z)=1-2z^\dagger z+|z^Tz|^2,
\]
the Bergman volume density in this chart is
\[
dV_B=N(z)^{-5}d\mu_L.
\]
This is the geometric Liouville–Bergman law already recorded in the Q6–D5 work. It is distinct from a claim that the finite-coupling Wilson marginal equals this measure.

## 3. Exact D4 invariance lemma on the phase-space chart

Take
\[
R_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad
S_2=\begin{pmatrix}-1&0\\0&1\end{pmatrix},
\]
and extend them to five dimensions by
\[
U_R=R_2\oplus I_3,\qquad U_S=S_2\oplus I_3.
\]
They are real orthogonal matrices and satisfy
\[
U_R^4=U_S^2=I_5,\qquad
U_SU_RU_S=U_R^{-1}.
\]
Thus they define an orthogonal five-dimensional representation of \(D_4\).

For any such real orthogonal \(U\), let
\[
(q,\pi)\mapsto(Uq,U\pi),\qquad z\mapsto Uz.
\]
The canonical symplectic form and Liouville measure are invariant:
\[
\sum_j d(Uq)_j\wedge d(U\pi)_j
=\sum_jdq_j\wedge d\pi_j,
\qquad U^*d\mu_L=d\mu_L.
\]
Since \(U^TU=I\) and \(U\) is real,
\[
(Uz)^\dagger(Uz)=z^\dagger z,
\qquad
(Uz)^T(Uz)=z^Tz.
\]
Consequently \(N(Uz)=N(z)\), and hence
\[
\boxed{U^*dV_B=dV_B.}
\]
The isotropic Hamiltonian \(H_5\) is invariant as well. This proves an exact D4 symmetry of the *five-dimensional Liouville–Bergman chart* for the specified representation.

## 4. The missing Q6 intertwining statement

The preceding lemma does **not** yet prove that this representation is the one induced by the D4 action on the 64 RGS/Q6 seed points.

In particular, the Q6 label map \(R\) sends two standard cube-edge directions to diagonals (the directions \(e_1+e_3\) and \(e_2+e_3\)). Therefore \(R\) is not an automorphism of the original cubical Q6 graph and cannot simply be applied to the original Q6 cochain complex or its eigenvalue-12 sector.

The M3 orbit graph, with the eight directions
\[
\{e_1,e_2,e_3,e_4,e_5,e_6,e_1+e_3,e_2+e_3\},
\]
is D4-invariant at the graph level. To identify its action with the five-mode D5 representation, a subsequent exact construction must:
1. build a D4-equivariant cell/cochain complex on the orbit closure (after resolving any non-regular square intersections);
2. construct its exact Hodge operator and determine the relevant five-dimensional invariant spectral subspace;
3. compute the induced matrices \(\rho_5(R),\rho_5(S)\) in an orthonormal rational/real frame;
4. exhibit an explicit intertwiner between that representation and \(R_2\oplus I_3,S_2\oplus I_3\), or replace the block representation by the actual induced one if they differ.

Until these steps are completed, the relation between the M3 D4 action and the previously established Q6 D5 eigenspace is a **candidate bridge**, not a proved identification.

## 5. Status table

- **Exact:** Q6 rational five-mode quotient and saturated rank-124 integer kernel (repository audit).
- **Exact:** Liouville–Bergman density formula in the stated D5 chart.
- **Exact conditional lemma:** any real orthogonal five-dimensional D4 representation acting diagonally on \((q,\pi)\) preserves the canonical Liouville measure, \(N\), and the Bergman density.
- **Open:** deriving the relevant five-dimensional representation from the M3 Q6 orbit complex and constructing an explicit intertwiner.
- **Open:** deriving the Bergman density or its Hua generic-norm regulator as a limit/pushforward of the finite-coupling Wilson fibre marginal.

The formula \(dV_B=N^{-5}d\mu_L\) must not be presented as the evaluation of \(W_{\rm eff}\), nor as a consequence of the rank-five integer quotient.


## 6. An exact five-dimensional D4 module in the orbit graph

There is a stronger finite result available directly from the M3 graph. Let
\[
\mathscr D=\{e_1,e_2,e_3,e_4,e_5,e_6,e_1+e_3,e_2+e_3\}
\subset\mathbb F_2^6
\]
be its eight edge directions. Its vertex Laplacian is the Cayley-graph operator
\[
(\Delta f)(v)=\sum_{d\in\mathscr D}(f(v)-f(v+d)).
\]
For every character \(\chi_k(v)=(-1)^{k\cdot v}\),
\[
\Delta\chi_k=2m(k)\chi_k,\qquad
m(k)=\sum_{d\in\mathscr D}(k\cdot d\bmod2).
\]
Writing \(k=(k_1,k_2,k_3,k_4,k_5,k_6)\),
\[
m(k)=k_1+k_2+k_3+k_4+k_5+k_6
 +(k_1\oplus k_3)+(k_2\oplus k_3).
\]
The equation \(m(k)=2\) has exactly five solutions:
\[
\begin{aligned}
k_A&=(1,0,0,0,0,0),&
k_B&=(0,1,0,0,0,0),\\
k_C&=(0,0,0,1,1,0),&
k_D&=(0,0,0,1,0,1),\\
k_E&=(0,0,0,0,1,1).
\end{aligned}
\]
Therefore the graph Laplacian has an exact five-dimensional eigenspace
\[
\mathcal E_4=\operatorname{span}_{\mathbb R}
\{\chi_{k_A},\chi_{k_B},\chi_{k_C},\chi_{k_D},\chi_{k_E}\},
\qquad \Delta|_{\mathcal E_4}=4I.
\]
Because the orbit graph is D4-invariant, this eigenspace is D4-invariant too.

In the ordered character basis \((D,E,A,B,C)\), pullback by the M3 generators has matrices
\[
\rho(R)=
\begin{pmatrix}
0&1&0&0&0\\
-1&0&0&0&0\\
0&0&1&0&0\\
0&0&0&1&0\\
0&0&0&0&-1
\end{pmatrix},
\qquad
\rho(S)=
\begin{pmatrix}
-1&0&0&0&0\\
0&1&0&0&0\\
0&0&1&0&0\\
0&0&0&1&0\\
0&0&0&0&-1
\end{pmatrix}.
\]
Here the action on functions is defined by \((g\cdot f)(v)=f(g^{-1}v)\), so the matrices form a genuine (rather than contravariant) representation. They satisfy
\[
\rho(R)^4=\rho(S)^2=I,\qquad
\rho(S)\rho(R)\rho(S)=\rho(R)^{-1}.
\]
Both matrices are orthogonal, so this is an explicit representation
\[
D_4\longrightarrow O(5).
\]
It decomposes as the standard two-dimensional rotation/reflection representation, two trivial one-dimensional representations, and one one-dimensional representation with \(R\mapsto-1,\ S\mapsto-1\).

This gives a **genuine D4-invariant five-dimensional mode space of the M3 orbit graph**, not merely an arbitrarily chosen five-dimensional representation. Applying the phase-space construction of Sections 2–3 to this representation gives an exact D4-invariant Liouville measure and Bergman density on the associated five-mode type-IV chart.

**Important distinction:** \(\mathcal E_4\) is the eigenvalue-4 eigenspace of the *vertex Laplacian of the D4-orbit graph*. It is not yet identified with the previously certified eigenvalue-12 five-dimensional coexact eigenspace of the original Q6 edge Hodge operator. An explicit intertwiner between those two five-dimensional sectors, and a derivation of the oscillator coefficients from the same discrete action, remain open. Thus the result establishes a rigorous new D4–five-mode–Liouville bridge, but not yet the Wilson-to-Bergman limit.


## 8. Exact obstruction to identifying the two five-mode sectors

The natural edge transport induced by the M3 generators was tested exactly,
not merely inferred from the fact that R changes two edge directions.

Let \(E:\mathbb Q^{192}\to\mathbb Q^{256}\) be the inclusion of the original
Q6 cubical edge cochains into the D4 orbit-graph edge cochains, and let
\(V\in\mathbb Q^{192\times5}\) be an exact basis of
\(\ker(D_1^TD_1-12I)\). Let \(J_R,J_S\) be the signed permutation actions
on the 256 oriented orbit edges. The exact audit computes
\[
\operatorname{rank}\big[(I-EE^T)J_REV\big]=2,
\qquad
(I-EE^T)J_SEV=0.
\]
Thus \(R\) sends part of the old five-mode sector outside the original
192-edge subspace: the old sector is not an invariant subspace for the
M3 rotation.

There is a second, independent obstruction using the common generator S.
On the original Q6 coexact eigenspace, its induced matrix is exactly
\[
\rho_{\rm old}(S)=-I_5.
\]
On the M3 orbit-graph five-character eigenspace, in the basis \((D,E,A,B,C)\),
\[
\rho_{\rm orbit}(S)=\operatorname{diag}(-1,1,1,1,-1).
\]
These matrices are not similar. In fact, an intertwiner \(T\) would have to
satisfy
\[
T(-I_5)=\rho_{\rm orbit}(S)T,
\quad\text{hence}\quad
(\rho_{\rm orbit}(S)+I_5)T=0.
\]
The matrix \(\rho_{\rm orbit}(S)+I_5\) has rank 3 and kernel dimension 2,
so every such \(T\) has rank at most 2. No invertible five-dimensional
intertwiner exists.

This is a **no-go result for the natural identification** of the original
Q6 eigenvalue-12 coexact sector with the M3 orbit-graph eigenvalue-4
vertex sector. It does not invalidate either five-dimensional construction
separately. It says they are inequivalent D4 modules under the specified
M3 action, and therefore the Liouville–Bergman symmetry of the orbit-graph
five-mode chart cannot be transferred to the original Q6 D5 quotient by
claiming an intertwiner.

The exact reproducible calculation is
\`audits/audit_q6_d5_m3_d4_intertwiner_obstruction.py\`, with regression
test \`tests/test_q6_d5_m3_d4_intertwiner_obstruction.py\`.

### What remains possible

A bridge may still exist after changing the construction, but it must be
derived rather than imposed. Viable routes are:

1. build the full D4-equivariant orbit-edge Hodge complex on 256 edges and
   compute its own coexact five-dimensional sector;
2. search for a different five-dimensional Q6 sector whose restricted
   \(S\)-character matches \((-1,-1,+1,+1,+1)\), then test the full D4
   relations;
3. construct a nontrivial quotient, induced module, or bundle map between
   the two complexes, rather than an isomorphism of the original eigenspaces.

Until one of these constructions is completed, the correct status is:
**two exact five-dimensional sectors, no natural D4 intertwiner between them**.


## 9. Full D4-orbit edge Hodge complex: construction and audit protocol

The next comparison is now formulated on the full orbit graph, rather than
by transporting vectors inside the old 192-edge subspace. Starting from the
64 Q6 vertices, take the D4 orbit of the original 192 unoriented edges:
\[
E_{\rm orb}=\{\,\{g(u),g(v)\}: \{u,v\}\in E(Q_6),\ g\in D_4\,\},
\qquad |E_{\rm orb}|=256.
\]
Likewise take the D4 orbit of the original square *cyclic boundaries*.
Two squares with the same four vertices but different cyclic order are
retained as distinct labelled 2-cells; they must not be silently identified.
Let \(F_{\rm orb}\) be this set of unoriented cyclic square cells.

Orient each edge by its ordered vertex labels and each square by a chosen
canonical cyclic representative. Define integer boundary maps
\[
B_1:C_1(E_{\rm orb};\mathbb Z)\to C_0,\qquad
B_2:C_2(F_{\rm orb};\mathbb Z)\to C_1
\]
by the signed endpoints and signed cyclic boundaries. By construction,
\[
B_1B_2=0.
\]
The edge Hodge operator is
\[
\boxed{H_1^{\rm orb}=B_1^TB_1+B_2B_2^T.}
\]
Its harmonic edge space is \(\ker H_1^{\rm orb}\), and its positive spectrum
contains the exact coexact modes contributed by the square boundary map.
The D4 signed permutation actions \(J_0,J_1,J_2\) must satisfy
\[
J_0B_1=B_1J_1,\qquad J_1B_2=B_2J_2.
\]
Consequently \(H_1^{\rm orb}\) commutes with every \(J_1\), and each of its
eigenspaces is a D4 module.

The executable exact-arithmetic construction is
\`audits/audit_m3_d4_orbit_edge_hodge.py\`; its regression tests are in
\`tests/test_m3_d4_orbit_edge_hodge.py\`. It reports the orbit 2-cell count,
integer boundary ranks, first Betti number, exact edge-Hodge spectrum, and
the D4 character traces on every eigenspace. The computation has been
committed but **has not yet been executed**. In particular, this document
does not pre-announce a five-dimensional positive eigenspace: its existence,
eigenvalue, and D4 character are outputs to be established by running the
audit.

The resulting object is an equivariant chain complex. Whether it is a
regular square CW complex is a separate question: the audit must retain and
report incompatible cyclic cells and non-regular intersections rather than
assume them away. If regularity fails, the chain complex still has the
stated algebraic boundary maps, but its topological interpretation must be
specified as a labelled cell complex or an appropriate quotient/refinement.
