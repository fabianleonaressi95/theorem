# Q6 hypercube law, Green–Kubo transport, and six-dimensional anomaly descent

**Document type:** synthesis and correction note  
**Status:** exact finite-complex identities and standard continuum formulas are separated from numerical model evidence and open bridges.  
**Dependencies:** Q6 cell complex; T017/T019/T020 and M1; six-dimensional Dirac/index theory.  
**Scope warning:** this note does not claim that the finite graph Q6 by itself defines a smooth spin manifold, a chiral index, an interacting Yang–Mills measure, or a Green–Schwarz-cancelled quantum theory.

## 1. The already established Q6 hypercube law

Let \(Q_6\) be the six-dimensional cube graph, regarded as the one-skeleton of the cubical cell complex of the 6-cube. Its cell counts are
\[
(N_0,N_1,N_2)=(64,192,240).
\]
For the plaquette variables \(\Omega_p\), \(p=1,\ldots,240\), in the original scalar/commuting-flux construction, define
\[
\mathcal F_{Q_6}=\sum_{p=1}^{240}(1-\cos\Omega_p).
\]
The previously derived fourth-moment relation is
\[
\boxed{\Delta\mu_4
=8w^4\sum_{p=1}^{240}(\cos\Omega_p-1)
=-8w^4\mathcal F_{Q_6}.}
\]
In particular, at \(w=2\),
\[
\boxed{\mathcal F_{Q_6}=-\frac{\Delta\mu_4}{128}.}
\]
For small flux,
\[
\mathcal F_{Q_6}
=\frac12\sum_p\Omega_p^2
-\frac1{24}\sum_p\Omega_p^4
+O(\|\Omega\|^6).
\]
The closure condition in the cubical chain complex is
\[
B_3^T\Omega=0,\qquad
P_{\rm cl}=I-B_3(B_3^TB_3)^+B_3^T.
\]
For the previously audited Q6 complex, the closed plaquette sector has dimension 129. These are statements about the stated finite combinatorial model and its original flux conventions.

**Non-Abelian qualification.** For general \(SU(3)\) links, a plaquette is a matrix holonomy
\[
U_p=U_{e_1}^{\epsilon_1}U_{e_2}^{\epsilon_2}
U_{e_3}^{\epsilon_3}U_{e_4}^{\epsilon_4}\in SU(3),
\]
with each edge orientation handled by \(U_e^{-1}=U_e^\dagger\). There is generally no globally defined scalar angle \(\Omega_p\) for which \(U_p\) can be replaced by \(\cos\Omega_p\). A gauge-invariant non-Abelian action may instead use
\[
S_{\rm W}[U]=\sum_p\left(1-\frac1{3}\operatorname{ReTr}U_p\right),
\]
with normalization chosen explicitly. The scalar hypercube law above is not silently promoted to this matrix-valued action; a bridge requires a specified abelianization, representation character, or controlled small-curvature expansion.

## 2. Green–Kubo: the independent dynamical branch

For an equilibrium system with extensive shear-stress observable \(\Pi_{xy}\), the Green–Kubo relation is
\[
\boxed{\eta=\frac1{k_BT\,V}
\int_0^\infty
\langle\delta\Pi_{xy}(t)\delta\Pi_{xy}(0)\rangle_{\rm eq}\,dt.}
\]
Here \(\delta\Pi_{xy}=\Pi_{xy}-\langle\Pi_{xy}\rangle\). If the stress observable is defined as an intensive density rather than an extensive total, the volume factor must be changed accordingly. In the retarded-correlator convention commonly used in field theory,
\[
\eta=-\lim_{\omega\to0^+}
\frac{\operatorname{Im}G^R_{\Pi_{xy}\Pi_{xy}}(\omega,\mathbf0)}{\omega},
\]
subject to the chosen Fourier and retarded-correlator sign convention.

For the Q6 transport construction, an oriented edge current is antisymmetric,
\[
j_{gh}=-j_{hg},\qquad
\dot\rho_g+\sum_{h\sim g}j_{gh}=0.
\]
A directional current can be defined by
\[
I_a=\sum_{(g,h)}\xi_a(g,h)j_{gh},
\]
where the edge orientation and geometric displacement factor \(\xi_a\) are fixed once and for all. The transport matrix is
\[
K_{ab}=\frac1{k_BT\,V}
\int_0^\infty\langle I_a(t)I_b(0)\rangle_{\rm eq}\,dt.
\]
If the dynamics and measure preserve the full cubic symmetry, then the rank-two tensor must obey
\[
K_{ab}=\kappa\,\delta_{ab}.
\]
This symmetry conclusion does not determine \(\kappa\); it follows only after the observable and equilibrium dynamics are specified.

