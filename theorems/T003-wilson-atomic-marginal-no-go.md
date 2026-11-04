# T003 — No-go per l'identificazione esatta fra marginale Wilson finita e misura di Bergman

**Stato: DIMOSTRATO sotto le ipotesi esplicitate.**  
**Ruolo nel programma RGS–PSU–PRISM: esclude un'identificazione esatta a cutoff finito ottenuta come push-forward/marginalizzazione di flussi interi su un numero finito di gradi di libertà. Non esclude un limite debole continuo.**

## 1. Enunciato

Sia \(\mathcal F\cong\mathbb Z^m\) un insieme numerabile di configurazioni di flusso intero (per il settore Q6 considerato, \(m\) è finito; il sottospazio di Gauss è un sottoinsieme numerabile). Sia
\[
w:\mathcal F\longrightarrow[0,\infty),\qquad
0<Z:=\sum_{n\in\mathcal F}w(n)<\infty,
\]
un peso Wilson normalizzabile.

Sia \(\Pi:\mathcal F\to D_5\subset\mathbb C^5\) una qualunque mappa, non necessariamente iniettiva. Definiamo la misura marginale push-forward
\[
\mu_\Pi:=\Pi_*\left(\frac1Z\sum_{n\in\mathcal F}
w(n)\,\delta_n\right).
\]
Allora \(\mu_\Pi\) è una misura puramente atomica, concentrata sull'insieme numerabile \(\Pi(\mathcal F)\).

In particolare, se \(\nu_B\) è una misura di Bergman troncata non nulla, assolutamente continua rispetto al volume euclideo su \(D_5\), per esempio
\[
d\nu_B(z)=C_\epsilon\,
\mathbf1_{\{N(z)\ge\epsilon\}}N(z)^{-5}\,d^{10}z
\]
su una regione di volume positivo, con \(C_\epsilon>0\), allora
\[
\boxed{\mu_\Pi\ne\nu_B.}
\]

La conclusione vale anche quando si sommano esattamente tutti i flussi appartenenti alla stessa fibra di \(\Pi\).

## 2. Dimostrazione

Per ogni boreliano \(A\subset D_5\), dalla definizione di push-forward,
\[
\mu_\Pi(A)
=\frac1Z\sum_{n\in\mathcal F}
w(n)\,\mathbf1_A(\Pi(n)).
\]
Raggruppando i termini con la stessa immagine \(y=\Pi(n)\), otteniamo
\[
\mu_\Pi
=\sum_{y\in\Pi(\mathcal F)}a_y\,\delta_y,
\qquad
a_y=\frac1Z\sum_{n:\Pi(n)=y}w(n).
\]
La somma definente \(a_y\) converge perché è dominata dalla somma totale \(Z\). Inoltre \(\Pi(\mathcal F)\) è numerabile, essendo immagine di un insieme numerabile. Dunque \(\mu_\Pi\) è concentrata su un insieme numerabile.

Un insieme numerabile in \(\mathbb R^{10}\) ha misura di Lebesgue nulla. Perciò ogni misura assolutamente continua rispetto a \(d^{10}z\) assegna massa zero a \(\Pi(\mathcal F)\), mentre
\[
\mu_\Pi(\Pi(\mathcal F))=1.
\]
Le due misure non possono quindi coincidere. \(\square\)

## 3. Applicazione al quoziente dei flussi Q6

Nel caso di una proiezione intera
\[
\Pi_5:\mathbb Z^{129}\longrightarrow\mathbb Q^5
\]
di rango 5, il quoziente ha immagine numerabile. Se il peso è il coefficiente di flusso Wilson, eventualmente ristretto ai flussi che soddisfano il vincolo di Gauss, la marginalizzazione esatta sulle fibre produce
\[
W(y)=\sum_{n:\Pi_5(n)=y}w(n),\qquad
\mu_5=\frac1Z\sum_{y\in\Pi_5(\mathbb Z^{129})}
W(y)\,\delta_y.
\]
La somma sulle fibre non rende continua la misura: modifica i pesi degli atomi, non il loro supporto numerabile.

Questo argomento non richiede che il peso sia prodotto di funzioni di Bessel, né che la proiezione sia lineare; richiede soltanto numerabilità dello spazio dei flussi e normalizzabilità del peso. Le specifiche Wilson determinano i valori di \(W(y)\), ma non cambiano questa conclusione.

## 4. Conseguenze precise

1. **Escluso:** a numero finito di gradi di libertà, una marginalizzazione esatta di flussi interi seguita da una mappa deterministica in \(D_5\) non può essere esattamente la misura continua di Bergman \(N^{-5}d^{10}z\), né una sua troncatura non nulla.
2. **Non escluso:** una successione di misure atomiche può convergere debolmente a una misura assolutamente continua. La densità continua può emergere solo in un limite, non come identità esatta a cutoff finito.
3. **Non dimostrato:** che la successione Wilson–Q6 scelta sia tight, converga debolmente o abbia limite Bergman.
4. **Non dimostrato:** che il cutoff \(\epsilon\) sia determinato dinamicamente. Non può essere fissato per adattare il valore di Wyler.

## 5. Cosa serve per il teorema successivo

Per dimostrare un limite Bergman occorre specificare una famiglia di misure \(\mu_a\) e mappe \(\Pi_a\), con parametro di raffinamento/scala \(a\), e provare almeno:

- tightness (o una condizione equivalente che impedisca la fuga di massa);
- identificazione del limite su una classe determinante di funzioni test;
- derivazione del fattore limite \(N^{-5}\) e della regione di supporto dal peso e dalla dinamica, non da un fit.

Il solo conteggio dei flussi, la convergenza puntuale dei pesi o una somma finita su fibre non bastano.

## 6. Riferimenti matematici

- P. Billingsley, *Convergence of Probability Measures*, 2nd ed., Wiley, 1999 — misure push-forward e convergenza debole.
- V. I. Bogachev, *Measure Theory*, Vol. I, Springer, 2007 — misure atomiche, assoluta continuità e decomposizione di misure.

I riferimenti sostengono i concetti generali di teoria della misura; la dimostrazione del no-go è fornita integralmente sopra.
