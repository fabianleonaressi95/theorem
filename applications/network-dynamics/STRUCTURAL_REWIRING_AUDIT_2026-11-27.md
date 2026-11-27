# Structural rewiring-intensity audit — 2026-11-27

## Status

**Classification:** numerical verification of a synthetic computational experiment.  
**Not:** an empirical organizational result, a theorem, or evidence that one organizational architecture is generally superior.

Source workflow: [Network Dynamics run #46](https://github.com/fabianleonaressi95/theorem/actions/runs/46019035009)  
Commit: `446cc8313a1b954ac4e8e174c0eb97204427e105`  
Artifact: `network-dynamics-synthetic-results` (236,286 bytes; SHA-256 `5704ecb6e44053b102b2df7f719fbe6b4667c3c7820ea93ff692c0744cb5dc6f`).

The workflow completed successfully. The artifact contains 126 aggregate rows: 3 architectures × 6 swap intensities × 7 metrics. Every cell contains 20 finite replicates. The reported mean accepted-swap fraction is 1.0 at every intensity, and the degree sequence check is true in every row.

## Experimental design

For each replicate:

- Generate 30 synthetic agents with 8 binary competence profiles; each agent initially has 2 or 3 skills.
- Generate three simple undirected graphs with exactly 45 edges: `hierarchical`, `matrix`, and `practices_like`.
- For each architecture and intensity, start from that replicate's original graph independently.
- Apply valid double-edge swaps. The requested number of accepted swaps is `swaps_per_edge × 45`, with intensities 0, 1, 5, 20, 50 and 100.
- Reject swaps that would create loops, duplicate edges, or invalid endpoint pairings.

Thus intensity 100 requests 4,500 accepted double-edge swaps per graph. The algorithm has a finite attempt cap; the observed accepted fraction was 1.0 for all 20 replicates and all tested conditions.

The rewiring preserves node degrees and edge count, but it does **not** preserve connected components, clustering, modularity, path lengths, or competence similarity. Each intensity uses a separate deterministic random stream; all intensities within a replicate share the same starting profile and original graph.

## Main results

Values below are replicate means at intensity 0 (original graph) and intensity 100 (4,500 accepted swaps). The delta is 100 minus 0.

| Architecture | Metric | Original (0) | Rewired (100) | Delta |
|---|---|---:|---:|---:|
| hierarchical | largest-component fraction | 1.0000 | 0.9933 | −0.0067 |
| hierarchical | local clustering | 0.0554 | 0.0827 | +0.0273 |
| hierarchical | greedy modularity | 0.1406 | 0.1491 | +0.0085 |
| hierarchical | competence Jaccard on edges | 0.2037 | 0.2155 | +0.0118 |
| hierarchical | mean path in largest component | 3.0607 | 3.1261 | +0.0654 |
| matrix | largest-component fraction | 0.9350 | 0.9383 | +0.0033 |
| matrix | local clustering | 0.0466 | 0.0910 | +0.0444 |
| matrix | greedy modularity | 0.1120 | 0.1168 | +0.0048 |
| matrix | competence Jaccard on edges | 0.0000 | 0.1972 | +0.1972 |
| matrix | mean path in largest component | 2.8399 | 2.8652 | +0.0253 |
| practices_like | largest-component fraction | 0.8717 | 0.9050 | +0.0333 |
| practices_like | local clustering | 0.3354 | 0.1079 | −0.2275 |
| practices_like | greedy modularity | 0.1432 | 0.1052 | −0.0380 |
| practices_like | competence Jaccard on edges | 0.6089 | 0.2674 | −0.3415 |
| practices_like | mean path in largest component | 3.2181 | 2.7729 | −0.4452 |

### Interpretation

1. **The Practices-like graph is the most sensitive to endpoint randomization in profile-related structure.** Its mean edge-level competence Jaccard falls from 0.609 to 0.267 (about a 56% reduction relative to its starting value), and mean local clustering falls from 0.335 to 0.108 (about a 68% reduction). Greedy modularity also decreases.
2. **The matrix graph begins with zero edge-level competence overlap by construction.** Its edge-level Jaccard rises to about 0.197 after randomization. This is not a paradox: the matrix generator preferentially links complementary profiles, so removing that selection rule allows ordinary overlaps to appear.
3. **The hierarchical graph is comparatively stable on these summaries.** Its largest component remains above 0.993 at the highest intensity; modularity changes only modestly. Its local clustering and mean path length do change, so the degree sequence is not a complete description of its structure.
4. **Degree variance is unchanged within each architecture across all intensities**, as required by the degree-preserving swap operation. The three architectures have different degree variances to begin with; the sweep does not equalize their degree sequences.

The improvement in largest-component fraction for the Practices-like graph after rewiring does not imply improved knowledge transfer or organizational performance. It is a graph-connectivity diagnostic only.

## Metric definitions and limitations

- `largest_component_fraction`: size of the largest connected component divided by 30.
- `degree_variance`: population variance of node degrees.
- `mean_local_clustering`: mean local clustering coefficient, assigning zero to nodes of degree below 2.
- `greedy_modularity`: output of the custom greedy positive-merge heuristic in `structural_sweep.py`; it is not guaranteed to find globally optimal modularity.
- `degree_assortativity`: Pearson correlation of endpoint degrees across edges.
- `mean_edge_competence_jaccard`: mean Jaccard similarity between the sets of active (positive) skills of the two endpoints of each edge.
- `largest_component_average_path`: mean shortest-path distance over ordered reachable pairs within the largest connected component; disconnected components outside it are excluded.

The reported `ci95_normal_lower/upper` values are normal-approximation intervals computed from the 20 replicate values for each individual cell. They are descriptive summaries, not empirical confidence intervals. They are not paired intervals for differences between intensities, are not adjusted for multiple comparisons, and can extend outside a metric's mathematical range (for example, a component fraction upper bound slightly above 1). Do not use overlap/non-overlap of these marginal intervals as a formal test of differences.

The algorithm's accepted-swap fraction confirms that the requested swaps were completed, but it does not prove that the resulting graphs are independent uniform samples from the degree-constrained graph ensemble or that the Markov chain has mixed. The intensity sweep is therefore a controlled perturbation experiment, not a proof of complete randomization.

## Reproduction

From the repository root:

```bash
python applications/network-dynamics/src/structural_sweep.py \
  --replicates 20 \
  --seed 20261119 \
  --intensities 0 1 5 20 50 100 \
  --output applications/network-dynamics/results/structural-sweep
```

The CI workflow runs the same command and uploads both CSV and JSON aggregates in the `network-dynamics-synthetic-results` artifact.

## Evidence boundary and next tests

**Supported:** in this specified synthetic setup, degree-preserving endpoint swaps leave degree sequences fixed but can substantially alter clustering, modularity, path lengths, component structure, and edge-level competence similarity. The magnitude and direction depend strongly on the starting architecture.

**Not supported:** conclusions about actual self-managed organizations, the historical Practices model, real-world learning outcomes, causal organizational superiority, or an RGS-specific advantage.

Next computational checks:

1. Retain per-replicate outputs and compute paired replicate-level differences with paired bootstrap or permutation intervals.
2. Add multiple independent rewiring chains per original graph and diagnostics for mixing / convergence of graph statistics.
3. Compare against degree-constrained null ensembles while explicitly reporting which graph invariants are preserved.
4. Keep graph-connectivity robustness separate from task-based competence resilience and knowledge-state dynamics.
