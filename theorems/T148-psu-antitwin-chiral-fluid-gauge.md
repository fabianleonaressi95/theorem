# T148 — PSU–Anti-Twin chiral fluid gauge: right/left locking on the two Q6 sheets

**Classification:** exact finite representation and conjugate-link identities; proposed physical identification of chirality with sheet index; continuum fluid dynamics and mass generation remain conditional.  
**Dependencies:** T016, T063, T129, T146, T147 and the prior PSU/Anti-Twin two-sheet audit.

## 1. Preserve the existing two-sheet data

There are 64 Q6 states on each sheet, hence 128 states in the doubled carrier. The sheet exchange is
\[
J_{\rm AT}=I\otimes\tau_1,\qquad J_{\rm AT}^2=I.
\]
The PSU sheet carries charge \(+q_0\), the Anti-Twin sheet charge \(-q_0\):
\[
Q=q_0\tau_3,\qquad J_{\rm AT}QJ_{\rm AT}^{-1}=-Q,\qquad \operatorname{tr}Q=0.
\]
For a compact \(U(1)\) link, the Anti-Twin representation is the conjugate one:
\[
U_{gh}^{(-)}=(U_{gh}^{(+)})^*=(U_{gh}^{(+)})^{-1}.
\]
For \(SU(2)\), complex conjugation is equivalent to the fundamental representation through the invariant antisymmetric intertwiner \(\epsilon=i\sigma_2\); it is not a second independent connection.

Both sheets share the same RGS vierbein. Their relative geometry remains the previously defined \(\rho\), \(\sigma=\ln(\rho/\rho_\infty)\), with \(e_-=\mathcal I^*e_+\). The exchange operation is not Cartan torsion.

## 2. Right/left is a locked sheet decomposition

Let \(\psi\) be a four-dimensional Dirac spinor and let the sheet factor be \(\mathbb C^2_{\rm AT}\). With
\[
P_R=\frac{1+\gamma^5}{2},\quad P_L=\frac{1-\gamma^5}{2},\quad
P_\pm=\frac{1\pm\tau_3}{2},
\]
define
\[
\mathscr C_{RL}=\gamma^5\otimes\tau_3,\qquad
P_{\rm lock}=\frac{1+\mathscr C_{RL}}2.
\]
The physical locked subspace is
\[
\boxed{\mathcal H_{\rm lock}
=(P_R\mathcal S\otimes\mathcal H_+)
\oplus(P_L\mathcal S\otimes\mathcal H_-).}
\]
It has complex dimension four per spacetime point: one Dirac spinor whose right-handed component resides on the PSU sheet and whose left-handed component resides on the Anti-Twin sheet. This is the two-sheet realization of the right/left fluid separation; it is not two unrelated Weyl species.

The bare sheet exchange anticommutes with the locking involution:
\[
J_{\rm AT}\mathscr C_{RL}J_{\rm AT}^{-1}=-\mathscr C_{RL}.
\]
Thus it exchanges the locked and anti-locked subspaces. The combined parity-plus-sheet operation
\[
\mathscr P_{\rm AT}=\gamma^0\otimes\tau_1,\qquad x\mapsto \mathsf P x,
\]
preserves the locked subspace because parity reverses \(\gamma^5\) while sheet exchange reverses \(\tau_3\). \(J_{\rm AT}\) alone is an internal exchange, not spacetime parity.

## 3. Fluid gauge variables and their even/odd modes

Retain the earlier two-sheet fluid variables:
\[
\Phi_\pm=\ln N_\pm,\qquad
n_{\pm\mu}=\frac{\mathcal A_{\pm\mu}}{N_\pm},\qquad
\xi_\pm=(n_\pm\cdot n_\pm)\ln N_\pm.
\]
For every sheet quantity \(X_\pm\), define
\[
X_e=\frac{X_++X_-}{2},\qquad X_o=\frac{X_+-X_-}{2}.
\]
In particular \(n_e,n_o,\Phi_e,\Phi_o,\xi_e,\xi_o\). Under \(J_{\rm AT}\), even fields are invariant and odd fields reverse sign. The previously used fluid modes are
\[
v_0=\frac{v_++v_-}{2},\qquad
s_{\rm AT}=\frac{v_+-v_-}{2}.
\]
The latter is the relative/Anti-Twin fluid mode.

