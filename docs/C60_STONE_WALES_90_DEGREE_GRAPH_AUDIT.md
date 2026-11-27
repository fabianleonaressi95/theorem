# C60 Stone-Wales 90° graph and covariance audit

**Status:** the repository contains the graph reconstruction, exact boundary-identity checks and the pyracylene patch regression. The recorded 2026-11-26 successful Actions run tested an earlier branch SHA, not the final merged PR #449 head. Therefore the exact merged revision still requires a fresh CI run. The chain map is not yet certified to induce an isomorphism on H₂; the new regression below tests that separately.

## Starting graph

The existing ideal truncated-icosahedron generator supplies the cage:
\[
(V,E,F;p,h)=(60,90,32;12,20),\qquad \deg(v)=3.
\]

## Exact graph operation

The audit works in the **dual triangulation**. Each vertex of the dual is a pentagonal or hexagonal face of C60; each triangular face of the dual corresponds to one carbon atom. For each dual edge joining two degree-6 vertices whose two opposite vertices both have degree 5, perform the diagonal flip
\[
(H_1,H_2)\longmapsto(P_1,P_2).
\]
This is the dual description of the pyracylene Stone–Wales move. Reconstruct the direct graph as the dual of the flipped triangulation and retain candidates only if they have 60 vertices, 90 edges, 32 faces, degree 3 at every carbon, and exactly 12 pentagons and 20 hexagons. The direct-graph operation is then recorded as its two removed and two added C–C bonds.
This is the dual description of the fullerene **pyracylene** move, conventionally denoted \\(SW_{5|6}\\). The notation labels the four-ring patch, not the ring pair sharing the rotated bond. The central direct-graph bond is a \\(6|6\\) bond shared by hexagons \\(H_1,H_2\\); the two opposite dual vertices \\(P_1,P_2\\) are pentagons. The initial patch is therefore \\(5/6/6/5\\), and the dual flip \\(H_1H_2\\to P_1P_2\\) changes it to \\(6/5/5/6\\). Reconstruct the direct graph as the dual of the flipped triangulation and retain candidates only if they have 60 vertices, 90 edges, 32 faces, degree 3 at every carbon, and exactly 12 pentagons and 20 hexagons. Record the two removed and two added C–C bonds.

This is distinct from graphenic \\(SW_{6|6}\\), whose initial patch is \\(6/6/6/6\\) and whose product contains the \\(5/7/7/5\\) defect. A criterion requiring the central direct bond itself to be 5|6 would select a different local environment, not the C60 pyracylene patch audited here.

## Chain-map construction

Vertices are identified by carbon labels, so \(S_0=I_{60}\). Each old edge is mapped to a path in the new graph, producing \(S_1\). Each mapped old face boundary is filled by an integral 2-chain in the new spherical cellulation, producing \(S_2\). The audit checks exactly
\[
B'_1S_1=S_0B_1,\qquad B'_2S_2=S_1B_2.
\]
Path and filling choices are not unique. This verifies a chain map for the chosen combinatorial correspondence, not uniqueness or an embedding-preserving isotopy.

## Geometric response proxy

With --relax, both graphs are relaxed using the same RDKit MMFF94s model and initial ideal coordinates. The script computes global and local-patch covariance tensors of the **carbon nuclear coordinates**. These are geometric descriptors only, not electron-density covariance or the De Aquino molecular overlap moment. MMFF94s is empirical molecular mechanics, not DFT or experiment.

An electronic-density vesica comparison requires a suitable electronic-structure calculation and a fixed projection/overlap convention.

## Reproduction

Run:
- python scripts/audit_c60_stone_wales.py --out-dir c60_stone_wales_audit --relax
- pytest -q tests/test_c60_stone_wales.py

The workflow uploads JSON/Markdown reports and graph arrays. Inspect the artifact before classifying the results as verified.

## Evidence classification

| Claim | Status |
|---|---|
| C60 starting topology is (60,90,32;12,20) | Existing repository audit |
| SW switch preserves vertex/edge counts and degree 3 | Exact property of specified switch |
| At least one admissible planar Stone–Wales 2-switch exists | Pending run |
| An admissible planar SW_5|6 post-graph exists | Pending run |
| Both chain-map identities hold for selected maps | Pending run |
| MMFF94s nuclear-coordinate covariance changes | Pending run |
| Electronic density anisotropy changes and matches vesica tensor | Open; not computed |
| A commutative map to Kathara/Q6 exists | Open; not computed |

## References

