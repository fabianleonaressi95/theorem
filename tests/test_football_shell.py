from pathlib import Path
import sys
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from models.football_shell import build_football_shell,compare_scan,cube_sphere_fields,read_point_cloud,run_shell_audit,sample_shell_surface,solve_discrete_shell

def test_closed_truncated_icosahedron_shell_counts():
 m=build_football_shell()
 assert len(m["vertices"])==60 and len(m["panels"])==32
 assert np.sum(m["panel_types"]=="pentagon")==12 and np.sum(m["panel_types"]=="hexagon")==20
 assert len(m["nodes"])==92 and len(m["triangles"])==180
 assert len(m["edge_triangles"])==270 and len(m["physical_seams"])==90

def test_cube_sphere_exact_geometry_and_h4():
 f=cube_sphere_fields(np.array([[1,0,0],[1,1,0],[1,1,1]],float))
 assert np.allclose(f["xi"],[1,np.sqrt(2),np.sqrt(3)])
 assert np.allclose(f["chi"],[0,np.sqrt(2)-1,np.sqrt(3)-1])
 assert np.allclose(f["H4"],[.4,-.1,-4/15])

def test_shell_equilibrium_residual_and_stability():
 m=build_football_shell()
 _,_,K,d=solve_discrete_shell(m,E1=1000,E2=1000,G12=1000/(2*1.25))
 assert d["linear_system_relative_residual_free_dofs"]<1e-10
 assert d["constrained_stiffness_min_eigenvalue"]>0 and d["physical_seam_count"]==90
 assert np.allclose(K,K.T,atol=1e-9)

def test_orthotropy_and_seam_reinforcement_change_response():
 m=build_football_shell()
 _,ui,_,_=solve_discrete_shell(m,E1=1000,E2=1000,G12=400)
 _,uo,_,_=solve_discrete_shell(m,E1=1400,E2=500,G12=250)
 _,us,_,_=solve_discrete_shell(m,E1=1000,E2=700,G12=300,seam_Et=10.,seam_bending_factor=8.)
 assert np.linalg.norm(ui-uo)>1e-10 and np.linalg.norm(ui-us)>1e-10

def test_cube_and_h4_modes_separately_identifiable():
 _,_,_,_,r=run_shell_audit(cube_alpha=.02,h4_alpha=.01)
 b=r["cube_sphere_geometry"]["shape_coefficients_before"]
 assert abs(b["cube_sphere_chi"]-.02)<1e-10 and abs(b["cubic_harmonic_H4"]-.01)<1e-10

def test_scan_icp_recovers_rigidly_transformed_synthetic_surface(tmp_path):
 m=build_football_shell(); target=sample_shell_surface(m["nodes"],m["triangles"],2)
 a=.23; R=np.array([[np.cos(a),-np.sin(a),0],[np.sin(a),np.cos(a),0],[0,0,1]])
 scan=target@R.T+np.array([2.,-1.,.5]); path=tmp_path/"synthetic_scan.csv"
 np.savetxt(path,scan,delimiter=",",header="x,y,z",comments="")
 result=compare_scan(read_point_cloud(path),m["nodes"],m["triangles"],2)
 assert result["symmetric_chamfer_rms"]<1e-8
