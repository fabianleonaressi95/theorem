# I tripletti nel modello del pallone — significato geometrico, cinematico e spettrale

**Dossier:** Morandotti  
**Versione:** 0.2 — 10 novembre 2026  
**Obiettivo:** spiegare che cosa sono i tripletti, perché compaiono nel modello cubico del pallone e come si collegano a sottospazi tangenti, quaternioni, modi elastici e proprietà dei pannelli.

## 1. La parola “tripletta” indica una struttura, non solo tre componenti

Un vettore tridimensionale ha tre componenti, ma non ogni terna di quantità costituisce un tripletto fisico nel senso della teoria delle rappresentazioni. Per parlare di tripletta occorre specificare:

1. uno spazio vettoriale (V\);
2. tre direzioni linearmente indipendenti che generano (V\);
3. un'azione delle simmetrie (D(g):V\to V\);
4. la legge con cui queste tre componenti si mescolano quando si applica una simmetria.

La proprietà decisiva è la chiusura: applicando una simmetria ammessa, una combinazione delle tre componenti deve restare nello stesso sottospazio. Se la simmetria porta fuori dal sottospazio, non abbiamo una rappresentazione autonoma di dimensione tre.

Quindi: **tre coordinate sono una descrizione; una tripletta è una descrizione più una legge di trasformazione.**

## 2. Prima tripletta: le tre rotazioni infinitesime del corpo

Siano (X_i\in\mathbb R^3) le posizioni dei nodi del pallone. Una rotazione infinitesima di vettore angolare \(\boldsymbol\omega=(\omega_x,\omega_y,\omega_z)\) produce
\[
\delta X_i=\boldsymbol\omega\times X_i
=\omega_x(e_x\times X_i)+\omega_y(e_y\times X_i)+\omega_z(e_z\times X_i).
\]
Definiamo i tre generatori
\[
(G_x)_i=e_x\times X_i,\qquad
(G_y)_i=e_y\times X_i,\qquad
(G_z)_i=e_z\times X_i.
\]
I vettori (G_x,G_y,G_z) generano lo spazio delle rotazioni rigide infinitesime, purché non siano eliminati dai vincoli. Insieme alle tre traslazioni
\[
(T_a)_i=e_a,\qquad a=x,y,z,
\]
formano i sei moti rigidi di un corpo libero in tre dimensioni.

Questi sei vettori non sono deformazioni elastiche: cambiano posizione/orientazione globale senza cambiare distanze interne. Perciò, in un modello elastico oggettivo non vincolato, l'energia deve rimanere invariata sotto questi moti. Nella Hessiana compaiono come modi a energia nulla, salvo vincoli, contatti, pressione/carichi o regolarizzazioni numeriche.

**Per Morandotti:** questa è la prima tripletta da identificare e rimuovere dalla lettura dei modi elastici, altrimenti si rischia di chiamare “deformazione” una semplice rotazione del pallone.

## 3. Seconda tripletta: le rappresentazioni (T_{1u}) e (T_{2u}) del gruppo cubico

La geometria cubica ha simmetria (O_h), il gruppo delle rotazioni e riflessioni che preservano il cubo. Le sue rappresentazioni irriducibili tridimensionali includono (T_{1u}) e (T_{2u}). Entrambe hanno dimensione tre, ma **non sono la stessa tripletta**.

### 3.1 (T_{1u}): vettori assiali/polari secondo la parità

La rappresentazione (T_{1u}) è quella associata al vettore polare ((x,y,z)) sotto il gruppo cubico completo, con parità dispari indicata da (u). Le rotazioni proprie agiscono sulle tre componenti con le usuali matrici tridimensionali.

Per esempio, una rotazione di 90° attorno all'asse (z) trasforma
\[
(x,y,z)\mapsto(-y,x,z).
\]
La tripletta è chiusa: le nuove componenti sono combinazioni lineari delle precedenti.

### 3.2 (T_{2u}): altra rappresentazione tridimensionale