For a finite-dimensional stationary Ornstein–Uhlenbeck surrogate with a stable drift matrix \(A\), the integrated covariance can be evaluated by a Lyapunov/resolvent calculation. In a scalar exponential example
\[
C(t)=G_0e^{-2\kappa_0t},
\qquad
\int_0^\infty C(t)\,dt=\frac{G_0}{2\kappa_0}.
\]
The previously recorded raw OU integral \(1.4149596639051703\) and the associated \(\psi=1.4655712318767682\) belong to that specific surrogate calculation. They are not a measured physical viscosity and are not a Yang–Mills simulation. A separate dimensionless spectral OU audit recorded \(\eta_{\rm GK}^{\rm dimless}=777.5298786\), with \(\lambda_{\min}(A_+)=0.0106227783\); this is a different normalization/model observable and must not be merged numerically with the raw integral above.

**The hypercube-to-transport bridge remains open.** To derive a Green–Kubo coefficient from the plaquette functional one must specify a stochastic or Hamiltonian dynamics, invariant measure, stress/current observable, volume convention, and a limiting procedure. The static identity for \(\Delta\mu_4\) does not by itself supply time correlations.

## 3. Six-dimensional chiral anomalies: the correct degree bookkeeping

For a six-dimensional chiral theory, the perturbative anomaly polynomial is an invariant closed 8-form. For a complex Weyl fermion coupled to a bundle \(V\) over a Spin six-manifold,
\[
\boxed{I_8=\left[\widehat A(TM)\operatorname{ch}(V)\right]_8.}
\]
Using the standard normalization of Pontryagin and Chern classes,
\[
\widehat A(TM)
=1-\frac{p_1}{24}
+\frac{7p_1^2-4p_2}{5760}+\cdots,
\]
so
\[
\boxed{
I_8=\operatorname{ch}_4(V)
-\frac{p_1(TM)}{24}\operatorname{ch}_2(V)
+\operatorname{rank}(V)\frac{7p_1(TM)^2-4p_2(TM)}{5760}.
}
\]
Only terms of total differential degree eight are retained. For an \(SU(N)\) bundle, \(c_1(V)=0\), hence
\[
\operatorname{ch}_2(V)=-c_2(V),\qquad
I_{8,\rm mixed}=+\frac1{24}p_1(TM)c_2(V).
\]
The pure gauge contribution is \(\operatorname{ch}_4(V)\), not universally just a bare trace without specifying representation and normalization. For \(c_1=0\),
\[
\operatorname{ch}_4(V)=\frac1{12}c_2(V)^2-\frac16c_4(V).
\]
For a Spin\(^c\) manifold, the index density instead contains the factor \(e^{c_1(L)/2}\):
\[
I_8=\left[\widehat A(TM)e^{c_1(L)/2}\operatorname{ch}(V)\right]_8.
\]
A six-dimensional index formula \([\widehat A\,\operatorname{ch}]_6\) and the eight-form anomaly polynomial \([\widehat A\,\operatorname{ch}]_8\) are related but are not interchangeable: the latter controls the local anomaly in six spacetime dimensions.

## 4. Stora–Zumino descent: corrected chain

Let \(A\) be a Lie-algebra-valued connection, \(F=dA+A^2\), and \(c\) the ghost. One consistent BRST convention is
\[
sA=-Dc,\qquad sc=-c^2,\qquad D=d+[A,\cdot],
\]
with \(s^2=0\) and \(sd+ds=0\). The extended or polyform formalism packages the descent; it must be used with a consistent total-degree and sign convention. In particular, the naive expression
\[
\mathcal F=F+dc+[A,c]+c^2
\]
is not the correct curvature superfield in the usual horizontality convention. With \(\widehat A=A+c\) and \(\widehat d=d+s\), the Russian formula/horizontality condition is
\[
\widehat F=\widehat d\,\widehat A+\widehat A^2=F.
\]
Expanding the Chern–Simons polyform by ghost number gives the descent tower.

