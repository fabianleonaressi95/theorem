# CYM-T002 — Stability of spectral morphology under perturbations

**Status:** open research problem; no theorem claimed.

## Question

For a specified family of self-adjoint operators (K(\varepsilon)) and mass matrices (M(\varepsilon)), under what assumptions do small coefficient, geometry, or boundary perturbations preserve (a) an isolated eigenspace, (b) its symmetry type, and (c) the topology of a selected nodal set?

## Required distinctions

1. **Eigenvalue stability:** perturbation bounds for isolated eigenvalues.
2. **Eigenspace stability:** subspace-angle estimates; individual eigenvectors are not stable under degeneracy.
3. **Nodal-set stability:** requires additional regularity and transversality assumptions; it does not follow from an eigenvalue gap alone.
4. **Observed-pattern stability:** also depends on forcing, damping, granular transport, imaging threshold, and noise.

## Minimal benchmark

Use the C01 square-plate operator, perturb its stiffness by a controlled asymmetric term, and record eigenvalue splitting, invariant-subspace rotation, and nodal-set displacement as the perturbation amplitude tends to zero.

## Potential route

Combine standard self-adjoint perturbation theory (including Davis–Kahan-type subspace estimates) with a separate analysis of zero-set regularity. State constants and norms explicitly. Do not infer topological stability from a spectral gap alone.

## Falsification criteria

The proposed stability statement fails if a sequence of perturbations with the stated norm bound produces an eigenspace rotation or nodal-topology change exceeding the claimed bound. All mesh and threshold effects must be separated from continuum effects.