Treat the normalized sheet one-forms \(a_\pm\) as the two fluid gauge connections. Their diagonal/relative decomposition is
\[
a_e=\frac{a_++a_-}{2},\qquad a_o=\frac{a_+-a_-}{2},\qquad a_\pm=a_e\pm a_o.
\]
The spinor-sheet connection is
\[
\mathbb A_\mu=a_{e\mu}I+a_{o\mu}\tau_3.
\]
On the locked subspace, \(\tau_3=\gamma^5\), so
\[
\boxed{\mathbb A_\mu\big|_{\rm lock}=a_{e\mu}I+a_{o\mu}\gamma^5.}
\]
Consequently the right-handed component couples to \(a_+=a_e+a_o\), while the left-handed component couples to \(a_-=a_e-a_o\). This is an exact projector identity. In the strict Anti-Twin conjugate limit \(a_-=-a_+\), one has \(a_e=0\) and the coupling is purely relative/axial.

The validated symmetry of the existing two-sheet construction is the discrete exchange \(Z_2\), not a proven local \(U(1)\). If one extends it to a continuous sheet-phase gauge symmetry, the candidate transformations are
\[
\psi_\pm\mapsto e^{-iq\chi_\pm}\psi_\pm,\qquad
a_\pm\mapsto a_\pm+d\chi_\pm/q,\qquad \chi_\pm=\chi_e\pm\chi_o.
\]
On the locked spinor this is
\[
\psi\mapsto e^{-iq(\chi_e+\gamma^5\chi_o)}\psi,\quad
a_e\mapsto a_e+d\chi_e/q,\quad
a_o\mapsto a_o+d\chi_o/q.
\]

## 4. PSU normalization

Retain
\[
\ell_{\rm PSU}=\lambda_{\rm PSU}\ell_P,\quad
r_{\rm PSU}=\ell_{\rm PSU}/2,\quad
V_{\rm PSU}=\frac{\pi\ell_{\rm PSU}^3}{6},\quad
A_{\rm eq}=\frac{\pi\ell_{\rm PSU}^2}{4}.
\]
Also retain \(\alpha_G=GM^2/(\hbar c)=(M/M_P)^2\) and \(q_0=\sqrt{\alpha_G}\). The charge operator is \(Q=q_0\tau_3\). A dimensionless model coupling may be normalized as \(g_{\rm PSU}=g_*\lambda_{\rm PSU}\sqrt{\alpha_G}\), with \(g_*\) explicit in the action; this is a normalization convention, not a measured coupling.

T146's PSU non-overlap constraint is \(\lambda_\parallel\ge2.5129180853\ell_P\) in the T129 projected-coordinate normalization. It is not a packing-density theorem.

## 5. Common spinor/gauge action and the mass gate

After a Lorentzian tetrad and independent Cartan spin connection are selected,
\[
D_\mu\psi=\left[
\partial_\mu+\frac14\omega_{\mu AB}\gamma^{AB}
+iq(a_{e\mu}+a_{o\mu}\gamma^5)
\right]\psi.
\]
A minimal gauge-plus-fermion action is
\[
\begin{aligned}
S_{\rm min}=\int d^4x\,e\bigg\{&
\frac{i}{2}\left[
\bar\psi\gamma^Ae_A{}^\mu D_\mu\psi
-(D_\mu\bar\psi)\gamma^Ae_A{}^\mu\psi
\right]\\
&-\frac{1}{4g_e^2}f_{e\mu\nu}f_e^{\mu\nu}
-\frac{1}{4g_o^2}f_{o\mu\nu}f_o^{\mu\nu}
\bigg\},\qquad f_{e/o}=da_{e/o}.
\end{aligned}
\]
Here \(\omega\) is the independent Lorentz/Cartan connection, not either fluid gauge connection.

