# Audit matematico indipendente: Herasymov / fractogenesis

**Oggetto:** `xcontcom/fractogenesis`, sorgenti `2d-ca/draw.js` e `3d-ca/draw.js`.  
**Scopo:** ricostruire le regole locali, verificare gli indici, isolare la simmetria cubica e delimitare ciò che può essere collegato rigorosamente a quaternioni, qutrit e RGS.

## 1. Esito sintetico

| Punto | Esito | Stato |
|---|---|---|
| Classificazione 2D | (q_2=9c+s_2), 18 classi | Verificato dal sorgente |
| Classificazione 3D | (q_3=27c+s_3), 54 classi | Verificato dal sorgente |
| Accesso fuori indice nella tabella 3D | Nessuno: (q_3\in\{0,\ldots,53\}) | Correzione di una precedente lettura errata |
| Equivarianza della regola locale 3D | Esatta per il gruppo cubico, con reticolo periodico | Dimostrata |
| Equivarianza del padding 3D `kk=0` | Esatta per l'azione lineare sull'origine degli indici qui definita | Dimostrata |
| Legame nativo con quaternioni/SU(2) | Non presente nel codice esaminato | Non dimostrato |
| Qutrit nativo | Non presente: stati cellulari binari | Non dimostrato |
| Ricorrenza supergolden (x^3-x^2-1=0) | Non deducibile dal solo codice esaminato | Aperto |

## 2. Ricostruzione delle regole locali

Sia (c\in\{0,1\}) lo stato della cella centrale e sia (s_d) il numero di celle attive tra i vicini di Moore in dimensione (d). Il codice costruisce l'indice

[
q_d=3^d c+s_d.
]

Poiché (0\leq s_d\leq 3^d-1), gli indici possibili sono

[
q_d\in\{0,\ldots,2\cdot3^d-1\}.
]

Ne segue che il numero di classi è (N_d=2\cdot3^d): 18 in 2D e 54 in 3D.

### 2.1 Caso 2D

La cella centrale è codificata separatamente dal conteggio dei vicini. La somma dei vicini di Moore esclude il centro e varia da 0 a 8. L'indice è dunque (q_2=9c+s_2), con intervallo 0–17. La tabella di 18 elementi è dimensionata correttamente.

### 2.2 Caso 3D

Il codice somma i 26 vicini e aggiunge (27c). Quindi (q_3=27c+s_3), con (s_3\in[0,26]). Se (c=0), (q_3\in[0,26]); se (c=1), (q_3\in[27,53]). La tabella di 54 elementi è corretta: non esiste accesso a (r[54]), né una classe 27 irraggiungibile.

La formula unificata è una proprietà combinatoria della codifica totalistica; non significa che le tabelle casuali 2D e 3D siano restrizioni della stessa legge dimensionale. I valori casuali sono generati separatamente.

## 3. Equivarianza cubica della regola 3D

Sia (Lambda_L=(\mathbb Z/L\mathbb Z)^3), con condizioni periodiche. Sia (O) il gruppo delle 24 matrici di permutazione con segni, a coefficienti interi, determinante (+1) (rotazioni proprie del cubo).

Per una configurazione (a:\Lambda_L\to\{0,1\}), definiamo l'azione

[
(Ra)(Rx)=a(x).
]

La regola locale dipende soltanto da:
1. il valore (c=a(x)) al centro;
2. la somma (s_3(x)) dei 26 vicini.

Ogni (R\in O) permuta l'insieme dei 26 vettori di vicinato e preserva il centro. Quindi

[
c_{Ra}(Rx)=c_a(x),\qquad s_{Ra}(Rx)=s_a(x).
]

Per qualunque tabella fissa (r:\{0,\ldots,53\}\to\{0,1\}),

[
\boxed{F_r(Ra)=R F_r(a).}
]

La conclusione non richiede che la tabella sia casuale o simmetrica: segue dalla dipendenza esclusiva da (c) e dal conteggio dei vicini. Vale anche per le 48 simmetrie del cubo se si include il gruppo completo (O_h).

