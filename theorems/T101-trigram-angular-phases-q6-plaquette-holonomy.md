# T101 — Two-circle trigram phases, complementary pairs, and Q6 plaquette holonomy

**Status:** exact finite construction and audit identities; measured phase data, circle registration, spatial embedding, and physical defect interpretation remain data-dependent/open.

**Purpose.** Start from the geometry the model requires: each trigram has a measurable angular position on a circle, and its linewise complement is compared with it on the *opposite* circle. The six-cube carries the same paired-circle structure at the level of all 64 hexagrams. This is not the assumption that a complement is automatically the antipode on the same circle.

## 1. Two circles and the eight complementary trigram pairs

Let \(C_+\) and \(C_-\) be the two measured circles. For every trigram \(t\in\{0,\ldots,7\}\), record its angular phases
\[
\theta_t^+,\theta_t^-\in\mathbb R/(2\pi\mathbb Z).
\]
If the circle centres and radii are known, the corresponding measured positions are
\[
x_t^\pm=c_\pm+R_\pm(\cos\theta_t^\pm,\sin\theta_t^\pm).
\]
The trigram complement is \(\bar t=t\mathbin{\mathrm{xor}}7\), with bit 0 the bottom line and bit 2 the top line. A calibrated registration of the two circle frames is
\[
\rho(\theta)=\sigma\theta+\chi\pmod{2\pi},\qquad \sigma\in\{+1,-1\},
\]
where \(\chi\) is the measured relative frame offset and \(\sigma\) records whether the angular orientations agree or are reversed. The complementary-pair mismatch is
\[
\epsilon_t=\operatorname{wrap}\big(\theta_{\bar t}^--\sigma\theta_t^+-\chi\big).
\]
Thus complementarity is tested *across* \(C_+\) and \(C_-\). The special antipodal convention is the calibrated case \(\chi=\pi\) (with the selected orientation \(\sigma\)); it is not silently imposed. There are eight residual entries but only four independent complementary pairs, with the reverse-pair relation fixed by the registration convention.

## 2. The 64 hexagrams on paired two-torus copies

Write each hexagram as \(h=\ell+8u\), where \(\ell\) and \(u\) are the lower and upper trigrams. Each circle layer gives a 64-point labelled configuration on a two-torus:
\[
\Phi_\pm:Q_6\to T^2,\qquad
\Phi_\pm(h)=
(e^{i\theta_\ell^\pm},e^{i\theta_u^\pm}).
\]
The opposite-circle complement comparison pairs \(h\) on the plus layer with
\[
\bar h=h\mathbin{\mathrm{xor}}63
\]
on the minus layer. Its two-coordinate mismatch is
\[
E_h=\left(
\operatorname{wrap}(\theta_{\ell\mathbin{\mathrm{xor}}7}^--\sigma\theta_\ell^+-\chi),
\operatorname{wrap}(\theta_{u\mathbin{\mathrm{xor}}7}^--\sigma\theta_u^+-\chi)
\right).
\]
These are 64 paired six-line comparisons built from the eight trigram complement pairs. The two coordinates retain the lower/upper line triples as ordered factors; this does not replace the individual hexagram as the node-level degree of freedom in T100.

## 3. The Q6 one-skeleton and all 240 square loops

For either circle layer, the six-cube has 64 vertices and 192 edges. An oriented edge is \((h,h\mathbin{\mathrm{xor}}2^i)\), with bit \(i\) initially zero. Bits \(0,1,2\) change the lower trigram and bits \(3,4,5\) change the upper trigram; each family has 96 edges.

For a fixed layer \(\nu\in\{+,-\}\), the endpoint phase increment is
\[
a_e^\nu=
\begin{cases}
\operatorname{wrap}(\theta_{\ell'}^\nu-\theta_\ell^\nu),&i<3,\\
\operatorname{wrap}(\theta_{u'}^\nu-\theta_u^\nu),&i\ge3.
\end{cases}
\]
For every pair of bit directions \(i<j\) and every base vertex \(h\) with both bits zero, the elementary square is
\[
p=(h,\ h\mathbin{\mathrm{xor}}2^i,\
h\mathbin{\mathrm{xor}}2^i\mathbin{\mathrm{xor}}2^j,\
h\mathbin{\mathrm{xor}}2^j).
\]
There are exactly
\[
\binom62\,2^4=240
\]
such squares per Q6 layer. The same enumeration is run on \(C_+\) and \(C_-\), while the cross-circle complement mismatches \(E_h\) are recorded separately.

## 4. Exact integrability: what the phase loops do and do not prove

The edge increments \(a_e^\nu\) are differences of vertex phases on each layer. Hence they define a pure-gauge \(U(1)\) connection:
\[
\prod_{e\in\partial p}e^{ia_e^\nu}=1
\]
for every one of the 240 plaquettes on each layer. Equivalently, the plaquette circulation is zero modulo \(2\pi\), up to floating-point roundoff. A sum of principal representatives may be \(2\pi n_p\) with integer \(n_p\); this is a branch/interpolation winding diagnostic, not nonzero \(U(1)\) curvature. It must not be labelled a disclination.

This result does **not** say that the paired-circle geometry has no defects. It says that vertex phases alone, differenced along edges, cannot measure a nontrivial local-frame holonomy. To measure a disclination, independently record local-frame transport \(\alpha_e^\nu\) and compute
\[
\mathcal H_p^\nu=\exp\left(i\sum_{e\in\partial p}\alpha_e^\nu\right).
\]
A nontrivial value is a candidate rotational holonomy; conversion to a Frank angle requires a calibrated frame and a declared rotational symmetry group.

A dislocation is translational closure failure. It requires physical-space registration \(X_h^\nu\), a displacement field, or a coframe. For a loop \(\Gamma\),
\[
b=\oint_\Gamma du.
\]
For a reconstructed reciprocal mode \(G\), the displaced-mode convention gives \(\Delta_\Gamma\theta_G=-G\cdot b\). The angular positions on the two circles alone do not determine \(b\) until the map to physical space and the reciprocal mode are specified.

## 5. Reproducible audit

The companion script \`scripts/audit_t101_trigram_phase_holonomy.py\` accepts two JSON arrays of eight measured phases (plus and minus circles), a calibrated frame offset \(\chi\), and orientation \(\sigma\). It constructs the 64 paired points on each \(T^2\), all 192 edges and 240 plaquettes per layer, the eight trigram complement residuals, and the 64 complementary-hexagram mismatches. It reports the plaquette holonomies separately from cross-circle mismatch.

Synthetic angles in tests are software fixtures only. They are not proposed physical measurements. T100 remains the node-charge/correlation layer; T101 supplies the two-circle angular geometry and the exact identifiability conditions for defects.

## 6. Evidence register

| Claim | Status |
|---|---|
| Eight trigram labels have measured phases on each of two circles | Input data / definition |
| Opposite-circle complement relation via calibrated \((\sigma,\chi)\) | Exact testable criterion |
| 64 paired hexagram comparisons, 192 edges and 240 squares per layer | Proved finite combinatorics |
| Endpoint phase differences have trivial plaquette \(U(1)\) holonomy | Proved exact identity |
| Cross-circle mismatch is itself a Frank angle or Burgers vector | Not claimed; requires frame/space reconstruction |
| Physical charge law from angular phases | Open; connect to T100 using measured node data |
