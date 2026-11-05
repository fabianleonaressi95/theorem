"""T042: exact full Rumin torsion combination on S^3/2I."""
from __future__ import annotations
import argparse, json
from fractions import Fraction
from pathlib import Path
import mpmath as mp
import sympy as sp
from src.t032_2i_molien import molien_coefficients

PERIOD=60
D_SUPPORT={12:-1,14:1,20:-1,22:1,24:-1,26:1,30:-1,34:1,36:-1,38:1,40:-1,46:1,48:-1,58:1,60:-2,62:1}
P_COEFFICIENTS=dict(D_SUPPORT)

def invariant_multiplicities(max_degree):
    if not isinstance(max_degree,int) or isinstance(max_degree,bool) or max_degree<0: raise ValueError('max_degree must be nonnegative')
    return molien_coefficients('1',max_degree)

def rumin_eigenvalue(m,p):
    if not isinstance(m,int) or isinstance(m,bool) or m<0: raise ValueError('m must be nonnegative')
    if not isinstance(p,int) or isinstance(p,bool) or p<0 or p>m+1: raise ValueError('p must lie in 0,...,m+1')
    v=m+2*p*(m-p)
    return Fraction(v*v,4)

def spectral_zeta0_partial(s,max_degree):
    a=invariant_multiplicities(max_degree); total=mp.mpf(1)
    for m in range(1,max_degree+1):
        for p in range(m+1):
            lam=rumin_eigenvalue(m,p); total+=a[m]*mp.power(mp.mpf(lam.numerator)/lam.denominator,-s)
    return total

def spectral_zeta1_partial(s,max_degree):
    a=invariant_multiplicities(max_degree); total=mp.mpf(0)
    for m in range(max_degree+1):
        for p in range(1,m+2):
            lam=rumin_eigenvalue(m,p); total+=2*a[m]*mp.power(mp.mpf(lam.numerator)/lam.denominator,-s)
    return total

def kappa_direct_partial(s,max_degree):
    return -2*spectral_zeta0_partial(s,max_degree)+spectral_zeta1_partial(s,max_degree)

def kappa_boundary_partial(s,max_degree):
    a=invariant_multiplicities(max_degree); total=mp.mpf(0)
    for m in range(1,max_degree+1):
        left=rumin_eigenvalue(m,0); right=rumin_eigenvalue(m,m+1)
        lv=mp.power(mp.mpf(left.numerator)/left.denominator,-s)
        rv=mp.power(mp.mpf(right.numerator)/right.denominator,-s)
        total+=2*a[m]*(rv-lv)
    return total

def difference_coefficient(n,a):
    if not isinstance(n,int) or isinstance(n,bool) or n<3 or n>=len(a): raise ValueError('n must be >=3 and covered')
    return a[n-2]-a[n]

def verify_period_60(max_n=600):
    if max_n<63: raise ValueError('max_n must be >=63')
    a=invariant_multiplicities(max_n+60)
    return all(difference_coefficient(n+60,a)==difference_coefficient(n,a) for n in range(3,max_n+1))

def verify_generating_function_identity():
    t=sp.symbols('t'); A=(1+t**30)/((1-t**12)*(1-t**20))
    D=(t**2-1)*A+1-t**2; P=sum(c*t**n for n,c in P_COEFFICIENTS.items())
    return sp.cancel((1-t**60)*D-P)==0

def finite_hurwitz_data():
    moment=sum((Fraction(d)*(Fraction(1,2)-Fraction(n,PERIOD)) for n,d in D_SUPPORT.items()),Fraction(0))
    return {'period':PERIOD,'representatives':[{'n':n,'d_n':d} for n,d in D_SUPPORT.items()],'sum_d':sum(D_SUPPORT.values()),'hurwitz_zero_moment':str(moment),'initial_convergence':'Re(s)>1','formula':'kappa(s)=2*4^s*60^(-2s)*sum d_n*zeta_H(2s,n/60)'}

