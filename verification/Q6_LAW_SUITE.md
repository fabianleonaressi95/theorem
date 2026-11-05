# Q6 law verification suite

Run from the repository root:

```bash
python -m pip install numpy
python scripts/verify_q6_laws.py --seed 20261105 --output q6-law-report.json
```

The script checks:
- Q6 cardinalities (64 vertices, 192 edges, 240 square 2-cells);
- the cubical chain identity \(\partial_1\partial_2=0\);
- graph cycle rank 129, separately from the first Betti number after square faces are filled;
- the six Euclidean Clifford relations;
- the exact free spectrum in T015;
- local SU(3) covariance of the link-coupled graph operator for a reproducible random gauge transformation;
- invariance of the three-color epsilon tensor.

## Interpretation of the topology output

For the 1-skeleton, the graph cycle rank is \(192-64+1=129\). This is not the first Betti number of the square-filled cubical 2-skeleton. With all 240 square faces included, the boundary ranks are 63 and 129, respectively, so the first homology rank is \(192-63-129=0\). The script reports floating-point SVD ranks as diagnostics, not exact integer certificates.

## Interpretation of a passing run

A passing run confirms the implemented finite algebra and the stated random-instance covariance tests. It does not establish a physical QCD action, a fermion determinant, confinement, baryon masses, reflection positivity, or a continuum limit. Those require separate constructions and proof obligations listed in `foundations/ESTABLISHED_AND_RGS_LAW_CATALOGUE.md`.
