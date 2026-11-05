# T012 — SU(3)_F baryon octet and decuplet from three light quarks

**Status:** representation-theoretic decomposition proved; physical assignment applies to the approximate light-flavor SU(3) model. It is not a derivation of QCD masses or confinement.

## 1. The tensor-product theorem

Let V=\mathbb C^3 be the fundamental representation of flavor SU(3)_F with basis (u,d,s). Then
\[
V^{\otimes3}=\mathbf{10}_{S}\oplus\mathbf8_{M}\oplus\mathbf8_{M}\oplus\mathbf1_{A}.
\]
Dimensions check:
\[
27=10+8+8+1.
\]

### Proof by Young diagrams

The Schur–Weyl decomposition for three tensor factors is indexed by partitions of 3:
- [3]: fully symmetric, dimension 10 for SU(3);
- [2,1]: mixed symmetry, dimension 8 for SU(3), with multiplicity dim([2,1])=2 as an S_3 representation;
- [1,1,1]: fully antisymmetric, dimension 1 for SU(3).

Thus the two octets are the same SU(3) irrep appearing with multiplicity two, not two inequivalent SU(3) representations. □

The dimension formula for an SU(3) irrep with Dynkin labels (p,q) is
\[
\dim(p,q)=\frac{(p+1)(q+1)(p+q+2)}2.
\]
Hence 10=(3,0), 8=(1,1), and 1=(0,0).

## 2. Ground-state spin-flavor selection (Pauli principle)

A baryon color singlet is
\[
|\mathrm{color}\rangle=\frac1{\sqrt6}\epsilon_{abc}|a b c\rangle,
\]
which is totally antisymmetric in color. For an L=0 ground state, the spatial wavefunction is symmetric. Since the complete three-quark state must be antisymmetric under quark exchange, the combined spin-flavor part must be symmetric.

For spin SU(2), three spin-1/2 quarks decompose as
\[
2\otimes2\otimes2=4_S\oplus2_M\oplus2_M.
\]
The symmetric spin quartet S=3/2 combines with the symmetric flavor 10 to form the ground-state decuplet. The mixed spin S=1/2 sector combines with the mixed flavor 8 to form the ground-state octet (in the symmetric SU(6) spin-flavor representation 56):
\[
\mathbf{56}_{SU(6)}\downarrow SU(3)_F\times SU(2)_S
=(\mathbf{10},\mathbf4)\oplus(\mathbf8,\mathbf2).
\]
Dimension check: 56=10×4+8×2.

The flavor singlet 1 is present in the abstract flavor product but is not part of this symmetric L=0 ground-state 56. It can occur in other orbital/spin-flavor symmetry sectors; do not declare it universally forbidden.

## 3. Physical ground-state multiplets

### Flavor octet (spin 1/2)

\[
\begin{matrix}
&& n && \\
& p && \Lambda && \Sigma^0 & \\
\Sigma^+ && \Sigma^- && \Xi^0 && \Xi^- 
\end{matrix}
\]
Members: p, n, Λ, Σ⁺, Σ⁰, Σ⁻, Ξ⁰, Ξ⁻.

### Flavor decuplet (spin 3/2)

Rows organized by strangeness:
- Δ quartet: Δ++, Δ+, Δ⁰, Δ⁻
- Σ* triplet: Σ*+, Σ*⁰, Σ*−
- Ξ* doublet: Ξ*⁰, Ξ*−
- Ω⁻ singlet

Total: 4+3+2+1=10.

The octet/decuplet labels are **flavor SU(3)_F**. They must not be confused with **color SU(3)_C**: color singlet baryons are constructed using ε_{abc}, while flavor multiplets classify u,d,s content.

## 4. Gell-Mann–Okubo mass relation for the octet

Under first-order SU(3)_F breaking by an octet perturbation, the ground-state octet masses satisfy the standard relation
\[
2(M_N+M_\Xi)=3M_\Lambda+M_\Sigma,
\]
where M_N and M_Ξ denote isospin-averaged masses and M_Σ is the isospin-averaged Σ mass. This is a phenomenological consequence of the representation structure plus the stated first-order breaking assumption, not an exact QCD identity.

For the decuplet, the corresponding first-order equal-spacing rule is
\[
M_{\Sigma^*}-M_\Delta\approx
M_{\Xi^*}-M_{\Sigma^*}\approx
M_\Omega-M_{\Xi^*}.
\]
Higher-order breaking and electromagnetic/isospin effects produce deviations.

## 5. What this establishes for the Q6–PSU program

**Established mathematically:** SU(3)_F representation decomposition, multiplicities, Young symmetry, ground-state spin-flavor selection under the stated Pauli/L=0 assumptions.

**Not established by the Q6 graph or Wilson-loop basis:** baryon masses, hadron wavefunctions, confinement, chiral symmetry breaking, or a QCD continuum limit.

To connect this to the Q6 lattice model, one must define:
1. a site/edge realization of three-quark operators with flavor labels u,d,s;
2. color indices and the antisymmetric color-singlet contraction;
3. a fermion Dirac/hopping operator and fermionic action;
4. gauge-invariant baryon interpolating operators, e.g.
\[
B_{f_1f_2f_3}(x)=\epsilon_{abc}
\big(q^{a}_{f_1}(x)^T C\Gamma q^{b}_{f_2}(x)\big)
q^{c}_{f_3}(x),
\]
with spin/flavor projections chosen to obtain octet or decuplet quantum numbers;
5. correlation functions and a controlled extraction of masses.

The 64 Q6 vertices, 192 edges and 240 plaquettes are combinatorial input; they do not alone determine the above fermionic and color structure.

## 6. References

- Particle Data Group, *Review of Particle Physics*, “Quark Model” and SU(3) multiplet sections: https://pdg.lbl.gov/
- M. Furuichi and K. Shimizu, “Description of SU(3) octet and decuplet baryons,” *Phys. Rev. C* 65, 025201 (2002), DOI: 10.1103/PhysRevC.65.025201.
- V. Cruceanu et al. survey is unrelated to this flavor decomposition; keep para-Kähler references separate from QCD bibliography.
