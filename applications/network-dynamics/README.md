# Network Dynamics — synthetic prototype

An isolated research application for comparing organizational network structures, competence distribution, knowledge transfer and task-based resilience.

**Evidence boundary:** all executable experiments use synthetic data. This code does not reconstruct Sun Microsystems Italia, validate Giovanni Vota's Practices empirically, establish that self-management is superior, or demonstrate an advantage of RGS embeddings.

## Components

- `src/network_dynamics.py`: synthetic hierarchical, matrix and Practices-like graphs; bounded knowledge-state diffusion; connectivity metrics and vertex-removal robustness.
- `src/competence_model.py`: thresholded skill coverage, Herfindahl-style competence concentration and effective-agent count.
- `src/knowledge_dynamics.py`: bounded diffusion/decay/external-input update for exploratory longitudinal models.
- `src/resilience.py`: task-based capability coverage under agent unavailability and ordering by uniquely covered skills.
- `src/monte_carlo.py`: paired-seed Monte Carlo summaries and descriptive normal-approximation intervals.
- `src/sensitivity.py`: factorial sensitivity across diffusion, learning input, competence density, removal fraction and removal mechanism.
- `src/topology_control.py`: profile-blind random graphs and degree-preserving rewires.
- `src/structural_sweep.py`: structural diagnostics over a range of accepted degree-preserving edge swaps.
- `tests/`: software checks for graph invariants and research metrics.

Graph-connectivity robustness and task-based competence resilience are distinct metrics and must not be reported as interchangeable.

## Install and test

From repository root:

```bash
python -m pip install -r applications/network-dynamics/requirements.txt
python -m pip install pytest
python -m pytest applications/network-dynamics/tests -q
```

## Reproduce the experiments

### Baseline

```bash
python applications/network-dynamics/src/network_dynamics.py \
  --seed 20261119 \
  --output applications/network-dynamics/results
```

### Paired-seed Monte Carlo

```bash
python applications/network-dynamics/src/monte_carlo.py \
  --replicates 100 \
  --seed 20261119 \
  --output applications/network-dynamics/results/monte-carlo
```

### Factorial sensitivity

```bash
python applications/network-dynamics/src/sensitivity.py \
  --replicates 20 \
  --seed 20261119 \
  --output applications/network-dynamics/results/sensitivity
```

The factorial grid varies three diffusion rates, three learning-input rates, three competence-density regimes, two removal fractions and two removal mechanisms. Architecture comparisons use paired replicate inputs.

### Topology-only controls

```bash
python applications/network-dynamics/src/topology_control.py \
  --replicates 100 \
  --seed 20261119 \
  --swaps-per-edge 20 \
  --removal-repetitions 40 \
  --output applications/network-dynamics/results/topology-control
```

The profile-blind `G(n,m)` baseline holds node and edge counts fixed but samples edges independently of competence profiles. Each architecture's degree-preserving rewire preserves its degree sequence and edge count while randomizing endpoint pairings. It does not preserve clustering, modularity, path lengths or connected components.

### Structural rewiring-intensity sweep

```bash
python applications/network-dynamics/src/structural_sweep.py \
  --replicates 100 \
  --seed 20261119 \
  --intensities 0 1 5 20 50 100 \
  --output applications/network-dynamics/results/structural-sweep
```

The sweep reports clustering, heuristic modularity, degree assortativity, competence-profile similarity on edges, path length in the largest component, component count, largest-component fraction, degree variance and achieved swap fraction. The modularity score is a deterministic heuristic, not a global optimum. The sweep changes several graph properties together and is not a causal decomposition.

## Quantitative audits

- [Baseline Monte Carlo and factorial sensitivity audit](RESULTS_AUDIT_2026-11-26.md): 100 paired baseline seeds and 108 factorial scenarios with 20 replicates per scenario.
- [Topology-only control audit](TOPOLOGY_CONTROL_AUDIT_2026-11-26.md): 100 paired replicates comparing original profile-informed graphs, degree-preserving rewires and a profile-blind reference.

### Main model-internal findings

1. The hierarchical construction retained the largest connected component most effectively under the tested removal procedures.
2. The Practices-like construction produced higher mean knowledge and threshold coverage in the tested setup, with greater within-skill dispersion and lower global connectivity.
3. Degree-preserving rewiring materially changed several metrics, especially for the Practices-like graph. Thus degree sequence alone does not explain the observed behavior.
4. Targeted highest-degree removal was more destructive than random removal in the tested grid.

These are findings about the specified synthetic graph-generation and update rules only. They are not empirical findings about real organizations.

## Continuous integration and evidence status

The [Network Dynamics workflow](../../.github/workflows/network-dynamics.yml) runs tests, a baseline smoke test, paired Monte Carlo, factorial sensitivity, topology-only controls and a structural rewiring-intensity sweep. The successful [run 45868636969](https://github.com/fabianleonaressi95/theorem/actions/runs/45868636969) on `main` uploaded the artifact `network-dynamics-synthetic-results`.

| Item | Status |
|---|---|
| Model definitions and source code | Implemented |
| Software tests and experiment smoke tests | CI passed |
| Paired Monte Carlo and factorial sensitivity | Executed; synthetic results audited |
| Topology-only controls | Executed; synthetic results audited |
| Structural rewiring-intensity sweep | Executed in CI; output retained in workflow artifact; separate quantitative interpretation pending |
| Empirical organizational validation | Not performed |
| Causal claims about organizational structures | Not established |
| RGS-specific modelling advantage | Open computational hypothesis |

Normal-approximation intervals summarize variability across synthetic replicates only. They are not empirical confidence intervals about real organizations, and the reported exploratory comparisons are not adjusted for multiple testing.

## Next research steps

1. Inspect and publish the structural-sweep artifact with a separate quantitative audit.
2. Add multiple independent rewires per graph and assess whether the requested swap counts adequately mix the degree-preserving ensemble.
3. Report continuous coverage curves alongside the threshold metric, particularly where the threshold is unattainable at a parameter boundary.
4. Validate model assumptions and metrics against an independently collected empirical network before making claims about real organizational systems.
