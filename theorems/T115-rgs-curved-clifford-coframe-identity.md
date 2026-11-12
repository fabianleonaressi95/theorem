# T115 — Curved Clifford relation from an invertible RGS spatial coframe

**Classification:** finite-dimensional algebraic theorem, proved below. The source test is a numerical implementation check. The static time leg and the RGS coframe are hypotheses, not field equations.

## 1. Data and conventions

At each vertex v let E_v\in GL^+(3,R), the invertible real 3x3 matrices with positive determinant. Define the static tetrad
\[
e^A{}_\mu(v)=
\begin{pmatrix}1&0\\0&E_v\end{pmatrix},
\qquad \eta_{AB}=\operatorname{diag}(-1,1,1,1).
\]
The induced metric and inverse tetrad are
\[
g_{\mu\nu}(v)=e^A{}_\mu(v)\eta_{AB}e^B{}_\nu(v),
\qquad e_A{}^\mu(v)=(e^{-1})^\mu{}_A.
\]
Let constant flat gamma matrices satisfy
\[
\gamma^A\gamma^B+\gamma^B\gamma^A=2\eta^{AB}I_4.
\]
Define the curved gamma matrices by
\[
\Gamma^\mu(v)=e_A{}^\mu(v)\gamma^A.
\]

## 2. Theorem

For every vertex v and all coordinate indices \mu,\nu,
\[
\boxed{\Gamma^\mu(v)\Gamma^\nu(v)+\Gamma^\nu(v)\Gamma^\mu(v)
=2g^{\mu\nu}(v)I_4.}
\]
Here g^{\mu\nu} is the inverse of the induced metric.

### Proof

By the flat Clifford relation,
\[
\begin{aligned}
\{\Gamma^\mu,\Gamma^\nu\}
&=e_A{}^\mu e_B{}^\nu\{\gamma^A,\gamma^B\}\\
&=2e_A{}^\mu e_B{}^\nu\eta^{AB}I_4.
\end{aligned}
\]
The inverse-tetrad identity gives
\[
g^{\mu\nu}=e_A{}^\mu e_B{}^\nu\eta^{AB}.
\]
Substitution yields the claimed relation. \(\square\)

The positive determinant condition fixes orientation and ensures the spatial coframe is nondegenerate. The algebraic Clifford identity itself requires invertibility; it does not require a connection or torsion.

## 3. Finite RGS/Q6 specialization

For the recovered 64-site seed, the source construction supplies one E_v per vertex and uses the static ansatz above. The test checks all 16 pairs (\mu,\nu) at all 64 vertices, as well as inversion of the induced metric. This is a pointwise algebraic test, not a refinement theorem.

## 4. Evidence and limits

- **Proved:** the curved Clifford anticommutator follows identically from the inverse tetrad and flat Clifford relations.
- **Numerically verified by the source test:** pointwise residuals for the supplied finite array and metric-inverse consistency.
- **Assumed:** static time leg e^0{}_0=1, zero shift, and a prescribed spatial coframe E_v.
- **Not established:** a dynamical Lorentzian tetrad, Levi-Civita or Cartan connection from this identity alone, torsion, Einstein/Einstein–Cartan equations, continuum Dirac limit, or Mosco convergence.

## 5. Reproducibility

Source implementation: \`src/discrete_dirac.py\`, functions \`static_tetrad_4d\`, \`curved_gamma_matrices\`, and \`curved_clifford_audit\`.  
Source tests: \`tests/test_discrete_dirac.py\`.

Run in \`rgs-qlg-quaternion-bridge\`:
\`\`\`bash
PYTHONPATH=. python -m pytest tests/test_discrete_dirac.py -q
\`\`\`
