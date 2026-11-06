# Herasymov parity rules: exact shared-face conformity criterion

## Geometric interpretation

The rotation-enhanced source assigns one of eight rules to each parity class
\(\delta\in\{0,1\}^3\) of the doubled output lattice. These are
interleaved sublattices, not eight contiguous octants.

For a source mode \(m\), the voxel-index map has the form
\[
v_m(p)=A_m p+b_m^{\rm vox},
\]
where \(A_m\) is a signed permutation matrix. Its induced continuous
isometry of the cube \([0,N]^3\) is
\[
\Phi_m(x)=A_mx+b_m,\qquad
(b_m)_i=(b_m^{\rm vox})_i+
\begin{cases}
1,&\text{row }i\text{ of }A_m\text{ has its nonzero entry }-1,\\
0,&\text{otherwise.}
\end{cases}
\]
The correction from \(N-1\) to \(N\) is essential: voxel indices label
unit cells, whereas the continuous map acts on their vertices.

For each parity class let \(\Phi_\delta\) be the affine cube map selected
by its mode. On a fine cell with index \(q=2p+\delta\), the cell map is
the restriction of \(\Phi_\delta\) to that fine cell.

## Theorem (necessary and sufficient criterion)

Assume \(N\geq2\), and require pointwise equality of the two affine traces
on every internal face shared by neighboring fine cells. Then the parity
assignment is face-conforming if and only if
\[
\Phi_\delta=\Phi_{\delta+e_i}
\quad\text{for every }i\text{ and every }\delta_i=0.
\]
Equivalently, because the parity cube is connected,
\[
\boxed{A_\delta=A,\quad b_\delta=b
\quad\text{for all }\delta\in\{0,1\}^3.}
\]

### Proof

Fix an axis \(i\) and a parity pair \(\delta,\delta+e_i\) with
\(\delta_i=0\). Their neighboring fine cells share faces at
\(x_i=p_i+\tfrac12\), for every parent index \(p_i=0,\ldots,N-1\).
The tangential face patch has nonempty relative interior.

Let
\[
\Psi(x)=\Phi_\delta(x)-\Phi_{\delta+e_i}(x)=Dx+c.
\]
If the traces agree on a shared face, \(\Psi\) vanishes on its
two-dimensional relative interior. This forces the two tangential columns
of \(D\) to vanish and fixes the corresponding affine offset on that
plane. Since \(N\geq2\), there are at least two distinct parallel
shared-face planes. Vanishing on both forces the remaining normal column
of \(D\) and \(c\) to vanish. Thus \(D=0\) and \(c=0\), so the two
affine maps are identical.

Conversely, if the affine maps are identical, their restrictions to every
shared face are identical. Applying this argument to all parity edges and
using connectedness of the three-dimensional parity cube proves that all
eight maps must be the same affine cube isometry. QED.

The proof is exact and does not depend on floating-point tolerances. The
implementation compares doubled integer coordinates at the four vertices
of every shared face; for affine maps, vertex equality is equivalent to
equality of the entire face trace.

## Geometry versus scalar data

The source's bit 3 toggles the scalar operation (increment versus unchanged)
without changing the coordinate map. Therefore two modes differing only by
bit 3 can be geometrically face-conforming while applying different scalar
rules. The audit reports these two conditions separately. A scalar field
continuity or conservation requirement would be an additional condition,
not part of geometric face conformity.

## Exhaustive finite audit

The audit exhausts all 256 source modes, identifies their 32 distinct
affine cube maps, each represented by exactly eight of the 256 source mode
values, and checks every ordered pair of distinct maps against each of the
three face normals on a grid with \(N=2\). Thus the necessary-and-sufficient
mode criterion is that all eight selected mode values belong to one and the
same coordinate-map equivalence class (eight scalar bit-3 variants may still
differ). It also tests:
- a uniform coordinate-map control;
- a bit-3-only control (same geometry, different scalar action);
- a mixed-reflection negative control.

This is an exact characterization of the **cellwise affine geometric
interpretation** defined above. It does not prove that the original
voxel-value recursion, by itself, specifies these cell maps or that it
realizes the standard cubical subdivision operator. That identification,
the commuting de Rham refinement map, FEEC stability, and Mosco convergence
remain separate proof obligations.

## Reproducibility

From the repository root:

~~~bash
python projects/de_rham_benchmark/audits/audit_herasymov_parity_face_conformity.py --self-test
pytest -q projects/de_rham_benchmark/tests/test_herasymov_parity_face_conformity.py
~~~