(T_{2u}) è anch'essa tridimensionale e dispari, ma ha caratteri diversi sotto le classi di simmetria di (O_h). Un modello intuitivo delle tre componenti è dato da funzioni quadratiche miste con parità dispari, ad esempio
\[
(xyz)\quad\text{e combinazioni equivalenti costruite con il fattore di parità appropriato,}
\]
ma questa immagine mnemonica non sostituisce la definizione tramite caratteri e matrici di rappresentazione. In particolare, la base concreta di (T_{2u}) nel nostro spazio discreto va ricavata dai proiettori, non scelta a occhio.

(T_{1u}) e (T_{2u}) non si trasformano nello stesso modo sotto tutte le operazioni di (O_h). Una deformazione che appartiene a (T_{2u}) non può essere trattata come una normale traslazione o rotazione vettoriale.

### 3.3 Perché la distinzione è ingegneristicamente importante

La simmetria cubica consente di classificare i modi prima di interpretarli meccanicamente. Modi appartenenti a rappresentazioni diverse non si mescolano se l'operatore elastico conserva esattamente (O_h). Se pannelli, cuciture, trama o carichi rompono la simmetria, il mescolamento può comparire: la sua entità si misura con commutatori e accoppiamenti tra sottospazi.

## 4. Come si estrae una tripletta: il proiettore di simmetria

Sia (D(g)) l'azione della simmetria (g\in O_h) sullo spazio completo delle configurazioni e sia (alpha) un'irriducibile di dimensione (d_\alpha), con carattere (chi_\alpha(g)). Il proiettore è
\[
P_\alpha=\frac{d_\alpha}{|O_h|}
\sum_{g\in O_h}\chi_\alpha(g)^*D(g).
\]
Applicando (P_\alpha) a un vettore si conserva soltanto la componente appartenente al settore (alpha). L'immagine di (P_\alpha) è la somma di tutte le copie di quella rappresentazione presenti nello spazio.

Se la rappresentazione è esatta e il proiettore è costruito correttamente:
\[
P_\alpha^2=P_\alpha,\qquad P_\alpha^T=P_\alpha,
\]
e il rango è multiplo della dimensione (d_\alpha=3). Il rango non è necessariamente tre: può contenere molte copie della stessa tripletta.

Se (\operatorname{rank}P_{T_{1u}}=39), ciò corrisponde a 13 copie tridimensionali; se (\operatorname{rank}P_{T_{2u}}=30), corrisponde a 10 copie. Questi sono ranghi complessivi dei settori, non la dimensione di un singolo tripletto.

## 5. Dove entrano i sottospazi tangenti

Per il modello a 64 punti, il vettore delle coordinate ha 192 componenti. Con quattro vincoli indipendenti:
\[
X\in\mathbb R^{192},\qquad \operatorname{rank}J=4,
\qquad \dim\ker J=188.
\]
Scegliamo una base ortonormale del nucleo:
\[
JQ=0,\qquad Q^TQ=I_{188}.
\]
Le perturbazioni ammissibili sono
\[
\delta X=Q\xi.
\]
Il proiettore tangente è (P_T=QQ^T). Se le simmetrie preservano i vincoli, l'azione di gruppo lascia invariato il sottospazio tangente. In coordinate ridotte la rappresentazione è
\[
D_T(g)=Q^TD(g)Q,
\]
a condizione che (D(g)\) mandi effettivamente (ker J) in sé. Il test numerico è
\[
\|(I-P_T)D(g)Q\|\simeq0.
\]
Solo dopo questa verifica si devono costruire i proiettori (T_{1u}) e (T_{2u}) nello spazio tangente.

Questa sequenza è essenziale:
\[
\text{configurazioni}
\;\longrightarrow\;
\text{vincoli}
\;\longrightarrow\;
\ker J
\;\longrightarrow\;
\text{azione di }O_h
\;\longrightarrow\;
\text{proiettori delle triplette}.
\]
Non è corretto decomporre prima uno spazio che contiene direzioni vietate dai vincoli e poi supporre che la decomposizione resti invariata dopo la proiezione tangente.

