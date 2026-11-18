# The cyclic chord operator: a common law for Vesica, hexagon and pentagon

**Research note — 18 November 2026**  
**Status:** the operator identity and the three geometric corollaries below are proved. The note identifies a common mathematical mechanism; it does not claim that the golden ratio is derived from the Vesica alone, nor that every Vesica-to-pentagon construction follows from one incidence pattern.

Related note: [Polloni–Needham–Vesica–Thales geometry](POLLONI_NEEDHAM_VESICA_THALES_GEOMETRY.md), especially §§3, 12–16.

## 1. The unifying object

Let V=R² with its Euclidean inner product, and let Rθ in SO(2) be rotation through angle θ. Define the **chord operator**
\[
\Delta_\theta:=R_\theta-I.
\]
For any vector v in V, the vector Δθv joins the endpoints of the radius vectors v and Rθv. It is therefore the chord subtending the central angle θ on the circle of radius ||v||.

In an orthonormal basis,
\[
R_\theta=
\begin{pmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{pmatrix},
\qquad
\Delta_\theta=
\begin{pmatrix}
\cos\theta-1&-\sin\theta\\
\sin\theta&\cos\theta-1
\end{pmatrix}.
\]

## 2. Theorem: universal chord identity

**Theorem 1 (cyclic chord operator).** For every real θ,
\[
\boxed{\Delta_\theta^{\mathsf T}\Delta_\theta
=4\sin^2(\theta/2)I.}
\]
Consequently, for every v in R²,
\[
\boxed{\lVert\Delta_\theta v\rVert
=2\left|\sin(\theta/2)\right|\lVert v\rVert.}
\]

**Proof.** Since Rθᵀ=R−θ,
\[
\begin{aligned}
\Delta_\theta^{\mathsf T}\Delta_\theta
&=(R_{-\theta}-I)(R_\theta-I)\\
&=2I-R_\theta-R_{-\theta}\\
&=2(1-\cos\theta)I\\
&=4\sin^2(\theta/2)I.
\end{aligned}
\]
Taking the quadratic form on v and the nonnegative square root proves the norm identity. \(\square\)

The theorem says more than the familiar chord formula: the chord operator is an isotropic similarity up to a rotation. Indeed,
\[
\Delta_\theta
=2\sin(\theta/2)R_{\theta/2+\pi/2},
\]
with the sign interpreted in the usual oriented-angle sense. Thus it scales every vector by the same absolute factor and rotates it.

## 3. Three exact corollaries

### 3.1 Vesica Piscis

Take two equal circles of radius E, with centre separation E. Their centres and either intersection point form an equilateral triangle. At either centre, the two radii to the intersection points subtend 120°. The common chord is therefore
\[
A=\lVert\Delta_{2\pi/3}v\rVert
=2E\sin(\pi/3)
=\boxed{\sqrt3 E}.
\]
Here E is the centre separation (the span), while A is the common-chord length (the opening). The distinction is essential.

### 3.2 Regular hexagon

Let a regular hexagon have circumradius and side E. Vertices separated by one intervening vertex subtend 120° at the centre. Their distance is
\[
d_2=\lVert\Delta_{2\pi/3}v\rVert
=\boxed{\sqrt3 E}.
\]
This is also the distance between opposite parallel sides (the across-flats width): the apothem is E cos(π/6)=√3 E/2, so the width is twice the apothem.

Thus the Vesica opening equals the across-flats width of a regular hexagon whose side/circumradius is the Vesica span:
\[
\boxed{A=W_6=\sqrt3 E.}
\]
This equality compares two precisely specified constructions. It does not say that the Vesica opening is the hexagon side.

### 3.3 Regular pentagon and the golden ratio

For a regular pentagon of circumradius R, a side subtends 72°, while a diagonal subtends 144°. The chord operator gives
\[
s=2R\sin(\pi/5),\qquad
d=2R\sin(2\pi/5).
\]
Therefore
\[
\frac ds
=\frac{\sin(2\pi/5)}{\sin(\pi/5)}
=2\cos(\pi/5)
=\boxed{\varphi}.
\]
The golden ratio is thus the ratio of two chord-operator scale factors at the two pentagonal angles:
\[
\boxed{
\frac{\lVert\Delta_{4\pi/5}v\rVert}
{\lVert\Delta_{2\pi/5}v\rVert}=\varphi
\quad(v\ne0).
}
\]
This is the standard diagonal/side theorem for a regular pentagon, now expressed in the same operator language as the Vesica and hexagon.

## 4. Invariance and covariance

The identity is independent of the chosen Cartesian axes. For every orthogonal map Q in O(2),
\[
Q R_\theta Q^{-1}=R_{\det(Q)\theta},
\]
and hence
\[
Q\Delta_\theta Q^{-1}=\Delta_{\det(Q)\theta}.
\]
Since sin²(θ/2) is unchanged by θ→−θ, Theorem 1 is invariant under rotations and reflections. Under a uniform similarity v→λQv, all chord lengths scale by |λ|, while every ratio of chord lengths is unchanged.

The common structure is therefore Euclidean and similarity-covariant, not dependent on a special drawing orientation.

## 5. Cyclotomic form

If ζn=e^(2πi/n), rotation by 2πk/n is multiplication by ζn^k in the complex plane. The chord operator becomes multiplication by
\[
\zeta_n^k-1,
\]
and its length factor is
\[
|\zeta_n^k-1|=2\left|\sin\frac{k\pi}{n}\right|.
\]

For the Vesica, the relevant third roots of unity give
\[
|\omega-\omega^2|=\sqrt3,\qquad \omega^3=1,\quad\omega\ne1.
\]
For the pentagon,
\[
\frac{|\zeta_5^2-1|}{|\zeta_5-1|}
=\frac{\sin(2\pi/5)}{\sin(\pi/5)}
=\varphi.
\]
This makes the arithmetic distinction transparent: the Vesica's √3 comes from third-root/triangular symmetry, whereas φ comes from fifth-root/pentagonal symmetry. The operator law is common; the roots of unity and the angles are different.

## 6. The separate homothetic closure in the green-pentagon construction

The span-based construction reconstructed in §16 of the related note contains an additional step not implied by Theorem 1. A unit regular pentagon is mapped by the homothety
\[
H(X)=T+\varphi(X-T).
\]
Because a homothety of ratio φ multiplies all lengths by φ, the image is a regular pentagon of side φE. The compatibility of the extended-diagonal construction is encoded by
\[
\varphi+1=\varphi^2.
\]

This is a **closure condition** for that particular incidence construction. It must not be folded into the universal chord identity: Theorem 1 does not select the homothety centre, does not construct the five vertices, and does not force a pentagon to be present in every Vesica.

The full coordinate construction and its diagram-reading qualification remain in §16 of [POLLONI_NEEDHAM_VESICA_THALES_GEOMETRY.md](POLLONI_NEEDHAM_VESICA_THALES_GEOMETRY.md).

## 7. What the unifying law does and does not claim

**Established:**
1. All Euclidean chord lengths are generated by the single operator family Δθ=Rθ−I.
2. The Vesica opening and the regular-hexagon across-flats width both equal √3 E under the normalisation stated in §3.
3. The regular-pentagon diagonal/side ratio is the quotient of two chord-operator scale factors and equals φ.
4. These identities are invariant under rotations, reflections and uniform similarities.
5. The Vesica and pentagon cases have a common cyclotomic/operator description, while retaining different symmetry orders.

**Not claimed:**
- φ is derivable from √3 alone.
- The Vesica alone determines a unique regular pentagon.
- Every diagram called a Vesica–pentagon construction has the incidence structure of the reconstruction in §16.
- The operator identity is a new physical law or a result about RGS, PRISM, Q6 or PSU.

## 8. Classification and proposed theorem record

| Statement | Classification |
|---|---|
| ΔθᵀΔθ=4 sin²(θ/2) I | **Proved — general theorem** |
| Vesica opening A=√3 E | **Proved — corollary** |
| Hexagon across-flats width W₆=√3 E | **Proved — corollary** |
| Pentagon diagonal/side ratio d/s=φ | **Proved — corollary** |
| Similarity/reflection covariance | **Proved** |
| Golden homothety in the specified green-pentagon construction | **Proved in the stated coordinate reconstruction; source-plate identification qualified** |
| A stronger universal theorem deriving fivefold closure from threefold Vesica data alone | **Not established / not implied** |

**Suggested theorem label:** CYCLIC-CHORD-01 — Universal Euclidean chord operator.

This is a candidate repository theorem record with a complete elementary proof. It should be classified as a proved mathematical theorem once reviewed against the repository's theorem-record conventions; it is not a claim of priority or novelty. The substantive contribution here is the unified formulation and its explicit application to the three constructions.
