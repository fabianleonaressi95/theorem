# T002 — Volume di Bergman sul dominio di tipo IV in dimensione 5

**Stato: DIMOSTRATO (identità geometrica esplicita).**  
**Ruolo nel programma RGS–PSU–PRISM: identifica esattamente la densità di Bergman con una densità rispetto al volume piatto in coordinate; non dimostra che tale densità sia prodotta dalla marginalizzazione Wilson.**

## 1. Enunciato

Sia
\[
D_5=\{z\in\mathbb C^5:
N(z)=1-2z^\dagger z+|z^Tz|^2>0,\quad |z^Tz|<1\}
\]
il dominio limitato di tipo IV in dimensione complessa 5. Poniamo
\[
g_{i\bar j}= -5\,\partial_i\partial_{\bar j}\log N(z).
\]
Allora
\[
\boxed{\det(g_{i\bar j})=\frac{10^5}{N(z)^5}.}
\]
Con la convenzione di volume riemanniano
\[
dV_g=2^5\det(g_{i\bar j})\,d^{10}z
\]
si ottiene
\[
\boxed{dV_g=N(z)^{-5}\,d\mu_0,\qquad
d\mu_0=20^5\,d^{10}z.}
\]

Qui \(d^{10}z\) è il volume euclideo su \(\mathbb C^5\simeq\mathbb R^{10}\). Se \(z=(q+ip)/\sqrt2\), con \(\omega_0=\sum_{j=1}^5dq_j\wedge dp_j\), allora \(d^{10}z=2^{-5}d\mu_L\), dove \(d\mu_L=dq_1\cdots dq_5dp_1\cdots dp_5\) a meno dell'orientazione. Pertanto, con questa precisa normalizzazione,
\[
d\mu_0=10^5d\mu_L.
\]
La costante dipende dalla normalizzazione delle coordinate; il fattore non costante \(N^{-5}\) è quello geometrico.

## 2. Calcolo della matrice metrica

Scriviamo
\[
s=z^\dagger z,\qquad t=z^Tz,\qquad N=1-2s+t\bar t.
\]
Le derivate sono
\[
N_i=-2\bar z_i+2z_i\bar t,
\qquad
N_{i\bar j}=-2\delta_{ij}+4z_i\bar z_j.
\]
Pertanto
\[
g_{i\bar j}
=-5\left(\frac{N_{i\bar j}}{N}
-\frac{N_iN_{\bar j}}{N^2}\right)
=-\frac5{N^2}A_{i\bar j},
\]
dove
\[
A_{i\bar j}=N N_{i\bar j}-N_iN_{\bar j}.
\]

## 3. Dimostrazione dell'identità determinante

Poniamo \(v=z\), \(w=\bar z\), e consideriamo \(U=(v\;w)\), matrice \(5\times2\). Dalle derivate precedenti,
\[
A=-2NI_5+UCU^T,
\qquad
C=4\begin{pmatrix}
\bar t & N-t\bar t\\
-1 & t
\end{pmatrix}.
\]
Inoltre
\[
U^TU=G=\begin{pmatrix}t&s\\s&\bar t\end{pmatrix}.
\]
Per il lemma del determinante (o sua forma rettangolare),
\[
\det A=(-2N)^5
\det\left(I_2-\frac{1}{2N}CG\right).
\]
Il determinante ridotto, calcolato esplicitamente, è
\[
\det\left(I_2-\frac{1}{2N}CG\right)
=-\frac{2Ns-N-2s|t|^2+4s^2-2s}{N}.
\]
Usando \(N=1-2s+|t|^2\), il numeratore tra parentesi si riduce a
\[
2Ns-N-2s|t|^2+4s^2-2s=2s-|t|^2-1=-N.
\]
Quindi il determinante ridotto vale 1 e
\[
\boxed{\det A=(-2N)^5.}
\]
Ne segue
\[
\det g
=\left(-\frac5{N^2}\right)^5\det A
=\frac{5^5 2^5}{N^5}
=\frac{10^5}{N^5}.
\]
Il calcolo vale dove si applica direttamente il lemma; l'identità si estende per continuità ai punti rimanenti del dominio.

## 4. Conseguenza per la misura

Per la convenzione adottata,
\[
dV_g=2^5\det(g)\,d^{10}z
=\frac{2^5 10^5}{N^5}d^{10}z
=N^{-5}(20^5d^{10}z).
\]
Dunque
\[
\boxed{dV_g=N^{-5}d\mu_0.}
\]
Questa è la relazione precisa fra volume metrico di Bergman e volume piatto nella carta \(D_5\), con le normalizzazioni dichiarate.

## 5. Cosa segue — e cosa non segue — per Liouville e Wilson

- **Segue:** una volta identificata la carta complessa \(D_5\) e fissata la normalizzazione del volume piatto, la densità di Bergman è esattamente \(N^{-5}\) rispetto a quel volume.
- **Non segue:** il teorema di Liouville non produce da solo il fattore \(N^{-5}\). Liouville conserva il volume simplettico della dinamica hamiltoniana; il fattore qui deriva dal determinante della metrica.
- **Non segue:** non è dimostrato che la marginalizzazione dei gradi di libertà Wilson di Q6 induca questa misura, né che il dominio \(D_5\) sia il suo spazio efficace.
- **Non segue:** non è stata determinata una soglia/cutoff fisica Hua. Non si deve sceglierla per adattare il valore di Wyler.

Il ponte ancora da dimostrare è quindi una mappa (o limite di mappe) dal settore efficace Wilson/PSU alla carta \(D_5\), con controllo della misura push-forward e della convergenza. T002 fornisce il lato geometrico del confronto, non il lato dinamico.

## 6. Riferimenti

- L. K. Hua, *Harmonic Analysis of Functions of Several Complex Variables in the Classical Domains*, American Mathematical Society, 1963.
- S. Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, Academic Press, 1978.
- J. Faraut e A. Korányi, *Analysis on Symmetric Cones*, Oxford University Press, 1994.

I riferimenti riguardano domini simmetrici, funzioni di Bergman e geometria; non sono presentati come prova di un'identificazione fisica con PSU o Q6.
