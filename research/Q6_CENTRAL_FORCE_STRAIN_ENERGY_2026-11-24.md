# Q6 central-force strain energy and microscopic stress: explicit derivation

**Date:** 2026-11-24  
**Status:** [P] exact finite-graph variational identities for any supplied embedding and positive spring constants; [N] finite-difference audit; [C] candidate embedding from the Q6/Jitterbug quotient; [O] physical 3D Q6-to-Jitterbug lift, material parameters, and hydrodynamic limit.

## 1. Why this construction is needed

A graph does not determine a material energy by itself. The 64 vertices and 192 edges of \(Q_6\) determine incidence, but not physical edge lengths, spatial directions, stiffnesses, masses, or a 3D embedding. T130's local least-squares gradient and positive resistance assembly
\[
R_h=\sum_i w_iJ_i^TD_iJ_i
\]
are a variational/discretization framework; they do not supply those missing material inputs. T131 likewise requires a Hessian derived from a specified potential and a stress derived from that same energy.

The construction below therefore takes an embedding as an explicit input and derives every force and stress from one central-force energy. It does not assign arbitrary physical weights to Q6 edges.

## 2. Data and notation

Let \(G=Q_6=(V,E)\), \(|V|=64\), \(|E|=192\). Choose an oriented incidence matrix \(B\in\mathbb R^{|E|\times|V|}\), with row \(b_e^T\) equal to \(-1\) at the tail and \(+1\) at the head of edge \(e=(v,w)\).

A spatial realization is a map
\[
y:V\longrightarrow\mathbb R^d,\qquad
r_e=y_w-y_v,\quad \ell_e=|r_e|>0,\quad n_e=r_e/\ell_e.
\]
The dimension \(d\), coordinates \(y_v\), and positive spring constants \(\kappa_e\) are physical/model inputs. Let \(u_v\in\mathbb R^d\) be the displacement of vertex \(v\), and \(u=(u_v)_{v\in V}\in\mathbb R^{d|V|}\).

For a symmetric strain tensor \(\varepsilon\), impose the affine deformation \(F_\varepsilon=I+\varepsilon\) on the reference bond while retaining the non-affine displacement \(u\).

## 3. One energy, with no independently chosen stress

The central-force Hookean energy is
\[
\boxed{
H(u,\varepsilon)=\frac12\sum_{e=(v,w)\in E}
\kappa_e\left(
\left|(I+\varepsilon)r_e+u_w-u_v\right|-\ell_e
\right)^2.
}
\tag{3.1}
\]
The rest length is the reference length \(\ell_e\). Thus \(u=0,\varepsilon=0\) is stress-free. The total extensive microscopic stress conjugate to symmetric strain is defined by
\[
\boxed{\Pi_{ij}(u)=-\left.\frac{\partial H(u,\varepsilon(\xi))}
{\partial\xi_{ij}}\right|_{\xi=0}.}
\tag{3.2}
\]
For clarity about shear factors, use independent strain coordinates \(\xi_{ij}\) with \(i\le j\) and write \(\varepsilon=\sum_{i\le j}\xi_{ij}S^{ij}\), where \(S^{ii}=e_ie_i^T\) and \(S^{ij}=(e_ie_j^T+e_je_i^T)/2\) for \(i<j\). Thus an off-diagonal tensor entry is \(\varepsilon_{ij}=\xi_{ij}/2\). The stress component conjugate to \(\xi_{ij}\) is defined by \(\Pi_{ij}=-\partial H/\partial\xi_{ij}\); this is the standard symmetric-tensor contraction convention.

Put \(s_e=r_e+(u_w-u_v)\) and \(\delta\ell_e=|s_e|-\ell_e\). Direct differentiation with respect to the conjugate coordinate \(\xi_{ij}\) gives the exact, non-expanded stress:
\[
\boxed{
\Pi_{ij}(u)=-
\sum_{e\in E}\kappa_e\,\delta\ell_e\,
\frac{s_e}{|s_e|}\cdot S^{ij}r_e.
}
\tag{3.3}
\]
This is the discrete virial stress obtained from the same energy as the force law. It includes the full nonlinear dependence on \(u\); no stress matrix is fitted independently.

## 4. Harmonic Hessian and the linear microscopic stress

