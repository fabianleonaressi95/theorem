#!/usr/bin/env python3
"""Graph-resolved axial-spin correlator on Q6 and PRISM.

NPZ: a_values (T,), spin_vectors (T,N,3) or (T,R,N,3), volumes (T,),
optional particle_counts (T,) or (T,R). A zero vector can represent a vacant
site. The graph supplies topology only, not a spin Hamiltonian or measure.
"""
from __future__ import annotations
import argparse, itertools, json, math
import numpy as np
Q6_DIMS=(2,2,2,2,2,2)
PRISM_DIMS=(64,6,6,6,5)

def offsets(dims, radius):
    if radius < 0: raise ValueError("radius must be non-negative")
    for d in itertools.product(*(range(L) for L in dims)):
        r=sum(min(x,L-x) for x,L in zip(d,dims))
        if r<=radius: yield d,r

def shell_correlations(spins,dims,max_distance):
    N=math.prod(dims)
    if np.shape(spins)!=(N,3): raise ValueError(f"spins must have shape ({N},3)")
    f=np.asarray(spins,float).reshape(*dims,3)
    if not np.isfinite(f).all(): raise ValueError("non-finite spin")
    fc=f-f.mean(axis=tuple(range(len(dims))),keepdims=True)
    raw=np.zeros(max_distance+1); conn=np.zeros(max_distance+1)
    count=np.zeros(max_distance+1,dtype=np.int64); axes=tuple(range(len(dims)))
    for d,r in offsets(dims,max_distance):
        sh=np.roll(f,tuple(-x for x in d),axis=axes)
        shc=np.roll(fc,tuple(-x for x in d),axis=axes)
        raw[r]+=np.sum(f*sh); conn[r]+=np.sum(fc*shc); count[r]+=N
    return {"mean_spin_vector":f.mean(axis=tuple(range(len(dims)))).tolist(),
            "shells":[{"distance":r,"directed_pair_count":int(count[r]),
                       "raw_dot_mean":float(raw[r]/count[r]),
                       "connected_dot_mean":float(conn[r]/count[r])}
                      for r in range(max_distance+1) if count[r]]}

def invariant_decomposition(spins,volume):
    s=np.asarray(spins,float)
    if s.ndim!=2 or s.shape[1]!=3 or not np.isfinite(s).all():
        raise ValueError("spins must be finite with shape (N,3)")
    V=float(volume)
    if not math.isfinite(V) or V<=0: raise ValueError("volume must be positive finite")
    total=s.sum(axis=0); self_num=float(np.sum(s*s)); total_num=float(total@total)
    self_term=self_num/V**2; pair=(total_num-self_num)/V**2; s2=total_num/V**2
    return {"s2_total":s2,"s2_self":self_term,"s2_distinct_pair":pair,
            "decomposition_residual":s2-self_term-pair,
            "mean_current_density":(total/V).tolist()}

def fit_q(a,y):
    a=np.asarray(a,float); y=np.asarray(y,float)
    m=np.isfinite(a)&np.isfinite(y)&(a>0)&(y>0)
    if m.sum()<2: return {"q":None,"points_used":int(m.sum()),"reason":"need >=2 positive samples"}
    x=np.log(a[m]); z=np.log(y[m]); slope,intercept=np.polyfit(x,z,1)
    ssr=float(np.sum((z-(slope*x+intercept))**2)); sst=float(np.sum((z-z.mean())**2))
    return {"q":float(-slope),"log_intercept":float(intercept),
            "r_squared_log_fit":(1.0 if sst==0 and ssr==0 else (None if sst==0 else 1-ssr/sst)),
            "points_used":int(m.sum())}

def _mean_corr(corrs):
    out=[]
    for i,row in enumerate(corrs[0]["shells"]):
        out.append({"distance":row["distance"],"directed_pair_count":row["directed_pair_count"],
          "raw_dot_mean":float(np.mean([c["shells"][i]["raw_dot_mean"] for c in corrs])),
          "connected_dot_mean":float(np.mean([c["shells"][i]["connected_dot_mean"] for c in corrs]))})
    return {"mean_spin_vector":np.mean([c["mean_spin_vector"] for c in corrs],axis=0).tolist(),"shells":out}

