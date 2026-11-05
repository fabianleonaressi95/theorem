# T028 — End-to-end closure audit for the nine \(2I\)-twisted Rumin torsions

**Status:** integration audit. It cross-checks the independently developed McKay/Molien, eventual-Hurwitz, and Gamma/sine calculations for all nine irreducible twists. It does not claim a new spectral theorem.

**Depends on:** T021–T027. In particular, T024 already proves the dimension-three Kitaoka/Rumin–Seshadri operator and torsion-convention match under the common contact metric and unitary-flat hypotheses stated there. T028 does not reopen that result.

## 1. Objective

The previous results establish distinct pieces:

- T021 gives the nine Molien covariant series, the paired Rumin zeta combination, its correction term, and the torsion values.
- T022 separates finite initial segments from eventual period-60 Hurwitz tails and evaluates the corresponding Gamma expression.
- T023 reduces the nine Gamma products exactly by recurrence and reflection to algebraic values (with the trivial twist's contact-volume factor).
- T026 independently generates all nine multiplicities from the affine-\(E_8\) McKay recurrence.
- T027 identifies the McKay multiplicities with the Molien coefficients degree by degree.
- T024 establishes the 3D operator/sign/determinant-line convention comparison with Rumin–Seshadri, subject to its stated hypotheses.

The remaining risk is an integration error between the nine independently represented multiplicity and regularization pipelines. T028 makes those interfaces executable acceptance tests.

## 2. Three-stage audit

The companion script audits/t028_nine_twist_torsion_closure.py imports the existing T022, T023 and T027 audits and checks:

### Stage A — representation multiplicities

For each of the nine irreducibles, compare the affine-\(E_8\) recurrence with the Molien coefficient sequence through degree \(M\). The label map is fixed as follows:

| T026 McKay node | T021–T023 label | Dimension |
|---|---|---:|
| \(1\) | \(1\) | 1 |
| \(2_s\) | \(2\) | 2 |
| \(3\) | \(3\) | 3 |
| \(4_s\) | \(4'\) | 4 |
| \(5\) | \(5\) | 5 |
| \(6_s\) | \(6\) | 6 |
| \(4\) | \(4\) | 4 |
| \(2'_s\) | \(2'\) | 2 |
| \(3'\) | \(3'\) | 3 |

The default \(M=240\) checks \(9(241)=2169\) exact coefficient equalities. T027 also checks the weighted dimension identity and central parity.

### Stage B — eventual-period decomposition

For every twist \(\rho\), independently invoke the T022 and T023 constructions and compare:

1. the exact polynomial \(P_\rho(t)=(1-t^{60})D_\rho(t)\);
2. every finite preperiod coefficient;
3. every eventual residue-class tail start and coefficient.

The polynomial and all finite/tail data must agree exactly in SymPy's rational domain. A disagreement aborts the audit.

### Stage C — analytic continuation and exact Gamma reduction

T023's exact audit must complete all nine Gamma-reflection/sine reductions. T022 independently evaluates the uncollapsed Hurwitz/Gamma expression. T028 compares the resulting values at the requested precision, with a residual threshold of \(10^{-\lfloor P/2\rfloor}\).

The comparison uses two routes:
- exact rational-angle Gamma recurrence/reflection to the algebraic benchmark;
- finite Hurwitz/Gamma expression with its period-60 scaling.

The script also checks that the value printed by T022 agrees with a direct evaluation of its own log-Gamma expression.

## 3. Reproducibility

From the repository root:

    python audits/t028_nine_twist_torsion_closure.py --max-degree 240 --precision 60 --json

Requirements: Python 3 and SymPy, already required by T022 and T023.

Expected acceptance conditions:

- 2,169 McKay/Molien coefficient equalities pass;
- all nine T022/T023 polynomial, finite-part, and tail decompositions agree exactly;
- all nine exact Gamma/sine reductions pass;
- all nine Hurwitz/Gamma values agree with those exact values at the chosen precision;
- the squared dimensions of the nine irreducibles sum to 120.

The report contains per-twist exact values, numerical values, residuals, period-polynomial degrees, and tail counts.

## 4. Interpretation and limits

This is an end-to-end consistency audit of the existing derivations. It is stronger than comparing only final decimal torsion values because it checks the intermediate polynomial and tail data where period shifts and finite corrections can be lost.

It does not replace the proofs in T021–T027, nor does it independently derive the contact spectrum from a new matrix discretization. The generic and exceptional spectral families remain those derived from Kitaoka and recorded in T021/T025. The trivial representation's non-acyclic determinant-line normalization and contact-volume factor remain the separate T021 treatment.

No claim is made about higher-dimensional contact manifolds, where Kitaoka's rescaling is not identically one. No inference to Q6, PRISM, Yang–Mills, or a physical model follows from this analytic-torsion audit.

## 5. Status ledger

| Item | Status after T028 |
|---|---|
| 3D Kitaoka/Rumin–Seshadri operator and torsion convention | Proved in T024 under stated hypotheses |
| Nine \(2I\) irreducible multiplicity sequences | Exact McKay recurrence; cross-checked against Molien |
| Generic middle-degree singular-value blocks | Exact reduction of Kitaoka Case V in T025 |
| Exceptional boundary families | Kept separate as in T025/T021 |
| Period-60 Hurwitz continuation | Exact construction in T021/T022 |
| Nine Gamma/sine reductions | Exact symbolic identities in T023 |
| Cross-consistency of all stages | Executable acceptance audit in T028 |
| Explicit unnormalized geometric differential matrices in one global harmonic basis | Still open; not needed to claim the T024 convention theorem |
| Higher-dimensional operator comparison | Open and outside this theorem |
| New spectral theorem | Not claimed |

## References

1. A. Kitaoka, *Analytic torsions associated with the Rumin complex on contact spheres*, Int. J. Math. 31 (2020), 2050112, arXiv:1911.03092.
2. M. Rumin and N. Seshadri, *Analytic torsions on contact manifolds*, Ann. Inst. Fourier 62 (2012), 727–782, DOI: 10.5802/aif.2693.
3. T021–T027, repository theorems and companion audits.