## 4. Equivarianza del padding 3D

Il padding sorgente con `kk=0` colloca ogni cella parentale (x\in\Lambda_L) nel sito (2x\in\Lambda_{2L}) e pone a zero gli altri sette siti del blocco (2\times2\times2):

[
(Pa)(2x)=a(x),\qquad
(Pa)(y)=0\quad\text{se }y\notin 2\Lambda_L.
]

Con l'azione di rotazione sull'origine degli indici, (R(2x)=2(Rx)) modulo (2L). Pertanto

[
\boxed{P(Ra)=R(Pa).}
]

Questa è una conclusione precisa per la convenzione di coordinate dichiarata. Non autorizza a ignorare eventuali traslazioni o convenzioni diverse per i centri geometrici delle celle: se si adotta un'azione affine diversa, la compatibilità va ricalcolata.

Di conseguenza, il ciclo composto (F_r\circ P), con la corretta identificazione dei reticoli parentale e raffinato, conserva l'equivarianza cubica in questa convenzione.

## 5. Momenti del padding

Con coordinate intere indicizzate a partire da zero:

- **2D, `kk=1`**: ogni sito ((x,y)) genera i quattro siti ((2x+\epsilon_x,2y+\epsilon_y)), con (epsilon_x,\epsilon_y\in\{0,1\}). Per il numero (N) di siti attivi e i momenti grezzi (X=\sum x a_{xy}), (Y=\sum y a_{xy}):
  [
  N'=4N,\quad X'=8X+2N,\quad Y'=8Y+2N.
  ]
- **3D, `kk=0`**: sopravvive un solo figlio per genitore:
  [
  N'=N,\quad (X',Y',Z')=2(X,Y,Z).
  ]

Sono identità del solo operatore di padding, non invarianti dell'aggiornamento cellulare successivo.

## 6. Ponte quaternionico: cosa è lecito affermare

L'inclusione

[
U(1)\hookrightarrow SU(2),\qquad
e^{i\theta}\mapsto \cos\theta+\mathbf u\sin\theta
]

per un asse immaginario unitario fissato (mathbf u) è un fatto algebrico standard. Ma le variabili del sorgente sono bit e la regola è booleana: non vi sono ampiezze complesse, spinori, fasi o moltiplicazioni quaternioniche.

Si può definire *a posteriori* un descrittore quaternionico da momenti spaziali, ad esempio normalizzando (1+\alpha(m_x i+m_y j+m_z k)). Questo sarebbe un'osservabile costruita sui dati, non una dinamica quaternionica implementata dal repository.

Inoltre, la coniugazione quaternionica unitaria induce rotazioni e preserva la norma: da sola non produce un fattore di crescita reale (psi>1). Un eventuale ponte con una ricorrenza supergolden richiederebbe un operatore radiale/di trasferimento distinto e derivato dai dati.

## 7. Qutrit e ricorrenza supergolden

Il fatto che si possano estrarre tre osservabili non costruisce uno spazio di Hilbert (ℝ^3) o (ℂ^3) con dinamica quantistica a tre livelli. Il codice esaminato è una dinamica deterministica su configurazioni binarie.

La radice positiva di (x^3-x^2-1=0), (psi\approx1.465571231876768), è associata alla matrice

[
M_\psi=
\begin{pmatrix}
0&0&1\\
1&0&0\\
0&1&1
\end{pmatrix},
\qquad r_{n+3}=r_{n+2}+r_n.
]

Questa è una ricorrenza supergolden, non la ricorrenza Tribonacci standard (x^3-x^2-x-1=0). Per attribuire (M_\psi) al sistema cellulare occorre derivare un trasferimento su osservabili o stati aggregati, dimostrare la chiusura del sottospazio scelto e verificare il polinomio caratteristico. Tre statistiche scelte arbitrariamente non bastano.

## 8. Collegamento rigoroso a RGS

