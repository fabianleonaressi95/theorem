# T161 — Q6–IVM–rhombic triacontahedron: Lorentzian spin lift

**Classification:** exact set identity for the projected cube and its Minkowski-sum representation; finite numerical general-position audit; conditional Lorentzian algebra; IVM/FCC map and continuum spinorial limit open.  
**Dependencies:** T129 (golden cut-and-project frame); T146 (Q6–IVM–PSU carrier and tetrahedral comparison); T147 (Spin(6) golden-frame lift); T148 (PSU–Anti-Twin chiral sheet lock); T149 (negative Q6 Clifford-operator result). T150 is a separate D6/Fibonacci two-sheet suborbit and is comparison-only.

## 1. Scope and terminology

This card connects four distinct objects without identifying them prematurely:

1. the six-bit hexagram carrier \(Q_6=\{0,1\}^6\);
2. the 6D golden cut-and-project frame and its 3D internal acceptance window;
3. the IVM/FCC vector-equilibrium geometry and the icosahedral rhombic triacontahedron;
4. Lorentzian spacetime and its \(\operatorname{Spin}^{+}(1,3)\) spinor representation.

“Minkowski sum” and “Minkowski spacetime” are different structures. The first constructs a spatial convex body; the second is a Lorentzian metric. Their connection here is mediated by a candidate coframe, not by an equality of geometries.

## 2. Exact golden 6D frame

Let
\[
\phi=(1+\sqrt5)/2,\qquad \phi_*=(1-\sqrt5)/2=-\phi^{-1},
\]
and define
\[
A(p)=\begin{pmatrix}
0&0&1&-1&p&p\\
1&-1&p&p&0&0\\
p&p&0&0&1&-1
\end{pmatrix},
\quad
P_\parallel=\frac{A(\phi)}{\sqrt{2(2+\phi)}},
\quad
P_\perp=\frac{A(\phi_*)}{\sqrt{2(2+\phi_*)}}.
\]
The frame identities are
\[
P_\parallel P_\parallel^T=I_3,\quad
P_\perp P_\perp^T=I_3,\quad
P_\parallel P_\perp^T=0.
\]
Thus the stacked projections form an orthogonal 6D frame. These are the projections already implemented in the companion cut-and-project construction and used by T129/T146; this card reuses that convention.

For each hexagram \(q\in\{0,1\}^6\), centre it:
\[
c(q)=q-\tfrac12\mathbf1,\qquad
x_\parallel(q)=P_\parallel c(q),\qquad
x_\perp(q)=P_\perp c(q).
\]

## 3. T161A — internal window as a Minkowski-sum zonotope

Let \(p_i=P_\perp e_i\) be the six columns of \(P_\perp\), and set \(g_i=p_i/2\). The projected centred cube is exactly
\[
W=P_\perp([-\tfrac12,\tfrac12]^6)
=\left\{\sum_{i=1}^6t_i g_i:-1\le t_i\le1\right\}
=[-g_1,g_1]\oplus\cdots\oplus[-g_6,g_6].
\]
This is the 3D zonotope/acceptance window of the golden cut-and-project model. For the stated golden frame, every triple of generators is linearly independent in the numerical audit; hence the generators are in 3D general position. The standard 3D zonotope counts for six generators then give 32 vertices, 60 edges and 30 parallelogram facets. In this golden icosahedral projection the facets are rhombi, so the window is a rhombic triacontahedron.

The 64 Q6 internal images are
\[
X_\perp(q)=P_\perp(q-\tfrac12\mathbf1)
=\sum_{i=1}^6(2q_i-1)g_i.
\]
They are the 64 projected cube-corner images in \(W\), not 64 extreme vertices of \(W\). The zonotope has 32 extreme vertices. The exact antipodal relation is
\[
X_\perp(\mathbf1-q)=-X_\perp(q).
\]
Q6's parity bipartition is also 32+32, but parity classes and antipodal pairs are different partitions; do not identify them without a separate map.

**Status:** the set identity and antipodal relation are exact. General position is checked numerically for the specified golden frame; the zonotope counts then follow from standard combinatorics. This is not a graph isomorphism: Q6 has 64 vertices/192 edges, whereas the triacontahedron has 32 vertices/60 edges.

## 4. T161B — IVM/FCC is a separate symmetry sector

T146 distinguishes the Fuller vector equilibrium/IVM spatial structures from the 64-state Q6 carrier and records the unresolved 64-tetrahedron-cell identification. The IVM/FCC vector-equilibrium convention uses 12 vectors in six antipodal pairs and has cubic \(O_h\) symmetry. The golden six-axis projection and rhombic triacontahedron have icosahedral symmetry \(I_h\).

The previously used IVM normalization \(NN^T=2I_3\) is a tight-frame identity for the six independent FCC directions; it does not imply that those directions are the golden icosahedral generators \(g_i\). A valid bridge requires an explicit map between the two decorated configurations and must state what it preserves: incidence, metric, group action, orientation, or only coarse-graining. No such map is asserted here. Nor does the 32+32 Q6 bipartition prove the existence of 64 IVM tetrahedra or an adjacency-preserving correspondence.

## 5. T161C — Lorentzian coframe candidate from PSU–Anti-Twin

