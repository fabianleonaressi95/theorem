# Exact quaternionic (2I) real Molien audit

**Date:** 16 November 2026  
**Status:** exact finite computation in (mathbb Q(sqrt5)); the general Fischer/Peter–Weyl identity is proved independently in [S013, §§2.1 and 4](../../theorems/S013-general-spherical-space-form-molien-diagonal-actions.md).

## Construction

Write (q=(a,b,c,d)=a+bi+cj+dk), with coordinates in (mathbb Q(sqrt5)), and
[
arphi=rac{1+sqrt5}{2},qquad arphi^{-1}=rac{sqrt5-1}{2}.
]
The vertex set used is the standard 600-cell set:
- the eight coordinate units ((pm1,0,0,0)) and their coordinate permutations;
- the sixteen points ((pmrac12,pmrac12,pmrac12,pmrac12));
- the 96 points obtained from the twelve even coordinate permutations of
  ((0,1,arphi^{-1},arphi)/2), with independent signs on **all three nonzero coordinates wherever they occur**.

The last qualification matters: signs must not be applied only to coordinates 2–4 after permutation, because the zero coordinate moves under the permutation. The construction produces 120 distinct unit quaternions.

All arithmetic in the audit uses pairs of rational numbers (r+ssqrt5), not floating-point rounding. The script checks all (120^2=14{,}400) Hamilton products for closure and checks all 120 quaternionic inverses.

## Real four-dimensional action and determinant

For scalar-first coordinates, left multiplication (L_q:xmapsto qx) has matrix
[
L_q=
egin{pmatrix}
a&-b&-c&-d\
b&a&-d&c\
c&d&a&-b\
d&-c&b&a
end{pmatrix}.
]
For (a^2+b^2+c^2+d^2=1), direct determinant expansion gives
[
oxed{det(I-tL_q)=(1-2at+t^2)^2.}
]
The script computes each (4	imes4) determinant by the 24-term Leibniz formula over (mathbb Q(sqrt5)), then checks this identity for all 120 group elements. It expands the reciprocal determinant series by exact coefficient recurrence and averages the 120 series.

Thus the computed real Molien function is the exact finite sum
[
M_{mathbb R^4}(t)=rac1{120}
sum_{qin2I}rac1{(1-2,operatorname{Re}(q)t+t^2)^2}.
]

## Result and independent comparison

Let
[
A(t)=rac{1+t^{30}}{(1-t^{12})(1-t^{20})}
=sum_{ellge0}c_ell t^ell,
]
so, explicitly,
[
c_ell=#{(p,q,epsilon)inmathbb Z_{ge0}^2	imes{0,1}:
12p+20q+30epsilon=ell}.
]
For the left action of (2Isubset SU(2)) on (S^3simeq SU(2)), Peter–Weyl gives
[
dimmathcal H_ell(S^3)^{2I}=(ell+1)c_ell.
]
The orthogonal Fischer decomposition
(P_ell(mathbb R^4)=mathcal H_ell(mathbb R^4)oplus
r^2P_{ell-2}(mathbb R^4)) then gives
[
oxed{
M_{mathbb R^4}(t)=
rac{A(t)+tA'(t)}{1-t^2}.
}
]
This is a theorem under the specified orthogonal left action, not an empirical assumption. The direct 4D Molien computation is an independent finite-group check of the formula.

The exact coefficient comparison passes at every degree (0le nle60). The coefficients of the real Molien series in degrees 0–60 are:
[
egin{aligned}
(&1,0,1,0,1,0,1,0,1,0,1,0,14,0,14,0,14,0,14,0,35,0,35,0,60,0,60,0,60,0,91,0,124,0,124,0,161,0,161,0,202,0,245,0,290,0,290,0,339,0,390,0,443,0,498,0,555,0,555,0,677).
end{aligned}
]

The optional SymPy check simplifies the complete finite sum exactly and verifies the rational-function identity above, not merely a truncated series. The script remains runnable without SymPy; its core construction, closure, determinant and coefficient audit use only the Python standard library.

## Reproduction

From the repository root:

```bash
python scripts/audit_2i_real_molien_exact.py
pytest -q tests/test_2i_real_molien_exact.py
```

Files:
- [exact audit script](../../scripts/audit_2i_real_molien_exact.py)
- [regression tests](../../tests/test_2i_real_molien_exact.py)
- [T119 group record](../../theorems/T119-binary-icosahedral-group-and-selected-representations.md)
- [S013 general Molien framework](../../theorems/S013-general-spherical-space-form-molien-diagonal-actions.md)

**Evidence boundary:** this certifies the specified finite quaternionic group, its left real four-dimensional representation, and the stated Molien coefficients/rational identity. It does not by itself establish any additional physical interpretation or a new Q6 coupling.
