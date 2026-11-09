# RGS–PRISM audit records

- [PRISM 69,120 incidence audit](prism_69120_audit.json): regenerated B1/B2 and exact B1B2=0 check; product-torus Betti values are formula-based.
- [188D Anti-Twin recovered-matrix audit](188d_antitwin_audit.json): intrinsic kernel/projector checks and the negative result for the stored geometric intertwiner.
- [Krist-All recovery status](KRISTALL_RECOVERY_STATUS.md): the recovered archive does not yet contain the 11,725-class enumerator or K/W0 data.
- [Recovery manifest](RECOVERY_MANIFEST.md): artifact provenance, hashes and missing source objects.

Run the PRISM audit with:

```bash
python -m pip install -r requirements-audit.txt
python scripts/audit_prism_69120.py
```

Run the 188D matrix audit after placing the recovered NPZ at a local path:

```bash
python scripts/audit_188d_antitwin.py --input /path/to/actual_original_X_report_matrices.npz
```

The 188D audit input is not committed in this repository release; its SHA-256 is recorded in the recovery manifest. No synthetic data is substituted for it.
