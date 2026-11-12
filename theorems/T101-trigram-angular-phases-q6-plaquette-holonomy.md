# T101 — Angular trigram phases, antipodal complements, and Q6 plaquette holonomy

**Status:** exact finite construction and audit identities; physical phase values, spatial embedding, and defect interpretation remain data-dependent/open.

**Purpose.** T101 corrects the order of construction: assign a measurable angular phase to each of the eight trigrams first; construct the 64 hexagrams as ordered pairs of trigram positions on two circle factors; then audit complementarity and all 240 square plaquettes of the six-cube. Individual hexagrams remain the charge-bearing degrees of freedom of T100. No phase values or charges are fabricated.

## 1. Eight trigram phases and the opposite-circle complement

Label a trigram by \(t\in\{0,\ldots,7\}\), with bit 0 the bottom line and bit 2 the top line. Its measured angular coordinate is
\[
z_t=e^{i\theta_t},\qquad \theta_t\in\mathbb R/(2\pi\mathbb Z).
\]
The linewise yin-yang complement is \(\bar t=t\mathbin{\mathrm{xor}}7\). The antipodal-complement hypothesis is
\[
z_{\bar t}=-z_t
\quad\Longleftrightarrow\quad
\operatorname{wrap}(\theta_{\bar t}-\theta_t-\pi)=0.
\]
Define the measured residual
\[
\epsilon_t=\operatorname{wrap}(\theta_{\bar t}-\theta_t-\pi)
\in(-\pi,\pi].
\]
This is an eight-entry diagnostic (four independent complement pairs, with opposite signs under pair exchange). Antipodality is a testable condition, not an imposed identity. The angular origin and orientation of the circle must be calibrated experimentally; a common rotation of all \(\theta_t\) changes no residual.

## 2. The 64 hexagrams as points on a two-torus

Encode an ordered hexagram by
\[
h=\ell+8u,\qquad \ell,u\in\{0,\ldots,7\},
\]
where \(\ell\) is the lower trigram and \(u\) the upper trigram. The phase map is
\[
\Phi:Q_6\longrightarrow S^1\times S^1,\qquad
\Phi(h)=(z_\ell,z_u)
=(e^{i\theta_\ell},e^{i\theta_u}).
\]
Thus the 64 six-line configurations are 64 labelled points (not necessarily distinct) on \(T^2\). The complementary hexagram is
\[
\bar h=h\mathbin{\mathrm{xor}}63,
\]
and its two-torus displacement is the ordered pair
\[
D_h=\left(
\operatorname{wrap}(\theta_{\ell\mathbin{\mathrm{xor}}7}-\theta_\ell),
\operatorname{wrap}(\theta_{u\mathbin{\mathrm{xor}}7}-\theta_u)
\right).
\]
Under exact antipodality, \(D_h=(\pi,\pi)\) modulo \(2\pi\). The relative phase
\[
\Delta_h=\operatorname{wrap}(\theta_u-\theta_\ell)
\]
is also directly measurable. No identification of the two circle factors, nor any Euclidean embedding of \(T^2\), is assumed.

## 3. All 192 edges and 240 plaquettes

