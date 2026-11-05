# T045 — Exhaustive exact certificate for the 2I representation layer

## Objective

Independently consolidate the finite representation claims used by T031–T044. T045 is a finite exact-algebra certificate; it is not a new continuum theorem.

## Source audit findings

The current `main` branch contains T034's exact arithmetic implementation and T036's independent symmetric-power extraction.

- T034 constructs nine representations over `Q(sqrt(5), i)`. Its homomorphism check verifies the identity and every Cayley edge for two generators, which proves the homomorphism on the generated finite group. Its weighted-unitarity check loops over all 120 group elements.
- T034 checks all 81 character row inner products and all 81 column inner products, with class sizes summing to 120. Its matrix-coefficient Schur test covers all coefficients.
- T034's matrix-unit test samples multiplication quadruples when there are more than 60. Therefore the phrase “all matrix-unit multiplication identities were exhaustively checked” would be too strong for the existing T034 run.
- T034's projector test checks idempotence, rank, and completeness for degrees 0–13, but explicitly requests pairwise orthogonality and commutation only for degrees 0–7.
- T036 extracts a second set of nine models and checks all 120 matrices against their induced invariant Gram matrices and recovers all 81 character values. It does not claim standard-Euclidean unitarity in its arbitrary extracted bases; the correct statement is unitarity with respect to the displayed positive invariant Gram matrix.
- The Molien variable in this chain is the defining two-dimensional representation (V) of (2Isubset SU(2)), and the coefficient is the multiplicity of (ho) in (operatorname{Sym}^m(V)).

## T045 implementation

`src/t045_2i_representation_certificate.py` adds exhaustive finite checks:

1. Rebuild the exact order-120 group and nine T034 models.
2. Check generator-edge homomorphism identities for every group element and weighted unitarity for all 120 elements.
3. Check character orthogonality and all matrix-coefficient Schur identities.
4. Check all 36 unordered projector pairs, both multiplication orders, and generator commutation for every degree (0\le m\le13).
5. Exhaustively check (E_{ij}E_{k\ell}=\delta_{jk}E_{i\ell}) for every index quadruple in each (operatorname{Sym}^m(V)), (0\le m\le7), plus the multiplicity-two test space (operatorname{Sym}^2(V)\oplus\operatorname{Sym}^{10}(V)).
6. Check that the sum of diagonal matrix units recovers the central isotypic projector.
7. Record explicitly that Molien concerns (operatorname{Sym}^m(V)), with (V) the defining two-dimensional representation.

## Reproducibility

```bash
python -m src.t045_2i_representation_certificate --max-projector-degree 13
```

The report is emitted as JSON to stdout. No passing result is claimed until this command is run locally or in CI.

## Dual convention

The T031 equivariant-section convention is (u(gq)=\rho(g)u(q)). The dual local system uses the contragredient representation (\rho^*(g)=\rho(g^{-1})^T). Since the nine characters in this repository are real, the characters of (ho) and (ho^*) agree, but this does not make the two coefficient conventions interchangeable without changing the associated-bundle convention. T045 records this distinction; it does not identify the underlying representations by an unproved basis-level equality.

## Classification

- **Exact finite identities already implemented in T034:** group and representation construction, generator-edge homomorphism proof, weighted unitarity, character orthogonality, matrix-coefficient Schur orthogonality, rational-function Molien numerator identity.
- **Exact finite identities added as exhaustive obligations in T045:** all projector pair checks through the selected degree range and all matrix-unit multiplication quadruples on the stated finite test spaces.
- **Independent construction in T036:** explicit symmetric-power models and invariant Gram matrices; execution status must be taken from CI, not inferred from the source file.
- **Not claimed:** all-degree analytic continuation, separate zeta determinants, Mosco convergence, or a Q6/PRISM-to-Rumin continuum limit.
