"""Increasing-harmonic Galerkin audit for the golden cumulative Markov operator."""
from bisect import bisect_right
from math import cos, pi, sin, sqrt
import argparse, json, random
PHI=(1.0+sqrt(5.0))/2.0
LAMBDA=1.0/PHI

def fourier_basis(t, h):
    out=[sqrt(2)*cos(2*pi*t),sqrt(2)*sin(2*pi*t),1.0]
    for k in range(2,h+1):
        out.extend((sqrt(2)*cos(2*pi*k*t),sqrt(2)*sin(2*pi*k*t)))
    return out

def estimate_compression(samples=30000, terms=48, max_harmonic=8, seed=20261124):
    if samples<1000 or terms<1 or max_harmonic<2: raise ValueError("invalid audit parameters")
    rng=random.Random(seed); powers=[LAMBDA**k for k in range(terms)]
    xs=sorted(sum(w if rng.getrandbits(1) else -w for w in powers) for _ in range(samples))
    dim=2*max_harmonic+1; a=[[0.0]*dim for _ in range(dim)]; inv=1.0/samples
    for ix,x in enumerate(xs):
        t=(ix+0.5)*inv
        tm=bisect_right(xs,LAMBDA*x-1.0)*inv
        tp=bisect_right(xs,LAMBDA*x+1.0)*inv
        src=fourier_basis(t,max_harmonic)
        lm=fourier_basis(tm,max_harmonic); rp=fourier_basis(tp,max_harmonic)
        dst=[(u+v)*0.5 for u,v in zip(lm,rp)]
        for i in range(dim):
            si=src[i]*inv; row=a[i]
            for j in range(dim): row[j]+=si*dst[j]
    return a

def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def frobenius(a): return sqrt(sum(x*x for row in a for x in row))
def power_norms(b,d,c,count=8):
    cur=[r[:] for r in c]; out={}
    for n in range(count):
        out[str(n)]=frobenius(matmul(b,cur)); cur=matmul(d,cur)
    return out
def power_radius_estimate(d,iterations=300):
    n=len(d); v=[1.0/sqrt(n)]*n; est=0.0
    for _ in range(iterations):
        w=[sum(d[i][j]*v[j] for j in range(n)) for i in range(n)]
        est=sqrt(sum(x*x for x in w))
        if est==0: return 0.0
        v=[x/est for x in w]
    return est
def reduce_matrix(matrix,h):
    dim=2*h+1
    if len(matrix)<dim or any(len(r)<dim for r in matrix[:dim]): raise ValueError("matrix too small")
    active=[0,1]; comp=list(range(3,dim))
    def block(rows,cols): return [[matrix[i][j] for j in cols] for i in rows]
    a,b,c,d=block(active,active),block(active,comp),block(comp,active),block(comp,comp)
    k0=matmul(b,c)
    return {"harmonic_cutoff":h,"active_dimension":2,"constant_mode":"removed_exactly",
            "complement_dimension":len(comp),"A11":a,"B":b,"C":c,"D":d,
            "K0":k0,"K0_frobenius":frobenius(k0),
            "memory_kernel_frobenius":power_norms(b,d,c),
            "D_power_radius_estimate":power_radius_estimate(d),
            "scope":"finite empirical-CDF Galerkin estimate; not exact L2"}
def audit(samples=30000,terms=48,cutoffs=(2,3,4,6,8),seed=20261124):
    matrix=estimate_compression(samples,terms,max(cutoffs),seed)
    return {"model":"increasing-harmonic finite Galerkin audit","samples":samples,
            "bernoulli_terms":terms,"seed":seed,"cutoffs":list(cutoffs),
            "cdf_series_tail_bound":LAMBDA**terms/(1-LAMBDA),
            "full_compression_dimension":len(matrix),
            "records":[reduce_matrix(matrix,h) for h in cutoffs],
            "warning":"Empirical-CDF/sampling errors remain; power estimate is not a certified spectral-radius bound. No convergence is asserted."}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--samples",type=int,default=30000); p.add_argument("--terms",type=int,default=48)
    p.add_argument("--cutoffs",type=int,nargs="+",default=[2,3,4,6,8])
    p.add_argument("--seed",type=int,default=20261124)
    p.add_argument("--output",default="results/tsmr_i_harmonic_convergence.json")
    x=p.parse_args(); result=audit(x.samples,x.terms,tuple(x.cutoffs),x.seed)
    with open(x.output,"w",encoding="utf-8") as f: json.dump(result,f,indent=2); f.write("\n")
    print(json.dumps(result,indent=2))
