# T006 — Il quoziente del toro di annichilazione Q6 è esattamente un 5-toro

**Stato: DIMOSTRATO (dualitá dei caratteri e reticoli interi).**  
**Risultato:** il toro di annichilazione di dimensione 68, dopo il quoziente per le trasformazioni di gauge ai vertici, è un 5-toro. La marginale Wilson completa può quindi essere riscritta come coefficiente di Fourier di una funzione gauge-averaged su un 5-toro. Non è necessario integrare numericamente su 68 variabili.

## 1. Dati interi

Sia \(Q_6\) il complesso cubico con 64 vertici e 192 lati. La matrice di incidenza ai vertici è
\[
D_0\in\mathbb Z^{64\times192}.
\]
Il grafo è connesso, dunque
\[
\operatorname{rank}D_0=63,
\qquad
Z_1:=\ker(D_0:\mathbb Z^{192}\to\mathbb Z^{64})
\]
è un reticolo libero di rango 129.

Sia
\[
C:\mathbb Z^{129}\overset{\cong}{\longrightarrow}Z_1
\]
una base intera fondamentale del reticolo dei cicli. La mappa dei cinque modi è
\[
P:\mathbb Z^{129}\longrightarrow\mathbb Q^5,
\qquad
P(c)=cM,
\]
con \(\operatorname{rank}_{\mathbb Q}M=5\). Definiamo il kernel intero saturo
\[
K=\ker(P:\mathbb Z^{129}\to\mathbb Q^5).
\]
Essendo il kernel di una mappa verso un gruppo additivo senza torsione, \(K\) è saturo; inoltre \(\operatorname{rank}K=124\).

Nel reticolo dei flussi sui lati poniamo
\[
L=K C\subset Z_1\subset\mathbb Z^{192}.
\]

## 2. I due sottogruppi compatti

Siano
\[
\mathbb T^{192}=\mathbb R^{192}/2\pi\mathbb Z^{192},
\]
\[
G=\operatorname{im}(D_0^T:\mathbb T^{64}\to\mathbb T^{192})
\]
il sottogruppo delle trasformazioni di gauge ai vertici, e
\[
H_L=\{x\in\mathbb T^{192}:
\ell\cdot x=0\pmod{2\pi}\quad\forall\ell\in L\}
\]
il toro annichilatore della fibra Wilson.

Poiché ogni \(\ell\in L\) è un ciclo,
\[
\ell\cdot D_0^T\theta=(D_0\ell)\cdot\theta=0.
\]
Quindi \(G\subset H_L\). Inoltre \(\dim G=63\) e \(\dim H_L=192-124=68\).

## 3. Teorema

Il quoziente compatto
\[
\boxed{H_L/G\cong\mathbb T^5}
\]
è un 5-toro con reticolo dei caratteri isomorfo a
\[
\boxed{Z_1/L\cong\mathbb Z^{129}/K.}
\]

In particolare non compare alcun gruppo finito residuo: il quoziente è connesso.

## 4. Dimostrazione

Per un sottogruppo chiuso \(H\subset\mathbb T^{192}\), indichiamo con
\[
H^\perp=\{n\in\mathbb Z^{192}:
e^{in\cdot x}=1\quad\forall x\in H\}
\]
il suo annichilatore nel reticolo dei caratteri.

Per definizione,
\[
H_L^\perp=L.
\]
Per il sottogruppo di gauge,
\[
G^\perp=\ker(D_0:\mathbb Z^{192}\to\mathbb Z^{64})=Z_1,
\]
poiché
\[
e^{in\cdot D_0^T\theta}=e^{i(D_0n)\cdot\theta}
\]
è identicamente uno se e solo se \(D_0n=0\).

