# Network Dynamics — synthetic prototype

An isolated research application for comparing organizational network structures, competence distribution, knowledge transfer and task-based resilience.

**Evidence boundary:** all executable experiments use synthetic data. This code does not reconstruct Sun Microsystems Italia, validate Giovanni Vota's Practices empirically, establish that self-management is superior, or demonstrate an advantage of RGS embeddings.

## Components

- `src/network_dynamics.py`: synthetic hierarchical, matrix and Practices-like graphs; bounded knowledge-state diffusion; connectivity metrics; random vertex-removal graph robustness.
- `src/competence_model.py`: thresholded skill coverage, Herfindahl-style competence concentration and effective-agent count.
- `src/knowledge_dynamics.py`: bounded diffusion/decay/external-input update for exploratory longitudinal models.
- `src/resilience.py`: task-based capability coverage under agent unavailability and ordering by uniquely covered skills.\n- `src/monte_carlo.py`: paired-seed Monte Carlo summaries with sample dispersion and normal-approximation confidence intervals.\n- `src/sensitivity.py`: factorial sensitivity across diffusion, learning input, competence density, removal fraction and random versus highest-degree removal.\n- `src/topology_control.py`: profile-blind random graphs and degree-preserving rewires to separate graph topology from profile-based edge selection.
- `tests/`: software checks for graph invariants and research metrics.

Graph-connectivity robustness and task-based competence resilience are distinct metrics and must not be reported as interchangeable.

## Install and test

From repository root:

```bash
python -m pip install -r applications/network-dynamics/requirements.txt
python -m pip install pytest
python -m pytest applications/network-dynamics/tests -q
```

## Run the synthetic baseline

```bash
python applications/network-dynamics/src/network_dynamics.py \
  --seed 20261119 \
  --output applications/network-dynamics/results
```

The command writes JSON and CSV summaries locally. Generated results are synthetic; record the command, environment, dependency versions and commit SHA before treating any output as reproducible evidence.

## Paired-seed Monte Carlo audit\n\nRun 100 independent synthetic seeds while comparing all architectures under the same generated profiles and initial states within each replicate:\n\n```bash\npython applications/network-dynamics/src/monte_carlo.py \\\n  --replicates 100 \\\n  --seed 20261119 \\\n  --output applications/network-dynamics/results\n```\n\nThis writes `monte_carlo.json` and `monte_carlo.csv`. The reported 95% intervals use a normal approximation over synthetic seed replicates; they quantify model variability only, not uncertainty about real organizations. The graph-generation rules remain stylized assumptions, not validated representations of organizational forms.\n\n## Topology-only controls\n\nRun the controlled comparison with:\n\n```bash\npython applications/network-dynamics/src/topology_control.py \\\n  --replicates 100 \\\n  --seed 20261119 \\\n  --swaps-per-edge 20 \\\n  --removal-repetitions 40 \\\n  --output applications/network-dynamics/results\n```\n\nThe profile-blind `G(n,m)` baseline holds node and edge counts fixed but samples edges independently of competence profiles. Each architecture's degree-preserving rewire preserves its degree sequence and edge count while randomizing endpoint pairings. These controls distinguish the bundled profile-informed graph rules from degree-sequence effects; they do not make all other structural properties identical.\n\n## Topology control results\n\nThe degree-preserving rewiring experiment and quantitative interpretation are documented in [TOPOLOGY_CONTROL_AUDIT_2026-11-26.md](TOPOLOGY_CONTROL_AUDIT_2026-11-26.md). The report distinguishes degree-sequence effects from profile-informed edge placement and includes paired replicate differences.\n\n## Results audit\n\nThe latest quantitative interpretation is maintained in [RESULTS_AUDIT_2026-11-26.md](RESULTS_AUDIT_2026-11-26.md). It distinguishes architecture trade-offs, paired contrasts, parameter effects and the limits of synthetic inference.\n\n## Factorial sensitivity audit\n\nThe sensitivity script evaluates a full factorial grid: three diffusion rates, three learning-input rates, three competence-density regimes, two removal fractions and two removal mechanisms. Each scenario is replicated with paired architecture comparisons.\n\n```bash\npython applications/network-dynamics/src/sensitivity.py \\\n  --replicates 20 \\\n  --seed 20261119 \\\n  --output applications/network-dynamics/results\n```\n\nIt writes `sensitivity.json` and `sensitivity.csv`. The normal-approximation intervals quantify synthetic seed variability only. Highest-degree removal is a deliberately stylized targeted-failure stress test, not a model of real personnel loss.\n\n## Evidence status

| Item | Status |
|---|---|
| Model definitions and source code | Specified |
| Software invariants | GitHub Actions CI passed (run 44568313472; pytest step successful) |
| Numerical outputs | Synthetic only |
| Practices rollout / profit claims | Unverified testimonial claims |
| Comparative organizational effects | Open empirical hypotheses |
| RGS-specific modelling advantage | Open computational hypothesis |

No empirical validation, causal conclusion or commercial-readiness claim is made.

## Structural diagnostics and rewiring-intensity sweep

The structural sweep evaluates each architecture at 0, 1, 5, 20, 50 and 100 accepted double-edge swaps per original edge. Every intensity starts independently from the same original graph and uses a deterministic replicate/architecture/intensity seed. Degree sequence and edge count are checked at every point.

Reported diagnostics:
- mean local clustering coefficient;
- greedy-merge modularity (a deterministic heuristic, not a global modularity optimum);
- degree assortativity (undefined values are retained as NaN);
- mean Jaccard similarity of endpoint competence profiles on edges;
- average shortest-path length inside the largest connected component;
- component count, largest-component fraction and degree variance;
- achieved fraction of requested accepted swaps.

The sweep is a structural sensitivity analysis, not a causal decomposition. The degree sequence is held fixed within each architecture, while other graph properties are allowed to change together. The modularity score is explicitly heuristic. Confidence intervals are normal-approximation intervals over synthetic replicates and are not adjusted for multiple comparisons.

Run locally:

```bash
python applications/network-dynamics/src/structural_sweep.py \
  --replicates 100 \
  --seed 20261119 \
  --intensities 0 1 5 20 50 100 \
  --output applications/network-dynamics/results/structural-sweep
```

