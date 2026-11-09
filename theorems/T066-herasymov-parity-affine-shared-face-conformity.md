# T066 — Herasymov parity-cell affine shared-face conformity

**Status:** proved under the explicit cellwise-affine geometric interpretation below.

## 1. Geometric data

Let (Delta={0,1}^3) label the eight interleaved parity classes of the doubled lattice. The labels are not contiguous octants. For each (deltainDelta), assign an affine cube isometry
[
Phi_delta(x)=A_delta x+b_delta,qquad xin[0,N]^3,
]
where (A_delta) is a signed permutation matrix and (b_delta) is the corresponding continuous cube-isometry offset. In particular, a reflected continuous coordinate uses the offset (N), not the voxel-index offset (N-1).

For neighboring parity classes (delta) and (delta+e_i), require their affine traces to agree pointwise on every internal shared face, for every parent-cell index and every tangential parity patch.

## 2. Theorem

For (Nge2), the parity-cell assignment is face-conforming if and only if
[
Phi_delta=Phi_{delta+e_i}
quad	ext{for every }delta_i=0, iin{1,2,3}.
]
Equivalently, there is one affine map (Phi(x)=Ax+b) such that
[
oxed{A_delta=A,qquad b_delta=bquad	ext{for all }deltainDelta.}
]

Thus all eight parity classes must select the same coordinate map. A source-mode bit that changes only a scalar increment and leaves the coordinate map unchanged is geometrically invisible to this face-trace criterion.

## 3. Proof

Fix a neighboring parity pair ((delta,delta+e_i)), and define
[
Psi(x)=Phi_delta(x)-Phi_{delta+e_i}(x)=Dx+c.
]
Pointwise agreement on a shared face means that (Psi) vanishes on a relatively open two-dimensional patch in a plane normal to the (i)-th coordinate axis. Since (Psi) is affine, vanishing on such a patch forces the two tangential columns of (D) to vanish and fixes the affine offset on that plane.

The hypothesis imposes agreement for every parent-cell index. Since (Nge2), there are at least two distinct parallel shared-face planes. Vanishing on a second such plane forces the remaining normal column of (D) to vanish; then (c=0). Hence (D=0), (c=0), and the two affine maps are identical.

Conversely, identical affine maps have identical restrictions to every common face. Finally, the parity adjacency graph is the connected three-dimensional cube graph. Equality along every parity edge therefore implies equality of all eight affine maps. (square)

## 4. Exact finite audit

The source-mode audit exhausts all 256 rotation-generator modes and identifies 32 distinct affine coordinate maps. It compares shared-face traces using doubled integer coordinates, avoiding floating-point tolerances, and exhausts all ordered pairs of distinct coordinate maps for each of the three face normals. Regression tests include:
- a uniform-coordinate positive control;
- a control in which the scalar-complement/increment rule changes while the geometry stays fixed;
- a mixed-reflection negative control;
- exhaustive pairwise verification of the face-compatibility criterion.

The theorem's general conclusion follows from the affine argument above. The enumeration verifies the finite source-mode classification and the implementation. GitHub Actions run #92, commit `6fd5ab9` (9 November 2026), completed the audit and regression tests successfully.

## 5. Scope and non-conclusions

The theorem applies only after the source rules have been interpreted as the explicit affine maps (Phi_delta). It does not establish that the original voxel-value recursion, by itself, defines such a geometric cell map. It also does not prove scalar continuity, conservation, a cellular chain map, FEEC stability, discrete compactness, Mosco convergence, or a continuum limit. The scalar increment rule must be audited separately from the coordinate geometry.
