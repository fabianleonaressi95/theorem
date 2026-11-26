# T113-G — Cut-and-project symmetry: microscopic anisotropy versus rank-two isotropy

**Classification:** exact representation-theoretic theorem; illustrative finite-dimensional verification; Q6/RGS cut-and-project realization remains open pending a canonical six-dimensional embedding and acceptance window.

## 1. Scope and correction

A cut-and-project set is specified by a lattice \(\mathcal L\subset E_\parallel\oplus E_\perp\), a physical projection \(\pi_\parallel\), an internal projection \(\pi_\perp\), and an acceptance window \(W\):
\[
\Lambda=\{\pi_\parallel(\ell):\ell\in\mathcal L,\ \pi_\perp(\ell)\in W\}.
\]
The lattice dimension and the fact that the projection is irrational do **not** by themselves force a macroscopically anisotropic rank-two transport tensor. The relevant constraint is the point group of the complete cut-and-project data (including the window and any decorations/interactions), and the representation carried by the observable.

This record corrects any reading of T113-F's \(L_{Q6}\otimes I_3\) benchmark as the physical cut-and-project elastic operator. That term is an isotropic graph control only. It does not encode a six-dimensional physical/internal decomposition.

## 2. Rank-two isotropy theorem in two physical dimensions

Let \(G\subset O(2)\) be a point group and let \(D\in\mathbb R^{2\times2}\) be a real symmetric tensor satisfying
\[
R D R^T=D\qquad (R\in G).
\]
If \(G\) contains a rotation \(R_\theta\) with \(\theta\not\equiv0,\pi\pmod{2\pi}\), then
\[
\boxed{D=\lambda I_2.}
\]

**Proof.** Since \(D\) is real symmetric, choose an orthonormal eigenbasis. If its eigenvalues were distinct, its two one-dimensional eigenspaces would be the only eigendirections and would have to be preserved individually by every commuting rotation. A planar rotation other than \(0\) or \(\pi\) preserves no real one-dimensional subspace. Thus the eigenvalues coincide and \(D=\lambda I_2\). \(\square\)

In particular, a dihedral point group \(D_n\) with \(n\ge3\), or a cyclic point group \(C_n\) with \(n\ge3\), forces every invariant symmetric rank-two tensor to be isotropic.

The converse is **not** true: an isotropic tensor may occur accidentally even when the point group has no such rotation. The theorem is a sufficient symmetry condition, not an if-and-only-if classification.

For a general real (not necessarily symmetric) invariant rank-two tensor, the conclusion is instead \(D=aI+bJ\), where \(J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\). Diffusion and ordinary reciprocal conductivity tensors are taken symmetric, so the theorem applies to them.

## 3. Three-dimensional version

Let \(G\subset O(3)\) act irreducibly on \(\mathbb R^3\). Any real symmetric \(G\)-invariant rank-two tensor is \(\lambda I_3\): its eigenspaces are invariant under \(G\), and irreducibility leaves only the full space.

The proper icosahedral rotation representation on \(\mathbb R^3\) is irreducible, so its invariant symmetric rank-two tensors are isotropic. This statement does not imply that every higher-rank response tensor is isotropic. The invariant subspaces must be computed separately for the tensor representation in question.

## 4. What isotropy does and does not say

The conclusion concerns an effective, symmetric, rank-two tensor that is invariant under the **actual symmetry of the complete model**. It does not imply microscopic isotropy. Directional projected generators, local edge stars, the acceptance window, phason strain, defect cores, and higher-rank constitutive tensors can retain directional structure.

Distinguish:
1. projection geometry and projected-vector stars;
2. acceptance-window/internal-space effects;
3. material constitutive tensors and phonon–phason couplings;
4. the finite RGS tangent Hessian and its spectrum;
5. the homogenized rank-two transport tensor.

A symmetry of the point cloud alone is insufficient if the window, edge weights, interactions, boundary conditions, or defect configuration break it. Likewise, isotropy of a rank-two homogenized tensor does not imply degeneracy of every microscopic mode.

## 5. Q6/RGS repository audit and data boundary

