# S.5 — Fourth-jump-moment consistency of symmetric graph Laplacians

**Status: PROVED under the stated moment and smoothness hypotheses.** This is the refinement/Taylor fourth-moment result. It is distinct from the 64-site RGS seed tensor in S.4.

## 1. Setting

Let (a>0) be a mesh scale and let a finite stencil at (x) consist of jumps (a\xi_{xy}), weights (w_{xy}\geq0), and total weight (m_a(x)>0). Consider
[
\Delta_a f(x)=\frac1{a^2m_a(x)}
\sum_yw_{xy}\bigl(f(x+a\xi_{xy})-f(x)\bigr).
]
The stencil may vary with (a) and (x). All moment tensors below include the weights and are normalized by (m_a(x)):
[
M_a^{(r)}(x)=\frac1{m_a(x)}\sum_yw_{xy}\,\xi_{xy}^{\otimes r}.
]

## 2. Taylor expansion through fourth order

For (f\in C^5) on a neighbourhood of all stencil points,
[
\begin{aligned}
\Delta_af(x)
={}&\frac1a M_a^{(1)}\!:\nabla f
+\frac12M_a^{(2)}\!:\nabla^2f
+\frac a6M_a^{(3)}\!:\nabla^3f\\
&+\frac{a^2}{24}M_a^{(4)}\!:\nabla^4f
+\mathcal R_a^{(5)}(x).
\end{aligned}
]
Here the colon denotes full contraction of tensors of matching order. If (|\xi_{xy}|\leq C_\xi) and (\sup\|M_a^{(5)}\|_{\mathrm{abs}}\leq C_5) uniformly, then
[
|\mathcal R_a^{(5)}(x)|
\leq \frac{a^3C_\xi^5}{120}
\sup_{z}\|D^5f(z)\|_{\mathrm{op}}
\frac1{m_a(x)}\sum_yw_{xy},
]
with the weight normalization absorbed into (M_a^{(r)}); equivalently, under the normalized stencil convention above, one may take the uniform bound (a^3C_\xi^5\sup\|D^5f\|/120).

The formula is the multivariate Taylor formula applied termwise; it does not assume isotropy.

## 3. Second-order consistency criterion

Suppose, uniformly in (x) and (a	o0),
[
M_a^{(1)}=0,qquad M_a^{(3)}=0,
]
and
[
\frac12M_a^{(2)}=g^{ij}(x)+O(a^2)
]
in the chosen tensor norm, while (M_a^{(4)}) is uniformly bounded. Then
[
\boxed{\Delta_af(x)=g^{ij}(x)\partial_{ij}f(x)+O(a^2)}
]
uniformly for (f\in C^5) with bounded derivatives through order five.

More generally, if (M_a^{(3)}=O(a)), its contribution (aM_a^{(3)}:D^3f/6) is also (O(a^2)). If the third moment is not zero or not sufficiently small, an (O(a)) consistency term generally remains. Thus symmetry/third-moment cancellation is an essential hypothesis, not a decorative assumption.

The fourth moment supplies the leading explicit truncation correction
[
\frac{a^2}{24}M_a^{(4)}:D^4f.
]
A uniform fourth-moment bound controls the size of this term; convergence of (M_a^{(4)}) gives a limiting fourth-order error coefficient.

## 4. Isotropy versus anisotropy

For an isotropic stencil in dimension (d), a fourth-order tensor may have the form
[
M^{(4)}_{ijkl}=\kappa_a(
\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}),
]
in which case
[
M^{(4)}:D^4f=3\kappa_a\,\Delta^2f
]
for a Euclidean Hessian convention. For a merely cubic-symmetric stencil, a nonzero anisotropic residual can remain and the fourth-order correction need not be a multiple of the biharmonic operator.

This is the correct conceptual link with S.4: both objects are rank-four moments, but S.4 is a raw fourth moment of a fixed 64-point cloud, whereas (M_a^{(4)}) is a normalized jump moment of a refinement stencil. Their numerical components cannot be identified without an explicit common stencil and normalization.

## 5. Relation to the metric second moment and curvature claims

The second moment determines the principal second-order operator. In a local coordinate frame, the intended metric consistency is encoded by
[
\frac12M_a^{(2)}\longrightarrow g^{-1}
]
(up to the declared sign and Laplacian convention). The fourth moment controls the next truncation term. This is a consistency statement for smooth test functions.

It does **not** by itself imply convergence of metrics, curvature tensors, Einstein tensors, resolvents, spectra or variational energies. In particular, a claim such as (\|g_a-g\|_\infty=O(a^2)) requires a separate reconstruction of (g_a) and hypotheses on the stencil moments; curvature convergence requires stronger derivative control, typically at least a compatible (C^2)-type convergence.

## 6. Evidence classification

- **PROVED:** Taylor expansion and the stated (O(a^2)) consistency criterion under the uniform moment hypotheses.
- **CONDITIONAL:** isotropic fourth-order correction reduces to a multiple of (\Delta^2) when the displayed isotropic tensor form holds.
- **OPEN:** verifying these hypotheses for the specific Q6/RGS/PRISM refinement family; deriving a curvature or Einstein limit; identifying its fourth jump moment with the S.4 64-site anisotropy tensor.
