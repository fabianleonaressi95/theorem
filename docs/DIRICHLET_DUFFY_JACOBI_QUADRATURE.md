# Dirichlet-weighted triangle quadrature: Duffy–Gauss–Jacobi audit

**Status:** exact change of variables and Gamma/Beta normalization; implementation supplied with A1–A3 regression tests. Test execution is not claimed by this document.

## 1. Duffy map and Jacobian

On the reference simplex use
\[
\lambda_0=(1-s)(1-t),\qquad
\lambda_1=s,\qquad
\lambda_2=(1-s)t,\qquad 0\leq s,t\leq1.
\]
The Jacobian is \(1-s\). Thus the Dirichlet weight becomes
\[
\prod_i\lambda_i^{a_i-1}\,d\lambda_1d\lambda_2
=s^{a_1-1}(1-s)^{a_0+a_2-1}
t^{a_2-1}(1-t)^{a_0-1}\,ds\,dt.
\]

For SciPy's convention
\[
\operatorname{roots\_jacobi}(n,\alpha,\beta):
\quad (1-x)^\alpha(1+x)^\beta,
\]
the parameters are
\[
\alpha_s=a_0+a_2-1,\quad \beta_s=a_1-1,
\qquad
\alpha_t=a_0-1,\quad \beta_t=a_2-1.
\]
Under \(x\mapsto(x+1)/2\), each one-dimensional weight receives its own factor
\(2^{-(\alpha+\beta+1)}\). The physical triangle integral has the additional factor \(2A_F\).

## 2. Normalization

The product Jacobi weight integrates to
\[
B(a_1,a_0+a_2)B(a_2,a_0)
=\frac{\Gamma(a_0)\Gamma(a_1)\Gamma(a_2)}{\Gamma(a_0+a_1+a_2)}.
\]
Therefore
\[
Z_F(a)=2A_F\frac{\prod_i\Gamma(a_i)}{\Gamma(S)}.
\]
For \(a=(1,1,1)\), the reference-square weight integrates to \(1/2\), so
\(Z_F=A_F\), as required for the uniform triangle measure.

## 3. Raw second moment versus covariance

The quadrature routine returns
\[
m_i=\mathbb E[\lambda_i],\qquad
M_{ij}=\mathbb E[\lambda_i\lambda_j].
\]
The covariance is **not** \(M\). It is
\[
C=M-mm^T,\qquad \Sigma_F=V^TCV,
\]
where the rows of \(V\) are the physical triangle vertices. The exact Dirichlet covariance is
\[
C_{ij}=\frac{a_i(S\delta_{ij}-a_j)}{S^2(S+1)}.
\]
The code exposes both arrays with distinct names to prevent the raw-moment/covariance confusion.

## 4. Regression protocol

- **A1:** uniform parameters \(a=(1,1,1)\); \(Z_F=A_F\), centroid is the vertex average, and covariance reduces to T068.
- **A2:** nonuniform \(a=(2,3,4)\); numerical mean and covariance agree with the closed Dirichlet formula.
- **A3:** constant normalization and a degree-two weighted polynomial integral are checked at two quadrature orders.
- Invalid parameters and degenerate triangles are rejected.

Source: src/dirichlet_triangle_quadrature.py. Tests: tests/test_dirichlet_triangle_quadrature.py.

This is a local cell quadrature tool. It does not establish global football-shell refinement, Mosco convergence, or Morandotti surface homogenisation.
