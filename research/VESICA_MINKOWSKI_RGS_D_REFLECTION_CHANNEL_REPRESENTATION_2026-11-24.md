# Vesica–Minkowski realization of the RGS half-sign involution

**Date:** 24 November 2026  
**Status:** exact finite geometric representation + numerical identification with the recovered RGS BA block  
**Scope:** this realizes the involution \(D=\operatorname{diag}(1,1,-1)\) as a reflection on three paired Vesica channels. It does **not** assert that \(K_0\) is invariant under this reflection or that the construction is the \(C_3\times C_3\) spherical extension.

## 1. The two null cones and their Vesica sections

Work in Minkowski \(\mathbb R^{2,1}\) with
\[
ds^2=-dt^2+dx^2+dy^2.
\]
Let the cone vertices be
\[
p_A=(0,0,0),\qquad p_B=(0,1,0).
\]
Their future null-cone parametrizations are
\[
X_A(r,\theta)=(r,r\cos\theta,r\sin\theta),\qquad
X_B(r,\phi)=(r,1+r\cos\phi,r\sin\phi).
\]
At \(r=1\), choose the two arcs facing the common lens:
\[
\theta\in[-\pi/3,\pi/3],\qquad
\phi\in[2\pi/3,4\pi/3].
\]
Pair the three distinguished channels by
\[
\begin{array}{c|c|c}
c & \theta_c & \phi_c\\ \hline
- & -\pi/3 & 2\pi/3\\
0 & 0 & \pi\\
+ & +\pi/3 & 4\pi/3
\end{array}
\]
and write \(a_c=X_A(1,\theta_c)\), \(b_c=X_B(1,\phi_c)\), suppressing the common time coordinate when displaying spatial positions. Explicitly,
\[
\begin{aligned}
a_-&=(1/2,-\sqrt3/2),&b_-&=(1/2,+\sqrt3/2),\\
a_0&=(1,0),&b_0&=(0,0),\\
a_+&=(1/2,+\sqrt3/2),&b_+&=(1/2,-\sqrt3/2).
\end{aligned}
\]
Every paired midpoint is the same Vesica center:
\[
\boxed{\frac{a_c+b_c}{2}=(1/2,0)\quad(c=-,0,+).}
\]
The endpoint channels have separation \(\sqrt3\), while the central channel has separation \(1\). Thus the three channels are distinct ordered pairs, not three equal-length links. All six points lie on the two null-cone sections; all three midpoints lie in the Vesica lens.

## 2. The Minkowski reflection and its three-channel representation

The ambient spatial reflection
\[
\mathscr R(t,x,y)=(t,x,-y)
\]
is a Lorentz isometry. It fixes both cone vertices, preserves both null cones and the Vesica lens, and acts on the selected arcs by
\[
\theta\mapsto-\theta,\qquad \phi\mapsto2\pi-\phi.
\]
Consequently
\[
a_-\leftrightarrow a_+,\quad b_-\leftrightarrow b_+,\quad
a_0\mapsto a_0,\quad b_0\mapsto b_0.
\]
On the ordered channel-label space with basis \((e_-,e_0,e_+)\), the reflection is the permutation
\[
P_{\rm ref}=
\begin{pmatrix}
0&0&1\\
0&1&0\\
1&0&0
\end{pmatrix}.
\]
Introduce the orthonormal reflection-adapted basis
\[
f_0=e_0,\qquad
f_+=\frac{e_-+e_+}{\sqrt2},\qquad
f_-=\frac{e_--e_+}{\sqrt2}.
\]
Then
\[
P_{\rm ref}f_0=f_0,\qquad
P_{\rm ref}f_+=f_+,\qquad
P_{\rm ref}f_-=-f_-.
\]
In the ordered basis \((f_0,f_+,f_-)\),
\[
\boxed{[P_{\rm ref}]_{(f_0,f_+,f_-)}
=D=\operatorname{diag}(1,1,-1).}
\]
This is the desired geometric meaning of the RGS half-sign involution: two reflection-even channel modes and one reflection-odd mode. It is an involution, not a threefold rotation.

## 3. Recovery of the original RGS \(BA\) half-block

The original arrays \(K_0,P_G,Z_A,Z_S\) give a six-dimensional carrier with orthonormal triplets \(J_A,J_B\). In the natural paired basis,
\[
Z_AJ_A=-\frac12J_B,\qquad Z_SJ_A=+\frac12J_B.
\]
The recovered historical channel gauge is
\[
J_B^\sharp=-J_BD.
\]
It yields
\[
\boxed{
(J_B^\sharp)^TZ_AJ_A=+\frac12D,\qquad
(J_B^\sharp)^TZ_SJ_A=-\frac12D.
}
\]
Identifying the geometric reflection-adapted channel basis \((f_0,f_+,f_-)\) with the coordinates of \(J_A\) and \(J_B^\sharp\), the original RGS BA blocks act as
\[
Z_A^{BA}=\frac12
\begin{pmatrix}1&0&0\\0&1&0\\0&0&-1\end{pmatrix},
\qquad
Z_S^{BA}=-\frac12
\begin{pmatrix}1&0&0\\0&1&0\\0&0&-1\end{pmatrix}.
\]
The coefficient \(+1/2\) is carried by the two even modes and \(-1/2\) by the odd mode. This is now a concrete geometric realization of the old half-sign block, not merely a numerical resemblance.

