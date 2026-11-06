#!/usr/bin/env python3
"""CLI entry point for the discrete de Rham benchmark.

Usage:
    python3 run_benchmark.py --config configs/default.json --out results/run1
    python3 run_benchmark.py --config configs/default.json --out results/run1 --no-plots
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ddr.experiment import run_config
from ddr.plotting import make_all_plots


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--no-plots", action="store_true")
    args = ap.parse_args()

    with open(args.config) as f:
        cfg = json.load(f)

    payload = run_config(cfg, args.out)
    if not args.no_plots:
        pdir = make_all_plots(payload, args.out)
        print(f"[done] plots in {pdir}")


if __name__ == "__main__":
    main()
