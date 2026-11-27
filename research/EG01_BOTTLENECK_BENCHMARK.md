# EG-01 benchmark: a one-edge bottleneck

**Classification:** analytic/numerical counterexample to a weakened hypothesis set. It is not a counterexample satisfying all of Matthias's assumptions.

## Construction

Take the square grid with n by n vertices in [0,1]^2 and mesh epsilon=1/n. Compare the full nearest-neighbour grid with the graph obtained by deleting all edges crossing the central vertical cut except one edge at the central height. Both have identical uniformly separated and relatively dense vertices; every retained edge has length epsilon and conductance one. The second graph remains connected through a single bridge.

Use E_epsilon(v) = (1/2) sum_edges (v(y)-v(x))^2 in dimension two. The Voronoi L2 mass is epsilon^2 sum_vertices |v|^2.

## Numerical spectral-gap diagnostic

The reported scaled gap is lambda_1(L_graph)/epsilon^2, i.e. the Rayleigh gap relative to Voronoi L2 mass.

| n | Full grid scaled gap | Single-bridge scaled gap | Full-grid cut edges | Bridge cut edges | Bridge step energy |
|---:|---:|---:|---:|---:|---:|
| 8 | 9.7434 | 1.9242 | 8 | 1 | 0.5 |
| 12 | 9.8134 | 1.7263 | 12 | 1 | 0.5 |
| 16 | 9.8379 | 1.6047 | 16 | 1 | 0.5 |
| 24 | 9.8555 | 1.4575 | 24 | 1 | 0.5 |
| 32 | 9.8617 | 1.3676 | 32 | 1 | 0.5 |
| 40 | 9.8645 | 1.3050 | 40 | 1 | 0.5 |

The full-grid scaled gap stabilizes near 9.87. The bridge graph's scaled gap decreases substantially on the tested range; these finite-size data do not establish its asymptotic rate.

More decisively, set v=0 on the left half and v=1 on the right half. Exactly one edge crosses the cut, so E_epsilon(v)=1/2 for every n. The Voronoi embeddings converge strongly in L2 to a jump function, which is not in H1((0,1)^2). Consequently, there cannot be a uniform estimate controlling the H1 seminorm of an L2-consistent H1 interpolant by this graph energy. Otherwise a bounded H1 sequence would have a weak H1 limit equal to the jump function.

## Why this does not refute Matthias's full assumptions

The single-bridge graph violates the approximate-geodesic path-tube condition (G5). Choose endpoints on opposite sides at height approximately 1/4. Every graph path must cross the sole bridge at height approximately 1/2, so the path leaves the straight segment by a macroscopic distance, not O(epsilon).

This demonstrates why ordinary connectivity is insufficient. It does **not** show that (G1)-(G5) are insufficient.

## Next mathematical tests

1. Determine whether (G1)-(G5), with precise boundary coverage and uniform constants, imply a uniform discrete Poincare inequality and H1-type compactness.
2. Quantify path length and edge congestion rather than assuming path existence is enough.
3. Test graph families satisfying (G5) but with nonuniform directional distributions.
4. If necessary, add a uniform local directional coercivity or discrete Poincare hypothesis.
5. Specify boundary coverage: an interior fill-distance condition alone does not provide a boundary extension theorem.

## Reproducibility

Run: python research/benchmarks/eg01_bottleneck.py

Requires NumPy and SciPy. The script writes eg01_bottleneck_results.csv and computes spectral gaps and step energies. Numerical evidence is diagnostic; the L2-limit obstruction above is analytic.

## Conclusion

**EG-01 remains open for the full (G1)-(G5) class.** This benchmark rigorously identifies a failure mode when approximate-geodesic connectivity is removed. It does not justify claiming that Matthias's assumptions fail. The next task is to determine whether (G5), together with separation and fill distance, rules out this bottleneck and yields uniform coercivity.
