# Q6–IVM–PSU and spatial spinor audit

**Date:** 27 November 2026  
**Status:** finite construction and audit; no physical PSU or fermion claim.

This dossier records the implementation corresponding to T146. The carrier is the six-bit I Ching state set with Hamming-one Q6 edges (64 vertices, 192 edges, 240 squares). The golden signed-vector realization is
\[
F(b)=\sum_{i=1}^6(-1)^{b_i}n_i,
\]
where the six \(n_i\) are the normalized icosahedral axes in T146. The complement operation gives 32 exact antipodal pairs; numerical coordinate checks give four radial shells with counts 12, 20, 20, 12.

The minimum separation of the 64 points is 1.125554844510479 in the chosen dimensionless normalization. For PSU spheres of radius \(\ell_P/2\), the centre separation must be at least \(\ell_P\). Thus a uniformly scaled point set \(P_b=\lambda F(b)\) must satisfy \(\lambda\ge0.8884507093343064\ell_P\). This is only a non-overlap bound; no packing fraction or space filling follows.

## Spinor lift

Each radial unit vector \(u_b=F(b)/\|F(b)\|\) is transported along a Q6 edge by the shortest spatial rotation. Its canonical unit-quaternion lift \(s_{gh}\) is represented on \(\mathbb C^2\) by
\[
\mathcal U_{gh}=s^0_{gh}I_2-i\mathbf s_{gh}\cdot\boldsymbol\sigma.
\]
The reverse edge is the inverse lift. Face products are computed in path order and projected back to SO(3), with all 240 Q6 squares included. The expected spin-1/2 behaviour is \(U(2\pi)=-I\) and \(U(4\pi)=I\).

This is a spatial Spin(3) link construction. It is not a Lorentzian Spin(1,3) bundle, a Dirac operator, or a fermionic matter theory. The latter requires the existing 4D tetrad and an independently specified Lorentz spin connection.

## IVM / 64 tetrahedra: no false identification

Fuller's original vector equilibrium is the cuboctahedron (12 vertices, 24 edges, 8 triangular and 6 square faces). The IVM is a tetrahedron–octahedron space-filling construction. ISF/Haramein presentations describe a distinct 64-tetrahedron grid made from eight star tetrahedra. Neither object is identical by definition to the 64 Q6 golden points.

The 64-tetrahedron construction does not yet have a coordinate/incidence data file in the inspected repository. Therefore the script reports the Q6-to-64-TG equivariant matching as NOT TESTED. The next comparison needs the 64 tetrahedron centroids or vertices, the cell incidence/adjacency, and the symmetry generators. Only then can we compare pair-distance spectra, adjacency spectra, stabilizers and equivariant maps without fitting arbitrary weights.

## Literature boundary

Haramein's 2013 paper defines the PSU as a spherical Planck unit with radius half the Planck length. The 64-tetrahedron grid is presented separately in ISF material. The cited PSU paper does not provide a derivation of the 64-tetrahedron grid from the PSU definition. The proposed bridge in T146 is therefore a research comparison, not a result already established by that paper.

## Reproduction

~~~bash
python scripts/audit_q6_ivm_psu_spinor.py
python -m unittest discover -s tests -p "test_q6_ivm_psu_spinor.py" -v
~~~
