# RGS Cellular Dynamics Benchmark v0.1

Initial reproducible scaffold for binary synchronous cellular automata on:
- periodic square Moore lattices (reference),
- the 6-dimensional hypercube Q6 (64 vertices, degree 6),
- PRISM = C64 □ C6 □ C6 □ C6 □ C5 (69,120 vertices, degree 10).

## Run
```bash
python scripts/rgs_cellular_dynamics_benchmark.py --model q6 --steps 100 --seeds 0 1 2 3 4 --output q6.json
python scripts/rgs_cellular_dynamics_benchmark.py --model prism --steps 20 --seeds 0 1 --output prism.json
pytest -q tests/test_rgs_cellular_dynamics_benchmark.py
```

## Rule encodings
For degree d, totalistic rules are tables of shape 2 x (d+1): 14 bits on Q6 and 22 on PRISM. Ordered rules have 2^(d+1) entries: 128 bits on Q6 and 2048 on PRISM. Ordered rules depend on the explicitly documented neighbour ordering.

## Scope and limitations
This version is a smoke benchmark with one randomly generated rule per family. It does not implement genetic evolution, common-random-number comparisons, Hodge fitness, or full automorphism-invariant symmetry. The Q6 symmetry statistic is only a partial diagnostic. No physical interpretation is claimed.

## Research status
Implemented and smoke-tested; not yet statistically validated. Next: evolutionary populations, paired seed protocol, Pareto objectives, then transfer tests Q6 -> PRISM.
