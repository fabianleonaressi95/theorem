# C60 — isotropic SBV lower bound

Date: 2026-11-21

Status: **proved lower-bound lemma** in the intrinsic polyhedral SBV formulation. The finite-face affine identification is recorded separately in C60_CF_POLYHEDRAL_AFFINE_THEOREM_2026-11-21.md.

## 1. Setting

Let \(\Sigma\) be a compact finite polyhedral surface, interpreted face by face in orthonormal tangent charts. Let
\[
g\in SBV(\Sigma;\mathbb R^3),\qquad
G\in L^1(\Sigma;\mathbb R^{3\times2}),
\]
and let \(u_n\in SBV(\Sigma;\mathbb R^3)\) satisfy
\[
u_n\to g\quad\text{in }L^1,\qquad
\nabla_\Sigma u_n\,\mathcal H^2
\stackrel{*}{\rightharpoonup}G\,\mathcal H^2.
\]
Assume
\[
\sup_n\int_{J_{u_n}}|[u_n]|\,d\mathcal H^1<\infty.
\]
The intrinsic derivative is understood in the facewise distributional sense, with the corresponding edge-trace jumps included in its singular part.

## 2. Singular-measure identification

Set \(\mu=D_\Sigma g-G\,\mathcal H^2\). The \(L^1\) convergence implies distributional convergence \(D_\Sigma u_n\to D_\Sigma g\). Subtracting the prescribed convergence of the absolutely continuous parts gives
\[
D^s_\Sigma u_n\longrightarrow\mu
\quad\text{in distributions}.
\]
For SBV maps,
\[
D^s_\Sigma u_n=[u_n]\otimes\nu_{u_n}\,
\mathcal H^1\!\llcorner J_{u_n},
\]
and, since \(|\nu_{u_n}|=1\),
\[
|D^s_\Sigma u_n|_*(\Sigma)
=\int_{J_{u_n}}|[u_n]|\,d\mathcal H^1.
\]
The assumed bound makes these matrix-valued measures bounded in total variation. Every weak-* convergent subsequence has distributional limit \(\mu\), so the weak-* limit is uniquely identified as \(\mu\). Lower semicontinuity of total variation gives
\[
\boxed{
\liminf_{n\to\infty}\int_{J_{u_n}}|[u_n]|\,d\mathcal H^1
\geq|\mu|_*(\Sigma).
}
\]
Since \(g\in SBV\),
\[
\mu=(\nabla_\Sigma g-G)\,\mathcal H^2+
[g]\otimes\nu_g\,\mathcal H^1\!\llcorner J_g.
\]
The two terms are mutually singular. Since \(|a\otimes\nu|_*=|a|\) for unit \(\nu\),
\[
\boxed{
\liminf_n\int_{J_{u_n}}|[u_n]|\,d\mathcal H^1
\geq
\int_\Sigma\|\nabla_\Sigma g-G\|_*\,d\mathcal H^2+
\int_{J_g}|[g]|\,d\mathcal H^1.
}
\]

## 3. Consequence for the total energy

Let
\[
E_W(u)=\int_\Sigma W(\nabla_\Sigma u)\,d\mathcal H^2+
\int_{J_u}|[u]|\,d\mathcal H^1.
\]
For \(W(F)=|F|_F\), the bulk lower bound follows from weak-* lower semicontinuity of the total variation of the absolutely continuous gradient measures:
\[
\liminf_n\int_\Sigma|\nabla_\Sigma u_n|_F\,d\mathcal H^2
\geq\int_\Sigma|G|_F\,d\mathcal H^2.
\]
For \(W(F)=|F|_F^2\), assume \(G\in L^2\) and bounded quadratic bulk energy along the subsequence under consideration. Weak compactness in \(L^2\), together with the prescribed measure convergence, identifies the weak limit with \(G\); weak lower semicontinuity yields the quadratic bulk bound.

Taking a subsequence that realizes the liminf of the **total** energy and applying both lower bounds on that same subsequence gives
\[
\boxed{
I_W(g,G)\geq
\int_\Sigma W(G)\,d\mathcal H^2+
\int_\Sigma\|\nabla_\Sigma g-G\|_*\,d\mathcal H^2+
\int_{J_g}|[g]|\,d\mathcal H^1.
}
\]
This is a lower bound, not a general identification of the infimum. Equality requires a recovery sequence.

## 4. Scope

The lemma applies to the stated isotropic linear jump cost. It does not extend by this proof to \(\psi(a,\nu)=|a|^2\), anisotropic surface densities, or admissible classes with an unpenalized Cantor part. For the quadratic bulk, the \(L^2\) condition is essential to the stated argument.

The finite-face affine recovery theorem is a separate upper-bound result under its own hypotheses; it does not imply recovery for general SBV data.
