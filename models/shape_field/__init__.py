"""Shape-Field FEM-01: 1-D electrostatic benchmarks (NumPy/SciPy backend).

Scope (protocol docs/SHAPE_FIELD_CADFEM_ELECTROSTATIC_PROTOCOL_2026-11-26.md):
  * parallel-plate capacitor  -> exact linear solution, beta = 1;
  * conducting sphere in uniform field E0 -> l=1 radial reduction,
    beta -> 3 at the poles.

The backend is deliberately small and inspectable. The public entry points
(`solve_plate`, `solve_sphere_l1`) isolate the discretisation so a future
FEniCSx/DOLFINx backend can replace `laplace_1d` internals without touching
the benchmark layer.
"""
