# A18 — Discrete U(1) Bianchi identity on the Q6 cubical complex

**Classification:** numerical verification on the archived finite Q6 cubical complex.  
**Input:** `psu_fibre_connection_matrices.npz` from the A13 bundle.  
**Scope:** compact lattice (U(1)) connection; no continuum or physical-monopole claim.

## Construction

From the archived (SO(3)) edge transports (R_{gh}), the radial unit section
(n_g=X_g/\|X_g\|), and a local oriented frame (E_g=(u_g,v_g,n_g)), form
(A_{gh}=(E_h^T R_{gh}E_g)|_{n_g^\perp}\in SO(2)\cong U(1)).

For the positively oriented ((a,b))-face based at (g), the edge path is
(+a,+b,-a,-b). Let (ar\Theta_{g;ab}\in(-\pi,\pi]) be its principal
plaquette angle. On a positively oriented 3-cube with axes (a<b<c), the
oriented boundary sum is

\[
S_{g;abc}=\Delta_a\bar\Theta_{g;bc}
-\Delta_b\bar\Theta_{g;ac}
+\Delta_c\bar\Theta_{g;ab}.
\]

The compact (U(1)) Bianchi identity requires (S_{g;abc}=0\pmod{2\pi}).
The integer branch charge is (m_{g;abc}=S_{g;abc}/(2\pi)\in\mathbb Z).

## Numerical result

Reproduce with:

```bash
python scripts/audit_rgs_q6_u1_bianchi.py data/psu_fibre_connection_matrices.npz \
  --output reports/RGS_A18_U1_BIANCHI_2026-11-26.json
```

| Test | Result |
|---|---:|
| 3-cubes tested | 160 |
| Maximum wrapped Bianchi residual | (3.063\times10^{-15}) rad |
| Maximum quantization residual | (3.553\times10^{-15}) rad |
| 4-cells tested | 60 |
| Maximum integer boundary of cube charges | 0 |
| Nonzero 4-cell boundaries | 0 |

Integer cube-charge histogram:

| (m) | Count |
|---:|---:|
| -2 | 5 |
| -1 | 9 |
| 0 | 137 |
| +1 | 9 |
| +2 | 0 |

There are 23 nonzero principal-branch cube charges. Their integer cochain is
closed: its oriented boundary vanishes on all 60 four-cells. The total charge
in this chosen finite cubical complex is -10; no neutrality condition is
assumed for this non-periodic 6-cube.

## Interpretation and limits

**PASS:** the compact abelian Bianchi identity holds modulo (2\pi) on all
160 3-cubes. The integer branch defects obey the next closure identity on all
60 4-cells ((d m=0)).

The nonzero integers arise from lifting compact plaquette angles to the
principal interval. They are lattice branch/monopole-*candidate* charges,
not evidence by themselves of physical magnetic monopoles or singularities.
A continuum field strength, continuum Bianchi equation, continuum limit,
or physical source interpretation remains **OPEN**.