At zero strain and to second order in displacements,
\[
|r_e+(Bu)_e|-\ell_e
=n_e\cdot(u_w-u_v)+O(|u|^2/\ell_e).
\]
Define the rigidity matrix \(\mathcal R:\mathbb R^{d|V|}\to\mathbb R^{|E|}\) by
\[
(\mathcal Ru)_e=n_e\cdot(u_w-u_v).
\]
In block form, row \(e\) is \(b_e^T\otimes n_e^T\). With \(K_\kappa=\operatorname{diag}(\kappa_e)\),
\[
\boxed{H_2(u,0)=\frac12u^TKu,\qquad
K=\mathcal R^TK_\kappa\mathcal R.}
\tag{4.1}
\]
Thus \(K\) is symmetric positive semidefinite, with its nullspace determined by rigid motions and any additional mechanisms of the chosen embedding. It is not legitimate to assume that translations are its only zero modes.

Expanding (3.3) to first order in \(u\) yields
\[
\Pi_{ij}(u)=c_{ij}^Tu+O(|u|^2),
\]
where
\[
\boxed{
c_{ij}=
-\sum_{e\in E}
\kappa_e\ell_e(n_e^TS^{ij}n_e)
\,(b_e\otimes n_e).
}
\tag{4.2}
\]
This is the leading harmonic microscopic stress. The exact nonlinear stress remains (3.3). The next term is quadratic and determines the strain derivative of the displacement Hessian.

### 4.1 The strain-Hessian derivative \(A^{ij}\), derived rather than fitted

For one edge at finite affine strain, put \(r_e^\xi=(I+\varepsilon(\xi))r_e\), \(\ell_e^\xi=|r_e^\xi|\), \(n_e^\xi=r_e^\xi/\ell_e^\xi\). The exact Hessian with respect to non-affine displacement at \(u=0\) is
\[
K_e(\xi)=\kappa_e\,b_eb_e^T\otimes
\left[
n_e^\xi(n_e^\xi)^T+
\frac{\ell_e^\xi-\ell_e}{\ell_e^\xi}
\left(I-n_e^\xi(n_e^\xi)^T\right)
\right].
\]
The second term is the geometric-stiffness contribution from the affine prestress; omitting it would give an incorrect strain derivative. At \(\xi=0\), it vanishes and (4.1) is recovered.

For the independent strain coordinate \(\xi_{ij}\), define
\[
q_e^{ij}=n_e^TS^{ij}n_e,\qquad
m_e^{ij}=(I-n_en_e^T)S^{ij}n_e.
\]
Differentiating the full Hessian gives the explicit matrix
\[
\boxed{
A^{ij}:=\left.\frac{\partial K(\xi)}{\partial\xi_{ij}}\right|_0
=\sum_{e\in E}\kappa_e\,b_eb_e^T\otimes
\left[
m_e^{ij}n_e^T+n_e(m_e^{ij})^T
+q_e^{ij}(I-n_en_e^T)
\right].
}
\tag{4.3}
\]
Thus \(A^{ij}\) is determined by the same embedding and spring constants as \(K\); it is not an independent fit.

The exact stress expansion is consequently
\[
\boxed{
\Pi_{ij}(u)=c_{ij}^Tu-\frac12u^TA^{ij}u+O(\|u\|^3),
}
\tag{4.4}
\]
with \(c_{ij}\) from (4.2). The linear term is the leading stress of a stress-free network; the quadratic term is precisely the strain derivative of the displacement Hessian. This reconciles the virial derivation with the quadratic Hessian-Wick calculation, while showing why the latter alone omits the leading term.

**Key correction to the generic quadratic ansatz.** For a stress-free central-force network, the full microscopic stress is not just \(-\tfrac12u^TA^{ij}u\): it has the linear term \(c_{ij}^Tu\) as well. The generic quadratic-Wick calculation in the companion Q6/Jitterbug bridge is a valid separate model-conditional identity; for this central-force energy, the quadratic part is now explicitly derived as (4.3)–(4.4).


## 5. Exact finite OU benchmark built from this Hessian

