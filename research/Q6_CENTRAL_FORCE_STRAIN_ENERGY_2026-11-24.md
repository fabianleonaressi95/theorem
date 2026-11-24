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
This is the leading harmonic microscopic stress. The exact nonlinear stress remains (3.3); the quadratic and higher displacement corrections must be retained if the harmonic approximation is not controlled.

**Key correction to the generic quadratic ansatz.** For a stress-free central-force network, the leading harmonic stress is linear in displacement, not automatically \(-\tfrac12u^TA^{ij}u\). A quadratic stress arises in other models or at higher order. The generic quadratic-Wick calculation in the Q6/Jitterbug bridge remains a valid separate model-conditional identity, but it must not be substituted for (3.3) without deriving that energy.

## 5. Exact finite OU benchmark built from this Hessian

Let \(\mathcal H=(\ker K)^\perp=\operatorname{Ran}K\), and let \(K_{\mathcal H}\) be the strictly positive restriction. This removes every zero mode, not just the constant vertex mode. For scalar mobility \(\mu>0\), define the equilibrium overdamped process on \(\mathcal H\):
\[
du_t=-\mu K_{\mathcal H}u_t\,dt+
\sqrt{2\mu k_BT}\,dW_t^{\mathcal H}.
\tag{5.1}
\]
Its invariant covariance is \(k_BT K_{\mathcal H}^{-1}\). For the leading harmonic stress \(\Pi_{ij}^{(1)}=c_{ij}^Tu\),
\[
C_{ij,kl}(t)
=k_BT\,c_{ij}^T e^{-\mu K_{\mathcal H}t}
K_{\mathcal H}^{-1}c_{kl}.
\]
Therefore
\[
\boxed{
\int_0^\infty C_{ij,kl}(t)\,dt
=\frac{k_BT}{\mu}
c_{ij}^T K_{\mathcal H}^{-2}c_{kl}.
}
\tag{5.2}
\]
The corresponding finite-model Green–Kubo tensor is
\[
\boxed{
\eta_{ij,kl}^{\rm OU}
=\frac{1}{\mu V}
c_{ij}^T K_{\mathcal H}^{-2}c_{kl}.
}
\tag{5.3}
\]
This is exact for the declared overdamped harmonic network. It is not yet the viscosity of a real Q6 material: the embedding, spring constants, mobility, volume, equilibrium regime, and physical dynamics must be justified. Inertial, anharmonic, or phason-flip dynamics changes the correlation function and generally changes (5.3).

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
