# Network Dynamics — topology-only control audit

**Date:** 2026-11-26  
**Workflow:** [Network Dynamics run 45868636969](https://github.com/fabianleonaressi95/theorem/actions/runs/45868636969)  
**Artifact:** `network-dynamics-synthetic-results` (100 paired replicates)

## Design

For each replicate the audit generates one shared set of 30 synthetic agents, 8 competence dimensions, profiles and initial states. Each graph has exactly 45 undirected edges. It compares:

1. the original profile-informed hierarchical, matrix and Practices-like graphs;
2. a degree-preserving double-edge-swap rewire of each original graph;
3. a profile-blind uniform (G(n,m)) graph with the same node and edge counts.

Each degree-preserving rewire preserves the original graph's complete degree sequence and edge count. The rewiring randomizes endpoint pairings; it does not preserve clustering, community structure, path lengths or connected-component structure. It is therefore a control for degree sequence, not a claim that every other graph statistic is held fixed.

All knowledge simulations use the same profiles, initial state and update parameters within each replicate ((eta=0.22,ho=0.008,160) steps). Random node-removal tests use common random streams. Targeted removal removes the 20% highest-degree nodes in one static attack step.

## Results: original graphs versus degree-preserving rewires

Means over 100 paired replicates. The paired difference is **rewired minus original**; intervals are normal-approximation 95% intervals over the paired replicate differences.

| Architecture | Metric | Original | Rewired | Paired difference (95% interval) |
|---|---|---:|---:|---:|
| Hierarchical | Random-removal component | 0.9543 | 0.9492 | −0.0052 [−0.0091, −0.0013] |
| Hierarchical | Targeted-removal component | 0.8392 | 0.7658 | −0.0733 [−0.1083, −0.0384] |
| Hierarchical | Mean knowledge | 0.2578 | 0.2578 | −0.000002 [−0.000067, 0.000063] |
| Hierarchical | Skill coverage >0.60 | 0.0000 | 0.0002 | +0.0002 [−0.0002, 0.0005] |
| Hierarchical | Within-skill dispersion | 0.0320 | 0.0343 | +0.0023 [+0.0008, +0.0038] |
| Matrix | Random-removal component | 0.8839 | 0.8826 | −0.0014 [−0.0071, +0.0044] |
| Matrix | Targeted-removal component | 0.4988 | 0.5071 | +0.0083 [−0.0300, +0.0467] |
| Matrix | Mean knowledge | 0.2486 | 0.2487 | +0.00014 [−0.00003, +0.00032] |
| Matrix | Skill coverage >0.60 | 0.0170 | 0.0179 | +0.0009 [+0.0002, +0.0016] |
| Matrix | Within-skill dispersion | 0.0754 | 0.0824 | +0.0069 [+0.0047, +0.0092] |
| Practices-like | Random-removal component | 0.7345 | 0.8342 | +0.0997 [+0.0832, +0.1162] |
| Practices-like | Targeted-removal component | 0.3600 | 0.4688 | +0.1088 [+0.0772, +0.1403] |
| Practices-like | Mean knowledge | 0.2718 | 0.2730 | +0.0012 [+0.0007, +0.0017] |
| Practices-like | Skill coverage >0.60 | 0.0675 | 0.0355 | −0.0321 [−0.0402, −0.0240] |
| Practices-like | Within-skill dispersion | 0.1717 | 0.1217 | −0.0501 [−0.0577, −0.0424] |

## Profile-blind reference

The profile-blind (G(n,m)) reference gives:

| Metric | Mean |
|---|---:|
| Random-removal largest component | 0.8954 |
| Targeted-removal largest component | 0.5913 |
| Mean knowledge | 0.2576 |
| Skill coverage >0.60 | 0.0116 |
| Within-skill dispersion | 0.0729 |

The (G(n,m)) reference is not degree matched; it is a profile-independent edge baseline with fixed (n) and (m).

## Interpretation

1. **Practices-like edge selection has a strong structural signature in this model.** When its edges are randomized while preserving every node's degree, random-removal connectivity rises by about 0.100 and targeted-removal connectivity by about 0.109. At the same time, coverage above 0.60 falls by about 0.032 and within-skill dispersion falls by about 0.050. This is consistent with the original shared-competence edge rule producing stronger competence-aligned clustering: it helps the selected knowledge metrics but creates a more fragile global graph.
2. **The hierarchical graph's degree sequence alone does not explain its targeted robustness.** Rewiring while preserving degrees lowers the retained component by about 0.073 under the static targeted attack. The original arrangement of edges matters beyond the degree sequence.
3. **The matrix result is more modest.** Its degree-preserving rewire has no clearly resolved change in random or targeted connectivity under these intervals, while dispersion increases slightly.
4. **Mean knowledge is comparatively insensitive to rewiring** for all three architectures at this particular update setting. Coverage and dispersion are more topology-sensitive.
5. The profile-blind random graph is a useful reference but is not a degree-sequence-matched null. Do not interpret differences from it as a pure topology effect.

## Limitations

- Synthetic agents and competence profiles; no real organizational dataset or empirical calibration.
- Normal-approximation intervals are descriptive, unadjusted for multiple metrics/comparisons.
- Double-edge swaps randomize the graph conditional on degree sequence, but 20 accepted swaps per edge do not prove complete mixing of the graph ensemble.
- Static highest-degree removal is a simplified attack model.
- The threshold 0.60 is near-degenerate for the hierarchical architecture at these parameters; continuous metrics should be reported alongside it.

## Research conclusion

This experiment supports a **model-internal** conclusion: graph organization beyond the degree sequence materially changes robustness and competence-diffusion metrics. In the Practices-like construction, the profile-informed placement of edges trades global connectivity for higher threshold coverage and greater within-skill dispersion. In the hierarchical construction, the original edge arrangement contributes to targeted robustness beyond degree sequence.

It does **not** establish that any real organizational design has these properties. The next valid step is a controlled sweep over rewiring intensity (including multiple independent rewires per original graph) and graph statistics such as clustering, modularity, assortativity and path length, followed by validation against empirical network data.