The current canonical repository seed is the hash-checked map \(X:Q_6\to\mathbb R^3\) in `src/rgs_seed_64_reconstruction.py`, with 64 sites and SHA-256
`6a158cb30a671a5c994d8ab223e9283b57ac703808041d46e67f286126e419cf`.
T113-D records its induced signed-coordinate-permutation point group \(O_h\), and the exact obstruction that only 16 of its 48 induced permutations preserve bare Q6 adjacency.

**Repository audit finding:** the canonical source inspected for this record supplies a 64-by-3 RGS point cloud and a six-cube graph, but does not supply a canonical pair of orthogonal 6D subspaces \(E_\parallel,E_\perp\), a 6D lattice basis in those coordinates, or an acceptance window \(W\). Therefore no 6D-to-3D cut-and-project matrix, perpendicular coordinates, phason star, or projection-derived phonon–phason elastic tensor is asserted here.

In particular, do not infer the missing six-dimensional projection from the 64-by-3 RGS point cloud, the abstract Q6 adjacency, or the generic icosahedral template T113-C. The 64-site Q6 labels do not themselves define perpendicular-space coordinates.

## 6. Correct next calculation for Q6/RGS

Once the canonical embedding is supplied and fixed, define orthonormal column frames \(B_\parallel,B_\perp\in\mathbb R^{6\times3}\) with
\[
B_\parallel^TB_\parallel=B_\perp^TB_\perp=I_3,
\quad B_\parallel^TB_\perp=0,
\quad B_\parallel B_\parallel^T+B_\perp B_\perp^T=I_6.
\]
Then
\[
P_\parallel=B_\parallel^T,\qquad P_\perp=B_\perp^T,
\]
and for each declared lattice generator \(a_j\in\mathbb Z^6\), compute
\[
a_j^\parallel=P_\parallel a_j,\qquad
a_j^\perp=P_\perp a_j.
\]
The acceptance condition is \(a\!\in\!\mathcal L\) with \(P_\perp a\in W\); it must be applied before assigning physical neighbor stars. From the resulting actual point set and declared interactions, construct the phonon, phason, and mixed blocks, then compute the subgroup preserving the full data. Only after that should one test rank-two isotropy, higher-rank anisotropy, and project the derived operator into the 188D RGS tangent space.

The block elastic form
\[
\mathcal E=\frac12\int
\begin{pmatrix}\varepsilon_\parallel\\\chi_\perp\end{pmatrix}^{T}
\begin{pmatrix}C_{\parallel\parallel}&C_{\parallel\perp}\\
C_{\perp\parallel}&C_{\perp\perp}\end{pmatrix}
\begin{pmatrix}\varepsilon_\parallel\\\chi_\perp\end{pmatrix}dx
\]
is a model template until its coefficients are derived from those projected stars/interactions or independently measured. Geometric anisotropy, phason-window effects, constitutive anisotropy, and RGS spectral splitting must not be identified without that derivation.

## 7. Status

- **Proved:** the planar symmetric rank-two isotropy theorem under a rotation of order at least three; the irreducible three-dimensional version.
- **Exact repository fact:** the inspected RGS seed is 64-by-3; T113-D documents the induced \(O_h\) action and its 16/48 adjacency-preservation result.
- **Not established:** a canonical Q6 6D cut-and-project embedding/window; projection-derived phonon/phason coordinates; material elastic constants; whether the actual Q6/RGS homogenized transport tensor is isotropic; the relation of the 188D T2u sector to physical phasons.
- **T113-F interpretation:** retain \(L_{Q6}\otimes I_3\) only as an isotropic graph benchmark/control, not as the cut-and-project constitutive operator.

## References within this repository

- T113-C: generic icosahedral phonon–phason template (not Q6).
- T113-D: exact Q6/RGS induced symmetry and graph-adjacency obstruction.
- T091–T093: Frank–Burgers tensorial composition and holonomy.
- T104: Q6 cycle/cocycle and cubical holonomy distinctions.
- `src/rgs_seed_64_reconstruction.py`: canonical hash-checked 64-by-3 RGS seed.
