# Sottospazi tangenti, quaternioni e triplette: ricostruzione del percorso RGS–PRISM

**Capitolo metodologico per il dossier destinato al prof. Marco Morandotti**  
Stato: ricostruzione matematica e numerica; non costituisce una prova di equivalenza fisica tra i modelli.

## 0. Perché questo capitolo è necessario

Il raccordo RGS–PRISM con l'elasticità incompatibile non nasce da un'analogia generica tra geometria discreta e difetti cristallini. Il percorso seguito è:

1. partire da una configurazione finita di 64 siti immersi in R³;
2. definire le variazioni ammissibili eliminando le direzioni che violano i vincoli geometrici;
3. costruire operatori e forme quadratiche sul sottospazio tangente;
4. isolare sottospazi tridimensionali e stabilire se siano modi di rotazione, degenerazioni numeriche o rappresentazioni di simmetria;
5. usare i quaternioni per codificare frame locali e azioni di rotazione;
6. trasferire, con una mappa geometrica esplicita, i sottospazi RGS verso il guscio calcistico;
7. separare identità cinematiche, verifiche numeriche e ipotesi.

Il punto da sottoporre a Morandotti è la costruzione di una geometria discreta con vincoli, metriche e operatori compatibili con un problema variazionale. Le triplette e i quaternioni sono strumenti strutturali; non dimostrano automaticamente una nuova simmetria fisica o un nuovo campo.

---

## 1. Dallo spazio delle configurazioni al sottospazio tangente 188D

### 1.1 Configurazione e spazio ambientale

La configurazione è costituita da 64 punti:
\[
X=(X_1,\ldots,X_{64}),\qquad X_i\in\mathbb R^3.
\]
Impilando le coordinate si ottiene x=vec(X) in R^192. Le 192 componenti non sono tutte variazioni ammissibili: alcune cambiano il centro della configurazione o la sua scala radiale.

### 1.2 I quattro vincoli

Si impongono tre vincoli di centratura e uno radiale:
\[
F_a(X)=\sum_{i=1}^{64}X_i^a=0,\quad a=1,2,3,
\]
\[
F_4(X)=\frac12\left(\sum_{i=1}^{64}\|X_i\|^2-R_{\rm ref}^2\right)=0.
\]
Il Jacobiano J(X) appartiene a R^(4×192). Le prime tre righe sono i vettori di traslazione uniforme; la quarta è il vettore radiale impilato:
\[
J(X)=
\begin{pmatrix}
1&0&0&1&0&0&\cdots\\
0&1&0&0&1&0&\cdots\\
0&0&1&0&0&1&\cdots\\
X_1^T&X_2^T&\cdots&X_{64}^T
\end{pmatrix}.
\]
Per una perturbazione infinitesima delta-x, la linearizzazione dei vincoli è J delta-x=0. Il tangente alla varietà dei vincoli è
\[
T_X\mathcal M=\ker J(X).
\]
Se rank(J)=4, allora dim(T_X M)=192−4=188.

### 1.3 Base ortonormale e proiettore

Si costruisce
\[
Q\in\mathbb R^{192\times188},\quad JQ=0,\quad Q^TQ=I_{188}.
\]
Ogni variazione ammissibile si scrive delta-x=Q xi, con xi in R^188. Il proiettore ortogonale è
\[
P_T=QQ^T,\qquad P_T^2=P_T=P_T^T,
\]
e il proiettore normale è P_N=I−P_T, di rango 4.

La riduzione evita di attribuire significato energetico alle quattro direzioni escluse dai vincoli. È la distinzione finito-dimensionale tra variazioni cinematicamente ammissibili e variazioni normali alla varietà vincolata.

### 1.4 Audit numerico recuperato

La ricostruzione A14 riporta:
- rank(J)=4, nullità 188;
- valori singolari di J: 15.4919333848, 8, 8, 8;
- norma di Frobenius di JQ: 1.2385×10⁻¹⁴;
- norma di QᵀQ−I: 1.3145×10⁻¹⁴;
- differenza tra proiettore della base archiviata e quello ricostruito via SVD pari a zero nel report;
- residuo del complemento tangente/normale: 9.01×10⁻¹⁵;
- residuo relativo della derivata direzionale a differenze finite: 4.11×10⁻⁹.

