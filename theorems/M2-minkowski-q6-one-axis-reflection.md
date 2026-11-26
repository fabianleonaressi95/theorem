# M2 — Minkowski one-axis reflection on the Q6 sign fibre

**Status:** exact finite cubical chain-map theorem; exact rational sector ranks; geometric identification is conditional on the stated coordinate convention. This record does not claim that the circle/square construction itself has been derived from Q6.

## 1. Geometric reflection and null coordinates

In a (1+1)-dimensional Minkowski plane use coordinates (X=ct), (x), metric
[
q(X,x)=X^2-x^2.
]
The null coordinates
[
u=X+x,qquad v=X-x
]
satisfy (q=uv). The spatial reflection
[
mathsf r_x(X,x)=(X,-x)
]
exchanges (u) and (v). It therefore exchanges the two null directions and the two oriented null rays used to form the future/past triangular sectors.

This is a **one-spatial-axis reflection**, not full spatial inversion in three dimensions.

## 2. Identification with the recovered RGS sign fibre

The recovered 64-point seed is labelled by six big-endian bits
[
v=(b_1,b_2,b_3mid s_1,s_2,s_3).
]
The first three bits select one of eight orbit representatives; the last three bits select the signs of the three spatial coordinates. Thus, with this fixed ordering,
[
X(v)=(s_1r_1(b),s_2r_2(b),s_3r_3(b)).
]

A reflection of the first spatial coordinate alone is
[
(X_1,X_2,X_3)mapsto(-X_1,X_2,X_3),
]
and is represented on labels by
[
oxed{vmapsto voplus 4}.
]
The other two coordinate reflections are (vmapsto voplus2) and (vmapsto voplus1). They are conjugate under coordinate permutations of the sign fibre and give the same sector dimensions.

By contrast, full three-dimensional central inversion is
[
vmapsto voplus7,
]
and the canonical graph antipode is (vmapsto voplus63). These are different operations. In particular, (voplus7) is not the (1+1) reflection that exchanges (u) and (v) for one selected spatial axis.

## 3. Cubical chain lift

Let (K=Q_6^{(2)}) be the cubical 2-skeleton with
[
(|C_0|,|C_1|,|C_2|)=(64,192,240).
]
Orient each edge and square as in T071. The bit flip (a_4(v)=voplus4) is a cubical automorphism. Its induced signed permutation maps on oriented cells are denoted
[
J_k:C_k(K;mathbb Z)	o C_k(K;mathbb Z),qquad k=0,1,2.
]
They satisfy
[
J_k^2=I,qquad
B_1J_1=J_0B_1,qquad
B_2J_2=J_1B_2.
]
Thus the chain complex splits over (mathbb Q) into the two eigensubcomplexes of
[
P_k^pm=	frac12(Ipm J_k).
]
The projectors are rational (not generally integral), which is why the sector calculation is stated over (mathbb Q).

## 4. Exact sector dimensions and homology

For the representative one-axis reflection (a_4), exact rational linear algebra gives:

| Chain space | (+) sector | (-) sector |
|---|---:|---:|
| (dim C_0^pm) | 32 | 32 |
| (dim C_1^pm) | 80 | 112 |
| (dim C_2^pm) | 80 | 160 |
| (operatorname{rank}(B_1|_{C_1^pm})) | 31 | 32 |
| (operatorname{rank}(B_2|_{C_2^pm})) | 49 | 80 |
| (b_0^pm) | 1 | 0 |
| (b_1^pm) | 0 | 0 |
| (b_2^pm) | 31 | 80 |

In particular,
[
oxed{b_2^+=31,qquad b_2^-=80,qquad b_2=111.}
]
The asymmetry (31/80) is a property of the **truncated 2-skeleton**. Its 111 second-homology classes are killed when the omitted 3-cells of the full 6-cube are restored. It is not, by itself, a physical chirality or a continuum anomaly.

The three one-axis masks (1,2,4) give the same dimensions and Betti numbers. Full sign inversion (a_7), on the other hand, has (b_2^+=55), (b_2^-=56). The earlier (55/56) result belongs to full three-coordinate inversion, not to a single Minkowski spatial reflection.

## 5. Spectral consequence

Because (J_k) is an orthogonal signed permutation and a chain map, it commutes with the combinatorial Hodge Laplacian
[
Delta_k=B_k^TB_k+B_{k+1}B_{k+1}^T
]
(with absent boundary terms omitted at the ends). Hence
[
[Delta_k,J_k]=0.
]
The Laplacian is block diagonal on the (+) and (-) eigenspaces. This is a finite combinatorial statement; it does not identify the cubical Laplacian with a Lorentzian wave operator.

## 6. Proof

A coordinate bit flip maps every vertex to a vertex, every coordinate edge to a coordinate edge, and every elementary square to an elementary square. On oriented cells it acts by a signed permutation, with the sign fixed by comparison of the mapped oriented boundary with the target orientation. Since it is induced by a cubical automorphism, it preserves incidence and has order two. This proves the chain-map identities and (J_k^2=I).

The chain-map identities imply (B_kP_k^pm=P_{k-1}^pm B_k), so each eigenspace is a subcomplex. The ranks and Betti numbers in Section 4 are reproduced by the exact-rational audit
`audits/audit_minkowski_q6_axis_reflection.py`; the test is
`tests/test_minkowski_q6_axis_reflection.py`.

## 7. Scope and open bridge

**Proved:** the (1+1) reflection exchanges the null coordinates; under the declared RGS sign-bit convention it is a one-bit flip; that flip lifts to a cubical chain involution; the stated rational sector dimensions, ranks, Betti numbers, and Laplacian commutation.

**Not proved:** that the user's two-circle/two-rotated-square construction canonically chooses one of the three RGS spatial axes; that the 2-skeleton sector imbalance survives the full 6-cube (it does not survive as (H_2)); any physical chirality, prime-divisibility law, or continuum Minkowski limit.

**Next geometric datum needed:** an explicit map from the two circle centres, the two square orientations, and their two triangular sectors to the ordered RGS coordinates ((X_1,X_2,X_3)). Once that map is fixed, the axis label (mask (1,2), or (4)) is no longer arbitrary.
