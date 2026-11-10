# Quaternionic lift of the RGS–PRISM football tangent space

## Purpose

The quaternion is the bridge between a local three-component geometric
triplet and rotations. It is not merely a relabelling of three numbers.
At each shell node, a local orthonormal frame is encoded by a unit
quaternion (q_i\in SU(2)\), and a pure-imaginary quaternion
(p=(0,v_1,v_2,v_3)\) is transported by

\[
p_{global}=q_i p q_i^{-1},\qquad q_i\sim -q_i.
\]

This is the standard double cover (SU(2)\to SO(3)\).

## Tangent projection

For each node, the averaged incident-face normal is (n_i\). A right-handed
frame (R_i=(e_{1i},e_{2i},n_i)\) is built and encoded by (q_i\).
The local tangent displacement has two components; its ambient embedding is

\[
T_i=\begin{pmatrix}e_{1i}&e_{2i}\end{pmatrix},\qquad
P_i=T_iT_i^T=I-n_in_i^T.
\]

Assemble (T=\operatorname{diag}(T_i)\in\mathbb R^{3N\times2N}\).
For the 92-node football mesh, (T\) is (276\times184\), with
(T^TT=I\). The reduced tangent stiffness is the Galerkin pullback

\[
K_{tan}=T^T K T\in\mathbb R^{184\times184}.
\]

The quaternion frames carry the orientation of each local tangent plane;
the pure-imaginary quaternion carries a 3-vector; its tangent restriction
is the span of the local \(\mathbf i,\mathbf j\) axes (zero local
\(\mathbf k\) component).

## Triplets and spectral tests

The code diagonalises the symmetric (K_{tan}\) and groups adjacent
eigenvalues using a declared relative-gap tolerance. A cluster of exactly
three is labelled **candidate_triplet**, not a proven irreducible
representation. To call it a symmetry-protected triplet, one must still
construct the relevant group action on the shell, test commutators
\([K_{tan},D(g)]\), compute projectors/characters, and check stability
under mesh refinement and material perturbations.

## Important distinctions

- The shell has 92 nodes, hence 276 ambient and 184 node-wise tangent DOF.
- The existing RGS tangent space has 188 DOF. There is no canonical
  188-to-184 identification; comparison requires an explicit geometric
  interpolation/restriction map and a principal-angle or intertwiner audit.
- The soccer-ball shell has icosahedral (I_h) geometry, whereas the
  cube/sphere fields carry cubic structure. They are independent inputs;
  no full cubic symmetry is imposed on the football mesh.
- A unit quaternion represents a frame rotation, not an independent physical
  field unless a constitutive or dynamical law for that field is specified.
- The present shell solver is linearised. The quaternion lift is a
  kinematic/geometric layer, not yet a nonlinear Cosserat/micropolar shell.

## Reproduction

```bash
python -m pytest -q tests/test_football_quaternion_tangent.py
```

Evidence status: quaternion algebra and tangent-frame construction are
exact identities implemented and tested numerically; candidate triplet
clusters are numerical observations only; RGS 188-DOF matching and
physical quaternion dynamics remain open.
