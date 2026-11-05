# T043 — Twisted Rumin torsion on the nine 2I sectors

T043 extends T042 to the nine irreducible 2I sectors, using the exact Molien multiplicities in T032. The eigenvalue is Lambda_m(p)=(m+2p(m-p))^2/4.

For each irrep rho, write A_rho(t)=sum_m b_(m,rho)t^m=N_rho(t)/((1-t^12)(1-t^20)). The alternating zeta functions are zeta_0,rho=b_(0,rho)+sum_(m>=1)b_(m,rho)sum_(p=0)^m Lambda_m(p)^(-s), and zeta_1,rho=2sum_(m>=0)b_(m,rho)sum_(p=1)^(m+1)Lambda_m(p)^(-s).

The interior terms cancel exactly in kappa_rho=-2zeta_0,rho+zeta_1,rho. The zero mode also cancels the two unit middle modes. Thus kappa_rho(s)=2*4^s*sum_(n>=1)d_(n,rho)n^(-2s), where D_rho(t)=(t^2-1)(A_rho(t)-b_(0,rho)).

Because the Molien denominator divides 1-t^60, P_rho=(1-t^60)D_rho is an integer polynomial. Each sector therefore has an exact finite Hurwitz-zeta continuation and a finite Gamma-product formula for T_rho, with 2log(T_rho)=kappa_rho'(0).

The code, tests, complete sector polynomials, finite terms, and residue-class representatives are in the accompanying source and JSON report. The numerical sector values and the regular-representation check are tabulated in the next sections.