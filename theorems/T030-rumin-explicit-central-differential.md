# T030 — Explicit local Rumin middle differential and chain identities

**Repository:** fabianleonaressi95/theroem  
**Branch:** theorems/T030-rumin-explicit-central-differential  
**Scope:** three-dimensional contact complex, local middle differential, chain identities, formal adjoint, and the limits of the comparison with sphere/torsion normalizations.

> T027 already exists as a separate McKay–Molien bridge. This file is a separate local-operator audit and does not replace T027.

## 1. Status ledger

| Claim | Status |
|---|---|
| Unique normalized representative in the middle degree | Proved algebraically under the contact hypothesis |
| Local Darboux formula for the middle differential | Derived algebraically in the convention below |
| Ordinary differential order two | Proved |
| Heisenberg homogeneous order two | Proved by weighted derivative counting |
| Both complex identities adjacent to the middle differential | Proved algebraically |
| Formal adjoint in the left-invariant model | Derived algebraically |
| Equality with every Kitaoka normalization | Not asserted |
| Spectral/torsion equality on S³/2I | Not established here |

## 2. Contact data and sign conventions

Let M be a three-dimensional co-oriented contact manifold. Fix a contact form theta with

$$
\\theta\\wedge d\\theta\\ne0,
\\qquad H=\\ker\\theta.
$$

Let T be its Reeb vector field:

$$
\\theta(T)=1,\\qquad \\iota_Td\\theta=0.
$$

In a Darboux chart choose

$$
\\theta=dt+\\frac12(x\\,dy-y\\,dx),
\\qquad d\\theta=dx\\wedge dy,
$$

and the horizontal frame

$$
X=\\partial_x+\\frac y2\\partial_t,
\\qquad
Y=\\partial_y-\\frac x2\\partial_t,
\\qquad T=\\partial_t.
$$

Then

$$
[X,Y]=-T,\\quad [T,X]=[T,Y]=0,
\\quad d\\theta(X,Y)=1.
$$

The coframe (theta, dx, dy) is dual to (T, X, Y), and the volume form is

$$
dV=\\theta\\wedge dx\\wedge dy.
$$

Every displayed sign below is tied to this convention.

## 3. Middle-degree quotient and annihilator

In contact dimension three, the middle Rumin bundles are

$$
E^1=\\Omega^1(M)/\\langle\\theta\\rangle,
\\qquad
E^2=J^2,
$$

where

$$
J^2=\\{\\omega\\in\\Omega^2(M):\\theta\\wedge\\omega=0\\}.
$$

Thus a section of E² has the local form

$$
\\gamma=p\\,\\theta\\wedge dx+q\\,\\theta\\wedge dy.
$$

The Rumin complex in this dimension is

$$
\\Omega^0(M)\\xrightarrow{d_H^0}E^1
\\xrightarrow{D_R}E^2
\\xrightarrow{d_H^2}\\Omega^3(M).
$$

The first arrow is induced by exterior differentiation followed by projection to the horizontal quotient. The last arrow is exterior differentiation restricted to E². The middle arrow requires a normalized representative.

## 4. Normalized representative and explicit D_R

Represent a class in E¹ by its horizontal representative

$$
\\alpha=a\\,dx+b\\,dy.
$$

Every representative of this class is alpha + f theta. There is a unique f for which

$$
\\beta=\\alpha+f\\theta,
\\qquad \\theta\\wedge d\\beta=0.
$$

Indeed,

$$
d\\beta=d\\alpha+df\\wedge\\theta+f\\,d\\theta.
$$

Wedge with theta. The term theta wedge df wedge theta vanishes, hence

$$
\\theta\\wedge d\\alpha+f\\,\\theta\\wedge d\\theta=0.
$$

Since theta wedge dtheta is nowhere zero, f is uniquely determined.

In the chosen Darboux frame, direct expansion gives

$$
d\\alpha=(Xb-Ya)\\,dx\\wedge dy
 +(Ta)\\,\\theta\\wedge dx
 +(Tb)\\,\\theta\\wedge dy.
