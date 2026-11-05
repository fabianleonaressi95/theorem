"""Exact quaternion model of 2I over Q(sqrt(5)); no floating point."""
from __future__ import annotations
import itertools, json, argparse
from fractions import Fraction as F
from collections import Counter
import sympy as sp
Pair=tuple[F,F]; Q=tuple[Pair,Pair,Pair,Pair]
Z=(F(0),F(0)); O=(F(1),F(0)); H=(F(1,2),F(0)); PH=(F(0),F(1,2)); IPH=(F(-1,2),F(1,2))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y):
 a,b=x; c,d=y
 return (a*c+b*d,a*d+b*c+b*d)
def qmul(x,y):
 a,b,c,d=x; e,f,g,h=y
 return (sub(sub(sub(mul(a,e),mul(b,f)),mul(c,g)),mul(d,h)),
 sub(add(add(mul(a,f),mul(b,e)),mul(c,h)),mul(d,g)),
 add(sub(add(mul(a,g),mul(c,e)),mul(b,h)),mul(d,f)),
 add(sub(add(mul(a,h),mul(b,g)),mul(c,f)),mul(d,e)))
def qconj(q): return (q[0],neg(q[1]),neg(q[2]),neg(q[3]))
def qnorm2(q):
 out=Z
 for x in q: out=add(out,mul(x,x))
 return out
def even(p): return sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2==0
def elements_2i():
 entries=(Z,H,PH,IPH); out=set()
 for p in itertools.permutations(range(4)):
  if not even(p): continue
  v=[entries[k] for k in p]; nz=[i for i,x in enumerate(v) if x!=Z]
  for signs in itertools.product((-1,1),repeat=3):
   w=list(v)
   for i,s in zip(nz,signs):
    if s<0: w[i]=neg(w[i])
   out.add(tuple(w))
 for axis in range(4):
  for s in (-1,1):
   v=[Z]*4; v[axis]=O if s>0 else neg(O); out.add(tuple(v))
 for signs in itertools.product((-1,1),repeat=4):
  out.add(tuple(H if s>0 else neg(H) for s in signs))
 if len(out)!=120: raise AssertionError(f"expected 120 elements, got {len(out)}")
 return tuple(sorted(out))
CLASS_SCALARS=(O,(-F(1),F(0)),(-F(1,2),F(0)),Z,IPH,(F(0),-F(1,2)),H,PH,(F(1,2),-F(1,2)))
CLASS_SIZES=(1,1,20,30,12,12,20,12,12); CLASS_ORDERS=(1,2,3,4,5,5,6,10,10)
def expr(x):
 phi=(1+sp.sqrt(5))/2
 return sp.Rational(x[0].numerator,x[0].denominator)+sp.Rational(x[1].numerator,x[1].denominator)*phi
def rho2(q):
 a,b,c,d=map(expr,q); I=sp.I
 return sp.Matrix([[a+I*b,c+I*d],[-c+I*d,a-I*b]])
def group_table(G):
 idx={g:i for i,g in enumerate(G)}; table=[]
 for x in G:
  row=[]
  for y in G:
   z=qmul(x,y)
   if z not in idx: raise AssertionError("not closed under quaternion multiplication")
   row.append(idx[z])
  table.append(tuple(row))
 e=idx[(O,Z,Z,Z)]; inv=tuple(idx[qconj(g)] for g in G)
 return tuple(table),e,inv
def audit():
 G=elements_2i(); table,e,inv=group_table(G)
 if any(table[e][g]!=g or table[g][e]!=g for g in range(120)): raise AssertionError("identity law")
 if any(table[g][inv[g]]!=e or table[inv[g]][g]!=e for g in range(120)): raise AssertionError("inverse law")
 if any(qnorm2(g)!=O for g in G): raise AssertionError("non-unit quaternion")
 counts=Counter(g[0] for g in G)
 sizes=tuple(counts.get(x,0) for x in CLASS_SCALARS)
 if sizes!=CLASS_SIZES: raise AssertionError(f"class sizes {sizes}")
 phi=(1+sp.sqrt(5))/2; chi=(2,-2,-1,0,phi-1,-phi,1,phi,1-phi)
 for j,a in enumerate(CLASS_SCALARS):
  if sp.simplify(2*expr(a)-chi[j])!=0: raise AssertionError("character convention")
 for g in G:
  M=rho2(g)
  if sp.simplify(M.det()-1)!=0: raise AssertionError("determinant")
  if sp.simplify(M.conjugate().T*M-sp.eye(2))!=sp.zeros(2): raise AssertionError("unitarity")
 probes=(G[e],G[0],G[-1])
 for x in probes:
  for y in probes:
   if sp.simplify(rho2(qmul(x,y))-rho2(x)*rho2(y))!=sp.zeros(2): raise AssertionError("not multiplicative")
 return {"passed":True,"group":"2I","order":120,"field":"Q(sqrt(5)","construction":"600-cell unit quaternions",
 "closure_products_checked":14400,"unit_norms_checked":120,"identity_inverse_checks":240,
 "fundamental_SU2_determinants_checked":120,"fundamental_SU2_unitarity_checked":120,
 "class_sizes":sizes,"class_orders":CLASS_ORDERS,
 "fundamental_character":[str(sp.simplify(2*expr(a))) for a in CLASS_SCALARS],
 "scope":"Exact group and defining 2D representation; eight further irreducible matrix models remain open."}
def main():
 p=argparse.ArgumentParser(); p.add_argument("--output",default=None); a=p.parse_args()
 report=audit(); payload=json.dumps(report,indent=2)
 if a.output:
  from pathlib import Path
  path=Path(a.output); path.parent.mkdir(parents=True,exist_ok=True); path.write_text(payload+"\n")
 print(payload)
if __name__=="__main__": main()
