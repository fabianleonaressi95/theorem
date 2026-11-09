# Edge-cochain comparator

This implementation makes the discrete kinematics explicit:

- each displacement component is a 0-cochain on mesh vertices;
- `d0` is the integer oriented vertex-to-edge incidence matrix;
- `d1` is the oriented edge-to-face incidence matrix;
- the exact chain identity `d1 @ d0 == 0` is tested;
- on each oriented triangle, edge differences reconstruct the constant P1 displacement gradient;
- the symmetric gradient enters the isotropic elastic energy.

The square is split along a fixed SW–NE diagonal. Each triangle inherits the smooth cellwise eigenstrain of its parent square. This is a cochain-based simplicial P1 comparator, not a physical realization of Q6 or the full PRISM graph. It also does not yet model singular Volterra dislocations, disclinations, or the Airy-stress formulation. The fixed diagonal may introduce directional bias, so a flipped-diagonal/orientation study is required before interpreting anisotropy.

Run:

```bash
python scripts/rgs_cochain_defect_benchmark.py --self-test
python scripts/rgs_cochain_defect_benchmark.py --out artifacts/rgs_cochain_defect
```

Outputs are `report.json` and `results.csv`. The tests check the chain identity, affine patch test, zero-source case, and finite single/dipole solutions. Passing these tests validates only the implementation-level comparator, not a continuum limit or a material model.
