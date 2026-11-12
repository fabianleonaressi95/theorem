# T113-E — Q6/RGS T2u triplet: spectral stability and admissible dynamical use

**Classification:** source-derived numerical spectral datum and exact conditional stability criterion. The triplet is a verified geometric/spectral sector of the 188D RGS tangent model. Its identification as a physical phonon or phason is not established.

## 1. Use the existing Q6/RGS tangent construction

The 64-site geometry \(X\in\mathbb R^{64\times3}\) is the repository's recovered, hash-checked RGS seed. The constrained displacement space is
\[
\mathcal T=\ker J,\qquad
J\in\mathbb R^{4\times192},\qquad
Q\in\mathbb R^{192\times188},\quad Q^TQ=I.
\]
The four constraints are three translations and one fixed-scale/radial constraint. The tangent dimension is 188.

The existing reconstruction in `models/tangent_triplet_anisotropy.py` constructs the 48-element signed-permutation action of \(O_h\), the character projector onto the 30-dimensional \(T_{2u}\)-isotypic component, and the constrained Coulomb Hessian
\[
K=Q^T(H+\lambda_{\rm force}I_{192})Q.
\]
The first isolated three-dimensional spectral cluster in that isotypic component is extracted as an orthonormal basis
\[
V\in\mathbb R^{188\times3},\qquad V^TV=I_3.
\]
This is the existing RGS/Q6 triplet; T113-E does not create a new icosahedral lattice or replace Q6.

## 2. Spectral fact and immediate physical consequence

The source reconstruction targets the triply degenerate eigenvalue
\[
\lambda_{T_{2u}}=-0.06994933008401777,
\]
with reported spread below \(10^{-10}\), rank three, and gap to the next \(T_{2u}\) eigenvalue greater than 0.3. The reconstruction test checks the projector idempotence, commutator, tangent constraints, eigen-residual, orthonormality, and gap.

For a conservative second-order dynamics with positive inertia \(m_T>0\) and stiffness equal to this unmodified constrained Hessian eigenvalue, the mode equation is
\[
m_T\ddot a+\lambda_{T_{2u}}a=0.
\]
Since \(\lambda_{T_{2u}}<0\), its solutions are exponentially growing/decaying, not oscillatory:
\[
a(t)=A e^{\gamma t}+B e^{-\gamma t},\qquad
\gamma=\sqrt{0.06994933008401777/m_T}.
\]
Therefore **this first T2u triplet of the unmodified constrained Coulomb Hessian is not a stable phonon or propagating phason mode**. Calling it either would be incorrect. It is a triply degenerate unstable tangent mode of that particular Coulomb functional and constrained geometry.

## 3. Conditional stabilization threshold

If a separately derived physical contribution adds a positive isotropic stiffness \(\mu I\) on this triplet, then
\[
\omega_T^2=\frac{\lambda_{T_{2u}}+\mu}{m_T}.
\]
The exact stability conditions are:
\[
\begin{array}{ll}
\mu<0.06994933008401777 &: \text{unstable},\\
\mu=0.06994933008401777 &: \text{marginal at harmonic order},\\
\mu>0.06994933008401777 &: \text{stable oscillatory triplet}.
\end{array}
\]
This is a conditional threshold in the normalization of the existing Coulomb Hessian. It is not a measured material constant, not a De Aquino threshold, and not a universal RGS prediction. A physical stabilizing term must be derived from the selected energy functional or measured constitutive input; it must not be inserted merely to force positivity.

## 4. Correct finite-dimensional phonon/internal-mode ansatz

Let \(a(t)\in\mathbb R^3\) be the amplitudes of this existing triplet. In the chosen deterministic basis, the restricted harmonic action is
\[
S_T=\frac12\int dt\left[
m_T\dot a^T\dot a
-a^T(\lambda_T I_3+\mathsf S_T)a
\right],
\]
where \(\mathsf S_T\) is a separately specified, symmetry-compatible stabilizing/self-energy correction. If the full \(O_h\) symmetry is retained and the triplet is irreducible, Schur's lemma forces a real symmetric invariant \(\mathsf S_T\) to be scalar on this irreducible real sector, \(\mathsf S_T=\mu I_3\). If symmetry is reduced by defects or external fields, a general symmetric 3-by-3 correction is possible and may split the triplet.