**Important basis qualification:** \(J_B^\sharp=-J_BD\) is a relative channel-sign gauge on the upper triplet. The ambient Lorentz reflection \(\mathscr R\) acts on both cone sections. Thus the full spacetime reflection is diagonal on the two geometric sheets, whereas the historical RGS gauge records the relative orientation convention used to express the BA coupling. Do not identify the gauge itself with a Lorentz transformation acting on only one half of a single spacetime.

## 4. Relation to the hexagrams

A hexagram is \(H=(L,U)\in\mathbb F_2^3\times\mathbb F_2^3\). The lower and upper trigrams label the two cone sectors. The six distinguished channel pairs above give a three-channel geometric carrier inside the two-sheet picture. This is a representation of the recovered three-dimensional RGS coupling sector; it is **not** a complete injective map of all 64 hexagrams to these six points.

The earlier eight-point-per-arc construction remains the set-level bridge for all 64 states: it maps each trigram to one of eight points on its corresponding Vesica arc, with a hexagram mapped to an ordered pair. The present three-channel construction is a reflection-adapted marked configuration on the same continuous arcs, but it is **not** a subset of the earlier eight-point sample: the arc midpoint lies between the two central samples of that even-sized grid. Its three paired midpoints coincide at the Vesica center, so midpoint alone does not encode the channel.

The bit/trigram labeling must be fixed consistently when embedding these three distinguished channels into the full eight-state lookup table. No unproved identification of a particular binary trigram orbit with \(c=-,0,+\) is imposed here.

## 5. What happens to \(C_3\)

The reflection exchanges the two endpoint channels and fixes the central channel. It is therefore the order-two reflection in the dihedral symmetry of a three-channel equilateral orbit, but the selected Vesica arc itself is not invariant under a nontrivial \(120^\circ\) rotation. The old planar fixed-point obstruction remains: this construction does not make the planar Vesica arc into a \(C_3\)-equivariant trigram model.

The separate \(S^2\) null-cone construction realizes \(C_3\) by two latitude triangles. Its reflection \(D\) is compatible with the usual dihedral relation \(DRD=R^{-1}\) on each full triangle. That spherical \(C_3\) extension and the present planar Vesica reflection model are related by their channel representation, but they are not the same embedded geometry.

## 6. Compatibility with \(K_0\): a proved obstruction for the recovered carrier

The recovered RGS data do not make the full carrier \(K_0\) reflection invariant under the channel involution in the natural \((J_A,J_B)\) decomposition. Nor does the half-sign block imply a symmetry of the full 188D operator. The previous audit found that the simple spectra on \(J_A,J_B\) preclude a nontrivial order-three orthogonal symmetry commuting with the corresponding \(K_0\) restrictions; the diagonal \(C_3\) also has a nonzero commutator with \(K_0\).

Accordingly, the present result is a geometric realization of the \(BA\) coupling block and its channel parity. It is not an intertwiner of the full triple \((K_0,Z_A,Z_S)\), and it does not establish a Lorentzian dynamics or a continuum limit.

## 7. Exact claims and status

| Claim | Status |
|---|---|
| The six selected points lie on the two unit null-cone sections | Exact |
| Their three paired midpoints all equal the Vesica center | Exact |
| \((t,x,y)\mapsto(t,x,-y)\) is a Lorentz isometry preserving both cones and the Vesica | Exact |
| Its three-channel representation is conjugate to \(\operatorname{diag}(1,1,-1)\) | Exact |
| The original RGS \(BA\) blocks equal \(\pm D/2\) in the recovered channel gauge | Numerically verified from stored arrays |
| The entire 188D RGS triple is intertwined with the Vesica reflection | Not claimed |
| The three channels encode all 64 hexagrams | Not claimed |
| The planar Vesica model is \(C_3\)-equivariant | False for the selected arcs |

The deterministic coordinate check is in audits/audit_vesica_minkowski_D_reflection.py; the underlying original-array reconstruction is in audits/reconstruct_rgs_half_carrier_basis.py.


### Discrete eight-sample check: what the reflection does to the 64-state bridge

In the earlier eight-point sampling
\[
\theta_k=-\pi/3+\frac{2k\pi}{21},\qquad
\phi_k=2\pi/3+\frac{2k\pi}{21},\qquad k=0,\ldots,7,
\]
the same ambient reflection sends \(k\mapsto7-k\) on each sheet. Since there are eight samples, this permutation has no fixed sample and decomposes into four transpositions. Its permutation representation on the trigram sample space therefore has \(+1\) and \(-1\) eigenspaces of dimensions \(4\) and \(4\), respectively. On the 64 hexagrams the single ambient Minkowski reflection acts diagonally on both factors. One can define an abstract independent (\mathbb Z_2\times\mathbb Z_2) action on the product of the two label sets, but its two generators are not both realized by that one ambient spacetime reflection.

This is not the three-dimensional \((2,1)\) parity representation above. The latter is a separately marked three-channel configuration on the continuous Vesica arcs, chosen to match the RGS carrier dimension. A linear compression/intertwiner from the eight-state trigram representation to this three-channel carrier has not yet been specified. In particular, no three of the eight equally spaced samples are being silently identified with \((-,0,+)\).
