# T096 — Airy-strain non-identifiability of elastic-distortion holonomy

**Date:** 11 November 2026  
**Status:** mathematical non-identifiability statement proved; polygonal witness numerically verified by regression test. This is a data-identifiability result, not a defect-field extraction theorem.  
**Dependencies:** T093 (Cartan holonomy conventions), T094 (SE(2) face audit), T095 (Morandotti two-core source adapter).

## 1. Question and scope

T095 connects prescribed Frank/Burgers core data to the Morandotti six-component source vector. The next intended step is to replace prescribed data by loop quantities extracted from finite-element fields. Before doing so, one must establish whether the available C0-IPDG Airy output contains enough information to determine those loop quantities.

The Airy potential determines the in-plane stress
\[
\sigma=\operatorname{cof}(D^2v).
\]
After choosing a constitutive law, stress determines the symmetric elastic strain. It does not, by itself, determine the skew part of the elastic distortion. The latter is needed to form a full distortion one-form and its translational loop closure.

## 2. Plane-strain constitutive recovery

For isotropic linear elasticity in plane strain, with Young modulus \(E>0\), Poisson ratio \(-1<\nu<1/2\), and in-plane symmetric stress \(\sigma\), the recovered in-plane strain is
\[
\varepsilon=\frac{1+\nu}{E}
\left(\sigma-\nu\,\operatorname{tr}(\sigma)I_2\right).
\]
This is a symmetric tensor. The full elastic distortion may be written
\[
\beta=\varepsilon+\omega J,
\qquad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\]
where \(\omega(x)\) is the infinitesimal local rotation. The pointwise map \(\beta\mapsto\operatorname{sym}\beta\) has a one-dimensional kernel, namely \(\{cJ:c\in\mathbb R\}\).

## 3. Non-identifiability proposition

**Proposition 96.1 (Airy strain does not identify Burgers loop closure).**  
Let \(\varepsilon\) be a prescribed symmetric strain field on a planar region containing a closed Lipschitz loop \(\gamma\). For any scalar field \(\omega\), define \(\beta_\omega=\varepsilon+\omega J\). The strain data \(\operatorname{sym}\beta_\omega=\varepsilon\) are independent of \(\omega\), whereas the distortion loop closure
\[
b_\omega(\gamma)=\oint_\gamma\beta_\omega\,dx
\]
depends on \(\omega\) in general. Consequently, stress/Airy data plus the constitutive recovery of \(\varepsilon\) do not determine \(b_\omega(\gamma)\), and therefore cannot determine the translational part of a Cartan/SE(2) defect holonomy without additional kinematic information.

**Proof.** Since \(J^T=-J\), one has \(\operatorname{sym}(\omega J)=0\), hence \(\operatorname{sym}\beta_\omega=\varepsilon\) for every \(\omega\). But
\[
b_{\omega_1}(\gamma)-b_{\omega_0}(\gamma)
=\oint_\gamma(\omega_1-\omega_0)J\,dx,
\]
which need not vanish. For example, take \(\varepsilon=0\), a positively oriented circle of radius \(r\), \(\omega_0=0\), and \(\omega_1(x,y)=c x\). Green's theorem gives
\[
b_{\omega_1}-b_{\omega_0}
=\left(-c\pi r^2,0\right)\ne0
\quad(c\ne0).
\]
Thus identical symmetric strain data can have different Burgers loop closures. \(\square\)

## 4. Discrete polygonal witness

The script scripts/rgs_airystress_holonomy_identifiability.py evaluates the loop integral on a counter-clockwise regular polygon using edge-midpoint quadrature. For affine \(\omega=cx\), this quadrature is exact on every straight edge and returns
\[
b_h=\left(-c|P_h|,0\right),
\]
where \(|P_h|\) is the polygon area. The regression test checks that (i) the symmetric strain is identical, (ii) the two closures differ, and (iii) the computed affine-field closure agrees with the exact polygon formula.

This witness is deliberately separate from the Morandotti P3 C0-IPDG solver. It demonstrates a missing degree of freedom; it does not extract a measured defect charge from an Airy field.

## 5. Consequence for the FEM extraction pipeline

The current two-core C0-IPDG export stores six Airy cell-field coefficient vectors, their DOF coordinates, mesh geometry and the interaction matrices. It does not export a displacement field, elastic distortion, plastic distortion, or independent microrotation. Therefore a unique SE(2) loop holonomy cannot be reconstructed from those arrays alone.

A physically interpretable extraction must add and audit at least one of the following:
1. a displacement field together with the plastic distortion/cut convention, so that the elastic distortion is defined;
2. an independently modelled microrotation field and its constitutive/coupling law (Cosserat or micropolar extension);
3. a specified gauge/recovery problem for the skew part, with its boundary conditions and regularization reported, and with the resulting gauge dependence quantified.

Only after that addition should loop transports be assembled, based at a common frame, and compared with the prescribed Frank/Burgers data in T095. A loop integral of symmetric strain alone must not be labelled a Burgers vector or an SE(2) holonomy.

## 6. Classification

- **Proved:** pointwise non-identifiability of the skew elastic-distortion component from symmetric strain.
- **Numerically verified:** polygonal loop witness with equal strain and unequal closure.
- **Open:** a constitutively justified recovery of rotation/distortion from the Morandotti FE solution; measured core-loop holonomy; convergence of extracted loop data under mesh refinement; and coupling of measured rather than prescribed data to the six-dimensional interaction system.

**FLN**