For a coupled internal field \(b(t)\in\mathbb R^3\) transforming in an equivalent \(T_{2u}\) representation, the most general quadratic invariant block in the isotropic multiplicity-space form is
\[
S_{T,\mathrm{coupled}}=\frac12\int dt\left[
\dot a^T m_a\dot a+2\dot a^T m_{ab}\dot b+\dot b^Tm_b\dot b
-a^T k_a a-2a^T g b-b^Tk_b b
\right].
\]
The coefficients \(m_a,m_b,m_{ab},k_a,k_b,g\) are scalars on the triplet indices; the 2-by-2 kinetic multiplicity matrix must be positive definite, and the 2-by-2 stiffness multiplicity matrix must be positive definite for strict stability. The actual Q6/RGS data supply the representation sector and \(\lambda_T\), but do **not** supply the second equivalent triplet, its inertia, or the mixed coupling. Thus this is a symmetry-allowed model form, not a derived phonon–phason identification.

The eigenfrequencies follow from
\[
\det(\mathsf K_{\rm mult}-\omega^2\mathsf M_{\rm mult})=0,
\]
each multiplicity-space eigenvalue occurring with triplet degeneracy three while \(O_h\) remains unbroken.

## 5. How to establish a genuine internal/phason channel

The already available 188D sector and the shell-transfer maps are not interchangeable:
- \(T_{2u}\) is an irreducible representation label for the recovered point-cloud \(O_h\) action.
- The 30D \(T_{2u}\)-isotypic component contains multiple equivalent triplet copies; the first spectral triplet is selected by the specific constrained Coulomb Hessian.
- A shell tangent-fibre map is a separate finite-mesh transfer construction; its rank-two image does not prove a phason degree of freedom.
- Q6 incidence \(B_1,B_2\), graph cycles/cocycles, and the 188D geometric tangent constraints are distinct linear maps with distinct domains and codomains.

A physical phason identification requires an independently defined internal displacement observable, its transformation law under the actual Q6 symmetry subgroup, a kinetic term and a restoring/relaxational law, and an explicit map into the 188D tangent variables. The map must be tested for equivariance and rank; it cannot be inferred solely from the symbol \(T_{2u}\).

## 6. Consequence for T113 gravitational response

The EKN acoustic formula applies to stable propagating packets. The unshifted first T2u triplet above is unstable, so it cannot be inserted into
\[
-\frac{d\log c_\alpha}{d\log\rho_m}\frac{E_\alpha}{c_\alpha^2}.
\]
First identify a physically justified stabilizing contribution or a different positive spectral branch, then define density dependence and a metric-coupled action. For a relaxational internal mode, use an open-system response calculation rather than assigning it an acoustic speed.

Even after stabilization, a finite Q6 graph has no unique continuum \(T_{00}\) until a site-to-volume reconstruction/quadrature and metric coupling are specified. The full background-subtracted metric variation remains mandatory.

## 7. Reproducibility and epistemic status

Existing reconstruction:
```bash
python scripts/reconstruct_rgs_t2u_triplet.py
pytest -q tests/test_reconstruct_rgs_t2u_triplet.py
```

- **Numerically verified by the existing source test:** \(188\times3\) orthonormal first-triplet basis; \(T_{2u}\) isotypic rank 30; triplet eigenvalue near \(-0.06994933008401777\); gap and residual conditions.
- **Exact conditional consequence:** a negative stiffness eigenvalue with positive inertia gives an exponentially unstable linear mode; a scalar positive correction stabilizes it only above the stated threshold.
- **Open:** physical origin of any stabilizing correction; a second equivalent internal triplet and its coupling; identification as phason; density-dependent dispersion; continuum metric response and gravitational packet mass.

No new numerical test or CI execution is claimed by this theorem record.
