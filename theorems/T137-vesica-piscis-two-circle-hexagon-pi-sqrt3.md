# T137 — Exact geometry of the Vesica Piscis and the \(\sqrt3\) hexagonal chord

**Record type:** theorem (Euclidean geometry) with a separate open spectral programme  
**Status:** geometric statements proved; any new DtN identity involving \(\pi\) and \(\sqrt3\) remains open.

## 1. Configuration

Let two circles of radius \(R>0\) have centres
\[
O_1=(-R/2,0),\qquad O_2=(R/2,0).
\]
Their centre distance is \(R\). Let \(P,Q\) be their two intersection points, and let \(\mathcal V\) be the intersection of the two closed disks (the Vesica Piscis).

The triangle \(O_1O_2P\) is equilateral, since all three sides have length \(R\). Consequently the radii to \(P,Q\) make angles \(\pm60^\circ\) with the centre axis.

## 2. Chord theorem

The common chord \(PQ\) is perpendicular to the line of centres and bisects it. In either equilateral triangle its half-length is the altitude:
\[
\frac{|PQ|}{2}=\sqrt{R^2-(R/2)^2}=\frac{\sqrt3}{2}R.
\]
Hence
\[
\boxed{|PQ|=\sqrt3\,R.}
\]

This is the exact geometric source of \(\sqrt3\) in the equal-circle Vesica.

## 3. Boundary length

The boundary of the intersection consists of two arcs, each subtending \(120^\circ=2\pi/3\) at its circle centre. Thus
\[
\boxed{P(\mathcal V)=2R\frac{2\pi}{3}=\frac{4\pi R}{3}.}
\]

The ratio of boundary length to common-chord length is therefore
\[
\boxed{\frac{P(\mathcal V)}{|PQ|}=\frac{4\pi}{3\sqrt3}.}
\]

## 4. Area

The Vesica is the union of two circular segments. Each segment is a \(120^\circ\) sector minus an equilateral triangle:
\[
A_{\rm seg}=\frac12R^2\frac{2\pi}{3}
-\frac{\sqrt3}{4}R^2
=\frac{\pi R^2}{3}-\frac{\sqrt3 R^2}{4}.
\]
Adding the two segments gives
\[
\boxed{|\mathcal V|=R^2\left(\frac{2\pi}{3}-\frac{\sqrt3}{2}\right).}
\]
Eliminating \(R\) by \(|PQ|^2=3R^2\),
\[
\boxed{\frac{|\mathcal V|}{|PQ|^2}
=\frac{2\pi}{9}-\frac{\sqrt3}{6}.}
\]

All these identities are exact Euclidean geometry; no spectral approximation is involved.

## 5. Exact regular-hexagon correspondence

For a regular hexagon of side \(R\), the circumradius is also \(R\). The distance between vertices separated by one vertex (central angle \(120^\circ\)) is
\[
2R\sin(60^\circ)=\sqrt3R.
\]
Therefore the Vesica common chord has exactly the same length as the short diagonal of a regular hexagon with side \(R\):
\[
\boxed{|PQ|=d_{\rm hex,short}=\sqrt3R.}
\]

This identifies a shared metric quantity. It does not by itself identify the Vesica with the hexagon, nor does it establish a further pentagon–hexagon theorem. Any such bridge must specify its map and prove which lengths or ratios it preserves.

## 6. What the geometry does — and does not — say about \(\pi\)

The dimensionless area and perimeter ratios contain both constants:
\[
\frac{|\mathcal V|}{|PQ|^2}=\frac{2\pi}{9}-\frac{\sqrt3}{6},
\qquad
\frac{P(\mathcal V)}{|PQ|}=\frac{4\pi}{3\sqrt3}.
\]
These are geometric relations between circular measure and the \(60^\circ/120^\circ\) triangular geometry. They are not an arithmetic identity determining \(\pi\) from \(\sqrt3\), or vice versa.

## 7. Interface with the anisotropic multimode DtN model

The companion model is [VESICA_ANISOTROPIC_DTN_MODEL.md](../docs/VESICA_ANISOTROPIC_DTN_MODEL.md). In that model:
- the domain profile \(w(y)=\sqrt{1-y^2}-1/2\) is the exact circular geometry of this Vesica in the chosen coordinates;
- transverse Dirichlet modes introduce \(n\pi/(2w(y))\);
- the chosen off-diagonal anisotropy contains \(\sqrt3/4\).

Thus \(\pi\) and \(\sqrt3\) both occur in the operator coefficients, but this observation alone does not produce a new spectral identity.

### Open spectral question (not a theorem)

For a precisely specified interior interval, truncation \(N\), boundary convention and spectral parameter \(\lambda\), compute the DtN matrix \(\Lambda_N(\lambda)\) with a stable propagation method. Then test whether a scale-free spectral invariant (for example, a suitably normalized determinant, eigenvalue ratio, or heat coefficient after a justified limit) has an exact relation to
\[
\frac{2\pi}{9}-\frac{\sqrt3}{6}
\quad\text{or}\quad
\frac{4\pi}{3\sqrt3}.
\]
A numerical fit is only a conjecture generator. A theorem requires: (i) a well-defined continuum DtN limit, including the singular Vesica tips if the full domain is used; (ii) proof that the proposed invariant exists and is normalization-independent; (iii) an analytic derivation of its value. The finite-\(N\), interior-interval transfer calculation in the companion model does not yet meet these obligations.

## 8. Proof status

- **Proved:** common chord \(\sqrt3R\).
- **Proved:** boundary length \(4\pi R/3\).
- **Proved:** area \(R^2(2\pi/3-\sqrt3/2)\).
- **Proved:** common chord equals the short diagonal of a regular hexagon of side \(R\).
- **Open:** any new DtN/spectral identity involving these constants.
- **Not claimed:** a derivation of \(\pi\) from \(\sqrt3\), a physical constant, or a pentagon–hexagon equivalence.
