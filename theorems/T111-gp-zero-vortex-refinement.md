# T111 — GP order-parameter zeros and T110 plaquette-vortex refinement

**Classification:** exact phase-winding identity for the stated lattice sampling; numerical verification on a manufactured static order parameter; Gross–Pitaevskii dynamics, continuum convergence beyond the localization bound, and reconnection remain open.

**Dependencies:** T110 (XY torus vorticity and 3D dual flux), T104 (cycle–cocycle–holonomy).

## 1. Scope

T110 extracts integer vortex charge from wrapped phase increments. A Gross–Pitaevskii (GP) order parameter is complex, \(\psi=\sqrt n e^{i\theta}\), and a vortex core is a zero of \(\psi\). This record tests whether plaquette winding localizes that zero with a controlled grid error.

The first benchmark is static and manufactured. It is **not** a numerical solution of the time-dependent GP equation and does not establish vortex dynamics, Kelvin-theorem breakdown, reconnection, or turbulence.

## 2. Manufactured unit vortex

On \([-1,1]^2\), choose a zero \(z_0=(x_0,y_0)\) away from grid vertices and define
\[
\psi(x,y)=((x-x_0)+i(y-y_0))e^{-2((x-x_0)^2+(y-y_0)^2)}.
\]
The Gaussian is strictly positive and does not change the phase. The isolated zero has local index +1.

For each oriented grid plaquette \(p\), sample \(\theta_v=\arg\psi(v)\) at its four vertices and set
\[
q_p=\frac1{2\pi}\sum_{(v,w)\in\partial p}
\operatorname{wrap}_{(-\pi,\pi]}(\theta_w-\theta_v).
\]
The result is integer-valued. For this one-zero field, the plaquette containing \(z_0\) carries \(q_p=+1\), and all other plaquettes carry zero.

## 3. Localization estimate

Let the square cell width be \(h\). Assigning the zero to the centre \(z_p\) of its charged cell gives
\[
|z_p-z_0|\leq\frac{\sqrt2}{2}h.
\]
This is a geometric cell-localization bound, not a convergence theorem for arbitrary GP solutions. It gives an \(O(h)\) localization error.

The implementation scripts/audit_t110_gp_zero_vortex.py evaluates sizes 8, 16, 32, 64, 128, checks that exactly one unit-positive plaquette is detected, and reports the localization error and refinement ratios. Tests are in tests/test_t110_gp_zero_vortex.py.

## 4. Three-dimensional straight-filament control

Extrude the same order parameter independently of a periodic coordinate \(z\):
\[
\psi(x,y,z)=((x-x_0)+i(y-y_0))e^{-2((x-x_0)^2+(y-y_0)^2)}.
\]
Its zero set is a straight line winding around the periodic \(z\)-direction. The \(xy\)-plaquette winding is copied along \(z\), producing a unit dual \(z\)-link flux at each layer; the other two plaquette orientations vanish. Since this flux is independent of \(z\), the discrete dual divergence is exactly zero. The script checks this on a \(32\times32\times8\) extrusion and reports eight unit-flux dual links.

This is a controlled straight-line geometry, not a general 3D GP simulation or a reconnection test.

## 5. Acceptance criteria and limitations

**Accepted by the manufactured benchmark if:**
1. exactly one plaquette has nonzero charge on every tested grid;
2. its charge is +1;
3. the localization error obeys \(\sqrt2 h/2\).

**Not established here:** a stationary or dynamically evolved GP solution; matching on arbitrary GP configurations; 3D dual-link flux matching to filament geometry; reconnection rates, helicity transfer, Kelvin-wave spectra, turbulence; or a Q6/QLG-to-GP continuum map.

## 6. Next physical validation gate

Solve the dimensionless time-dependent GP equation on periodic 2D/3D grids, extract phase winding and density minima independently, and compare their locations under refinement. In 3D, convert all three oriented plaquette fields to T110 dual-link flux and check exact divergence closure. Study reconnection only after static identification and the time integrator's conservation/error budget are validated.

## References

1. L. P. Pitaevskii and S. Stringari, *Bose-Einstein Condensation and Superfluidity*, Oxford University Press (2016).
2. C. F. Barenghi, L. Skrbek and K. R. Sreenivasan, “Introduction to quantum turbulence,” *PNAS* 111 (2014), 4647–4652, DOI: 10.1073/pnas.1312541111.
