# T069 — Q6 antipodality, RGS coordinate inversion, Walsh sectors and covariance

**Status:** exact finite identities for the stated pair decompositions and Walsh actions; numerical verification for the recovered 64-point RGS seed. The phase/dynamics and cell-covariance bridges remain open.

## 1. Purpose and essential distinction

Let Q6 have six-bit big-endian labels (v=0,\ldots,63). The canonical graph antipode is
\[
a_6(v)=v\mathbin{\mathrm{XOR}}(2^6-1)=v\mathbin{\mathrm{XOR}}63.
\]
The recovered RGS seed is ordered in eight blocks: the first three bits select one of eight orbit representatives, and the last three bits select its coordinate signs. Consequently the coordinate inversion of this particular labelled seed is instead
\[
a_{\rm RGS}(v)=v\mathbin{\mathrm{XOR}}7.
\]
These are different involutions. This distinction is decisive: the central inversion of the RGS point cloud must not be identified with the canonical antipode of the six-cube graph.

The seed convention is implemented in `rgs-qlg-quaternion-bridge/src/rgs_psu_fibred_intertwiner.py` and reconstructed/hash-checked by `src/rgs_ellis_refinement.py`. The audit in this repository independently reproduces the documented orbit representatives and sign ordering.

## 2. Pair decomposition and total covariance

For any involution (a) without fixed points on 64 labels, choose one representative from each of its 32 pairs and write
\[
m_i=\frac{X_i+X_{a(i)}}2,\qquad
d_i=\frac{X_i-X_{a(i)}}2.
\]
With a symmetric Bernoulli sign (σ\in\{-1,+1\}), (P(\sigma=+1)=P(\sigma=-1)=1/2), the paired observation is (X_{i,\sigma}=m_i+\sigma d_i). For uniform pair weights (q_i=1/32),
\[
\operatorname{Cov}(X\mid i)=d_i d_i^T,
\]
and
\[
\boxed{\operatorname{Cov}(X)=\frac1{32}\sum_i d_i d_i^T+
\frac1{32}\sum_i(m_i-\bar m)(m_i-\bar m)^T.}
\]
This is the finite law of total covariance. It holds for either involution; the two terms depend on which pairing is chosen.

## 3. Walsh actions

For χ_S(v)=(-1)^{v\cdot S}, the bit-flip involution (a_r(v)=v\mathbin{\mathrm{XOR}}r) acts by
\[
\chi_S(a_r(v))=(-1)^{\operatorname{popcount}(r\mathbin{\&}S)}\chi_S(v).
\]
Thus the even/odd Walsh sectors are defined relative to the chosen flip mask (r), not independently of it.

For the canonical Q6 antipode (r=63), the sign is ((-1)^{|S|}), giving the familiar 32-dimensional sectors according to the parity of (|S|). For the RGS coordinate inversion (r=7), the sign is instead ((-1)^{\operatorname{popcount}(S\mathbin{\&}7)}): parity is determined by the number of selected sign-fibre bits (the last three label bits).

## 4. Numerical audit of the recovered RGS seed

The finite audit reconstructs the eight orbit representatives from the archived constants in the bridge source, then applies all eight sign triples. It obtains:

- (\max_v\|X_{a_{\rm RGS}(v)}+X_v\|_\infty=0) to floating-point precision;
- (\max_v\|X_{a_6(v)}+X_v\|_\infty\approx1.4234808254), so the graph antipode is not the coordinate inversion;
- the point-cloud mean is zero and its normalized covariance is
  \[
  \Sigma_X=\frac1{64}\sum_v X_vX_v^T=\frac54 I_3;
  \]
- pairing by (a_{\rm RGS}) gives zero pair means and within-pair covariance (\frac54I_3);
- pairing by (a_6) gives nonzero pair means. The two terms in the total-covariance identity are approximately (0.978032165055798I_3) and (0.271967834944202I_3), whose sum is (1.25I_3).

The normalized Walsh coefficients are \hat X(S)=64^{-1}\sum_v\chi_S(v)X_v. Their squared Frobenius energy splits under the canonical graph antipode as
\[
E_{|S|\,\mathrm{even}}\approx0.8159035048326072,\qquad
E_{|S|\,\mathrm{odd}}\approx2.934096495167399.
\]
Neither global Q6 parity sector vanishes. Under the RGS coordinate inversion, however, the even sign-fibre sector vanishes (up to numerical roundoff) and all energy lies in the odd sign-fibre sector, exactly as required by (X_{a_{\rm RGS}(v)}=-X_v).

## 5. What this establishes — and what it does not

**Exact algebraic statements:** the pair mean/difference decomposition; the law of total covariance; the Walsh character transformation under any specified bit-flip mask.

**Numerically verified finite-model statements:** the recovered RGS seed's coordinate inversion is (v\mapsto v\mathbin{\mathrm{XOR}}7), not the canonical Q6 graph antipode (v\mapsto v\mathbin{\mathrm{XOR}}63); the point-cloud covariance is (5I_3/4); the Walsh energy behaves accordingly.

**Not established:** a physical phase variable, a time-evolution or oscillation equation, a physical Bernoulli process, or a canonical comparison with a triangle/cell covariance \(\Sigma_F\). The last comparison requires a specified map from vertex observables to geometric cells and a declared normalization. The point-cloud covariance \(\Sigma_X\) is not the within-cell covariance \(\Sigma_F\).

A complex scalar observable obtained by a nonzero linear functional of the coordinates changes sign under (a_{\rm RGS}), hence its phase shifts by \(\pi\) where it is nonzero. This is a consequence of that chosen complex encoding, not an intrinsic phase dynamics of Q6.

## 6. Reproduction

Run:
```bash
python audits/audit_t069_q6_antipodal_covariance.py
pytest -q tests/test_t069_q6_antipodal_covariance.py
```

The audit is self-contained and uses only NumPy. It reproduces the seed coordinate convention documented by the bridge implementation; it does not require importing the bridge repository.
