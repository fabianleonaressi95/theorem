# Network Dynamics — synthetic results audit

**Audit date:** 2026-11-26  
**Source:** GitHub Actions run [45858814288](https://github.com/fabianleonaressi95/theorem/actions/runs/45858814288), artifact `network-dynamics-synthetic-results`.  
**Scope:** 30 synthetic agents, 8 skills, 45 edges, 160 update steps. The sensitivity grid contains 108 parameter/stress scenarios, 20 replicates per scenario, and three graph-generation rules.

## 1. Baseline Monte Carlo (100 paired seeds)

| Architecture | Mean knowledge state | Skill coverage > 0.60 | Within-skill dispersion | Largest component after 20% random removal |
|---|---:|---:|---:|---:|
| Hierarchical | 0.2578 | 0.0000 | 0.0320 | 0.9556 |
| Matrix | 0.2486 | 0.0170 | 0.0754 | 0.8851 |
| Practices-like | 0.2718 | 0.0675 | 0.1717 | 0.7316 |

The hierarchy has the highest retained connectivity and lowest dispersion in this baseline. Practices-like has the highest mean knowledge and threshold coverage, but also the highest dispersion and lowest random-removal connectivity. These are trade-offs, not a single overall ranking.

The baseline intervals in the artifact are normal-approximation intervals over synthetic seeds; they are not empirical confidence intervals about real organizations.

## 2. Factorial sensitivity and paired architecture contrasts

The 108 scenarios vary:
- diffusion rate `eta`: 0.05, 0.22, 0.50;
- target/learning rate `rho`: 0, 0.008, 0.05;
- skills per agent: 1–2, 2–3, 4–5;
- removal fraction: 10%, 30%;
- removal mechanism: random or highest-degree targeted removal.

For each scenario, architectures use the same generated skill profiles, initial state, seed, and removal-mask random stream. The report now includes replicate-level paired architecture differences, not merely comparisons of separate architecture means.

### Mean paired differences across the 108 scenarios

Positive values mean the architecture named first has a larger metric.

| Contrast | Largest component retained | Mean knowledge | Skill coverage | Dispersion |
|---|---:|---:|---:|---:|
| Hierarchical − Matrix | +0.1478 | +0.0066 | +0.0159 | −0.0254 |
| Hierarchical − Practices-like | +0.2649 | −0.0108 | −0.0774 | −0.1097 |
| Matrix − Practices-like | +0.1171 | −0.0174 | −0.0933 | −0.0843 |

Across these scenarios, hierarchical exceeds matrix and Practices-like in largest-component retention in all 108 paired scenario means. Matrix exceeds Practices-like in 105/108 scenario means. This is a result about these specific graph-generation rules and node-removal experiments only.

Practices-like has higher mean knowledge than both alternatives in the scenario-averaged paired comparisons, while its skill-coverage metric is also higher. It pays for this in graph fragmentation and within-skill dispersion.

### Targeted removal matters

Average retained largest-component fractions over the grid:

| Architecture | Random 10% | Random 30% | Highest-degree 10% | Highest-degree 30% |
|---|---:|---:|---:|---:|
| Hierarchical | 0.987 | 0.877 | 0.967 | 0.592 |
| Matrix | 0.913 | 0.815 | 0.819 | 0.284 |
| Practices-like | 0.806 | 0.669 | 0.644 | 0.245 |

Targeted removal is much more damaging than random removal, particularly at 30%. The hierarchy is most robust under the chosen attack rule. Highest-degree removal is a graph stress test, not a model of real personnel decisions.

### Parameter effects

- `rho` strongly changes mean knowledge and threshold coverage. With `rho=0`, the update has no pull toward target profiles; because initial states are at most 0.55 and neighbor mixing is convex, the threshold `>0.60` is mathematically unattainable. Therefore the zero coverage at `rho=0` is a metric-boundary effect, not evidence that an architecture fails.
- Increasing skill density raises mean knowledge and coverage, but also increases within-skill dispersion in this model.
- `eta` has a much smaller effect on mean knowledge than `rho` in the tested range.
- Increasing removal from 10% to 30%, and switching from random to highest-degree removal, sharply lowers connectivity.

## 3. Interpretation and limits

1. **No universal winner.** The hierarchy is strongest for connectivity/robustness; Practices-like is strongest for mean knowledge and the chosen coverage metric; dispersion differs substantially.
2. **Architecture is bundled with its construction rule.** The hierarchy uses a tree backbone and depth similarity; matrix prioritizes complementary skill profiles; Practices-like prioritizes shared competencies. Since profiles influence graph edges, these are not topology-only comparisons.
3. **No empirical validation.** All agents, profiles, graphs, and update parameters are synthetic. The results do not establish that real Practices organizations outperform or underperform hierarchical organizations.
4. **Exploratory intervals.** The reported 95% intervals are normal approximations across 20 synthetic replicates, unadjusted for the many scenario/metric comparisons. Treat them as descriptive uncertainty summaries, not confirmatory tests.
5. **Threshold caveat.** Coverage at 0.60 is degenerate when `rho=0`; future reporting should include a lower threshold or a continuous coverage curve.

## 4. Research status

**Established computationally within this prototype:** the tested hierarchical graph-generation rule yields the highest retained giant-component fraction across the factorial grid; targeted high-degree removal is more destructive than random removal; the Practices-like rule yields higher average knowledge and dispersion in the tested setup.

**Not established:** causal effects of organizational structure, empirical claims about Sun Practices, or topology-only superiority.

## 5. Next required control

Implement a topology-only comparison in which edge generation is independent of skill profiles (or degree-preserving rewiring is applied while holding degree sequence fixed), while keeping node attributes and update parameters paired. Compare that control with the current bundled architecture effects. Only then can we distinguish effects of topology from effects of profile-based assortativity/complementarity.
