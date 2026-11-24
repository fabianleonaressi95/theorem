# TSMR-02 — Chaos-game and anisotropic IFS validation

**Status:** computational test specification and reproducible implementation.  
**Source method:** [Chaos Game, section 3.2](https://chaosgame.drwhy.ai/chaos-game-1.html).

## Scope

This audit turns the chaos-game construction into executable checks for:

1. the Sierpiński triangle IFS;
2. the Barnsley fern with probabilities `1%, 79%, 10%, 10%` shown in the source page;
3. a two-map anisotropic affine IFS with singular values `1/2` and `1/4`;
4. exact pressure in the common-diagonal special case;
5. finite-depth pressure as a numerical diagnostic.

Implementation: `audits/tsmr02_chaos_game.py`. Regression tests:
`tests/test_tsmr02_chaos_game.py`. The code uses only the Python standard library.

## Mathematical contract

Each affine map has the form

`f_i(x)=A_i x+b_i`.

The validator computes the largest singular value of each `A_i` and requires
`sigma_max(A_i) < 1`, sufficient for strict contraction in the Euclidean
norm. Sampling probabilities are strictly positive and sum to one. Positivity
ensures that every map in the finite IFS is sampled with nonzero probability.

The chaos game chooses map `i` with probability `p_i`, then applies it to
the current point. For a finite family of contractions, the associated IFS
has a unique compact attractor. Under positive sampling probabilities, the
random orbit samples the attractor in the standard IFS setting; a finite
point cloud is only a numerical approximation.

## Test cases and acceptance criteria

| Test | Acceptance criterion |
|---|---|
| Sierpiński triangle | 30,000 retained points; all lie in the closed generating triangle |
| Reproducibility | Same seed produces exactly the same points and map counts |
| Barnsley fern | 50,000 retained points; empirical map frequencies within 0.012 of source probabilities; all points finite and vertically bounded |
| Anisotropic IFS | Singular values equal `0.5` and `0.25` within floating-point tolerance; sampled points finite |
| Exact pressure | For two maps sharing `diag(1/2,1/4)`, (P(s)=\log 2+\log(1/2)+(s-1)\log(1/4)) on (1\le s\le2), with root (s=1) |
| Finite-depth pressure | Depth-8 computation agrees with the exact common-diagonal pressure in the tested case |
| Invalid inputs | Reject probabilities not summing to one and maps that are not strict contractions |

## Interpretation limits

- A chaos-game point cloud is not proof that an arbitrary physical geometry is fractal.
- The common-diagonal pressure formula is exact only for the stated special case.
- `finite_depth_pressure` is a finite-depth diagnostic, not by itself a certificate for limiting pressure.
- Affinity dimension is an upper bound for Hausdorff dimension in the general affine setting. Equality requires additional hypotheses and must not be presumed.
- No vesica/elliptic-vesica fractality is asserted by these tests. A separate geometric model must specify its maps, domain, overlap conditions, and observables before it can be tested.

## Run locally

```bash
python -m unittest tests.test_tsmr02_chaos_game -v
```

The test suite follows the repository's existing `unittest` convention.