The six-cube has one edge for each pair \((h,i)\) with \(0\le h<64\), \(0\le i<6\), and bit \(i\) of \(h\) equal to zero; its other endpoint is \(h'=h\mathbin{\mathrm{xor}}2^i\). This gives \(64\cdot6/2=192\) edges. Bits \(0,1,2\) change the lower-trigram coordinate; bits \(3,4,5\) change the upper-trigram coordinate.

For an oriented edge \(e=(h,h')\), define the phase increment in the factor that changes:
\[
a_e=
\begin{cases}
\operatorname{wrap}(\theta_{\ell'}-\theta_\ell),&i<3,\\
\operatorname{wrap}(\theta_{u'}-\theta_u),&i\ge3.
\end{cases}
\]
For each pair of bit directions \(i<j\), and each base vertex \(h\) with bits \(i,j\) both zero, there is one elementary square
\[
p=(h,\ h\mathbin{\mathrm{xor}}2^i,\
h\mathbin{\mathrm{xor}}2^i\mathbin{\mathrm{xor}}2^j,\
h\mathbin{\mathrm{xor}}2^j).
\]
There are \(\binom62 2^4=240\) such plaquettes. The phase circulation is
\[
W_p=\operatorname{wrap}\left(\sum_{e\in\partial p}^{\rm oriented}a_e\right).
\]

**Exact integrability gate.** Since the edge variables above are differences of vertex phases, they are a pure-gauge \(U(1)\) connection. Therefore
\[
\prod_{e\in\partial p}e^{ia_e}=1,\qquad W_p=0
\]
for every plaquette, up to floating-point roundoff. The sum of principal representatives may equal \(2\pi n_p\) for an integer \(n_p\); that integer is a branch/interpolation winding diagnostic, not nonzero \(U(1)\) curvature. It must not be called a disclination. This is a crucial no-false-positive result: eight vertex phases alone cannot generate nontrivial plaquette gauge curvature.

## 4. What is additionally required to identify dislocations and disclinations

A genuine rotational defect requires independently measured local-frame transport (link connection) \(\alpha_e\), not merely the endpoint phase difference \(a_e\). Its plaquette holonomy is
\[
\mathcal H_p=\exp\left(i\sum_{e\in\partial p}\alpha_e\right).
\]
Nontrivial \(\mathcal H_p\) is a candidate rotational holonomy; its interpretation as a Frank angle requires a calibrated frame and a declared rotational symmetry group.

A dislocation is translational closure failure. It requires a spatial reconstruction \(X_h\), a displacement/registration field, or a coframe on the reconstructed structure. For a loop \(\Gamma\), the Burgers vector is
\[
b=\oint_\Gamma du.
\]
The phase winding of a reconstructed reciprocal mode \(G\) obeys \(\Delta_\Gamma\theta_G=-G\cdot b\) under the usual displaced-mode convention. This cannot be computed from the two angular labels alone without specifying the map from \(T^2\) or Q6 to physical space and the reciprocal mode.

Accordingly, T101 separates three objects:
1. **complement mismatch** \(\epsilon_t\): directly testable from the eight trigram angles;
2. **phase circulation** \(W_p\): identically zero modulo \(2\pi\) for the endpoint-derived pure-gauge connection;
3. **physical defect holonomy**: requires independent link-frame transport and/or translational registration data.

The same distinction applies to the hypercube: its 240 squares provide the complete set of elementary loops on which additional transport data can be tested, but the abstract combinatorial squares do not by themselves supply a physical plane or a material lattice.

## 5. Computational audit and data format

The companion script \`scripts/audit_t101_trigram_phase_holonomy.py\` accepts a JSON array of exactly eight measured phases in radians, indexed by the three-bit trigram label. It constructs all 64 torus points, 192 oriented cube edges, and 240 elementary plaquettes; reports the eight complement residuals, all 64 complement displacements, the 240 principal plaquette circulations and integer branch windings; and verifies that every \(U(1)\) plaquette holonomy is unity within tolerance.

Synthetic phases in tests are fixtures for software verification only. They are not proposed measurements and do not select a physical charge law. T100 remains responsible for node charges and their correlations; T101 supplies the angular geometry and the exact conditions under which defect claims can or cannot be inferred.

## 6. Evidence register

| Claim | Status |
|---|---|
| Eight trigram phases define 64 labelled points on \(T^2\) | Definition, conditional on measured \(\theta_t\) |
| Antipodal complement relation and residual \(\epsilon_t\) | Exact testable criterion |
| Q6 has 192 edges and 240 elementary square plaquettes | Proved finite combinatorics |
| Endpoint-derived phase connection has trivial \(U(1)\) plaquette holonomy | Proved exact identity |
| Nonzero branch winding is a physical disclination | **Not claimed**; requires independent frame transport |
| Burgers vector from trigram phases alone | **Not identifiable** without spatial reconstruction |
| Physical charge law from angular phases | Open; connect to T100 using measured node data |