def kappa_hurwitz(s):
    return 2*mp.power(4,s)*mp.power(PERIOD,-2*s)*sum(d*mp.zeta(2*s,mp.mpf(n)/PERIOD) for n,d in D_SUPPORT.items())

def gamma_log_torsion(dps=50):
    if not isinstance(dps,int) or isinstance(dps,bool) or dps<20: raise ValueError('dps must be >=20')
    with mp.workdps(dps):
        value=mp.log(2*mp.pi)
        for n,d in D_SUPPORT.items(): value+=2*d*mp.loggamma(mp.mpf(n)/PERIOD)
        return +value

def gamma_torsion(dps=50):
    with mp.workdps(dps): return mp.exp(gamma_log_torsion(dps))

def volume_reference(dps=50):
    with mp.workdps(dps): return 2*mp.pi**2/15

def audit(max_degree=180,dps=50):
    if max_degree<63: raise ValueError('max_degree must be >=63')
    if not verify_generating_function_identity(): raise AssertionError('generating function identity failed')
    if not verify_period_60(max(600,max_degree)): raise AssertionError('period-60 check failed')
    gl=gamma_log_torsion(dps); tv=gamma_torsion(dps); vol=volume_reference(dps)
    with mp.workdps(dps):
        torsion_residual=abs(tv-vol)
        checks={}
        for sval in (mp.mpf('1.25'),mp.mpf('2.0')):
            direct=kappa_direct_partial(sval,min(max_degree,80)); reduced=kappa_boundary_partial(sval,min(max_degree,80))
            checks[str(sval)]={'direct':mp.nstr(direct,dps),'boundary_reduced':mp.nstr(reduced,dps),'absolute_residual':mp.nstr(abs(direct-reduced),8)}
            if abs(direct-reduced)>mp.mpf(10)**(-(dps//2)): raise AssertionError('finite spectral cancellation failed')
    return {'task':'T042','passed':True,'group_order':120,'molien_invariant_series':'(1+t^30)/((1-t^12)(1-t^20))','spectral_eigenvalue':'Lambda_m(p)=(m+2*p*(m-p))^2/4','spectral_zeta':{'zeta0':'1 + sum_{m>=1} a_m sum_{p=0}^m Lambda_m(p)^(-s)','zeta1':'2 * sum_{m>=0} a_m sum_{p=1}^{m+1} Lambda_m(p)^(-s)','kappa':'-2*zeta0(s)+zeta1(s)','initial_convergence':'Re(s)>1','zero_mode_convention':'constant E0 mode contributes 1'},'finite_cancellation_checks':checks,'difference_generating_function':{'identity_verified_symbolically':True,'D':'(t^2-1)*(1+t^30)/((1-t^12)*(1-t^20))+1-t^2','P_over_1_minus_t60':True,'P_coefficients':[{'degree':n,'coefficient':c} for n,c in P_COEFFICIENTS.items()],'period_60_verified_through_n':max(600,max_degree),**finite_hurwitz_data()},'torsion':{'log_T':mp.nstr(gl,dps),'T':mp.nstr(tv,dps),'volume_2pi2_over_15':mp.nstr(vol,dps),'absolute_T_minus_volume':mp.nstr(torsion_residual,8),'gamma_product':'2*pi*product Gamma(n/60)^(2*d_n)','exact_target':'2*pi^2/15'},'scope':{'proved':['interior cancellation','period-60 generating function','finite Hurwitz continuation of combined kappa','Gamma-product formula'],'numerical':['finite-cutoff cancellation at s=5/4 and s=2','Gamma product versus volume'],'not_claimed':['separate continuations of zeta0 and zeta1','twisted flat bundles']}}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--max-degree',type=int,default=180); p.add_argument('--dps',type=int,default=50); p.add_argument('--output',default='data/t042_full_rumin_torsion_audit.json'); a=p.parse_args()
    report=audit(a.max_degree,a.dps); path=Path(a.output); path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'task':report['task'],'passed':report['passed'],'torsion':report['torsion'],'period_60_verified_through_n':report['difference_generating_function']['period_60_verified_through_n']},indent=2))
if __name__=='__main__': main()