def audit_snapshots(a_values,spin_vectors,volumes,dims,particle_counts=None,max_distance=3):
    a=np.asarray(a_values,float); x=np.asarray(spin_vectors,float); V=np.asarray(volumes,float)
    if x.ndim==3 and x.shape[-1]==3: x=x[:,None,:,:]
    if x.ndim!=4 or x.shape[-1]!=3: raise ValueError("spin_vectors shape must be (T,N,3) or (T,R,N,3)")
    T,R,N,_=x.shape
    if N!=math.prod(dims): raise ValueError("spin-vector node count does not match geometry")
    if a.shape!=(T,) or V.shape!=(T,) or not np.isfinite(a).all() or np.any(a<=0): raise ValueError("invalid a_values/volumes shape or scale factor")
    if not np.isfinite(V).all() or np.any(V<=0) or not np.isfinite(x).all(): raise ValueError("non-finite spins or invalid volume")
    if particle_counts is None:
        counts=np.full((T,R),N,float); count_note="assumed one carrier per site"
    else:
        counts=np.asarray(particle_counts,float)
        if counts.shape==(T,): counts=np.repeat(counts[:,None],R,axis=1)
        if counts.shape!=(T,R) or not np.isfinite(counts).all() or np.any(counts<0): raise ValueError("particle_counts shape/value invalid")
        count_note="supplied carrier counts"
    rows=[]
    for t in range(T):
        dec=[invariant_decomposition(x[t,r],V[t]) for r in range(R)]
        avg=lambda key:float(np.mean([d[key] for d in dec]))
        n=float(np.mean(counts[t]/V[t]))
        rows.append({"a":float(a[t]),"volume":float(V[t]),"number_density":n,"ensemble_size":R,
          "s2_total":avg("s2_total"),"s2_self":avg("s2_self"),"s2_distinct_pair":avg("s2_distinct_pair"),
          "decomposition_residual":avg("decomposition_residual"),
          "mean_current_density":np.mean([d["mean_current_density"] for d in dec],axis=0).tolist(),
          "pair_g_effective":avg("s2_distinct_pair")/n**2 if n>0 else None,
          "correlation":_mean_corr([shell_correlations(x[t,r],dims,max_distance) for r in range(R)])})
    rows.sort(key=lambda z:z["a"]); aa=[z["a"] for z in rows]
    return {"schema":"q6-prism-microscopic-spin-correlator/v1",
      "geometry":{"name":"Q6" if dims==Q6_DIMS else ("PRISM" if dims==PRISM_DIMS else "custom"),
                  "dims":list(dims),"vertices":N,"metric":"sum of shortest cyclic coordinate distances"},
      "assumptions":{"spin":"vertex axial 3-vectors; zero may encode vacancy",
        "carrier_count":count_note,"invariant":"ensemble mean |sum_i s_i/V|^2 = 1/2 S_ij S_ij",
        "contact":"no quantum contact renormalization/subtraction performed"},
      "snapshots":rows,"scaling_fits":{
        "q_total":fit_q(aa,[z["s2_total"] for z in rows]),
        "q_self":fit_q(aa,[z["s2_self"] for z in rows]),
        "q_pair":fit_q(aa,[z["s2_distinct_pair"] for z in rows]),
        "q_density":fit_q(aa,[z["number_density"] for z in rows])},
      "checks":{"decomposition_identity":all(abs(z["decomposition_residual"])<1e-10*max(1,z["s2_total"]) for z in rows),
                "all_finite":bool(np.isfinite(x).all())},
      "limitations":["Topology does not determine spin dynamics or an equilibrium measure.",
        "Finite graph fits do not establish a cosmological or continuum exponent.",
        "The pair term can be negative; log fits use positive values only.",
        "EC local four-fermion contact requires a specified quantum ordering/renormalization prescription.",
        "If spin lives on edges/faces, use an oriented cochain correlator and gauge transport."]}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",required=True); p.add_argument("--geometry",choices=("q6","prism"),required=True)
    p.add_argument("--max-distance",type=int,default=3); p.add_argument("--output",default="")
    args=p.parse_args(); dims=Q6_DIMS if args.geometry=="q6" else PRISM_DIMS
    with np.load(args.input,allow_pickle=False) as z:
        missing={"a_values","spin_vectors","volumes"}-set(z.files)
        if missing: p.error("missing NPZ keys: "+", ".join(sorted(missing)))
        report=audit_snapshots(z["a_values"],z["spin_vectors"],z["volumes"],dims,
                               z["particle_counts"] if "particle_counts" in z.files else None,args.max_distance)
    rendered=json.dumps(report,indent=2,sort_keys=True)
    if args.output:
        with open(args.output,"w",encoding="utf-8") as f:f.write(rendered+"\n")
    print(rendered)
    if not all(report["checks"].values()): raise SystemExit(1)

if __name__=="__main__": main()
