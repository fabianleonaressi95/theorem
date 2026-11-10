# Theorem — Kathara square similarity, silver ratio, and digamma law

**Status:** proved from the explicitly stated square-similarity matrix and the Gamma reflection identity.  
**Scope:** this theorem establishes the silver branch. It does not derive the supergolden three-channel substitution from Kathara geometry.

## 1. Geometric hypothesis and exact matrix

Consider the planar stage map
\[
T=\begin{pmatrix}1&1\\-1&1\end{pmatrix}.
\]
A direct calculation gives
\[
T^TT=2I_2,\qquad \det T=2,
\]
and
\[
T=\sqrt2\,R(-\pi/4),\qquad
R(-\pi/4)=\begin{pmatrix}
\cos(\pi/4)&\sin(\pi/4)\\
-\sin(\pi/4)&\cos(\pi/4)
\end{pmatrix}.
\]
Thus the map is an orientation-preserving similarity: it scales lengths by \(\sqrt2\) and rotates by \(-\pi/4\).

## 2. Theorem

Let \(\alpha=\pi/4\) be the magnitude of the stage rotation. Define the half-angle coefficient
\[
\delta_T:=\cot(\alpha/2).
\]
Then:

1. \(\delta_T=1+\sqrt2\), the silver ratio;
2. \(\delta_T\) is the unique positive solution of
   \[
   \delta_T^2-2\delta_T-1=0;
   \]
3. the digamma reflection difference at the normalized half-angle is
   \[
   \boxed{
   \psi\!\left(1-\frac{\alpha}{2\pi}\right)
   -\psi\!\left(\frac{\alpha}{2\pi}\right)
   =\pi\delta_T;
   }
   \]
4. since \(\alpha/(2\pi)=1/8\), this is exactly
   \[
   \boxed{\psi(7/8)-\psi(1/8)=\pi(1+\sqrt2).}
   \]

This is the precise angle-to-digamma law associated with the stated Kathara square similarity.

## 3. Proof

From the exact matrix,
\[
T=\sqrt2R(-\pi/4),
\]
so the absolute rotation angle is \(\alpha=\pi/4\). Hence
\[
\delta_T=\cot(\alpha/2)=\cot(\pi/8).
\]
The tangent half-angle identity gives
\[
\tan(\pi/8)=\sqrt2-1,
\]
and therefore
\[
\delta_T=\frac1{\sqrt2-1}=1+\sqrt2.
\]
Squaring this expression yields
\[
\delta_T^2=3+2\sqrt2=2(1+\sqrt2)+1=2\delta_T+1.
\]

Now set \(x=\alpha/(2\pi)=1/8\) in the Gamma/digamma reflection identity:
\[
\psi(1-x)-\psi(x)=\pi\cot(\pi x).
\]
Since \(\pi x=\alpha/2\), the right-hand side is
\[
\pi\cot(\alpha/2)=\pi\delta_T.
\]
This proves all four statements. \(\square\)

## 4. Iteration law of the same square map

The powers of the stage map satisfy
\[
T^2=\begin{pmatrix}0&2\\-2&0\end{pmatrix}
=2R(-\pi/2),
\qquad
T^4=-4I_2,
\qquad
T^8=16I_2.
\]
Thus the stage map has a four-step half-turn with scale factor \(4\), and an eight-step return to the original orientation with scale factor \(16\).

These identities describe the square similarity exactly. They do not imply that \(T\) has silver ratio as an eigenvalue: its complex eigenvalues are \(1\pm i\), each of modulus \(\sqrt2\). The silver ratio arises from the cotangent of the half-rotation angle, not from the spectrum of \(T\).

## 5. What this theorem establishes

The chain of implications is
\[
\boxed{
T=\sqrt2R(-\pi/4)
\ \Longrightarrow\
\alpha=\pi/4
\ \Longrightarrow\
\cot(\alpha/2)=1+\sqrt2
\ \Longrightarrow\
\psi(7/8)-\psi(1/8)=\pi(1+\sqrt2).
}
\]
Every arrow is an exact identity under the stated stage-map convention.

The theorem does not establish that the source drawing convention is a unique physical law, nor does it produce the supergolden transfer matrix. The supergolden branch is instead covered by the separate three-channel substitution theorem, whose geometric realization remains open.
