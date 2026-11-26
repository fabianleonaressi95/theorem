# T114 — Gauge-covariant cubical Dirac–Kähler differential on Q6

**Classification:** finite-dimensional algebraic theorem, proved below under the stated cell-anchor and link conventions; numerical checks are implementation audits. No continuum spin-Dirac or Yang–Mills limit is claimed.

## 1. Cubical complex and fibres

Let X=I^6 be the standard cubical complex. Its cell counts in degrees 0 through 6 are
\[
(64,192,240,160,60,12,1),\qquad |X|=729.
\]
For each vertex v put a fibre V_v=C^2. For an oriented Q6 edge (v,v+e_i), let U_{v,i}\in SU(2) transport a vector in the upper-vertex fibre to the lower-vertex fibre:
\[
U_{v,i}:V_{v+e_i}\longrightarrow V_v.
\]
A k-cell is represented by (b;I), where b is its lower vertex and I=(i_0<\cdots<i_{k-1}) is its set of varying coordinate directions. Anchor its fibre at b. A local gauge is a family G_v\in SU(2), acting by
\[
(P_k\omega)_{(b;I)}=G_b\omega_{(b;I)}.
\]
The link transformation compatible with the stated transport direction is
\[
U'_{v,i}=G_vU_{v,i}G_{v+e_i}^{\dagger}.
\]

## 2. Covariant cubical coboundary

For a (k+1)-cell c=(b;i_0,\ldots,i_k), let c^-_p and c^+_p be its lower and upper k-faces normal to i_p. The lower face is anchored at b and the upper face at b+e_{i_p}. Define
\[
(D_U\omega)_c=
\sum_{p=0}^{k}(-1)^p
\left[
U_{b,i_p}\omega_{c^+_p}-\omega_{c^-_p}
\right].
\]
Both terms in each bracket lie in the fibre at b.

**Theorem.** Under the gauge transformations above,
\[
\boxed{D_{U'}=P_{k+1}D_UP_k^{\dagger}}
\]
on every degree. Consequently the Hermitian Dirac–Kähler operator
\[
H_U=D_U+D_U^{\dagger}
\]
obeys
\[
\boxed{H_{U'}=P H_U P^{\dagger}},\qquad P=\bigoplus_{k=0}^6P_k.
\]
In particular its spectrum is gauge invariant.

### Proof

For an upper-face term,
\[
U'_{b,i_p}(P_k\omega)_{c^+_p}
=G_bU_{b,i_p}G_{b+e_{i_p}}^{\dagger}
  G_{b+e_{i_p}}\omega_{c^+_p}
=G_bU_{b,i_p}\omega_{c^+_p}.
\]
The lower-face term transforms as
\[
(P_k\omega)_{c^-_p}=G_b\omega_{c^-_p}.
\]
Thus every signed summand transforms by the same factor G_b, exactly the gauge action on the anchored (k+1)-cell. This proves the coboundary identity. Since P is unitary, taking adjoints proves the identity for H_U. Unitary conjugation preserves the spectrum. \(\square\)

## 3. Flatness and curvature obstruction

For identity links, D_U is the ordinary cubical coboundary, hence D_U^2=0. For non-flat links, the two transports around a square need not agree. The corresponding plaquette holonomy is the obstruction to cancellation of the two routes; therefore D_U^2 is generally nonzero. This is the expected curvature of the coefficient connection, not a failure of the ordinary incidence identity.

The full cubical complex has 240 elementary square holonomies. Under a gauge transformation each based holonomy is conjugated at its base vertex, so its trace is gauge invariant.

## 4. Independent exterior Clifford factor

Let \Lambda^* C^6 be the 64-dimensional exterior module, with
\[
\gamma_i=\varepsilon_i+\iota_i,\qquad
\gamma_i\gamma_j+\gamma_j\gamma_i=2\delta_{ij}I.
\]
The local Clifford action is on this exterior factor, while SU(2) acts on the separate internal factor C^2. On C^2\otimes\Lambda^*C^6,
\[
(U\otimes I_{64})(I_2\otimes\gamma_i)
=(I_2\otimes\gamma_i)(U\otimes I_{64}).
\]
This is a product internal-gauge/exterior-Clifford module. It is not a Spin(6) connection or a lift of the RGS coframe connection.

## 5. Evidence and limits

- **Proved:** cell-anchor gauge covariance of the all-degree coboundary; covariance and spectral invariance of its Hermitian sum; independent tensor-factor commutation.
- **Exact by construction:** identity-link nilpotency and the cell counts of I^6.
- **Numerically audited in the source repository:** seeded local SU(2) covariance, Hermiticity, flat D_U^2=0, nonzero D_U^2 for a curved link field, 240 plaquette conjugations, Wilson-trace invariance, Clifford relations and tensor-factor commutation.
- **Not established:** a Spin(6) or Spin(1,3) connection, continuum Dirac limit, absence of fermion doubling, Mosco/spectral convergence, or a physical Yang–Mills coupling derived from RGS.

## 6. Reproducibility

Source implementation: \`src/rgs_q6_gauged_full_clifford.py\`.  
Source test: \`tests/test_rgs_q6_gauged_full_clifford.py\`.  
Source specification: \`docs/RGS_Q6_GAUGED_FULL_CLIFFORD_TRANSPORT.md\`.

Run in \`rgs-qlg-quaternion-bridge\`:
\`\`\`bash
PYTHONPATH=. python -m pytest tests/test_rgs_q6_gauged_full_clifford.py -q
\`\`\`

The theorem is finite and algebraic; numerical tests support the implementation but are not a substitute for the proof.
