# T-DEC-SE3 — Bundle-valued discrete exterior calculus on \(SE(3)\)

**Status:** foundational specification. The algebraic identities are stated with their hypotheses. This document does not claim that a complete higher-degree DEC complex or a physical dislocation theory has been established.

## Scope and conventions

Let \(K\) be a finite, connected, oriented cell complex of dimension at most three. A dual complex \(K^\ast\), if used, is additional structure. Cell orientations, local frames, edge orientations, and basepoints are part of the input.

\[
SE(3)=SO(3)\ltimes\mathbb R^3,\quad
(R_2,t_2)(R_1,t_1)=(R_2R_1,t_2+R_2t_1),
\]
\[
(I,0)\text{ is the identity},\qquad (R,t)^{-1}=(R^{-1},-R^{-1}t).
\]

## Definitions

### 1. Discrete connection and path transport

A discrete \(SE(3)\) connection on the 1-skeleton assigns to each oriented edge \(e=(v,w)\)
\[
G_{vw}=(R_{vw},t_{vw})\in SE(3),\qquad G_{wv}=G_{vw}^{-1}.
\]
For a path \(\gamma=(v_0,\ldots,v_n)\), define
\[
G_\gamma=G_{v_{n-1}v_n}\cdots G_{v_1v_2}G_{v_0v_1}.
\]
For composable paths \(\gamma_1:v_0\to v_1\) and \(\gamma_2:v_1\to v_2\),
\[
G_{\gamma_2\circ\gamma_1}=G_{\gamma_2}G_{\gamma_1}.
\]
Path transport is derived from edge transports. Distinct paths with the same endpoints need not have equal transport.

### 2. Representations and local frames

Let \(V\) be finite-dimensional and \(\rho:SE(3)\to GL(V)\) a representation. Distinguish the vector representation
\[
\rho_{\rm vec}(R,t)x=Rx
\]
(which ignores translations) from the homogeneous affine representation
\[
\widetilde\rho(R,t)=\begin{pmatrix}R&t\\0&1\end{pmatrix},\qquad
(x,1)^T\mapsto(Rx+t,1)^T.
\]
A local frame change is a family \(h_v\in SE(3)\), acting by
\[
G'_{vw}=h_wG_{vw}h_v^{-1},\qquad u'_v=\rho(h_v)u_v.
\]

### 3. Covariant coboundary on 0-cochains