A bare Dirac mass \(m\bar\psi\psi\) couples the two chiralities and is not invariant under local relative axial \(U(1)\). It must either be absent in the exactly chiral phase or arise from an inter-sheet bridge \(\Delta\):
\[
S_\Delta=-\int d^4x\,e\,
(\bar\psi_L\Delta\psi_R+\bar\psi_R\Delta^*\psi_L),
\quad \Delta\mapsto e^{2iq\chi_o}\Delta.
\]
The earlier \(\rho\) is a relative-sheet modulus; it does not supply the phase of \(\Delta\) by itself. A complex bridge phase, Q-ball \(SO(2)\), or Higgs mechanism must be derived, not assumed.

### Continuous-gauge anomaly gate

The established Anti-Twin operation is \(Z_2\), not a validated local \(U(1)\). If the pure relative connection is nevertheless gauged continuously, the locked pair has \(q_R=+q_0\), \(q_L=-q_0\). Its four-dimensional anomaly coefficients (up to the overall chirality sign convention) are
\[
\mathcal A_{\rm grav}\propto q_L-q_R=-2q_0,\qquad
\mathcal A_{U(1)^3}\propto q_L^3-q_R^3=-2q_0^3.
\]
Both are nonzero for \(q_0\ne0\). Therefore the minimal one-pair axial \(U(1)\) action is not a consistent standalone quantum gauge theory. It must remain an effective/background fluid connection, or additional fermions/anomaly inflow must cancel both anomalies. The finite audit explicitly checks that these coefficients are nonzero. This is not a defect of the \(Z_2\) exchange itself.

## 6. Q6 discretization and Nielsen–Ninomiya

Q6 is finite and has no Brillouin torus of a translationally invariant periodic lattice. The theorem's hypotheses therefore cannot be transferred verbatim from an infinite periodic hypercubic lattice. Nevertheless, finiteness alone is not a proof of absence of doubling.

The two-sheet lock supplies a vector-like Dirac pair: the right component on PSU and the left component on Anti-Twin form one four-component Dirac field. It does **not** claim a single isolated Weyl fermion or evade Nielsen–Ninomiya. A discrete kinetic operator must still be tested for locality, Hermiticity, low-energy zeros and species multiplicity. The existing \(D_{\rm DK}=d_\nabla+d_\nabla^\dagger\) is a cochain operator, not yet a proven one-Dirac operator.

## 7. 64 tetrahedra and Q6

Q6 is bipartite with 32 even and 32 odd vertices. Some 64-tetrahedron-grid descriptions likewise distinguish 32 positive and 32 negative tetrahedra. This permits an orientation-compatible *candidate labeling*, not an adjacency-preserving or metric/equivariant isomorphism. The 64-cell coordinates, oriented incidence and symmetry generators are still required; no arbitrary point set is substituted.

## 8. Status ledger

| Claim | Status |
|---|---|
| \(J^2=I\), \(JQJ^{-1}=-Q\) | Exact two-sheet representation identity |
| Right-on-PSU / left-on-AntiTwin locking projector | Exact finite Clifford/projector identity; physical assignment is a model postulate |
| \(a_e\) vector and \(a_o\) axial fluid one-forms | Exact even/odd decomposition; local (U(1)) is only a candidate extension |
| \(a_-=-a_+\Rightarrow a_e=0\) | Exact conjugate \(U(1)\) limit |
| \(v_0,s_{\rm AT},\Phi_\pm,n_\pm,\xi_\pm\) parity | Exact exchange decomposition |
| PSU radius/volume/area and \(q_0^2=\alpha_G\) | Algebraic normalization |
| Gauge/fermion action | Classical/effective ansatz; fundamental axial (U(1)) blocked by anomaly unless cancelled |
| Massive chiral phase | Requires a charged inter-sheet bridge \(\Delta\) |
| One isolated Weyl fermion without mirror | Not claimed; Nielsen–Ninomiya remains |
| Q6–64 tetrahedron metric correspondence | Open pending coordinates/incidence |

## 9. Reproduction

~~~bash
python scripts/audit_q6_psu_antitwin_chiral_fluid.py
python -m unittest discover -s tests -p "test_q6_psu_antitwin_chiral_fluid.py" -v
~~~

The script writes audits/Q6_PSU_ANTITWIN_CHIRAL_FLUID_GAUGE_AUDIT.json.
