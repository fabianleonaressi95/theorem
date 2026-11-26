# C01–C04 baseline output

Run:

```bash
python scripts/cymatics_wave_benchmarks.py --output results/cymatics_baseline.json
python -m unittest discover -s tests -p 'test_cymatics_wave_benchmarks.py' -v
```

The generated JSON is intentionally not committed as a claimed result until the script has been executed in the target repository environment. The expected invariants are:
- C01: finite-difference plate eigenvalues agree with the exact discrete separation formula to floating-point tolerance.
- C02: the ideal square has equal ((1,2)) and ((2,1)) modal eigenvalues.
- C03: the selected asymmetric diagonal stiffness perturbation splits the degenerate pair.
- C04: the 6-cube graph Laplacian has eigenvalues (0,2,4,6,8,10,12) with multiplicities (1,6,15,20,15,6,1).

These are deterministic mathematical checks, not experimental measurements.
