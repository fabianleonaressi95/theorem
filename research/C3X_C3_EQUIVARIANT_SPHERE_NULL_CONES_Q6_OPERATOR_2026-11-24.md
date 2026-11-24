# C3 × C3 equivariance: an S² null-cone extension and an invariant Q6 operator

**Date:** 24 November 2026  
**Status:** exact equivariant embedding into two 3+1D null-cone sections and exact Reynolds-averaged graph operator; identification with the previous 2+1D Vesica lens remains unproved and is not claimed.

This note advances [NEEDHAM_C3_TRIGRAM_Q6_VESICA_EQUIVARIANCE_2026-11-24.md](NEEDHAM_C3_TRIGRAM_Q6_VESICA_EQUIVARIANCE_2026-11-24.md). It addresses the next mathematical question: can the finite action on trigrams be represented geometrically without the fixed-point obstruction encountered on a single planar circle, and can a Q6 operator be made invariant under the independent actions?

## 1. The finite action to be represented

Use the already defined map
\[
T(a,b,c)=(b,a+b,c),\qquad (a,b,c)\in\mathbb F_2^3.
\]
It has order three, with fixed states 000 and 001 and cycles
\[
010\to110\to100\to010,\qquad
011\to111\to101\to011.
\]
The product group \(G=C_3\times C_3\) acts independently on \(H=(L,U)\in\mathbb F_2^3\times\mathbb F_2^3\). Its 64-state orbit distribution is
\[
4\text{ orbits of size }1,\quad
8\text{ orbits of size }3,\quad
4\text{ orbits of size }9.
\]

## 2. An explicit equivariant embedding into the unit sphere

The planar obstruction disappears if the target has a two-dimensional fixed axis and two distinct latitude circles. Define \(p:\mathbb F_2^3\to S^2\subset\mathbb R^3\) as follows:
\[
p(000)=(0,0,1),\qquad p(001)=(0,0,-1).
\]
For the first three-cycle, set
\[
\begin{aligned}
p(010)&=(\sqrt3/2,0,1/2),\\
p(110)&=(-\sqrt3/4,3/4,1/2),\\
p(100)&=(-\sqrt3/4,-3/4,1/2).
\end{aligned}
\]
For the second three-cycle, use the same three azimuths at the opposite latitude:
\[
\begin{aligned}
p(011)&=(\sqrt3/2,0,-1/2),\\
p(111)&=(-\sqrt3/4,3/4,-1/2),\\
p(101)&=(-\sqrt3/4,-3/4,-1/2).
\end{aligned}
\]
All eight points are distinct and have unit norm. Let \(R\) be rotation by \(2\pi/3\) around the z-axis:
\[
R(x,y,z)=\left(-\frac{x}{2}-\frac{\sqrt3y}{2},
\frac{\sqrt3x}{2}-\frac y2,z\right).
\]
Then direct substitution gives the exact intertwining identity
\[
\boxed{p(Tb)=R\,p(b)\quad\text{for every }b\in\mathbb F_2^3.}
\]
The two fixed trigrams map to the two poles, both fixed by the rotation; the two nontrivial orbits map to equilateral triangles on the latitudes \(z=\pm1/2\). This is an injective, isometric-action realization of the finite \(C_3\)-set on \(S^2\).

## 3. Two null-cone sections in Minkowski 3+1

Use Minkowski spacetime with metric
\[
ds^2=-dt^2+dx^2+dy^2+dz^2.
\]
Take two cone vertices on the common rotation axis:
\[
P_-=(0,0,0,0),\qquad P_+=(0,0,0,1).
\]
Their future null cones have unit-radius sections
\[
X_-(1,u)=(1,u),\qquad
X_+(1,u)=(1,e_z+u),\qquad u\in S^2.
\]
Because \(|u|=1\), each point is null-separated from its corresponding vertex. The z-axis rotation fixes both vertices and acts isometrically on each spherical section.

For a hexagram \(H=(L,U)\), define the ordered two-sheet embedding
\[
\widehat\Phi(H)=\big(X_-(1,p(L)),X_+(1,p(U))\big).
\]
It is injective. The independent action \((T^i,T^j)\) is intertwined with the independent pair of rotations \((R^i,R^j)\):
\[
\widehat\Phi((T^i,T^j)H)
=(R^i,R^j)\widehat\Phi(H).
\]
The product metric on the two sphere sections is preserved by \(C_3\times C_3\).

**Geometric scope:** this is an exact extension to two 3+1-dimensional null-cone sections. It is not the previous 2+1-dimensional construction with two 120-degree Vesica boundary arcs. In particular, the eight points now occupy two latitude triangles and the two poles on \(S^2\); they have not been shown to lie in the old planar Vesica lens. The construction resolves the equivariance problem by enlarging the section, not by retroactively making the old eight arc samples equivariant.

## 4. Independent rotations and the inter-sheet distance

The ordinary cross-sheet squared distance
\[
D^2(L,U)=|e_z+p(U)-p(L)|^2
\]
is not invariant under independent rotations of the two sheets: it depends on their relative azimuth. It is invariant under the diagonal subgroup \((R^k,R^k)\), but not under all of \(C_3\times C_3\).

