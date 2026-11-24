# Vesica Piscis, Minkowski cones and the two-trigram decomposition of Q6

**Date:** 24 November 2026  
**Status:** exact combinatorial identification + exact (2+1)-dimensional geometry; geometric realization of Q6 as the two conic sheets remains a construction target.

## 1. The 64 vertices are the 64 hexagrams

A hexagram consists of six binary line values. With a fixed convention (lower trigram first, upper trigram second), write
[
H=(L,U),qquad L,Uinmathbb F_2^3.
]
The eight possible lower trigrams and eight possible upper trigrams give
[
mathcal H=mathbb F_2^3	imesmathbb F_2^3,qquad |mathcal H|=8cdot8=64.
]
Thus the vertex set of the six-bit cube (Q_6) is canonically identified with the set of six-line patterns, once the bit-to-line convention and bit order are declared. This is a bijection of sets; it does not by itself identify every chosen Q6 edge, face, operator or metric with a traditional I Ching relation.

The lower/upper split is structural, not a numerical convenience:
[
mathbb F_2^6=V_{m lower}oplus V_{m upper},qquad
V_{m lower}simeq V_{m upper}simeqmathbb F_2^3.
]
The Gray-code order used in some computational tables is only an enumeration convention. It must not be conflated with the intrinsic six line bits or with the lower/upper trigram decomposition.

## 2. The exact affine-filtration result

For the ordered-prefix filtration (E_j), an affine map (T(x)=Px+b) commutes with (E_j) exactly when the upper-right (j	imes(6-j)) block of (P) vanishes (with the row/column convention of the audited implementation). Equivalently, (P) preserves the corresponding prefix subspace. The translation (b) does not affect the conditional-expectation sigma-algebra.

At the trigram boundary (j=3), every block-diagonal transformation
[
P=\begin{pmatrix}A&0\\0&D\end{pmatrix},
qquad A,Din GL(3,2),
]
preserves the split and commutes with (E_3). The subgroup (GL(3,2)\times GL(3,2)) has (168^2=28,224) elements; the reported exhaustive enumeration finds 16 full commutator profiles and zero commutator at (j=3) for every element. More generally, the exact criterion also permits lower block-triangular mixing from the first block into the second; block diagonal maps are the subgroup preserving both trigram factors separately.

