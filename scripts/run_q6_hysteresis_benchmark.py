#!/usr/bin/env python3
"""Run exact Q6 cellular audit and finite NL/NLT continuation sweeps."""
import argparse
import json
import sys
from pathlib import Path

# Allow direct execution as: python scripts/run_q6_hysteresis_benchmark.py
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import numpy as np
from models.q6_topological_synchronization import (
    build_q6_complex, audit_q6_complex, simulate_branch,
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--steps-per-sigma", type=int, default=40)
    parser.add_argument("--sigma-max", type=float, default=2.0)
    parser.add_argument("--sigma-count", type=int, default=9)
    parser.add_argument("--seed", type=int, default=20261109)
    parser.add_argument("--output", type=Path, default=Path("q6_hysteresis_results.json"))
    args = parser.parse_args()
    if args.steps_per_sigma < 1 or args.sigma_count < 2 or args.sigma_max <= 0:
        parser.error("steps-per-sigma >= 1, sigma-count >= 2, sigma-max > 0 required")

    K = build_q6_complex()
    report = {
        "complex_audit": audit_q6_complex(K),
        "protocol": {
            "steps_per_sigma": args.steps_per_sigma,
            "sigma_max": args.sigma_max,
            "sigma_count": args.sigma_count,
            "seed": args.seed,
            "frequency_distribution": {"omega0": 2.0, "omega1": 2.0, "tau0": 1.0, "tau1": 1.0,
                "convention": "node N(Omega0,1/tau0) in co-rotating frame; link N(Omega1,1/tau1), mean retained"},
        },
    }
    sigmas = np.linspace(0.0, args.sigma_max, args.sigma_count)
    for model in ("NL", "NLT"):
        forward, terminal = simulate_branch(
            K, sigmas, model, args.seed, args.steps_per_sigma, return_final=True
        )
        backward = simulate_branch(
            K, sigmas[::-1], model, args.seed, args.steps_per_sigma, initial=terminal
        )
        report[model] = {"forward": forward, "backward": backward}

    report["interpretation"] = {
        "status": "exploratory finite-size numerical benchmark",
        "hysteresis_claim": "not established; inspect branch separation and refine protocol",
        "limitations": [
            "finite Q6 only; no thermodynamic-limit result",
            "no experimental industrial data loaded",
            "no Preisach/Prandtl-Ishlinskii/Bouc-Wen/Jiles-Atherton fitting",
            "cubical extension is not the simplicial model studied in the 2021 paper",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["complex_audit"], indent=2))
    print("wrote", args.output)


if __name__ == "__main__":
    main()
