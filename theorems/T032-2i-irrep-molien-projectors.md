# T032 — Exact Molien covariants and the 2I isotypic-projector interface

## Scope

T021 already records the nine covariant Molien numerators for the binary
icosahedral group. T032 turns that finite data into an independently testable
exact-arithmetic module inside theroem. It has no dependency on the slower
quaternion-bridge repository.

The implementation computes multiplicities in restrictions of
\(\operatorname{Sym}^m(\mathbb C^2)\) and checks their dimension
decomposition. It does not claim to construct all nine irreducible unitary
matrix models or a full character table.

## Exact data imported from T021

For each irreducible label rho, T021 gives
\[
M_\rho(t)=\sum_{m\geq0}b_{m,\rho}t^m
=\frac{N_\rho(t)}{(1-t^{12})(1-t^{20})}.
\]
The numerator supports are encoded in src/t032_2i_molien.py. Coefficients
are integers, obtained by counting solutions m=n+12a+20b with n in the
numerator support.

The exact decomposition identity is
\[
\sum_{\rho\in\widehat{2I}}d_\rho b_{m,\rho}=m+1,
\]
because dim Sym^m(C^2)=m+1. The dimensions are 1,2,2,3,3,4,4,5,6, and
\[
\sum_\rho d_\rho^2=1+4+4+9+9+16+16+25+36=120.
\]

## Character projector

For a unitary representation U of 2I, the central isotypic projector is
\[
P_\rho=\frac{d_\rho}{120}
\sum_{g\in2I}\overline{\chi_\rho(g)}U(g).
\]
Its idempotence and orthogonality follow from character orthogonality.
T032 records the exact normalization but does not claim a computed matrix
for P: that requires explicit character values and representation matrices.

## Verification

Run from the repository root:
python -m unittest tests.test_t032_2i_molien -v

Tests check all nine labels, sum of squares, initial coefficients, and
dimension decomposition for degrees 0 through 240.

## Epistemic status

- PROVED (finite-group theory): character-projector formula and normalization,
  conditional on the stated irreducible character.
- EXACT DATA TRANSCRIBED FROM T021: nine Molien numerator supports.
- VERIFIED BY EXACT INTEGER TESTS: coefficient generation and decomposition
  identity through degree 240 (once the test command passes).
- OPEN: explicit unitary matrices for all nine irreps, exact machine-readable
  character table, and direct matrix evaluation of each projector.
- NOT CLAIMED: new analytic torsion result or Q6/PRISM continuum limit.

## Provenance

All implementation is internal to fabianleonaressi95/theroem. No code import,
CI job, or runtime dependency comes from rgs-qlg-quaternion-bridge.

Sources: T021, T031, and T024.
