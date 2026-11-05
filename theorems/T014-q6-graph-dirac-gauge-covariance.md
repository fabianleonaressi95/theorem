# T014 — Graph Dirac operator and SU(3) gauge covariance on Q6

**Status:** Conditional exact algebraic theorem for a graph Dirac operator built from unitary links and gauge-covariant edge transport. This is not yet a validated Q6 discretization of continuum QCD.

## 1. Setup

Let G=(V,E) be a finite oriented graph. For every directed edge e=(v,w), choose a reverse edge and link
\[
U_{vw}\in SU(3)_C,\qquad U_{wv}=U_{vw}^{\dagger}.
\]
Let spinors be \(\psi(v)\in\mathbb C^4\otimes\mathbb C^3\). A local gauge transformation is a map \(g:V\to SU(3)\), acting as
\[
\psi(v)\mapsto g_v\psi(v),\quad
U_{vw}\mapsto g_vU_{vw}g_w^{-1}.
\]

Choose edge coefficients \(c_{vw}\) and spin matrices \(\Gamma_{vw}\) acting only on spin space. Define the covariant graph difference
\[
(D_U\psi)(v)=m\psi(v)+
\sum_{w\sim v}c_{vw}\Gamma_{vw}
\big(U_{vw}\psi(w)-\psi(v)\big).
\]
The coefficients and Γ are assumed gauge-independent, and color links commute with spin matrices.

## 2. Gauge covariance theorem

**Theorem.** If each link transforms as above and the operator is assembled only from local terms and covariant edge transports, then
\[
D_{U^g}(g\psi)(v)=g_v(D_U\psi)(v).
\]

**Proof.** For each edge,
\[
U^g_{vw}(g_w\psi(w))
=g_vU_{vw}g_w^{-1}g_w\psi(w)
=g_vU_{vw}\psi(w).
\]
The local term satisfies m g_vψ(v)=g_v mψ(v). Since Γ and scalar coefficients act trivially on color, every summand factors by g_v. Summing proves the identity. □

Thus the fermion bilinear \(\sum_v\bar\psi(v)D_U\psi(v)\) is gauge invariant when \(\bar\psi(v)\mapsto\bar\psi(v)g_v^{-1}\).

## 3. Adjoint and hermiticity caveat

Gauge covariance alone does **not** imply Hermiticity, anti-Hermiticity, γ5-Hermiticity, absence of doublers, or a correct continuum limit.

For a chosen edge pairing, define the hopping part
\[
(H_U\psi)(v)=\sum_{w\sim v}A_{vw}U_{vw}\psi(w).
\]
It is Hermitian if the reverse-edge coefficients obey
\[
A_{wv}=A_{vw}^{\dagger}
\]
(with the corresponding spin/color ordering), because U_{wv}=U_{vw}†. A Dirac-like anti-Hermitian kinetic operator may instead require a signed orientation and
\[
A_{wv}=-A_{vw}^{\dagger}.
\]
These are distinct conventions and must not be conflated. The mass term is usually added separately.

## 4. Wilson-type graph operator (candidate)

A graph Wilson analogue can be written
\[
D_W=m_0I+\frac12\sum_{w\sim v}
\left[\Gamma_{vw}(U_{vw}\psi(w)-\psi(v))
+r\,(2\psi(v)-U_{vw}\psi(w)-U_{wv}\psi(v))\right],
\]
but this expression is only schematic until:
- edge orientation/sign conventions and Γ_{vw} are fixed;
- a Q6 notion of lattice spacing and directional derivatives is defined;
- the graph is bipartite (Q6 is) and possible doubling modes are studied;
- a γ5 operator and γ5-Hermiticity are checked explicitly;
- the continuum/low-energy scaling is specified.

The Wilson term suppresses unwanted modes in standard lattice discretizations; it cannot be assumed to do so on an arbitrary finite graph.

## 5. Q6-specific finite graph data

For the six-dimensional hypercube graph Q6:
- |V|=2^6=64;
- |E|=6·2^5=192;
- degree=6;
- adjacency spectrum: 6−2k with multiplicity \(\binom6k\), k=0,…,6;
- graph Laplacian spectrum: 2k with multiplicity \(\binom6k\).

These are graph facts, not a claim that the Q6 adjacency spectrum is the physical Dirac spectrum. A Dirac operator requires spin structure, edge Clifford directions, and a prescription for discrete derivatives.

## 6. What this theorem does and does not establish

**Proved under stated construction:** local SU(3)_C gauge covariance of the edge-coupled graph operator and gauge invariance of the associated fermion bilinear.

**Not established:** Q6 continuum limit, correct fermion species count, chirality, anomaly structure, confinement, physical baryon masses, or a valid SU(3) QCD path integral.

### Next audit targets
1. Build explicit 4×4 Γ_i with \(\{\Gamma_i,\Gamma_j\}=2\delta_{ij}I\) (or an explicitly Euclidean convention).
2. Test free operator eigenvalues at all 64 Q6 momentum characters and identify zero/doubler modes.
3. Verify γ5-Hermiticity numerically and analytically.
4. Add SU(3) links and test covariance to machine precision on random g_v,U_e,ψ.
5. Only then construct fermion determinants and baryon correlators.

## References
- C. Gattringer and C. B. Lang, *Quantum Chromodynamics on the Lattice*, Springer (2010).
- K. G. Wilson, “Confinement of quarks,” *Phys. Rev. D* 10, 2445 (1974).
