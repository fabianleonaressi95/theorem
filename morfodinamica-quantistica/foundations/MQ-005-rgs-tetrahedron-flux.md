# MQ-005 — RGS carrier tetrahedron and classical flux closure

**Status:** finite geometric construction and numerical audit completed; exact \(SU(2)\) representation assignment and RGS–Q6 cellular identification remain open.

## 1. Purpose

MQ-002 and MQ-003 establish the representation-theoretic four-valent intertwiner and invariant one-link gluing. MQ-005 asks whether a tetrahedral geometry can be extracted from the existing RGS carrier without assigning arbitrary face vectors or weights.

The repository already contains a hash-checked 64-site coordinate reconstruction and a separate four-point carrier tetrahedron. This module reuses that exact source and computes its face bivectors directly from the four vertices.

## 2. Source and tetrahedron

The coordinate source is **src/rgs_seed_64_reconstruction.py**. It reconstructs \(X\in\mathbb R^{64\times3}\) and checks the canonical float64 SHA-256

**6a158cb30a671a5c994d8ab223e9283b57ac703808041d46e67f286126e419cf**.

The selected carrier indices are

\[
I=(0,8,32,56).
\]

They define four points \(p_0,p_1,p_2,p_3\) and a nondegenerate oriented tetrahedron with volume

\[
V=\frac16\det[p_1-p_0,\ p_2-p_0,\ p_3-p_0]
=0.11513116875074175.
\]

The six Euclidean edge lengths and the four outward face area vectors are computed from these coordinates. No edge weight, face normal, or face area is fitted.

## 3. Classical closure theorem

For an oriented triangular face \(f=(i,j,k)\), define

\[
\mathbf A_f=\frac12(p_j-p_i)\times(p_k-p_i),
\]

and choose its sign so that it points outwards, i.e. away from the opposite tetrahedron vertex. Put

\[
A_f=\|\mathbf A_f\|,\qquad
\mathbf n_f=\frac{\mathbf A_f}{A_f}.
\]

**Theorem MQ-T005A (tetrahedral flux closure).** For every nondegenerate Euclidean tetrahedron, its four outward face area vectors satisfy

\[
\boxed{\sum_{f=1}^4 A_f\mathbf n_f
=\sum_{f=1}^4\mathbf A_f=0.}
\]

*Proof.* The oriented boundary of a tetrahedron is a closed polyhedral surface. For any constant vector \(c\), the divergence theorem applied to the constant vector field \(x\mapsto c\) gives
\[
0=\int_T \nabla\cdot c\,dV
=\int_{\partial T}c\cdot n\,dA
=c\cdot\sum_f A_f n_f.
\]
Since this holds for every \(c\in\mathbb R^3\), the vector sum vanishes. \(\square\)

Thus the RGS-derived face normals and areas give a **classical closed flux configuration**. Under a common spatial rotation \(R\in SO(3)\), every \(\mathbf A_f\) transforms to \(R\mathbf A_f\), so closure is rotation covariant.

## 4. Numerical instance

The four outward face areas, in face order \((012),(013),(023),(123)\), are

\[
(0.7311849740919621,\;
0.34359801185807737,\;
0.47567321328600487,\;
0.4720653654111676).
\]

Their area ratios relative to face \((012)\) are

\[
(1,\;0.469919410317180,\;0.650551132942427,\;0.645616885108193).
\]

The closure residual from the hash-checked coordinates is

\[
\left\|\sum_f\mathbf A_f\right\|_2
=6.36\times10^{-17}.
\]

The complete face normals, vectors, edge lengths, and provenance are stored in **results/mq005_rgs_tetrahedron_flux.json**. Reproduce with

~~~bash
python scripts/audit_mq005_rgs_tetrahedron_flux.py
python -m pytest -q tests/test_mq005_rgs_tetrahedron_flux.py
~~~

## 5. The decisive Q6 incidence obstruction

The selected carrier indices are binary Q6 labels. Their pairwise Hamming distances are

| Pair | Hamming distance | Q6 edge? |
|---|---:|---|
| \(0,8\) | 1 | yes |
| \(0,32\) | 1 | yes |
| \(0,56\) | 3 | no |
| \(8,32\) | 2 | no |
| \(8,56\) | 2 | no |
| \(32,56\) | 2 | no |

The induced Q6 graph on these four vertices has only two of the six tetrahedral edges. It is therefore **not** a \(K_4\), and this geometric tetrahedron is not a Q6 tetrahedral subcomplex. Its four triangular faces are geometric faces of the selected Euclidean tetrahedron, not Q6 2-cells.

This is not a defect in the geometric closure calculation. It is a precise obstruction to identifying this selected four-point fixture directly with a Q6 tetrahedral cell. More strongly, the entire Q6 graph is bipartite: the parity function on six-bit labels changes across every Q6 edge. Hence Q6 contains no odd cycle and in particular no triangle or (K_4). No alternative choice of four Q6 vertices can make a tetrahedron whose six edges are Q6 edges. An RGS–QLG tetrahedral incidence map therefore requires a distinct, explicitly constructed 3-complex/refinement/dual complex and a separately verified map from Q6 data; it cannot identify tetrahedral edges with the Q6 1-skeleton.

## 6. Conditional quantum interpretation

A classical flux configuration suggests, but does not by itself determine, an \(SU(2)\) spin-network intertwiner. To pass to a quantum tetrahedron one must assign admissible labels \(j_f\) and a common physical area scale \(a_0\), with an area-spectrum convention such as

\[
A_f=a_0\sqrt{j_f(j_f+1)}.
\]

The scale \(a_0\) (including the relevant physical constants and Immirzi parameter in the chosen convention) is not fixed by the present RGS coordinate seed. The four measured areas are unequal, so the equal-area \(j_f=\tfrac12\) model from MQ-002 cannot simply be assigned to these four faces. No integer/half-integer spin labels are claimed here.

Once compatible labels and a scale are independently justified, one may test a Livine–Speziale-type group-averaged coherent intertwiner
\[
|\mathcal I\rangle
=\int_{SU(2)}dg\;
\bigotimes_{f=1}^4 D^{j_f}(g)|j_f,\mathbf n_f\rangle.
\]
This is a conditional next construction, not a result of this audit. Exact quantum closure, nonvanishing of the group average, semiclassical peakedness, and shape matching require separate checks.

## 7. Evidence ledger

| Claim | Classification |
|---|---|
| Outward area-vector closure for a nondegenerate tetrahedron | Exact geometric identity |
| Selected RGS coordinates match the checked source hash | Source-verified by the reconstruction module |
| Four face areas/normals and nonzero volume | Explicit finite construction; numerically audited |
| Closure residual \(6.36\times10^{-17}\) | Numerical verification |
| Selected four vertices form a Q6 \(K_4\) | False; only two of six pairs are Q6 edges |
| Identification with Q6 2-cells or a Q6 tetrahedral subcomplex | Not established; this fixture fails the direct incidence test |
| Spin labels and physical area scale | Open |
| Exact \(SU(2)\) coherent intertwiner for this RGS tetrahedron | Open |
| RGS–QLG gluing, global shape matching, refinement and continuum limit | Open |

**Conclusion.** MQ-005 now has a genuine geometric bridge component: the archived RGS carrier supplies a nondegenerate tetrahedron with derived face fluxes satisfying closure. The same audit also prevents an invalid shortcut: the chosen four vertices do not form a tetrahedral cell of Q6. The quantum representation map must wait for a valid incidence construction and independently justified spin/area data.
