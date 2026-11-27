# T146 — Q6–IVM–PSU: golden 64-state carrier, tetrahedral comparison and spinorial lift

**Classification:** finite geometric construction and numerical audit; Q6-to-64-tetrahedron identification is open; PSU interpretation is a model hypothesis; spatial SU(2) edge lift is numerically audited.  
**Dependencies:** Q6/Kirchhoff carrier; T063 (quaternionic SU(2) to SO(3) double cover); T129 (golden 6D cut-and-project frame); RGS–Q6 static coframe and Cartan link audits.

## 1. The 64-state carrier is fixed combinatorially

Let
\[
H=\{0,1\}^{6},\qquad |H|=64,
\]
with adjacency given by a single bit flip. This is the six-cube graph Q6, with 64 vertices, 192 undirected edges, degree 6 and 240 square faces. The 64 labels are the six-line binary hexagrams; the Kirchhoff operator is the unweighted graph Laplacian. This combinatorial origin is retained: the 64 count is not fitted to a tetrahedral diagram.

## 2. Golden signed-vector realization

Set
\[
\phi=\frac{1+\sqrt5}{2},
\]
and take the six normalized icosahedral axes
\[
\begin{aligned}
n_1&=\frac{(0,1,\phi)}{\sqrt{1+\phi^2}},&
n_2&=\frac{(0,1,-\phi)}{\sqrt{1+\phi^2}},\\
n_3&=\frac{(1,\phi,0)}{\sqrt{1+\phi^2}},&
n_4&=\frac{(1,-\phi,0)}{\sqrt{1+\phi^2}},\\
n_5&=\frac{(\phi,0,1)}{\sqrt{1+\phi^2}},&
n_6&=\frac{(\phi,0,-1)}{\sqrt{1+\phi^2}}.
\end{aligned}
\]
For each hexagram \(b=(b_1,\ldots,b_6)\), define
\[
F(b)=\sum_{i=1}^{6}(-1)^{b_i}n_i,\qquad
\widehat F(b)=\frac{F(b)}{\|F(b)\|}.
\]
The complement involution gives the exact identity
\[
F(1-b)=-F(b),
\]
hence 32 antipodal pairs. The finite audit checks that all 64 vectors are distinct and recovers four radial shells with multiplicities \(12+20+20+12\). A Q6 edge flips one sign, so its unscaled Euclidean chord has length exactly 2.

This signed-vector construction is not an unrelated golden point cloud: it is exactly the physical projection already defined in T129. With low-bit-first indexing and the fixed relabelling mask \(53=1+4+16+32\),
\[
\boxed{
P_\parallel\left(b-\frac12\mathbf1\right)
=\frac{1}{2\sqrt2}F_\phi(b\oplus53).
}
\]
The same identity holds in internal space for the algebraic conjugate \(\phi_*=(1-\sqrt5)/2\):
\[
\boxed{
P_\perp\left(b-\frac12\mathbf1\right)
=\frac{1}{2\sqrt2}F_{\phi_*}(b\oplus53).
}
\]
The two identities follow directly by comparing the six columns of \(A(\phi)\) and \(A(\phi_*)\) with the signed axes; the sign changes in columns 2 and 4 and the centred-cube factor produce the fixed bit relabelling and scale. The executable audit checks both coordinate identities with residuals below \(10^{-12}\). Thus the 64 golden vectors are the physical 3D cut-and-project image of the 64 hexagrams, while the internal 3D image is its algebraic conjugate. They are still not the 64 tetrahedron *cells*.


## 3. Distinguish the three geometric objects

1. **Fuller vector equilibrium (VE):** in Synergetics this is the cuboctahedral 12-vertex, 24-edge polyhedron with six square and eight triangular faces. Fuller also describes the tetrahedron–octahedron isotropic vector matrix (IVM) as a space-filling lattice.
2. **64-tetrahedron grid:** ISF/Haramein presentations describe a construction from eight star tetrahedra and call it a 64-tetrahedron grid / two-octave VE construction. This is a separate cell complex, not the original 12-vertex VE.
3. **Q6 golden vectors:** the 64 points \(F(b)\) above, indexed by six-bit hexagrams and carrying the 192 Hamming-one edges.

The equality of the three counts (64 states / 64 tetrahedra / 64 points) is not a geometric equivalence. An equivariant correspondence requires the actual tetrahedron coordinates, tetrahedron incidence, and a declared symmetry action. No such machine-readable 64-cell dataset was present in the inspected repository/source material; the audit therefore reports the comparison as **NOT TESTED**, rather than manufacturing a coordinate match.

## 4. PSU scale and the only conclusion currently justified

In Haramein's 2013 article, a PSU is defined as a sphere of Planck mass and diameter \(\ell_P\), hence radius \(r_P=\ell_P/2\), volume
\[
V_{PSU}=\frac{4\pi}{3}\left(\frac{\ell_P}{2}\right)^3
=\frac{\pi\ell_P^3}{6},
\]
and equatorial area \(\pi\ell_P^2/4\). This is the paper's proposed geometric unit; it is not an experimentally established constituent of spacetime.

