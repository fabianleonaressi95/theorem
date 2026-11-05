# T036 — Explicit exact irreducible matrix models of 2I

Status: constructive exact-algebraic extraction from symmetric powers of the defining SU(2) representation. The implementation and tests are included; execution is not yet certified.

## Construction

For each irreducible label rho, select the least degree m for which the exact T021 Molien multiplicity b(m,rho) is one. The code determines these degrees from the numerator series, without hard-coding them.

On homogeneous polynomials of degree m, use the action f(v) -> f(rho_2(g)^(-1) v). The character projector is

P(rho,m) = d(rho)/120 sum over g in 2I of conjugate(chi_rho(g)) Sym^m(rho_2)(g).

At a multiplicity-one occurrence its image has dimension d(rho). An exact column basis B_rho of this image therefore gives an explicit irreducible model.

For every group element, solve

Sym^m(rho_2)(g) B_rho = B_rho R_rho(g)

using an exact nonsingular pivot-row minor. This produces matrices for all 120 elements.

## Invariant Hermitian metric

In the monomial basis X^(m-k)Y^k, the symmetric-power representation has invariant Gram matrix

W_m = diag(1/binomial(m,0), ..., 1/binomial(m,m)).

The induced metric is G_rho = B_rho^* W_m B_rho. The audit checks R_rho(g)^* G_rho R_rho(g) = G_rho for all 120 elements. The matrices need not be unitary in the arbitrary extracted basis; they are unitary with respect to this explicit positive invariant metric.

## Exact acceptance checks

For all nine irreducibles, the code checks central-projector idempotence and rank, invariance of the extracted subspace, exact recovery of all nine character values by traces, preservation of the induced Hermitian metric, and sum of squared dimensions equal to 120.

The JSON export stores exact bases, Gram matrices, all group matrices, group-element coordinates, and selected Molien degrees. Algebraic entries are serialized as exact SymPy expression strings.

## Reproducibility

Run from repository root:

```bash
python -m unittest tests.test_t036_2i_irreducible_models -v
python -m src.t036_2i_irreducible_models --output data/t036_2i_irreducible_models_exact.json
```

## Scope

T036 constructs explicit exact matrix models and invariant metrics. Together with T033, this makes the finite-group matrix-unit construction executable. The next step is to apply those matrix units to the Rumin harmonic eigenspaces and compute the Rumin-specific multiplicity bases and reduced geometric differential matrices.

No new spectral theorem, analytic torsion value, or continuum-limit claim is made.
