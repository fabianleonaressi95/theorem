# T004 — Convergenza delle somme di Riemann alla misura di Bergman troncata

**Stato: DIMOSTRATO (teorema di approssimazione geometrica).**  
**Non è ancora un teorema Wilson.** Stabilisce un criterio concreto per ottenere la misura continua di Bergman da misure atomiche; individua quindi la condizione locale che una marginalizzazione Wilson dovrebbe soddisfare.

## 1. Enunciato

Sia \(D_5\subset\mathbb C^5\simeq\mathbb R^{10}\) il dominio di tipo IV e
\[
N(z)=1-2z^\dagger z+|z^Tz|^2.
\]
Fissiamo \(\epsilon>0\) e poniamo
\[
K_\epsilon=\{z\in D_5:N(z)\geq\epsilon\}.
\]
Supponiamo che \(K_\epsilon\) sia limitato e che il suo bordo abbia misura di Lebesgue nulla. Definiamo
\[
f_\epsilon(z)=\mathbf1_{K_\epsilon}(z)N(z)^{-5},
\qquad
Z_\epsilon=\int_{K_\epsilon}N(z)^{-5}\,d^{10}z.
\]
Assumiamo \(0<Z_\epsilon<\infty\).

Sia \(h_k\downarrow0\) una successione di passi di griglia e sia
\[
\Lambda_k=h_k\mathbb Z^{10}.
\]
Definiamo la misura atomica non normalizzata
\[
\rho_k=h_k^{10}\sum_{x\in\Lambda_k\cap K_\epsilon}
N(x)^{-5}\,\delta_x
\]
e la sua normalizzazione
\[
\mu_k=\frac{\rho_k}{\rho_k(K_\epsilon)}.
\]
Allora
\[
\boxed{\mu_k\Rightarrow
\nu_\epsilon
=\frac{\mathbf1_{K_\epsilon}(z)N(z)^{-5}}
{Z_\epsilon}\,d^{10}z.}
\]
Qui \(\Rightarrow\) indica convergenza debole di probabilità.

## 2. Dimostrazione

Poiché \(N\) è continua e \(N\geq\epsilon\) su \(K_\epsilon\), la funzione \(N^{-5}\) è continua e limitata su tale insieme. Il bordo di \(K_\epsilon\) ha misura nulla; pertanto la funzione \(f_\epsilon\), estesa con zero fuori da \(K_\epsilon\), è Riemann-integrabile su ogni rettangolo limitato che contiene \(K_\epsilon\).

Per il teorema delle somme di Riemann in dimensione 10,
\[
h_k^{10}\sum_{x\in h_k\mathbb Z^{10}}
f_\epsilon(x)
\longrightarrow
\int_{\mathbb R^{10}}f_\epsilon(z)\,d^{10}z
=Z_\epsilon.
\]
Più in generale, per ogni funzione continua e limitata \(\varphi\) su un compatto che contiene \(K_\epsilon\), il prodotto \(\varphi f_\epsilon\) è Riemann-integrabile e
\[
\int\varphi\,d\rho_k
=h_k^{10}\sum_{x\in h_k\mathbb Z^{10}}
\varphi(x)f_\epsilon(x)
\longrightarrow
\int_{K_\epsilon}\varphi(z)N(z)^{-5}\,d^{10}z.
\]
In particolare, scegliendo \(\varphi=1\), si ha
\[
\rho_k(K_\epsilon)\longrightarrow Z_\epsilon>0.
\]
Possiamo quindi dividere per le masse totali. Per ogni funzione continua limitata \(\varphi\),
\[
\begin{aligned}
\int\varphi\,d\mu_k
&=\frac{\int\varphi\,d\rho_k}{\rho_k(K_\epsilon)}\\
&\longrightarrow
\frac1{Z_\epsilon}
\int_{K_\epsilon}\varphi(z)N(z)^{-5}\,d^{10}z
=\int\varphi\,d\nu_\epsilon.
\end{aligned}
\]
Questa è precisamente la convergenza debole dichiarata. \(\square\)

## 3. Che cosa dimostra rispetto a T003

T003 dimostra che ogni marginale atomica a scala finita non può essere esattamente la misura continua di Bergman. T004 mostra che questo fatto non impedisce la convergenza:
\[
\text{misure atomiche }\mu_k
\quad\xRightarrow[k\to\infty]{}
\quad
\text{misura continua }\nu_\epsilon.
\]
La continuità emerge nel limite perché il passo della griglia tende a zero e i pesi sono campioni della densità \(N^{-5}\).

## 4. Il test che deve superare la marginalizzazione Wilson

Per applicare T004 a Q6 non basta sapere che i flussi sono interi o che la proiezione ha rango 5. Occorre costruire, per ogni scala \(k\):

1. una mappa di scala \(\Pi_k\) dai flussi ammessi alle posizioni \(z_{k,n}\in D_5\);
2. il peso marginale effettivo
   \[
   W_k(z_{k,n})=
   \sum_{n':\Pi_k(n')=z_{k,n}}w_k(n');
   \]
3. una normalizzazione \(Z_k=\sum_z W_k(z)\);
4. una dimostrazione che, per ogni funzione test continua \(\varphi\),
   \[
   \frac{1}{Z_k}\sum_zW_k(z)\varphi(z)
   \longrightarrow
   \frac{1}{Z_\epsilon}
   \int_{K_\epsilon}\varphi(z)N(z)^{-5}\,d^{10}z.
   \]

In termini locali, una condizione sufficiente è che i pesi normalizzati delle celle convergano alle masse
\[
\frac1{Z_\epsilon}
\int_{C_{k,z}\cap K_\epsilon}N(u)^{-5}\,d^{10}u
\]
con errore totale che tende a zero. T004 dimostra la convergenza se questa struttura di pesi è presente; non dimostra che i coefficienti Wilson la generino.

## 5. Limite decisivo

La dimostrazione sopra usa una griglia euclidea e inserisce esplicitamente \(N^{-5}\) nei pesi. È un teorema matematico di controllo, **non** una derivazione fisica della misura.

Per ottenere il risultato richiesto dal programma, il prossimo passo non è adattare la griglia: è calcolare i pesi Wilson marginali e provare che il loro rapporto con le masse delle celle tende proprio a \(N^{-5}\), mentre il supporto limite e l'eventuale cutoff emergono dal modello. Se ciò non accade, l'identificazione Wilson–Bergman è falsa per quella scelta di mappa e di scala.

Inoltre, \(\epsilon\) è qui fissato dall'esterno. Questo teorema non determina il cutoff Hua e non consente di usarlo per calibrare la costante di struttura fine.

## 6. Riferimenti

- G. B. Folland, *Real Analysis: Modern Techniques and Their Applications*, 2nd ed., Wiley, 1999 — integrazione e approssimazione di Riemann.
- P. Billingsley, *Convergence of Probability Measures*, 2nd ed., Wiley, 1999 — convergenza debole di misure di probabilità.

La dimostrazione è autosufficiente; i riferimenti sono per il contesto generale.
