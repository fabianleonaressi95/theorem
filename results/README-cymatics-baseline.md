# C01–C04 baseline output

Run:

```bash
python scripts/cymatics_wave_benchmarks.py --output results/cymatics_baseline.json
python -m unittest discover -s tests -p 'test_cymatics_wave_benchmarks.py' -v
```

The baseline JSON in this directory records a local NumPy 2.3.5 execution of the committed benchmark implementation at grid size 18. It is a deterministic numerical control, not an experimental measurement. Re-run the script to regenerate it. The expected invariants are:
The committed baseline JSON records a local NumPy 2.3.5 execution of the benchmark implementation at grid size 18. It is a deterministic numerical control, not an experimental measurement. Re-run the script to regenerate it. The expected invariants are:
- C01: finite-difference plate eigenvalues agree with the exact discrete separation formula to floating-point tolerance.
- C02: the ideal square has equal ((1,2)) and ((2,1)) modal eigenvalues.
- C03: the selected asymmetric diagonal stiffness perturbation splits the degenerate pair.
- C04: the 6-cube graph Laplacian has eigenvalues (0,2,4,6,8,10,12) with multiplicities (1,6,15,20,15,6,1).

These are deterministic mathematical checks, not experimental measurements.
