# Stone–Wales 90° rotation, fullerene growth, and the anisotropic-vesica bridge

**Date:** 2026-11-23  
**Status:** mathematical definitions and graph invariants are exact; the proposed cross-model map to Krist-All/Q6 and the molecular density tensor is an open, falsifiable construction. No physical equivalence is claimed.

## 1. The 90° operation: precise meaning

The Stone–Wales (SW) rearrangement is a local rotation by 90° of a C–C bond (equivalently, of the central C2 unit in the pyracylene patch), followed by reconnection of the four surrounding carbon sites. It is an isomerization of a fixed carbon cage:

- the vertex set is unchanged: \(|V'|=|V|\);
- the edge count is unchanged: \(|E'|=|E|\);
- for a trivalent fullerene graph, every carbon remains degree 3;
- the local face/ring incidence changes, while the rest of the cage is unchanged.

The familiar graphene ideal-lattice case is the 6/6 rotation, which produces a local 5–7–7–5 defect. On a fullerene, the relevant local patch can be a 5/6 pyracylene-type environment; one must inspect the actual four-ring neighbourhood before assigning a 5–7–7–5 label. It is incorrect to apply that ring sequence indiscriminately to every C60 Stone–Wales event.

A useful graph description is a degree-preserving edge switch (2-switch) on the four boundary vertices of the chosen patch. It changes adjacency, not the number of carbon atoms. The geometrical 90° is the local bond-rotation pathway; the graph operation records the resulting connectivity.

## 2. Stone–Wales is not C60 → C64 growth

For a closed trivalent fullerene graph, \(3V=2E\) and Euler's relation is \(V-E+F=2\). If all faces are pentagons or hexagons, the face-size sum gives \(5p+6h=2E\), with \(p+h=F\). These equations imply \(p=12\) for every such fullerene.

| Cage | Vertices \(V\) | Edges \(E\) | Faces \(F\) | Pentagons \(p\) | Hexagons \(h\) |
|---|---:|---:|---:|---:|---:|
| C60 | 60 | 90 | 32 | 12 | 20 |
| C64 | 64 | 96 | 34 | 12 | 22 |

Thus C60 → C64 requires \(\Delta V=4\), \(\Delta E=6\), and \(\Delta F=2\). It cannot be achieved by a Stone–Wales rearrangement, which preserves \(V\) and \(E\). A C60-to-C64 pathway needs a separate growth/insertion/coalescence mechanism and an explicit atom-and-bond map. Stone–Wales rearrangements may occur before or after growth, but are not the growth step itself.

This distinction also prevents a common confusion between (i) a fullerene isomerization at fixed carbon count, (ii) an insertion/growth operation changing carbon count, and (iii) a continuous geometric deformation of an embedded cage.

## 3. Chain-complex formulation of the 90° reconnection

Represent the initial and final cage cellulations by cellular chain complexes
\[
C_2\xrightarrow{\partial_2}C_1\xrightarrow{\partial_1}C_0,
\qquad
C'_2\xrightarrow{\partial'_2}C'_1\xrightarrow{\partial'_1}C'_0.
\]
A proposed correspondence between cells is represented by maps \(S_i:C_i\to C'_i\). If the local reconnection admits a cellular chain map, it must satisfy
\[
\boxed{\partial'_1S_1=S_0\partial_1,\qquad
\partial'_2S_2=S_1\partial_2.}
\]
These are test conditions, not identities that follow merely from drawing a 90° arrow. In particular, because the face boundaries are changed by the SW move, \(S_2\) must be constructed from the actual before/after face lists. If no bijective face correspondence exists, use a local chain correspondence or a common refinement and state it explicitly.

The same discipline applies to the existing Kathara–Q6 maps. The archived dimensions are
\[
R_0\in\mathbb Z^{64\times12},\quad
R_1\in\mathbb Z^{192\times21},\quad
R_2\in\mathbb Z^{240\times10},
\]
with the recorded boundary-compatibility checks
\[
B_1^{Q6}R_1=R_0B_1^K,\qquad
B_2^{Q6}R_2=R_1B_2^K,
\]
and \(\operatorname{rank}R_2=10\) in T116. Those facts establish the recorded Kathara–Q6 chain-map layer; they do **not** establish a fullerene-to-Q6 map.

A genuine bridge would require explicit fullerene maps \(S_i\), explicit maps \(T_i\) from the fullerene complex to the Kathara complex, and a verified commutative relation between the SW move and the induced Q6/Kathara action. The shorthand \(R'S_{90}=Q_{90}R\) is retained only as a target diagram, not as a proven identity.

## 4. Relation to the vesica anisotropy tensor

For a planar density projection \(\rho_\Pi(q)\) on a fixed overlap lens \(\Omega_2\), define
\[
\bar q=\frac{\int_{\Omega_2}q\rho_\Pi(q)\,d^2q}
{\int_{\Omega_2}\rho_\Pi(q)\,d^2q},\qquad
Q=\frac{\int_{\Omega_2}(q-\bar q)(q-\bar q)^T\rho_\Pi(q)\,d^2q}
{\int_{\Omega_2}\rho_\Pi(q)\,d^2q}.
\]
For a rigid planar rotation \(U(\alpha)\), covariance transforms as
\[
Q' = U(\alpha)Q U(\alpha)^T.
\]
At \(\alpha=90^\circ\),
\[
U_{90}=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
The eigenvalues and scalar anisotropy
\[
\mathcal A_Q=\frac{\lambda_+-\lambda_-}{\lambda_++\lambda_-}
\]
are invariant under this rigid rotation; the principal-axis angle changes by 90° (modulo 180°). This is an exact tensor identity.

But Stone–Wales is not a rigid rotation of the whole electron density: it is a local change in graph connectivity and in the relaxed atomic/electronic structure. Therefore the physically meaningful test is to compute the relaxed density before and after the SW move, project both using the same plane and overlap-region convention, and compare \(Q_{\rm before}\), \(Q_{\rm after}\), their eigenvalues, principal axes, and centroid. A change in \(Q\) is a computed response of the relaxed structure, not a consequence of the angle 90° alone.

For the H2+ molecular-distance scan, the existing proposed \(Q(R)\) remains a separate two-centre density observable. The fullerene calculation can test whether the same tensorial descriptors are useful across geometries; it cannot validate H2+ values without the archived Ritz coefficients or densities.

## 5. Falsifiable bridge programme

The minimal reproducible sequence is:

1. Specify the exact C60 isomer, atom numbering, rotated bond, and four-site patch.
2. Generate the post-SW graph by the 90° bond-reconnection rule; verify \(V,E\), degree sequence, planarity, face sizes, and Euler characteristic.
3. Relax both cages with the same electronic-structure method, charge, spin, and convergence settings; record energy difference and coordinates.
4. Construct the before/after cellular boundary matrices and test the chain-map equations, or explicitly document why a common refinement is needed.
5. Compute density covariance tensors with a fixed projection and fixed region-selection rule. Do not tune the lens after seeing the result.
6. Only then seek a map to Krist-All/Kathara/Q6. Test commutativity and rank numerically/exactly; do not infer it from visual similarity.
7. Treat C60 → C64 as a separate graph-growth problem with its own insertion map and invariants.

### Evidence classification

| Statement | Status |
|---|---|
| SW is a 90° local C–C bond rotation/rearrangement | Established literature |
| SW preserves the number of carbon vertices and bonds | Exact graph property of the rearrangement |
| 6/6 graphene SW gives the 5–7–7–5 defect | Established standard case |
| Every fullerene SW patch has the same 5–7–7–5 ring sequence | False; local ring environment matters |
| C60 → C64 is a single SW move | False by vertex-count invariant |
| A relaxed SW cage has a changed density covariance tensor | Testable numerical question; not assumed |
| A chain map intertwines SW and the existing Kathara–Q6 maps | Open |
| The fullerene and H2+ vesica tensors obey one universal law | Open; requires cross-system validation |

## References

1. Terrones, H. et al. (2016), “The Stone–Wales transformation: from fullerenes to graphite, from radiation damage to heat capacity,” *Philosophical Transactions of the Royal Society A* **374**, 20150317. DOI: [10.1098/rsta.2015.0317](https://doi.org/10.1098/rsta.2015.0317).
2. “Chlorination-Promoted Skeletal Transformations of Fullerenes,” *Accounts of Chemical Research* (2019). DOI: [10.1021/acs.accounts.9b00175](https://doi.org/10.1021/acs.accounts.9b00175).
3. “The topology of fullerenes,” *WIREs Computational Molecular Science* (2015). DOI: [10.1002/wcms.1207](https://doi.org/10.1002/wcms.1207).

**Conclusion.** The 90° Stone–Wales event is now treated as a local, atom-conserving graph reconnection; C60 → C64 is a distinct growth operation. The common language with vesica anisotropy is the covariance tensor and, potentially, a verified chain-map diagram. The physical bridge remains open until the atomistic relaxation, density calculation, and chain-map tests are performed.

## 6. Executed C60 graph audit (2026-11-26)

The implementation and output are recorded in [C60_STONE_WALES_90_DEGREE_GRAPH_AUDIT.md](../docs/C60_STONE_WALES_90_DEGREE_GRAPH_AUDIT.md), with script [audit_c60_stone_wales.py](../scripts/audit_c60_stone_wales.py) and test [test_c60_stone_wales.py](../tests/test_c60_stone_wales.py).

The correct construction is performed in the **dual triangulation**: flip a dual edge joining two degree-6 vertices whose two opposite vertices have degree 5. The corresponding direct graph is reconstructed as the dual of the flipped triangulation. The run found 30 labelled admissible flips. For every retained candidate, the direct graph has (V,E,F;p,h)=(60,90,32;12,20), all carbon degrees 3, and Euler characteristic 2.

For the selected representative, the direct graph removes bonds (5,37) and (13,36), and adds (5,36) and (13,37). The exact integer chain maps satisfy
\[
B'_1S_1=B_1,\qquad B'_2S_2=S_1B_2,
\]
with rank(S1)=90 and rank(S2)=31. This verifies a cellular chain correspondence for the chosen path and filling maps. It does **not** construct an intertwiner with Kathara/Q6.

The paired RDKit MMFF94s relaxations give reported model energies 945.1698747 and 963.0943689 (difference +17.9244942 in the same force-field units). The global carbon-coordinate covariance anisotropy changes from 0.0438637 to 0.1381264; the local-patch proxy changes from 0.8911495 to 0.8997506. These are geometric nuclear-coordinate descriptors for one empirical force-field model, not electronic-density moments, DFT energies, or a reaction barrier. The nonzero final gradient norms (0.22199 and 0.21343) are retained as a convergence caveat.

### Updated classification

- C60 dual Stone–Wales graph reconstruction and 30-flip enumeration: numerically verified.
- Chain-map boundary identities for the selected direct-graph correspondence: exact integer verification.
- MMFF94s nuclear-coordinate covariance response: numerically verified for one selected representative.
- Electronic-density anisotropy and the vesica (Q)-tensor: still open.
- Fullerene-to-Kathara/Q6 chain-map intertwining: still open.
- Universal fullerene/molecular response law: still open.
