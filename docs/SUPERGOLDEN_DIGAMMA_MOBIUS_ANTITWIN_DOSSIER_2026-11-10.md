# Dossier — digamma, fase supergolden, Möbius e quoziente Anti-Twin

**Data:** 10 novembre 2026  
**Ambito:** identità analitiche e algebriche esatte; dinamica spettrale della sostituzione a tre canali; audit topologico Anti-Twin; problema aperto della realizzazione geometrica Q6–PSU.

> **Regola epistemica.** Le dimostrazioni relative alla matrice astratta sono risultati matematici. Non costituiscono una derivazione della matrice dalla geometria Q6. I valori numerici sono riportati come orientamento; quando una conclusione richiede un certificato di aritmetica intervallare, ciò è dichiarato esplicitamente.

## 1. Oggetto e notazione

Sia
\[
f(X)=X^3-X^2-1.
\]
Il polinomio è irriducibile su \(\mathbb Q\) (non ha radici razionali) e ha discriminante
\[
\Delta(f)=-31.
\]
Indichiamo con \(s\) la sua unica radice reale positiva:
\[
s=1.4655712318767680266\ldots,\qquad s^3=s^2+1.
\]
Le altre radici sono \(z,\bar z\), con \(\operatorname{Im}z>0\), e scriviamo
\[
z=\rho e^{i\theta},\qquad \rho=s^{-1/2},\qquad
\theta=1.85647854147\ldots\ {\rm rad}.
\]
Poniamo inoltre
\[
x_\theta=\frac{\theta}{2\pi},\qquad c=\cot\frac{\theta}{2}.
\]
Le lettere \(s\) e \(c\) non indicano rispettivamente una funzione e una costante intercambiabile: \(s\) è la radice reale della cubica, \(c\) è il coefficiente di fase.

## 2. Legge di crescita a tre canali e correzione asintotica

### 2.1 Sostituzione e convenzione

La sostituzione orientata è
\[
A\mapsto A+B,\qquad B\mapsto C,\qquad C\mapsto A.
\]
Con vettori-colonna \(v_n=(a_n,b_n,c_n)^T\), la matrice d'incidenza è
\[
M=\begin{pmatrix}1&0&1\\1&0&0\\0&1&0\end{pmatrix},
\qquad v_{n+1}=Mv_n.
\]
Per il seme costituito da un solo canale \(A\),
\[
v_0=(1,0,0)^T,\quad
v_1=(1,1,0)^T,\quad
v_2=(1,1,1)^T,\quad
v_3=(2,1,1)^T.
\]
Quindi i conteggi totali iniziano con
\[
N_0=1,\ N_1=2,\ N_2=3,\ N_3=4,\ N_4=6,\ldots
\]
e includono \(N_{10}=60\), \(N_{20}=2745\), \(N_{30}=125491\), \(N_{40}=5736961\).

**Correzione di indicizzazione importante:** il vettore \((2,1,1)\) è \(v_3\), non \(v_2\). Una fixture generica che soddisfa la ricorrenza non deve essere confusa con i dati iniziali della sostituzione partita da un solo \(A\).

### 2.2 Teorema spettrale

Il polinomio caratteristico è
\[
\chi_M(\lambda)=\lambda^3-\lambda^2-1.
\]
Per Cayley–Hamilton,
\[
M^3=M^2+I,
\qquad v_{n+3}=v_{n+2}+v_n,
\qquad N_{n+3}=N_{n+2}+N_n.
\]
La matrice è primitiva. Per Perron–Frobenius, il suo autovalore dominante è \(s\), e
\[
N_n=C s^n+2\operatorname{Re}(Bz^n),\qquad C>0.
\]
Per il seme \(v_0=(1,0,0)^T\), i coefficienti si possono scrivere esattamente:
\[
C=\frac{1+2s+s^{-1}}{3s^2-2s}
=1.31342306\ldots,
\]
\[
|B|^2=\frac{1+s-s^2}{(3s-2)(3s+1)}
=0.0245603001\ldots,
\qquad |B|=0.15671726\ldots.
\]
La formula per \(|B|^2\) è un'espressione in \(\mathbb Q(s)\); la positività segue dalla scelta della radice reale \(s\).

