# TSMR-C — Numerical audit protocol

**Purpose:** provide reproducible finite-resolution diagnostics for cumulative coordinates. These tests do not prove singularity, strict increase of the limiting golden CDF, or a dynamical conjugacy.

## Exact control cases

1. For the symmetric Bernoulli convolution at \(\lambda=1/2\), the law is uniform on \([-2,2]\), so \(F(x)=(x+2)/4\) on that interval.
2. For the golden parameter \(\lambda=\varphi^{-1}\), verify the exact algebraic identities \(\lambda^2=1-\lambda\), \(1/(1-\lambda)=\varphi^2\), and the support endpoints.
3. Approximate the golden distribution by its depth-\(n\) discrete convolution. Record that finite approximants are atomic step functions; they cannot establish the regularity of the limiting CDF.
4. Check the probability-integral-transform identity on an explicitly finite non-atomic toy distribution only at the level of its quantile construction; do not infer a physical model.

## Interpretation

A finite histogram, finite Fourier product, or finite-depth sample can diagnose scaling and numerical stability. None can prove that the limiting measure is singular. The theorem-level argument for singularity must remain separate from numerical evidence. The proposed golden Markov partition and transfer matrices are intentionally excluded from the test suite until their interval transitions are derived and proved.
