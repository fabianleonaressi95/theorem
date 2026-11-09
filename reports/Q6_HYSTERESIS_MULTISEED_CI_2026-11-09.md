# Q6 multiseed/multirate hysteresis study — CI record (2026-11-09)

## Execution provenance

- Repository: `fabianleonaressi95/theorem`
- Workflow run: [42647088030](https://github.com/fabianleonaressi95/theorem/actions/runs/42647088030)
- Checked-out commit: `0bd39b7f840483bc483e930aa62d858e4b7be79f`
- Job: `audit` — **success**
- Artifact: [q6-multiseed-multirate-study](https://github.com/fabianleonaressi95/theorem/actions/runs/42647088030/artifacts/13688791144)
- Artifact SHA-256: `3a26ccdf51ccc7625b372ed2a71e3d23eef3612bb3d4a2cbba2bc261570a442d`
- Artifact contains `q6_hysteresis_sweep_study.json`, `q6_hysteresis_sweep_nl.png`, and `q6_hysteresis_sweep_nlt.png`.

## Reproducible study configuration

The full sweep completed with:
- seeds: `11,23,37,51,67`
- dwell steps: `10,40,160,640`
- `sigma_max=2`, `sigma_count=21`
- `dt=0.025`
- `omega0=omega1=2`
- `tau0=tau1=1`

The workflow also ran the small benchmark and a smoke sweep. The full JSON records per-seed means and standard deviations for branch-gap and loop-area diagnostics, separated by NL/NLT and reversal branch.

## Test evidence

All test commands in the job passed:
- 19 passed: Q6 synchronization, hysteresis metrics, constitutive hysteresis, sweep study.
- 22 passed: the same suite plus asymmetric Prandtl–Ishlinskii.
- 20 passed: synchronization, metrics, constitutive hysteresis, asymmetric Prandtl–Ishlinskii, CSV audit.

The final 20-test command completed in 0.28 s. The job also completed both the benchmark and full multiseed/multirate sweep and uploaded the three output files.

## Independent Q6 topology checks emitted by the benchmark

The run reported:
- vertices/edges/square faces: `64/192/240`
- exact chain identity `B1 @ B2 = 0`: true
- numerical ranks: `rank(B1)=63`, `rank(B2)=129`
- graph cycle rank: `129`
- filled first Betti number: `b1=0`
- second Betti number of the truncated 2-skeleton: `b2=111`
- Anti-Twin squared identity and chain-map checks: true.

The reported ranks are numerical; the exact statement in this run is the chain identity, not an exact-arithmetic rank certificate.

## Interpretation and limits

This is a successful **synthetic/reproducible computational benchmark**, not experimental validation. It does not establish predictive accuracy for a physical actuator or magnetic material, nor industrial readiness, lifetime, cost, or control benefits. The experimental-data validation track remains separate. In particular, do not treat this run as closing issue #113 or as a substitute for the measured-data protocol.

The JSON and plots are preserved in the linked Actions artifact; they were uploaded by CI and are not committed as repository result files in this commit.
