# T162 — Q6 six-neighbour gradient, barycentric P1 projection and Lorentzian tangent lift

**Status:** exact affine-patch identity and exact conditional Lorentzian tangent-lift lemma; finite implementation tests pending CI. The arbitrary-field operator residual and the Q6-to-4D cell resolution remain OPEN.

## 1. Combinatorial cells and declared shape map

The six-bit cube has 64 vertices, 192 coordinate edges and 240 elementary square faces. A deterministic split of each square along its ((v_0,v_2)) diagonal gives 480 oriented triangles. This is a triangulation of the combinatorial square 2-skeleton, not an assertion that its projection is an embedded planar surface.

Let (x_v=Phi(v)inmathbb R^2) be the declared calibrated Q6 shape coordinate. The calibration is an input: the six-dimensional cut-and-project internal frame does not canonically select a unique two-dimensional shape plane.

## 2. Two gradient operators

The T130 six-neighbour weighted least-squares gradient is
[
G_v=sum_{wsim v}rac{(x_w-x_v)(x_w-x_v)^T}{|x_w-x_v|^2},qquad
b_v=sum_{wsim v}rac{(x_w-x_v)(f_w-f_v)}{|x_w-x_v|^2},
qquad

abla_{Q6}f(v)=G_v^{-1}b_v.
]
It is defined when every local star spans (mathbb R^2).

For each nondegenerate projected triangle (F=(v_0,v_1,v_2)), let (
abla_F^{P1}f) be the exact constant gradient of the affine interpolant. Define its area-weighted vertex projection
[

abla_{P1}^{m bar}f(v)=
rac{sum_{F
i v}|F|,
abla_F^{P1}f}
{sum_{F
i v}|F|}.
]
The operator compatibility residual is
[
mathfrak r_v(f)=
abla_{Q6}f(v)-
abla_{P1}^{m bar}f(v).
]

## 3. Affine patch theorem

**Theorem.** Suppose every projected Q6 edge star spans (mathbb R^2), and every triangle in the chosen square split is nondegenerate. For any affine field (f_v=acdot x_v+c),
[

abla_{Q6}f(v)=a
=
abla_F^{P1}f
=
abla_{P1}^{m bar}f(v)
]
for every vertex and every incident triangle. Hence (mathfrak r_v(f)=0) exactly in exact arithmetic.

**Proof.** On each edge, (f_w-f_v=acdot(x_w-x_v)), so (b_v=G_va). Invertibility gives the first equality. The affine P1 interpolant reproduces (f) on every nondegenerate triangle, giving the second. An area-weighted average of identical vectors remains (a). (square)

For non-affine fields, the two operators need not agree. The residual is therefore reported rather than constrained to zero. This is the required compatibility diagnostic for the discrete action; no arbitrary correction or fitted weight is introduced.

## 4. Triangle barycentre and covariance

For each triangle with projected vertices (x_i), the area centroid and normalized covariance are
[
c_F=rac{x_0+x_1+x_2}{3},qquad
Sigma_F=rac1{12}sum_{i=0}^2(x_i-c_F)(x_i-c_F)^T.
]
These are the T068 local cell moments. They are distinct from the 64-vertex Q6 covariance and from the antipodal pair covariance.

## 5. Conditional Lorentzian tangent lift

Let (Binmathbb R^{4	imes2}) have rank two and let (eta=mathrm{diag}(1,-1,-1,-1)). Assume the induced Gram matrix (G_B=B^Teta B) is nondegenerate. For a shape-plane gradient (ginmathbb R^2), define
[

abla_4^{,B}f=B(B^Teta B)^{-1}g.
]
Then
[
B^Teta
abla_4^{,B}f=g.
]
This is the unique vector in (mathrm{im}(B)) satisfying the prescribed tangential duality relation. The formula is exact linear algebra. It fails for a degenerate/null selected 2-plane, which the implementation rejects.

**Crucial limitation:** this lifts a two-dimensional shape gradient into a selected two-plane of Minkowski space. It does not construct the complementary two spacetime directions, a Lorentzian four-cell, a regular 4D Q6 complex, or a spin connection. The Q6-to-4D cell-resolution workstream remains open; M3's D4 orbit graph and its regularity audit do not supply that missing structure.

## 6. Reproducible implementation

- `audits/q6_barycentric_gradient_bridge.py`
- `tests/test_q6_barycentric_gradient_bridge.py`

The audit constructs the 240 square faces, their 480-triangle split, compares T130's six-neighbour least-squares operator with the area-weighted P1 vertex projection, reports the arbitrary-field residual and local conditioning, and checks the conditional Lorentzian tangent lift.

## 7. Evidence classification

- **PROVED:** affine patch identity under the stated rank/nondegeneracy assumptions; conditional Lorentzian tangent-lift identity.
- **NUMERICAL TESTS:** Q6 face/triangle counts, affine patch, arbitrary-field residual reporting, and degenerate-plane rejection; CI status is reported separately.
- **OPEN:** physical calibration of (Phi); robustness of the chosen square diagonal; non-affine operator convergence; map from this two-dimensional shape plane to a full four-dimensional tetrad; Q6 4D cell closure; Cartan curvature/torsion equations and Sakharov heat coefficients on that resolved 4D complex.


## 8. Independent numerical patch/residual audit

For the declared calibration
[
C=\begin{pmatrix}1&0.2&-0.1\\0.3&0.8&0.4\end{pmatrix},
]
an independent numerical reconstruction of the committed formulas gives:
- 64 vertices, 192 edges, 240 square faces and 480 triangles;
- minimum projected triangle area (8.766444521870514\times10^{-3});
- maximum Q6 star condition number (2.0212145278087736);
- affine-patch operator residual (8.01\times10^{-16});
- for the declared non-affine parity test field (f_v=(-1)^{|v|_1}(1+v/64)), maximum Q6/P1 operator mismatch (6.850733090221455).

The last number is not an error estimate tending to zero: it is a finite diagnostic showing that the two operators differ on a non-affine field at this resolution. A refinement study and a calibrated projection are required before asserting convergence or replacing one operator by the other. These are local numerical checks; the GitHub Actions status remains separate.


## 9. Extension to the explicit four-dimensional carrier

T163 now constructs a rank-four 4x6 golden cut-project frame and defines the corresponding six-neighbour Q6 gradient directly in the projected 4D chart. Its affine patch audit supersedes the conditional two-plane lift here as the operative 4D gradient test. T162 remains the local 2D T130/P1 compatibility theorem and the general conditional tangent-lift identity; T163 supplies the distinct 4D cut-project construction and records its three-way branch incidence.
