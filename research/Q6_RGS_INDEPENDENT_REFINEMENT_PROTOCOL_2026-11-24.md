# Q6–RGS independent refinement: admissibility audit and test protocol

**Date:** 24 November 2026  
**Classification:** methodological audit / open verification  
**Status:** BLOCKED — no independent refined RGS operator is currently certified in the repository

## 1. Question

Do the coefficients
\[
a=\frac12,\qquad b=\frac1{120},\qquad c=\frac1{240}
\]
persist under an independently constructed spectral refinement, rather than merely interpolate the three selected pairs
\[
(0,1/2),\quad(4,3/5),\quad(6,7/10)?
\]

This audit distinguishes a reproducible finite-dimensional identity from evidence that the coefficients are structural invariants.

## 2. What the present data establish

The existing Q6–RGS audit reconstructs:
- the Q6 reduced Laplacian with selected spectrum \(\{0,4,6\}\);
- a three-dimensional RGS lower carrier block with eigenvalues \(\{1/2,3/5,7/10\}\);
- the unique polynomial of degree at most two matching those three pairs;
- the upper/lower shift of \(3/10\).

Thus
\[
p(\lambda)=\frac12+\frac{\lambda}{120}+\frac{\lambda^2}{240}
\]
is a verified spectral matching identity on the selected rank-three sector. Since there are three unknown coefficients and exactly three interpolation nodes, exact agreement is guaranteed once those three pairs are fixed. It is not an out-of-sample test.

The existing numerical audit remains valid as a check of the stored arrays and the selected-sector intertwining. Its PASS status must not be interpreted as a refinement-invariance test.

## 3. Provenance and invariance blockers

The repository's provenance record states that the exact generating cell, inputs, and coordinate-basis certificate for the archived \(K_0\) remain unresolved. The numerical identities of the stored matrices are reproducible, but their geometric interpretation as a common 188D coordinate basis is not certified.

The existing Q6 embedding block audit also reports:
- the embedded 64D Q6 subspace is not invariant under \(K_0\);
- the off-diagonal coupling between that subspace and its 124D complement is nonzero in both directions;
- only the separately reconstructed geometric operator \(R_{geo,tangent}\) reduces that embedded 64D sector in the reported calculation.

The latter fact does not yet provide a replacement RGS operator for this test: the archive does not establish an independently certified basis identification linking the 188D arrays used for \(K_0\) to the geometric tangent representation.

Finally, \(T_{transport}\) is not independent evidence: the provenance audit records it as a polar transport built using \(P_G\) and the geometry frame. It cannot serve as a held-out operator.

## 4. Preregistered refinement test

A future refinement is admissible only if all the following are supplied before coefficient fitting.

### 4.1 Independent inputs

1. A refined graph/complex and its combinatorial or discretized Laplacian \(L_h\), constructed without using the target coefficients.
2. An independently assembled RGS operator \(K_h\), with its energy/Hessian definition, input geometry, and generation script archived.
3. An explicit basis map or isometry \(U_h\) between the compared spaces, including dimensions, normalization, and coordinate provenance.
4. A proof or numerical certificate for the relevant invariant subspace. Report leakage
\[
\|(I-U_hU_h^T)K_hU_h\|_F
\]
and the corresponding Laplacian leakage.
5. A refinement relation between at least two levels (restriction/prolongation or a documented mesh map), fixed before examining fitted coefficients.

### 4.2 Fit and held-out validation

- Use at least three distinct spectral nodes to estimate a degree-two polynomial.
- Reserve at least one additional distinct spectral node, not used in fitting, as a held-out test.
- Preferably repeat at two or more refinement levels and report coefficient drift, spectral residuals, invariant-subspace leakage, and numerical uncertainty.
- Do not force degree two. Compare the minimal polynomial degree and residual against constant, linear, quadratic, and higher-degree alternatives using a predeclared criterion.
- Rational recognition is diagnostic only; report raw floating coefficients and condition numbers.

A positive result requires the same coefficients (within a tolerance justified by conditioning and discretization error) to predict the held-out spectral values and remain stable across independent refinement levels. If only three nodes are available at each level, the result remains interpolation at every level, not held-out validation.

## 5. Required report fields

For each level \(h\), archive:
- source hashes and generation commands for \(L_h,K_h,U_h\);
- dimensions and ranks;
- spectra and node-pairing rule fixed independently of the fit;
- invariant-subspace leakage;
- fitted coefficients and fit residual;
- held-out nodes, predictions, and residuals;
- coefficient drift across levels;
- condition numbers and uncertainty/tolerance;
- failed checks as well as passed checks.

## 6. Current verdict

**BLOCKED / OPEN.** The repository currently contains no certified independent refined RGS operator and no held-out spectral pair for this coefficient test. The present coefficients remain a verified degree-at-most-two interpolation / selected-sector functional-calculus identity, not established invariants of Q6–RGS.

No new refinement data, physical law, or successful refinement test are claimed by this audit.
