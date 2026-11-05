"""T046: scale-dependent Hadamard finite-part determinants for Rumin degrees.

For zeta(s)=R/s+C+D*s+..., define
  log det_FP(mu) = -FP_{s=0} d/ds [mu^(2s) zeta(s)]
                = -(D+2*C*log(mu)+2*R*log(mu)^2).
The alternating combination is regular and fixes one exact relation between
the two finite-part determinants, but not their individual values.
"""
from __future__ import annotations
from fractions import Fraction
import mpmath as mp
from src.t032_2i_molien import IRREP_DIMENSIONS, IRREP_NUMERATORS
from src.t043_twisted_2i_rumin_torsion import tail_data, log_torsion
from src.t045_individual_rumin_zeta_poles import sector_residues

def kappa_at_zero(label):
    """Exact kappa_rho(0) from the periodic Hurwitz representation."""
    cutoff, _poly, finite, tails = tail_data(label)
    value = Fraction(sum(finite.values()), 1)
    for first_n, coeff in tails.items():
        value += Fraction(coeff, 1) * (Fraction(1,2)-Fraction(first_n,60))
    return 2*value

def residues(label):
    d=IRREP_DIMENSIONS[label]
    return {"zeta0":Fraction(d,960),"zeta1":Fraction(d,480)}

def finite_part_derivative(Laurent_C, Laurent_D, residue, log_mu):
    """FP derivative of mu^(2s)*(R/s+C+D*s+O(s^2))."""
    return Laurent_D + 2*Laurent_C*log_mu + 2*residue*log_mu**2

def log_fp_determinant(Laurent_C, Laurent_D, residue, log_mu=0):
    return -finite_part_derivative(Laurent_C,Laurent_D,residue,log_mu)

def alternating_constraint(label, log_mu=0, dps=60):
    """Exact/precision-controlled relation between the two FP log-dets."""
    r=residues(label)
    k0=kappa_at_zero(label)
    with mp.workdps(dps):
        lt=log_torsion(label,dps)
        # D_kappa = kappa'(0) = 2 log(T_rho), by T043 convention.
        Dk=2*lt
        # D1-2D0 = Dk; Ck=kappa(0); Rk=0.
        # At scale mu: D1_mu-2D0_mu = Dk + 2*Ck*log(mu).
        lhs=Dk+2*mp.mpf(k0.numerator)/k0.denominator*mp.mpf(log_mu)
        return {
            "residue_zeta0":str(r["zeta0"]),
            "residue_zeta1":str(r["zeta1"]),
            "residue_alternating":str(-2*r["zeta0"]+r["zeta1"]),
            "kappa_zero_exact":str(k0),
            "kappa_derivative_zero":mp.nstr(Dk,dps),
            "D1_mu_minus_2D0_mu":mp.nstr(lhs,dps),
            "log_mu":str(log_mu),
            "identity":"D1_mu - 2*D0_mu = 2*log(T_rho) + 2*kappa_rho(0)*log(mu)",
        }

def audit(log_mu=0,dps=60):
    sectors={}
    for label in IRREP_NUMERATORS:
        sectors[label]=alternating_constraint(label,log_mu,dps)
    return {
      "task":"T046",
      "scheme":"Hadamard finite part of d/ds[mu^(2s) zeta_k,rho(s)] at s=0",
      "definition":"log det_FP,k(mu) = -[D_k+2*C_k*log(mu)+2*R_k*log(mu)^2]",
      "zeta_laurent":"zeta_k(s)=R_k/s+C_k+D_k*s+O(s^2)",
      "exact_residues":{
        "zeta0":"dim(rho)/960",
        "zeta1":"dim(rho)/480",
        "alternating":"0"
      },
      "alternating_relation":"D1_mu-2*D0_mu=2*log(T_rho)+2*kappa_rho(0)*log(mu)",
      "scope":{
        "proved_exact":[
          "finite-part prescription and its scale transformation",
          "individual residues and their cancellation",
          "exact rational kappa_rho(0) from the period-60 Hurwitz formula",
          "constraint on the two finite-part determinants from the known alternating torsion"
        ],
        "not_computed":[
          "individual Laurent constants C_0 and C_1",
          "individual linear Laurent coefficients D_0 and D_1",
          "individual finite-part determinant values"
        ],
        "reason":"The alternating torsion fixes only D1-2D0 (and C1-2C0); it cannot determine two individual coefficients."
      },
      "scale_log_mu":str(log_mu),
      "sectors":sectors
    }

if __name__=="__main__":
    import argparse,json
    p=argparse.ArgumentParser()
    p.add_argument("--log-mu",type=str,default="0")
    p.add_argument("--dps",type=int,default=60)
    a=p.parse_args()
    print(json.dumps(audit(mp.mpf(a.log_mu),a.dps),indent=2))