Questi numeri validano Jacobiano dei vincoli e base tangente archiviata. **Non validano da soli la Hessiana energetica originale né il suo spettro.** La correttezza del sottospazio ammissibile è un risultato autonomo.

---

## 2. Dalla Hessiana ambientale alla forma quadratica tangente

Sia E(x) un'energia e F(x)=0 il vincolo. In un punto stazionario vincolato si introduce il Lagrangiano
\[
\mathcal L(x,\lambda)=E(x)+\lambda^TF(x).
\]
La Hessiana rilevante per la stabilità vincolata è
\[
H_{\mathcal L}=D_x^2E+\sum_a\lambda_aD_x^2F_a.
\]
La forma quadratica sulle variazioni ammissibili è
\[
K_T=Q^TH_{\mathcal L}Q\in\mathbb R^{188\times188}.
\]
Per il vincolo radiale quadratico, il contributo della Hessiana del vincolo è proporzionale all'identità; il fattore dipende dalla convenzione scelta per F4 e dal moltiplicatore. Non si deve quindi sostituire automaticamente QᵀH_EQ a QᵀH_LQ.

Gli autovalori positivi, negativi e quasi nulli descrivono rispettivamente curvature energetiche positive, direzioni di instabilità e possibili simmetrie/modi rigidi/degenerazioni numeriche. Un autovalore quasi nullo richiede sempre un'identificazione indipendente.

Nelle ricostruzioni RGS sono comparsi conteggi diversi per operatori diversi. Un audit precedente della Hessiana tangente riportava 29 autovalori negativi, 3 quasi-zero associati a rotazioni e 156 positivi. Un diverso oggetto recuperato, K0, ha invece 64 modi quasi nulli e 124 positivi. Non sono automaticamente la stessa Hessiana: il bundle A13 contiene K0 e K_geometry_tangent, ma la loro relazione esatta con la Hessiana vincolata originale deve essere ricostruita. Non si devono fondere i due spettri.

---

## 3. Perché compaiono sottospazi tridimensionali

Una tripletta è innanzitutto un sottospazio di dimensione tre. Può derivare da rotazioni rigide, da un autovalore triplo protetto da simmetria, da tre modi quasi degeneri per coincidenza numerica oppure da una rappresentazione irriducibile. La dimensione tre da sola non decide l'interpretazione.

### 3.1 Tripletta geometrica delle rotazioni infinitesime

Per ciascun asse cartesiano e_a, la rotazione infinitesima globale genera
\[
G_a(X)_i=e_a\times X_i,\quad a=1,2,3.
\]
Impilando i tre campi si ottiene G in R^(192×3). Questi campi rispettano i vincoli al primo ordine:
- traslazione: somma_i e_a×X_i = e_a×somma_i X_i = 0;
- raggio: X_i·(e_a×X_i)=0 per ogni sito.

Quindi JG=0 e le colonne di G appartengono al tangente. In aritmetica finita si applica comunque il proiettore:
\[
G_T=P_TG=QQ^TG.
\]
Una SVD/decomposizione polare fornisce una base ortonormale U_rot in R^(192×3), se il rango è tre.

Questa tripletta è **definita cinematicamente dalla geometria**. Non è necessario cercarla nello spettro. Solo se l'energia e i vincoli sono invarianti sotto rotazioni ci si aspetta che sia anche un kernel della Hessiana vincolata. Se la simmetria è rotta, la tripletta resta tangente ma non deve avere autovalore nullo.

### 3.2 Tripletta spettrale e rappresentazione

Se un operatore simmetrico K commuta con l'azione di gruppo D(g),
\[
KD(g)=D(g)K\quad\forall g,
\]
i suoi autospazi sono invarianti. Una degenerazione di dimensione tre può corrispondere a una rappresentazione irriducibile tridimensionale. Ma la degenerazione numerica è soltanto un indizio: servono azione di gruppo, caratteri, proiettori d'irrep e commutatori.

Nel gruppo cubico completo, T1u e T2u sono entrambe irriducibili tridimensionali. Non si distinguono dal rango o dal numero di autovalori: si distinguono tramite caratteri e azione dei generatori.

