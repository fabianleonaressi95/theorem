#!/usr/bin/env python3
"""Optimize V4-equivariant Q6->C60 intertwiners for face-graph locality.

Requires NumPy and PyTorch. Inputs are the two NPZ files produced by the
q6-c60-v4-equivariance GitHub Actions artifact:
  * Q6_C60_V4_intertwiner.npz
  * Q6_C60_V4_locality.npz

The optimizer searches only within the O(16)^4 commutant freedom. It reports
local numerical optima, not a proof of global optimality or exact locality.
"""
import argparse
import itertools
import json
from pathlib import Path

import numpy as np
import torch


def character_bases(reps):
    bases = []
    for sa, sb in itertools.product((-1.0, 1.0), repeat=2):
        character = np.asarray([1.0, sa, sb, sa * sb])
        P = sum(character[k] * reps[k] for k in range(4)) / 4.0
        P = (P + P.T) / 2.0
        values, vectors = np.linalg.eigh(P)
        B = vectors[:, values > 0.5]
        if B.shape[1] != 16:
            raise RuntimeError(f"Expected multiplicity 16, got {B.shape[1]}")
        bases.append(B)
    return bases


def make_skew(parameters, upper_i, upper_j, dtype):
    S = torch.zeros((16, 16), dtype=dtype)
    S[upper_i, upper_j] = parameters
    S[upper_j, upper_i] = -parameters
    return S


def block_statistics(D, face_adjacency):
    blocks = D.reshape(32, 2, 32, 2).transpose(0, 2, 1, 3)
    norms = np.linalg.norm(blocks, axis=(2, 3))
    eye = np.eye(32, dtype=np.int8)
    nonadj = 1 - face_adjacency - eye
    offdiag = 1 - eye
    Eadj = float(np.sum((D.reshape(32, 2, 32, 2).transpose(0, 2, 1, 3) ** 2)
                        * face_adjacency[:, :, None, None]))
    Enon = float(np.sum((blocks ** 2) * nonadj[:, :, None, None]))
    Ediag = float(np.sum((blocks ** 2) * eye[:, :, None, None]))
    support = {}
    for tol in (1e-12, 1e-10, 1e-8, 1e-6, 1e-4, 1e-2):
        S = norms > tol
        diag = int(np.trace(S))
        adj = int(np.sum(S * face_adjacency))
        non = int(np.sum(S * nonadj))
        support[f"{tol:.0e}"] = {
            "nonzero_2x2_blocks": int(S.sum()),
            "diagonal_blocks": diag,
            "adjacent_face_blocks": adj,
            "nonadjacent_offdiagonal_blocks": non,
            "adjacent_edge_coverage": float(adj / face_adjacency.sum()),
            "nonadjacent_fraction_of_offdiagonal_support": float(
                non / max(int(S.sum()) - diag, 1)
            ),
        }
    l1_non = float(np.sum(norms * nonadj))
    l1_off = float(np.sum(norms * offdiag))
    return {
        "block_support_thresholds": support,
        "adjacent_frobenius_energy_fraction": Eadj / max(Eadj + Enon, 1e-30),
        "nonadjacent_frobenius_energy_fraction": Enon / max(Eadj + Enon, 1e-30),
        "diagonal_face_block_energy_fraction": Ediag / max(Eadj + Enon + Ediag, 1e-30),
        "nonadjacent_block_l1_fraction": l1_non / max(l1_off, 1e-30),
        "max_block_norm": float(norms.max()),
        "median_nonadjacent_block_norm": float(np.median(norms[nonadj.astype(bool)])),
    }