T148 supplies the two-sheet variables and locked spinor subspace. If, as an additional physical hypothesis, \(u_+\) and \(u_-\) are future-directed unit timelike vectors in a common Minkowski space with signature \((+---)\), write
\[
u_+\cdot u_-=\cosh\chi,\quad
v_0=(u_++u_-)/2,\quad
s_{\rm AT}=(u_+-u_-)/2.
\]
Then exactly
\[
v_0\cdot s_{\rm AT}=0,\quad
v_0^2=\cosh^2(\chi/2),\quad
s_{\rm AT}^2=-\sinh^2(\chi/2).
\]
For \(\chi>0\),
\[
e_0=\frac{v_0}{\cosh(\chi/2)},\qquad
e_{\rm AT}=\frac{s_{\rm AT}}{\sinh(\chi/2)}
\]
are respectively unit timelike and unit spacelike. This is a conditional Minkowski identity, not a derivation that the existing fluid fields are normalized relativistic four-velocities. At \(\chi=0\), the relative vector vanishes and this normalization is undefined.

A spatial triad must be constructed independently in \(e_0^\perp\), for example by projecting three independent spatial IVM/triacontahedral directions and orthonormalizing with the induced negative-definite metric. Only then can one define
\[
g_{\mu\nu}=\eta_{ab}e^a{}_\mu e^b{}_\nu,\qquad
\eta=\operatorname{diag}(1,-1,-1,-1).
\]
The 6D internal 3-plane is not physical time by definition. The existing torsion-coupled internal-axis selector remains a candidate-selection algorithm until an independent torsion trace and Lorentzian causal structure are established.

## 6. T161D — independent Cartan connection and spin lift

For a nondegenerate Lorentzian coframe \(e^a\), retain an independent metric-compatible connection \(\omega^{ab}\):
\[
T^a=de^a+\omega^a{}_b\wedge e^b,\qquad
R^{ab}=d\omega^{ab}+\omega^a{}_c\wedge\omega^{cb}.
\]
Both may be nonzero. The teleparallel branch \(R^{ab}=0\) is a distinct constrained connection choice, not the generic Riemann–Cartan branch. The discrete SE(3) Bianchi/covariance audit is not yet an \(\mathrm{ISO}^{+}(1,3)\) audit.

Given a Lorentzian coframe and time/space orientation, the spin lift is
\[
\operatorname{Spin}^{+}(1,3)\simeq SL(2,\mathbb C),\qquad
\{\gamma^a,\gamma^b\}=2\eta^{ab}I_4,
\]
with
\[
\mathcal D_\mu\psi=
\left(\partial_\mu+\tfrac14\omega_{\mu ab}\gamma^{ab}\right)\psi,
\quad
\slashed D=i\gamma^ae_a{}^\mu\mathcal D_\mu.
\]
The six-dimensional Euclidean cut-and-project frame does not by itself yield a noncompact Lorentz group: the \(\operatorname{Spin}(6)\) and \(\operatorname{Spin}(1,3)\) structures require an explicit signature-selecting construction, not a formal group identification.

A local Dirac spinor has four complex components. The 64 Q6 labels index sites/cells, so a lattice field has carrier \(\mathbb C^{64}\otimes\mathbb C^4\), with the T148 sheet factor subject to its right/left lock. Do not interpret the 64 Q6 labels as 64 spinor components.

## 7. T149 negative result and continuum gate

T149 proves that the bare identity-link operator
\[
D_{Q6}=\frac12\sum_iK_i\otimes\Gamma_i
\]
has
\[
D_{Q6}^2=-\frac32I,\qquad
\operatorname{spec}(iD_{Q6})=\{-\sqrt{3/2},+\sqrt{3/2}\},
\]
with multiplicity 256 for each sign. It therefore does not supply the desired massless low-energy Dirac branch. T161 does not override that result. A physical lattice fermion still requires a refinement-consistent kinetic operator or a domain-wall/overlap construction, with locality, self-adjoint Hamiltonian, spectral-flow, species and anomaly tests.

## 8. Status ledger

| Claim | Status |
|---|---|
| Golden \(P_\parallel,P_\perp\) orthogonal 3+3 frame | Exact algebraic identities; finite numerical audit |
| Projected centred cube equals six-segment Minkowski sum | Exact set identity |
| Six generators in general position; 32/60/30 zonotope counts | Numerical general-position check plus standard zonotope combinatorics |
| 64 projected Q6 points and antipodal pairing | Exact finite construction |
| Q6 graph is the triacontahedron graph | False by vertex/edge counts |
| IVM/FCC to golden icosahedral metric/equivariant map | Open |
| PSU–Anti-Twin timelike/spacelike decomposition | Exact conditional identity; physical hypotheses unverified |
| Lorentzian coframe and ISO\((1,3)\) Cartan lattice | Open |
| Spin\((1,3)\) lift from Q6/IVM data | Open |
| Continuum Dirac limit | Open; T149 bare operator is exactly gapped |

## 9. Reproduction

\`\`\`bash
python scripts/audit_q6_golden_zonotope_t161.py
python -m unittest discover -s tests -p "test_q6_golden_zonotope_t161.py" -v
\`\`\`
