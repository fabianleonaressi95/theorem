# T041 — Barnes derivative at zero and the weighted exceptional Rumin contribution

## 1. Fixed convention

Use the unscaled Barnes double zeta
\[
\zeta_2(z,a\mid w_1,w_2)=
\sum_{r,s\ge0}(a+r w_1+s w_2)^{-z}.
\]
To avoid convention ambiguities among multiple-gamma normalizations, define
\[
\Gamma_2^{B}(a\mid w_1,w_2)
:=\exp\left(\left.\partial_z\zeta_2(z,a\mid w_1,w_2)\right|_{z=0}\right).
\]
All Barnes gamma symbols below mean precisely this function.

T040 gives, for one exceptional boundary orientation,
\[
Z_{\partial}(s)=4^s\{\zeta_2(2s,2\mid12,20)
+\zeta_2(2s,32\mid12,20)\}.
\]

## 2. Exact evaluation at zero

The Barnes value at zero is
\[
\zeta_2(0,a\mid w_1,w_2)=\frac12 B_{2,2}(a\mid w_1,w_2),
\]
where
\[
B_{2,2}(a\mid w_1,w_2)
=a^2-a(w_1+w_2)+\frac{w_1^2+w_2^2+3w_1w_2}{6}.
\]
For \((w_1,w_2)=(12,20)\), the constant in the numerator is \(632/3\). Therefore
\[
\zeta_2(0,2\mid12,20)=\frac{226}{3},\qquad
\zeta_2(0,32\mid12,20)=\frac{316}{3},
\]
and
\[
\boxed{Z_{\partial}(0)=\frac{542}{3}.}
\]

Differentiating the T040 identity at zero gives
\[
\boxed{
Z'_{\partial}(0)=\frac{542}{3}\log4+
2\log\left[
\Gamma_2^B(2\mid12,20)\,
\Gamma_2^B(32\mid12,20)
\right].
}
\]
This is an exact closed special-function expression. T041 does not present a decimal approximation: it would require a separately validated numerical implementation of the Barnes double gamma with these non-coprime periods.

The zeta-regularized determinant of the single boundary Laplacian block is
\[
\log\det_\zeta\Delta_{\partial}=-Z'_{\partial}(0).
\]

## 3. Alternating Rumin weight in contact dimension three

For a three-dimensional contact manifold, \(n=1\), and Kitaoka's contact torsion function is
\[
\kappa_E(s)=\sum_{k=0}^{1}(-1)^{k+1}(2-k)
\zeta(\Delta_E^k)(s)
=-2\zeta(\Delta_E^0)(s)+\zeta(\Delta_E^1)(s).
\]

Kitaoka Proposition 1.1 places the exceptional cases VI and VII in bidegrees \((1,0)\) and \((0,1)\), respectively. Both are components of Rumin degree \(k=1\). Their alternating coefficient is therefore
\[
(-1)^{1+1}(2-1)=+1
\]
for each sector. Keeping the two orientations distinct, their combined contribution to the torsion function is
\[
\boxed{\kappa_{\partial}(s)=Z_{VI}(s)+Z_{VII}(s)=2Z_{\partial}(s).}
\]
Consequently,
\[
\kappa'_{\partial}(0)=2Z'_{\partial}(0),\qquad
\log T_{\partial}=\frac12\kappa'_{\partial}(0)=Z'_{\partial}(0).
\]
This last quantity is only the partial contribution of the two exceptional degree-one families.

In particular, the partial value \(\kappa_{\partial}(0)=1084/3\) is not expected to vanish by itself. Any vanishing statement for the full torsion function concerns the complete alternating sum, including the other spectral families.

## 4. Reproducibility

- src/t041_boundary_barnes_determinant.py: exact Bernoulli-polynomial evaluation, Barnes-gamma derivative expression, determinant sign, and Rumin grading weight.
- tests/test_t041_boundary_barnes_determinant.py: exact rational tests, a (1,1)-period Barnes-zeta sanity check, degree-one weights, and scope guards.
- data/t041_boundary_barnes_determinant.json: machine-readable exact audit.

Commands:
\`\`\`bash
python -m pytest tests/test_t041_boundary_barnes_determinant.py -q
python -m src.t041_boundary_barnes_determinant
\`\`\`

## 5. Status ledger

| Claim | Status |
|---|---|
| T040 Barnes representation | Exact from the T039 Molien coefficient |
| \(\zeta_2(0,2\mid12,20)=226/3\), \(\zeta_2(0,32\mid12,20)=316/3\) | Exact Bernoulli-polynomial evaluation |
| \(Z'_{\partial}(0)\) in terms of the fixed Barnes double gamma | Exact differentiation identity |
| VI and VII each have Rumin degree one | Source identification from Kitaoka Proposition 1.1 |
| Their coefficient in \(\kappa_E\) is \(+1\) each | Exact from the alternating definition for \(n=1\) |
| Numerical Barnes-gamma value | Not evaluated |
| Complete \(\kappa_E'(0)\) and torsion on \(S^3/2I\) | Open |

## References

1. A. Kitaoka, Analytic torsions associated with the Rumin complex on contact spheres, arXiv:1911.03092, Proposition 1.1 (exceptional VI/VII) and definition of \(\kappa_E\).
2. T040, theorems/T040-boundary-barnes-zeta.md.
3. F003, bibliography/spin-geometry-quaternionic/KITAOKA_RUMIN_FORMULA_AUDIT.md, sections 2–4 and 6.
4. Barnes double zeta: generalized Bernoulli value at zero, derived from the generating function \(t^2e^{-at}/((1-e^{-w_1t})(1-e^{-w_2t}))\).

## Classification

T041 closes the exact \(s=0\) value and Barnes-gamma expression for the two exceptional boundary sectors and fixes their alternating coefficient in the three-dimensional Rumin torsion function. It does not compute the full torsion of \(S^3/2I\).