- Austin et al., “The Stone–Wales map for C60,” *Chemical Physics Letters* 235 (1995), 146–151, DOI: [10.1016/0009-2614(95)00082-F](https://doi.org/10.1016/0009-2614(95)00082-F).
- “Topological Anisotropy of Stone–Wales Waves in Graphenic Fragments,” *Nanoscale Research Letters* (2011): [PMC3233447](https://pmc.ncbi.nlm.nih.gov/articles/PMC3233447/).
- “The topology of fullerenes,” *WIREs Computational Molecular Science* (2015), DOI: [10.1002/wcms.1207](https://doi.org/10.1002/wcms.1207).

## 7. Numerical result from GitHub Actions

**Run:** 2026-11-26, dedicated C60 Stone–Wales workflow; graph audit and focused pytest both completed successfully.

The dual-edge-flip enumeration returned **30 labelled admissible flips** from the ideal truncated-icosahedral C60. The selected representative is:

- dual edge flipped: (15, 19);
- opposite pentagonal dual vertices: (2, 3);
- corresponding carbon vertices: (36, 37);
- direct bonds removed: (5, 37), (13, 36);
- direct bonds added: (5, 36), (13, 37).

The reconstructed graph has the same topology before and after:
\[
(V,E,F;p,h)=(60,90,32;12,20),\qquad \deg(v)=3,\qquad \chi=2.
\]
The integer chain-map audit passed with \(S_1\) of size 90×90 and rank 90, and \(S_2\) of size 32×32 and rank 31. Both boundary identities were exact.

### MMFF94s relaxed-coordinate proxy

The same RDKit MMFF94s protocol was applied to the ideal C60 graph and the selected post-SW graph. Reported final force-field energies were 945.1698747 and 963.0943689 (same model and units), a difference of +17.9244942. Optimizer status was 0 for both; final gradient norms were 0.22199 and 0.21343.

| Nuclear-coordinate covariance descriptor | Before | After |
|---|---:|---:|
| Global 3D anisotropy | 0.0438637 | 0.1381264 |
| Local switched-patch anisotropy | 0.8911495 | 0.8997506 |

These values are **nuclear-coordinate covariance proxies** for one selected labelled flip and one empirical force-field relaxation. They are not electronic-density covariance, a De Aquino overlap moment, a DFT result, or a transition-state barrier. The local patch is defined by the switched bond endpoints and one graph-neighbour shell. The result establishes that this particular MMFF94s relaxation changes the geometric covariance; it does not yet establish a universal fullerene–vesica law.

### Evidence classification after the run

| Claim | Status |
|---|---|
| 30 admissible dual-edge flips on the ideal C60 graph | Numerically verified by the enumerator |
| C60 topology and ring inventory preserved for each retained flip | Verified by exact graph checks |
| Chain-map identities for selected representative | Exact integer verification |
| MMFF94s relaxed nuclear-coordinate covariance changes | Numerically verified for one selected representative |
| Electronic-density anisotropy changes | Open; no electronic density computed |
| A commutative fullerene–Kathara/Q6 map exists | Open |
| The molecular vesica tensor and fullerene nuclear covariance obey one common law | Open |

The 30 labelled flips are consistent with the classical C60 Stone–Wales patch count reported in the C60 isomer literature; labelled flips should not be confused with 30 non-isomorphic chemical isomers.\n\n### Symmetry and graph-isomorphism classification (new audit)\n\nThe companion script `scripts/classify_c60_sw_orbits.py` enumerates the automorphism group of the icosahedral fullerene dual graph, verifies its order, and partitions the 30 labelled dual flips under that action. The action is applied to the dual edge being flipped, not to an arbitrarily labelled carbon-graph reconstruction.

The exact finite-graph result is:

- admissible labelled SW_{5|6} dual flips: **30**;
- automorphism group order of the dual graph: **120** (the full (I_h) symmetry group);
- unlabelled post-switch carbon-graph isomorphism classes: **1**, of size 30;
- (I_h)-orbits of admissible dual edges: **1**, of size 30.

Thus the 30 labelled operations are one symmetry orbit and produce one unlabelled post-switch graph class. They are **not 30 non-isomorphic C60 chemical isomers**. The classification is combinatorial; it does not calculate transition-state trajectories, barriers, or multi-step isomer networks. The full partition is written to `orbit_classification.json` by the workflow.

### Chemical identification of the local move

The dual flip has two degree-6 endpoints (hexagons) and two opposite degree-5 vertices (pentagons). In the direct fullerene surface, this is the pyracylene (mathrm{SW}_{5|6}) rearrangement, with the local four-ring pattern (5/6/6/5 \rightarrow 6/5/5/6). It is not the graphenic (mathrm{SW}_{6|6}) operation, whose initial four-ring patch consists of four hexagons and produces a (5/7/7/5) defect. The distinction follows the established fullerene/graphene terminology in Ori et al. (2011) and the dual-edge description in Sabirov & Ori (2020).
The 30 labelled flips are consistent with the classical C60 Stone–Wales patch count reported in the C60 isomer literature; labelled flips should not be confused with 30 non-isomorphic chemical isomers.


## Pyracylene patch signature: explicit regression criterion

For each accepted dual flip, the two endpoints of the flipped dual edge must have degree 6 and the two opposite vertices must have degree 5. Thus the initial four-ring patch is exactly \(5/6/6/5\), with a central direct \(6|6\) bond. After the flip, the two old degree-6 dual vertices become degree 5 and the two old degree-5 vertices become degree 6, giving \(6/5/5/6\). The regression test checks this degree exchange explicitly; it also checks that the direct-graph ring inventory remains 12 pentagons and 20 hexagons.

The 30 labelled flips remain one symmetry orbit, not 30 distinct isomer classes. This is a finite-graph result and does not by itself establish a transition-state trajectory or activation barrier.


## Homology qualification

The two boundary identities establish a chain map, but do not alone prove that the induced map on homology is an isomorphism. In particular, the rank of the chosen face-chain matrix \(S_2\) is not a substitute for checking the fundamental class. The regression test now constructs the one-dimensional kernel of each cellular boundary matrix \(B_2\) and verifies that the chain map sends a generator of the old spherical fundamental class to exactly \(+1\) or \(-1\) times a generator of the new one. This certifies the induced map on \(H_2(S^2;\mathbb Z)\) for the selected chain map. It does not establish an embedding isotopy or a chemical transition path.

## CI provenance

The previously reported successful workflow run was attached to an earlier commit SHA, not the final PR #449 head SHA. Until the new regression passes on this branch and the resulting run SHA is recorded, the merged implementation should not be described as fully CI-verified.
