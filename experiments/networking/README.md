# Q6 Modular Interconnection Fabric — experimental benchmark

This directory contains a reproducible **graph/queueing abstraction** for the
proposed modular Q6 network. It is intended to test hypotheses, not to claim
that Q6 is already faster, cheaper, or more resilient than established fabrics.

## Modelled networks

- `Q6-K64-direct`: 64 Q6 modules, complete global graph (K_{64}).
- `Q6-C8-direct`: 64 Q6 modules, degree-8 circulant global graph with
  neighbours at offsets +/-1, +/-2, +/-3, +/-4 modulo 64.
- `Q6-C8-Valiant`: same degree-8 global graph, with a uniformly selected
  intermediate module for inter-module traffic.
- `Torus-16x16x16`: 4096-endpoint 3D torus, dimension-order routing.
- `FatTree-1to1`: abstract 64-pod folded-Clos reference model, 1:1
  oversubscription ratio by construction. It is not a vendor-specific design.

The Q6 gateway assignment is deterministic: each module's sorted global
neighbour list determines gateway slots 0 through degree-1. This is a logical
wiring convention, not a claim that this is the optimal physical placement.

## Run locally

Requires Python 3.10+ and the standard library only.

```bash
python experiments/networking/q6_fabric_sim.py --self-test
python experiments/networking/q6_fabric_sim.py --flows 4096 --seed 20261116 --csv q6_fabric_results.csv
```

## GitHub Actions

The workflow `.github/workflows/q6-fabric.yml` runs graph-invariant checks and
a reproducible smoke benchmark on pushes and pull requests. It can also be
started manually with `workflow_dispatch`; the default manual run uses 4096
flows. The CSV is uploaded as the artifact
`q6-fabric-benchmark-results`.

## Interpretation and limitations

This is a deliberately simple contention model:

- all flows are injected at time zero;
- each directed link is full-duplex and serializes one packet per cycle;
- store-and-forward, one cycle per hop;
- flows are processed in a seeded randomized arbitration order.

It does **not** model finite buffers, packet lengths, switch arbitration,
credit-based flow control, virtual channels, deadlock avoidance, adaptive
routing beyond the selected Valiant intermediate, unequal link rates,
transceiver power, cabling cost, or physical switch latency.

The reported latency and throughput are therefore **model-dependent cycle
counts**, not hardware predictions. In particular, the Fat Tree and torus
models use different logical switch/link representations from the Q6 graph.
A fair hardware comparison requires calibrated per-link and per-switch
parameters, identical traffic traces, packet-level or cycle-accurate
simulation, and eventually a physical demonstrator.

The traffic pattern `all-to-all-permutation` is one random derangement
(one destination per source), not the full (N(N-1)) pairwise all-to-all
exchange. `gather-broadcast-proxy` is a centralized stress pattern, not an
implementation of MPI All-Reduce.

No performance superiority is asserted. The purpose of this benchmark is to
make assumptions explicit and identify workloads where the modular Q6
fabric may warrant deeper evaluation.