The exhaustive/census details, sampled (GL(6,2)) results, natural Q6 automorphisms, and regression tests are recorded in [PR #437](https://github.com/fabianleonaressi95/theorem/pull/437) and its associated research record. These are finite algebraic results. They do not yet select a physical evolution or a unique geometric embedding.

## 3. Vesica geometry and two null cones in Minkowski (2+1)

Use coordinates ((t,x,y)) and metric (ds^2=-dt^2+dx^2+dy^2). Take two cone vertices
[
p_A=(0,0,0),qquad p_B=(0,1,0).
]
Their null cones are
[
mathcal C_A: t^2=x^2+y^2,qquad
mathcal C_B: t^2=(x-1)^2+y^2.
]
On the slice (t=-1), their spatial sections are the unit circles
[
x^2+y^2=1,qquad (x-1)^2+y^2=1.
]
The corresponding closed disks intersect in the Vesica Piscis. Their boundary circles meet at
[
C,D=\left(\frac12,\pm\frac{\sqrt3}{2}\right).
]
The common chord is (x=1/2), of length (\sqrt3) for unit radius.

The two cone *surfaces* intersect where (x=1/2) and (t^2=1/4+y^2). Their intersection is a spacetime curve; the chord (CD) is only its intersection with the slice (t=-1). Therefore the cone-surface intersection, the spatial Vesica, and the common chord are three distinct objects and must not be identified.

## 4. What is established, and what is not

| Statement | Status |
|---|---|
| Six binary line values are equivalent to an ordered pair of three-bit trigrams | Exact bijection after fixing the line/bit convention |
| The (j=3) prefix boundary is preserved by (GL(3,2)\times GL(3,2)) | Exact finite algebra; exhaustive enumeration reported in PR #437 |
| The two unit circles and their lens-shaped intersection form a Vesica Piscis | Exact Euclidean geometry |
| The two null cones have the stated circular sections and common spacetime intersection | Exact Minkowski (2+1) geometry |
| The two trigram factors are literally the two conic sheets, or Q6 vertices lie on those sheets with a specified incidence/metric | **Open:** requires an explicit map and compatibility proofs |

In particular, “two sheets” is currently a proposed geometric interpretation of the lower/upper trigram factors. The set-theoretic (3+3) split alone does not construct a Lorentzian metric, a causal order, or a map from the 64 hexagrams to points on the cones.

## 5. Required construction to close the bridge

1. Fix the six-bit convention against the traditional lower/upper trigram ordering and publish the lookup table for all 64 hexagrams.
2. Define explicit maps (\Phi_-,\Phi_+) from the two trigram spaces (or from the 64 paired states) into the proposed geometric sheets.
3. State whether the image is a set of points, cells, directions, or labels; these are not interchangeable.
4. Specify the metric and causal relation on the target and test which Q6 adjacency relations map to geometric incidence or causal adjacency.
5. Prove equivariance for the claimed symmetry subgroup. At minimum, verify that the action of (GL(3,2)\times GL(3,2)) on the two trigram factors agrees with the induced action on the two geometric sectors.
6. Compare the construction with the existing Vesica/Jitterbug records and preserve the distinction between point-set congruence and incidence embedding.

## 6. Monograph links

This record belongs to the common programme:
- chapters 2–5: Q6, binary vertices, Walsh filtration and finite cube symmetries;
- chapters 12–14: Anti-Twin, Vesica Piscis, two-sector geometry and Jitterbug;
- chapters 15–17: only if a compatible frame/coframe or Lorentzian structure is actually constructed.

Cross-links: T137 (Vesica), T142 (antipodal (3+3)), T143 (six-state isometric embedding), the Q6 affine/Walsh theorem record, and [PR #437](https://github.com/fabianleonaressi95/theorem/pull/437).

**No new theorem number is assigned here.** The exact combinatorial and Minkowski identities are recorded separately from the still-open Q6-to-cone geometric realization.


## 7. Explicit finite geometric realization on two null-cone patches

This section supplies an explicit realization of the 64 hexagrams as ordered pairs of points on two null-cone patches. It is a finite geometric model in Minkowski (2+1), not yet a derivation of physical dynamics.

Let
[
eta=-dt^2+dx^2+dy^2,qquad p_-=(0,0,0),quad p_+=(0,1,0).
]
The future null cones are parametrized by
[
X_-(r,\theta)=(r,r\cos\theta,r\sin\theta),qquad
X_+(r,\varphi)=(r,1+r\cos\varphi,r\sin\varphi).
]
Direct substitution gives (eta(dX_\pm,dX_\pm)=0) along the radial generators. At (r=1), the spatial sections are unit circles centered at ((0,0)) and ((1,0)).

The arc of the first circle lying inside the second closed unit disk is characterized exactly by
[
2-2\cos\theta\leq1
\iff \theta\in[-\pi/3,\pi/3].
]
The arc of the second circle lying inside the first disk is
[
2+2\cos\varphi\leq1
\iff \varphi\in[2\pi/3,4\pi/3].
]
Choose eight equally spaced sample directions on each arc:
[
\theta_k=-\frac{\pi}{3}+\frac{k\pi}{21},\qquad
\varphi_k=\frac{2\pi}{3}+\frac{k\pi}{21},\qquad k=0,\ldots,7.
]
Both sampled arcs lie on the boundary of the Vesica lens (V=D_-(1)\cap D_+(1)).

Fix once and for all a bijection \(\kappa:\mathbb F_2^3\to\{0,\ldots,7\}\), with the bit order and lower/upper trigram convention explicitly declared in the implementation. For instance, \(\kappa\) may use binary indexing or inverse Gray indexing; these choices are not geometrically equivalent and must not be silently interchanged. For a hexagram \(H=(L,U)\), define
[
\Phi(H)=\big(X_-(1,\theta_{\kappa(L)}),\ X_+(1,\varphi_{\kappa(U)})\big)
\in \Sigma_-\times\Sigma_+,
]
where \(\Sigma_\pm\) are the two sampled null-cone patches. Since each factor map is injective, \(\Phi\) is an injection of the 64 hexagrams into the product of the two patches. Thus the two trigram factors are represented by two separate conic sheets, and an esagram is their ordered pair.

### Vesica coupling and information retained

Write the spatial endpoints of the pair as \(q_-(L)\) and \(q_+(U)\). Each endpoint lies in both closed disks: the first is on \(\partial D_-\cap D_+\), and the second on \(D_-\cap\partial D_+\). By convexity, the midpoint
[
m(H)=\frac12(q_-(L)+q_+(U))
]
lies in the Vesica lens \(V\). The relative displacement
[
\delta(H)=q_+(U)-q_-(L)
]
records the separation of the two sheet points. The pair \((m,\delta)\) is equivalent to the ordered pair, since
\[
q_-=m-\frac12\delta,\qquad q_+=m+\frac12\delta.
\]
The midpoint alone is not an injective encoding: with the symmetric angular sampling above, the eight pairs with equal indices have the same midpoint \((1/2,0)\). Therefore the geometric state is the pair (or equivalently midpoint plus displacement), not the Vesica midpoint alone.

At fixed \(r=1\), each circle has line element \(d\ell^2=d\theta^2\) or \(d\varphi^2\). The product of the two sampled arcs inherits the Riemannian product metric
[
ds^2_{\rm pair}=d\theta^2+d\varphi^2.
]
This is a positive metric on the two-angle configuration space. It is not the Lorentzian metric on spacetime and should not be confused with the degenerate metric induced on a full null cone.

A natural geometric coupling observable is the squared inter-sheet separation
[
D^2(L,U)=|q_+(U)-q_-(L)|^2=|\delta(H)|^2,
]
and a possible harmonic interaction energy is
[
\mathcal U_\kappa(L,U)=\frac{\kappa}{2}D^2(L,U),\qquad \kappa\geq0.
]
This defines a legitimate finite geometric interaction functional. The value of \(\kappa\), its physical units, the dynamics, and any identification with electromagnetic, gravitational or material energy are not fixed by geometry and remain open.

### Q6 incidence and symmetry: exact factorization, not automatic isometry

Under the hexagram bijection, the Cartesian cube graph is
[
Q_6\cong Q_3^{\rm lower}\square Q_3^{\rm upper}.
]
An edge changes exactly one bit in exactly one trigram, so it changes exactly one factor of \(\Phi(H)\). This gives a two-sheet product realization of the *vertex set and factorized edge incidence*. It does not assert that all Q6 edge lengths are equal in the product angular metric: their lengths depend on the chosen bijection \(\kappa\) and on the angular sampling.

Likewise, \(GL(3,2)\times GL(3,2)\) acts separately on the two finite trigram sets and preserves the factor boundary \(j=3\), as in the affine-filtration audit. It is not the isometry group of the sampled circular arcs in general. A geometric equivariance theorem would require a specified action on the cone patches and a proof that it preserves the chosen angular metric and the Vesica coupling. No such claim is made here.

### Status of the construction

- **Exact:** both parametrized surfaces are null; the chosen arcs lie in the Vesica boundary; the 64-state map into \(\Sigma_-\times\Sigma_+\) is injective; the midpoint lies in the Vesica; the pair is recovered from midpoint and displacement; Q6 incidence factorizes as \(Q_3\square Q_3\).
- **Model choice:** the bijection \(\kappa\), angular sample positions, and harmonic coupling \(\mathcal U_\kappa\).
- **Open:** canonical/natural choice of \(\kappa\); equivariance of the finite \(GL(3,2)\) actions; a dynamics and conserved quantities; a derivation of a physical action or field equations; continuum/refinement limit and relation to the full Vesica/Jitterbug/RGS constructions.

The construction is therefore a rigorous finite geometric bridge from the 64 hexagrams to two conic sheets coupled through the Vesica, with the physical interpretation explicitly separated from the proved geometric statements.


### Reproducible finite audit

The implementation is in [`audits/audit_vesica_hexagram_two_cone.py`](../audits/audit_vesica_hexagram_two_cone.py), with output [`results/json/vesica_hexagram_two_cone_audit.json`](../results/json/vesica_hexagram_two_cone_audit.json). The script uses only the Python standard library. Its execution checks all 64 ordered pairs, both null-cone equations, membership of all endpoints and all 64 midpoints in the Vesica lens, reconstruction from midpoint plus displacement, and all 192 Q6 Cartesian-product edges.

The independent execution returned: 64 distinct ordered geometric pairs; 57 distinct midpoints at rounding tolerance (10^{-12}); eight equal-index pairs share the same midpoint; 192 Q6 edges; and squared inter-sheet separation in the interval approximately ([1,3]), with mean (1.096173671917929). All programmed assertions passed. The 57 midpoint count is a useful warning: the Vesica midpoint is a many-to-one projection, and the relative displacement is necessary to retain all 64 states.

**Reproduction:** `python audits/audit_vesica_hexagram_two_cone.py`.


**Sampling correction (24 November 2026):** the eight samples cover the entire 120-degree arcs, including both endpoints, with step (2\pi/21). The previous (\pi/21) step covered only 60 degrees and is superseded. The corrected audit gives minimum squared separation (0) (the two circle-intersection points), maximum approximately (3), mean (1.096173671917929), and still 57 distinct midpoints for 64 ordered pairs.
