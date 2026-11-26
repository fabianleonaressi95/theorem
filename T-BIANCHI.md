# T-BIANCHI — Discrete Covariant Bianchi Identities

## Scope

This specification defines the discrete covariant Bianchi identities for an \(SE(3)\)-valued connection on a three-dimensional cellular complex.

It requires a volumetric complex. A two-dimensional surface such as C60 cannot validate a three-dimensional Bianchi identity because it has no 3-cells.

## Status

**Derivation to complete. This is not an assumed identity.**

## Prerequisites

This specification depends on:

- T-DEC-SE3;
- T-DEWIT.

Required objects:

- an \(SE(3)\)-valued connection;
- face holonomies;
- a discrete co-frame \(e\);
- a discrete torsion \(T\);
- a discrete curvature \(R\);
- a covariant discrete exterior product \(\wedge_A\).

## Continuum identities

In the continuum, with connection \(\omega\), co-frame \(e\), torsion \(T\), and curvature \(R\), the Cartan–Bianchi identities are

\[
D_\omega R=0,
\]

\[
D_\omega T=R\wedge e.
\]

The first is the Bianchi identity for curvature. The second is the Bianchi identity for torsion.

The second identity implies that, when curvature is nonzero, the covariant derivative of torsion is not generally zero:

\[
R\neq0
\quad\Longrightarrow\quad
D_\omega T\neq0
\quad\text{in general}.
\]

## Definitions

### Volumetric holonomy

Let \(c\) be an oriented 3-cell with boundary faces

\[
\partial c=f_1+\cdots+f_m.
\]

Define

\[
H_c
=
H_{f_m}\cdots H_{f_2}H_{f_1}
=
(R_c,b_c).
\]

### Rotational Bianchi residual

Define

\[
\mathcal B_R(c)=R_c-I.
\]

### Translational Bianchi residual

Define

\[
\mathcal B_T(c)=b_c-\mathcal C_c,
\]

where \(\mathcal C_c\) is the curvature–co-frame coupling term.

The term \(\mathcal C_c\) must be derived from the ordered composition of the face holonomies. It must not be inserted by hand.

## Theorem to prove

### Theorem 1 — Discrete Bianchi identities

Let \(K\) be a three-dimensional oriented cellular complex with:

1. an \(SE(3)\)-valued connection;
2. a coherent system of local frames;
3. a discrete co-frame \(e\);
4. a discrete torsion \(T=D_Ae\);
5. a discrete curvature \(R\).

Then, for every oriented 3-cell \(c\),

\[
\mathcal B_R(c)=0,
\]

\[
\mathcal B_T(c)=0.
\]

**Status.** Theorem to prove.

## Proof strategy

1. Compute the \(SE(3)\) holonomy of each boundary face.
2. Compose the face holonomies according to the orientation of \(\partial c\).
3. Separate the rotational and translational components.
4. Prove cancellation of the rotational component.
5. Derive the translational coupling term from the ordered product of translations and rotations.
6. Show that the remaining translational residual equals the discrete version of \(R\wedge e\).

## Correct formulation

The correct discrete statement is not

\[
D_A\alpha=0.
\]

The correct candidate is

\[
D_A\alpha=\mathcal D_A(R\wedge e),
\]

where \(\mathcal D_A\) is the discrete covariant exterior derivative and \(\mathcal D_A\) denotes the discrete covariant exterior product.

In the flat limit,

\[
R=0
\quad\Longrightarrow\quad
D_A\alpha=0,
\]

but this must be derived from the discrete identity, not imposed.

## Required volumetric test complex

The test suite must include at least one of the following:

- a tetrahedralization of a small three-dimensional domain;
- a prismatic thickening of the C60 surface;
- a cubic lattice with controlled \(SE(3)\) connection;
- a complex whose boundary contains C60 but whose interior contains 3-cells.

The C60 complex may be used only as a boundary subcomplex.

## Numerical tests

| Test | Statement | Success criterion |
|---|---|---|
| `test_volume_complex` | Valid 3D complex | Oriented boundary and 3-cells present |
| `test_bianchi_rotation` | Curvature Bianchi | \(\mathcal B_R(c)=0\) |
| `test_bianchi_translation` | Torsion Bianchi | \(\mathcal B_T(c)=0\) |
| `test_coupling_term` | Nonzero curvature | \(R\wedge e\) term is required |
| `test_flat_limit` | \(R=0\) | Coupling term vanishes |
| `test_c60_boundary_only` | C60 as boundary | No 3D Bianchi claim on C60 alone |
| `test_gauge_covariance_bianchi` | Frame change | Bianchi residual remains zero |

## Acceptance criteria

T-BIANCHI may be merged only when:

- the volumetric complex is explicitly constructed;
- the co-frame is defined;
- the discrete exterior product is defined;
- the coupling term is derived;
- both Bianchi residuals are proved to vanish;
- the tests distinguish C60 surface data from volumetric data;
- no identity is asserted without proof.

## Open questions

- What is the exact discrete definition of \(\wedge_A\)?
- Does the identity hold for arbitrary cellular complexes or only for sufficiently regular meshes?
- What is the correct transport of \(R\wedge e\) from faces to 3-cells?
- Does the discrete identity survive nonuniform dual-cell measures?
