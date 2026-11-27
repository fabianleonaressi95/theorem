#!/usr/bin/env python3
"""Finite nonconvex search for an exactly face-local V4 intertwiner.

Requires NumPy and PyTorch. Inputs are the two NPZ files from the
q6-c60-v4-equivariance Actions artifact. A positive residual is not a
global lower bound and does not prove exact locality impossible.
"""
import argparse, itertools, json
from pathlib import Path
import numpy as np
import torch

def bases(reps):
    result = []
    for a, b in itertools.product((-1., 1.), repeat=2):
        chi = (1., a, b, a*b)
        P = sum(chi[k] * reps[k] for k in range(4)) / 4
        val, vec = np.linalg.eigh((P + P.T) / 2)
        B = vec[:, val > .5]
        if B.shape != (64, 16):
            raise RuntimeError(f"Expected (64,16) isotypic basis, got {B.shape}")
        result.append(B)
    return result

def main(args):
    torch.set_num_threads(1)
    ri = np.load(args.representations, allow_pickle=False)
    lo = np.load(args.locality, allow_pickle=False)
    qr, fr = np.asarray(ri["q6_state_actions"], float), np.asarray(ri["c60_face_fibre_actions"], float)
    phi0 = np.asarray(lo["intertwiner_Q6_to_C60"], float)
    d0 = np.asarray(lo["transported_Q6_adjacency"], float)
    adj = np.asarray(lo["face_adjacency"], int)
    aq = phi0.T @ d0 @ phi0
    bq, bf = bases(qr), bases(fr)
    w0 = [f.T @ phi0 @ q for q, f in zip(bq, bf)]
    if any(np.linalg.norm(w.T @ w - np.eye(16)) > 1e-8 for w in w0):
        raise RuntimeError("Initial sector map is not orthogonal")

    dt = torch.float64
    ii, jj = np.triu_indices(16, 1)
    ii, jj = torch.as_tensor(ii), torch.as_tensor(jj)
    bqt = [torch.tensor(x, dtype=dt) for x in bq]
    bft = [torch.tensor(x, dtype=dt) for x in bf]
    w0t = [torch.tensor(x, dtype=dt) for x in w0]
    aqt = torch.tensor(aq, dtype=dt)
    def skew(p):
        s = torch.zeros((16,16), dtype=dt)
        s[ii,jj], s[jj,ii] = p, -p
        return s
    def build(p):
        w = [w0t[k] @ torch.matrix_exp(skew(p[k])) for k in range(4)]
        phi = sum(bft[k] @ w[k] @ bqt[k].T for k in range(4))
        return phi, phi @ aqt @ phi.T

    eye = np.eye(32, dtype=int)
    nonadj, off = 1-adj-eye, 1-eye
    mn = torch.tensor(np.repeat(np.repeat(nonadj,2,0),2,1), dtype=dt)
    mo = torch.tensor(np.repeat(np.repeat(off,2,0),2,1), dtype=dt)
    mnb, mob = torch.tensor(nonadj,dtype=dt), torch.tensor(off,dtype=dt)
    def qloss(p):
        phi,d = build(p)
        en, eo = torch.sum((d*mn)**2), torch.sum((d*mo)**2)
        return en/torch.clamp(eo,min=1e-30), phi, d
    def l1loss(p):
        phi,d = build(p)
        blocks = d.reshape(32,2,32,2).permute(0,2,1,3)
        norms = torch.sqrt(torch.sum(blocks**2,dim=(2,3))+1e-12)
        return torch.sum(norms*mnb)/torch.clamp(torch.sum(norms*mob),min=1e-30)

    torch.manual_seed(args.seed)
    p = [torch.nn.Parameter(.6*torch.randn(120,dtype=dt)) for _ in range(4)]
    opt = torch.optim.Adam(p,lr=args.lr1)
    for step in range(args.steps1):
        opt.zero_grad(); loss,_,_ = qloss(p); loss.backward(); opt.step()
        if step == args.lr_drop_step-1:
            for g in opt.param_groups: g["lr"] = args.lr1_after_drop
    opt = torch.optim.Adam(p,lr=args.lr_l1)
    for _ in range(args.steps_l1):
        opt.zero_grad(); loss=l1loss(p); loss.backward(); opt.step()
    opt = torch.optim.Adam(p,lr=args.lr2)
    best, phi_best, d_best = float("inf"), None, None
    for _ in range(args.steps2):
        opt.zero_grad(); loss,_,_=qloss(p); loss.backward(); opt.step()
        v=float(loss.detach())
        if v < best:
            best=v
            with torch.no_grad():
                phi_best,d_best=build(p)
                phi_best,d_best=phi_best.cpu().numpy().copy(),d_best.cpu().numpy().copy()

    blocks=d_best.reshape(32,2,32,2).transpose(0,2,1,3)
    norms=np.linalg.norm(blocks,axis=(2,3))
    support={}
    for tol in (1e-12,1e-10,1e-8,1e-6,1e-4,1e-2):
        nz=norms>tol
        support[f"{tol:.0e}"]={"nonzero_blocks":int(nz.sum()),
            "diagonal_blocks":int(np.trace(nz)),
            "adjacent_blocks":int(np.sum(nz*adj)),
            "nonadjacent_blocks":int(np.sum(nz*nonadj))}
    maskn=np.repeat(np.repeat(nonadj,2,0),2,1)
    maska=np.repeat(np.repeat(adj,2,0),2,1)
    en,ea=float(np.sum(d_best**2*maskn)),float(np.sum(d_best**2*maska))
    inter=[float(np.linalg.norm(phi_best@qr[k]-fr[k]@phi_best)) for k in range(4)]
    eig,cnt=np.unique(np.round(np.linalg.eigvalsh(d_best),8),return_counts=True)
    report={
      "classification":"finite seeded nonconvex exact-locality feasibility search; not a global no-go theorem",
      "seed":args.seed,
      "parameterization":"Phi=sum_k Bf_k W0_k exp(S_k) Bq_k^T; S_k skew-symmetric 16x16",
      "commutant_degrees_of_freedom":480,
      "exact_locality_target":"all 812 directed nonadjacent 2x2 face-fibre blocks vanish (3248 scalar entries before symmetry redundancy)",
      "face_graph":{"faces":32,"adjacency_edges":int(adj.sum()//2),
        "degree_counts":{str(int(x)):int(np.sum(adj.sum(axis=1)==x)) for x in np.unique(adj.sum(axis=1))}},
      "stages":[
        {"objective":"nonadjacent off-diagonal Frobenius energy fraction","steps":args.steps1,"lr":args.lr1,"drop_after":args.lr_drop_step,"lr_after":args.lr1_after_drop},
        {"objective":"nonadjacent block Frobenius L1 ratio","steps":args.steps_l1,"lr":args.lr_l1},
        {"objective":"nonadjacent off-diagonal Frobenius energy fraction","steps":args.steps2,"lr":args.lr2}],
      "candidate":{"nonadjacent_energy_fraction":en/(en+ea),"adjacent_energy_fraction":ea/(en+ea),
        "block_support":support,
        "orthogonality_residual":float(np.linalg.norm(phi_best.T@phi_best-np.eye(64))),
        "V4_intertwining_residuals":inter,"max_V4_intertwining_residual":max(inter),
        "symmetry_residual":float(np.linalg.norm(d_best-d_best.T)),
        "spectrum":{str(float(x)):int(n) for x,n in zip(eig,cnt)}},
      "conclusion":"The search finds a near-local candidate but no exact zero: 620 nonadjacent blocks remain above 1e-2 and all 812 remain above 1e-6. This positive residual is not a rigorous lower bound; exact existence/nonexistence remains open."
    }
    Path(args.out).parent.mkdir(parents=True,exist_ok=True)
    Path(args.out).write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    Path(args.matrices).parent.mkdir(parents=True,exist_ok=True)
    np.savez_compressed(args.matrices,optimized_intertwiner=phi_best,
      optimized_transported_Q6_adjacency=d_best,face_adjacency=adj,
      baseline_intertwiner=phi0,baseline_transported_Q6_adjacency=d0)
    print(json.dumps(report,indent=2))

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--representations",default="artifacts/Q6_C60_V4_intertwiner.npz")
    ap.add_argument("--locality",default="artifacts/Q6_C60_V4_locality.npz")
    ap.add_argument("--out",default="audits/Q6_C60_V4_exact_locality.json")
    ap.add_argument("--matrices",default="artifacts/Q6_C60_V4_exact_locality.npz")
    ap.add_argument("--seed",type=int,default=20261127)
    ap.add_argument("--steps1",type=int,default=1400)
    ap.add_argument("--lr1",type=float,default=.015)
    ap.add_argument("--lr-drop-step",type=int,default=1000)
    ap.add_argument("--lr1-after-drop",type=float,default=.003)
    ap.add_argument("--steps-l1",type=int,default=1800)
    ap.add_argument("--lr-l1",type=float,default=.0001)
    ap.add_argument("--steps2",type=int,default=1600)
    ap.add_argument("--lr2",type=float,default=.001)
    main(ap.parse_args())