### 5.1 La shell Morandotti non eredita automaticamente la base 188D

La shell a 92 nodi ha 276 coordinate cartesiane prima dei vincoli. Il suo Jacobiano (J_{sh}), il nucleo e la base (Q_{sh}) devono essere costruiti da capo. La matrice (Q\in\mathbb R^{192\times188}) appartiene al modello a 64 punti: non è la base tangente della shell a 92 nodi.

Per trasferire una tripletta dal modello 64 punti alla shell occorre una mappa (T) tra i due spazi e verificare:
\[
T D_{64}(g)\simeq D_{sh}(g)T,
\qquad
\|J_{sh}TQ\|\simeq0.
\]
Se la mesh o i materiali non rispettano la simmetria cubica, la relazione sarà soltanto approssimata e va misurata.

## 6. Come si collegano i tripletti ai quaternioni

Un quaternione unitario che rappresenta una rotazione è
\[
q=\cos\frac\theta2+
(\mathbf i n_x+\mathbf j n_y+\mathbf k n_z)\sin\frac\theta2.
\]
La parte immaginaria ha tre componenti. I versori (mathbf i,mathbf j,mathbf k) forniscono una base tridimensionale per gli assi di rotazione; non sono tre quaternioni indipendenti che descrivono tre rotazioni finite separate. Un'unica rotazione è specificata dall'asse (hat n) e dall'angolo (	heta).

Un vettore (v\in\mathbb R^3), rappresentato da un quaternione puro, si trasforma come
\[
v'=qvq^{-1}.
\]
Per piccole rotazioni:
\[
q\simeq1+\frac12(\omega_x\mathbf i+\omega_y\mathbf j+\omega_z\mathbf k).
\]
I coefficienti ((\omega_x,\omega_y,\omega_z)) sono proprio le coordinate della tripletta cinematica delle rotazioni infinitesime.

Il collegamento preciso è dunque:
- il tripletto (G_x,G_y,G_z) descrive le tre direzioni infinitesime di rotazione della configurazione;
- il quaternione combina queste tre componenti in una rotazione finita;
- (Q) proietta le variazioni compatibili con i vincoli;
- i proiettori (P_{T_{1u}}) e (P_{T_{2u}}) classificano i modi secondo la simmetria cubica.

Non si deve confondere la base immaginaria dei quaternioni con una base di modi elastici (T_{1u}) o (T_{2u}): la prima codifica l'algebra delle rotazioni; la seconda classifica sottospazi di configurazioni.

## 7. Perché possono esserci più triplette e perché si accoppiano

Una struttura con molti nodi possiede uno spazio di deformazione di dimensione elevata. La stessa rappresentazione tridimensionale può comparire molte volte:
\[
\mathcal V\simeq
m_{1u}T_{1u}\oplus m_{2u}T_{2u}\oplus\cdots.
\]
Ogni copia è una tripletta distinta, con una propria forma spaziale sui pannelli. Due triplette possono avere la stessa legge di trasformazione ma distribuzioni di deformazione diverse.

Se la simmetria è esatta, un operatore elastico (K) che commuta con tutte le simmetrie,
\[
KD(g)=D(g)K\quad\forall g\in O_h,
\]
non accoppia irriducibili inequivalenti. Può però accoppiare le diverse copie della stessa irriducibile attraverso una matrice nello spazio delle molteplicità.

Se le cuciture o i materiali rompono la simmetria, i commutatori
\[
C_g=KD(g)-D(g)K
\]
misurano la rottura. Anche l'accoppiamento tra settori può essere misurato:
\[
\|P_{T_{1u}}KP_{T_{2u}}\|.
\]
Un valore non nullo può indicare rottura della simmetria, proiettori non coerenti con il prodotto scalare/massa, o errore numerico. Non va interpretato immediatamente come nuova fisica.

## 8. Che cosa significa per pannelli, trama e cuciture