Let \(\mathcal H=(\ker K)^\perp=\operatorname{Ran}K\), and let \(K_{\mathcal H}\) be the strictly positive restriction. This removes every zero mode, not just the constant vertex mode. For scalar mobility \(\mu>0\), define the equilibrium overdamped process on \(\mathcal H\):
\[
du_t=-\mu K_{\mathcal H}u_t\,dt+
\sqrt{2\mu k_BT}\,dW_t^{\mathcal H}.
\tag{5.1}
\]
Its invariant covariance is \(k_BT K_{\mathcal H}^{-1}\). For the leading harmonic stress \(\Pi_{ij}^{(1)}=c_{ij}^Tu\),
\[
C_{ij,kl}^{(1)}(t)
=k_BT\,c_{ij}^T e^{-\mu K_{\mathcal H}t}
K_{\mathcal H}^{-1}c_{kl}.
\]
Therefore
\[
\boxed{
\int_0^\infty C_{ij,kl}^{(1)}(t)\,dt
=\frac{k_BT}{\mu}
c_{ij}^T K_{\mathcal H}^{-2}c_{kl}.
}
\tag{5.2}
\]
For the stress retained through quadratic order in (4.4), center the quadratic observable:
\[
\delta\Pi_{ij}^{(2)}
=-\frac12\left(u^TA^{ij}u-k_BT\operatorname{Tr}(A^{ij}K_{\mathcal H}^{-1})\right).
\]
The linear–quadratic cross-correlations vanish because the stationary process is centered Gaussian. Thus
\[
C_{ij,kl}^{(2)}(t)
=\frac{(k_BT)^2}{2}
\operatorname{Tr}\!\left(
A^{ij}e^{-\mu K_{\mathcal H}t}K_{\mathcal H}^{-1}
A^{kl}K_{\mathcal H}^{-1}e^{-\mu K_{\mathcal H}t}
\right).
\]
If \(K_{\mathcal H}\phi_\alpha=\lambda_\alpha\phi_\alpha\), then
\[
\boxed{
\int_0^\infty C_{ij,kl}^{(2)}(t)\,dt
=\frac{(k_BT)^2}{2\mu}
\sum_{\alpha,\beta}
\frac{A^{ij}_{\alpha\beta}A^{kl}_{\alpha\beta}}
{\lambda_\alpha\lambda_\beta(\lambda_\alpha+\lambda_\beta)}.
}
\tag{5.3}
\]
For the stress truncated at quadratic order, the Green–Kubo tensor is therefore
\[
\boxed{
\eta_{ij,kl}^{\rm OU,(2)}
=\frac{1}{\mu V}c_{ij}^TK_{\mathcal H}^{-2}c_{kl}
+\frac{k_BT}{2\mu V}
\sum_{\alpha,\beta}
\frac{A^{ij}_{\alpha\beta}A^{kl}_{\alpha\beta}}
{\lambda_\alpha\lambda_\beta(\lambda_\alpha+\lambda_\beta)}.
}
\tag{5.4}
\]
For an autocorrelation, the quadratic contribution is nonnegative. Formula (5.4) is exact for the quadratic-truncated stress under the declared finite OU process; the cubic and higher terms of the exact virial stress (3.3) are not included. It is not yet the viscosity of a real Q6 material: the embedding, spring constants, mobility, volume, equilibrium regime, and physical dynamics must be justified. Inertial, anharmonic, or phason-flip dynamics changes the correlation function and generally changes these expressions.

## 6. What the abstract six-cube itself predicts—and does not

The canonical abstract embedding \(y(x)=a x\) of \(x\in\{0,1\}^6\) in \(\mathbb R^6\), with uniform \(\kappa_e=\kappa\), is an exact combinatorial/elastic toy model. Every edge in coordinate direction \(k\) has \(n_e=e_k\), \(\ell_e=a\). Formula (4.2) then gives:
- for diagonal strain \(i=i\), \(c_{ii}=-\kappa a\sum_{e\parallel e_i}(b_e\otimes e_i)\);
- for off-diagonal shear \(i\ne j\), \(c_{ij}=0\).

The vanishing off-diagonal shear stress is a consequence of the axis-aligned six-dimensional embedding, not a physical prediction for a three-dimensional Jitterbug. The model is highly anisotropic and may have internal mechanisms. It is useful as a unit test and a no-hidden-isotropy control only.

## 7. The missing Q6–Jitterbug geometric input

The \(8{:}1\) quotient in the companion note labels each Q6 state by one of eight Jitterbug panels and collapses a three-bit fibre. It does not specify the 3D positions of the eight states in each fibre. Therefore it does not yet provide the map
\[
y:V(Q_6)\to\mathbb R^3
\]
needed to evaluate \(r_e,\ell_e,n_e\), the rigidity matrix, and the stress tensor in physical three-space.

The required next geometric object is a fibre lift
\[
y(a,b;t)=c_a(t)+R_a(t)\,\rho_{a,b}(t),
\]
where \(a\in\mathbb F_2^3\) labels the Kabsch-fitted panel frame and \(b\in\mathbb F_2^3\) labels the fibre. The internal coordinates \(\rho_{a,b}(t)\) must be derived—not guessed—and must satisfy:
1. panel-local constraints and the eight rigid panel frames;
2. compatibility across all 12 panel contacts;
3. an explicit treatment of the three fibre edge directions;
4. the full Gray/Jitterbug branch and its phase convention;
5. higher-cell incidence if the map is to extend beyond the graph 1-skeleton.

