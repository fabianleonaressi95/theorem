# GitHub Actions validation register — 12 November 2026

Repository: fabianleonaressi95/theorem

This report records completed CI executions. The statuses below refer to finite graph/model/software checks only. They do not constitute experimental validation, material calibration, or a proof of any physical interpretation beyond the stated theorem hypotheses.

| Record | Run | Result | Evidence |
|---|---:|---|---|
| T103/T104 | [#43245722504](https://github.com/fabianleonaressi95/theorem/actions/runs/43245722504) | PASS | 11 tests; cycle rank 129; cocycle rank 63; H1=0; magnetic holonomy audit completed |
| T105 | [#43245721916](https://github.com/fabianleonaressi95/theorem/actions/runs/43245721916) | PASS | 8 tests; deterministic audit PASS |
| T107 | [#43245722241](https://github.com/fabianleonaressi95/theorem/actions/runs/43245722241) | PASS | 5 tests; deterministic audit PASS; Gray graph isomorphism true |
| T131/T132 | [#43245274034](https://github.com/fabianleonaressi95/theorem/actions/runs/43245274034) | PASS | Python module compilation; 11 tests |

## Failure triage

The four earlier failed runs on 12 November were diagnosed from their logs:

- T103 and T107: import-path configuration (ModuleNotFoundError: scripts) on earlier commits.
- T105: the test runner was not installed in the environment on earlier PR commits (No module named pytest).

The maintenance PR sets repository-root PYTHONPATH for T103/T107 and installs NumPy plus pytest for T105. The corrected PR-triggered runs listed above all pass. Historical failed runs remain in GitHub's audit history and are not erased or reclassified.

## Scope

A green workflow certifies only the executed assertions and tests. It does not certify a physical realization, a continuum limit, experimental agreement, or material transport coefficients unless those are independently included in the audit and supported by data.