For \(I_8=dI_7^{(0)}\), the first equations are
\[
\boxed{
\begin{aligned}
dI_7^{(0)}&=I_8,\\
sI_7^{(0)}+dI_6^{(1)}&=0,\\
sI_6^{(1)}+dI_5^{(2)}&=0,\\
sI_5^{(2)}+dI_4^{(3)}&=0.
\end{aligned}}
\]
The superscript is ghost number and the subscript is form degree. The consistent six-dimensional anomaly is represented by
\[
\boxed{\mathcal A_{\rm cons}\ \propto\ \int_{M^6}I_6^{(1)}.}
\]
It is not \(\int sI_7^{(0)}\), and the fact that \(dI_6^{(1)}\) appears in the second equation does not imply that the integrated anomaly vanishes. The descent ensures the Wess–Zumino consistency condition \(s\mathcal A_{\rm cons}=0\) modulo spacetime-exact terms.

For a pure gauge invariant polynomial \(P_8(F)=C\,\operatorname{Tr}_V(F^4)\), the transgression is
\[
I_7^{(0)}
=4C\int_0^1dt\,
\operatorname{Tr}_V\!\left[
A\,(t\,dA+t^2A^2)^3
\right],
\]
where \(C\) includes the chosen Chern-character normalization. The factor 4 is required by transgression of a degree-four invariant polynomial. In six dimensions the consistent descendant has the structural form
\[
I_6^{(1)}\propto
\operatorname{Tr}_V\!\left[
c\,d\left(A\,dA+\frac12A^3\right)
\right],
\]
with the overall coefficient fixed by \(P_8\), the representation, chirality, and generator convention. Coefficients such as \(1/(24\pi^3)\) cannot be transplanted between conventions without this normalization audit.

## 5. Bardeen–Zumino distinction

The consistent anomaly is obtained from the descent and obeys Wess–Zumino consistency. The covariant anomaly transforms covariantly but, in general, is not the variation of an effective action and does not itself obey the consistent Wess–Zumino condition. The Bardeen–Zumino construction relates the consistent and covariant currents by adding a local Bardeen–Zumino current. It is therefore misleading to state universally that one obtains the covariant anomaly by adding \(sP_5(A,c)\) directly to the consistent anomaly. In six dimensions the covariant pure-gauge structure is proportional to \(\operatorname{Tr}_V(cF^3)\), with coefficient fixed independently by the same trace and chirality conventions.

## 6. Mixed gauge–gravitational descent

The mixed part for an \(SU(N)\) bundle is
\[
I_{8,\rm mixed}=\frac1{24}p_1(TM)c_2(V).
\]
Write the characteristic factors locally as
\[
p_1(TM)=dQ_3^{\rm L}(\omega),\qquad
c_2(V)=dQ_3^{\rm G}(A),
\]
and their BRST descents as
\[
sQ_3^{\rm L}+dQ_2^{(1),\rm L}=0,\qquad
sQ_3^{\rm G}+dQ_2^{(1),\rm G}=0.
\]
Then, up to the common sign convention for the descent and the normalization of the characteristic forms, the mixed six-form descendant is the product-rule combination
\[
I_{6,\rm mixed}^{(1)}
=\frac1{24}\left[
Q_2^{(1),\rm L}c_2(V)
+p_1(TM)Q_2^{(1),\rm G}
\right].
\]
Both summands have form degree six and ghost number one. A proposed term containing a two-form Lorentz ghost times a four-form gravitational derivative times a four-form gauge density has degree eight and cannot itself be integrated as a six-dimensional anomaly. Gauge and local-Lorentz ghosts must be descended in their respective factors.

## 7. Green–Schwarz factorization and six-dimensional supergravity

For a theory with tensor fields \(B^\alpha_2\), the reducible anomaly polynomial must factorize in the tensor charge pairing:
\[
\boxed{
I_8=\frac12\Omega_{\alpha\beta}X_4^\alpha X_4^\beta,
\qquad
X_4^\alpha=a^\alpha p_1(TM)+\sum_i b_i^\alpha\,\operatorname{tr}(F_i^2)+\cdots.
}
\]
This is generally a bilinear factorization, not necessarily the square of one scalar four-form. The tensor field strengths obey a modified Bianchi identity
\[
H^\alpha=dB^\alpha+\omega_3^\alpha,\qquad
d\omega_3^\alpha=X_4^\alpha.
\]
Their gauge/Lorentz transformation includes the compensating descent term
\[
\delta B^\alpha=-\omega_2^{(1),\alpha}+d\Lambda_1^\alpha
\]
in the convention \(H^\alpha=dB^\alpha+\omega_3^\alpha\). The six-dimensional coupling has the degree-correct form
\[
S_{\rm GS}\propto
\frac12\int_{M^6}\Omega_{\alpha\beta}B^\alpha_2\wedge X_4^\beta.
\]
Its variation cancels the reducible one-loop anomaly when the factorization and charge quantization conditions are satisfied. Irreducible pieces must vanish separately.

