#!/usr/bin/env python3
"""T027 exact McKay-Molien coefficient cross-audit; standard library only."""
import argparse, json
NAMES=("1","2_s","3","4_s","5","6_s","4","2'_s","3'")
DIMS=(1,2,3,4,5,6,4,2,3)
EDGES=((0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(5,8))
MAP={"1":"1","2_s":"2","3":"3","4_s":"4'","5":"5","6_s":"6","4":"4","2'_s":"2'","3'":"3'"}
NUM={"1":{0:1,30:1},"2":{1:1,11:1,19:1,29:1},"2'":{7:1,13:1,17:1,23:1},"3":{2:1,10:1,12:1,18:1,20:1,28:1},"3'":{6:1,10:1,14:1,16:1,20:1,24:1},"4":{6:1,8:1,12:1,14:1,16:1,18:1,22:1,24:1},"4'":{3:1,9:1,11:1,13:1,17:1,19:1,21:1,27:1},"5":{4:1,8:1,10:1,12:1,14:1,16:1,18:1,20:1,22:1,26:1},"6":{5:1,7:1,9:1,11:1,13:1,15:2,17:1,19:1,21:1,23:1,25:1}}
def adjacency():
 a=[[0]*9 for _ in range(9)]
 for i,j in EDGES:a[i][j]=a[j][i]=1
 return a
def recurrence(N):
 a=adjacency(); out=[[1,0,0,0,0,0,0,0,0]]
 if N==0:return out
 out.append([0,1,0,0,0,0,0,0,0])
 for _ in range(1,N):
  p,c=out[-2],out[-1]
  out.append([sum(a[i][j]*c[j] for j in range(9))-p[i] for i in range(9)])
 return out
def molien(label,N):
 out=[]
 for m in range(N+1):
  v=0
  for e,c in NUM[label].items():
   r=m-e
   if r>=0:
    for b in range(r//20+1):
     if (r-20*b)%12==0:v+=c
  out.append(v)
 return out
def audit(N):
 assert sum(x*x for x in DIMS)==120 and sum(DIMS)==30
 a=adjacency()
 assert [sum(a[i][j]*DIMS[j] for j in range(9)) for i in range(9)]==[2*x for x in DIMS]
 R=recurrence(N); M={k:molien(k,N) for k in NUM}
 for i,node in enumerate(NAMES):
  for m in range(N+1):assert R[m][i]==M[MAP[node]][m],(m,node,MAP[node],R[m][i],M[MAP[node]][m])
 for m,row in enumerate(R):
  assert all(x>=0 for x in row) and sum(DIMS[i]*row[i] for i in range(9))==m+1
  odd=(1,3,5,7); even=(0,2,4,6,8)
  assert all(row[i]==0 for i in (odd if m%2==0 else even))
 sel=(0,1,2,3,4,5,6,7,8,9,10,11,12,15,30,60,N)
 return {"audit":"T027 exact McKay-Molien bridge","max_degree":N,"degrees_checked":N+1,"coefficient_equalities_checked":9*(N+1),"label_map_T026_to_T021":MAP,"dimension_vector":"A*d=2*d","weighted_dimension":"sum d_i*n_i(m)=m+1","central_parity":"even nonspinorial; odd spinorial","all_assertions_passed":True,"selected_decompositions":{str(m):{NAMES[i]:R[m][i] for i in range(9) if R[m][i]} for m in sel if m<=N}}
def main():
 p=argparse.ArgumentParser();p.add_argument("--max-degree",type=int,default=240);p.add_argument("--json",action="store_true");a=p.parse_args()
 if a.max_degree<0:p.error("--max-degree must be >=0")
 r=audit(a.max_degree)
 if a.json:print(json.dumps(r,indent=2))
 else:
  print(r["audit"]);print("degrees:",r["degrees_checked"]);print("coefficient equalities:",r["coefficient_equalities_checked"]);print("label map: PASS");print("all nine Molien series: PASS");print("dimensions/parity: PASS");print("all assertions passed")
if __name__=="__main__":main()
