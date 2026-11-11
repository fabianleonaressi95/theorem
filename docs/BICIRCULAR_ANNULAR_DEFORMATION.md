# Bicircular-annular deformation measurement

This note is the operational companion to [T099](../theorems/T099-bicircular-annular-deformation-reconstruction.md).

## What is measured

The two disks provide a lens domain and two natural sampling centres. Annuli around both centres provide directional samples of a displacement or feature field. The reconstruction reports:

- lens chord, area and centroid;
- least-squares deformation gradient (F_h);
- Green–Lagrange strain (E_h=(F_h^TF_h-I)/2);
- principal strains and the planar anisotropy magnitude;
- residuals of the affine fit;
- polygonal Frank/Burgers loop closures when an independently defined kinematic field is supplied.

The geometric parameters alone are not enough to reconstruct an arbitrary deformation. Displacement/feature correspondences and a full-rank sampling design are required.

## Run

```bash
python scripts/run_bicircular_annular_audit.py --out artifacts/bicircular_annular_audit.json
python -m pytest -q tests/test_bicircular_annular_geometry.py
```

## Interpretation rules

1. Keep geometric anisotropy, strain anisotropy and constitutive material anisotropy separate.
2. Keep the centroid distinct from a density-weighted barycentre.
3. Keep the mesh-map metric distinct from the physical strain field.
4. Do not identify a nonzero residual with a dislocation/disclination without a loop/connection definition.
5. Treat the Frank/Burgers runner as a manufactured circulation test, not as an elasticity solution.
6. For Möbius or other non-orientable domains, use local frames and explicit transition maps; do not impose a global orientation.