Un audit precedente riportava ranghi P_T2u=30 e P_T1u=39 e 18 intertwiners in uno specifico confronto. I ranghi sono dimensioni di sottospazi isotypic nell'intero spazio, non la dimensione di una singola copia irriducibile. Inoltre la base archiviata B_T2U_TAN, pur avendo tre colonne, è stata segnalata in un audit come numericamente compatibile con T1u, non certificata come T2u. L'etichetta va sospesa finché non siano riprodotti caratteri, proiettori e azione dei generatori sulla stessa base.

### 3.3 Terminologia da usare nel dossier

1. **Tripletta geometrica:** sottospazio costruito da tre generatori cinematici, per esempio e_a×X.
2. **Cluster spettrale candidato:** tre autovalori vicini secondo una tolleranza dichiarata.
3. **Tripletto irriducibile certificato:** sottospazio per il quale sono state verificate azione di gruppo, caratteri e proiettori.

Non chiameremo una tripletta T1u o T2u prima del terzo livello.

---

## 4. Perché introduciamo i quaternioni

### 4.1 Frame locale e doppio ricoprimento

Un piano tangente locale è bidimensionale ma immerso in R³. Per confrontare spostamenti e orientazioni in punti diversi si costruisce un frame destrorso
\[
R_i=(e_{1i},e_{2i},n_i)\in SO(3),
\]
dove n_i è la normale e e_1i,e_2i sono versori tangenti ortonormali.

Il frame è sollevato a un quaternione unitario
\[
q_i=(w_i,x_i,y_i,z_i)\in SU(2).
\]
Un vettore v è identificato con il quaternione puro p=(0,v_1,v_2,v_3) e ruotato tramite
\[
p_{global}=q_i p q_i^{-1}.
\]
I quaternioni q_i e −q_i inducono la stessa rotazione: è il doppio ricoprimento SU(2)→SO(3).

Il vantaggio è una rappresentazione delle rotazioni senza le singolarità delle coordinate di Eulero e con composizione mediante prodotto quaternionico. Non significa che i quaternioni aggiungano automaticamente gradi di libertà fisici.

### 4.2 Restrizione al piano tangente

La matrice locale
\[
T_i=\begin{pmatrix}e_{1i}&e_{2i}\end{pmatrix}\in\mathbb R^{3\times2}
\]
soddisfa
\[
T_i^TT_i=I_2,\qquad P_i=T_iT_i^T=I_3-n_in_i^T.
\]
Per N nodi:
\[
T=\operatorname{diag}(T_1,\ldots,T_N)\in\mathbb R^{3N\times2N}.
\]
Uno spostamento tangente ambientale è u=T eta, con eta in R^(2N). La rigidezza ridotta è il pullback di Galerkin:
\[
K_{tan}=T^TKT.
\]
La forma energetica ambientale viene così valutata soltanto sugli spostamenti tangenti.

### 4.3 Applicazione al guscio calcistico

Il modello attuale ha 92 nodi: 60 vertici del troncato icosaedrico e 32 centri di pannello. Pertanto 3N=276 e 2N=184. La matrice T ha forma 276×184, rango 184 e colonne ortonormali; K_tan è 184×184.

Le normali sono medie pesate delle normali delle facce incidenti; i frame sono resi destrorsi e codificati da quaternioni unitari. I test verificano ortogonalità dei frame, determinante positivo, doppio ricoprimento e proiezione tangente.

**Limite fisico:** nel codice il quaternione codifica il frame locale. Non è ancora un campo Cosserat/micropolare indipendente con propria energia, inerzia o legge di evoluzione. Per affermarlo occorre introdurre una legge costitutiva specifica.

### 4.4 Frame quaternionici e gruppo binario icosaedrale

Il fatto che un frame sia rappresentato da un elemento di SU(2) non dimostra che sia stata costruita l'azione del gruppo binario icosaedrale 2I. Servono i 120 quaternioni espliciti, con verifiche di chiusura, inversi, identità e proiezione al gruppo icosaedrale rotazionale. Nel materiale recuperato la tabella completa dei 120 elementi non è ancora disponibile. Vanno tenuti separati:
- il doppio ricoprimento universale SU(2)→SO(3);
- il frame quaternionico locale del guscio, implementato;
- la rappresentazione finita di 2I, ancora da recuperare/verificare.

---

## 5. Confronto tra tangente RGS 188D e shell 184D

### 5.1 Il mismatch dimensionale

