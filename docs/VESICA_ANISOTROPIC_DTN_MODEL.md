# Vesica anisotropic multimode operator and DtN audit

**Record type:** model specification and reproducible numerical audit  
**Status:** finite-dimensional variational reduction derived; low-mode numerical checks implemented; full-domain endpoint analysis and multimode convergence remain open.

## 1. Geometry and anisotropy

Use the full Vesica, not a half-domain:
\[
-w(y)<X<w(y),\qquad
w(y)=\sqrt{1-y^2}-\frac12,\qquad |y|<\frac{\sqrt3}{2}.
\]
For the Eisenstein-direction triplet \((\kappa_1,\kappa_2,\kappa_3)=(2,1,2)\),
\[
A=\begin{pmatrix}11/4&\sqrt3/4\\ \sqrt3/4&9/4\end{pmatrix},
\qquad \det A=6.
\]
The PDE is \(-\nabla\cdot(A\nabla u)=\lambda u\), with Dirichlet data on the two moving lateral arcs. All DtN computations below are on an interior longitudinal interval \([a,b]\); they do not impose a boundary condition at the Vesica tips.

## 2. Moving transverse basis

Set
\[
t=\frac{X+w(y)}{2w(y)},\qquad
\phi_n(X;y)=w(y)^{-1/2}\sin(n\pi t).
\]
Then \(\int_{-w}^w\phi_m\phi_n\,dX=\delta_{mn}\), and
\[
\phi_{n,X}=\frac{n\pi}{2w^{3/2}}\cos(n\pi t),
\]
\[
\phi_{n,y}=-\frac{w'}{2w^{3/2}}\sin(n\pi t)
-\frac{n\pi w'}{w^{3/2}}(t-\tfrac12)\cos(n\pi t).
\]

For \(u_N=\sum_{n=1}^N f_n(y)\phi_n(X;y)\), define
\[
C_{mn}=\int\phi_m\phi_{n,y}\,dX,\quad
G_{mn}=\int\phi_{m,y}\phi_{n,y}\,dX,
\]
\[
B_{mn}=\int\phi_{m,X}\phi_n\,dX,\quad
D_{mn}=\int\phi_{m,X}\phi_{n,y}\,dX.
\]
The integrals are over \((-w(y),w(y))\). Orthonormality and the vanishing lateral trace imply \(C^T=-C\) and \(B^T=-B\); \(G\) is symmetric.

An important index check: differentiating \(u_N\) and contracting indices gives
\[
\int |u_y|^2\,dX
=|f'|^2+2f'^T C f+f^T Gf,
\]
whereas
\[
\int u_Xu_y\,dX=f'^T B^T f+f^T Df
=-f'^T Bf+f^T Df.
\]
Thus the two cross terms have different signs after using skew-symmetry. In particular, the \(C\)-term is **positive** in this convention and the \(B\)-term is **negative**.

## 3. Correct finite-dimensional quadratic form

Writing \(A=\begin{pmatrix}a&c\\c&d\end{pmatrix}\), here
\(a=11/4\), \(c=\sqrt3/4\), \(d=9/4\), and
\[
S(y)=\operatorname{diag}\left(\frac{n^2\pi^2}{4w(y)^2}\right)_{n=1}^N,
\]
the exact Ritz quadratic form is
\[
Q_N[f]=\int_a^b\left[
a f^TSf
+d\left(|f'|^2+2f'^TCf+f^TGf\right)
+2c\left(-f'^TBf+f^TDf\right)
\right]dy.
\]
Equivalently,
\[
\mathcal L=f'^THf'+2f'^TKf+f^TWf,
\]
with
\[
H=dI,\qquad K=dC-cB,\qquad
W=aS+dG+c(D+D^T).
\]
The generalized eigenvalue problem is obtained by subtracting
\(\lambda\int |f|^2dy\).

The distinction \(G\ne C^TC\) is essential: \(G\) includes the component of \(\partial_y\phi_n\) outside the first \(N\) basis functions.

## 4. First-order system and DtN

The variational momentum is
\[
p=Hf'+Kf.
\]
The Euler–Lagrange equation is
\[
p'-K^Tf'-Wf+\lambda f=0.
\]
Since \(H=dI\) is constant, the state \(Y=(f,p)^T\) obeys
\[
Y'=\mathcal A(y,\lambda)Y,\quad
\mathcal A=
\begin{pmatrix}
-H^{-1}K&H^{-1}\\
W-\lambda I-K^TH^{-1}K&K^TH^{-1}
\end{pmatrix}.
\]
For the canonical matrix \(J=\begin{psmallmatrix}0&I\\-I&0\end{psmallmatrix}\),
\[
\mathcal A^TJ+J\mathcal A=0.
\]
Consequently the exact fundamental matrix is symplectic; numerical integration should monitor
\(\|M^TJM-J\|\).

Partition \(M(b,a)=\begin{psmallmatrix}A&B\\C&D\end{psmallmatrix}\).
When \(B\) is invertible, the DtN map for outward variational fluxes
\((-p(a),p(b))\) is
\[
\Lambda_N(\lambda)=
\begin{pmatrix}
B^{-1}A&-B^{-1}\\
C-DB^{-1}A&DB^{-1}
\end{pmatrix}.
\]
It should be symmetric away from Dirichlet poles. A large symplectic residual or an ill-conditioned \(B\) block invalidates a numerical certification, even if the printed matrix appears plausible.

## 5. Reproducibility

Run:
\`\`\`bash
python scripts/audit_vesica_anisotropic_dtn.py --max-modes 4
pytest -q tests/test_vesica_anisotropic_dtn.py
\`\`\`
The script uses Gauss–Legendre quadrature for the moving-basis matrices and DOP853 for the transfer system. Tests compare the reduced quadratic form against direct integration of the original two-dimensional energy, check \(C^T=-C\), \(B^T=-B\), \(G^T=G\), verify the Hamiltonian generator, and test transfer/DtN symmetry at low truncation.

The transfer matrix becomes increasingly ill-conditioned as \(N\) grows because transverse energies scale like \(n^2/w^2\). The audit therefore prints the symplectic residual and warns when it is too large; it does not interpret a failed high-mode residual as convergence. A stable multiple-shooting, Riccati, or high-precision method is needed before certifying \(N=8,16,\ldots\).

## 6. Status and open obligations

- **Derived:** the finite-\(N\) variational form and its first-order Hamiltonian system.
- **Implemented:** geometric matrix assembly, direct-energy identity check, transfer matrix, and interior DtN.
- **Numerical checks:** limited to the truncations and tolerances reported by an actual run of the audit.
- **Open:** stable high-\(N\) DtN, convergence as \(N\to\infty\), and the singular tip limit \(w(y)\to0\).
- **Not implied:** the triplet \((2,1,2)\) is a model choice; the norm-three Eisenstein chord does not uniquely determine it. No digamma or Fibonacci formula is asserted here.
