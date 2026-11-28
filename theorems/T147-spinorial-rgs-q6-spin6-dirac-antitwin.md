# T147 — Spinorial RGS–Q6: Spin(6), the golden 3+3 split, Lorentz spinors and Anti-Twin

**Classification:** exact finite Clifford/Spin representation identities; golden-frame Spin(6) lift structure established algebraically and audited at generator level; Q6 Dirac operator and physical spinor dynamics remain open.  
**Dependencies:** T063 (Spin(3) double cover); T115 (coframe Clifford anticommutator); T129 (golden 6D cut-and-project frame); T146 (Q6 edgewise SU(2) lift); T016 (fermion-doubling constraint); Cartan/teleparallel synthesis.

## 1. Three distinct spinorial layers

- The **spatial** link model of T146 uses \(Spin(3)\simeq SU(2)\), the double cover of \(SO(3)\).
- The **Euclidean cut-and-project carrier** uses \(Spin(6)\), the double cover of \(SO(6)\), with a complex Dirac module of dimension 8 and chiral modules of dimension 4.
- A **Lorentzian spacetime fermion** transforms under \(Spin(1,3)\simeq SL(2,\mathbb C)\), not under \(SU(2)\) alone.

The 6D golden split is an orthogonal geometric decomposition. It does not by itself choose a time direction or produce a Lorentzian spin bundle.

## 2. The golden frame is an SO(6) transformation

Use \(P_\parallel,P_\perp\) from T129 and stack them:
\[
O_6=\begin{pmatrix}P_\parallel\\P_\perp\end{pmatrix}.
\]
The existing convention gives \(O_6O_6^T=I_6\), \(\det O_6=+1\). Thus \(O_6\in SO(6)\) and has exactly two lifts in \(Spin(6)\), differing by the central sign. The lift is a change of spin frame, not a new physical interaction. The audit checks orthogonality and orientation; it does not assign dynamics to this constant frame rotation.

## 3. Explicit Euclidean Clifford module

Let \(\sigma_1,\sigma_2,\sigma_3\) be the Pauli matrices. With \(I=I_2\), choose the \(8\times8\) Hermitian generators
\[
\begin{aligned}
\Gamma_1&=\sigma_1\otimes I\otimes I,&
\Gamma_2&=\sigma_2\otimes I\otimes I,\\
\Gamma_3&=\sigma_3\otimes\sigma_1\otimes I,&
\Gamma_4&=\sigma_3\otimes\sigma_2\otimes I,\\
\Gamma_5&=\sigma_3\otimes\sigma_3\otimes\sigma_1,&
\Gamma_6&=\sigma_3\otimes\sigma_3\otimes\sigma_2.
\end{aligned}
\]
They satisfy \(\{\Gamma_I,\Gamma_J\}=2\delta_{IJ}I_8\). Define
\[
\Gamma_* = i\Gamma_1\Gamma_2\Gamma_3\Gamma_4\Gamma_5\Gamma_6.
\]
Then \(\Gamma_*^\dagger=\Gamma_*\), \(\Gamma_*^2=I_8\), and \(\{\Gamma_*,\Gamma_I\}=0\). The chiral projectors \(P_\pm^{(6)}=(I_8\pm\Gamma_*)/2\) have rank 4.

## 4. Spin(6) lift of rotations

For a rotation in the \(I,J\) plane, with active convention \(e_I\mapsto\cos\theta\,e_I+\sin\theta\,e_J\), use
\[
S_{IJ}(\theta)=
\exp\!\left(-\frac{\theta}{2}\Gamma_I\Gamma_J\right)
=\cos\frac\theta2\,I_8-\sin\frac\theta2\,\Gamma_I\Gamma_J.
\]
It is unitary and obeys
\[
S_{IJ}\Gamma_I S_{IJ}^{-1}
=\cos\theta\,\Gamma_I+\sin\theta\,\Gamma_J,\qquad
S_{IJ}\Gamma_J S_{IJ}^{-1}
=-\sin\theta\,\Gamma_I+\cos\theta\,\Gamma_J.
\]
Also \(S_{IJ}(2\pi)=-I_8\) and \(S_{IJ}(4\pi)=I_8\). Products of plane rotations generate \(Spin(6)\).

## 5. Restriction to the physical/internal 3+3 subgroup

The orthogonal split \(\mathbb R^6=E_\parallel\oplus E_\perp\) has subgroup
\[
Spin(3)_\parallel\times Spin(3)_\perp
\simeq SU(2)_\parallel\times SU(2)_\perp.
\]
Each chiral 4-dimensional Spin(6) module restricts to the tensor-product bi-spinor representation
\[
S_+^{(6)}\big|_{Spin(3)\times Spin(3)}
\simeq(\mathbf2,\mathbf2),\qquad
S_-^{(6)}\big|_{Spin(3)\times Spin(3)}
\simeq(\mathbf2,\mathbf2),
\]
with the two chiral sectors distinguished by \(\Gamma_*\). This is a representation-theoretic bridge, not yet a dynamical coupling. In particular, \(SU(2)_\perp\) is not automatically a time-rotation group. The torsion-coupled internal-axis selector remains a candidate for selecting a distinguished internal direction; it must not be relabelled as physical time before a Lorentzian tetrad and causal structure are derived.

## 6. Q6 spinor field and the discrete operator gate

Assign to each hexagram vertex \(b\in\{0,1\}^6\) a 6D spinor \(\Psi_b\in\mathbb C^8\), with chiral components \(P_\pm^{(6)}\Psi_b\). A connection on Q6 links must be specified in \(Spin(6)\), with reverse-link inverse and face products in the correct order. The constant golden frame \(O_6\) only changes the decomposition of spinor components; it is not itself the link connection.

