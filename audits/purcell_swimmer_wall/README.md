# Purcell swimmer near a wall — reproducibility audit

This directory contains a **first-pass independent reconstruction**, not a validated reproduction.

## Run

Dependencies: Python 3.10+, NumPy, SciPy.

```bash
python benchmark.py --amplitude 1e-3 --order 64
```

The script builds the generalized resistance matrix by Gauss–Legendre quadrature of
\(J^T D J\), with \(D=C_\perp(I-ee^T/2)\), and integrates the four-stage
shape-velocity gait using DOP853.  The geometric parameters match the example
reported in the article: unit link lengths, initial wall distance \(10^{-2}\),
and link radius \(10^{-4}\).

## Current result

At amplitude \(10^{-3}\), quadrature orders 16, 32, 48, 64 and 96 all give
\(\Delta x/\xi^2\approx0.0370356\).  The article reports a limiting value
\(0.0617\) (\(5/81\)) for the same aligned, equal-link example.

This is a **failed reproduction**, not evidence against the paper.  The next audit
must compare every generalized-force term and the sign convention for the two
hinge coordinates with equations (7)–(13) of the article.  No Q6 coupling is
introduced until this continuous benchmark is reconciled.

Primary source:
Micalizio et al. (2026), DOI 10.1007/s11012-026-02136-0,
https://link.springer.com/article/10.1007/s11012-026-02136-0
