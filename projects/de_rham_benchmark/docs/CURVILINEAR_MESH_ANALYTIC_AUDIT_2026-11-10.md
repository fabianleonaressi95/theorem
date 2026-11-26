# Analytic audit of the curvilinear cubical mesh maps

**Date:** 10 November 2026  
**Scope:** global geometry of the `sinusoid` and `axis_bump` maps used by
`configs/feec_default.json`. This note upgrades the default-configuration
injectivity checks from sampled diagnostics to analytic sufficient conditions.
It does not prove FEEC projection stability, discrete compactness, or Mosco
convergence.

## 1. Mesh family and conformity

The physical mesh is the image of the structured reference cubical mesh
under one global map
\[
\Phi:[0,1]^d\longrightarrow\mathbb R^d,\qquad
F_{K,h}(\xi)=\Phi(p_K+h\xi).
\]
The cell map is a restriction of the same global function on every cell.
Consequently, the two traces on a shared reference face are restrictions of
the same \(\Phi\); shared geometric faces and their parameterizations
coincide exactly (up to floating-point evaluation). This is stronger than
checking only that the number of incident cells is correct.

For the two nonlinear map families below, the displacement vanishes on
\(\partial[0,1]^d\). Thus the boundary is fixed pointwise. An injectivity
proof for \(\Phi\) then establishes a globally non-folded, conforming
curvilinear image of the reference cube.

## 2. A reusable global injectivity lemma

Let \(\Phi(x)=x+u(x)\) on the convex cube \(\overline\Omega\).
If
\[
L:=\sup_{x\in\overline\Omega}\|Du(x)\|_2<1,
\tag{2.1}
\]
then for all \(x,y\in\overline\Omega\), the mean-value estimate gives
\[
\begin{aligned}
|\Phi(x)-\Phi(y)|
&\ge |x-y|-|u(x)-u(y)|\\
&\ge (1-L)|x-y|.
\end{aligned}
\tag{2.2}
\]
Therefore \(\Phi\) is globally injective and has a Lipschitz inverse on
its image. Moreover, every singular value of \(D\Phi=I+Du\) lies in
\([1-L,1+L]\), so
\[
(1-L)^d\le \det D\Phi\le(1+L)^d
\]
when the determinant is positive; positivity follows continuously from
the homotopy \(I+tDu\), since \(\|tDu\|_2<1\) for \(0\le t\le1\).
This is a global, refinement-independent sufficient condition. It is not
necessary: maps can be injective even when this contraction bound fails.

## 3. Sinusoidal rank-one map

The implementation is
\[
\Phi(x)=x+aP(x)c,\qquad
P(x)=\prod_{j=1}^d\sin(m\pi x_j),\qquad |c|_2=1.
\]
The displacement vanishes on every boundary face. Its Jacobian is
\[
D\Phi=I+a\,c\otimes\nabla P,
\qquad
\det D\Phi=1+a\,\nabla P\cdot c,
\tag{3.1}
\]
where the determinant identity is the matrix determinant lemma.
Since
\[
|\partial_jP|\le m\pi,\qquad
\|\nabla P\|_2\le m\pi\sqrt d,
\]
we obtain
\[
\|D(\Phi-I)\|_2
=|a|\,\|c\|_2\,\|\nabla P\|_2
\le |a|m\pi\sqrt d.
\tag{3.2}
\]
Thus the explicit sufficient condition
\[
|a|m\pi\sqrt d<1
\tag{3.3}
\]
proves global injectivity and uniform bi-Lipschitz bounds. For the default
direction \(c=e_1\), equation (3.1) also gives the sharper orientation
bound \(\det D\Phi\ge1-|a|m\pi\).

### Default configurations

| Case | \(d\) | \(a\) | \(m\) | Bound \(L\le |a|m\pi\sqrt d\) | Result |
|---|---:|---:|---:|---:|---|
| `sinusoid_2d` | 2 | 0.20 | 1 | 0.888577 | globally injective |
| `aniso_metric_2d` | 2 | 0.15 | 1 | 0.666432 | globally injective |
| `axis_bump_2d` | 2 | 0.15 | — | 0.666432 | globally injective |
| `sinusoid_3d` | 3 | 0.15 | 1 | 0.816248 | globally injective |

All three satisfy the strict bound (3.3). For the default direction \(e_1\),
the sharper determinant lower bounds are respectively
\(1-0.2\pi=0.371681\) and
\(1-0.15\pi=0.528761\). These are analytic lower bounds, not sampled
minimum values.

## 4. Multi-directional axis-bump map

The implementation is
\[
\Phi_i(x)=x_i+a_i\sin(\pi x_i)\sin(\pi x_{i+1}),
\]
with cyclic indices. On a boundary face \(x_j\in\{0,1\}\), the
displacement components \(u_j\) and \(u_{j-1}\) vanish because they
contain \(\sin(\pi x_j)\); all other components are independent of
\(x_j\). Hence the entire boundary is fixed pointwise.

