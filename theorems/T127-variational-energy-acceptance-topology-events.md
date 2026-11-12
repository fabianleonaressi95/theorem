# T127 — Variational acceptance and energy dissipation for Burgers-conserving topology events

**Classification:** PROVED abstract finite-dimensional hybrid-system theorem under the stated differentiability, positivity and event-acceptance hypotheses; MODEL-DEPENDENT as a dislocation mechanics model; OPEN for material calibration, event kinetics, Frank–Read source regeneration and continuum convergence.

## 1. State space with changing topology

Let \(\mathfrak G\) be a declared family of finite oriented graphs. For each \(G\in\mathfrak G\), let \(Q_G\) be a finite-dimensional admissible configuration space and let
\[
c_G\in C_1(G;\Lambda_B)
\]
be a Burgers-labelled 1-chain over a fixed additive lattice \(\Lambda_B\). On each graph sector define a differentiable energy
\[
\mathcal E_G:Q_G\to\mathbb R.
\]
The energy includes whichever line, core, pinning and conservative loading terms have been declared for that sector. Comparisons between different graph sectors are meaningful only when these energies use a common normalization, common units and the same external loading state.

A candidate topology event is a map
\[
\mathscr R:(G,q,c_G)\longmapsto(G^+,q^+,c_{G^+}^+)
\]
that satisfies the Burgers-boundary constraint
\[
\partial_1c_{G^+}^+=\partial_1c_G
\]
under the chosen identification of the event patch's boundary vertices. T126 proves this constraint for the restricted equal-Burgers head-exchange rule.

## 2. Energetic acceptance rule

Associate to a proposed event a declared event cost \(C_{\mathscr R}\ge0\), expressed in the same energy units as \(\mathcal E\). It represents a modelled non-negative energetic/dissipative allowance for the topology update. It is **not**, without an additional saddle-point or kinetic model, an activation barrier.

The event is accepted exactly when
\[
\boxed{
\mathcal E_{G^+}(q^+)+C_{\mathscr R}
\le \mathcal E_G(q).
}
\tag{127.1}
\]
Equivalently, the energetic margin
\[
\mathfrak m_{\mathscr R}
=\mathcal E_G(q)-\mathcal E_{G^+}(q^+)-C_{\mathscr R}
\tag{127.2}
\]
must be non-negative. The event map, candidate geometry, event cost and energy on both graph sectors are declared model inputs; (127.1) is a selection/acceptance criterion, not a law deriving those inputs.

## 3. Hybrid energy-dissipation theorem

Between topology events, suppose the state evolves on a fixed graph sector by the autonomous overdamped gradient flow
\[
\mathsf M_G(q)\dot q
=-\operatorname{grad}_{Q_G}\mathcal E_G(q),
\qquad \mathsf M_G(q)>0.
\tag{127.3}
\]
At each event time, suppose the update satisfies the Burgers-boundary constraint and is accepted by (127.1).

**Theorem 127.** Along every such piecewise-smooth trajectory with finitely many accepted events on a bounded time interval:

1. On every smooth segment,
\[
\frac{d}{dt}\mathcal E_G(q(t))
=-\left\langle\operatorname{grad}\mathcal E_G,
\mathsf M_G^{-1}\operatorname{grad}\mathcal E_G\right\rangle
\le0.
\tag{127.4}
\]

2. At every accepted event,
\[
\mathcal E_{G^+}(q^+)-\mathcal E_G(q)
\le -C_{\mathscr R}\le0.
\tag{127.5}
\]

3. Therefore the piecewise-defined energy is non-increasing across both smooth evolution and topology updates. For \(N\) accepted events,
\[
\boxed{
\sum_{k=1}^{N}C_{\mathscr R_k}
\le \mathcal E(0)-\mathcal E(T)
}
\tag{127.6}
\]
provided the energy comparisons use the same declared reference and no external work is injected between or at events.

If, in addition, the energy is bounded below by \(\mathcal E_{\min}\), then
\[
\sum_{k=1}^{N}C_{\mathscr R_k}
\le \mathcal E(0)-\mathcal E_{\min}.
\tag{127.7}
\]
In particular, a hybrid trajectory cannot spend an unbounded total positive event cost while its energy remains bounded below.

