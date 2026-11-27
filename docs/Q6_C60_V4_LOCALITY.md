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
