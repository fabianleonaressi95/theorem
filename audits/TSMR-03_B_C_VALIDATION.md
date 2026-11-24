# TSMR-03 — Vesica geometry (B) and discrete refinement (C)

**Status:** executable finite-model tests; no claim that the vesica is fractal.  
**Dependencies:** Python standard library only.

## B — Geometric vesicae

Implementation: `audits/tsmr03_vesica_geometry.py`. Tests:
`tests/test_tsmr03_vesica_geometry.py`.

- The circular vesica is the intersection lens of two equal disks with
  radius (r>0) and centre separation (0<d<2r).
- Its boundary is sampled as the two inward-facing circular arcs.
- An elliptic vesica is obtained by an invertible affine map
  (R(\theta)\operatorname{diag}(a,b)), with (a,b>0).
- Bivesica and trivesica are explicitly defined as unions of translated
  vesica boundaries; this is a chosen test geometry, not a universal
  definition of those terms.
- Box-count slopes are reported only as finite-scale estimates. A smooth
  vesica boundary is expected to have asymptotic box dimension 1; the
  numerical test uses a broad tolerance and does not establish fractality.

## C — Discrete refinement

Implementation: `audits/tsmr03_discrete_refinement.py`. Tests:
`tests/test_tsmr03_discrete_refinement.py`.

- Use the 1-dimensional simplicial complex given by a cycle (C_n).
- Build its oriented boundary matrix (B_1) and compute its rank exactly
  over rational numbers.
- Verify (eta_0=1), (eta_1=1) under edge subdivision (C_n\to C_{2n}).
- Compute the graph Laplacian spectrum (2-2\cos(2\pi j/n)).
- Prolong vertex data by piecewise-linear interpolation and compare the
  first spectral gap after the expected (h^{-2}) rescaling.

## Scope and limitations

These tests provide a minimal, exact homological model and a controlled
spectral-refinement experiment. They do **not** yet test the user's full
Q6/PRISM complexes, higher-dimensional cellular boundary maps, nontrivial
torsion, or a physical transport law. Those require importing the actual
complexes and defining their refinement maps. No inference about a
Gödelian fixed point or physical fractality follows from these tests.

## Run

```bash
python -m unittest tests.test_tsmr02_chaos_game tests.test_tsmr03_vesica_geometry tests.test_tsmr03_discrete_refinement -v
```
