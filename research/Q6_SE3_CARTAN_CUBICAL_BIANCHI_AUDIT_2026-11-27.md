# Q6 affine Cartan links and exact cubical Bianchi identity

**Status:** finite lattice identity and numerical covariance audit; not a continuum theorem.

## 1. Affine link construction

The existing finite Q6 Cartan audit supplies a source-frame coframe increment theta_gh and an SO(3) link U_gh, mapping source-frame components to target-frame components. Package them as
\[
\mathsf G_{gh}=(U_{gh},b_{gh}),\qquad b_{gh}=U_{gh}\theta_{gh},
\]
in \(SE(3)=SO(3)\ltimes\mathbb R^3\), with
\[
(U,b)(V,c)=(UV,b+Uc).
\]
Then the inverse is
\[
\mathsf G_{gh}^{-1}=(U_{gh}^{-1},-U_{gh}^{-1}b_{gh})
=(U_{gh}^{T},-\theta_{gh}).
\]
This exactly matches the reverse-edge convention already used by the Q6 coframe data:
\[
U_{hg}=U_{gh}^{T},\qquad \theta_{hg}=-U_{gh}\theta_{gh}.
\]
Thus the affine encoding resolves the orientation issue without changing the prior developed closure observable.

For a face loop, the affine holonomy is \(\mathsf H_p=(H_p,t_p)\). The closure vector in the base frame is
\[
\tau_p=H_p^{-1}t_p=H_p^Tt_p.
\]
The implementation compares H_p with the old rotational plaquette holonomy and tau_p with the old developed boundary closure defect. Both should agree to numerical precision.

## 2. Cube Bianchi identity from adjacent path swaps

Consider a 3-cube with coordinate directions a,b,c. Its six paths from the lower vertex to the opposite vertex are permutations of the three coordinate steps. Arrange them in the closed adjacent-swap cycle
\[
abc\to bac\to bca\to cba\to cab\to acb\to abc.
\]
Each adjacent swap changes the order of two consecutive steps. The two paths bound one square face. Let P be the transporter from the cube base to the prefix vertex of that swap, and H_f the corresponding face holonomy. Transport it back to the cube base:
\[
\widehat H_f=P^{-1}H_fP.
\]
The six transported face loops telescope in SE(3):
\[
\widehat H_6\widehat H_5\cdots\widehat H_1=I.
\]
This is an exact non-Abelian lattice Bianchi consistency identity. It is not a sum of six curvature matrices and does not assume commutativity. It is checked independently in rotational and translational components for all 160 elementary Q6 cubes.

## 3. Full affine gauge covariance

For arbitrary local frame changes g_v=(G_v,a_v) in SE(3), transform links by
\[
\mathsf G'_{gh}=g_h\mathsf G_{gh}g_g^{-1}.
\]
A face holonomy based at v must then satisfy
\[
\mathsf H'_p=g_v\mathsf H_pg_v^{-1}.
\]
The script tests this on all 240 faces and repeats the 160-cube Bianchi identity after deterministic random local affine frame changes. This includes both local rotations and local origin shifts.

## 4. Reproducibility

Run:
\`\`\`bash
python scripts/audit_q6_se3_cartan_bianchi.py
python -m unittest discover -s tests -p "test_q6_se3_cartan_bianchi.py" -v
\`\`\`

The test suite checks:
- exact reverse-link inversion;
- agreement with the previous SO(3) face holonomies and developed closure defects;
- all 160 cube Bianchi identities;
- full SE(3) gauge covariance of face holonomies and the cube identity.

## 5. Scope and limits

This is an exact finite group identity for the present Q6 link data. The translational face holonomy is a discrete closure/dislocation observable and a candidate torsion diagnostic. A continuum Cartan torsion 2-form, its Bianchi identity DT=R wedge e, and convergence under refinement remain to be established. The current model is spatial SO(3) semidirect R^3, not Lorentzian Spin(1,3); no variational action, physical time direction, TEGR equivalence, or direct polariton/Q-ball realization is claimed.


## CI result

Focused workflow run 46062090773 completed successfully:
https://github.com/fabianleonaressi95/theorem/actions/runs/46062090773

Measured residuals on the archived Q6 seed:
- affine rotational face holonomy versus the previous SO(3) plaquette holonomy: \(2.95\times10^{-16}\);
- affine base-frame closure versus the previous developed face torsion: \(1.40\times10^{-14}\);
- maximum rotational cube-Bianchi residual over 160 cubes: \(1.75\times10^{-14}\);
- maximum translational cube-Bianchi residual over 160 cubes: \(2.62\times10^{-14}\);
- full local SE(3) face-conjugation residuals: \(1.81\times10^{-15}\) (rotation), \(5.05\times10^{-15}\) (translation);
- Bianchi residuals after arbitrary local SE(3) frame changes: \(1.80\times10^{-14}\) (rotation), \(3.11\times10^{-14}\) (translation).

All four dedicated unit tests passed, and both cubical-chain and affine-Bianchi audit scripts completed successfully. These are finite-lattice numerical residuals; they do not prove a continuum limit or a physical field equation.
