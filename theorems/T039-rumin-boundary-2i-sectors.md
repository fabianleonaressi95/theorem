# T039 — Exact SU(2) degree and 2I multiplicities of the Rumin boundary sectors

**Status:** exact representation identification from Kitaoka's n=1 boundary weights, combined with exact T032 Molien multiplicities. This closes the degree-identification gap left open in the first T039 draft.

## 1. Boundary weights and SU(2) degree

Kitaoka Proposition 1.1, cases VI and VII, gives for n=1:

- VI: q=-1, p>=1, in E^(1,0), with U(2) highest weight (q,-p)=(-1,-p).
- VII: p=-1, q>=1, in E^(0,1), with U(2) highest weight (q,-p)=(q,1).

For a U(2) highest weight (q,-p), restriction to SU(2) has highest-weight degree m=q+p, and the restricted module is Sym^m(C^2), because the determinant factor is trivial on SU(2). Thus, writing n>=1 for the positive boundary index, m=n-1 on both exceptional boundaries:
- q=-1: m=p-1;
- p=-1: m=q-1.

This follows from the exceptional U(2) weights in cases VI/VII and the standard U(2) to SU(2) highest-weight restriction. It is not an extrapolation from the generic middle block.

## 2. Boundary eigenvalues

The special Reeb-field calculation in Kitaoka section 2.3, cases VI/VII, gives:
- lambda_VI(p)=(p+1)^2/4;
- lambda_VII(q)=(q+1)^2/4.

In terms of m=n-1, both are lambda_boundary(m)=(m+2)^2/4. The two orientations remain separate geometric sectors even though their scalar eigenvalues and SU(2) degrees agree.

## 3. Exact 2I multiplicities

Let b_(m,rho) denote the multiplicity of irreducible rho of 2I in Sym^m(C^2)|2I. T032 supplies exact Molien coefficient functions for all nine irreducibles. T039 evaluates them at the geometrically determined degree m=n-1.

The audit verifies the dimension identity:
sum_rho d_rho*b_(m,rho)=m+1.

For the untwisted quotient, the boundary multiplicity of a single U(2) type is a_m=b_(m,1), the trivial-irrep Molien coefficient. All twisted isotypic dimensions are also reported.

## 4. Deliverables and reproducibility

- src/t039_rumin_boundary_2i_sectors.py: exact boundary weight, degree, eigenvalue and all nine 2I multiplicities.
- tests/test_t039_rumin_boundary_2i_sectors.py: exact degree/eigenvalue checks, both orientations, dimension sum, and first nonconstant invariant degree.
- data/t039_rumin_boundary_2i_audit.json: CLI output.

CLI:
- python -m pytest tests/test_t039_rumin_boundary_2i_sectors.py -q
- python -m src.t039_rumin_boundary_2i_sectors --kind q=-1 --index 13
- python -m src.t039_rumin_boundary_2i_sectors --kind p=-1 --index 13

At n=13, m=12, the boundary eigenvalue is 49 and the trivial 2I multiplicity is a_12=1, matching the independent T025/Kitaoka boundary audit.

## 5. Scope ledger

| Claim | Status |
|---|---|
| Boundary U(2) highest weights, cases VI/VII | Source-level identification from Kitaoka Proposition 1.1 |
| SU(2) degree m=n-1 | Exact highest-weight restriction |
| Boundary eigenvalues | Exact special-case formula from Kitaoka section 2.3 |
| All nine finite 2I multiplicities | Exact T032 Molien coefficients |
| Dimension sum m+1 | Exact finite-dimensional identity checked by code |
| Full boundary differential matrices in one common geometric basis | Open |
| Complete twisted analytic torsion / zeta derivative at zero | Open |

## References

1. A. Kitaoka, Analytic torsions associated with the Rumin complex on contact spheres, arXiv:1911.03092, Proposition 1.1 cases VI/VII and section 2.3 equations (1.3), (2.4).
2. T025, theorems/T025-rumin-middle-degree-blocks.md.
3. T032, src/t032_2i_molien.py and theorems/T032-2i-irrep-molien-projectors.md.
4. T037, exact intertwiner/projector realization of the finite-degree decomposition.

## Classification

The boundary-to-Sym^(n-1) identification is source-derived and exact. The 2I decomposition is exact finite-group representation theory. This does not by itself evaluate the regularized spectral zeta derivative or analytic torsion.