Il percorso matematicamente sensato non è identificare direttamente le configurazioni binarie con il settore tangente RGS. Per un reticolo finito, la mappa cellulare induce un operatore di Koopman sulle osservabili:

[
(\mathcal K f)(a)=f(F_r(a)).
]

Poiché (F_r) è (O_h)-equivariante, (ℚ) commuta con l'azione di (O_h) sulle osservabili. Si può quindi decomporre lo spazio delle osservabili in componenti irriducibili e studiare i blocchi di molteplicità. È in questi blocchi, se esistono sottospazi invarianti di dimensione appropriata, che può essere cercato un trasferimento (3\times3).

Resta necessario costruire esplicitamente:
1. una famiglia di osservabili con trasformazione nota sotto (O_h);
2. una proiezione/intertwiner verso il settore RGS scelto;
3. un test di chiusura del sottospazio;
4. la matrice di trasferimento indotta;
5. il residuo di commutazione e il polinomio caratteristico.

Non è corretto confondere una tripla di coordinate che trasforma come un'irrep spaziale tridimensionale con uno spazio di molteplicità tridimensionale su cui possa agire un trasferimento non scalare compatibile con la simmetria.

## 9. Limiti e classificazione epistemica

- **Dimostrato analiticamente:** conteggio delle classi; assenza di overflow nella tabella 3D; equivarianza della regola locale; equivarianza del padding 3D nella convenzione esplicitata; formule dei momenti.
- **Verificabile numericamente dallo script:** enumerazione delle 24 rotazioni, residui esatti su configurazioni campione, identità del padding.
- **Non presente nel sorgente:** stato quaternionico, qutrit, dinamica SU(2), ricorrenza supergolden.
- **Aperto:** costruzione di osservabili equivarianti, operatore di Koopman utile, riduzione RGS e derivazione di un eventuale trasferimento supergolden.

## 10. Sorgenti primarie

