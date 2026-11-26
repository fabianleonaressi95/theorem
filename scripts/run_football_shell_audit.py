#!/usr/bin/env python3
import argparse,json,csv,sys
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from models.football_shell import run_shell_audit
def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument("--radius",type=float,default=1.); p.add_argument("--pressure",type=float,default=1e-3)
 p.add_argument("--thickness",type=float,default=.02); p.add_argument("--E1",type=float,default=1000.)
 p.add_argument("--E2",type=float,default=700.); p.add_argument("--nu12",type=float,default=.25)
 p.add_argument("--G12",type=float,default=300.); p.add_argument("--material-angle",type=float,default=0.)
 p.add_argument("--seam-Et",type=float,default=0.); p.add_argument("--seam-bending-factor",type=float,default=4.)
 p.add_argument("--cube-alpha",type=float,default=0.); p.add_argument("--h4-alpha",type=float,default=0.)
 p.add_argument("--scan",type=Path); p.add_argument("--json",type=Path,default=Path("reports/football_shell_audit.json"))
 p.add_argument("--csv",type=Path,default=Path("reports/football_shell_displacements.csv")); a=p.parse_args()
 mesh,X,u,K,r=run_shell_audit(radius=a.radius,pressure=a.pressure,thickness=a.thickness,E1=a.E1,E2=a.E2,
  nu12=a.nu12,G12=a.G12,material_angle=a.material_angle,seam_Et=a.seam_Et,
  seam_bending_factor=a.seam_bending_factor,cube_alpha=a.cube_alpha,h4_alpha=a.h4_alpha,scan_path=a.scan)
 r["reproducibility"]={"command":" ".join(sys.argv),"numpy":np.__version__,"python":sys.version.split()[0],"stiffness_shape":list(K.shape)}
 a.json.parent.mkdir(parents=True,exist_ok=True); a.json.write_text(json.dumps(r,indent=2,sort_keys=True)+"\n")
 a.csv.parent.mkdir(parents=True,exist_ok=True)
 with a.csv.open("w",newline="") as f:
  w=csv.writer(f); w.writerow(["node","x0","y0","z0","ux","uy","uz","x","y","z"])
  for i,(x0,ui,x) in enumerate(zip(mesh["nodes"],u,X)): w.writerow([i,*x0,*ui,*x])
 print(json.dumps(r,indent=2,sort_keys=True))
if __name__=="__main__": main()
