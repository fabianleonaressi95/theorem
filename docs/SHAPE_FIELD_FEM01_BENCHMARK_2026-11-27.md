# Shape–Field FEM-01 — 1-D benchmark results (2026-11-27)

First computational stage of the Shape–Field workstream
(`SHAPE_FIELD_CADFEM_ELECTROSTATIC_PROTOCOL_2026-11-26.md`, status OPEN).
Backend: custom NumPy/SciPy P1 finite elements (`models/shape_field/`).
**These are solver-verification benchmarks against known analytic solutions —
not physical validation, not a theorem, and no discharge/plasma claim.**

## 1. Implementation

- `models/shape_field/laplace1d.py` — generic 1-D P1 assembler/solver
  (`assemble_and_solve`, `graded_mesh`); 2-pt Gauss quadrature per element;
  SciPy sparse direct solve. Backend-isolated: a future FEniCSx/DOLFINx
  implementation can replace this module without touching the benchmarks.
- `models/shape_field/benchmarks.py` — `solve_plate`, `solve_sphere_l1`,
  `sphere_convergence`. All outputs are plain dicts (JSON-serialisable).
- `tests/test_shape_field_fem01.py` — 8 tests, all passing.

## 2. Parallel plate (exact check)

`φ'' = 0` on `[0,d]`, `φ(0)=0`, `φ(d)=V`. P1 elements reproduce the linear
solution exactly:

| Quantity | Numerical | Exact | Error |
|---|---|---|---|
| E (d=1, V=1) | −0.9999999999999998 | −1 | 2.2e-16 rel |
| β | 0.9999999999999998 | 1 | ~2e-16 |
| max \|φ_num − φ_exact\| | — | — | 5.6e-17 |
| energy/area (d=2, V=3) | 0.5·(1.5)²·2 | same | < 1e-12 rel |

The protocol's 1e-6 target is exceeded by ~10 orders of magnitude — expected,
since the exact solution lies inside the P1 space.

## 3. Conducting sphere in uniform field — l=1 reduction

`φ(r,θ) = u(r) cos θ` reduces Laplace to the radial equation
`u'' + (2/r)u' − (2/r²)u = 0` on `[a, r_far]`, weak form
`∫(r²u'v' + 2uv)dr = 0`. This is **not** a scalar radial problem: the `l=1`
angular mode and the `2u/r²` curvature-potential term are retained; only the
θ-dependence is factored out analytically.

Inner BC `u(a)=0` (grounded sphere). Two outer-BC variants, per the protocol
correction:

- `exact`: `u(r_far)` = analytic `−E0(r_far − a³/r_far²)` — isolates pure
  discretisation error.
- `far_field`: `u(r_far) = −E0·r_far` — the physical truncated-domain BC
  (`φ = −E0 z` on the boundary); its defect vs the exact tail is
  `E0·a³/r_far²`.

### Convergence (a=1, E0=1, r_far=20, graded mesh β=6)

| n_elem | BC | β_recovered | \|β−3\| | max\|u−u_exact\| | BC gap |
|---|---|---|---|---|---|
| 100 | exact | 2.94510 | 5.5e-2 | 1.9e-4 | — |
| 200 | exact | 2.98958 | 1.0e-2 | 4.8e-5 | — |
| 400 | exact | 2.99833 | 1.7e-3 | 1.2e-5 | — |
| 800 | exact | 2.99975 | **2.5e-4** | 3.0e-6 | — |
| 100 | far_field | 2.94547 | 5.5e-2 | 2.5e-3 | 2.5e-3 |
| 200 | far_field | 2.98995 | 1.0e-2 | 2.5e-3 | 2.5e-3 |
| 400 | far_field | 2.99870 | 1.3e-3 | 2.5e-3 | 2.5e-3 |
| 800 | far_field | 3.00013 | 1.3e-4 | 2.5e-3 | 2.5e-3 |

### Error separation (mandated)

- **Discretisation error** (`exact` BC): `u` converges ~O(h²); β (via cubic
  recovery through the first 8 nodes, differentiated at `r=a`) reaches
  **2.5e-4 < 1e-3** at n=800. Raw P1 boundary gradient converges only
  ~O(h) (err 2.5e-2 at n=800) — reported separately as `beta_raw`, never
  silently upgraded.
- **Domain-truncation error** (`far_field` BC): potential error floors at
  exactly `E0·a³/r_far² = 2.5e-3` for r_far=20 — matching the analytic BC
  gap to all printed digits. Doubling the domain to r_far=40 reduces the gap
  to ~3.1e-4 (≈8×, the expected `1/R²` scaling).
- **Domain independence** (protocol §8.5): β at r_far=20 vs 40 differs by
  4.3e-4 absolute (**0.014 %** < 1 %).

## 4. What is NOT claimed

- No 2-D/3-D geometry (wedge, opposed tips, triangle, disk) is implemented —
  FEM-02 scope, pending FEniCSx evaluation.
- β=3 is reproduced as a **solver check** against the known analytic
  solution; it is not evidence about physical discharges.
- Inception voltage, plasma, Maxwell–Fluent coupling: untouched (protocol
  stages 7+, explicitly out of scope here).
- The 1e-6 protocol tolerance is met for the plate (exact) and approached
  for the sphere potential (3e-6 at n=800); β meets the 1e-3 target only via
  the documented derivative-recovery post-processing.

## 5. Reproduction

```bash
python3 -m pytest tests/test_shape_field_fem01.py -q   # 8 passed
python3 - <<'EOF'
from models.shape_field.benchmarks import sphere_convergence
for r in sphere_convergence(n_elems=(100,200,400,800), outer_bc="exact"):
    print(r["n_elem"], r["beta_recovered"], r["beta_err"], r["max_abs_u_err"])
EOF
```

Dependencies: NumPy, SciPy only.