- [2D cellular automaton source](https://raw.githubusercontent.com/xcontcom/fractogenesis/main/2d-ca/draw.js)
- [3D cellular automaton source](https://raw.githubusercontent.com/xcontcom/fractogenesis/main/3d-ca/draw.js)
- [Repository fractogenesis](https://github.com/xcontcom/fractogenesis)

L'audit è riferito al contenuto dei sorgenti consultati; per una riproducibilità piena andrebbe registrato anche lo SHA del commit upstream esatto e ripetuta la verifica quando il sorgente cambia.


## 11. Primo test Koopman: chiusura di una tripla di osservabili

È stato aggiunto `audit_koopman.py`, che esegue un test diagnostico su un toro periodico (3^3). Fissa una tabella totalistica casuale di 54 bit, genera configurazioni binarie, ne considera l'orbita sotto le 24 rotazioni cubiche proprie e misura tre primi momenti di Fourier:

[
f_i(a)=\frac{1}{L^3}\sum_{x\in(\mathbb Z/L\mathbb Z)^3}
a(x)\sin\!\left(\frac{2\pi x_i}{L}\right),\qquad i=1,2,3.
]

Si adatta una matrice (A\in\mathbb R^{3\times3}) mediante minimi quadrati a
[
f(F_r(a))\simeq A f(a).
]
Il residuo relativo è
[
\varepsilon_{\rm cl}=\frac{\|Y-XA^T\|_F}{\|Y\|_F}.
]

**Interpretazione corretta:** se il residuo è grande, la tripla scelta non è un sottospazio chiuso (o approssimativamente chiuso a quella precisione) per l'azione di Koopman. La matrice (A) è soltanto una regressione proiettata; i suoi autovalori non sono automaticamente autovalori esatti dell'operatore di Koopman.

L'augmentazione per orbite cubiche controlla l'equivarianza e riduce il bias statistico. Per una distribuzione di campionamento esattamente invariante sotto il gruppo, la regressione ortogonale su una tripla che trasforma come l'irrep vettoriale cubica deve essere scalare per il lemma di Schur. Un risultato quasi scalare è quindi atteso e **non** costituisce una scoperta di una dinamica supergolden.

Il test confronta anche gli autovalori della matrice proiettata con (p(\lambda)=\lambda^3-\lambda^2-1), ma tale confronto è solo diagnostico. Per dimostrare una ricorrenza supergolden occorre prima individuare un sottospazio di molteplicità invariante, distinto dal tripletto spaziale, e verificare una restrizione esatta o un limite controllato dell'operatore.

### 11.1 Risultato numerico riproducibile

Esecuzione locale dello script con seed `20261106`, (L=3), 1.000 configurazioni base e augmentazione per 24 rotazioni (24.000 campioni):

- mismatch di equivarianza dell'aggiornamento: **0**;
- residuo relativo di chiusura lineare: **0.9641625028**;
- matrice proiettata: (A\simeq0.1321873593\,I_3);
- distanza di Frobenius da (\frac{\operatorname{tr}A}{3}I_3): (8.78\times10^{-17});
- autovalore triplo della regressione: (0.1321873593);
- residuo ( |\lambda^3-\lambda^2-1|\): circa **1.01516**.

Il dato più importante è il residuo di chiusura, circa 96.4%: la tripla dei primi momenti sinusoidali scelta qui non è una riduzione lineare utile della dinamica. La regressione risulta scalare, come atteso dalla simmetria cubica, ma questo non rivela un blocco di molteplicità né una ricorrenza supergolden. È un risultato negativo circoscritto a questa scelta di osservabili e a questa regola casuale fissata dal seed, non un'impossibilità generale.


## 12. Correzione del tipo di rappresentazione e test T2u dedicato

### 12.1 Correzione necessaria: i primi momenti sono T1u, non T2u

La tripla dei primi momenti sinusoidali usata in `audit_koopman.py` trasforma come il vettore cartesiano ((x,y,z)): è il tipo (T_{1u}) di (O_h), non (T_{2u}). Quel test resta valido come test T1u, ma non poteva essere interpretato come ponte diretto al settore RGS T2u.

Per costruire una tripla T2u si usano invece gli armonici cubici
[
h(x,y,z)=\big(x(y^2-z^2),\ y(z^2-x^2),\ z(x^2-y^2)\big).
]
Sotto le 48 matrici di permutazione con segni (O_h), essi realizzano una rappresentazione tridimensionale T2u. La matrice (D(g)) è ricostruita dalle identità (h(gx)=D(g)h(x)), e si controllano sia la legge di rappresentazione sia la covarianza numerica delle feature.

### 12.2 Costruzione delle dieci copie candidate

Sul toro (L=5), con coordinate centrate ({-2,-1,0,1,2}^3), si definisce il conteggio dei 26 vicini (s_a(x)). Per dieci intervalli (I_j) che partizionano ([0,27)), si costruiscono
[
G_j(a)=\sum_x a(x)\,\mathbf 1_{I_j}(s_a(x))\,h(x),
\qquad j=0,\ldots,9.
]
Ogni (G_j) è una tripla covariante T2u. Le dieci triplette formano un vettore di 30 componenti, candidato al modello (\mathbb R^3\otimes\mathbb R^{10}). La regressione equivarante cerca la matrice di molteplicità (M_{10}) tale che
[
G(F(a))\simeq (M_{10}\otimes I_3)G(a),
]
con convenzione di ordinamento canale/carrier dichiarata nel codice.

### 12.3 Risultati numerici riproducibili

Script: [`audit_t2u_multiplicity.py`](audit_t2u_multiplicity.py). Seed fissi `20261106, 20261107, 20261108`; 500 configurazioni base a densità casuale uniforme in ([0.1,0.9]); 48 trasformazioni di gruppo, quindi 24.000 campioni.

- residuo massimo dell'identità armonica (h(gx)=D(g)h(x)): (2.52\times10^{-14});
- residuo massimo della legge (D(g_1g_2)=D(g_1)D(g_2)): (6.66\times10^{-16});
- mismatch dell'aggiornamento CA sotto (O_h): **0**;
- residuo massimo di covarianza delle feature T2u: (3.27\times10^{-14});
- rango della matrice di disegno sulle dieci copie: **10**;
- numero di condizionamento: **5.983**;
- residuo relativo di chiusura: **0.9812368906**.

Il disegno è quindi numericamente identificabile, ma la chiusura è pessima: circa il 98.1% della norma dell'output resta fuori dalla migliore regressione equivarante scelta. Gli autovalori di (M_{10}) non soddisfano (p(\lambda)=\lambda^3-\lambda^2-1=0); nessun autovalore vicino a (\psi) emerge. Questo è un risultato negativo per queste dieci feature e per la regola fissata, non una dimostrazione di impossibilità per tutte le osservabili T2u.

### 12.4 Audit della discrepanza 30/39 e limite del ponte RGS

Il settore isotypic T2u già identificato nell'audit RGS ha rango 30, cioè dieci copie della rappresentazione tridimensionale. Il rango 39 riportato in una sezione storica del notebook compare invece in un helper che assume una base interna (39\times39) etichettata T2u; la sola forma della matrice non prova l'identificazione irrep. La documentazione storica presenta dunque un'incongruenza di etichettatura da risolvere confrontando i caratteri e i proiettori effettivi. Il codice di recupero del primo tripletto non va usato come autorità per il rango isotypic.

**Limite esplicito:** questo esperimento costruisce dieci copie T2u sullo spazio delle configurazioni del CA, ma non calcola ancora un intertwiner numerico (J:\mathbb R^{30}\to\mathbb R^{188}). Per farlo servono, nello stesso run riproducibile, le matrici dell'azione (U_{\rm tan}(g)), il proiettore RGS (P_{T2u}) (o una base ortonormale verificata del suo range), e la definizione delle osservabili/feature che si intende mappare. La condizione da imporre è
[
U_{\rm tan}(g)J=J\,(I_{10}\otimes D_{T2u}(g))
]
(con la convenzione di ordinamento coerente), insieme a (P_{T2u}J=J). Solo dopo questi residui si può comprimere un operatore RGS sul fattore di molteplicità e testare una dinamica supergolden. Non si deve identificare (M_{10}) del CA con il blocco RGS senza questo intertwiner.


### 12.5 Ostruzione esatta: Koopman su un toro finito non può avere autovalore supergolden

Per un toro finito fissato, lo spazio delle configurazioni binarie \(\Omega=\{0,1\}^{L^3}\) è finito. Per una regola deterministica fissata \(F:\Omega\to\Omega\), l'operatore di Koopman sulle osservabili è \(Kf=f\circ F\). Nella norma sup:
\[
\|Kf\|_\infty=\max_{a\in\Omega}|f(F(a))|\leq\max_{b\in\Omega}|f(b)|=\|f\|_\infty.
\]
Se \(Kf=\lambda f\) con \(f\neq0\), allora \(|\lambda|\leq1\). Dunque **\(\psi=1.465571\ldots\) non può essere un autovalore dell'operatore di Koopman esatto di un CA deterministico su un toro finito fissato**. Questa conclusione è un teorema, non una stima numerica.

Non vieta un autovalore superunitario per un operatore diverso: ad esempio un trasferimento di rinormalizzazione tra scale, una mappa di raffinamento non autonoma, oppure un operatore di crescita su quantità non normalizzate. Ma tale operatore va definito esplicitamente; non può essere chiamato semplicemente Koopman del CA finito.

Per il fit T2u corrente, il massimo modulo spettrale della matrice proiettata \(M_{10}\) è circa 0.268345; il minimo residuo polinomiale tra i suoi dieci autovalori è circa 0.999869 e la distanza minima da \(\psi\) è circa 1.198933. Questi numeri confermano che la regressione campionata non sta approssimando la ricorrenza supergolden.
