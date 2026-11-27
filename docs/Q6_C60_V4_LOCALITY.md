# Q6–C60 V4: face-adjacency locality diagnostic

**Classification:** numerical diagnostic for one explicit V4 intertwiner. This is not a no-go theorem for all V4-equivariant intertwiners.

## Question

The previous audit constructs an orthogonal map
\[
\Phi:\mathbb R^{64}_{Q6}\longrightarrow
\bigoplus_{f=1}^{32} E_f,
\qquad E_f=n_f^\perp,
\]
intertwining the two restricted V4 representations. We now ask whether the transported Q6 adjacency
\[
D_{C60}=\Phi A_{Q6}\Phi^{T}
\]
is local with respect to the adjacency graph of the 32 actual truncated-icosahedron faces.

The face graph is reconstructed geometrically from the truncated icosahedron: two faces are adjacent when their polygons share an edge. Its inventory must be 12 pentagons, 20 hexagons, 90 shared edges, with face degrees 5 and 6 respectively.

## Diagnostic

The script `scripts/audit_q6_c60_v4_locality.py`:

1. loads the archived `Q6_adjacency` and 64-point Q6 coordinate data;
2. reconstructs the same V4 actions and projector-built intertwiner as the preceding audit;
3. reconstructs the 32 C60 faces and their edge-sharing adjacency;
4. transports the Q6 adjacency to the 64D face-fibre space;
5. partitions the transported matrix into 32×32 blocks of size 2×2;
6. reports nonzero block support and Frobenius energy on adjacent versus nonadjacent face pairs, over several numerical thresholds.

Reproduce with:

```bash
python scripts/audit_q6_c60_v4_locality.py data/RGS_PSU_all_matrices.npz \
  --out audits/Q6_C60_V4_locality.json \
  --matrices artifacts/Q6_C60_V4_locality.npz
```

The GitHub Actions workflow runs this diagnostic alongside the V4 representation audit and uploads the JSON and matrix bundle.

## Critical limitation: intertwiner nonuniqueness

Each of the four real V4-isotypic sectors has multiplicity 16. Once an intertwiner is fixed, it can still be composed with an orthogonal transformation in the commutant; in this decomposition the residual freedom is of type
\[
O(16)\times O(16)\times O(16)\times O(16).
\]
The present diagnostic uses the deterministic projector/eigensolver choice from the previous audit. It does **not** minimize nonlocal blocks over this freedom.

Therefore:
- a dense transported matrix proves that this explicit intertwiner is not face-local;
- it does **not** prove that every V4 intertwiner is nonlocal;
- a sparse result would be evidence for this particular representative, not by itself a canonical geometric correspondence;
- no C60 spectral equivalence or local differential operator is asserted.

## Status

The numerical report `audits/Q6_C60_V4_locality.json` is the authoritative output of the workflow. The classification remains **numerical diagnostic / open optimization problem** until the intertwiner freedom is handled explicitly.


## Numerical result (GitHub Actions run 17)

The workflow completed successfully on 2026-11-27. The actual C60 face graph was reconstructed with 32 faces (12 pentagons and 20 hexagons), 90 shared edges, and degree counts 12 of degree 5 and 20 of degree 6.

The transported matrix is symmetric to residual `4.46e-15`. The intertwiner has orthogonality residual `8.33e-15` and maximum V4 intertwining residual `5.66e-15`.

For the deterministic projector-built intertwiner, at every tested block threshold from `1e-12` through `1e-2`:

- 944 of the 1024 possible `2x2` face blocks are nonzero;
- 24 diagonal blocks and 160 directed adjacent-face blocks are nonzero;
- 760 off-diagonal blocks connect nonadjacent faces;
- 82.61% of the off-diagonal support is therefore nonadjacent;
- only 80 of the 90 undirected face adjacencies have a nonzero transported block (88.89% coverage).

The Frobenius energy is also predominantly nonlocal: 76.73% lies in nonadjacent off-diagonal face blocks, while 23.27% lies in adjacent-face blocks.

**Conclusion for this representative:** the explicit transported Q6 adjacency is dense and not face-local with respect to the C60 face graph. This is a strong negative result for the current deterministic intertwiner, but it is not a no-go theorem: the unresolved `O(16)^4` freedom could change block locality. An optimization or a structural obstruction over the full intertwiner family is still required.

Workflow: https://github.com/fabianleonaressi95/theorem/actions/runs/46015219978  
Artifact: `q6-c60-v4-equivariance` (includes the JSON report and NPZ matrix bundle).


## 7. Optimization over the full V4 commutant

