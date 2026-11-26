# T-DEC-SE3 — Bundle-Valued Discrete Exterior Calculus

## Scope

This specification defines the foundational discrete structure for a cellular complex equipped with an `SE(3)`-valued connection. It defines transport, covariant difference, face holonomy, rotational curvature, and affine translational defect.

It does **not** claim a discrete DeWit defect theory, a discrete Bianchi identity, or a cohomological classification of dislocation densities. Those are treated in separate specifications.

## Status

**Foundational specification. Definitions and covariance must be completed and tested before any downstream theorem is stated.**

## Conventions

Let \(K\) be a finite, connected, oriented cellular complex of dimension at most \(3\).

- Vertices are denoted \(v,w\).
- Oriented edges are denoted \(e=(v,w)\).
- Oriented faces are denoted \(f\).
- Oriented 3-cells are denoted \(c\).
- All orientations, basepoints, local frames, and transport conventions are explicit data.

The structure group is

\[
SE(3)=SO(3)\ltimes\mathbb R^3.
\]

For \(A=(R,t)\in SE(3)\), composition is

\[
(R_2,t_2)(R_1,t_1)
=
(R_2R_1,\;t_2+R_2t_1).
\]

The identity is \((I,0)\). The inverse is

\[
(R,t)^{-1}=(R^{-1},-R^{-1}t).
\]

## Definitions

### Discrete \(SE(3)\) bundle

A discrete \(SE(3)\) bundle over \(K\) consists of:

- a fiber \(F_v\) at every vertex \(v\);
- for every oriented edge \(e=(v,w)\), a transport
  \[
  G_{vw}=(R_{vw},t_{vw})\in SE(3);
  \]
- the inverse condition
  \[
  G_{wv}=G_{vw}^{-1};
  \]
- path-composition consistency:
  \[
  G_{v_0v_n}=G_{v_{n-1}v_n}\cdots G_{v_0v_1}.
  \]

### Representation

Let \(V\) be a finite-dimensional real vector space and let

\[
\rho:SE(3)\to GL(V)
\]

be a representation.

For vector quantities in \(\mathbb R^3\), use

\[
\rho(R,t)x=Rx.
\]

For affine quantities, use

\[
\tilde\rho(R,t)
\begin{pmatrix}
x\\1
\end{pmatrix}
=
\begin{pmatrix}
R&t\\
0&1
\end{pmatrix}
\begin{pmatrix}
x\\1
\end{pmatrix}.
\]

### Covariant difference

For a \(0\)-cochain \(u\) with \(u_v\in V_v\), define

\[
(d_Au)_{vw}
=
\rho(G_{vw})u_v-u_w.
\]

This is the discrete covariant difference from \(v\) to \(w\).

### Higher-degree covariant coboundary

For \(k\ge1\), a \(k\)-cochain assigns a value to each oriented \(k\)-cell in a chosen local reference frame.

For a \(1\)-cochain \(\omega\), define

\[
(d_A\omega)_f
=
\sum_{e\subset\partial f}
\operatorname{sgn}(e,f)\,
P_{e\to f}\omega_e,
\]

where \(P_{e\to f}\) is the transport from the reference frame of \(e\) to the reference frame of \(f\).

**Required clarification before implementation:**

- orientation of each edge relative to its face;
- basepoint of each edge;
- transport path from edge frame to face frame;
- order of noncommutative transport composition;
- behavior under mesh refinement.

### Face holonomy

For an oriented face \(f\) with boundary

\[
\partial f=e_1+\cdots+e_m,
\]

define

\[
H_f=G_{e_m}\cdots G_{e_2}G_{e_1}
=(R_f,b_f).
\]

Here:

- \(R_f\in SO(3)\) is the rotational holonomy;
- \(b_f\in\mathbb R^3\) is the affine closure defect, expressed in the face reference frame.

### Rotational curvature

When \(R_f\) is sufficiently close to the identity, define

\[
\mathcal R_f=\log R_f\in\mathfrak{so}(3).
\]

In general, retain \(R_f\in SO(3)\). Do not assume that the logarithm is globally available or single-valued.

## Propositions

### Proposition 1 — Transport inverse

For every oriented edge \(e=(v,w)\),

\[
G_{wv}=G_{vw}^{-1}.
\]

**Proof to complete.** Direct consequence of the definition of a discrete connection and the inverse law in \(SE(3)\).

### Proposition 2 — Path composition

For every oriented path \(v_0\to v_1\to\cdots\to v_n\),

\[
G_{v_0v_n}
=
G_{v_{n-1}v_n}\cdots G_{v_0v_1}.
\]

**Proof to complete.** Induction on path length, using associativity of \(SE(3)\).

### Proposition 3 — Gauge covariance

Let \(h_v\in SE(3)\) be a local frame change at each vertex. If

\[
G'_{vw}=h_wG_{vw}h_v^{-1},
\]

then the covariant difference transforms according to the representation \(\rho\).

**Proof to complete.** Substitute \(G'_{vw}\) into the definition of \(d_Au\), then use associativity and the representation law.

### Proposition 4 — Failure of \(d_A^2\)

In general,

\[
d_A^2\neq0.
\]

The obstruction is measured by holonomy around closed loops.

For a loop \(\gamma\), write

\[
H_\gamma=(R_\gamma,b_\gamma).
\]

Then:

- \(R_\gamma\neq I\) indicates rotational curvature;
- \(b_\gamma\neq0\) indicates affine translational non-closure;
- \(R_\gamma=I\) does **not** imply \(b_\gamma=0\).

### Proposition 5 — Flatness criterion

If

\[
H_\gamma=(I,0)
\]

for every closed loop \(\gamma\), then the connection is flat and

\[
d_A^2=0.
\]

In this case, the coefficient system is a local system and twisted cohomology is available.

If the connection is not flat, \(d_A^2\neq0\) in general. The failure is curvature data, not an algebraic error.

## Numerical tests

| Test | Statement | Success criterion |
|---|---|---|
| `test_inverse_transport` | \(G_{wv}=G_{vw}^{-1}\) | Exact or error below \(10^{-14}\) |
| `test_path_composition` | \(G_{v_0v_2}=G_{v_1v_2}G_{v_0v_1}\) | Error below \(10^{-14}\) |
| `test_gauge_covariance` | Local frame change | Observable transforms by declared law |
| `test_face_holonomy` | Face holonomy | Independent of boundary starting point after transport |
| `test_flat_connection` | \(H_\gamma=(I,0)\) | \(d_A^2=0\) |
| `test_rotational_curvature` | \(R_\gamma\neq I\) | Curvature localized on the relevant face |
| `test_pure_translation_defect` | \(R_\gamma=I\), \(b_\gamma\neq0\) | Translational defect detected independently |
| `test_c60_regression` | Existing C60 audit | No regression of merged PR #341 results |

## Acceptance criteria

T-DEC-SE3 may be merged only when:

- all transport conventions are explicit;
- all local frames and basepoints are explicit;
- gauge covariance is proved and tested;
- face holonomy is proved and tested;
- flatness and curvature are separated;
- the C60 surface is never used to validate a 3-dimensional Bianchi identity;
- no downstream theorem is claimed as proved.

## Open questions

- What is the canonical transport from an edge frame to an incident face frame?
- Which class of mesh refinements preserves the discrete holonomy?
- Under which conditions does the affine closure defect \(b_f\) descend to a well-defined geometric object?
- What is the correct notion of gauge equivalence for the full \(SE(3)\) connection?
