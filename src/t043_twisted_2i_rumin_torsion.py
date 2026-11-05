"""T043: all nine 2I-isotypic Rumin torsion sectors."""
import argparse, json
from pathlib import Path
import mpmath as mp
import sympy as sp
from src.t032_2i_molien import IRREP_DIMENSIONS, IRREP_NUMERATORS, molien_coefficients, verify_dimension_decomposition, verify_sum_of_squares

PERIOD=60
LABELS=tuple(IRREP_NUMERATORS)

def multiplicities(label, degree):
    if label not in IRREP_DIMENSIONS: raise KeyError(label)
    return molien_coefficients(label, degree)

def eigenvalue(m,p):
    if not isinstance(m,int) or isinstance(m,bool) or m<0: raise ValueError("m >= 0 required")
    if not isinstance(p,int) or isinstance(p,bool) or not 0<=p<=m+1: raise ValueError("p outside range")
    x=m+2*p*(m-p)
    return sp.Rational(x*x,4)

def difference_polynomial(label):
    t=sp.symbols("t")
    numerator=sum(t**j for j in IRREP_NUMERATORS[label])
    A=numerator/((1-t**12)*(1-t**20))
    b0=1 if label=="1" else 0
    P=sp.Poly(sp.cancel((1-t**PERIOD)*(t**2-1)*(A-b0)),t)
    return {int(k[0]):int(v) for k,v in P.terms()}

def differences(label,max_n):
    b=multiplicities(label,max_n)
    return tuple((b[n-2] if n>=2 else 0)-b[n]-(b[0] if n==2 else 0)
                 for n in range(1,max_n+1))

def tail_data(label):
    P=difference_polynomial(label); cutoff=max(P)+1
    d=differences(label,cutoff+2*PERIOD)
    finite={n:d[n-1] for n in range(1,cutoff) if d[n-1]}
    tails={}
    for r in range(1,PERIOD+1):
        n=cutoff+(r-cutoff)%PERIOD
        if d[n-1]: tails[n]=d[n-1]
    return cutoff,P,finite,tails

def verify_sector(label):
    cutoff,P,finite,tails=tail_data(label)
    d=differences(label,cutoff+2*PERIOD)
    for n in range(1,cutoff+2*PERIOD+1):
        predicted=P.get(n,0)+P.get(n-PERIOD,0)+P.get(n-2*PERIOD,0)
        if d[n-1]!=predicted: return False
    return all(d[n-1]==d[n-PERIOD-1] for n in range(cutoff+PERIOD,cutoff+2*PERIOD+1))

def zeta0_partial(label,s,M):
    b=multiplicities(label,M); total=mp.mpf(b[0])
    for m in range(1,M+1):
        for p in range(m+1):
            lam=eigenvalue(m,p); total+=b[m]*mp.power(mp.mpf(lam.p)/lam.q,-s)
    return total

def zeta1_partial(label,s,M):
    b=multiplicities(label,M); total=mp.mpf(0)
    for m in range(M+1):
        for p in range(1,m+2):
            lam=eigenvalue(m,p); total+=2*b[m]*mp.power(mp.mpf(lam.p)/lam.q,-s)
    return total

def kappa_direct_partial(label,s,M):
    return -2*zeta0_partial(label,s,M)+zeta1_partial(label,s,M)

def kappa_boundary_partial(label,s,M):
    b=multiplicities(label,M)
    return 2*sum(b[m]*(mp.power((m+2)**2/4,-s)-mp.power(m**2/4,-s)) for m in range(1,M+1))

def log_torsion(label,dps=50):
    if not isinstance(dps,int) or isinstance(dps,bool) or dps<20: raise ValueError("dps >= 20 required")
    _,_,finite,tails=tail_data(label)
    with mp.workdps(dps):
        value=mp.fsum(c*(mp.log(4)-2*mp.log(n)) for n,c in finite.items())
        for n,c in tails.items():
            a=mp.mpf(n)/PERIOD
            value+=c*((mp.log(4)-2*mp.log(PERIOD))*(mp.mpf("0.5")-a)
                      +2*mp.loggamma(a)-mp.log(2*mp.pi))
        return +value