Ogni modo tridimensionale ha tre componenti correlate dalla simmetria. La sua forma spaziale indica quali pannelli si allungano, ruotano, si incurvano o caricano le cuciture. Per questo, dopo la decomposizione, non basta riportare tre autovalori: occorre visualizzare le tre forme modali e calcolare per ciascuna:
- energia membranale;
- energia flessionale;
- energia accumulata nelle cuciture;
- scorrimento/apertura relativa delle interfacce;
- contributo delle direzioni materiali 1 e 2;
- sensibilità a pressione e condizioni al contorno.

Una tripletta quasi degenere in una struttura quasi cubica può separarsi quando si introducono cuciture non equivalenti o materiali orientati. Lo splitting degli autovalori è una misura utile della rottura di simmetria, ma va confrontato con incertezza, mesh e tolleranze.

## 9. Numeri preliminari del framework 64/188 e loro interpretazione

Nel precedente audit del modello (O_h) a 64 punti sono stati registrati:
- 192 coordinate cartesiane;
- 4 vincoli indipendenti e 188 direzioni tangenti;
- base (Q\in\mathbb R^{192\times188}), con residuo di ortogonalità molto piccolo;
- ranghi dei settori riportati: (P_{T_{1u}}) pari a 39 e (P_{T_{2u}}) pari a 30;
- 18 intertwiners registrati nell'analisi di collegamento tra sottospazi.

I ranghi 39 e 30 sono compatibili con 13 e 10 copie di rappresentazioni tridimensionali. Il dato “18 intertwiners” non va però trasformato in una conclusione senza specificare domini, codomini, normalizzazione e rango di ciascun operatore. Va recuperato il calcolo originale e verificato sul modello shell.

Questi numeri sono risultati del framework discreto precedente, non ancora risultati sperimentali del pallone e non ancora una decomposizione certificata della shell a 92 nodi.

## 10. Test necessari prima di presentare i tripletti come risultato

1. **Azione di gruppo:** verificare (D(g_1g_2)=D(g_1)D(g_2)) e ortogonalità rispetto al prodotto scalare scelto.
2. **Compatibilità vincoli:** verificare ((I-P_T)D(g)Q\) per tutti i generatori di (O_h).
3. **Proiettori:** controllare (P^2-P), (P^T-P), rango e ortogonalità tra settori.
4. **Molteplicità:** verificare che il rango dei settori tridimensionali sia multiplo di tre.
5. **Hessiana:** verificare commutatori (KD(g)-D(g)K) e accoppiamenti tra settori.
6. **Modi:** visualizzare le tre componenti di ogni copia e distinguere modi rigidi da modi deformativi.
7. **Quaternioni:** confrontare (qvq^{-1}) con la matrice (R(q)v) e verificare norma unitaria/composizione.
8. **Shell:** ricostruire (J_{sh},Q_{sh},D_{sh}(g)) sulla mesh reale; non riutilizzare la base 64/188.
9. **Rottura di simmetria:** introdurre pannelli/cuciture/materiali misurati e quantificare splitting e commutatori.
10. **Validazione:** confrontare le forme modali con scansioni e prove, separando calibrazione e validazione.

## 11. Messaggio sintetico per Morandotti

I tripletti sono modi tridimensionali classificati dalla simmetria della struttura. La tripletta cinematica delle rotazioni rigide descrive i tre assi di rotazione del pallone; le triplette (T_{1u}) e (T_{2u}) descrivono invece famiglie distinte di deformazioni che si trasformano secondo rappresentazioni diverse del gruppo cubico. I quaternioni rappresentano le rotazioni finite e collegano in modo naturale le tre componenti angolari; il sottospazio tangente elimina le variazioni incompatibili con i vincoli; la Hessiana ridotta permette di studiare stabilità e modi elastici. Sul pallone reale bisogna ricostruire questi oggetti sulla mesh shell, poi misurare come pannelli, trama e cuciture separino o accoppino le triplette.
