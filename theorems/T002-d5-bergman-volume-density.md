# T002 — Volume di Bergman sul dominio di tipo IV in dimensione 5

**Stato: DIMOSTRATO (identità geometrica esplicita).**  
**Ruolo nel programma RGS–PSU–PRISM: identifica esattamente la densità di Bergman con una densità rispetto al volume euclideo/simplettico in coordinate; non dimostra che tale densità sia prodotta dalla marginalizzazione Wilson.**

## 1. Enunciato

Sia
\[
D_5=\{z\in\mathbb C^5:
N(z)=1-2z^\dagger z+|z^Tz|^2>0,\quad |z^Tz|<1\}
\]
il dominio limitato irriducibile di tipo IV (dominio di Lie) in dimensione complessa 5. Poniamo
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
Qui \(d^{10}z\) è il volume euclideo su \(\mathbb C^5\simeq\mathbb R^{10}\). Se le coordinate sono normalizzate come coordinate canoniche \((q,p)\) tramite \(z=(q+ip)/\sqrt{2}\), allora \(d\mu_0\) è una costante convenzionale per la misura di Liouville. La costante dipende dalla normalizzazione scelta per \(q,p,z\), mentre il fattore non costante \(N^{-5}\) è quello geometrico.

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

## 3. Identità determinante

L'identità algebrica necessaria è
\[
\boxed{\det A=(-2)^5N^5.}
\]

La si verifica applicando il lemma del determinante
\[
\det(M+UV^T)=\det(M)\det(I+V^TM^{-1}U)
\]
a \(M=-2NI_5\). Infatti, ponendo \(v=z\), \(w=\bar z\), la matrice \(A\) è una perturbazione di \(-2NI_5\) di rango al più due, perché
\[
A=-2NI_5+4Nvw^T
-4(w-\bar t v)(v^T-tw^T).
\]
Si applica quindi il lemma nella forma a rango due, riducendo il determinante a quello di una matrice \(2\times2\). Sostituendo
\[
v^Tv=t,\quad w^Tw=\bar t,\quad v^Tw=w^Tv=s,
\]
e \(N=1-2s+t\bar t\), il determinante ridotto si semplifica in \(N^5\); il fattore proveniente da \(-2NI_5\) dà precisamente
\[
\det A=(-2N)^5\frac{N^5}{N^5}=(-2)^5N^5.
\]
Questa è un'identità polinomiale, valida su tutto il dominio (e per continuità anche nei punti in cui la rappresentazione intermedia del lemma usa una matrice singolare).

Ne segue
\[
\det g
=\left(-\frac5{N^2}\right)^5\det A
=\frac{5^5\,2^5}{N^5}
=\frac{10^5}{N^5}.
\]
La positività della metrica sul dominio scelto è quella della metrica di Bergman del dominio di tipo IV; il calcolo determina il suo determinante nella normalizzazione qui fissata.

## 4. Conseguenza per la misura

Per definizione della convenzione adottata,
\[
dV_g=2^5\det(g)\,d^{10}z
=\frac{2^5 10^5}{N^5}d^{10}z
=N^{-5}(20^5d^{10}z).
\]
Dunque
\[
\boxed{dV_g=N^{-5}d\mu_0.}
\]
Questa è la relazione precisa fra volume di Bergman e volume piatto nella carta \(D_5\). Non è un'uguaglianza fra due misure invarianti senza specificare la carta e la normalizzazione.

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

I riferimenti riguardano domini simmetrici, loro funzioni di Bergman e geometria; non sono presentati come prova di un'identificazione fisica con PSU o Q6.