$$

Therefore

$$
\\boxed{f=Ya-Xb.}
$$

Define the middle differential by

$$
D_R[\\alpha]=d\\beta=d(\\alpha+f\\theta).
$$

Using df wedge theta = -Xf theta wedge dx -Yf theta wedge dy, we obtain

$$
\\boxed{
D_R[\\alpha]
=(Ta-Xf)\\,\\theta\\wedge dx
 +(Tb-Yf)\\,\\theta\\wedge dy,
\\qquad f=Ya-Xb.
}
$$

In components:

$$
\\boxed{
D_R(a,b)=
\\begin{pmatrix}
Ta-X(Ya-Xb)\\\\
Tb-Y(Ya-Xb)
\\end{pmatrix}.
}
$$

This is an ordinary differential operator of order two. Under Heisenberg weights wt(X)=wt(Y)=1 and wt(T)=2, every term has homogeneous weight two. It is therefore **not** of homogeneous order four.

The construction is intrinsic: take a class in the quotient, choose its unique representative beta satisfying theta wedge d beta = 0, and apply d. The displayed formula is its Darboux-coordinate expression.

## 5. Outer differentials

For a function u,

$$
d_H^0u=[du]=(Xu,Yu).
$$

For gamma = p theta wedge dx + q theta wedge dy, exterior differentiation gives

$$
\\boxed{
d_H^2\\gamma=(Yp-Xq)\\,dV.
}
$$

For example, d(p theta wedge dx) = dp wedge theta wedge dx = Yp dV, while d(q theta wedge dy) = -Xq dV. This fixes the sign in the last arrow.

## 6. Chain identities

### 6.1 The identity D_R d_H^0 = 0

For u, choose alpha = (Xu)dx + (Yu)dy. Its normalization coefficient is

$$
f=Y(Xu)-X(Yu)=[Y,X]u=Tu,
$$

because [X,Y] = -T. Thus beta = alpha + (Tu)theta = du, and

$$
D_R(d_H^0u)=d(du)=0.
$$

### 6.2 The identity d_H^2 D_R = 0

By construction D_R[alpha] = d beta. Consequently

$$
d_H^2(D_R[\\alpha])=d(d\\beta)=0.
$$

### 6.3 Well-definedness on the quotient

The condition theta wedge d(alpha + f theta) = 0 has exactly one solution f. If alpha is replaced by another representative of the same class, the normalized one-form beta is unchanged. Hence d beta depends only on the class in E¹.

### 6.4 The outer complex identities

The identity d² = 0 also gives the vanishing of the composition of consecutive exterior-differential arrows wherever defined. The Rumin complex is therefore a differential complex, not merely a sequence of operators.

## 7. Formal adjoints in the left-invariant Heisenberg model

Equip the model with the left-invariant metric for which (theta, dx, dy) is orthonormal, and use dV = theta wedge dx wedge dy. The fields X, Y, T are divergence-free for Haar volume, so

$$
X^*=-X,\\qquad Y^*=-Y,\\qquad T^*=-T.
$$

It follows that

$$
(d_H^0)^*(p,q)=-Xp-Yq,
$$

and

$$
(d_H^2)^*h=(-Yh,Xh).
$$

For the middle operator write C = Ya - Xb. Then

$$
D_R(a,b)=(Ta-XC,Tb-YC)
$$

or, as an operator matrix,

$$
D_R=
\\begin{pmatrix}
T-XY & X^2\\\\
-Y^2 & T+YX
\\end{pmatrix}.
$$

Taking formal adjoints reverses operator order. In particular, (XY)* = YX and (YX)* = XY. Therefore

$$
\\boxed{
D_R^*(u,v)=
\\begin{pmatrix}
-T-YX & -Y^2\\\\
X^2 & -T+XY
\\end{pmatrix}
\\begin{pmatrix}u\\\\v\\end{pmatrix}.
}
$$