Ne segue il limite additivo
\[
N_n-Cs^n=O(\rho^n),\qquad \rho=s^{-1/2}<1,
\]
non soltanto il limite del rapporto \(N_{n+1}/N_n\to s\). La correzione è oscillante, con fase \(n\theta+\arg B\), e inviluppo \(2|B|\rho^n\). Il periodo formale è
\[
\frac{2\pi}{\theta}=3.3845\ldots
\]
passi.

### 2.3 Arrotondamento all'intero più vicino: dimostrazione

Per il seme \(A\),
\[
|N_n-Cs^n|\le 2|B|\rho^n\le 2|B|.
\]
Si può dimostrare esattamente che \(2|B|<1/2\). Infatti, usando la formula precedente, questa disuguaglianza equivale a
\[
25s^2-19s-18>0.
\]
La cubica \(f\) è strettamente crescente per \(X>2/3\), e
\[
f(7/5)=-27/125<0,
\]
quindi \(s>7/5\). La funzione \(25X^2-19X-18\) è crescente per \(X>19/50\), e al punto \(7/5\) vale \(22/5>0\). Pertanto
\[
\boxed{|N_n-Cs^n|<\frac12\quad\text{per ogni }n\ge0.}
\]
Poiché \(N_n\) è intero, \(N_n\) è l'unico intero più vicino a \(Cs^n\) per ogni \(n\ge0\).

Questo risultato è più forte di un controllo su 1200 indici: la conclusione segue dalla maggiorazione algebrica esatta di \(|B|\), non da un campionamento numerico. Il valore decimale di \(|B|\) serve solo come controllo.

## 3. Fase complessa, trascendenza dell'angolo e digamma

### 3.1 Trascendenza di \(\theta/\pi\)

Dalle relazioni di Viète:
\[
s+z+\bar z=1,\qquad sz\bar z=1.
\]
Quindi
\[
\operatorname{Re}z=\frac{1-s}{2},\qquad |z|^2=\frac1s,
\]
e
\[
\cos^2\theta=\frac{s(1-s)^2}{4},\qquad
\sin^2\theta=\frac{s^2-s+3}{4}.
\]
Poniamo \(t=z/\bar z=e^{2i\theta}\). Un coniugato Galois di \(t\) è \(s/z\), il cui modulo è
\[
\left|\frac{s}{z}\right|=s^{3/2}>1.
\]
Dunque \(t\) non è una radice dell'unità: se lo fosse, tutti i suoi coniugati sarebbero radici dell'unità e avrebbero modulo uno.

Se \(\theta/\pi\) fosse razionale, \(e^{2i\theta}\) sarebbe una radice dell'unità, assurdo. Se fosse algebrico irrazionale, il teorema di Gelfond–Schneider applicato a
\[
e^{i\theta}=(-1)^{\theta/\pi}
\]
(dove si sceglie \(\log(-1)=i\pi\)) lo renderebbe trascendente; ma il suo quadrato \(t\) è algebrico, e quindi anche \(e^{i\theta}\) sarebbe algebrico. Contraddizione. Pertanto
\[
\boxed{\theta/\pi\text{ è trascendente}.}
\]
Il passaggio usa sia l'algebraicità di \(t\) sia l'esclusione della possibilità che \(t\) sia una radice dell'unità.

### 3.2 Il coefficiente di fase è algebrico di grado 12

Poniamo
\[
g=s^2-s+3.
\]
Il risultante dà
\[
N_{\mathbb Q(s)/\mathbb Q}(g)=\operatorname{Res}(f,g)=31=-\Delta(f).
\]
Dalla formula di \(\sin^2\theta\),
\[
\sin^2\theta=\frac g4.
\]
Con \(c=\cot(\theta/2)\), l'identità
\[
\cot^2(\theta/2)+\cot^{-2}(\theta/2)
=\frac4{\sin^2\theta}-2
\]
fornisce
\[
e:=c^2+c^{-2}=\frac{16}{g}-2.
\]
Eliminando \(s\) tra \(f(s)=0\) e \((e+2)g(s)-16=0\), si ottiene
\[
31e^3-262e^2+884e-1032=0.
\]
Poiché \(c^6(e^3,e^2,e)\) si espande in potenze pari di \(c\), segue
\[
\boxed{
P(c)=31c^{12}-262c^{10}+977c^8-1556c^6
+977c^4-262c^2+31=0.
}
\]
Il polinomio è pari e palindromo.

