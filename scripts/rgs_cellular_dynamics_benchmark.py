#!/usr/bin/env python3
"""RGS Cellular Dynamics Benchmark v0.1.

Synchronous binary cellular automata on periodic Moore lattices, Q6, and
PRISM = C64 x C6 x C6 x C6 x C5. This is a computational benchmark scaffold,
not a physical model. Randomness is seeded and neighbour ordering explicit.
"""
from __future__ import annotations
import argparse, json, math, platform, time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
import numpy as np

@dataclass(frozen=True)
class Graph:
    name: str
    neighbours: np.ndarray
    metadata: dict
    @property
    def n(self): return int(self.neighbours.shape[0])
    @property
    def degree(self): return int(self.neighbours.shape[1])

def cycle_product_graph(lengths: tuple[int, ...], name: str) -> Graph:
    n=math.prod(lengths)
    coords=np.indices(lengths,dtype=np.int64).reshape(len(lengths),-1).T
    strides=np.array([math.prod(lengths[i+1:]) for i in range(len(lengths))],dtype=np.int64)
    nb=np.empty((n,2*len(lengths)),dtype=np.int64)
    for v,c in enumerate(coords):
        k=0
        for axis,L in enumerate(lengths):
            for delta in (-1,1):
                cc=c.copy(); cc[axis]=(cc[axis]+delta)%L
                nb[v,k]=int(np.dot(cc,strides)); k+=1
    return Graph(name,nb,{"factor_lengths":list(lengths),"degree":2*len(lengths),"node_count":n})

def q6_graph() -> Graph:
    nb=np.empty((64,6),dtype=np.int64)
    for v in range(64):
        for bit in range(6): nb[v,bit]=v^(1<<bit)
    return Graph("Q6",nb,{"node_count":64,"degree":6,"edges":192})

def square_moore_graph(side:int) -> Graph:
    offsets=[(dy,dx) for dy in (-1,0,1) for dx in (-1,0,1) if (dy,dx)!=(0,0)]
    nb=np.empty((side*side,8),dtype=np.int64)
    for y in range(side):
        for x in range(side):
            v=y*side+x
            for k,(dy,dx) in enumerate(offsets): nb[v,k]=((y+dy)%side)*side+(x+dx)%side
    return Graph(f"Moore_{side}x{side}",nb,{"side":side,"boundary":"periodic","degree":8})

def totalistic_table(rng:np.random.Generator,degree:int)->np.ndarray:
    return rng.integers(0,2,size=(2,degree+1),dtype=np.uint8)

def ordered_table(rng:np.random.Generator,degree:int)->np.ndarray:
    return rng.integers(0,2,size=(1<<(degree+1),),dtype=np.uint8)

def update(state:np.ndarray,graph:Graph,rule:np.ndarray,kind:str)->np.ndarray:
    neigh=state[graph.neighbours]
    if kind=="totalistic":
        return rule[state.astype(np.int64),neigh.sum(axis=1,dtype=np.int64)].astype(np.uint8)
    if kind=="ordered":
        idx=state.astype(np.int64).copy()
        for j in range(graph.degree): idx|=(neigh[:,j].astype(np.int64)<<(j+1))
        return rule[idx].astype(np.uint8)
    raise ValueError(f"Unknown rule kind: {kind}")

def orbit_symmetry_score(state:np.ndarray,graph:Graph)->float:
    if graph.name!="Q6": return float("nan")
    scores=[]
    for shift in range(1,6):
        perm=np.array([sum(((v>>b)&1)<<((b+shift)%6) for b in range(6)) for v in range(64)])
        scores.append(float(np.mean(state==state[perm])))
    return float(np.mean(scores))

def run_trajectory(graph:Graph,rule:np.ndarray,kind:str,seed:int,steps:int,initial_density:float=.35)->dict:
    rng=np.random.default_rng(seed)
    state=(rng.random(graph.n)<initial_density).astype(np.uint8)
    densities=[]; activity=[]
    for _ in range(steps):
        nxt=update(state,graph,rule,kind)
        densities.append(float(nxt.mean())); activity.append(float(np.mean(nxt!=state))); state=nxt
    tail=np.asarray(activity[-min(20,len(activity)):],dtype=float)
    return {"seed":seed,"steps":steps,"initial_density":initial_density,"final_density":float(state.mean()),
      "mean_density":float(np.mean(densities)) if densities else float(state.mean()),
      "mean_activity":float(np.mean(activity)) if activity else 0.0,
      "tail_activity_mean":float(tail.mean()) if tail.size else 0.0,
      "tail_activity_std":float(tail.std()) if tail.size else 0.0,
      "density_trace":densities,"activity_trace":activity,"symmetry_proxy":orbit_symmetry_score(state,graph)}

def aggregate(records:list[dict])->dict:
    keys=["final_density","mean_density","mean_activity","tail_activity_mean","tail_activity_std"]
    out={"n_seeds":len(records)}
    for k in keys:
        vals=np.asarray([r[k] for r in records],dtype=float)
        out[k+"_mean"]=float(np.nanmean(vals))
        out[k+"_sd"]=float(np.nanstd(vals,ddof=1)) if len(vals)>1 else 0.0
    return out

def benchmark(model:str,steps:int,seeds:Iterable[int],quick:bool=False)->dict:
    seeds=list(seeds); master=np.random.default_rng(20261105)
    if model=="moore": graph=square_moore_graph(17 if quick else 89); degree=8
    elif model=="q6": graph=q6_graph(); degree=6
    elif model=="prism": graph=cycle_product_graph((64,6,6,6,5),"PRISM_C64xC6^3xC5"); degree=10
    else: raise ValueError(model)
    rules={"totalistic":totalistic_table(master,degree),"ordered":ordered_table(master,degree)}
    results={}
    for kind,rule in rules.items():
        rec=[run_trajectory(graph,rule,kind,int(s),steps) for s in seeds]
        results[kind]={"rule_bits":int(rule.size),"rule":rule.astype(int).tolist(),"aggregate":aggregate(rec),"runs":rec}
    return {"schema":"rgs-ca-benchmark-v0.1","timestamp_utc":None,"python":platform.python_version(),
      "numpy":np.__version__,"model":model,"graph":graph.metadata|{"name":graph.name},"steps":steps,
      "seeds":[int(s) for s in seeds],"results":results,
      "limitations":["One random rule per family: smoke benchmark only, not evolutionary search.",
      "Ordered rules depend on declared neighbour ordering.","Symmetry proxy is only a partial Q6 diagnostic, not the full automorphism group.",
      "No Hodge or spectral fitness is included in v0.1."]}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--model",choices=["moore","q6","prism"],default="q6")
    p.add_argument("--steps",type=int,default=100); p.add_argument("--seeds",type=int,nargs="+",default=[0,1,2,3,4])
    p.add_argument("--quick",action="store_true"); p.add_argument("--output",default="rgs_ca_results.json")
    a=p.parse_args()
    if a.quick: a.steps=min(a.steps,20); a.seeds=[0,1]
    t=time.time(); report=benchmark(a.model,a.steps,a.seeds,a.quick); report["runtime_seconds"]=time.time()-t
    Path(a.output).write_text(json.dumps(report,indent=2,allow_nan=True)+"\n",encoding="utf-8")
    print(json.dumps({"output":a.output,"model":a.model,"runtime_seconds":report["runtime_seconds"],
      "summary":{k:v["aggregate"] for k,v in report["results"].items()}},indent=2))
if __name__=="__main__": main()