Il tangente RGS ha 188 coordinate ridotte, la shell calcistica 184. Non esiste una corrispondenza canonica: geometrie, siti, vincoli e operatori energetici sono diversi. Non si può identificare una base con l'altra solo perché entrambe contengono triplette.

### 5.2 Trasferimento geometrico 192→276

Si parte dalle 64 direzioni sorgente n_i=X_i/||X_i|| e dalle 92 direzioni bersaglio m_j=Y_j/||Y_j||. Per ogni nodo bersaglio si selezionano i vicini sorgente e si determinano pesi di norma minima:
\[
\min_w\|w\|_2^2,\quad
\sum_iw_i=1,\quad \sum_iw_in_i=m_j.
\]
Ponendo C=[1; n_i^T] e d=[1;m_j], la soluzione è
\[
w=C^T(CC^T)^+d.
\]
I pesi scalari formano W_s in R^(92×64), poi estesi alle componenti cartesiane:
\[
W=W_s\otimes I_3\in\mathbb R^{276\times192}.
\]
Dopo il trasferimento si proietta ogni vettore sul piano tangente locale della shell.

La mappa riproduce costanti e direzioni radiali per costruzione. Non preserva automaticamente rigidezza, energia, spettro o azione di gruppo: è un'interpolazione geometrica, non un'identificazione fisica dei siti.

### 5.3 Angoli principali

Date due basi ortonormali U,V di sottospazi della stessa dimensione, gli angoli principali derivano dai valori singolari di UᵀV:
\[
\theta_i=\arccos(\sigma_i).
\]
Misurano l'allineamento geometrico dei sottospazi dopo il trasferimento. Non dimostrano equivalenza degli operatori o delle dinamiche.

### 5.4 Esperimento spettrale implementato

Il test end-to-end non usa la vecchia base T2u non verificata. Usa la tripletta geometrica delle rotazioni infinitesime e_a×X_i. La proietta nel tangente RGS, la ortonormalizza, la trasferisce con W, la proietta nel tangente della shell e la confronta con i tre autovettori più bassi di K_tan. Il report registra rango/ortogonalità, diagnostica del trasferimento, gap tra terzo e quarto autovalore, angoli principali e residuo normalizzato della rigidezza.

La lettura corretta è: **esperimento di allineamento geometrico-spettrale tra una tripletta rotazionale definita dalla geometria RGS e il settore a bassa frequenza della shell linearizzata**. Non è un'identificazione T2u, né prova di simmetria protetta, né prova di identità microscopica.

---

## 6. Intertwiners: significato e limiti

Se due modelli hanno azioni di rotazione R_g e S_g, un intertwiner è una matrice non nulla X tale che
\[
S_gX=XR_g
\]
per ogni generatore accoppiato. Per vettorizzazione:
\[
\operatorname{vec}(S_gX-XR_g)
=(I\otimes S_g-R_g^T\otimes I)\operatorname{vec}(X).
\]
Accatastando i generatori si ottiene un problema lineare omogeneo; la SVD individua il nucleo o il vettore singolare di residuo minimo.

Un residuo piccolo significa che le azioni fornite sono quasi intrecciate. Per interpretarlo come equivalenza di rappresentazioni occorre:
1. giustificare l'accoppiamento fisico dei generatori;
2. verificare le relazioni del gruppo su entrambi i lati;
3. verificare i commutatori degli operatori energetici con le azioni;
4. controllare caratteri e proiettori irriducibili;
5. verificare stabilità rispetto a perturbazioni e raffinamento.

Un'intertwiner calcolato con generatori accoppiati arbitrariamente non dimostra una simmetria del materiale.

---

## 7. Il raccordo con l'elasticità incompatibile di Morandotti

Il collegamento matematico non è l'uguaglianza tra una tripletta quaternionica e un difetto cristallino. È la possibilità di costruire una discretizzazione in cui:
- gli spostamenti ammissibili appartengono a un tangente ben definito;
- il gradiente discreto produce una deformazione simmetrica;
- metrica e frame orientati permettono di confrontare quantità tensoriali tra patch;
- l'operatore di incompatibilità agisce sulla deformazione e restituisce una sorgente di Burgers/Frank;
- energia e condizioni di interfaccia derivano da un funzionale coerente.

