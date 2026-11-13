# T133 — Finite-dimensional KKT existence, uniqueness and energy identity

**Classification:** [P] fully proved under the stated finite-dimensional hypotheses. This theorem is an abstract variational result; its application to an assembled Morandotti matrix pair requires separate verification of positive definiteness and full row rank.

**Dependencies:** none. Related implementation: `models/discrete_incompatibility_weak.py`, `models/morandotti_bfs_kkt.py`; specification: `manuscripts/MORANDOTTI_BENCHMARK_I_DISCRETE_SAINT_VENANT_KKT.md`.

## 1. Statement

Let (M\in\mathbb R^{n\times n}) be symmetric positive definite and let (A\in\mathbb R^{m\times n}) have full row rank (m). For any (z\in\mathbb R^m), consider
\[
\min_{e\in\mathbb R^n}\frac12 e^TMe
\qquad\text{subject to }Ae=z.
\]
Set
\[
L:=AM^{-1}A^T.
\]
Then (L) is symmetric positive definite, the feasible set is nonempty, and the problem has a unique minimizer (e_*) and a unique Lagrange multiplier (\lambda_*) for the convention
\[
\mathcal L(e,\lambda)=\frac12e^TMe+\lambda^T(Ae-z).
\]
They are
\[
\boxed{\lambda_*=-L^{-1}z,\qquad
e_*=M^{-1}A^TL^{-1}z.}
\]
The primal-dual energy identity is
\[
\boxed{\frac12e_*^TMe_*
=\frac12z^TL^{-1}z
=-\frac12z^T\lambda_*.}
\]

## 2. Proof

Since (M\succ0), its inverse exists and (M^{-1}\succ0). Full row rank of (A) means that (A:\mathbb R^n\to\mathbb R^m) is surjective, so (Ae=z) is feasible for every (z\in\mathbb R^m).

For every nonzero (y\in\mathbb R^m), (A^T) is injective and hence (A^Ty\ne0). Consequently
\[
y^TLy=(A^Ty)^TM^{-1}(A^Ty)>0.
\]
Thus (L\succ0) and is invertible.

Define (\lambda_*=-L^{-1}z) and (e_*=M^{-1}A^TL^{-1}z). Direct substitution verifies feasibility and stationarity:
\[
Ae_*=AM^{-1}A^TL^{-1}z=LL^{-1}z=z,
\qquad
Me_*+A^T\lambda_*=0.
\]
This constructs an admissible candidate without presupposing existence of a minimizer.

For any other feasible (e=e_*+v), one has (Av=0). Therefore
\[
\begin{aligned}
\frac12e^TMe-\frac12e_*^TMe_*
&=e_*^TMv+\frac12v^TMv\\
&=-\lambda_*^TAv+\frac12v^TMv
=\frac12v^TMv\ge0.
\end{aligned}
\]
Positive definiteness of (M) makes equality possible only for (v=0). Hence (e_*) is the unique minimizer. The multiplier is unique because (L) is invertible (equivalently, because (A^T) is injective).

Finally,
\[
\begin{aligned}
\frac12e_*^TMe_*
&=\frac12 z^TL^{-1}AM^{-1}A^TL^{-1}z\\
&=\frac12z^TL^{-1}LL^{-1}z
=\frac12z^TL^{-1}z
=-\frac12z^T\lambda_*.
\end{aligned}
\]
This proves the claim. \(\square\)

## 3. Scope for the Morandotti discretization

For a discrete strain-energy matrix (M_h) and incompatibility matrix (A_h), T133 applies if and only if the relevant assembled matrix (M_h) is symmetric positive definite and (A_h) has full row rank (after any explicitly declared quotient or constraint reduction). These are mathematical hypotheses, not consequences of a successful linear solve or a small residual.

The theorem does **not** prove:
- that a particular assembled (M_h) is positive definite;
- that a particular (A_h) has full row rank;
- coercivity of the P3 C0-IPDG bilinear form;
- consistency or convergence as (h\to0);
- convergence of the multi-core interaction matrix or a distance law.

The code-level acceptance checks are symmetry, smallest eigenvalue (with a scale-aware tolerance), rank/singular-value diagnostics, feasibility, KKT residual, and independent primal/dual energy agreement. Numerical checks support the application of the hypotheses to tested instances; they do not replace a uniform proof for a mesh family.

## 4. Sign convention

The negative sign in (\lambda_*=-L^{-1}z) and in the dual energy expression is tied to (\mathcal L=f+\lambda^T(Ae-z)). Replacing the constraint term by (\lambda^T(z-Ae)) reverses the multiplier sign, but leaves (e_*), (L), and the primal energy unchanged.
