"""Plots: convergence/spectral behaviour, geometry diagnostics, residuals."""
from __future__ import annotations

import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def _series(exp, key):
    """Extract (h, values) for runs of an experiment."""
    hs, vals = [], []
    for r in exp["runs"]:
        hs.append(r["h"])
        try:
            vals.append(key(r))
        except Exception:
            vals.append(np.nan)
    return np.array(hs), np.array(vals, float)


def plot_lambda_minpos(results, outdir):
    """Smallest positive Hodge eigenvalue vs h, per level k and experiment."""
    for k in range(4):
        fig, ax = plt.subplots(figsize=(7, 5))
        any_ = False
        for exp in results:
            d = exp["dim"]
            if k >= d + 1:
                continue
            hs, vals = _series(
                exp, lambda r, kk=str(k): r["spectra"][kk]["lambda_min_pos"])
            if np.all(np.isnan(vals)):
                continue
            any_ = True
            ax.loglog(hs, vals, "o-", label=exp["name"], ms=4)
        if not any_:
            plt.close(fig)
            continue
        ax.set_xlabel("h")
        ax.set_ylabel(f"lambda_min^+ (k={k})")
        ax.set_title("Smallest positive Hodge-Laplacian eigenvalue")
        ax.grid(True, which="both", alpha=0.3)
        ax.legend(fontsize=8)
        fig.tight_layout()
        fig.savefig(os.path.join(outdir, f"lambda_minpos_k{k}.png"), dpi=130)
        plt.close(fig)


def plot_lambda_max(results, outdir):
    for k in range(4):
        fig, ax = plt.subplots(figsize=(7, 5))
        any_ = False
        for exp in results:
            d = exp["dim"]
            if k >= d + 1:
                continue
            hs, vals = _series(
                exp, lambda r, kk=str(k): r["spectra"][kk]["lambda_max"])
            if np.all(np.isnan(vals)):
                continue
            any_ = True
            ax.loglog(hs, vals, "o-", label=exp["name"], ms=4)
        if not any_:
            plt.close(fig)
            continue
        ax.set_xlabel("h")
        ax.set_ylabel(f"lambda_max (k={k})")
        ax.set_title("Largest computed Hodge-Laplacian eigenvalue")
        ax.grid(True, which="both", alpha=0.3)
        ax.legend(fontsize=8)
        fig.tight_layout()
        fig.savefig(os.path.join(outdir, f"lambda_max_k{k}.png"), dpi=130)
        plt.close(fig)


def plot_cond_M(results, outdir):
    for k in range(4):
        fig, ax = plt.subplots(figsize=(7, 5))
        any_ = False
        for exp in results:
            if k >= exp["dim"] + 1:
                continue
            hs, vals = _series(
                exp, lambda r, kk=k: r["inner_products"][kk]["cond"])
            if np.all(np.isnan(vals)):
                continue
            any_ = True
            ax.loglog(hs, vals, "o-", label=exp["name"], ms=4)
        if not any_:
            plt.close(fig)
            continue
        ax.set_xlabel("h")
        ax.set_ylabel(f"cond(M_{k})")
        ax.set_title("Condition number of discrete inner product")
        ax.grid(True, which="both", alpha=0.3)
        ax.legend(fontsize=8)
        fig.tight_layout()
        fig.savefig(os.path.join(outdir, f"cond_M_k{k}.png"), dpi=130)
        plt.close(fig)


