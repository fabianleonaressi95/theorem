# C60 MMFF94s relaxation and Coulomb tangent-Hessian audit

**Status: executable protocol committed; numerical relaxed-geometry result pending execution in GitHub Actions.**

This audit follows up the ideal truncated-icosahedron comparison. It deliberately separates two functionals:

1. MMFF94s molecular mechanics is used to relax the neutral C60 cage.
2. The all-pairs Coulomb energy is then evaluated on that relaxed geometry, and its *raw* Hessian is restricted to the subspace orthogonal to three translations and global dilation.

No Coulomb Lagrange shift is applied unless the Coulomb tangential gradient is numerically zero. An MMFF stationary point is not automatically a Coulomb stationary point.

## Molecular model

The ideal cage is generated from the 12 vertices and 30 edges of a regular icosahedron. Its 60 sites are the directed-edge truncation points
[
x_{u\to v}=(2u+v)/3.
]
The graph is required to have 60 vertices and 90 nearest-neighbour bonds. The script encodes this graph as a neutral all-aromatic carbon cage and asks RDKit for MMFF94s parameters. This is an explicit model choice, not a claim that an all-aromatic parameterization is the unique physical description of C60.

## Reproduction

Install NumPy, SciPy, and RDKit, then run:

```bash
python scripts/audit_c60_mmff94s_relaxed_coulomb.py --out-dir c60_mmff94s_audit
```

The script writes:
- `C60_MMFF94s_relaxed_coulomb.npz`: ideal and relaxed coordinates, graph, tangent basis, Coulomb Hessian and spectrum;
- `report.json`: MMFF energy/force diagnostics, Coulomb gradient and tangent residual, Hessian inertia.

## Interpretation rules

- A successful MMFF minimization is not a DFT result and is not experimental validation.
- If RDKit cannot sanitize the graph or provide MMFF94s parameters, the run must fail visibly; no fallback or synthetic geometry is silently substituted.
- If the Coulomb tangential gradient is nonzero, report the Hessian restriction as a diagnostic, not as the second variation at a Coulomb equilibrium.
- Exact (I_h/T_h) decomposition is only valid if the relaxed geometry preserves the corresponding action within a stated numerical tolerance. A symmetry-broken relaxed geometry must not inherit the ideal cage's irrep labels.
- Compare with Q6-64 only after matching scale, tangent constraints, Hessian convention, and group action.

## Current classification

**Candidate computational protocol; no new numerical claim until the workflow has completed and its artifacts have been inspected.**