For \(6D\), \(\mathcal N=(1,0)\) supergravity, the irreducible gravitational constraint is
\[
n_H-n_V+29n_T=273,
\]
with the standard multiplet-counting conventions. It is necessary but not sufficient: gauge and mixed anomaly factorization constraints remain.

## 8. The intended bridge and its status

The intended chain is
\[
\text{Q6 cubical cells and link holonomies}
\longrightarrow
\text{discrete curvature}
\longrightarrow
\text{continuum characteristic forms}
\longrightarrow
I_8
\longrightarrow
I_6^{(1)}
\longrightarrow
\text{Green--Schwarz cancellation}.
\]
The parallel dynamical branch is
\[
\mathcal F_{Q_6}\ \text{or a specified stress functional}
\longrightarrow \Pi_{xy}(t)
\longrightarrow \langle\delta\Pi_{xy}(t)\delta\Pi_{xy}(0)\rangle
\longrightarrow \eta.
\]
The two branches may share the gauge-link and geometric data, but Green–Kubo is a dynamical response formula and Stora–Zumino is a local cohomological descent. Neither implies the other.

### Status ledger

| Claim | Status |
|---|---|
| Q6 counts \(64,192,240\) | Exact combinatorics |
| Scalar-flux fourth-moment law \(\Delta\mu_4=-8w^4\mathcal F_{Q6}\) | Exact in the original scalar/commuting-flux construction |
| \(B_3^T\Omega=0\), closed-sector dimension 129 | Finite-complex result in the stated Q6 model |
| Green–Kubo relation | Standard linear-response formula |
| OU integrals quoted in §2 | Numerical/model-specific surrogate evidence, not physical viscosity |
| Six-dimensional \(I_8=[\widehat A\,\mathrm{ch}(V)]_8\) | Standard index/anomaly polynomial |
| Stora–Zumino descent | Standard cohomological framework; coefficients require convention fixing |
| Green–Schwarz factorization | Standard cancellation mechanism conditional on factorization/quantization |
| Q6 link data converge to the characteristic classes in \(I_8\) | OPEN |
| Q6 construction yields a chiral index/anomaly with controlled continuum limit | OPEN |
| Q6-derived dynamics yields a physical Green–Kubo transport coefficient | OPEN |
| Q6 anomaly polynomial factorizes with a valid tensor charge lattice | OPEN |

## 9. Relation to the Q6 Wilson refinement

T017 defines the periodic refinement \((C_{2n})^{\square6}\); it is not the finite 64-vertex graph \(Q_6\). T019 establishes the free generalized strong-resolvent result. T020 records the gauge-covariant Wilson operator with its stated consistency condition and finite-dimensional covariance/plaquette audits. M1 treats prescribed continuous/Hölder \(SU(3)\) backgrounds under its own assumptions. These results concern convergence of operators on a six-dimensional torus. They do not by themselves establish convergence of heat-kernel supertraces, spectral flow, Fredholm indices, determinant-line bundles, or anomaly polynomials. Those are separate analytical/topological tasks.

The next mathematical bridge must therefore define a compatible discrete spin/chirality structure and prove convergence of an index-sensitive quantity (for example a suitably normalized heat-kernel supertrace), while independently proving that the lattice characteristic representatives converge to the continuum Chern–Weil forms. No claim of an automatic discrete Atiyah–Singer theorem is made here.

## 10. References for the standard continuum framework

- Reinhold A. Bertlmann, *Anomalies in Quantum Field Theory*, chapter 9, “Stora–Zumino chain of descent equations,” Oxford University Press (2000), DOI: 10.1093/acprof:oso/9780198507628.003.0009.
- H. Fukaya, “Six-dimensional regularization of chiral gauge theories,” PoS (2016), which displays the six-dimensional consistent descent and its Chern–Simons representative.
- “Anomaly polynomial of general 6D SCFTs,” *Progress of Theoretical and Experimental Physics* (2014), for six-dimensional Green–Schwarz contributions and tensor-branch factorization.
