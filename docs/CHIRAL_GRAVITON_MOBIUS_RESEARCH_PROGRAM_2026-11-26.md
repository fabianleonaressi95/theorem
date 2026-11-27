# Research programme: chiral lattice modes and Möbius/Brownian statistics

**Date:** 2026-11-26  
**Purpose:** connect two external research leads to falsifiable RGS research tasks without asserting a common physical mechanism.

## Two independent workstreams

### CG — Chiral graviton modes in fractional Chern insulators

Source: Long et al., arXiv:2601.05196 (2026), DOI 10.1088/1361-6633/ae8369.

The source constructs lattice stress and short-range quadrupolar density operators and studies chirality-resolved many-body spectral response. Its lifetime diagnostic separates broadening η from intrinsic decay through Γtot(η) ≃ ΓG+cη, with c ≃ 1. The reported FCI intrinsic decay is finite, not zero.

Canonical record: open-problems/CHIRAL_GRAVITON_FCI_LATTICE_RESPONSE.md.

### MB — Möbius coefficients and Brownian diagnostics

Source: Mussardo & Leclair, arXiv:2101.10336 (2021), DOI 10.1088/1742-5468/ac22fb.

The exact finite arithmetic objects are μ(n), M(N)=Σ(n≤N)μ(n), and the restricted sign sequence μ(fⱼ) on square-free integers. Statistical tests concern finite samples under stated null models, not proofs of RH/GRH or functional Brownian convergence.

Canonical record: open-problems/MOBIUS_BROWNIAN_GRH_REPRODUCTION.md.

## Shared method, not shared physics

1. Define the microscopic object and conventions.
2. Define observables independently of the desired output.
3. Compute exact finite identities first.
4. Separate finite-size/broadening effects from intrinsic quantities.
5. Test robustness under scale, truncation and parameter changes.
6. Record negative results and uncertainty.
7. Distinguish theorem, exact finite computation, numerical evidence and hypothesis.

There is no established map from Möbius sums to FCI stress response, nor from Q6/PRISM graph spectra to a fractional Chern insulator. No such identification is claimed here.

## Repository placement

- The central mathematical programme tracks both records and the finite Möbius audit.
- The RGS–QLG quaternion bridge may later host an FCI Hamiltonian implementation only after the Chern band, interactions, filling, many-body sector and operator derivation are explicitly supplied.
- PRISM/Krist-All may provide reusable graph/spectral infrastructure, but it does not by itself establish fractional topological order.

## Acceptance criteria

- Source equations and conventions link to original papers.
- The Möbius implementation passes exact small-value tests.
- The FCI document distinguishes source results from proposed RGS transfer.
- No RH/GRH, topological-phase or physical-graviton claim is upgraded by analogy.
- Every later numerical result includes code, input provenance, tolerances and a reproducible command.
