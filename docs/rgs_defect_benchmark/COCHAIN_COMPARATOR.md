# Edge-cochain comparator

This implementation makes the discrete kinematics explicit:

- each displacement component is a 0-cochain on mesh vertices;
- `d0` is the integer oriented vertex-to-edge incidence matrix;
- `d1` is the oriented edge-to-face incidence matrix;
- the exact chain identity `d1 @ d0 == 0` is tested;
- on each oriented triangle, edge differences reconstruct the constant P1 displacement gradient;
- the symmetric gradient enters the isotropic elastic energy.

The square can be split along either the SW–NE or SE–NW diagonal. Both orientations are now assembled as separate chain complexes and are included in the Q1-versus-cochain comparison. Each triangle inherits the smooth cellwise eigenstrain of its parent square. This allows a first sensitivity audit for mesh-orientation bias, but does not eliminate all mesh anisotropy or replace a rotated-mesh study. This is a cochain-based simplicial P1 comparator, not a physical realization of Q6 or the full PRISM graph. It also does not yet model singular Volterra dislocations, disclinations, or the Airy-stress formulation.

Run:

```bash
python scripts/rgs_cochain_defect_benchmark.py --self-test
python scripts/rgs_cochain_defect_benchmark.py --out artifacts/rgs_cochain_defect
```

Outputs are `report.json` and `results.csv`. The tests check the chain identity, affine patch test, zero-source case, and finite single/dipole solutions. Passing these tests validates only the implementation-level comparator, not a continuum limit or a material model.


## Regularized Volterra edge-dislocation source

A first Volterra-type source is now available as `volterra_edge`. It is a finite-width regularization of a slip cut starting at `(x0,y0)=(0.5,0.5)) and extending to the right boundary. For Burgers vector `b = b e_x` and cut normal `n = e_y`, the plastic distortion is represented distributionally by

`beta_p = b (e_x tensor e_y) delta(y-y0) H(x-x0)`.

The elastic energy uses the symmetric plastic strain, whose engineering shear component is

`gamma_p_xy = b delta(y-y0) H(x-x0)`.

The delta is regularized by a normalized Gaussian of width `core_width=0.025`. The code integrates this engineering shear across a vertical section to audit the Burgers magnitude (`b=0.02`). Both Q1 and cochain solvers include this source, and the comparison script runs it for both triangulation diagonals.

This is a controlled regularized Volterra slip-cut benchmark, not an exact singular Volterra solution: the core is smeared, the cut is represented by an eigenstrain field, and no atomistic core physics is included. The Burgers integral validates the imposed slip jump; it does not by itself validate the far-field Volterra stress/displacement asymptotics.
