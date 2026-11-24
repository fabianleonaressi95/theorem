# From the Q6 pair-overlap automaton to a stress operator: exact transfer and missing intertwiner

**Date:** 2026-11-24  
**Status:** [P] exact transfer-operator construction from the existing finite automaton; [P] exact distinction between pair-overlap statistics and one-trajectory stress correlations; [C] stress-weighted overlap observable; [O] conservative physical dynamics, stress map, and spectral intertwining.

**Purpose.** This note makes the proposed bridge operator-level. It does not claim that the geometric overlap automaton already is a physical relaxation process. It identifies the exact operator that the automaton does define, the exact statistic it computes, and the additional mathematical structure required before Green–Kubo can follow.

## 1. Input: the already-defined Q6 pair automaton

Let \(G=Q_6\), with 64 vertices and six neighbours at every vertex. Let
\[
s:V(G)\to\mathbb Z[\lambda],\qquad
\lambda=\varphi^{-1},\qquad r=\lambda^6=5-8\lambda,
\]
be the existing golden scalar coding. The pair automaton has states
\[
\mathcal S=\{(p,q,\delta):p,q\in V(G),\ \delta\in\mathbb Z[\lambda]\}
\]
restricted to the finite reachable enclosure already certified by
\`audits/tsmr_c_iching_overlap_automaton.py\`. We write \(\delta=a+b\lambda\).

For neighbours \(j\sim p\), \(k\sim q\), the update is
\[
(p,q,\delta)\longmapsto
\left(j,k,\frac{\delta+s(j)-s(k)}{r}\right).
\tag{1.1}
\]
There are exactly \(6\cdot6=36\) candidate paired moves before the real/conjugate enclosure filters them.

The existing finite certificate reports 5,566 reachable states and 34,762 retained directed transitions. Those counts are inherited inputs; this note does not redo the close-pair coverage or dimension proof.

## 2. Exact transfer operator

Let \(A=(A_{xy})_{x,y\in\mathcal S}\) be the integer adjacency matrix, where \(A_{xy}\) counts the number of paired choices from \(x\) to \(y\). Define
\[
\boxed{\quad T_{\rm pair}=\frac1{36}A.\quad}
\tag{2.1}
\]
For a function \(f:\mathcal S\to\mathbb R\),
\[
(T_{\rm pair}f)(x)
=\frac1{36}\sum_{y\in\mathcal S}A_{xy}f(y).
\tag{2.2}
\]
Because at most 36 paired choices are retained in each row,
\[
T_{\rm pair}\mathbf1\leq\mathbf1.
\tag{2.3}
\]
Thus \(T_{\rm pair}\) is a **substochastic transfer operator**. The missing row mass is the probability of a paired move leaving the finite real/conjugate enclosure. It is not legitimate to renormalize each row: doing so would change the original independent Q6 walk and its path weights.

Let \(\rho_0\) be the initial row distribution
\[
\rho_0(p,q,0)=\frac1{64^2}=\frac1{4096},
\]
and zero on all other states. For a terminal test function \(\chi\),
\[
Z_n(\chi)=\rho_0T_{\rm pair}^{\,n}\chi.
\tag{2.4}
\]
For example, \(\chi_D(p,q,\delta)=\mathbf1_{\{|\delta|\leq D\}}\) is a close-pair terminal test at the chosen normalized scale. Equation (2.4) is the retained-path contribution. Its identification with the full close-pair probability requires the enclosure-coverage lemma for the particular terminal event; the finite-state construction alone does not supply that lemma.

The exact operator audit is implemented in
\`audits/tsmr_q6_stress_transfer_bridge.py\`. It reports row deficits, support reciprocity, and equality of forward/reverse transition multiplicities. It does not infer a physical stress or claim a relaxation spectrum.

## 3. Stress insertion: what can be computed without overclaiming

Suppose an independently specified mechanical model supplies a state-resolved stress observable
\[
\sigma_{xy}:V(Q_6)\to\mathbb R.
\]
Then the pair automaton admits the stress-weighted terminal insertion
\[
\chi_D^\sigma(p,q,\delta)
=\mathbf1_{\{|\delta|\leq D\}}\,
\sigma_{xy}(p)\sigma_{xy}(q),
\tag{3.1}
\]
and the corresponding quantity
\[
Z_n^\sigma(D)=
\rho_0T_{\rm pair}^{\,n}\chi_D^\sigma.
\tag{3.2}
\]
The same construction works for a more general pair observable
\(\Sigma_{xy}(p,q,\delta)\), provided it is derived from a specified energy/geometry rather than fitted to produce a desired exponent.

**Interpretation boundary.** Equations (3.1)–(3.2) define a two-replica, overlap-conditioned stress statistic. The two entries \(p,q\) label two independent Q6 walks. They are not the same physical trajectory at times \(0\) and \(t\). Therefore \(Z_n^\sigma(D)\) is not, by itself,
\[
C_{\Pi\Pi}(t)=
\langle\delta\Pi_{xy}(t)\delta\Pi_{xy}(0)\rangle_{\rm eq}.
\]
It can be a useful geometric diagnostic: it tests whether the golden overlap structure is correlated with a separately derived stress observable. A theorem relating it to temporal stress memory is an additional requirement, not a relabelling.

There is also a model-input gap. The central-force stress in
\`research/Q6_CENTRAL_FORCE_STRAIN_ENERGY_2026-11-24.md\` depends on an embedding \(y:V(Q_6)\to\mathbb R^d\), spring constants, and displacement variables. The golden scalar \(s(p)\) is not such an embedding and does not determine \(\sigma_{xy}(p)\). The missing three-dimensional Q6/Jitterbug fibre lift remains open.

## 4. The physical Green–Kubo operator is a different object

For a reversible equilibrium mechanical model, let \(\mathcal H_{\rm phys}\) be its equilibrium \(L^2\) space and let
\(\mathcal L_{\rm phys}\geq0\) be the nonnegative self-adjoint relaxation generator (the sign convention is chosen so the semigroup is \(e^{-t\mathcal L_{\rm phys}}\)). Let \(\Pi_{xy}\in\mathcal H_{\rm phys}\) be the centered, conserved-mode-projected total stress. Then
\[
C_{\Pi\Pi}(t)
=\langle\Pi_{xy},e^{-t\mathcal L_{\rm phys}}\Pi_{xy}\rangle,
\tag{4.1}
\]
and its spectral measure is
\[
\mu_\Pi(B)=
\langle\Pi_{xy},E_{\mathcal L_{\rm phys}}(B)\Pi_{xy}\rangle.
\tag{4.2}
\]
Consequently
\[
\eta_{\rm GK}
=\frac1{k_BT V}
\int_{(0,\infty)}\frac{d\mu_\Pi(\gamma)}{\gamma}
\tag{4.3}
\]
for total extensive stress, provided the zero mode has been removed and the inverse-rate moment is finite.

The operator in (4.1) evolves one physical system in time. The operator in (2.2) propagates two independent symbolic paths while discarding paths that leave a finite overlap enclosure. Their state spaces, conservation laws, and probabilistic meanings differ.

## 5. Exact criterion for a legitimate spectral bridge

A precise sufficient route would require a sequence of refinement levels \(h\downarrow0\), physical Hilbert spaces \(\mathcal H_h\), and maps
\[
J_h:\ell^2(\mathcal S_h,w_h)\longrightarrow\mathcal H_h
\]
with all of the following properties.

1. **A conservative closed symbolic dynamics.** The finite pair transfer must be replaced by a closed state-space dynamics, or its escape channels must be represented by genuine physical states. The killed finite enclosure cannot silently stand for a conservative equilibrium process.
2. **Reversible positive generator.** There must be a positive weight \(w_h\) for which the proposed symbolic relaxation operator is self-adjoint and nonnegative. A necessary finite-matrix test for the raw transfer is detailed balance,
   \[
   W_hT_h=T_h^TW_h,\qquad W_h=\operatorname{diag}(w_h)>0.
   \tag{5.1}
   \]
   If (5.1) fails, the raw transfer cannot be used as a reversible Green–Kubo generator. A symmetrization or lazy walk is a different model and requires an independent physical derivation.
3. **Stress map.** The physical stress must be the image of a specified symbolic observable \(a_h\):
   \[
   \Pi_{xy,h}=J_ha_h,
   \]
   with \(a_h\) obtained from the same strain-dependent energy as the mechanical Hessian and forces.
4. **Intertwining.** For a symbolic nonnegative generator \(G_h\), the map must satisfy
   \[
   \mathcal L_{{\rm phys},h}J_h=J_hG_h
   \tag{5.2}
   \]
   on a common invariant core, with compatible domains. An isometric \(J_h\) gives equality of the corresponding stress spectral measures:
   \[
   \langle\Pi_{xy,h},E_{\mathcal L_h}(B)\Pi_{xy,h}\rangle
   =
   \langle a_h,E_{G_h}(B)a_h\rangle.
   \tag{5.3}
   \]
   Without the isometry, the right-hand side contains the metric \(J_h^*J_h\) and must be treated accordingly.
5. **Infrared and continuum control.** The measures in (5.3) must have no residual zero atom after conserved-mode projection, a finite inverse-rate moment, and uniform small-rate tail control as \(h\downarrow0\).

For the raw pair transfer, the natural formal candidate \(G_{\rm pair}=I-T_{\rm pair}\) is **not yet an admissible physical generator**. Substochasticity means it contains enclosure killing; self-adjointness, nonnegative spectrum, and a physical interpretation of escape have not been established. In particular, the factor \(r^{-1}=\varphi^6\) in the symbolic difference update does not imply a physical relaxation ratio \(\varphi^{-1}\).

## 6. Exact obstruction and next decision gate

The current state of the bridge is:

- **[P]** The Q6 pair automaton defines the finite substochastic transfer \(T_{\rm pair}=A/36\).
- **[P]** Its iterates compute retained two-replica path sums (2.4).
- **[P]** A stress insertion gives the two-replica statistic (3.2), once a state stress has independently been supplied.
- **[P]** Green–Kubo is governed by the spectral measure of the physical self-adjoint relaxation generator, equation (4.2).
- **[O]** No physical isometry/intertwiner \(J_h\) from the pair automaton to the Q6 mechanical dynamics has been constructed.
- **[O]** No state-resolved shear stress follows from the golden scalar coding alone.
- **[C]** A golden hierarchy of physical stress relaxation rates remains testable only after the operator and observable maps are derived.

**Decision gate:** run the exact transfer audit first. If the raw transfer fails detailed balance or has enclosure killing incompatible with the proposed equilibrium interpretation, do not force it into Green–Kubo. Retain it as a geometric overlap/large-deviation operator and construct the physical relaxation generator independently from the same-energy mechanical model. The two sectors may then be connected by a proved observable/intertwining map, or they may remain distinct.

## 7. Repository dependencies

- \`audits/tsmr_c_iching_overlap_automaton.py\`: exact golden Q6 pair automaton and finite path-count certificate.
- \`audits/tsmr_q6_stress_transfer_bridge.py\`: transfer matrix and reversibility/escape audit.
- \`research/Q6_GOLDEN_MEMORY_SPECTRUM_GREEN_KUBO_2026-11-24.md\`: golden rate/weight ansatz and infrared Green–Kubo criterion.
- \`research/Q6_CENTRAL_FORCE_STRAIN_ENERGY_2026-11-24.md\`: same-energy mechanical stress and OU benchmark.
- \`research/Q6_JITTERBUG_MICROSCOPIC_STRESS_GREEN_KUBO_STOKES_2026-11-24.md\`: conditional Green–Kubo/Stokes matching theorem.
- \`theorems/T131-q6-phonon-phason-green-kubo-transport.md\` and \`theorems/T132-coupled-phonon-phason-ou-green-kubo.md\`: phonon/phason stress-sector requirements and controlled OU identities.


## 8. Executed exact audit: decisive obstruction

The audit was executed on GitHub Actions (Python 3.12), run [45394600161](https://github.com/fabianleonaressi95/theorem/actions/runs/45394600161), commit `d85b9ab6036e1ec7311c4a1ca1c68d0b535716cf`. The run completed the exact-state transfer calculation and returned:

| Quantity | Exact audit output |
|---|---:|
| Reachable states | 5,566 |
| Directed support edges | 34,762 |
| Diameter in \\(\\mathbb Z[\\lambda]\\) | \\(\\frac{33}{20}+\\frac{31}{20}\\lambda\\) |
| Row-sum range of integer multiplicities | 0–18 |
| Rows with at least one killed candidate move | 5,566 / 5,566 |
| Missing paired choices (counted with multiplicity) | 165,614 |
| Directed edges whose reverse is also present | 848 |
| Reciprocal support fraction | 0.0243944537138 |
| Maximum forward/reverse multiplicity defect on support edges | 1 |
| Uniform reversible | `False` |

The row-sum maximum 18 is strictly below the 36 candidate paired moves; every reachable state loses at least half of its candidate choices, and some states have no retained outgoing move. This is substantial enclosure killing, not a small boundary correction.

More decisively, the support is not symmetric: only 848 of 34,762 directed support edges have their reverse. Therefore **there is no strictly positive diagonal weight matrix** \\(W=\\operatorname{diag}(w_x)\\) satisfying detailed balance
\\[
WT_{\\rm pair}=T_{\\rm pair}^{T}W,\\qquad w_x>0.
\\]
Indeed, for any retained edge \\(x\\to y\\) with no reverse edge, detailed balance would require \\(w_xT_{xy}=w_yT_{yx}=0\\), contradicting \\(w_x>0\\) and \\(T_{xy}>0\\). The conclusion is stronger than failure of the uniform measure: no positive diagonal reweighting can make this raw finite transfer reversible.

**Status update:** [N] the numerical support audit is executed; [P] the implication “asymmetric support excludes every strictly positive diagonal detailed-balance measure” is an exact finite-matrix argument. Consequently the raw \\(T_{\\rm pair}\\) is ruled out as a reversible equilibrium transfer on this state space. It remains a valid substochastic geometric overlap operator. Do not repair it by row-normalization or ad hoc symmetrization: either operation changes the model and would need a new derivation.

The CI workflow is `.github/workflows/tsmr-q6-stress-transfer.yml`; the script remains `audits/tsmr_q6_stress_transfer_bridge.py`.


## 9. Independent mechanical branch: canonical Q6 central-force OU model

The failed detailed-balance test above does not prevent a separate physical-model construction. The central-force energy now supplies an independent route:
- `research/Q6_CENTRAL_FORCE_STRAIN_ENERGY_2026-11-24.md` derives the Hessian and strain stress from one energy;
- `audits/q6_central_force_ou_green_kubo.py` evaluates the canonical six-dimensional cube control;
- the combined CI run [45396828057](https://github.com/fabianleonaressi95/theorem/actions/runs/45396828057) passes both the pair-transfer obstruction audit and the mechanical OU benchmark.

For the canonical (Q_6\hookrightarrow\mathbb R^6) embedding, the quadratic shear-stress OU calculation gives
[
\int_0^\infty C_{ij,ij}(t)\,dt
=16(k_BT)^2/\mu,
\qquad
\eta^{ij,ij}_{\rm OU}=16k_BT/(\mu V).
]
This is a finite model result, not a spectral bridge from (T_{\rm pair}): the mechanical generator is derived independently from the rigidity Hessian and the declared OU bath. The unresolved three-dimensional Q6/Jitterbug fibre lift and material calibration remain necessary for a physical prediction.