There is, however, a canonical finite-group invariant obtained by Reynolds averaging:
\[
\overline D^{\,2}(L,U)
=\frac19\sum_{i,j=0}^2
|e_z+R^j p(U)-R^i p(L)|^2.
\]
Writing \(z_L\) and \(z_U\) for the third coordinates of the two sphere points, the transverse terms cancel and the sum reduces exactly to
\[
\boxed{\overline D^{\,2}
=3+2z_U-2z_L-2z_Uz_L.}
\]
This is invariant under independent \(C_3\) actions. It is a legitimate invariant coupling observable, but it deliberately discards relative azimuthal phase. It is not the original Vesica separation functional and should not be identified with a physical interaction without an independent action principle and calibration.

## 5. Why the ordinary Q6 cube Laplacian is not C3 × C3 invariant

The standard six-cube graph is
\[
Q_6=Q_3\square Q_3,
\]
with 192 edges. But \(T\in GL(3,2)\) is not an automorphism of the Hamming cube \(Q_3\): for example,
\[
000\sim100\quad\text{in }Q_3,
\]
while
\[
T(000)=000,\qquad T(100)=010,
\]
and 000 and 010 are not adjacent in \(Q_3\). Therefore the standard unweighted Q6 Laplacian does not commute with this \(C_3\times C_3\) action.

This distinction matters: preserving the trigram factor boundary is not the same as preserving the Hamming adjacency or its Laplacian.

## 6. The Reynolds-averaged Q6 operator

Let \(L_3\) be the ordinary combinatorial Laplacian of \(Q_3\), and let \(P_T\) be the permutation matrix induced by \(T\) on its eight vertices. Define
\[
\overline L_3
=\frac13\sum_{k=0}^2
(P_T^k)^\mathsf T L_3 P_T^k.
\]
Then
\[
\overline L_3\succeq0,\qquad
P_T^\mathsf T\overline L_3P_T=\overline L_3.
\]
It is therefore a positive-semidefinite, exactly \(C_3\)-invariant graph Laplacian. Its off-diagonal conductance on an unordered pair is the number of the three conjugated cube edge sets containing that pair, divided by three.

Exact enumeration gives:
- the original \(Q_3\) has 12 edges;
- the union of its three conjugate edge sets has 16 distinct edges;
- 12 of those pairs occur with multiplicity 2 (conductance \(2/3\));
- 4 occur with multiplicity 3 (conductance \(1\)).

The invariant operator on the 64 states is the Cartesian-product sum
\[
\boxed{
\overline L_6
=\overline L_3\otimes I_8+I_8\otimes\overline L_3.
}
\]
It is positive semidefinite and commutes with the independent \(C_3\times C_3\) permutation action. Its weighted support has
\[
16\cdot8+8\cdot16=\boxed{256}
\]
undirected edges, rather than the 192 edges of the standard Q6 cube. It is a new invariant operator on the same 64 states, not the standard Q6 Laplacian. Its connectedness follows because every original cube edge remains in the averaged support with positive conductance.

For a real-valued field \(f\) on the 64 states, the corresponding energy is
\[
\mathcal E_{C_3\times C_3}(f)
=\frac12 f^\mathsf T\overline L_6 f\ge0.
\]
This gives a well-defined spectral object for comparison with the existing Q6/RGS operators. No continuum limit, physical Hamiltonian, or identification with the old Vesica-weighted operator is claimed.

## 7. Reproducible audit and classification

The standard-library audit is in [audit_c3x_c3_two_sheet_equivariance.py](../audits/audit_c3x_c3_two_sheet_equivariance.py); its machine-readable output is [c3x_c3_two_sheet_equivariance_audit.json](../results/json/c3x_c3_two_sheet_equivariance_audit.json). Run:

    python audits/audit_c3x_c3_two_sheet_equivariance.py

| Claim | Status |
|---|---|
| Explicit \(C_3\)-equivariant injection of 8 trigrams into \(S^2\) | **Proved by coordinates** |
| Two 3+1D null-cone sections and 64-state product injection | **Proved by construction** |
| Product sphere metric invariant under \(C_3\times C_3\) | **Proved** |
| Reynolds-averaged cross-sheet observable invariant | **Proved** |
| Standard Q6 Laplacian invariant under this action | **False** |
| Reynolds-averaged 64-state operator invariant and PSD | **Proved** |
| Identification with the previous 2+1D Vesica lens | **Open / not claimed** |
| Physical interaction or continuum/fractal interpretation | **Open / not established** |

## 8. Next test

The next mathematically meaningful comparison is spectral, not rhetorical: compute the exact spectrum and eigenspace decomposition of \(\overline L_6\), compare it with the standard Q6 Laplacian and the previously recorded RGS/QLG operators, and test whether the invariant eigenspaces align with the \(C_3\times C_3\) representation sectors. Any such alignment must be reported as a numerical or exact finite-dimensional result, not as evidence of a physical continuum theory.


