# Network Dynamics — synthetic prototype

An isolated research application for comparing organizational network structures, competence distribution, knowledge transfer and task-based resilience.

**Evidence boundary:** all executable experiments use synthetic data. This code does not reconstruct Sun Microsystems Italia, validate Giovanni Vota's Practices empirically, establish that self-management is superior, or demonstrate an advantage of RGS embeddings.

## Components

- `src/network_dynamics.py`: synthetic hierarchical, matrix and Practices-like graphs; bounded knowledge-state diffusion; connectivity metrics; random vertex-removal graph robustness.
- `src/competence_model.py`: thresholded skill coverage, Herfindahl-style competence concentration and effective-agent count.
- `src/knowledge_dynamics.py`: bounded diffusion/decay/external-input update for exploratory longitudinal models.
- `src/resilience.py`: task-based capability coverage under agent unavailability and ordering by uniquely covered skills.
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

## Evidence status

| Item | Status |
|---|---|
| Model definitions and source code | Specified |
| Software invariants | GitHub Actions CI passed (run 44568313472; pytest step successful) |
| Numerical outputs | Synthetic only |
| Practices rollout / profit claims | Unverified testimonial claims |
| Comparative organizational effects | Open empirical hypotheses |
| RGS-specific modelling advantage | Open computational hypothesis |

No empirical validation, causal conclusion or commercial-readiness claim is made.