For a vertex field \(u_v\in V\), represented in the frame at \(v\), set
\[
(d_Au)_{vw}=\rho(G_{vw})u_v-u_w.
\]
The result is represented in the frame at \(w\). Direct substitution gives
\[
(d_{A'}u')_{vw}=\rho(h_w)(d_Au)_{vw}.
\]

### 4. Face holonomy and curvature

For an oriented face \(f\), choose a boundary starting vertex \(v_f\) and traverse its boundary once:
\[
H_f=G_{\partial f,v_f}=(R_f,b_f)\in SE(3).
\]
Changing the starting vertex changes the based holonomy by conjugation with the intervening boundary transport. Thus the based matrix is not literally independent of starting point; its conjugacy class is. Comparisons between basepoints require explicit parallel transport.

The rotational curvature is \(R_f\in SO(3)\). Only when \(R_f\) lies in a neighbourhood where the principal logarithm is unambiguous may one set \(\mathcal R_f=\log R_f\in\mathfrak{so}(3)\). The translational component \(b_f\) is affine translational holonomy (closure defect) in the chosen frame; without further structure it is not torsion or dislocation density.

## Propositions and proofs

### Proposition 1 — Inverse and path composition

The inverse-edge and path-composition identities follow from the edge assignment and the ordered product definition. Product order matters because \(SE(3)\) is non-abelian.

### Proposition 2 — Gauge covariance of the 0-cochain coboundary

If \(G'_{vw}=h_wG_{vw}h_v^{-1}\) and \(u'_v=\rho(h_v)u_v\), then
\[
(d_{A'}u')_{vw}=\rho(h_w)(d_Au)_{vw}.
\]
Indeed,
\[
\begin{aligned}
(d_{A'}u')_{vw}
&=\rho(h_wG_{vw}h_v^{-1})\rho(h_v)u_v-\rho(h_w)u_w\\
&=\rho(h_w)\bigl(\rho(G_{vw})u_v-u_w\bigr).
\end{aligned}
\]
For the affine action, fields must be represented in homogeneous coordinates.

### Proposition 3 — Gauge transformation of based holonomy

For a loop \(\gamma\) based at \(v\),
\[
G'_\gamma=h_vG_\gamma h_v^{-1}.
\]
This follows by cancellation of intermediate frame factors in the path-ordered product. The conjugacy class is gauge invariant; the translational vector \(b_\gamma\) itself is frame-dependent.

### Proposition 4 — Local flatness, global holonomy, and \(d_A^2\)

For a cellular local system, the covariant coboundary on all degrees satisfies \(d_A^2=0\) when holonomy around the attaching loops of the 2-cells is trivial, with basepoint transports included.

**Crucial distinction:** local flatness does not require trivial holonomy around every global loop. A flat connection on a non-simply-connected complex can have nontrivial global holonomy and still define a local coefficient system with \(d_A^2=0\). Trivial holonomy on every loop is the stronger condition that makes transport path-independent between fixed endpoints.

For a curved connection, the square of a properly defined covariant coboundary is a curvature action and is not generally the zero operator. It may still vanish on particular cochains or in representations on which the holonomy acts trivially. A test must therefore exhibit a witness cochain on which the curvature action is nonzero.

**Status:** the 0-cochain covariance identity is proved here. A complete higher-degree operator \(d_A:C^k(K;V)\to C^{k+1}(K;V)\), including incidence transports and basepoint conventions, is not defined by the 0-cochain formula alone. The chain-level \(d_A^2\) statement is conditional on that construction.

### Proposition 5 — Rotational flatness does not imply affine flatness

Take a loop whose edge transports are translations \((I,a_1),\ldots,(I,a_m)\), with \(\sum_i a_i\ne0\). Then
\[
H_\gamma=(I,\sum_i a_i),
\]
so \(R_\gamma=I\) while \(b_\gamma\ne0\). This disproves identification of rotational curvature with full affine holonomy. It does not by itself identify \(b_\gamma\) with continuum torsion.

## Higher cochains: construction required

A higher-degree covariant coboundary cannot be defined merely by saying “transport each boundary value to the upper cell.” Required data are:

1. reference point/frame for every cell;
2. orientation convention for each incidence number \([\sigma:\tau]\);
3. specified path, or a path-independence theorem, from each incident lower-cell frame to the upper-cell frame;
4. explicit composition and path-change rules;
5. proof of gauge covariance;
6. proof identifying the obstruction to \(d_A^2=0\) with the chosen discrete curvature.

If a transport path changes by a loop with nontrivial holonomy, the transported value can change. Path choices cannot be suppressed in a curved connection. A cellular local system is available in the flat case, where transports depend only on homotopy classes relative to endpoints. In the curved case, a separate curvature-aware operator must be specified; it is not an ordinary local-coefficient cochain complex unless its coboundary squares to zero.

## Numerical tests and acceptance thresholds

A test report must include exact command, Python/dependency versions, random seed, fixture description, and maximum residual. A claimed pass count is not evidence until test files and a run log are available in the repository or attached to the PR.

| Test | Invariant | Criterion |
|---|---|---|
| identity/product/inverse | \(SE(3)\) group laws | residual \(\le10^{-14}\) |
| inverse transport | \(G_{wv}G_{vw}=I\) | residual \(\le10^{-14}\) |
| path composition | ordered path products | residual \(\le10^{-14}\) |
| vector gauge covariance | transform connection and vector field | residual \(\le10^{-12}\) |
| affine gauge covariance | homogeneous-coordinate action | residual \(\le10^{-12}\) |
| loop holonomy conjugation | \(H'_\gamma=h_vH_\gamma h_v^{-1}\) | residual \(\le10^{-12}\) |
| face basepoint change | conjugacy after boundary transport | residual \(\le10^{-12}\) |
| local flatness | trivial face holonomies | higher coboundary-square residual \(\le10^{-12}\) |
| flat nontrivial global holonomy | nontrivial \(\pi_1\) witness | \(d_A^2=0\), global loop may be nonidentity |
| curvature obstruction | curved face plus witness cochain | nonzero curvature action on witness |
| pure translation holonomy | \(R_\gamma=I,\ b_\gamma\ne0\) | affine holonomy detects translation |
| surface fixture | closed 2D fixture | cell/orientation/boundary checks pass |

A surface fixture tests the 2D connection API only. It cannot validate a 3D Bianchi identity.

## Open questions

1. Is the higher-degree operator a cellular local-coefficient coboundary (flat case), a lattice-gauge curvature operator, or a DEC operator with explicit curvature correction?
2. Which cellwise basepoints and transport paths are canonical for the chosen primal/dual pair?
3. Does \(b_f\) represent only affine closure defect, or an integrated torsion under a specified coframe?
4. Which inner products and primal/dual volume weights define adjoints, Hodge stars, and a Laplacian?
5. What refinement maps and convergence notion define a continuum DEC limit?

## Acceptance criteria

- [ ] Group product, inverse, and path order are tested.
- [ ] Vector and affine representations are tested separately.
- [ ] Gauge transformation includes both connection and cochain.
- [ ] Face holonomy comparisons include basepoint conjugation.
- [ ] Local flatness is distinguished from trivial global holonomy.
- [ ] Higher-degree incidence transports are defined before claiming \(d_A^2=0\).
- [ ] Curvature obstruction is tested on a witness cochain.
- [ ] Translational holonomy is not labelled torsion/dislocation without a coframe derivation.
- [ ] Surface tests are not used as evidence for volumetric Bianchi identities.
- [ ] Numerical evidence includes committed tests and a reproducible run record.

## Dependency order

- **T-DEWIT** depends on a defined discrete coframe, its gauge action, and a derived torsion operator. It must not identify \(b_f\) with torsion by definition.
- **T-BIANCHI** requires a genuine 3D cell complex and a basepoint-aware non-abelian discrete Bianchi construction.
- **T-H2-DISLOC** requires a well-defined coefficient system/complex, cocycle condition, and pairing with chains. Homological invariance is conditional on these data.

T-DEC-SE3 is the foundation for these modules, but does not prove them.