def main(args):
    torch.set_num_threads(1)
    dtype = torch.float64
    zrep = np.load(args.representations, allow_pickle=False)
    zloc = np.load(args.locality, allow_pickle=False)
    qreps = np.asarray(zrep["q6_state_actions"], float)
    freps = np.asarray(zrep["c60_face_fibre_actions"], float)
    O0 = np.asarray(zloc["intertwiner_Q6_to_C60"], float)
    D0 = np.asarray(zloc["transported_Q6_adjacency"], float)
    Af = np.asarray(zloc["face_adjacency"], int)
    Aq = O0.T @ D0 @ O0

    Bq = character_bases(qreps)
    Bf = character_bases(freps)
    W0 = [bf.T @ O0 @ bq for bq, bf in zip(Bq, Bf)]
    for k, W in enumerate(W0):
        if np.linalg.norm(W.T @ W - np.eye(16)) > 1e-8:
            raise RuntimeError(f"Initial sector map {k} is not orthogonal")

    upper_i, upper_j = np.triu_indices(16, 1)
    ui = torch.as_tensor(upper_i, dtype=torch.long)
    uj = torch.as_tensor(upper_j, dtype=torch.long)
    Aqt = torch.as_tensor(Aq, dtype=dtype)
    Bqt = [torch.as_tensor(x, dtype=dtype) for x in Bq]
    Bft = [torch.as_tensor(x, dtype=dtype) for x in Bf]
    W0t = [torch.as_tensor(x, dtype=dtype) for x in W0]
    eye64 = torch.eye(64, dtype=dtype)
    nonadj_face = 1 - Af - np.eye(32, dtype=int)
    offdiag_face = 1 - np.eye(32, dtype=int)
    Mnon = torch.as_tensor(np.repeat(np.repeat(nonadj_face, 2, axis=0), 2, axis=1), dtype=dtype)
    Moff = torch.as_tensor(np.repeat(np.repeat(offdiag_face, 2, axis=0), 2, axis=1), dtype=dtype)
    Mnon_block = torch.as_tensor(nonadj_face, dtype=dtype)
    Moff_block = torch.as_tensor(offdiag_face, dtype=dtype)

    def build(params):
        Ws = [W0t[k] @ torch.matrix_exp(make_skew(params[k], ui, uj, dtype))
              for k in range(4)]
        Phi = sum(Bft[k] @ Ws[k] @ Bqt[k].T for k in range(4))
        D = Phi @ Aqt @ Phi.T
        return Phi, D

    def quadratic_objective(params):
        Phi, D = build(params)
        Enon = torch.sum((D * Mnon) ** 2)
        Eoff = torch.sum((D * Moff) ** 2)
        return Enon / torch.clamp(Eoff, min=1e-30), Enon, Eoff, Phi, D

    best = None
    restart_records = []
    for seed in range(args.restarts):
        torch.manual_seed(args.seed + seed)
        params = [torch.nn.Parameter(0.6 * torch.randn(120, dtype=dtype))
                  for _ in range(4)]
        optimizer = torch.optim.Adam(params, lr=0.015)
        for step in range(args.restart_steps):
            optimizer.zero_grad()
            objective, _, _, _, _ = quadratic_objective(params)
            objective.backward()
            optimizer.step()
            if step == 999:
                for group in optimizer.param_groups:
                    group["lr"] = 0.003
        value = float(quadratic_objective(params)[0].detach())
        restart_records.append({"seed": args.seed + seed, "nonadjacent_energy_fraction": value})
        candidate = [p.detach().clone() for p in params]
        if best is None or value < best[0]:
            best = (value, candidate)

    params = [torch.nn.Parameter(x.clone()) for x in best[1]]
    optimizer = torch.optim.Adam(params, lr=0.001)
    for _ in range(args.refine_steps):
        optimizer.zero_grad()
        objective, _, _, _, _ = quadratic_objective(params)
        objective.backward()
        optimizer.step()
    l2_value = float(quadratic_objective(params)[0].detach())

    # L1 block-norm refinement suppresses weak nonadjacent blocks. It trades a
    # small amount of squared-energy locality for a sparser thresholded pattern.
    params = [torch.nn.Parameter(p.detach().clone()) for p in params]
    optimizer = torch.optim.Adam(params, lr=0.0005)
    def l1_objective():
        Phi, D = build(params)
        blocks = D.reshape(32, 2, 32, 2).permute(0, 2, 1, 3)
        norms = torch.sqrt(torch.sum(blocks ** 2, dim=(2, 3)) + 1e-12)
        numerator = torch.sum(norms * Mnon_block)
        denominator = torch.sum(norms * Moff_block)
        return numerator / torch.clamp(denominator, min=1e-30), Phi, D
    for _ in range(args.l1_steps):
        optimizer.zero_grad()
        objective, _, _ = l1_objective()
        objective.backward()
        optimizer.step()

    l1_value, Phi_t, D_t = l1_objective()
    Phi = Phi_t.detach().cpu().numpy()
    D = D_t.detach().cpu().numpy()
    q_orth = float(np.linalg.norm(Phi.T @ Phi - np.eye(64)))
    intertwining = [float(np.linalg.norm(Phi @ qreps[k] - freps[k] @ Phi))
                    for k in range(4)]
    metrics0 = block_statistics(D0, Af)
    metrics1 = block_statistics(D, Af)
    report = {
        "classification": "numerical local optimization over the V4 intertwiner commutant; not a global-optimality proof",
        "method": {
            "parameterization": "Phi = sum_k Bf_k W0_k exp(S_k) Bq_k^T, S_k real skew-symmetric 16x16",
            "commutant_freedom": "O(16)^4",
            "quadratic_stage": {
                "objective": "nonadjacent off-diagonal face-block Frobenius energy / all off-diagonal face-block Frobenius energy",
                "random_restarts": args.restarts,
                "steps_per_restart": args.restart_steps,
                "best_restart": min(restart_records, key=lambda x: x["nonadjacent_energy_fraction"]),
                "refinement_steps": args.refine_steps,
                "best_quadratic_fraction_after_refinement": l2_value
            },
            "sparsity_stage": {
                "objective": "sum of nonadjacent 2x2 block Frobenius norms / sum of all off-diagonal 2x2 block Frobenius norms",
                "steps": args.l1_steps,
                "final_block_L1_fraction": float(l1_value.detach())
            },
            "seed": args.seed,
            "optimizer": "PyTorch Adam, CPU float64"
        },
        "baseline_deterministic_intertwiner": metrics0,
        "optimized_intertwiner": {
            **metrics1,
            "orthogonality_residual": q_orth,
            "per_element_V4_intertwining_residuals": intertwining,
            "max_V4_intertwining_residual": max(intertwining),
            "quadratic_objective_after_L2_stage": l2_value,
            "block_L1_objective_after_sparsity_stage": float(l1_value.detach())
        },
        "interpretation": (
            "Optimization substantially concentrates the transported Q6 adjacency on adjacent C60 face pairs, "
            "while preserving orthogonality and V4 intertwining to numerical precision. The result remains "
            "nonlocal: nonadjacent blocks are not exactly zero. The reported point is a local numerical optimum "
            "from finite random restarts, not a global optimum or a proof that exact locality is impossible."
        )
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    Path(args.matrices).parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(args.matrices, optimized_intertwiner=Phi,
                        optimized_transported_Q6_adjacency=D,
                        original_intertwiner=O0,
                        original_transported_Q6_adjacency=D0,
                        face_adjacency=Af,
                        sector_maps=np.stack([Bf[k].T @ Phi @ Bq[k] for k in range(4)]))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--representations", default="artifacts/Q6_C60_V4_intertwiner.npz")
    parser.add_argument("--locality", default="artifacts/Q6_C60_V4_locality.npz")
    parser.add_argument("--out", default="audits/Q6_C60_V4_locality_optimization.json")
    parser.add_argument("--matrices", default="artifacts/Q6_C60_V4_locality_optimization.npz")
    parser.add_argument("--restarts", type=int, default=8)
    parser.add_argument("--restart-steps", type=int, default=1500)
    parser.add_argument("--refine-steps", type=int, default=5000)
    parser.add_argument("--l1-steps", type=int, default=3000)
    parser.add_argument("--seed", type=int, default=100)
    main(parser.parse_args())
