# RGS–PRISM: cube/sphere geometry and orthotropic football shell

## 1. Reuse of the existing RGS cube–sphere work

This module reuses the audited fields:
\[
r_C(\mathbf n)=a/\|\mathbf n\|_\infty,\quad r_S=a,\quad
\xi_{CS}=1/\|\mathbf n\|_\infty,\quad \chi_{CS}=\xi_{CS}-1,
\]
\[
H_4(\mathbf n)=n_x^4+n_y^4+n_z^4-\frac35.
\]
The exact continuum bounds are \(0\leq\chi_{CS}\leq\sqrt3-1\). The degree-four cubic harmonic has zero spherical mean. These fields remain distinct: \(\chi_{CS}\) is the exact radial excess of a cube relative to its inscribed sphere; \(H_4\) is a smooth cubic-symmetry harmonic. Neither is identified with the football's pentagon/hexagon constitutive contrast.

The previous RGS Q6 cube/sphere audit used 64 directions and 192 links. A separate graph-compatible lift audit found a common geometry/graph subgroup of order 16, not the full cubic group \(O_h\) of order 48. Here the analytic cube fields are used as shape modes; no full \(O_h\) covariance of the Q6 adjacency is claimed.

The radial reference surface is
\[
X_0(\mathbf n)=R[1+\alpha_C(\chi_{CS}-\langle\chi_{CS}\rangle)+\alpha_4H_4]\mathbf n.
\]
The amplitudes default to zero. They are explicit calibration parameters, not arbitrary weights inferred from football topology. A least-squares projection onto \(\{1,\chi_{CS},H_4\}\) is reported before and after the shell solve.

## 2. Football topology and shell mesh

| Quantity | Count |
|---|---:|
| Original vertices | 60 |
| Pentagon panels | 12 |
| Hexagon panels | 20 |
| Physical panel seams | 90 |
| Triangular shell elements | 180 |
| Shell nodes including panel centres | 92 |
| Dihedral hinges | 270 |

Each polygon is fan-triangulated from a panel-centre node. The mesh is closed and conforming; every triangular edge has exactly two incident triangles. Physical seams are distinguished from internal fan edges.

## 3. Orthotropic triangular membrane elements

Each triangle uses a constant-strain triangular (CST) membrane element. Its material axes are defined panel by panel. The plane-stress constitutive matrix is
\[
D=\begin{pmatrix}E_1/\Delta&\nu_{12}E_2/\Delta&0\\
\nu_{12}E_2/\Delta&E_2/\Delta&0\\0&0&G_{12}\end{pmatrix},
\quad \Delta=1-\nu_{12}\nu_{21},\quad \nu_{21}=\nu_{12}E_2/E_1.
\]
The element stiffness is \(K_e=tA_eB_e^TDB_e\), transformed into global 3D displacement degrees of freedom. \(E_1,E_2,G_{12},\nu_{12}\), thickness and material-frame angle are independent inputs. Defaults are demonstration values, not measured textile properties.

## 4. Discrete shell bending and seams

Adjacent facets are coupled by a signed-dihedral hinge. Its linearised contribution is
\[
K_h=k_h(\nabla\theta_h)(\nabla\theta_h)^T,\quad
k_h=D_b\ell_h/w_h,\quad D_b=E_1t^3/[12(1-\nu_{12}^2)].
\]
The signed-dihedral gradient is evaluated by central finite differences on the reference mesh. Physical seams have a separately configurable bending multiplier and optional line reinforcement \(E_st_s\), represented by an axial line-spring term. Six gauge constraints remove rigid modes. Pressure is integrated over reference facets and distributed to nodes.

This is a **linearised discrete shell**: CST membrane + dihedral bending + seam reinforcement. It is more expressive than the earlier panel-centre scalar model, but is not a geometrically nonlinear finite-strain shell. Contact, folds, damage, adhesive slip and yarn-scale homogenisation are not included.

## 5. Experimental scan interface

The runner accepts CSV (x,y,z columns), XYZ, OBJ vertex, and ASCII PLY point clouds. Scan and model radius must use the same length unit. Rigid ICP alignment is followed by symmetric sampled-surface metrics: scan-to-model mean/RMS/95th percentile, model-to-scan mean/RMS, symmetric Chamfer RMS, and sampled symmetric Hausdorff distance.

No experimental scan is bundled. The committed baseline is marked not_run_no_experimental_scan; a synthetic rigid-transform ICP test checks software only. A real scan and coupon/assembly measurements are required before physical fit or material identification can be claimed.

Template: data/scans/football_scan_template.csv.

## 6. Reproduction

~~~bash
python scripts/run_football_shell_audit.py \
  --radius 1.0 --pressure 0.001 --thickness 0.02 \
  --E1 1000 --E2 700 --nu12 0.25 --G12 300 \
  --cube-alpha 0 --h4-alpha 0 --seam-Et 0 \
  --json reports/football_shell_audit.json \
  --csv reports/football_shell_displacements.csv
python -m pytest -q tests/test_football_shell.py tests/test_football_anisotropy.py
~~~

For a measured scan, add --scan path/to/scan.csv and set radius to the same physical unit. The geometric amplitudes, orthotropic constants and seam constants must be identified from independent measurements or a pre-registered fit protocol; do not tune all parameters to the same scan without regularisation and held-out validation.

## 7. Evidence status

| Statement | Status |
|---|---|
| Cube/sphere radial formula and chi bounds | Exact geometry |
| H4 cubic harmonic | Exact analytic definition |
| Truncated-icosahedron counts and closed incidence | Exact finite combinatorics; tested |
| CST orthotropic membrane assembly | Implemented; numerical tests |
| Signed-dihedral shell bending and seam line term | Implemented; numerical tests |
| Linear equilibrium and positive constrained stiffness | Numerically checked |
| ICP on synthetic rigid transform | Software test only |
| Fit to actual football scan | Open; no scan supplied |
| Material constants and seam law | Open; coupon/assembly measurements required |
| Geometrically nonlinear inflation and contact | Not implemented |

The Morandotti-facing claim is narrow: the code provides a common geometric/mechanical language in which cube-induced radial anisotropy, cubic H4 distortion, pentagon/hexagon panel orbits, textile orthotropy and seam stiffness can be varied independently and compared with 3D scan data. It does not yet establish which mechanism explains a measured ball shape.