Il programma è
\[
u_h\xrightarrow{G_h}\nabla_hu_h
\xrightarrow{sym}\epsilon_h
\xrightarrow{Inc_h}\zeta_h.
\]
La chiusura del complesso cinematico d_1,h d_0,h=0 resta distinta dalla legge di incompatibilità elastica:
\[
Inc_h\epsilon_h=\zeta_h.
\]
I quaternioni possono trasportare frame e componenti locali; non sostituiscono Inc_h. Le triplette isolano settori geometrici o rappresentativi; non sostituiscono le sorgenti di Burgers e Frank. Il passaggio a patch curve richiede la derivazione degli operatori superficiali e dei termini di curvatura.

Questo è il punto d'incontro con Morandotti: costruire e verificare una discretizzazione variazionale dell'incompatibilità, non proporre una corrispondenza simbolica tra oggetti di natura diversa.

---

## 8. Tabella di stato

| Oggetto | Stato corretto |
|---|---|
| Jacobiano dei quattro vincoli e rango 4 | Ricostruito e validato numericamente |
| Base tangente 192×188 e proiettore | Verificati a precisione numerica |
| Hessiana vincolata originale e suo spettro | Provenienza/relazione tra matrici da chiudere |
| Tripletta e_a×X_i | Costruzione geometrica; rango tre da audit |
| Tripletti T1u/T2u | Richiedono caratteri, proiettori e generatori coerenti |
| Frame quaternionici locali | Implementati e testati numericamente |
| Doppio ricoprimento SU(2)→SO(3) | Identità matematica standard, usata nel codice |
| Campo quaternionico dinamico/Cosserat | Non implementato |
| Gruppo binario 2I esplicito con 120 elementi | Non ancora recuperato e certificato |
| Tangente shell 276×184 e K_tan | Implementati nel modello linearizzato |
| Trasferimento 192→276 | Interpolazione geometrica; non stiffness-preserving |
| Angoli principali | Misura geometrica, non equivalenza fisica |
| Intertwiner tra azioni | Test candidato; generatori da giustificare |
| Ponte Inc_h epsilon_h=zeta_h | Da costruire e dimostrare |
| Convergenza Mosco/Γ su famiglie curve | Aperta |

---

## 9. Fonti interne e riproducibilità

File del repository:
- data/rgs_188d/A14_jacobian_report.json
- data/rgs_188d/RECOVERED_SOURCE_ARTIFACTS.md
- reports/188d_recovered_geometry_audit_2026-11-09.json
- reports/188d_antitwin_audit.json
- models/football_quaternion_tangent.py
- models/football_quaternion_bridge.py
- docs/FOOTBALL_QUATERNION_TANGENT.md
- docs/RGS_FOOTBALL_QUATERNION_BRIDGE.md
- docs/RGS_FOOTBALL_GEOMETRIC_TRANSFER.md
- scripts/run_rgs_football_triplet_spectral_comparison.py
- docs/RGS_FOOTBALL_TRIPLET_SPECTRAL_COMPARISON.md

Comandi principali:
    python -m pytest -q tests/test_football_quaternion_tangent.py
    python -m pytest -q tests/test_football_quaternion_bridge.py
    python -m pytest -q tests/test_rgs_football_triplet_spectral_comparison.py
    python scripts/run_rgs_football_triplet_spectral_comparison.py

I risultati numerici da allegare al dossier devono provenire da un'esecuzione corrente e riportare il relativo report JSON; non si devono mescolare valori provenienti da run diverse.

---

## 10. Messaggio scientifico per il colloquio

La sequenza logica da illustrare è:

**vincoli geometrici → Jacobiano → sottospazio tangente → forma energetica ridotta → settori modali/triplette → azioni di rotazione → frame quaternionici → trasferimento geometrico alla shell → confronto variazionale con l'incompatibilità elastica.**

Ogni freccia ha un significato matematico distinto e un proprio controllo. La proposta a Morandotti è di stabilire quali passaggi possano essere integrati in una formulazione discreta rigorosa dell'elasticità incompatibile e quali proprietà meritino una dimostrazione di convergenza.

La forza della presentazione sta nel mostrare una catena di costruzioni verificabili, dichiarare i punti aperti e individuare un benchmark nel quale un risultato positivo o negativo sia scientificamente informativo.
