# Quadratic functional calculus for the Q6–RGS carrier

**Date:** 24 November 2026  
**Classification:** finite-dimensional operator identity, numerically verified from the stored arrays  
**Status:** verified on the selected rank-three sector; not a universal physical law

## 1. Independently reconstructed operators

The Q6 symmetric one-excitation sector has reduced Laplacian
\[
L_{\rm red}=\operatorname{diag}(0,4,6).
\]
The six-dimensional RGS carrier reconstructed from the original \(K_0,Z_A,Z_S\) arrays has compression
\[
K_c=\begin{pmatrix}H&-0.15I_3\\-0.15I_3&H\end{pmatrix},
\qquad
\operatorname{spec}(H)=\{0.65,0.75,0.85\}.
\]
The symmetric/antisymmetric diagonalization of this block gives lower and upper triplets
\[
K_- = H-0.15I,\qquad K_+=H+0.15I,
\]
with spectra \((0.5,0.6,0.7)\) and \((0.8,0.9,1.0)\). The splitting is exactly \(0.30I\), twice the magnitude of the off-diagonal coupling.

The ordered eigenbasis of \(H\) is used to identify the three lower RGS modes with the ordered Q6 modes \((0,4,6)\). This is the mode matching already used in the verified composite intertwiner; it is not a claim of a full 64-dimensional equivalence.

## 2. Derivation by spectral projectors

On the selected sector, the three spectral projectors of \(L_{\rm red}\) are the Lagrange polynomials
\[
P_0=\frac{(L_{\rm red}-4I)(L_{\rm red}-6I)}{24}
=I-\frac5{12}L_{\rm red}+\frac1{24}L_{\rm red}^2,
\]
\[
P_4=-\frac{L_{\rm red}(L_{\rm red}-6I)}8
=\frac34L_{\rm red}-\frac18L_{\rm red}^2,
\]
\[
P_6=\frac{L_{\rm red}(L_{\rm red}-4I)}{12}
=-\frac13L_{\rm red}+\frac1{12}L_{\rm red}^2.
\]
They are mutually orthogonal, sum to identity, and project onto eigenvalues 0, 4, and 6.

The lower RGS block assigns the independently measured eigenvalues \(1/2,3/5,7/10\) to these three modes. Hence its unique degree-at-most-two functional-calculus representative is
\[
\begin{aligned}
f(L_{\rm red})
&=\frac12P_0+\frac35P_4+\frac7{10}P_6\\
&=\boxed{\frac12I+\frac1{120}L_{\rm red}
+\frac1{240}L_{\rm red}^2}.
\end{aligned}
\]
This derives both coefficients by combining the independently reconstructed RGS carrier spectrum with the Q6 spectral projectors. Equivalently, solving the three coefficient equations gives
\[
a=\frac12,\quad 4b+16c=\frac1{10},\quad
6b+36c=\frac15,
\]
and therefore \(b=1/120\), \(c=1/240\).

The upper block is
\[
K_+=f(L_{\rm red})+\frac3{10}I.
\]

## 3. Numerical reproduction

The audit script now reconstructs \(H\) from the four original binary arrays, diagonalizes it, solves for the polynomial coefficients without hard-coding them, recognizes the resulting rationals, and asserts:
- coefficient vector \((a,b,c)=(1/2,1/120,1/240)\) within \(10^{-8}\);
- quadratic fit residual below \(10^{-8}\);
- upper/lower splitting residual below \(10^{-8}\);
- all previously established Q6, projector, carrier, and composite intertwining checks.

GitHub Actions run: [Q6 Vesica RGS numerical audit](https://github.com/fabianleonaressi95/theorem/actions/runs/45414155835). The run passed. The recovered floating coefficients were
\[
(0.5000000000000001,\;0.008333333333333677,\;0.004166666666666612),
\]
with rational recognition \((1/2,1/120,1/240)\), fit residual zero at reported precision, and upper/lower shift residual \(5.55\times10^{-17}\).

## 4. Scope

This is an exact algebraic identity on the selected three-dimensional spectral sector, numerically verified from the stored finite matrices. The polynomial is the unique degree-at-most-two representative on the three-point spectrum. The derivation does **not** prove that degree two is selected by a deeper physical principle, does not determine a continuum law, and does not establish an equivalence on all 64 Q6 states. Those remain open questions.