Only after this lift is available can the six-dimensional toy energy be replaced by a physically three-dimensional Q6/Jitterbug energy. The Jitterbug coil/flux calculation supplies frame-dependent electromagnetic observables, not the missing internal coordinates or mechanical spring constants.

## 8. Relation to T130, T131 and the Stokes target

- T130's local least-squares gradients and positive resistance assembly can be used to construct discrete strain/gradient operators after the embedding and local geometric moments are supplied. Its resistance matrix is not automatically the central-force Hessian \(K\); the two must be related by a derived constitutive model.
- T131 requires the Hessian and mass/dynamics from the same potential, and total stress including phonon, phason and interaction cross-correlations. Formulae (3.3)–(5.3) provide a concrete phonon-network starting point. A phason field \(w\) must be added to the same energy \(H(u,w,\varepsilon)\), with its own conjugate phason stress; it cannot be folded into \(u\) by relabelling.
- A Stokes coefficient follows only if a sequence of these models has a controlled continuum/hydrodynamic limit, its Green–Kubo tensor converges, and the limit is local, isotropic and Newtonian. If not, the limit is a tensorial/nonlocal/frequency-dependent constitutive law. The conditional theorem in the companion note remains conditional; this energy construction alone does not verify its hypotheses.

## 9. Acceptance tests

For any supplied embedding and \(\kappa_e>0\):
1. \(K=\mathcal R^TK_\kappa\mathcal R\) is symmetric PSD to numerical tolerance.
2. The exact stress (3.3) agrees with a centred finite difference of \(H(u,\varepsilon)\).
3. The derivative of the energy at \(u=0,\varepsilon=0\) vanishes (stress-free reference).
4. The harmonic stress coefficient (4.2) agrees with a finite-difference derivative of (3.3) at \(u=0\).
5. The OU covariance on \(\mathcal H\) is \(k_BT K_{\mathcal H}^{-1}\); the integrated correlation agrees with (5.2).
6. For the canonical \(\mathbb R^6\) embedding, off-diagonal \(c_{ij}\) vanish; this must not be interpreted as 3D isotropy.

## 10. Classification

| Statement | Status |
|---|---|
| Exact central-force energy (3.1) for supplied embedded Q6 graph | [P] definition/model |
| Stress formula (3.3) by strain differentiation | [P] exact |
| Rigidity Hessian (4.1) and harmonic stress (4.2) | [P] exact expansions |
| OU Green–Kubo formula (5.2)–(5.3) | [P] exact for declared finite overdamped model |
| Canonical \(Q_6\hookrightarrow\mathbb R^6\) anisotropy control | [P] exact |
| Physical \(Q_6\to\mathbb R^3\) fibre lift from Jitterbug | [O] |
| Calibrated \(\kappa_e\), masses, mobility and phason energy | [O] |
| Isotropic Newtonian hydrodynamic limit and \(\eta_{\rm GK}=\eta_{\rm Stokes}\) | [O] |

No new theorem number is assigned. This note supplies the missing variational energy model while preserving the distinction between an exact finite graph model and a physical material.



## 9. Operator-level relation to the golden overlap automaton

The golden Q6 pair automaton now has an explicit substochastic transfer operator and a separate stress-insertion construction; see [From the Q6 pair-overlap automaton to a stress operator](Q6_PAIR_AUTOMATON_TO_STRESS_OPERATOR_2026-11-24.md). The symbolic state coding does not supply the spatial embedding or the central-force stress coefficients in §§2–4. In particular, a two-replica overlap-weighted stress statistic is not the temporal autocorrelation of this mechanical stress. The missing map from the pair-transfer space to the physical mechanical Hilbert space remains an open theorem target.


## 11. Exact canonical Q6-in-\(\mathbb R^6\) shear benchmark

The abstract cube admits a canonical unit-edge embedding
\[
y(x)=x,\qquad x\in\{0,1\}^6,
\]
with unit spring constants. This is an exact **six-dimensional control model**, not a three-dimensional Jitterbug realization. It is useful because its central-force Hessian and shear-stress derivative can be evaluated without fitting geometric parameters.