def audit(max_degree=100,dps=50):
    if max_degree<60: raise ValueError("max_degree >= 60 required")
    if not verify_sum_of_squares(): raise AssertionError("irrep dimensions do not sum to 120")
    if not verify_dimension_decomposition(max_degree): raise AssertionError("dimension decomposition failed")
    sectors={}
    with mp.workdps(dps):
        for label in LABELS:
            if not verify_sector(label): raise AssertionError("periodic polynomial check failed: "+label)
            lt=log_torsion(label,dps)
            cutoff,P,finite,tails=tail_data(label)
            sectors[label]={
              "dimension":IRREP_DIMENSIONS[label],
              "molien_numerator_degrees":list(IRREP_NUMERATORS[label]),
              "tail_cutoff":cutoff,
              "difference_polynomial":[{"degree":n,"coefficient":c} for n,c in sorted(P.items())],
              "finite_dirichlet_terms":[{"n":n,"coefficient":c} for n,c in finite.items()],
              "hurwitz_tail_terms":[{"first_n":n,"coefficient":c,"argument":f"{n}/60"} for n,c in tails.items()],
              "log_torsion":mp.nstr(lt,dps),"torsion":mp.nstr(mp.exp(lt),dps)
            }
        regular_log=mp.fsum(IRREP_DIMENSIONS[k]*mp.mpf(sectors[k]["log_torsion"]) for k in LABELS)
        regular=mp.exp(regular_log); cover=16*mp.pi**2
    return {
      "task":"T043","passed":True,"group_order":120,"irreducible_sector_count":9,
      "sum_squared_dimensions":sum(d*d for d in IRREP_DIMENSIONS.values()),
      "dimension_decomposition_verified_through_degree":max_degree,
      "eigenvalue":"Lambda_m(p)=(m+2*p*(m-p))^2/4",
      "multiplicity":"b_(m,rho)=[t^m]N_rho(t)/((1-t^12)(1-t^20))",
      "zeta0":"b_(0,rho)+sum_(m>=1)b_(m,rho)*sum_(p=0)^m Lambda_m(p)^(-s)",
      "zeta1":"2*sum_(m>=0)b_(m,rho)*sum_(p=1)^(m+1)Lambda_m(p)^(-s)",
      "kappa":"-2*zeta0+zeta1=2*4^s*sum_(n>=1)d_(n,rho)*n^(-2s)",
      "initial_convergence":"Re(s)>1",
      "sectors":sectors,
      "regular_representation_check":{
        "decomposition":"regular representation = direct sum of dim(rho) copies of each rho",
        "weighted_log_torsion":mp.nstr(regular_log,dps),
        "weighted_torsion":mp.nstr(regular,dps),
        "covering_sphere_volume_16pi2":mp.nstr(cover,dps),
        "absolute_residual":mp.nstr(abs(regular-cover),8),
        "status":"high-precision consistency check"
      },
      "scope":{
        "exact":["nine Molien-isotypic series","nine rational difference generating functions","interior cancellation in every sector","finite Hurwitz continuation and Gamma-product formula in each sector"],
        "numerical":["sector torsion values","regular-representation weighted product versus 16*pi^2"],
        "not_claimed":["separate zeta0 and zeta1 continuations","non-flat or non-unitary coefficients","independent reconstruction of the T032 character table"]
      }
    }

def main():
    p=argparse.ArgumentParser(); p.add_argument("--max-degree",type=int,default=100); p.add_argument("--dps",type=int,default=50); p.add_argument("--output",default="data/t043_twisted_2i_rumin_torsion.json"); a=p.parse_args()
    report=audit(a.max_degree,a.dps); path=Path(a.output); path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"task":report["task"],"passed":True,"torsions":{k:v["torsion"] for k,v in report["sectors"].items()},"regular":report["regular_representation_check"]},indent=2))
if __name__=="__main__": main()