For centres \(P_b=\lambda F(b)\), non-overlap of equal PSU spheres requires
\[
\lambda\min_{b\ne c}\|F(b)-F(c)\|\ge\ell_P.
\]
The finite pair-distance audit in the \(F_\phi\) normalization gives
\[
d_{min}^{(F)}=1.125554844510479,
\qquad
\lambda_F\ge0.8884507093343064\,\ell_P.
\]
In the T129 physical projection coordinates \(x_\parallel=F_\phi(b\oplus53)/(2\sqrt2)\), the minimum separation is
\[
d_{min}^{(\parallel)}=0.3979437315753649,
\qquad
\lambda_\parallel\ge2.5129180852811452\,\ell_P.
\]
These are the same geometric bound in two coordinate normalizations, not two independent predictions. It does not establish a space-filling packing, a density, a surface/volume holographic law, or a physical Planck-scale lattice.

## 5. Spatial spinorial model on Q6

Let \(u_b=\widehat F(b)\in S^2\). For each oriented Q6 edge \(g\to h\), the shortest rotation carrying \(u_g\) to \(u_h\) has quaternion lift
\[
s_{gh}=
\left(
\sqrt{\frac{1+u_g\cdot u_h}{2}},
\frac{u_g\times u_h}{\sqrt{2(1+u_g\cdot u_h)}}
\right)\in SU(2),
\]
provided the directions are not antipodal. The canonical choice has nonnegative scalar part. Its reverse is
\[
s_{hg}=s_{gh}^{-1}=\overline{s_{gh}}.
\]
Writing Pauli matrices \(\sigma=(\sigma_1,\sigma_2,\sigma_3)\), define the fundamental spinor transport
\[
\boxed{\mathcal U_{gh}=s^0_{gh}I_2-i\,\mathbf s_{gh}\cdot\boldsymbol\sigma.}
\]
Then \(\mathcal U_{gh}\in SU(2)\), and its adjoint action on Pauli vectors projects to the corresponding \(SO(3)\) edge rotation. Along an oriented face \(p=(v_0,v_1,v_2,v_3)\), the spin holonomy is the ordered product
\[
\mathcal U_p=\mathcal U_{v_3v_0}\mathcal U_{v_2v_3}
\mathcal U_{v_1v_2}\mathcal U_{v_0v_1}.
\]
The audit compares this product with the lift of the corresponding SO(3) holonomy on all 240 Q6 squares, checks unitarity, and checks reverse-edge inversion.

For a rotation about \(\hat n\),
\[
\mathcal U(\theta)=
\exp\!\left(-\frac{i\theta}{2}\hat n\cdot\boldsymbol\sigma\right),
\quad
\mathcal U(2\pi)=-I_2,\quad
\mathcal U(4\pi)=I_2.
\]
This is the standard Spin(3) double cover, not a new spin-statistics derivation.

## 6. Extension to the existing Cartan / teleparallel architecture

The SU(2) links are the spatial spin lift of the SO(3) connection. They do not replace the independent Cartan connection or identify curvature with torsion. On the existing RGS programme:
- general Riemann–Cartan branch: \(T\ne0\) and \(R\ne0\) are both allowed;
- teleparallel branch: the selected Lorentz/spin connection is flat, with torsion generally nonzero;
- Levi–Civita remains a torsion-free benchmark, not the fundamental connection by default.

The present code is only a spatial \(Spin(3)\simeq SU(2)\) link lift. A genuine relativistic spinor model requires a nondegenerate Lorentzian tetrad, a specified \(Spin(1,3)\simeq SL(2,\mathbb C)\) connection, its representation on Dirac spinors, and a compatible discrete Dirac operator/action. Those are subsequent gates. In particular, the static \(e^0=dt\) ansatz does not itself produce a Dirac equation or physical time dynamics.

## 7. Reproduction and status

Run:

~~~bash
python scripts/audit_q6_ivm_psu_spinor.py
python -m unittest discover -s tests -p "test_q6_ivm_psu_spinor.py" -v
~~~

The script writes audits/Q6_IVM_PSU_SPINOR_AUDIT.json. It audits the Q6 golden vectors, radial shells, PSU non-overlap threshold, all 192 edge lifts and all 240 face spin holonomies.

| Claim | Status |
|---|---|
| Q6 counts from six-bit hexagrams and Hamming-one adjacency | Exact combinatorics |
| 64 distinct signed golden vectors; 32 antipodal pairs | Finite construction / numerical audit |
| Four shells \(12+20+20+12\) | Numerical audit |
| PSU non-overlap scale | Geometric necessary condition |
| 64 Q6 vectors equivariant to 64 tetrahedra | Open; comparison data missing |
| Spatial SU(2) lift of Q6 SO(3) links | Finite numerical audit |
| \(2\pi\) sign and \(4\pi\) periodicity | Standard representation identity |
| Lorentzian Spin(1,3), Dirac operator and fermion dynamics | Open |
| PSU as physical spacetime constituents | Hypothesis, not established |

## References

- B. C. Fuller, Synergetics: Explorations in the Geometry of Thinking, §§430–451, online corpus: https://future.buckyverse.org/read/synergetics/manuscriptch5/
- N. Haramein, “Quantum Gravity and the Holographic Mass,” Physical Science International Journal 3(4), 270–292 (2013): https://journalpsij.com/index.php/PSIJ/article/view/158
- International Space Federation, “Spacetime Geometry — The Isotropic Vector Matrix & Star Tetrahedron” (2018 presentation): https://www.youtube.com/watch?v=gxbFbSfF6po
- T063, quaternionic \(SU(2)\to SO(3)\) double-cover theorem.
- T129, golden \(6D\to3D+3D\) cut-and-project frame.