A conservative first finite operator is the twisted Dirac–Kähler operator on cubical cochains,
\[
D_{\rm DK}=d_\nabla+d_\nabla^\dagger,
\]
where \(d_\nabla\) is the covariant cubical coboundary induced by the spin links and the adjoint is defined by a declared cell inner product. It acts on inhomogeneous cochains tensored with the spinor fibre; it is not automatically a single irreducible Dirac fermion.

A vertex-based Dirac stencil, its Hermiticity, continuum symbol, boundary conditions and low-energy multiplicities must be derived separately. T016's Nielsen–Ninomiya analysis is a mandatory constraint: no claim of a single undoubled local lattice fermion is allowed without identifying which theorem hypotheses are absent or which additional mechanism is used. The Q6 graph is finite and non-periodic as a graph, but that fact alone does not certify absence of spectral doubling.

## 7. Lorentzian 4D spinor and independent Cartan connection

Once a nondegenerate Lorentzian tetrad \(e^A{}_\mu\) and a metric-compatible Lorentz connection \(\omega_\mu{}^{AB}\) are specified, define
\[
D_\mu\psi=
\left(\partial_\mu+\frac14\omega_{\mu AB}\gamma^{AB}
-iqA_\mu\right)\psi,\qquad
\gamma^{AB}=\frac12[\gamma^A,\gamma^B].
\]
The minimally coupled symmetrized Dirac action is
\[
S_D=\int d^4x\,e\left[
\frac{i}{2}\left(
\bar\psi\gamma^Ae_A{}^\mu D_\mu\psi
-(D_\mu\bar\psi)\gamma^Ae_A{}^\mu\psi
\right)-m\bar\psi\psi
\right].
\]
Here \(A_\mu\) is the electromagnetic \(U(1)\) connection; it is distinct from the Lorentz spin connection. The Riemann–Cartan branch allows both \(T\ne0\) and \(R\ne0\). The teleparallel branch is the separately constrained flat Lorentz connection with generally nonzero torsion. Levi–Civita is the torsion-free benchmark, not the default fundamental connection.

If the gravitational action is Einstein–Cartan with minimally coupled Dirac matter, varying the independent connection yields the standard algebraic spin-current/torsion relation. A different Poincaré-gauge or quadratic-torsion action gives different field equations. No torsion–axial-current coefficient is inserted before the action is selected.

## 8. Anti-Twin doubling

For two sheets, take
\[
\boldsymbol\Psi=
\begin{pmatrix}\psi_+\\\psi_-\end{pmatrix}
\in\mathbb C^4\otimes\mathbb C^2,\qquad
S_{\rm AT}=I_4\otimes\tau_1,
\]
with \(P_{\rm even/odd}=(I_8\pm S_{\rm AT})/2\). An exchange-symmetric operator commutes with \(S_{\rm AT}\) and preserves the two sectors. An off-diagonal sheet-mixing mass proportional to \(I_4\otimes\tau_1\) is symmetry-allowed, but its coefficient is a model parameter until derived from a common action or constrained by data. Sheet exchange is not Cartan torsion and is not electromagnetic curvature.

The 4D fibre can therefore be organized as \(\mathbb C^4_{\rm Dirac}\otimes\mathbb C^2_{\rm AntiTwin}\), with separate Lorentz-spin, electromagnetic \(U(1)\), and sheet-exchange factors. A six-dimensional internal spinor factor may be retained as an additional internal representation only after its coupling and reduction map are specified; it must not be counted twice as a second spacetime spinor.

## 9. PSU–Anti-Twin chiral-fluid specialization

The two-sheet chirality locking and the fluid-gauge connection are specialized in **T148**. In particular, do not treat the generic \(I_4\otimes\tau_1\) doublet written here as an unconstrained second Dirac species: T148 imposes \(P_R\) on the PSU sheet and \(P_L\) on the Anti-Twin sheet. The validated symmetry remains \(Z_2\); a continuous relative axial \(U(1)\) is only a candidate extension and is subject to the anomaly and mass gates in T148.

## 10. Status ledger

| Component | Status |
|---|---|
| Euclidean Cl(6) gamma matrices and chirality | Exact representation identity; numerical audit |
| Spin(6) plane-rotation lift | Exact representation identity; numerical audit |
| Golden 3+3 frame in SO(6) | Existing T129 construction; orthogonality audited |
| Spin(3) spatial link lift on Q6 | T146 finite numerical audit |
| 4D Lorentzian Spin(1,3) bundle | Requires derived Lorentzian tetrad and connection |
| Q6 covariant Dirac–Kähler operator | Finite construction template; implementation/convergence open |
| Single undoubled Q6 Dirac fermion | Open; T016 constraint applies |
| Anti-Twin Dirac doublet | Representation/action template; coupling not fixed |
| Torsion–spin-current dynamics | Depends on selected gravitational action |
| Physical fermion interpretation / spin-statistics | Not established by these finite algebra checks |

## Reproduction

~~~bash
python scripts/audit_q6_spin6_clifford.py
python -m unittest discover -s tests -p "test_q6_spin6_clifford.py" -v
~~~

The script writes audits/Q6_SPIN6_CLIFFORD_AUDIT.json.

## References

- T016 — Q6 fermion doubling / Nielsen–Ninomiya audit.
- T063 — quaternionic \(SU(2)\to SO(3)\) double cover.
- T115 — pointwise curved Clifford anticommutator for the RGS spatial coframe.
- T129 — golden \(6D\to3D+3D\) cut-and-project frame.
- T146 — Q6 golden vectors, PSU separation threshold and spatial SU(2) edge lift.
- B. C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer (2015).
