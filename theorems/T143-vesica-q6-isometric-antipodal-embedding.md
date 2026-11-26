# T143 — Vesica embedding with the geometric RGS AntiTwin

**Record type:** exact finite-dimensional embedding and diagonal-extension theorem.  
**Status:** algebraic identities are proved under the stated involution \(p(g)=g\oplus7\). The archive reports this geometric labelling, but this PR does not claim an independent binary replay of the RGS matrices. Transport-based phase selection remains open.

## 1. Geometric antipodal involution and canonical representatives

For \(g\in\{0,\ldots,63\}\), take
\[
p(g)=g\oplus7,\qquad J_{\rm RGS}e_g=e_{p(g)}.
\]
This is the geometric AntiTwin convention documented by the archived RGS audit through the minimizer of \(\|X_h+X_g\|\). It is adopted here as an archive-documented convention, not newly recomputed from the binary matrices.

Choose the canonical representative
\[
r=\min(g,g\oplus7),\qquad r<r\oplus7.
\]
The complete set is
\[
R=\{0,1,2,3,8,9,10,11,16,17,18,19,24,25,26,27,
32,33,34,35,40,41,42,43,48,49,50,51,56,57,58,59\}.
\]
The three Vesica pairs are
\[
(2,5),\qquad(3,4),\qquad(9,14),
\]
with representatives \(2,3,9\). The remaining 29 representatives are exactly
\[
\begin{aligned}
R_{\rm free}=\{&0,1,8,10,11,16,17,18,19,24,25,26,27,\\
&32,33,34,35,40,41,42,43,48,49,50,51,56,57,58,59\}.
\end{aligned}
\]
Each element labels one distinct pair; there is no overlap with the three fixed pairs.

## 2. Six-state Vesica embedding

Order the six Vesica points as
\[
(1,\omega,\omega^2,-1,-\omega,-\omega^2),\qquad \omega=e^{2\pi i/3}.
\]
Define
\[
\begin{aligned}
\iota\delta_1&=e_3,& \iota\delta_\omega&=e_5,&
\iota\delta_{\omega^2}&=e_9,\\
\iota\delta_{-1}&=e_4,& \iota\delta_{-\omega}&=e_2,&
\iota\delta_{-\omega^2}&=e_{14}.
\end{aligned}
\]
The six labels are distinct, hence \(\iota^\dagger\iota=I_6\). Let \(J_6\) exchange the first and last three basis vectors. Since \(3\leftrightarrow4\), \(5\leftrightarrow2\), and \(9\leftrightarrow14\) under \(p\),
\[
\boxed{J_{\rm RGS}\iota=\iota J_6.}
\]
The image is invariant and has three states of each Hamming-parity.

## 3. Coordinate operators and zero extension

On the six-state basis set
\[
X=\operatorname{diag}(\Re z_k),\qquad
Y=\operatorname{diag}(\Im z_k).
\]
Then \(X,Y\) are Hermitian, odd under \(J_6\), and \(X^2+Y^2=I_6\). Define
\[
\widetilde X_0=\iota X\iota^\dagger,\quad
\widetilde Y_0=\iota Y\iota^\dagger,\quad
\Pi=\iota\iota^\dagger.
\]
Exactly,
\[
\widetilde X_0^2+\widetilde Y_0^2=\Pi
\]
(not \(I_{64}\)), and
\[
J_{\rm RGS}\widetilde X_0J_{\rm RGS}=-\widetilde X_0,\qquad
J_{\rm RGS}\widetilde Y_0J_{\rm RGS}=-\widetilde Y_0.
\]
The zero extensions have ranks 6 and 4; \(\Pi\) has rank 6. The orthogonal complement has dimension 58, split 29+29 under \(J_{\rm RGS}\). The embedded even-to-odd block ranks are 3 for \(X\) and 2 for \(Y\).

## 4. Full diagonal extension and the 29 angles

Assume additionally that the full operators are real diagonal multipliers in the Q6 vertex basis. Fix values at the **canonical representatives**:
\[
(a_2,b_2)=\left(\frac12,-\frac{\sqrt3}{2}\right),\quad
(a_3,b_3)=(1,0),\quad
(a_9,b_9)=\left(-\frac12,-\frac{\sqrt3}{2}\right).
\]
The value at representative 2 is the coordinate of label 2, namely \(-\omega\), not \(\omega\). On partners 5, 4, 14 the values are the negatives, so the six embedded entries agree with T142.

For each \(r\in R_{\rm free}\), choose \(\theta_r\in\mathbb R/(2\pi\mathbb Z)\) and put
\[
(a_r,b_r)=(\cos\theta_r,\sin\theta_r),\qquad
(a_{r\oplus7},b_{r\oplus7})=-(a_r,b_r).
\]
With \(X_{\rm RGS}=\operatorname{diag}(a_g)\) and \(Y_{\rm RGS}=\operatorname{diag}(b_g)\), one obtains
\[
J_{\rm RGS}X_{\rm RGS}J_{\rm RGS}=-X_{\rm RGS},\quad
J_{\rm RGS}Y_{\rm RGS}J_{\rm RGS}=-Y_{\rm RGS},\quad
\boxed{X_{\rm RGS}^2+Y_{\rm RGS}^2=I_{64}.}
\]
This is a 29-parameter family only within the diagonal real-multiplier ansatz; it is neither a canonical extension nor a classification of general nondiagonal extensions.

## 5. Transport and phase-selection gate

The archived A13 package identifies SO(3) edge transports, SU(2) lifts and 240 plaquette holonomies. Aggregate curvature-angle statistics do not determine a vertex phase \(u_g=a_g+ib_g\), nor prove path independence.

A geometric phase assignment must specify an edge transport law relating \(u_h\) to \(u_g\) and satisfy its loop-consistency conditions. The audit gates are separate:
1. compare \(p(g)=g\oplus7\) with \(\arg\min_h\|X_h+X_g\|\);
2. check \(p(p(g))=g\);
3. check \(J_{\rm RGS}\iota=\iota J_6\);
4. check the proposed phase law against archived \(R_{\rm SO(3)}\), \(U_{\rm SU(2)}\), and plaquette holonomies.

Nontrivial holonomy may obstruct a path-independent global phase or make it gauge-dependent. No flatness, unique phase law, or selection of the 29 angles is claimed. Replaying the binary archives and specifying the phase action remain open.

## 6. Evidence and limitations

**Exact algebraic results:** canonical pair enumeration; the 29/3 partition; isometry; intertwining conditional on the archive-documented \(p\); zero-extension identities and ranks; and the 29-angle diagonal family.

**Documented but not independently replayed here:** extraction of \(p(g)=g\oplus7\) from the archived embedding.

**Open:** independent binary reproduction of the antipodal argmin; transport/holonomy replay; a gauge-covariant phase law; geometric selection of the 29 angles; a justified nondiagonal extension; and physical PSU–AntiTwin dynamics.

## 7. Reproduction

\`\`\`bash
python scripts/audit_t143_vesica_q6_embedding.py
python -m unittest tests.test_t143_vesica_q6_embedding
\`\`\`
