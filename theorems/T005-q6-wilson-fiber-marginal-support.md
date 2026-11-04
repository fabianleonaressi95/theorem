# T005 — Marginale Wilson Q6: formula esatta e assenza di cutoff a beta finito

**Stato: DIMOSTRATO (identità di Fourier–Haar e positività).**  
**Esito del test sui pesi Wilson effettivi:** la marginale elettrica a cinque modi è strettamente positiva su ogni classe del quoziente a ogni \(\beta>0\). Quindi non seleziona un cutoff duro Hua a accoppiamento finito.

## 1. Dati e definizioni

Sia \(C\in\mathbb Z^{129\times192}\) la matrice dei cicli fondamentali del complesso Q6. Sia
\[
\Pi_5:\mathbb Z^{129}\to\mathbb Q^5
\]
la mappa intera-razionale di rango 5 ottenuta componendo il flusso di ciclo con il settore coesatto selezionato. Indichiamo con
\[
K_{\mathbb Z}=\ker_{\mathbb Z}(\Pi_5),\qquad
L=K_{\mathbb Z}C\subset\mathbb Z^{192}
\]
il kernel saturo di rango 124 e la sua immagine nel reticolo dei flussi sui 192 lati.

Per \(\beta>0\), definiamo
\[
w_\beta(n)=\prod_{e=1}^{192}
\frac{I_{|n_e|}(\beta)}{I_0(\beta)},
\qquad n\in\mathbb Z^{192},
\]
e per una classe rappresentata da \(c\in\mathbb Z^{129}\)
\[
W_\beta([c])=
\sum_{k\in K_{\mathbb Z}}w_\beta((c+k)C).
\]
La somma è assolutamente convergente per il maggiorante fattoriale Bessel del kernel Q6.

## 2. Teorema

Per ogni \(\beta>0\) e ogni classe \([c]\in\mathbb Z^{129}/K_{\mathbb Z}\):

1. \(W_\beta([c])\) è finita e strettamente positiva;
2. è indipendente dal rappresentante della classe;
3. ammette la rappresentazione esatta
   \[
   \boxed{
   W_\beta([c])=
   \int_{H_L}
   \prod_{e=1}^{192}\frac{e^{\beta\cos x_e}}{I_0(\beta)}
   \,e^{-i(cC)\cdot x}\,d\mu_{H_L}(x),
   }
   \]
   dove
   \[
   H_L=\{x\in\mathbb T^{192}:
   \ell\cdot x=0\pmod{2\pi}\quad
   \forall\ell\in L\}
   \]
   e \(\mu_{H_L}\) è la misura di Haar normalizzata;
4. non esiste alcuna classe esclusa dal supporto della marginale: \(W_\beta([c])>0\) per tutte le classi.

## 3. Dimostrazione

**Convergenza e positività.** Per ogni intero \(m\geq0\) e \(\beta>0\), la serie definente la funzione di Bessel modificata dà \(I_m(\beta)>0\). Quindi ogni termine \(w_\beta(n)\) è positivo. La convergenza assoluta della somma sulle fibre segue dal maggiorante
\[
w_\beta(n)\leq
\frac{(\beta/2)^{\|n\|_1}}{\prod_e|n_e|!}
\]
e dal conteggio dei vettori interi a norma \(\ell^1\) fissata, come nel maggiorante globale Q6. Ne segue che \(0<W_\beta([c])<\infty\).

**Indipendenza dal rappresentante.** Se \(c'=c+k_0\), con \(k_0\in K_{\mathbb Z}\), allora la sostituzione \(k\mapsto k+k_0\) permuta il kernel intero nella somma. Dunque \(W_\beta([c'])=W_\beta([c])\).

**Formula di Fourier–Haar.** La funzione
\[
f_\beta(x)=\prod_{e=1}^{192}
\frac{e^{\beta\cos x_e}}{I_0(\beta)}
\]
ha serie di Fourier assolutamente convergente
\[
f_\beta(x)=\sum_{n\in\mathbb Z^{192}}
w_\beta(n)e^{in\cdot x}.
\]
Per ortogonalità dei caratteri sul sottogruppo compatto \(H_L\),
\[
\int_{H_L}e^{i(n-cC)\cdot x}\,d\mu_{H_L}(x)
=
\begin{cases}
1,&n-cC\in L,\\
0,&n-cC\notin L.
\end{cases}
\]
Integrando la serie (lecita per convergenza assoluta), sopravvivono esattamente i termini \(n=(c+k)C\), e si ottiene la formula incorniciata.