La dualità dei caratteri per il quoziente dà
\[
(H_L/G)^\wedge\cong G^\perp/H_L^\perp
=Z_1/L.
\]
Ma la base fondamentale \(C\) identifica integralmente
\[
Z_1/L\cong
\mathbb Z^{129}/K.
\]
Infine, per il primo teorema di isomorfismo,
\[
\mathbb Z^{129}/K\cong P(\mathbb Z^{129})\subset\mathbb Q^5.
\]
Il gruppo \(P(\mathbb Z^{129})\) è finitamente generato, senza torsione e di rango 5; pertanto è isomorfo a \(\mathbb Z^5\). Il duale compatto è quindi \(\mathbb T^5\). Questo dimostra anche la connessione e l'assenza di componenti finite. \(\square\)

## 5. Formula Wilson esatta sul 5-toro

Per \(\beta>0\), definiamo la funzione positiva e continua su \(\mathbb T^{192}\)
\[
f_\beta(x)=\prod_{e=1}^{192}
\frac{e^{\beta\cos x_e}}{I_0(\beta)}.
\]
Non è invariante sotto gauge in generale. La sua media gauge è però ben definita:
\[
\bar f_\beta([x])=
\int_G f_\beta(x+g)\,d\mu_G(g),
\qquad [x]\in H_L/G.
\]
È una funzione positiva e continua sul 5-toro.

Per una classe \([c]\in\mathbb Z^{129}/K\), il carattere corrispondente è
\[
\chi_{[c]}([x])=e^{-i(cC)\cdot x}.
\]
È ben definito su \(H_L/G\): cambiare \(c\) di un elemento di \(K\) non cambia il carattere su \(H_L\), e i caratteri ciclici sono invarianti sotto gauge.

La formula Fourier–Haar di T005 e l'integrazione sulle fibre del quoziente danno
\[
\boxed{
W_\beta([c])=
\int_{H_L/G}
\bar f_\beta([x])\,
\chi_{[c]}([x])\,
d\mu_{H_L/G}([x]).
}
\]
Qui la misura di Haar del quoziente è normalizzata. La media gauge è essenziale: non si può trattare \(f_\beta\) come se fosse già gauge-invariante.

**Conseguenza:** il problema della marginale completa non richiede una QMC su \(\mathbb T^{68}\). La stessa quantità è un coefficiente di Fourier di una funzione gauge-averaged su \(\mathbb T^5\). Questa riduzione è esatta, non un'approssimazione numerica.

## 6. Cosa non segue

Il teorema identifica il gruppo compatto efficace e la sua misura di Haar, ma non dimostra ancora:
- che \(\bar f_\beta\) abbia simmetria del dominio di Cartan \(D_5\);
- che la sua densità, in coordinate canoniche, sia \(N(z)^{-5}\);
- che esista un limite di raffinamento con convergenza debole verso la misura di Bergman;
- che il parametro di cutoff Hua sia selezionato dalla dinamica Wilson.

La riduzione a cinque variabili elimina un ostacolo dimensionale della formulazione precedente. Il passo successivo è determinare esplicitamente la media gauge \(\bar f_\beta\), e confrontarne le simmetrie e i coefficienti con la densità di Hua, senza imporre un fattore \(N^{-5}\).

## 7. Riferimenti

- D. L. Pontryagin, *The Theory of Topological Commutative Groups*, 1939; dualità dei caratteri per gruppi abeliani compatti.
- W. Rudin, *Fourier Analysis on Groups*, Wiley, 1962; annichilatori, quozienti e ortogonalità di Haar.
- NIST Digital Library of Mathematical Functions, §§10.25 e 10.35; serie e generatrice delle funzioni di Bessel modificate: https://dlmf.nist.gov/10.25 e https://dlmf.nist.gov/10.35.
- Documentazione Q6 del progetto: `docs/Q6_D5_INTEGER_FIBER_QUOTIENT.md`, `docs/Q6_D5_SATURATED_KERNEL_AND_TAIL_BOUND.md`, `docs/Q6_D5_WILSON_FIVE_TORUS_MARGINAL.md`, `docs/Q6_GLOBAL_TORUS_STRUCTURE.md`.

Le fonti esterne forniscono la dualità astratta e le identità di Bessel. La specifica identificazione \(H_L/G\cong\mathbb T^5\) segue dalla struttura intera Q6 e dal kernel saturo del proiettore a cinque modi.
