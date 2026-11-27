# dec-se3 volumetric complex and Bianchi tests

Run:

```bash
cd output/dec_se3
python -m pytest -q
```

Includes:

- `SE(3)` connection algebra and holonomy;
- gauge covariance;
- tetrahedralization of a cube;
- icosahedral volumetric complex with C60-like boundary;
- discrete boundary-holonomy identity on every tetrahedron;
- curvature and torsion fixtures;
- explicit separation between surface-only C60 data and volumetric Bianchi tests.