The initial deterministic intertwiner was not the end of the test. The four 16-dimensional isotypic sectors leave an `O(16)^4` freedom. The optional PyTorch script `scripts/optimize_q6_c60_v4_intertwiner_locality.py` parameterizes it as
\[
\Phi=\sum_{k=1}^4 B_{f,k}\,W_{0,k}\exp(S_k)\,B_{q,k}^{T},
\qquad S_k^T=-S_k,
\]
and runs two stages: (i) minimize nonadjacent off-diagonal face-block Frobenius energy, with eight seeded random starts; (ii) refine the block-L1 objective to suppress weak nonadjacent blocks.

Reproduction requires the two NPZ files in the GitHub Actions artifact `q6-c60-v4-equivariance` (from run 17): `Q6_C60_V4_intertwiner.npz` and `Q6_C60_V4_locality.npz`. Install PyTorch, then run:

```bash
python scripts/optimize_q6_c60_v4_intertwiner_locality.py \
  --representations artifacts/Q6_C60_V4_intertwiner.npz \
  --locality artifacts/Q6_C60_V4_locality.npz \
  --out audits/Q6_C60_V4_locality_optimization.json \
  --matrices artifacts/Q6_C60_V4_locality_optimization.npz
```

### Numerical outcome

The deterministic starting intertwiner placed 76.73% of its off-diagonal face-block Frobenius energy on nonadjacent face pairs. The quadratic stage reduced this to 1.81%; after the block-L1 refinement the final nonadjacent energy fraction was 2.10%, with 97.90% on adjacent face pairs. The nonadjacent block-L1 fraction fell from 79.96% to 9.72%.

The optimized map still satisfies the constraints numerically:
- orthogonality residual: `4.42e-14`;
- maximum V4 intertwining residual: `6.18e-15`;
- transported-matrix symmetry residual: `1.19e-14`.

At block threshold `1e-2`, all 90 undirected C60 face adjacencies are represented, while the number of nonzero 2x2 blocks falls to 368/1024; 156 off-diagonal nonadjacent blocks remain above threshold. At thresholds through `1e-6`, all 1024 blocks remain nonzero. Thus this is **near-local concentration, not exact locality**.

The optimizer is nonconvex and uses finite random restarts. The result is a numerical local optimum, not a global-optimality certificate. The exact-locality question remains open. Machine-readable values: `audits/Q6_C60_V4_locality_optimization.json`.


## Exact-locality feasibility test (2026-11-27)

The next question was whether some point in the full `O(16)^4` intertwiner family makes **every** block between distinct nonadjacent C60 faces exactly zero. The parameter space has 480 continuous degrees of freedom. The target imposes 812 directed 2x2 block-zero conditions (3248 scalar entries before accounting for symmetry redundancy).

The reproducible search is `scripts/test_q6_c60_v4_exact_locality.py`. It uses the same isotypic parameterization as the preceding optimizer, with a fixed seed and three stages: quadratic nonlocal-energy reduction, block-L1 sparsification, and a final quadratic refinement. It requires NumPy and PyTorch. Reproduce from the two NPZ inputs in the `q6-c60-v4-equivariance` Actions artifact:

```bash
python scripts/test_q6_c60_v4_exact_locality.py \
  --representations artifacts/Q6_C60_V4_intertwiner.npz \
  --locality artifacts/Q6_C60_V4_locality.npz \
  --out audits/Q6_C60_V4_exact_locality.json \
  --matrices artifacts/Q6_C60_V4_exact_locality.npz
```

### Verified numerical outcome

For seed `20261127`, the best candidate found in this finite search has:
- nonadjacent off-diagonal Frobenius energy fraction: **1.7915%**;
- adjacent off-diagonal energy fraction: **98.2085%**;
- orthogonality residual: `4.37e-14`;
- maximum V4 intertwining residual: `6.23e-15`;
- transported-operator symmetry residual: `1.25e-14`;
- exact Q6 adjacency spectrum retained: eigenvalues `-6,-4,-2,0,2,4,6` with multiplicities `1,6,15,20,15,6,1`.

At block threshold `1e-2`, all 180 directed adjacent-face blocks remain, but **620 nonadjacent blocks** are also above threshold. At thresholds through `1e-6`, all 812 nonadjacent blocks remain nonzero. Thus the search did **not** find exact locality.

### What this does and does not establish

This is a reproducible near-local candidate and a failed exact-zero search from one seeded nonconvex trajectory. The positive residual is **not** a certified lower bound: other initializations or a different method may do better. Consequently, this does not prove that exact locality is impossible. The mathematical status remains **open**; a global obstruction or an exact construction is still needed.

Machine-readable report: `audits/Q6_C60_V4_exact_locality.json`.