Equivalently, its two components are

$$
(D_R^*(u,v))_1=(-T-YX)u-Y^2v,
$$

$$
(D_R^*(u,v))_2=X^2u+(-T+XY)v.
$$

This is a formal local adjoint for the stated metric and volume. It does not specify global operator domains or self-adjoint extensions on a compact quotient.

No identity of the form D_R* = -*D_R* is assumed. Such a formula must be checked against the precise Hodge star, bundle metrics, degree conventions, and signs in the source under comparison.

## 8. Exact intertwiner supplied by normalization

Let q: Omega¹ -> E¹ be the quotient map. Let s: E¹ -> Omega¹ assign to each class its unique normalized representative. Then

$$
q\\circ s=\\operatorname{id}_{E^1},
\\qquad D_R=d\\circ s.
$$

This is the exact middle-arrow identity. The map s is a differential operator of order one in the chosen contact splitting, not a pointwise bundle isomorphism. It gives the corrected-representative realization of the intrinsic Rumin differential.

This identity does **not** prove a unitary equivalence with a differently normalized operator in Kitaoka. Such a comparison additionally needs:
- an explicit identification of the bundles;
- the same contact form and Reeb normalization;
- matching CR structure and orientation;
- matching coefficient bundle and unitary representation;
- matching L² metrics and formal adjoints;
- matching Laplacian and determinant-line conventions.

No global spectral intertwiner is claimed in this document.

## 9. Geometric descent to S³/2I: scope

The standard CR/contact structure on S³ is invariant under SU(2). The binary icosahedral group 2I is a finite subgroup of SU(2) acting freely on S³ by left multiplication. Hence the contact and CR structures descend to S³/2I.

The Hopf circle action is realized by right multiplication and commutes with the left SU(2) action, so it descends as a circle action on the quotient. Its quotient base is the icosahedral spherical orbifold. The fundamental group of S³/2I is 2I.

A unitary representation rho: 2I -> U(r) defines a flat unitary coefficient bundle. The trivial representation and nontrivial twists must be analyzed separately.

These geometric facts identify a natural setting for applying contact/CR analytic-torsion results. They do not, by themselves, verify every hypothesis of a particular theorem or prove equality with Kitaoka's spectral formulas. In particular, the local differential calculation above is not a torsion computation.

## 10. Remaining proof obligations

1. Read the full Rumin–Seshadri and Kitaoka texts and record the exact operator definitions, equation numbers, and hypotheses.
2. Fix a common contact form, Reeb period, orientation, CR metric, and coefficient-bundle convention.
3. Construct the 2I-equivariant bundle maps before descending to the quotient.
4. Verify the operator diagram on smooth sections.
5. Prove unitarity for the selected L² structures, or compute the conjugating density.
6. Compare Laplacians and their zero-mode spaces.
7. Only then compare zeta functions, determinant lines, and analytic torsion.

## 11. References

1. M. Rumin, “Formes différentielles sur les variétés de contact,” Journal of Differential Geometry 39 (1994), 281–330.
2. M. Rumin and N. Seshadri, “Analytic torsions on contact manifolds,” Annales de l’Institut Fourier 62 (2012), no. 2, 727–782. DOI: 10.5802/aif.2693.
3. A. Kitaoka, “Analytic Torsions Associated with the Rumin Complex on Contact Spheres,” International Journal of Mathematics 31 (2020), 2050112. DOI: 10.1142/S0129167X20501128; arXiv:1911.03092.

## 12. Reproducibility checklist

A symbolic implementation should verify:
- [X,Y] = -T and [T,X] = [T,Y] = 0;
- dtheta = dx wedge dy;
- f = Ya - Xb;
- D_R(a,b) = (Ta-Xf, Tb-Yf);
- D_R(Xu,Yu) = 0;
- d_H²(D_R(a,b)) = 0;
- the formal-adjoint identity by integration by parts on compactly supported test fields.

These local algebraic checks do not replace a global spectral calculation on S³/2I.