Infine, la positività del peso della classe è già stabilita dalla somma di termini strettamente positivi, che include almeno il termine \(k=0\). \(\square\)

## 4. Applicazione: il cutoff Hua non è generato a beta finito

La misura marginale normalizzata sul reticolo delle classi assegna massa positiva a ogni classe. Di conseguenza, a \(\beta\) finito non può avere supporto limitato a
\[
\{z\in D_5:N(z)\geq\epsilon\}
\]
se esistono classi del reticolo mappate nella regione \(N(z)<\epsilon\). In particolare, il peso Wilson non contiene un meccanismo di cancellazione o annullamento esatto delle classi: tutti i coefficienti Bessel sono positivi.

Quindi:

- **Escluso:** un cutoff duro Hua ottenuto semplicemente dalla marginalizzazione elettrica esatta a \(\beta>0\).
- **Non escluso:** concentrazione asintotica, perdita di massa in certe regioni o un cutoff emergente in un limite congiunto di scala e accoppiamento; ciascuno richiede una dimostrazione di convergenza.
- **Non dimostrato:** che i pesi normalizzati tendano localmente a \(N^{-5}\). La positività non implica quella legge di densità.

## 5. Perché questo non è ancora T004 applicato a Wilson

La mappa \(\Pi_5\) produce un reticolo numerabile di rango 5 nel settore elettrico. Il suo supporto non è una griglia a passo isotropo in \(\mathbb R^{10}\). La marginalizzazione integra/somma i 124 gradi interi complementari, ma non crea da sola le cinque coordinate canoniche coniugate \(q\).

Il teorema locale Q6–D5 già disponibile fornisce una carta lineare
\[
(q,p)\in\mathbb R^5\times\mathbb R^5\longleftrightarrow z\in\mathbb C^5
\]
e l'identità
\[
\Phi^*(dV_B)=N(\Phi(q,p))^{-5}d\mu_L.
\]
Ma T005 non identifica la marginale Wilson con \(d\mu_L\), né costruisce il settore \(q\). Pertanto non si può applicare T004 ai pesi Wilson senza prima derivare tale struttura.

## 6. Conclusione del test effettivo

Il test matematico sui pesi Wilson disponibili dà un risultato netto:

\[
\boxed{W_\beta([c])>0\quad
\text{per ogni classe e ogni }\beta>0.}
\]

La marginale completa esiste, è una formula di Fourier–Haar esatta su \(H_L\cong\mathbb T^{68}\) per il reticolo Q6 auditato, ma non seleziona un cutoff Hua a accoppiamento finito. Il fattore \(N^{-5}\) rimane una densità geometrica del settore D5, non ancora la densità derivata dalla marginale Wilson.

## 7. Provenienza e riferimenti

Le costruzioni Q6-specifiche sono documentate nel repository di ricerca:
- `docs/Q6_D5_INTEGER_FIBER_QUOTIENT.md` — mappa razionale, kernel saturo e marginale sulle fibre;
- `docs/Q6_D5_SATURATED_KERNEL_AND_TAIL_BOUND.md` — convergenza assoluta e maggiorante globale;
- `docs/Q6_D5_WILSON_FIVE_TORUS_MARGINAL.md` — identità esatta Fourier–Haar e torus \(H_L\cong\mathbb T^{68}\).

Riferimenti matematici:
- NIST Digital Library of Mathematical Functions, §§10.25 e 10.35 — positività/serie e generatrice di Fourier delle \(I_n\): https://dlmf.nist.gov/10.25 e https://dlmf.nist.gov/10.35.
- W. Rudin, *Fourier Analysis on Groups*, Wiley, 1962 — ortogonalità dei caratteri e misura di Haar.
- FLINT, *Hermite and Smith normal forms* — struttura del kernel intero e invarianti di Smith: https://flintlib.org/doc/algorithms/linear-algebra/hermite-smith.html.

I riferimenti sostengono gli strumenti generali. La dimostrazione sopra specifica il risultato per la marginale Wilson Q6.
