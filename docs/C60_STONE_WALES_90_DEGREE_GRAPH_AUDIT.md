# C60 Stone-Wales 90° graph and covariance audit

**Status:** implementation added; numerical status is pending the dedicated GitHub Actions run. No result is promoted to verified until the workflow report and artifact are inspected.

## Starting graph

The existing ideal truncated-icosahedron generator supplies the cage:
\[
(V,E,F;p,h)=(60,90,32;12,20),\qquad \deg(v)=3.
\]

## Exact graph operation

For a central edge \(B-C\) shared by a pentagon and a hexagon, enumerate the four-site Stone-Wales switch
\[
AB,CD\mapsto AC,BD,
\]
retaining \(BC\). Keep only resulting graphs that are planar, trivalent, have 60 vertices and 90 edges, and retain exactly 12 pentagons and 20 hexagons. Distinct post-graphs are deduplicated.

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
| An admissible planar SW_5|6 post-graph exists | Pending run |
| Both chain-map identities hold for selected maps | Pending run |
| MMFF94s nuclear-coordinate covariance changes | Pending run |
| Electronic density anisotropy changes and matches vesica tensor | Open; not computed |
| A commutative map to Kathara/Q6 exists | Open; not computed |

## References

- Austin et al., “The Stone–Wales map for C60,” *Chemical Physics Letters* 235 (1995), 146–151, DOI: [10.1016/0009-2614(95)00082-F](https://doi.org/10.1016/0009-2614(95)00082-F).
- “Topological Anisotropy of Stone–Wales Waves in Graphenic Fragments,” *Nanoscale Research Letters* (2011): [PMC3233447](https://pmc.ncbi.nlm.nih.gov/articles/PMC3233447/).
- “The topology of fullerenes,” *WIREs Computational Molecular Science* (2015), DOI: [10.1002/wcms.1207](https://doi.org/10.1002/wcms.1207).
