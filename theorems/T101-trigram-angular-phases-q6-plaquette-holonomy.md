# T101 — Two-circle trigram phases, complementary pairs, and Q6 defect winding

**Status:** exact finite construction and combinatorial audit; measured phases, circle registration, physical-space reconstruction, and defect classification remain data-dependent/open.

**Purpose.** Each trigram has a measurable angular position on one of two opposite circles. Its linewise complement is compared on the other circle. The resulting cross-circle mismatch is then lifted to the 64-hexagram hypercube and tested around all 240 elementary squares. This preserves the individual hexagrams as the node-level degrees of freedom of T100.

## 1. Two circles and the eight complementary trigram pairs

Let \(C_+\) and \(C_-\) be two measured circles. For every trigram \(t\in\{0,\ldots,7\}\), record phases \(\theta_t^+,\theta_t^-\in\mathbb R/(2\pi\mathbb Z)\). If centres and radii are known, positions are
\[
x_t^\pm=c_\pm+R_\pm(\cos\theta_t^\pm,\sin\theta_t^\pm).
\]
The linewise complement is \(\bar t=t\mathbin{\mathrm{xor}}7\), with bit 0 the bottom line and bit 2 the top line. Calibrate the relative circle-frame registration
\[
\rho(\theta)=\sigma\theta+\chi\pmod{2\pi},\qquad \sigma\in\{+1,-1\}.
\]
Here \(\chi\) is the measured frame offset and \(\sigma\) records whether the two angular orientations agree or are reversed. Define the opposite-circle complement mismatch
\[
\epsilon_t=\operatorname{wrap}\big(\theta_{\bar t}^--\sigma\theta_t^+-\chi\big).
\]
The special antipodal registration corresponds to the calibrated choice \(\chi=\pi\); it is not imposed without measurement. The eight residuals contain four complementary pairs, with the pairwise relation determined by the chosen registration.

## 2. Lift to the 64 individual hexagrams

Write \(h=\ell+8u\), with lower trigram \(\ell\) and upper trigram \(u\). Each circle layer defines a labelled 64-point configuration on a two-torus:
\[
\Phi_\pm(h)=\big(e^{i\theta_\ell^\pm},e^{i\theta_u^\pm}\big)\in T^2.
\]
The complementary hexagram is \(\bar h=h\mathbin{\mathrm{xor}}63\). Its cross-circle mismatch relative to \(h\) is
\[
E_h=(\epsilon_\ell,\epsilon_u).
\]
Thus the 64 hexagrams inherit a two-component mismatch field from their two constituent trigram positions, while remaining distinct charge-bearing nodes. The map does not identify lower/upper trigram decomposition with a 32/32 bipartition.

## 3. The 192 edges and 240 elementary squares

The Q6 one-skeleton has 64 vertices and 192 edges. Bits \(0,1,2\) change the lower trigram (96 edges); bits \(3,4,5\) change the upper trigram (96 edges). For each pair of directions \(i<j\), and each base vertex \(h\) whose bits \(i,j\) are zero, the elementary square is
\[
p=(h,\ h\mathbin{\mathrm{xor}}2^i,\
h\mathbin{\mathrm{xor}}2^i\mathbin{\mathrm{xor}}2^j,\
h\mathbin{\mathrm{xor}}2^j).
\]
There are exactly \(\binom62\,2^4=240\) such squares.

Within either circle layer, endpoint phase differences are exact vertex differences and therefore form a pure-gauge \(U(1)\) connection. Their Wilson product around every square is one. This does not exhaust the defect information: the *cross-circle mismatch field* \(E_h\) is a separate observable.

For an oriented edge \(e=(h,h')\), define the mismatch-phase increment using the component changed by that edge:
\[
d_e=
\begin{cases}
\operatorname{wrap}(\epsilon_{\ell'}-\epsilon_\ell),&i<3,\\
\operatorname{wrap}(\epsilon_{u'}-\epsilon_u),&i\ge3.
\end{cases}
\]
The integer phase-winding index on a square is
\[
n_p=\frac{1}{2\pi}\sum_{e\in\partial p}^{\rm oriented}d_e\in\mathbb Z,
\]
with principal increments in \((-\pi,\pi]\). Numerically, the sum is rounded to the nearest integer after checking its residual from \(2\pi\mathbb Z\). A nonzero \(n_p\) is a **candidate vortex/winding defect of the cross-circle mismatch field**. Mixed lower/upper plaquettes have zero winding for this separable two-component construction; lower-only and upper-only squares test the corresponding trigram mismatch sectors.

## 4. From phase winding to disclination or dislocation

The winding number is a topological phase diagnostic, not automatically a material defect label. Its physical interpretation depends on what the measured angular phase represents:

- If the mismatch phase is a calibrated local-frame orientation, with an \(n\)-fold rotational identification, a winding can encode Frank/disclination charge. For orientation \(\alpha\) defined modulo \(2\pi/n\), the Frank angle is obtained from the lifted orientation winding with the declared \(n\)-fold convention.
- If it is the phase of a translational density-wave mode with reciprocal vector \(G\), a winding \(2\pi m\) gives \(G\cdot b=-2\pi m\) under the displaced-mode convention, constraining the Burgers vector \(b\).
- If the phase is only an abstract label or an uncalibrated angular coordinate, \(n_p\) remains a mathematical winding index and cannot be called a Frank angle or Burgers vector.

A separate local-frame link connection \(\alpha_e\) can also be measured. Its rotational holonomy is
\[
\mathcal H_p=\exp\left(i\sum_{e\in\partial p}\alpha_e\right).
\]
A nontrivial value is evidence of frame holonomy; the Frank angle requires calibration of the frame and its rotational symmetry. A translational defect additionally requires a spatial embedding \(X_h\), displacement/registration field, or coframe, with
\[
b=\oint_\Gamma du.
\]
The eight phase pairs alone do not determine physical-space coordinates or a Burgers vector.

## 5. Reproducible audit and evidence boundary

The companion script \`scripts/audit_t101_trigram_phase_holonomy.py\` accepts two JSON arrays of eight measured phases, one for each circle, plus the calibrated frame offset \(\chi\) and relative orientation \(\sigma\). It reports:
- all eight cross-circle trigram complement residuals;
- all 64 hexagram mismatch pairs;
- 192 edges and 240 squares per Q6 layer;
- pure-gauge Wilson holonomies on each layer;
- all 240 winding indices of the lifted complement-mismatch field.

Synthetic angles in tests are software fixtures, not physical measurements. No charge law is invented. T100 remains the charge/correlation model; T101 provides the opposite-circle phase geometry and a falsifiable route to candidate defect indices.

## 6. Evidence register

| Claim | Status |
|---|---|
| Opposite-circle complement residuals \(\epsilon_t\) | Exact measurable definition |
| 64 two-component hexagram mismatch values \(E_h\) | Exact lift from trigram data |
| 192 edges and 240 square faces of Q6 | Proved finite combinatorics |
| Endpoint-phase Wilson product on either layer is one | Proved pure-gauge identity |
| Nonzero mismatch winding \(n_p\) | Exact discrete phase-vortex diagnostic |
| Winding as Frank/disclination charge | Conditional on calibrated orientation field and symmetry |
| Winding as Burgers/dislocation charge | Conditional on translational density-wave phase and reciprocal vector |
| Physical Burgers vector and material Frank angle | Require spatial/frame reconstruction and calibration |