def plot_jacobian(results, outdir):
    """min/max det J and singular values vs h (mesh-independent quantities)."""
    for key, fname, ylab in [
        ("min_det_jac", "detJ_min.png", "min det D Phi"),
        ("max_det_jac", "detJ_max.png", "max det D Phi"),
        ("min_sv_jac", "sv_min.png", "min sigma(D Phi)"),
        ("max_sv_jac", "sv_max.png", "max sigma(D Phi)"),
        ("max_cond_g", "cond_g_max.png", "max cond g_K"),
    ]:
        fig, ax = plt.subplots(figsize=(7, 5))
        any_ = False
        for exp in results:
            hs, vals = _series(exp, lambda r, kk=key: r["geometry"][kk])
            if np.all(np.isnan(vals)):
                continue
            any_ = True
            ax.semilogx(hs[::-1], vals[::-1], "o-", label=exp["name"], ms=4)
        if not any_:
            plt.close(fig)
            continue
        ax.set_xlabel("h")
        ax.set_ylabel(ylab)
        ax.set_title("Jacobian / metric diagnostics vs refinement")
        ax.grid(True, which="both", alpha=0.3)
        ax.legend(fontsize=8)
        fig.tight_layout()
        fig.savefig(os.path.join(outdir, fname), dpi=130)
        plt.close(fig)


def plot_sweeps(results, outdir):
    """Sweep experiments: quantity vs swept parameter (fixed N)."""
    for exp in results:
        if "sweep_param" not in exp["runs"][0]:
            continue
        par = exp["runs"][0]["sweep_param"]
        vals = np.array([r["sweep_value"] for r in exp["runs"]], float)
        order = np.argsort(vals)
        vals = vals[order]
        rsorted = [exp["runs"][i] for i in order]
        panels = [
            ("lambda_min_pos", lambda r: r["spectra"]["0"]["lambda_min_pos"]),
            ("lambda_min_pos_k1", lambda r: r["spectra"]["1"]["lambda_min_pos"]),
            ("min_det_jac", lambda r: r["geometry"]["min_det_jac"]),
            ("kernel0", lambda r: r["spectra"]["0"]["kernel_num"]),
        ]
        fig, axes = plt.subplots(2, 2, figsize=(11, 8))
        for ax, (name, fn) in zip(axes.ravel(), panels):
            try:
                y = np.array([fn(r) for r in rsorted], float)
            except Exception:
                y = np.full(len(rsorted), np.nan)
            ax.semilogy(vals, y, "o-") if name != "min_det_jac" and name != "kernel0" \
                else ax.plot(vals, y, "o-")
            ax.set_xlabel(par)
            ax.set_ylabel(name)
            ax.grid(True, alpha=0.3)
        fig.suptitle(f"Sweep: {exp['name']} (N={rsorted[0]['N']})")
        fig.tight_layout()
        safe = par.replace(".", "_").replace("/", "_")
        fig.savefig(os.path.join(outdir, f"sweep_{safe}_{exp['name']}.png"),
                    dpi=130)
        plt.close(fig)


def plot_residuals(results, outdir):
    """Bar summary of the largest algebraic residuals per experiment."""
    names, vals = [], []
    for exp in results:
        worst = 0.0
        for r in exp["runs"]:
            rr = r["algebraic_residuals"]
            worst = max(worst, rr["max_abs_dd"], rr["max_abs_B_minus_BT"],
                        rr["max_rel_adjoint"], rr["max_rel_selfadjoint"],
                        rr["partition_of_unity_err"])
            for k, s in r["spectra"].items():
                er = s["max_eig_resid"]
                if er == er:  # not nan
                    worst = max(worst, er)
        names.append(exp["name"])
        vals.append(worst)
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(range(len(names)), vals)
    ax.set_yscale("log")
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names, rotation=30, ha="right", fontsize=8)
    ax.set_ylabel("max algebraic residual")
    ax.set_title("Algebraic identity residuals (log scale)")
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "residuals_summary.png"), dpi=130)
    plt.close(fig)


def make_all_plots(payload, outdir):
    pdir = os.path.join(outdir, "plots")
    os.makedirs(pdir, exist_ok=True)
    results = payload["results"]
    plot_lambda_minpos(results, pdir)
    plot_lambda_max(results, pdir)
    plot_cond_M(results, pdir)
    plot_jacobian(results, pdir)
    plot_sweeps(results, pdir)
    plot_residuals(results, pdir)
    return pdir