**Grado:** il calcolo simbolico esatto riportato per \(P\) dà irriducibilità su \(\mathbb Q\), e quindi \([\mathbb Q(c):\mathbb Q]=12\). Per rendere questa parte pienamente auditabile da terzi, il repository deve conservare anche un certificato d'irriducibilità indipendente dal solo output di un CAS (ad esempio un certificato di fattorizzazione esatta o una prova del grado della torre). Fino all'aggiunta di tale certificato, si classifica il grado 12 come **verifica simbolica esatta da corredare**, non come dimostrazione autosufficiente contenuta in questo dossier.

La relazione di riflessione del digamma diventa
\[
\boxed{
\psi(1-x_\theta)-\psi(x_\theta)=\pi c,
\qquad x_\theta=\frac{\theta}{2\pi}.
}
\]
Qui \(x_\theta\) è trascendente, mentre \(c\) è algebrico. Questo è un controesempio esplicito all'estensione indiscriminata del teorema “parametro algebrico irrazionale implica cotangente trascendente”: l'ipotesi sul parametro algebrico è essenziale.

Non si conclude che \(\pi c\) sia algebrico o trascendente. La formula determina esattamente il valore del coefficiente cotangente e la differenza del digamma, ma non risolve la natura aritmetica del loro prodotto con \(\pi\).

## 4. Dinamica di Möbius della fase

Per \(\phi=\theta/2\), la formula di addizione della cotangente dà
\[
u_{n+1}=\frac{cu_n-1}{u_n+c},
\qquad u_n=\cot(n\phi).
\]
È l'azione proiettiva della matrice
\[
A_c=\begin{pmatrix}c&-1\\1&c\end{pmatrix}.
\]
Il rapporto degli autovalori di \(A_c\) è
\[
\frac{c+i}{c-i}=e^{2i\phi}=e^{i\theta}.
\]
Pertanto \(A_c\) ha ordine proiettivo finito se e solo se \(\theta/(2\pi)\) è razionale. Nel caso supergolden tale rapporto non è una radice dell'unità, quindi l'ordine proiettivo è infinito. Inoltre la rotazione di angolo \(\theta\) sul cerchio ha orbita densa, perché \(\theta/(2\pi)\) è irrazionale (anzi trascendente).

Il confronto con il caso argenteo è netto:
\[
c_{\rm Ag}=\cot(\pi/8)=1+\sqrt2,\qquad
\frac{c_{\rm Ag}+i}{c_{\rm Ag}-i}=e^{i\pi/4}.
\]
La corrispondente trasformazione proiettiva ha ordine 8. La matrice di similitudine quadrata di Kathara e la matrice di Möbius sono oggetti diversi: condividono la fase angolare, ma non vanno identificate come la stessa matrice.

## 5. Azione di Galois e quoziente di Möbius \(V_4\)

Il polinomio \(P\) è invariato dalle trasformazioni
\[
c\mapsto-c,\qquad c\mapsto c^{-1},\qquad c\mapsto-c^{-1}.
\]
Esse generano un gruppo di Klein \(V_4\) di trasformazioni di Möbius. La coordinata invariante è
\[
e=c^2+c^{-2}.
\]
La cubica di \(e\) descrive quindi il quoziente algebrico rispetto a queste simmetrie. La descrizione come gruppo di Galois dell'estensione \(\mathbb Q(c)/\mathbb Q(s)\) richiede il grado 12 sopra indicato; finché non è allegato il certificato d'irriducibilità, questa identificazione va letta con la stessa riserva sul grado.

## 6. Audit Anti-Twin: ciò che segue e ciò che non segue

Si assumano i dati cellulari dichiarati per il 2-scheletro \(K\) di Q6:
- 64 vertici, 192 archi e 240 facce;
- l'involuzione \(J\) agisce senza celle fisse;
- sulle catene, \(J_1=-I\) sugli archi e \(J_2=+I\) sulle facce;
- le mappe di bordo commutano con l'azione nelle convenzioni dichiarate;
- \(K\) è semplicemente connesso.