## 9. Exact spectrum and C3-character decomposition

The averaged factor matrix has diagonal entries 3; its off-diagonal conductances are 1 on four pairs and 2/3 on twelve pairs. Its characteristic polynomial factors exactly as
\[
\boxed{
\chi_{\overline L_3}(\lambda)
=\lambda(\lambda-2)(3\lambda-8)^3(3\lambda-14)^3/729.
}
\]
Hence
\[
\operatorname{spec}(\overline L_3)
=\{0^{(1)},2^{(1)},(8/3)^{(3)},(14/3)^{(3)}\}.
\]
Because \(\overline L_3\) commutes with the order-three permutation, its eigenspaces split into the three complex characters \(1,\omega,\omega^2\). The eigenspaces at 0 and 2 are trivial-character lines; each of the eigenspaces at 8/3 and 14/3 contains one copy of each of the three characters.

The product spectrum is the pairwise sum of factor eigenvalues. The exact eigenvalues and multiplicities are:
\[
\begin{array}{c|rrrrrrrrr}
\lambda&0&2&8/3&4&14/3&16/3&20/3&22/3&28/3\\
\hline
m&1&2&6&1&12&9&6&18&9
\end{array}
\]
The multiplicities sum to 64. In particular, the invariant operator has a one-dimensional kernel (the constants) and spectral gap exactly 2. This matches the numerical value of the standard Q6 gap, but the operators are different and their remaining spectra are not the same. The equality of the first positive eigenvalue is a finite exact coincidence of these two operators, not evidence of continuum equivalence.

The factor character decomposition also gives the product representation sectors: the nine characters of \(C_3\times C_3\) are obtained by pairing the three characters from each factor. The spectrum above is the exact sum spectrum across those sectors; no physical interpretation is assigned to the character labels.

## 10. Next test

The next mathematically meaningful comparison is to compute the exact intertwining maps and eigenspace overlaps with the previously stored RGS/QLG operators, after fixing a common ordering of the 64 states. In particular, test whether the new 2-eigenspace or the nontrivial character sectors have a canonical image under the established Q6 tangent/Möbius projectors. This requires the actual stored matrices and must not be inferred from matching eigenvalues alone.


**Action-space qualification:** the independent rotations R^i and R^j act on the two factors of the product configuration space separately. They are not a single common Lorentz transformation of one ambient Minkowski spacetime acting differently on two points. The construction is an equivariant product of two cone-section models; the cross-sheet observable is then defined on that product and Reynolds-averaged as above.


## 11. The recurring one-half: an exact geometric value and a separate RGS datum

The spherical coordinates contain a structurally forced half:
[
z=pmrac12,qquad ho=sqrt{1-z^2}=rac{sqrt3}{2}.
]
These are not arbitrary fitted latitudes. A 120-degree orbit on the unit circle has chord length (sqrt3); on the unit sphere, choosing the orbit planes at height (z=pm1/2) gives horizontal radius \\(\\sqrt3/2\\) and triangle side length \\(3/2\\) for the two equilateral triangles used above. Equivalently, their colatitudes are (pi/3) and (2pi/3), so the axial projection is (cos(pi/3)=1/2). The same (1/2) is the familiar midpoint coordinate of the unit-separation two-vertex Vesica/Minkowski setup, but the midpoint and the spherical latitude are different geometric objects.

There is also a prior RGS datum that must be compared rather than silently identified with this coordinate. In the 6 October 2026 stepping-operator calculation, the isolated rank-three block was reported as
[
Z_A^{BA}=rac12operatorname{diag}(1,1,-1),qquad
Z_S^{BA}=-Z_A^{BA},
]
with (z_A=(1/2,1/2,-1/2)), supported only on the (J_Aleftrightarrow J_B) block ((Delta k=3)); the reported associated changes were (Delta K_0=0.3) and (Delta N=3). A related spectral involution was recorded as
[
mathcal I_A=P_{0.5}+P_{0.6}-P_{0.7},qquad
mathcal I_A|_{J_A}=operatorname{diag}(1,1,-1).
]
The original matrix artifacts were named `Z_A.npy`, `Z_S.npy`, `K0.npy`, and `P_G.npy`, with report `K0_STEPPING_OPERATORS_REPORT.json`.

The shared occurrence of the coefficient (1/2) and the sign pattern ((+,+,-)) is a concrete comparison target, not yet an identity: the spherical (z)-coordinate is a geometric embedding coordinate, whereas (Z_A^{BA}) is a block of an RGS stepping operator. To establish a bridge, one must recover the original arrays, identify the same ordered three-dimensional subspace and basis convention, and test an explicit intertwiner (U) satisfying the appropriate relation (for example (U Z_A^{BA} U^{-1}) against the relevant coordinate or projected operator). A matching diagonal pattern alone is insufficient.

The next audit should therefore report separately: (i) the exact (1/2) geometry of the two latitude triangles; (ii) the old RGS block and involution; (iii) whether the RGS block embeds into a (C_3)-representation sector or a canonical subspace of (overline L_6). Until the original matrices and basis maps are available, item (iii) remains open.
