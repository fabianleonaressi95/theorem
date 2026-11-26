# T-DEWIT — Discrete DeWit Defect Equations

## Scope

This specification separates rotational curvature, torsion, and translational defect. It defines the discrete objects needed to compare the \(SE(3)\) holonomy framework with the continuum theory of elastoplastic defects.

It does **not** assume that the face closure defect \(b_f\) is already a physical dislocation density.

## Status

**Derivation to complete. No theorem may be merged until the relationship between \(b_f\), torsion, and dislocation density is derived from explicit conventions.**

## Prerequisites

This specification depends on T-DEC-SE3.

Required objects:

- an \(SE(3)\)-valued discrete connection \(G\);
- face holonomy
  \[
  H_f=(R_f,b_f);
  \]
- a discrete co-frame \(e\);
- a covariant discrete derivative \(D_A\);
- dual cells and their measures.

## Definitions

### Discrete co-frame

A discrete co-frame is an assignment

\[
e_c\in\mathbb R^3\otimes\Lambda^1(T_cK)
\]

to each relevant cell \(c\), together with transport rules between incident cells.

The co-frame is not optional. Without it, there is no well-defined discrete torsion and therefore no well-defined comparison with DeWit theory.

### Discrete torsion

For an oriented face \(f\), define

\[
T_f=D_Ae_f.
\]

This is the discrete torsion associated with the face.

### Dislocation density

Let \(|f^\ast|\) denote the measure of the dual cell associated with \(f\). Let \(P_f\) denote the transport from the face reference frame to the chosen global reference frame.

Define

\[
\alpha_f
=
\frac{P_fT_f}{|f^\ast|}.
\]

This is a candidate discrete dislocation density.

### Integrated Burgers flux

For an oriented 2-chain

\[
C=\sum_f n_ff,
\]

define

\[
B_A(C)=\sum_f n_fP_f\alpha_f.
\]

This is a candidate Burgers resultant, subject to the cinematic convention and reference-frame choice.

## Continuum comparison

In the continuum theory of elastoplastic distortion, one writes

\[
\beta=\beta^e+\beta^p.
\]

The dislocation density is associated with the incompatibility of the plastic distortion:

\[
\alpha=\operatorname{Curl}\beta^p,
\]

up to sign and index conventions.

In a Cartan formalism, with co-frame \(e\), connection \(\omega\), torsion \(T\), and curvature \(R\),

\[
T=D_\omega e=de+\omega\wedge e,
\]

\[
R=d\omega+\omega\wedge\omega.
\]

The discrete object \(\alpha_f\) must be compared with a discretization of \(T\), not directly with \(R_f\).

## Propositions

### Proposition 1 — Rotational flatness does not imply translational closure

If

\[
R_f=I,
\]

then it does not follow that

\[
b_f=0.
\]

**Proof to complete.** Construct a loop whose rotational components compose to the identity while its translational components fail to close. This establishes the existence of a purely translational defect.

### Proposition 2 — Torsion is not face closure defect

In general,

\[
T_f\neq b_f.
\]

**Proof to complete.** The object \(b_f\) is an affine holonomy defect. The object \(T_f\) is a covariant derivative of the discrete co-frame. Their equality requires additional structure and normalization.

### Proposition 3 — Candidate relation

Under explicit assumptions on mesh regularity, co-frame transport, and dual-cell normalization,

\[
\alpha_f
=
\frac{1}{|f^\ast|}
P_f(D_Ae)_f.
\]

**Status.** Candidate proposition. Must be derived, not assumed.

## Required convention table

| Continuum object | Discrete candidate | Required convention |
|---|---|---|
| Plastic distortion \(\beta^p\) | To be defined | Edge or face assignment |
| Torsion \(T\) | \(D_Ae\) | Co-frame and transport rule |
| Dislocation density \(\alpha\) | \(\alpha_f\) | Dual-cell normalization |
| Curvature \(R\) | \(R_f\) | Rotational holonomy |
| Burgers vector | \(B_A(C)\) | 2-chain and common reference frame |
| Disclination density | \(\mathcal R_f\) | Rotational holonomy and normalization |

## Numerical tests

| Test | Statement | Success criterion |
|---|---|---|
| `test_pure_translation_defect` | \(R_f=I\), \(b_f\neq0\) | Translational defect detected |
| `test_pure_rotation_defect` | \(R_f\neq I\), \(b_f=0\) | Rotational defect detected |
| `test_torsion_definition` | \(T_f=D_Ae_f\) | Co-frame covariance verified |
| `test_density_normalization` | \(\alpha_f=T_f/|f^\ast|\) | Convergence under refinement |
| `test_burgers_2chain` | \(B_A(C)\) | Correct orientation and transport |
| `test_dewit_sign_convention` | Sign and index convention | Explicit correspondence table verified |
| `test_local_vs_global_defect` | Nonzero local density | Does not imply nontrivial cohomology class |

## Acceptance criteria

T-DEWIT may be merged only when:

- the co-frame is fully defined;
- the transport rules are explicit;
- the dual-cell normalization is defined;
- the sign convention is fixed;
- the relation between \(b_f\), \(T_f\), and \(\alpha_f\) is derived;
- the distinction between local defect, integrated flux, and topological class is tested.

## Open questions

- What is the minimal regularity assumption on the mesh?
- Which dual-cell normalization preserves the correct continuum limit?
- Does \(b_f\) admit a coordinate-free interpretation as a torsion density?
- Under which conditions is \(B_A(C)\) independent of the chosen common reference frame?