Row \(i\) of \(Du\) has at most two nonzero entries:
\[
\partial_i u_i=a_i\pi\cos(\pi x_i)\sin(\pi x_{i+1}),\qquad
\partial_{i+1}u_i=a_i\pi\sin(\pi x_i)\cos(\pi x_{i+1}).
\]
The sum of their squared trigonometric factors is
\[
\cos^2(\pi x_i)\sin^2(\pi x_{i+1})
+\sin^2(\pi x_i)\cos^2(\pi x_{i+1})\le1.
\]
Therefore the Euclidean norm of row \(i\) is at most \(\pi|a_i|\), and
\[
\|Du\|_2\le\|Du\|_F
\le\pi\Big(\sum_i a_i^2\Big)^{1/2}.
\tag{4.1}
\]
A sufficient global injectivity condition is consequently
\[
\pi\|a\|_2<1.
\tag{4.2}
\]

For the default equal amplitudes \(a_i=0.15\), the bounds are
\(\pi(0.15\sqrt2)=0.666432<1\) in 2D and
\(\pi(0.15\sqrt3)=0.816248<1\) in 3D. The default 2D
`axis_bump` mesh is therefore globally injective by (2.2).

## 5. Pullback metric and uniform ellipticity

Let the ambient metric satisfy
\[
g_-I\le G(y)\le g_+I.
\]
Since \(g= D\Phi^T G(\Phi)D\Phi\), the preceding bounds imply
\[
g_-(1-L)^2I\le g\le g_+(1+L)^2I.
\tag{5.1}
\]
For the identity ambient metric, \(g_-=g_+=1\). For the configured
anisotropic metric \(G=\operatorname{diag}(1,2.5)\), one has
\(g_-=1\), \(g_+=2.5\). Thus the default nonlinear configurations
have an analytic, mesh-independent ellipticity bound. The constants
obtained from the simple contraction estimate are conservative; sampled
singular values and condition numbers in the numerical report may be
sharper but are not substitutes for (5.1).

The physical cell Jacobian is
\[
DF_{K,h}(\xi)=D\Phi(p_K+h\xi)\,hI
\]
for the unit, isotropically refined grids used here. Equation (5.1)
therefore supplies the standard \(h^2\)-scaled pullback metric
ellipticity required by the local FEEC mass-equivalence estimate.

## 6. What this closes, and what it does not

### Closed analytically for the shipped default maps

1. The `sinusoid` cases in 2D and 3D satisfy a global contraction
   criterion, so they are injective and orientation preserving.
2. The `axis_bump` 2D case satisfies the same type of criterion.
3. The maps fix the boundary and are restrictions of one global smooth
   map; shared-face conformity follows exactly from the construction.
4. The configured ambient metrics are uniformly positive definite.
   Combining these facts gives explicit, refinement-independent
   ellipticity constants for the pullback metric.

### Still open

1. The amplitude/frequency sweeps outside the strict bounds above need
   their own analytic certificates or interval-arithmetic verification.
   Positive determinants at quadrature points alone do not prove global
   injectivity.
2. The map-quality code's sampled \(\det D\Phi\), singular values and
   face checks remain useful diagnostics, but must be labelled as sampled
   checks unless accompanied by a global estimate.
3. The face-integral cochain interpolator is exactly commuting on smooth
   forms by Stokes' theorem, but its degree-zero point evaluation is not
   bounded on \(H^1\) in dimensions 2 and 3. It is therefore not the
   uniformly bounded \(H\Lambda\) projection required by FEEC
   convergence theory.
4. The observed boundary layer in \(\delta_h\pi_hu-\pi_h\delta u\)
   for the unconstrained complex is not removed by geometric injectivity.
   Boundary conditions and the continuous/discrete adjoint domains must
   be matched before interpreting this residual as an interior
   consistency failure.
5. Uniform commuting smoothed projections, adjoint graph convergence,
   a discrete Gaffney/compactness estimate, Mosco convergence,
   norm-resolvent convergence and harmonic-kernel stability remain open.

## 7. Required numerical follow-up

The following checks should be added to the executable audit for every
nonlinear map configuration:

- evaluate the analytic contraction bound and store it in JSON;
- fail the certified-injectivity flag unless the bound is strictly below 1;
- independently check \(\det D\Phi>0\) on a dense validation grid;
- report sampled \(\sigma_{\min}(D\Phi)\) and
  \(\operatorname{cond}(g)\), clearly marked as sampled;
- test boundary identity and shared-face coordinate agreement;
- repeat mass quadrature with increased orders and report convergence of
  the assembled Gram matrices and their smallest eigenvalues.

The dense-grid determinant check is a regression diagnostic, not the proof;
the proof is the analytic estimate (3.2) or (4.1). For parameter sweeps
that fail the contraction criterion, use interval arithmetic or a
separate global univalence argument rather than silently treating a
positive sampled determinant as a certificate.

## 8. Scientific status

**Analytically established:** global injectivity and uniform pullback
metric ellipticity for the default sinusoid and axis-bump maps under the
explicit bounds above.

**Numerically verified in the existing benchmark:** finite-level
incidence identities, mass symmetry/positivity diagnostics, face
commutation on selected smooth forms, projection errors, adjoint
residuals and spectral indicators as recorded in `docs/REPORT.md` and
`docs/FEEC_PROJECTIONS.md`.

**Not established:** a uniformly bounded commuting projection on the full
\(H\Lambda\) graph spaces, discrete compactness, Mosco convergence,
norm-resolvent convergence, or spectral convergence on the full
curvilinear refinement family.
