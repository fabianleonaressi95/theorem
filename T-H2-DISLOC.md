# T-H2-DISLOC — Homological Dislocation Density

## Scope

This specification concerns the relation between local dislocation densities, integrated Burgers flux over oriented 2-chains, and twisted cohomology classes.

It is an open problem. No global cohomological invariance may be claimed without explicit flatness, cocyclicity, and transport assumptions.

## Status

**Open problem. Conditional theorem only.**

## Prerequisites

This specification depends on:

- T-DEC-SE3;
- T-DEWIT;
- T-BIANCHI.

## Definitions

### Oriented 2-chain

Let

\[
C=\sum_f n_ff\in C_2(K;\mathbb Z)
\]

be an oriented 2-chain.

### Burgers resultant

Let \(\alpha_f\) be the discrete dislocation density associated with face \(f\). Let \(P_f\) transport \(\alpha_f\) into a common reference frame.

Define

\[
B_A(C)=\sum_f n_fP_f\alpha_f.
\]

This is the candidate Burgers resultant over \(C\).

### Twisted cocycle

The density \(\alpha\) is a twisted 2-cocycle if

\[
D_A\alpha=0.
\]

This condition is meaningful only after the covariant coboundary \(D_A\) has been rigorously defined.

### Twisted cohomology class

If the connection is flat, then \(d_A^2=0\), and one may define

\[
[\alpha]\in H^2(K;\mathcal V_A),
\]

where \(\mathcal V_A\) is the local coefficient system induced by the flat connection.

If the connection is not flat, this class is not automatically available.

## Conditional theorem

### Theorem 1 — Homological invariance under flatness

Assume:

1. the connection is flat;
2. \(\alpha\) is a twisted 2-cocycle;
3. the transports \(P_f\) are coherent with the connection;
4. \(C_1\) and \(C_2\) are homologous 2-chains.

Then

\[
B_A(C_1)=B_A(C_2).
\]

**Status.** Conditional theorem to prove.

### Proof strategy

If

\[
C_1-C_2=\partial D
\]

for some 3-chain \(D\), then

\[
B_A(C_1)-B_A(C_2)
=
B_A(\partial D).
\]

The proof must establish that, under flatness and cocyclicity,

\[
B_A(\partial D)=0.
\]

This is the central missing step.

## Curved correction

If the connection is not flat, the invariance statement fails in general. The corrected balance is expected to be

\[
B_A(C_1)-B_A(C_2)
=
\mathcal K_A(D),
\]

where \(\mathcal K_A(D)\) is a curvature-dependent correction associated with the 3-chain \(D\).

If

\[
D_A\alpha=\mathcal D_A(R\wedge e),
\]

then the candidate correction is

\[
\mathcal K_A(D)
=
\sum_{c\subset D}\mathcal D_A(R\wedge e)_c.
\]

**Status.** Candidate formula. Must be derived.

## Conceptual distinctions

| Level | Object | Meaning |
|---|---|---|
| Local | \(\alpha_f\) | Defect density on a face |
| Integrated | \(B_A(C)\) | Burgers flux over a 2-chain |
| Topological | \([\alpha]\) | Cohomology class, only under flatness and cocyclicity |

A nonzero local density does **not** imply a nontrivial cohomology class.

A distribution of defects may be cohomologically exact, meaning that its net flux over every closed 2-cycle vanishes even though local defects are present.

## Numerical tests

| Test | Statement | Success criterion |
|---|---|---|
| `test_flat_cocycle` | Flat connection and \(D_A\alpha=0\) | Cocycle condition verified |
| `test_homologous_chains` | \(C_1-C_2=\partial D\) | Boundary relation verified |
| `test_burgers_invariance_flat` | Flat case | \(B_A(C_1)=B_A(C_2)\) |
| `test_burgers_failure_curved` | Nonflat case | Correction term detected |
| `test_exact_defect_distribution` | \(\alpha=D_A\eta\) | Zero net flux on closed 2-cycles |
| `test_nontrivial_class` | Nontrivial cohomology class | Flux depends only on homology class |
| `test_c60_surface_flux` | C60 2-chains | Surface flux only, no 3D Bianchi claim |

## Acceptance criteria

T-H2-DISLOC may be merged only when:

- flatness is explicitly assumed or explicitly excluded;
- cocyclicity is explicitly assumed or explicitly excluded;
- the transport convention is fixed;
- the proof of homological invariance is complete;
- the curved correction is derived;
- the distinction between local defect, integrated flux, and cohomology class is tested.

## Open questions

- Under which conditions does \(B_A(C)\) define a homomorphism from \(H_2(K)\) to \(\mathbb R^3\)?
- What is the exact discrete definition of the curvature correction \(\mathcal K_A(D)\)?
- Does the correction vanish for all contractible 3-chains?
- Can the C60 audit provide evidence for a surface-level invariant without establishing a 3D cohomological theorem?