Il quoziente ha 32 vertici, 96 archi e 120 facce, dunque
\[
\chi(K/J)=32-96+120=56.
\]
Poiché \(K\to K/J\) è un rivestimento doppio e \(K\) è semplicemente connesso,
\[
\pi_1(K/J)\cong\mathbb Z/2.
\]
Se inoltre l'azione su \(H_2(K;\mathbb Q)\) ha autospazi \(+1\) e \(-1\) di dimensioni 55 e 56, rispettivamente, il teorema di trasferimento identifica
\[
\dim H_2(K/J;\mathbb Q)=55.
\]

**Correzione topologica:** questi dati non identificano \(K/J\) con il piano proiettivo reale. Infatti \(H_2(\mathbb{RP}^2;\mathbb Q)=0\), mentre qui la seconda omologia razionale ha dimensione 55. La conclusione giustificata è soltanto: quoziente con gruppo fondamentale \(\mathbb Z/2\), caratteristica di Eulero 56 e seconda omologia razionale di dimensione 55, sotto le ipotesi cellulari elencate.

Non è un nastro di Möbius: il nastro ha gruppo fondamentale \(\mathbb Z\). Non si deduce neppure una struttura di fibrato non orientabile o una torsione geometrica. Queste richiedono costruzioni e invarianti aggiuntivi.

## 7. Separazione dei risultati

| Affermazione | Stato corretto |
|---|---|
| Ricorrenza della sostituzione astratta e autovalore dominante \(s\) | **Dimostrato** |
| Decomposizione \(N_n=Cs^n+2\operatorname{Re}(Bz^n)\) | **Dimostrabile esattamente dalla diagonalizzazione** |
| \(N_n\) è l'intero più vicino a \(Cs^n\) per ogni \(n\) | **Dimostrato dalla maggiorazione algebrica di \(|B|\)** |
| \(\theta/\pi\) trascendente | **Dimostrato via Gelfond–Schneider e coniugati Galois** |
| Polinomio di grado 12 per \(c=\cot(\theta/2)\) | **Identità algebrica esatta** |
| Irriducibilità di \(P\) e grado 12 | **Verifica simbolica esatta; certificato autosufficiente da aggiungere** |
| Dinamica di Möbius di ordine infinito | **Dimostrato** |
| Dati cellulari Anti-Twin elencati | **Da ricondurre ai file sorgente e ai test del complesso** |
| Identificazione del quoziente con \(\mathbb{RP}^2\) | **Falsa alla luce di \(b_2=55\)** |
| Derivazione della matrice \(M\) da Q6/Kathara | **Aperto** |
| Equivarianza quaternionica del raffinamento e compatibilità Anti-Twin | **Aperto** |
| Identificazione di \(c\) come osservabile geometrica PSU | **Aperto** |

## 8. Programma minimo per la realizzazione geometrica Q6

Una realizzazione geometrica non può partire dalla matrice \(M\) e poi cercare una lettura geometrica a posteriori. Deve definire prima:
1. le tre classi orientate \(A,B,C\) a partire da celle, cuciture o sottospazi tangenti;
2. l'elenco effettivo dei figli di ciascun elemento, con orientazione e regole di identificazione dei figli condivisi;
3. l'azione Anti-Twin su genitori, figli e orientazioni;
4. il trasporto dei riferimenti quaternionici e la relativa equivarianza;
5. la chiusura del sottospazio dei tre canali, oppure la matrice di leakage;
6. la matrice d'incidenza risultante e il suo polinomio caratteristico.

Solo se questo procedimento produce indipendentemente \(M\), la legge supergolden diventa una legge geometrica RGS–PSU. La suddivisione uniforme T055, con trasferimento \(2I_3\), resta un controllo negativo: non realizza la matrice supergolden.

**Conclusione.** Il ponte analitico-algebrico fra crescita supergolden, fase complessa, digamma e trasformazioni di Möbius è preciso. Il ponte Anti-Twin è una struttura di quoziente cellulare da descrivere con invarianti corretti. La derivazione della matrice a tre canali dalla geometria Q6 e dal trasporto quaternionico resta il problema matematico centrale.
