#!/usr/bin/env python3
"""Assemble independent Morandotti T134 FEM shards and run global statistics."""
from __future__ import annotations
import argparse, gzip, hashlib, json, shutil
from pathlib import Path
from scripts.audit_morandotti_curved_p3_trace_constant import statistical_model_audit

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--shards",default="shards")
    p.add_argument("--out",default="artifacts/morandotti_trace_constant")
    p.add_argument("--bootstrap-replicates",type=int,default=2000)
    a=p.parse_args()
    root,out=Path(a.shards),Path(a.out); out.mkdir(parents=True,exist_ok=True)
    reports=sorted(root.glob("morandotti-t134-case-*/report.json"))
    expected={(d,h,s) for d in (0.48,0.56) for h in (0.08,0.045) for s in (11,29,47)}
    if len(reports)!=len(expected): raise SystemExit(f"expected {len(expected)} reports, found {len(reports)}")
    runs=[]; seen=set(); cert_paths=[]
    for path in reports:
        data=json.loads(path.read_text())
        if not data.get("partial_shard"): raise SystemExit(f"{path}: not a partial shard")
        if len(data.get("runs",[]))!=1: raise SystemExit(f"{path}: expected exactly one FEM run")
        row=data["runs"][0]; key=(float(row["distance"]),float(row["h_target"]),int(row["mesh_seed"]))
        if key not in expected or key in seen: raise SystemExit(f"unexpected/duplicate shard key {key}")
        seen.add(key); runs.append(row)
        cert=path.parent/"cell-certificates.jsonl.gz"
        if not cert.exists(): raise SystemExit(f"missing exact geometry archive: {cert}")
        cert_paths.append(cert)
    if seen!=expected: raise SystemExit(f"incomplete sweep: missing {sorted(expected-seen)}")
    runs.sort(key=lambda r:(r["distance"],r["h_target"],r["mesh_seed"]))
    distances=[0.48,0.56]; mesh_sizes=[0.08,0.045]; seeds=[11,29,47]
    grouped={}
    import numpy as np
    for d in distances:
      for h in mesh_sizes:
        sample=[r for r in runs if r["distance"]==d and r["h_target"]==h]
        vals=[r["quadrature_estimates"][-1]["C_tr_h"] for r in sample]
        grouped[f"d{d:.4f}_h{h:.4f}"]={
          "realizations":len(sample),"seeds":sorted(r["mesh_seed"] for r in sample),
          "C_tr_h_max_over_seeds":float(max(vals)),
          "C_tr_h_mean_over_seeds":float(np.mean(vals)),
          "C_tr_h_sample_std_over_seeds":float(np.std(vals,ddof=1)),
          "alpha_10_exceeds_twice_max_C_tr_h":bool(10.0>2.0*max(vals)),
          "alpha_40_margin_over_max_C_tr_h":float(40.0-2.0*max(vals)),
          "alpha_40_exceeds_twice_max_C_tr_h":bool(40.0>2.0*max(vals))}
    statistical=statistical_model_audit(runs,distances,mesh_sizes,a.bootstrap_replicates)
    archive=out/"cell-certificates.jsonl.gz"
    digest=hashlib.sha256()
    with archive.open("wb") as dst:
      for src in cert_paths:
        blob=src.read_bytes(); dst.write(blob); digest.update(blob)
    base=json.loads(reports[0].read_text())
    payload={k:v for k,v in base.items() if k not in ("runs","group_summary","statistical_model_audit","partial_shard","cell_certificate_archive")}
    payload.update({"partial_shard":False,"status":"complete finite-mesh sweep; not a mesh-uniform proof",
      "mesh_sizes":mesh_sizes,"distances":distances,"seeds":seeds,
      "quadrature_degrees":[24,32,40],"group_summary":grouped,
      "statistical_model_audit":statistical,"runs":runs,
      "cell_certificate_archive":{"path":str(archive),"format":"concatenated gzip JSONL streams; exact-rational per-cell records",
        "sha256":digest.hexdigest(),"source_shards":len(cert_paths)}})
    (out/"report.json").write_text(json.dumps(payload,indent=2)+"\\n")
    print(f"assembled {len(runs)} FEM realizations; {len(cert_paths)} exact cell archives")
if __name__=="__main__": main()