**Proof.** On a smooth segment, differentiate \(\mathcal E_G(q(t))\) and substitute (127.3), giving (127.4) by positive definiteness of \(\mathsf M_G\). At an event, (127.1) rearranges to (127.5). Summing the smooth-segment energy drops and event jumps telescopes; discarding the additional non-negative smooth dissipation yields (127.6). The lower bound gives (127.7). \(\square\)

## 4. Exact algorithmic counterpart

The source implementation is [\`src/reconnection_energy.py\`](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/feat/variational-reconnection-event-acceptance-2026-11-12/src/reconnection_energy.py). It evaluates (127.1) using finite real inputs and an optional numerical comparison tolerance. The tolerance is a floating-point allowance only; it is not physical energy, thermal activation or an event barrier.

The corresponding tests are in [\`tests/test_reconnection_energy.py\`](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/feat/variational-reconnection-event-acceptance-2026-11-12/tests/test_reconnection_energy.py), proposed in source [PR #200](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/pull/200). They check downhill and uphill candidates, event-cost accounting, numerical tolerance and invalid inputs. **CI is not claimed to have passed** at this record's creation.

The evaluator only decides whether a supplied candidate passes the energy test. It does not construct \(\mathscr R\), check Burgers conservation itself, compute \(\mathcal E_G\), or solve the smooth evolution; those are separate responsibilities (T125–T126).

## 5. Relation to T124–T126 and Frank–Read dynamics

- **T124:** supplies the reduced circular-arc line-tension threshold under its declared assumptions. T127 does not derive that threshold or replace the core/atomistic analysis.
- **T125:** supplies the fixed-topology variational energy, first variation and autonomous gradient-flow dissipation.
- **T126:** supplies one explicit local topology rewrite with exact Burgers-boundary preservation for equal Burgers vectors.
- **T127:** joins smooth dissipation and accepted topology jumps into one hybrid Lyapunov statement.

The combined chain is
\[
\text{Q6/PRISM incidence}
\to \text{Burgers-labelled chain}
\to \text{T125 smooth variational flow}
\to \text{T126 conservative event map}
\to \text{T127 energetic acceptance}.
\]
The graph incidence data do not determine the physical Burgers lattice, event cost, core energy, mobility, activation mechanism or loading protocol.

## 6. Status ledger and exclusions

1. **PROVED:** energy decreases on each autonomous fixed-topology gradient-flow segment.
2. **PROVED:** every accepted event has a non-positive energy jump and pays its declared non-negative event cost.
3. **PROVED:** total accepted event cost is bounded by the total available energy drop when no external work is injected and the energy is bounded below.
4. **MODEL-DEPENDENT:** graph-sector energies, event cost, candidate topology map, mobility, loading and material calibration.
5. **OPEN:** derive event costs and candidate maps from atomistic/core calculations and calibrated material data.
6. **OPEN:** derive thermal event rates from a saddle-point/free-energy landscape and kinetic prefactor; a deterministic event cost is not an Arrhenius activation barrier.
7. **OPEN:** prove a Frank–Read emission/regeneration result, mesh-independent convergence and a Q6/PRISM-derived constitutive law.

Time-dependent loading, non-conservative Peach–Koehler work, inertia, stochastic forcing and quantum tunnelling are excluded from (127.4)–(127.7) unless their work/noise/action contributions are explicitly added to the balance.

**Conclusion.** T127 closes the abstract variational bookkeeping between smooth line motion and Burgers-conserving topology changes. It provides a Lyapunov-consistent acceptance rule for declared candidate events, not a material-specific prediction that a Frank–Read reconnection will occur.

## References

1. [T124 — Frank–Read source, line-tension threshold and atomistic core input](T124-frank-read-source-line-tension-atomistic-core.md).
2. [T125 — Q6/PRISM Burgers-labelled chains and the variational Frank–Read interface](T125-q6-prism-burgers-chain-frank-read-variational-interface.md).
3. [T126 — Exact Burgers conservation under a local equal-vector reconnection](T126-exact-burgers-conserving-local-reconnection.md).
4. [Source implementation PR #200](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/pull/200).

**FLN**