For coordinate direction \(k\), let \(L_k\) be the Laplacian of the perfect matching consisting of the 32 Q6 edges parallel to that coordinate. The rigidity Hessian decomposes by displacement component:
\[
K=\operatorname{diag}(L_1,L_2,\ldots,L_6).
\]
Each \(L_k\) has eigenvalues 0 and 2, each with multiplicity 32. Hence
\[
\operatorname{rank}K=6\cdot32=192,
\qquad
\operatorname{nullity}K=384-192=192,
\]
and every positive eigenvalue of \(K_{\mathcal H}\) equals 2. The large nullspace is a real mechanism of this deliberately sparse toy embedding; it must not be silently replaced by a rigid-body-only nullspace.

For an independent off-diagonal strain coordinate \(\xi_{ij}\), \(i<j\), use
\[
S^{ij}=\frac12(e_ie_j^T+e_je_i^T).
\]
The linear stress coefficient (4.2) vanishes because every reference bond is parallel to a coordinate axis:
\[
c_{ij}=0.
\]
The strain-Hessian derivative is instead
\[
A^{ij}=(L_i+L_j)\otimes S^{ij}.
\]
In the common Walsh-character basis, its restriction to \(\mathcal H=\operatorname{Ran}K\) has 16 independent two-dimensional blocks
\[
\begin{pmatrix}0&2\\2&0\end{pmatrix},
\]
and is zero on the remaining directions. Therefore, exactly,
\[
\|A^{ij}_{\mathcal H}\|_F^2=128,
\qquad
\sum_{\alpha,\beta}
\frac{|A^{ij}_{\alpha\beta}|^2}
{\lambda_\alpha\lambda_\beta(\lambda_\alpha+\lambda_\beta)}
=\frac{128}{2\cdot2\cdot4}=8.
\]
For the reversible overdamped OU process on \(\mathcal H\), with mobility \(\mu\), temperature \(T\), and the stress retained through quadratic order, this gives
\[
C_{ij,ij}(t)=16(k_BT)^2e^{-4\mu t},
\qquad
\int_0^\infty C_{ij,ij}(t)\,dt
=4\frac{(k_BT)^2}{\mu},
\]
and
\[
\boxed{\eta^{ij,ij}_{\rm OU}=4\frac{k_BT}{\mu V}.}
\]
All 15 off-diagonal components of the six-dimensional cube control give the same value by coordinate-permutation symmetry. This is a finite exact benchmark for the declared quadratic-stress OU model, not a physical viscosity prediction: the embedding is six-dimensional, the energy is harmonicized, and the OU bath is imposed.

The reproducible implementation is audits/q6_central_force_ou_green_kubo.py. It checks the Hessian rank/eigenvalues, the vanishing linear shear coefficient, the Frobenius norm and the Green–Kubo spectral sum for all 15 shear components.

### 11.1 Reproducibility result

The implementation was executed in GitHub Actions with NumPy on Python 3.12. The combined audit run completed successfully:
[Q6 pair-transfer and central-force OU audit](https://github.com/fabianleonaressi95/theorem/actions/runs/45397243586).

For every one of the 15 off-diagonal strain components, the program returned
\[
\|c_{ij}\|=0,\qquad
\|A^{ij}_{\mathcal H}\|_F^2=128,\qquad
\sum_{\alpha,\beta}\frac{|A^{ij}_{\alpha\beta}|^2}
{\lambda_\alpha\lambda_\beta(\lambda_\alpha+\lambda_\beta)}=8.
\]
It also verified numerically that \(K\) has rank 192, nullity 192, and positive spectrum consisting only of 2 (within the stated numerical tolerance). The computed OU Green–Kubo coefficient is therefore the exact value predicted by the character-space derivation:
\[
\eta^{ij,ij}_{\rm OU}=4\,k_BT/(\mu V).
\]
This is a successful numerical reproduction of the finite toy-model identity. It does not upgrade the six-dimensional model to a three-dimensional material model or establish a hydrodynamic limit.


### 11.2 Spectral conclusion: one relaxation atom, not a golden hierarchy

For this canonical model the stress correlation is a single exponential:
\[
C_{ij,ij}(t)=16(k_BT)^2e^{-4\mu t}.
\]
Thus its stress spectral measure is exactly
\[
d\mu_{\Pi_{ij}}(\gamma)=16(k_BT)^2\,\delta_{4\mu}(d\gamma).
\]
There is one relaxation rate, \(4\mu\), in this harmonicized six-dimensional control. No \(\varphi\)-spaced hierarchy follows from the bare canonical Q6 central-force Hessian and scalar-mobility OU bath. A golden hierarchy would have to arise from additional derived structure—e.g. a nontrivial fibre lift, multiple physical internal sectors, scale-dependent mobility, or anharmonic/activated kinetics—and must be measured or proved from that enlarged model. It must not be inserted by relabelling the single atom.
